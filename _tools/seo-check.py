#!/usr/bin/env python3
"""
seo-check.py - invariant checker for blog.dugong.live

Run from the repository root:

    python3 _tools/seo-check.py

Exit code 0 when every invariant holds, 1 otherwise. Add --quiet to print
only failures. Lives under _tools/ so Jekyll never publishes it.

Written 2026-10-17. The checks here are the ones the daily blog run has
actually broken in the past, plus the standing field-level audit:

  * 2026-10-16: a dispatch shipped a 201-character meta description.
  * 2026-10-16: four pages gained a dispatch without their dateModified moving.
  * 2026-10-17: a dispatch shipped a 74-character <title>.
  * 2026-10-17: three pages had sitemap lastmod moved but not dateModified.
  * 2026-10-18: every HowTo block was a paraphrase of the visible playbook
    rather than a copy of it, and 6 claimed a step the page does not show.
  * 2026-10-18: the FAQPage and BreadcrumbList nodes had no @id, and no
    article claimed either of them as a part.

Every one of those would have been caught by running this file.

DOCUMENTED EXCEPTIONS (deliberate, not drift) are listed in EXCEPTIONS below.
Add to it only with a reason, and only when the exception is genuinely
intended.
"""
import os, re, sys, json, glob
from html import unescape as html_unescape
import xml.etree.ElementTree as ET
from collections import defaultdict

BASE = "https://blog.dugong.live/"
TITLE_MAX = 60
# Node types that must carry an @id so other nodes can reference them.
GRAPH_NODE_TYPES = (
    "BlogPosting", "Article", "FAQPage", "HowTo", "BreadcrumbList",
    "ItemList", "CollectionPage", "ProfilePage", "Blog", "WebSite",
    "Organization",
)
DESC_MIN, DESC_MAX = 70, 165

EXCEPTIONS = {
    # index.html and 404.html carry hand-written og:/twitter: copy that
    # deliberately differs from their meta description. Both inside the caps.
    "desc_channel_mismatch": {"index.html", "404.html"},
    # The lead essay's URL first appeared 2026-10-14; the essay text itself
    # has not changed since 2026-05-28. Both dates are true and the recent
    # lastmod is the useful crawl hint.
    "lastmod_vs_datemodified": {"the-death-of-the-drag-and-drop-builder.html"},
    # 404.html is noindex by design and is intentionally not linked from
    # anywhere, so it is exempt from the orphan and sitemap checks.
    "noindex_allowed": {"404.html"},
    "orphan_allowed": {"404.html"},
    "sitemap_exempt": {"404.html"},
}

fails = defaultdict(list)
notes = []


def fail(key, detail):
    fails[key].append(detail)


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


PLAYBOOK = re.compile(r'<pre id="playbook"><code>(.*?)</code></pre>', re.S)


def folded(value):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", value.lower())).strip()


def visible_text(html):
    """The page as a reader sees it: scripts and styles gone, tags stripped,
    whitespace collapsed, punctuation and case folded away. Markup that claims
    something the page does not say is invisible to a reader and contradicts
    the page for an answer engine, so several checks below compare against
    this rather than against the raw file."""
    body = re.sub(r"<script.*?</script>", " ", html, flags=re.S)
    body = re.sub(r"<style.*?</style>", " ", body, flags=re.S)
    body = re.sub(r"<[^>]+>", " ", body)
    return folded(html_unescape(body))


def playbook_steps(html):
    """The numbered steps of the visible <pre id="playbook"> block, in order.
    Returns None when the page has no playbook."""
    match = PLAYBOOK.search(html)
    if not match:
        return None
    raw = html_unescape(re.sub(r"<[^>]+>", "", match.group(1)))
    if "# steps" not in raw:
        return None
    steps = []
    for line in raw.split("# steps", 1)[1].split("\n"):
        numbered = re.match(r"\s*(\d+)\.\s+(.*)$", line)
        if numbered:
            steps.append(numbered.group(2).strip())
        elif steps and line.strip():
            steps[-1] += " " + line.strip()
    return [re.sub(r"\s+", " ", s).strip() for s in steps if s.strip()]



# ---------------------------------------------------------------- discovery
def classify():
    """Split *.html into rendered pages and redirect stubs."""
    rendered, stubs = [], []
    for name in sorted(glob.glob("*.html")):
        text = read(name)
        if 'http-equiv="refresh"' in text.lower() or len(text) < 3000:
            stubs.append(name)
        else:
            rendered.append(name)
    return rendered, stubs


def jsonld(text, name):
    out = []
    for block in re.findall(
        r'<script type="application/ld\+json">(.*?)</script>', text, re.S
    ):
        try:
            out.append(json.loads(block))
        except Exception as exc:  # noqa: BLE001
            fail("jsonld_parse", f"{name}: {exc}")
    return out


def nodes(docs):
    for doc in docs:
        for node in doc.get("@graph", [doc]) if isinstance(doc, dict) else doc:
            if isinstance(node, dict):
                yield node


def expected_url(name):
    return BASE + ("" if name == "index.html" else name)


# ------------------------------------------------------------------- checks
def main():
    quiet = "--quiet" in sys.argv
    if not os.path.exists("sitemap.xml"):
        print("seo-check: run me from the repository root", file=sys.stderr)
        return 2

    rendered, stubs = classify()
    docs = {n: jsonld(read(n), n) for n in rendered}
    titles, descs = defaultdict(list), defaultdict(list)
    date_modified = {}
    posts = []

    for name in rendered:
        text = read(name)
        page_nodes = list(nodes(docs[name]))

        if len(re.findall(r"<h1\b", text)) != 1:
            fail("h1_count", name)

        canon = re.search(r'<link rel="canonical" href="([^"]+)"', text)
        ogurl = re.search(r'<meta property="og:url" content="([^"]+)"', text)
        want = expected_url(name)
        if not canon or canon.group(1) != want:
            fail("canonical", f"{name}: {canon.group(1) if canon else 'missing'}")
        if not ogurl or ogurl.group(1) != want:
            fail("og_url", f"{name}: {ogurl.group(1) if ogurl else 'missing'}")

        title = re.search(r"<title>(.*?)</title>", text, re.S)
        if not title:
            fail("title_missing", name)
        else:
            value = title.group(1).strip()
            titles[value].append(name)
            if len(value) > TITLE_MAX:
                fail("title_too_long", f"{name}: {len(value)} chars > {TITLE_MAX}")

        desc = re.search(r'<meta name="description" content="([^"]*)"', text)
        if not desc:
            fail("desc_missing", name)
        else:
            value = desc.group(1)
            descs[value].append(name)
            if not DESC_MIN <= len(value) <= DESC_MAX:
                fail(
                    "desc_length",
                    f"{name}: {len(value)} chars, want {DESC_MIN}-{DESC_MAX}",
                )
            if name not in EXCEPTIONS["desc_channel_mismatch"]:
                for prop, pattern in (
                    ("og:description", r'<meta property="og:description" content="([^"]*)"'),
                    ("twitter:description", r'<meta name="twitter:description" content="([^"]*)"'),
                ):
                    other = re.search(pattern, text)
                    if other and other.group(1) != value:
                        fail("desc_channel_mismatch", f"{name}: {prop} differs")

        ids = re.findall(r'\sid="([^"]+)"', text)
        for dup in {i for i in ids if ids.count(i) > 1}:
            fail("duplicate_id", f"{name}: #{dup}")

        if re.search(r'name="robots" content="[^"]*noindex', text):
            if name not in EXCEPTIONS["noindex_allowed"]:
                fail("unexpected_noindex", name)

        if "�" in text:
            fail("mojibake", name)
        for dash in ("—", "–"):
            if dash in text:
                fail("em_or_en_dash", name)
                break

        if text.count("<style") != text.count("</style>"):
            fail("style_tag_balance", name)

        # Any page that declares a dateModified must agree with its sitemap
        # lastmod, not only the dispatches. The 2026-10-17 drift was on a
        # ProfilePage and two CollectionPages, which an Article-only sweep
        # would have walked straight past.
        for node in page_nodes:
            if node.get("dateModified") and name not in date_modified:
                date_modified[name] = node["dateModified"][:10]

        # structured data integrity
        for node in page_nodes:
            kind = node.get("@type")
            if kind in ("BlogPosting", "Article"):
                posts.append(name)
                for required in (
                    "headline", "description", "datePublished", "dateModified",
                    "author", "publisher", "image", "inLanguage",
                    "isAccessibleForFree", "about",
                ):
                    if not node.get(required):
                        fail("blogposting_field", f"{name}: missing {required}")
                about = node.get("about") or []
                for thing in about if isinstance(about, list) else [about]:
                    same = thing.get("sameAs")
                    label = thing.get("name", "?")
                    if isinstance(same, str):
                        fail(
                            "entity_no_wikidata",
                            f"{name}: '{label}' has only {same}",
                        )
                    elif isinstance(same, list):
                        if not any("en.wikipedia.org/wiki/" in u for u in same):
                            fail("entity_no_wikipedia", f"{name}: '{label}'")
                        if not any("wikidata.org/wiki/Q" in u for u in same):
                            fail("entity_no_wikidata", f"{name}: '{label}'")
                    else:
                        fail("entity_no_sameas", f"{name}: '{label}'")
            elif kind == "FAQPage":
                entities = node.get("mainEntity") or []
                if not entities:
                    fail("faq_empty", name)
                for question in entities:
                    if question.get("@type") != "Question" or not question.get("name"):
                        fail("faq_question", name)
                    answer = question.get("acceptedAnswer") or {}
                    if answer.get("@type") != "Answer" or not answer.get("text"):
                        fail("faq_answer", f"{name}: {question.get('name', '?')[:48]}")
            elif kind == "HowTo":
                steps = node.get("step") or []
                if not steps:
                    fail("howto_no_steps", name)
                for step in steps:
                    if step.get("@type") not in ("HowToStep", "HowToSection"):
                        fail("howto_step_type", name)
                    if not step.get("name"):
                        fail("howto_step_name", name)
                # The markup must describe the procedure the reader is shown.
                # On 2026-10-18 all 82 HowTo blocks were paraphrases of the
                # visible playbook: 474 of 572 step texts appeared nowhere on
                # the page and 6 pages claimed a seventh step that did not
                # exist. See the three checks below.
                visible = playbook_steps(text)
                if visible is None:
                    fail("howto_without_playbook", name)
                else:
                    if len(steps) != len(visible):
                        fail(
                            "howto_step_count",
                            f"{name}: markup {len(steps)} steps, page shows {len(visible)}",
                        )
                    page_text = visible_text(text)
                    for step in steps:
                        for field in ("text", "name"):
                            value = step.get(field) or ""
                            if value and folded(value) not in page_text:
                                fail(
                                    f"howto_step_{field}_not_visible",
                                    f"{name}: {value[:56]}",
                                )
            elif kind in ("BreadcrumbList", "ItemList"):
                items = node.get("itemListElement") or []
                positions = [i.get("position") for i in items]
                if positions != list(range(1, len(items) + 1)):
                    fail(
                        "itemlist_positions",
                        f"{name} ({kind}): {len(items)} items, positions not 1..n",
                    )

            # Every node in a @graph needs an @id, or nothing can point at it.
            # Until 2026-10-18 the FAQPage and BreadcrumbList nodes had none,
            # so the blocks sat in the same array as the article asserting no
            # relationship to it.
            if kind in GRAPH_NODE_TYPES and "@id" not in node:
                fail("node_without_id", f"{name}: {kind}")

        # An article, its how-to and its FAQ sitting in one @graph array
        # asserts no relationship between them; adjacency is not an edge.
        # The article has to say which blocks are part of it.
        article = next(
            (n for n in page_nodes if n.get("@type") in ("BlogPosting", "Article")),
            None,
        )
        if article is not None:
            want = [
                n["@id"]
                for n in page_nodes
                if n.get("@type") in ("HowTo", "FAQPage") and "@id" in n
            ]
            have = [
                p.get("@id")
                for p in (article.get("hasPart") or [])
                if isinstance(p, dict)
            ]
            for part in want:
                if part not in have:
                    fail("article_haspart", f"{name}: does not claim {part.split('#')[-1]}")

    posts = sorted(set(posts))

    for value, owners in titles.items():
        if len(owners) > 1:
            fail("duplicate_title", f"{owners}: {value[:60]}")
    for value, owners in descs.items():
        if len(owners) > 1:
            fail("duplicate_description", f"{owners}: {value[:60]}")

    # ------------------------------------------------------------- linkage
    on_disk = set(os.listdir("."))
    if os.path.isdir("md"):
        on_disk |= {"md/" + f for f in os.listdir("md")}
    page_ids = {n: set(re.findall(r'\sid="([^"]+)"', read(n))) for n in rendered}

    for name in rendered + stubs:
        text = read(name)
        local_ids = set(re.findall(r'\sid="([^"]+)"', text))
        for href in re.findall(r'href="([^"]+)"', text):
            if href.startswith(("http", "mailto:", "tel:", "//", "data:")):
                continue
            if href.startswith("#"):
                if href[1:] and href[1:] not in local_ids:
                    fail("broken_anchor", f"{name}: {href}")
                continue
            target = href.split("#")[0].split("?")[0].lstrip("/")
            if not target:
                continue
            if target not in on_disk and not os.path.exists(target):
                fail("broken_link", f"{name}: {href}")
                continue
            frag = href.split("#")[1] if "#" in href else ""
            if frag and target in page_ids and frag not in page_ids[target]:
                fail("broken_cross_anchor", f"{name}: {href}")

    inbound = defaultdict(int)
    for name in rendered + stubs:
        for href in set(re.findall(r'href="/?([a-z0-9\-]+\.html)[\"#]', read(name))):
            if href != name:
                inbound[href] += 1
    for name in rendered:
        if inbound[name] == 0 and name not in EXCEPTIONS["orphan_allowed"]:
            fail("orphan_page", name)

    # ------------------------------------------------------------- sitemap
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    root = ET.parse("sitemap.xml").getroot()
    locs, lastmod = [], {}
    for entry in root.findall("s:url", ns):
        loc = entry.find("s:loc", ns).text
        locs.append(loc)
        node = entry.find("s:lastmod", ns)
        if node is not None:
            lastmod[loc] = node.text
    if len(locs) != len(set(locs)):
        fail("sitemap_duplicate", f"{len(locs) - len(set(locs))} duplicate loc(s)")
    listed = set()
    for loc in locs:
        rel = loc.replace(BASE, "") or "index.html"
        listed.add(rel)
        if rel not in on_disk:
            fail("sitemap_ghost", loc)
        if rel in stubs:
            fail("sitemap_lists_stub", loc)
    for name in rendered:
        if name not in listed and name not in EXCEPTIONS["sitemap_exempt"]:
            fail("sitemap_missing", name)
    for name, declared in date_modified.items():
        if name in EXCEPTIONS["lastmod_vs_datemodified"]:
            continue
        hint = lastmod.get(expected_url(name))
        if hint and hint[:10] != declared:
            fail(
                "lastmod_vs_datemodified",
                f"{name}: sitemap says {hint}, page says {declared}",
            )
    for name in rendered:
        if name in EXCEPTIONS["sitemap_exempt"]:
            continue
        if expected_url(name) in lastmod and name not in date_modified:
            notes.append(f"{name} is in the sitemap with a lastmod but declares "
                         f"no dateModified of its own")

    # ---------------------------------------------------------------- feed
    feed = ET.parse("feed.xml").getroot()
    items = feed.findall(".//item")
    if len(items) != len(posts):
        fail("feed_count", f"feed has {len(items)} items, site has {len(posts)} posts")
    for item in items:
        link = item.find("link")
        rel = (link.text or "").replace(BASE, "") if link is not None else ""
        if rel not in on_disk:
            fail("feed_ghost", link.text if link is not None else "<no link>")

    # ------------------------------------------------- llms.txt and /md/
    llms = read("llms.txt") if os.path.exists("llms.txt") else ""
    llms_full = read("llms-full.txt") if os.path.exists("llms-full.txt") else ""
    for name in posts:
        md = "md/" + name.replace(".html", ".md")
        if name not in llms:
            fail("llms_missing", name)
        if name not in llms_full:
            fail("llms_full_missing", name)
        if not os.path.exists(md):
            fail("markdown_twin_missing", md)
        if 'type="text/markdown"' not in read(name):
            fail("markdown_alternate_missing", name)

    # ------------------------------------------------------------- robots
    robots = read("robots.txt") if os.path.exists("robots.txt") else ""
    if not re.search(r"(?im)^sitemap:\s*\S+", robots):
        fail("robots_no_sitemap", "robots.txt declares no Sitemap:")
    for prefix in ("/QA-report-", "/blog-run-", "/SEO-GEO-report-"):
        groups = re.split(r"(?im)^user-agent:", robots)[1:]
        for group in groups:
            agent = group.splitlines()[0].strip()
            if f"Disallow: {prefix}" not in group:
                fail("robots_report_exposed", f"{agent} may crawl {prefix}*")

    # --------------------------------------------------------------- report
    print(f"seo-check: {len(rendered)} rendered pages, {len(stubs)} redirect stubs, "
          f"{len(posts)} dispatches, {len(locs)} sitemap URLs, {len(items)} feed items")
    for note in notes:
        print("  note:", note)
    if not fails:
        print("seo-check: PASS - every invariant holds")
        return 0
    total = sum(len(v) for v in fails.values())
    print(f"seo-check: FAIL - {total} problem(s) in {len(fails)} category(ies)")
    for key in sorted(fails):
        entries = fails[key]
        print(f"\n  {key} ({len(entries)}):")
        for entry in entries if not quiet else entries[:10]:
            print(f"    - {entry}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
