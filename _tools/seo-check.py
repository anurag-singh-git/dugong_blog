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
from datetime import datetime

BASE = "https://blog.dugong.live/"
TITLE_MAX = 60
# Node types that must carry an @id so other nodes can reference them.
GRAPH_NODE_TYPES = (
    "BlogPosting", "Article", "FAQPage", "HowTo", "BreadcrumbList",
    "ItemList", "CollectionPage", "ProfilePage", "Blog", "WebSite",
    "Organization", "WebPage",
)
DESC_MIN, DESC_MAX = 70, 165

EXCEPTIONS = {
    # index.html and 404.html carry hand-written og:/twitter: copy that
    # deliberately differs from their meta description. Both inside the caps.
    "desc_channel_mismatch": {"index.html", "404.html"},
    # Lapsed 2026-10-31. The lead essay's URL first appeared 2026-10-14 while
    # the essay text had not changed since 2026-05-28, so its lastmod and its
    # dateModified disagreed on purpose and the exception held the difference.
    # On 2026-10-31 the essay gained a short answer, which is new prose the
    # reader has not seen, so both dates moved to that day together and the
    # exception has nothing left to excuse. The key is kept, empty, because
    # the same situation will recur the next time a page's URL is republished
    # without its text changing.
    "lastmod_vs_datemodified": set(),
    # 404.html is noindex by design and is intentionally not linked from
    # anywhere, so it is exempt from the orphan and sitemap checks.
    "noindex_allowed": {"404.html"},
    "orphan_allowed": {"404.html"},
    "sitemap_exempt": {"404.html"},
    # Entities whose concept has a Wikidata item but no en.wikipedia article.
    # Pointing these at the nearest Wikipedia page would be a disambiguation
    # page or a near-miss concept, so they carry Wikidata alone. Verified
    # 2026-10-19 against the Wikipedia and Wikidata APIs in both directions.
    #   Click and collect -> Q15794580, "shopping in which merchandise is
    #   purchased online and picked up at a local store". No sitelinks.
    #   en.wikipedia.org/wiki/Click_and_collect is a disambiguation page
    #   (Q101423394) and was the target until this pass.
    "wikidata_only_entity": {"Click and collect"},
    # Bare structural wrappers that group children and are never themselves
    # painted, plus one label that inherits its parent's type on purpose.
    # Verified 2026-10-31: each renders identically with and without a rule.
    "unstyled_class": {"faq-list", "signup-left", "hero-date", "qa-post"},
    # index.html declares a WebSite and a Blog rather than a page node, which
    # is correct: the home page of a blog is the Blog. 404.html carries no
    # JSON-LD at all and is noindex by design, so there is nothing for a page
    # node to anchor. Every other rendered page must say what it is.
    "page_node_exempt": {"index.html", "404.html"},

    # .pb-node.muted .pb-icon is a single emoji in a bordered box, sitting
    # beside a text label that says the same thing, so dimming it moves no
    # text contrast. Every other fractional opacity on a container is a
    # finding; see fractional_opacity_on_container.
    # .pb-node.muted .pb-icon is a single emoji in a bordered box, sitting
    # beside a text label that says the same thing, so dimming it moves no
    # text contrast.
    # .qa-list a and .qa-guide-link a on the question index dim near-black ink
    # (#11110e) on #f6f6f1, which measures 10.49 and 7.34 against the 4.5 AA
    # needs even after the opacity is folded in. Measured in Chromium with the
    # real webfonts, 2026-11-18. These are intended and are listed rather than
    # the check being softened; anything else is a finding.
    "fractional_opacity_ok": {
        ".pb-node.muted .pb-icon",
        ".qa-list a",
        ".qa-guide-link a",
    },

    # Lapsed 2026-11-19. index.html used to wrap its whole page, header and
    # footer included, in one <div class="view" role="main">, so its
    # hand-written sections were inside a landmark already and axe's region
    # rule passed them unnamed. That wrapper was the defect they were hiding
    # behind; on 2026-11-19 role="main" moved onto a <main> that holds only
    # the content sections and all nine sections were named from the text
    # already on screen, so there is nothing left to excuse. The key is kept,
    # empty, because the next hand-written page will want the same decision.
    "section_name_exempt": set(),

    # Selectors allowed to truncate with an ellipsis; see
    # text_truncated_by_ellipsis. Empty on 2026-11-19: the site's one such
    # rule was the defect that added the check. A selector goes in here only
    # with the other way a reader can reach the text written beside it.
    "ellipsis_ok": set(),
}

# Claimed words per minute. The 89 dispatches run 172 to 312; the band is
# widened a little at each end so honest editorial variation does not fire.
# Smallest -webkit-line-clamp that truncates no card dek on the site, plain
# or under the WCAG 1.4.12 text-spacing override. Measured 2026-11-17 at 12
# and raised to 15 on 2026-11-18: the 11-17 measurement reported 11 lines as
# the most any dek needs under the override, and re-measuring all 5,597 deks
# at 320, 360, 375, 414, 768, 1024 and 1280px found aanya-rao.html's one card
# dek needing 14 lines at 320px under the override, so the clamp of 12 was
# still cutting it. 11 is the most needed plain, 14 the most under the
# override, and 15 is one line of headroom above both. It costs no height:
# nothing on the site reaches 12 lines today.
CLAMP_MIN = 15

WPM_MIN = 150
WPM_MAX = 320

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

def heading_slug(inner_html):
    """The id a section heading is entitled to: its own visible words under the
    `h-` convention the question index has used since it was written.

    Two things are deliberately dropped before slugging, because an anchor is a
    promise that a URL keeps working and this site's numbers do not keep still:

      * a rendered count, whether it trails the heading as `&middot; 86
        QUESTIONS` or leads it as `18 DISPATCHES IN THIS GUIDE`. Every one of
        those counts is recomputed on publication, and six of them moved in the
        week before this check was written, so a count in an anchor is a dead
        link waiting for the next dispatch.
      * a leading list ordinal, `1. `, `2. `, so a numbered section is addressed
        by what it says rather than by where it currently sits in the list.

    A digit that is part of what the heading means is kept, which is why
    `h-the-14-0-8-gap` and `h-the-27-billion-that-never-gets-spent` survive.
    Apostrophes are dropped rather than hyphenated, so "doesn't hold" gives
    `h-doesnt-hold` and not `h-doesn-t-hold`."""
    count_noun = r"(?:dispatch|dispatches|question|questions)"
    text = html_unescape(re.sub(r"<[^>]+>", "", inner_html))
    text = text.replace("\u25c6", " ").lower()
    text = text.replace("'", "").replace("\u2019", "")
    text = text.strip(" \t\n\u00b7")
    text = re.sub(r"\u00b7\s*\d+\s+" + count_noun + r"\s*$", "", text)
    text = re.sub(r"^\s*\d+[.)]\s+", "", text)
    text = re.sub(r"^\s*\d+\s+(?=" + count_noun + r"\b)", "", text)
    return "h-" + re.sub(r"[^a-z0-9]+", "-", text).strip("-")


# h2 classes that are not section headings: the FAQ questions are addressed by
# their .faq-item wrapper's #faq-N, and the rest are component titles in the
# page furniture rather than places in an argument.
NON_SECTION_H2 = {"faq-q", "cta-title", "featured-title", "signup-title", "author-name"}


# A `## ` heading in a machine rendition that is not an <h2> carrying an id of
# its own. Both of these sections are addressable; the id sits on the element
# that labels the section rather than on the heading, so the heading's own text
# cannot resolve it and the mapping has to be written down. `#faq-heading` is
# the anchor the FAQ section's `aria-labelledby` has always pointed at and the
# `url` the FAQPage node has carried since 2026-11-18.
SECTION_BY_LABEL = {
    "Common questions": "faq-heading",
    "Read next": "related-heading",
}


def section_anchor_pairs(page_html, md_text):
    """The (heading, anchor) pairs a dispatch's two machine renditions are
    entitled to: one for every `## ` heading the md writes, in the order it
    writes them, each resolved against an id that is already in the page's
    markup.

    Resolution is by the heading's visible text first, because 765 of the 876
    headings are an <h2> whose text is identical in both renditions, and only
    then by SECTION_BY_LABEL and by the slug convention. An anchor is returned
    as None when nothing on the page resolves it, so the caller can say which
    heading has no address rather than inventing one.

    This lives here, beside heading_slug, so the writer imports it instead of
    restating it. Two implementations of one convention is how the two short
    answer writers came to disagree."""
    ids = set(re.findall(r'\sid="([^"]+)"', page_html))
    by_text = {}
    for attr, inner in re.findall(r"<h2([^>]*)>(.*?)</h2>", page_html, re.S):
        got = re.search(r'id="([^"]+)"', attr)
        if got:
            plain = html_unescape(re.sub(r"<[^>]+>", "", inner))
            by_text.setdefault(re.sub(r"\s+", " ", plain).strip(), got.group(1))
    pairs = []
    for heading in re.findall(r"^## (.+)$", md_text, re.M):
        heading = heading.strip()
        anchor = by_text.get(heading) or SECTION_BY_LABEL.get(heading)
        if anchor is None:
            slug = heading_slug(heading)
            anchor = slug if slug in ids else None
        pairs.append((heading, anchor))
    return pairs, ids


def heading_regions(text, name):
    """Where section headings are expected to be addressable. On a dispatch
    that is the <article>; on a topic guide or author archive the headings sit
    outside one, so the whole page counts. 404.html is noindex and unlinked by
    design, so it is left alone for the same reason it is exempt elsewhere."""
    if name in EXCEPTIONS["noindex_allowed"]:
        return []
    start = re.search(r"<article\b", text)
    if start:
        end = text.find("</article>", start.start())
        return [text[start.start(): end if end != -1 else len(text)]]
    if re.search(r'"@type":\s*"(CollectionPage|ProfilePage)"', text):
        return [text]
    return []



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


def element_contents(html, class_name):
    """Yield the inner HTML of every element carrying class_name.

    Walks tags so a container holding nested elements of the same name,
    such as the <p> children of .article-body, is measured whole rather
    than cut off at the first closing tag.
    """
    opener = re.compile(
        r'<([a-z]+)[^>]*\bclass="[^"]*\b' + re.escape(class_name) + r'\b[^"]*"[^>]*>'
    )
    for match in opener.finditer(html):
        tag = match.group(1)
        depth, pos = 1, match.end()
        token = re.compile(r"<(/?)" + tag + r"\b[^>]*>")
        while depth and pos < len(html):
            nxt = token.search(html, pos)
            if not nxt:
                break
            depth += -1 if nxt.group(1) else 1
            pos = nxt.end()
            if depth == 0:
                yield html[match.end():nxt.start()]
                break


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


def date_days(value):
    """Days since 2026-01-01 for a YYYY-MM-DD string, for comparing recency
    without pulling in a clock. Only differences are ever used."""
    year, month, day = (int(part) for part in value.split("-")[:3])
    return (year - 2026) * 372 + month * 31 + day


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
    stub_target = {}
    for name in stubs:
        hit = re.search(r'url=https://blog\.dugong\.live/([^"\']+)', read(name))
        if hit:
            stub_target[name] = hit.group(1)
    docs = {n: jsonld(read(n), n) for n in rendered}
    titles, descs = defaultdict(list), defaultdict(list)
    date_modified = {}
    posts = []

    for name in rendered:
        text = read(name)
        page_nodes = list(nodes(docs[name]))

        if len(re.findall(r"<h1\b", text)) != 1:
            fail("h1_count", name)

        # A -webkit-line-clamp cuts the dek at a fixed number of lines and drops
        # the rest. On 2026-11-17 the clamp was 5 (8 on tall and wide cards) and
        # 19 deks across 11 pages needed 6 to 8 lines, so each lost the closing
        # clause the card exists to sell, and the WCAG 1.4.12 text-spacing
        # override cut 281 of them. Measured in Chromium over all 5,597 deks on
        # the site: 8 lines is the most any dek needs rendered plain and 11 the
        # most under the override, and the clamp costs 314px of height across
        # all 109 pages at 12. Anything below 12 can truncate, so anything below
        # 12 is a failure rather than a smaller clamp.
        for value in re.findall(r"-webkit-line-clamp:\s*(\d+)", text):
            if int(value) < CLAMP_MIN:
                fail("card_dek_clamp_too_low", f"{name}: -webkit-line-clamp: {value}")

        # The base .article-body pre rule carried overflow-x: auto and the
        # initial white-space: pre. On 2026-11-17 six playbooks ran 588px wide
        # against a 580px content box, which made each one a horizontally
        # scrollable region that no keyboard user can reach (WCAG 2.1.1) and
        # whose last 8px of text only a mouse drag revealed. The <=820px rule
        # has wrapped these blocks since they were written; the base rule has to
        # wrap them too, or the next long line reopens the same hole in silence.
        base_pre = re.search(r"\.article-body pre \{([^}]*)\}", text)
        if base_pre and "white-space: pre-wrap" not in base_pre.group(1):
            fail("pre_does_not_wrap", name)

        # .article-title carried no overflow-wrap, so a long word in a headline
        # had nothing to break on. On 2026-11-18 "personalization" plus the
        # WCAG 1.4.12 letter-spacing override rendered 330px wide in a 320px
        # viewport and pushed the whole page 10px sideways. The site already
        # writes overflow-wrap 588 times elsewhere; the headline rule is the
        # one place it was missing, and the defect is one long headline away
        # at any time. Same shape as pre_does_not_wrap added 2026-11-17.
        base_title = re.search(r"\.article-title \{([^}]*)\}", text)
        if base_title and "overflow-wrap" not in base_title.group(1):
            fail("article_title_does_not_wrap", name)

        # Exactly one main landmark per rendered page. Added 2026-11-18:
        # 404.html carried no landmark of any kind, no header, no nav, no main
        # and no footer, while the other 109 pages carry all four. That is the
        # third time 404.html has shipped without something every other page
        # has: :focus-visible on 11-02 and prefers-reduced-motion on 11-04.
        n_main = len(re.findall(r'<main\b|role="main"', text))
        n_main -= len(re.findall(r'<main\b[^>]*role="main"', text))
        if n_main != 1:
            fail("main_landmark_count", f"{name}: {n_main}")

        # No banner and no contentinfo inside the main landmark. Added
        # 2026-11-19: index.html wrapped its whole document, header and
        # footer included, in <div class="view" role="main">, so main on the
        # most-crawled page of the site contained the entire page and carried
        # no information, and the nav and the footer were announced as main
        # content. axe reported it as landmark-banner-is-top-level and
        # landmark-contentinfo-is-top-level, the only two automated a11y
        # violations left anywhere on the site, and it had stood since at
        # least 11-18. The landmark is now a <main> holding only the content
        # sections. Page-wise rather than site-wise for the same reason
        # main_landmark_count is: the page that got this wrong is the one
        # page nothing else writes.
        _main = re.search(r'<main\b[^>]*>|<[a-z]+[^>]*role="main"[^>]*>', text)
        if _main:
            _tag = re.match(r"<([a-z]+)", _main.group(0)).group(1)
            _depth, _end = 0, None
            for _m in re.finditer(r"<(/?)" + _tag + r"\b[^>]*>", text[_main.start():]):
                _depth += -1 if _m.group(1) else 1
                if _depth == 0:
                    _end = _main.start() + _m.start()
                    break
            _inside = text[_main.end():_end] if _end else text[_main.end():]
            for _land, _why in (("header", "banner"), ("footer", "contentinfo")):
                if re.search(r"<" + _land + r"\b", _inside):
                    fail("landmark_inside_main", f"{name}: <{_land}> ({_why})")

        # Truncation that hides text the reader cannot get back. Added
        # 2026-11-19: .pb-node-sub carried white-space: nowrap with
        # overflow: hidden and text-overflow: ellipsis, which cut 112px of
        # "type, vendor, weight, tags, title pattern" at 320px plain and
        # 181px of it at 1280 under the WCAG 1.4.12 text-spacing override, on
        # a line that renders in full at 1280 without the override. Content
        # the reader loses by setting their own spacing is exactly what
        # 1.4.12 forbids, and an ellipsis is an affordance only where there
        # is some other way to read the text. There was none here. Same shape
        # as pre_does_not_wrap on 11-17 and article_title_does_not_wrap on
        # 11-18, and the same remedy: let it wrap.
        for _sel, _body in re.findall(
                r"([^{}\n]+)\{([^{}]*text-overflow:\s*ellipsis[^{}]*)\}", text):
            _sel = _sel.strip()
            if _sel in EXCEPTIONS["ellipsis_ok"]:
                continue
            fail("text_truncated_by_ellipsis", f"{name}: {_sel}")

        # A fractional opacity on a container scales the alpha of every text
        # run inside it, so it silently moves that text's contrast ratio.
        # Added 2026-11-18: .pb-node.muted { opacity: 0.72 } put two text runs
        # in the homepage's DISPATCH OF THE WEEK card at 2.78 and 3.02 against
        # the 4.5 AA needs, and no opacity below 0.98 would have kept them
        # above it, so dimming by opacity was the wrong tool rather than the
        # wrong value. Muting is expressed with background and border instead.
        # Rules inside @keyframes are exempt: an animation on a decorative
        # element is not a standing contrast claim.
        _no_frames = re.sub(r"@keyframes[^{]*\{(?:[^{}]|\{[^{}]*\})*\}", "", text)
        for _sel, _body in re.findall(r"([^{}\n]+)\{([^{}]*opacity:\s*0?\.\d+[^{}]*)\}",
                                      _no_frames):
            _sel = _sel.strip()
            if _sel in EXCEPTIONS["fractional_opacity_ok"]:
                continue
            # A ::before or ::after whose content is the empty string renders
            # no text, so its opacity cannot move any contrast ratio. This is
            # scoping the check to its subject, not relaxing it: a pseudo
            # element with real content in it is still read.
            if re.search(r"::(?:before|after)$", _sel) and re.search(
                    r'content:\s*(?:""|\'\')\s*;', _body):
                continue
            fail("fractional_opacity_on_container",
                 f"{name}: {_sel} {{{_body.strip()}}}")

        # Every aria-labelledby resolves on its own page. Added 2026-11-18
        # after the pass that added the names below first wrote
        # aria-labelledby="related-heading" onto ten pages whose section-head
        # already carried its own h2 id, leaving ten dangling references, which
        # is worse for a screen reader than the unnamed section it replaced.
        _ids = set(re.findall(r'\bid="([^"]+)"', text))
        for _ref in re.findall(r'aria-labelledby="([^"]+)"', text):
            for _tok in _ref.split():
                if _tok not in _ids:
                    fail("aria_labelledby_unresolved", f"{name}: {_tok}")

        # Every <section> outside an <article> carries an accessible name, so
        # it is a region a screen reader can reach and name. Added 2026-11-18:
        # <section class="related"> on 107 pages, <section class="topics"> on
        # the 8 guides and <section class="cta-band"> on 35 pages had none,
        # while <section class="faq"> directly above the first of them has
        # carried aria-labelledby since it was written. 536 nodes of content
        # sat in no region at all. The node exists, the edge does not, the same
        # shape as the FAQPage before 10-18 and the 660 ListItem entries
        # before 11-04.
        if name not in EXCEPTIONS["section_name_exempt"]:
            _depth = 0
            for _m in re.finditer(r"<(/?)(article|section)\b([^>]*)>", text):
                _close, _tag, _attrs = _m.group(1), _m.group(2), _m.group(3)
                if _tag == "article":
                    _depth += -1 if _close else 1
                    continue
                if _close or _depth > 0:
                    continue
                if "aria-label" not in _attrs:
                    _cls = re.search(r'class="([^"]*)"', _attrs)
                    fail("section_without_accessible_name",
                         f"{name}: <section class=\"{_cls.group(1) if _cls else ''}\">")

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

        # Every section heading a reader can see is a place an answer engine, a
        # search result jump link or another dispatch may want to point at, and
        # a heading with no id cannot be pointed at. The slug is the heading's
        # own words under the `h-` convention the question index has used since
        # it was written, so the anchor stays derivable from the visible text
        # instead of being a number that means nothing. A `-2` suffix is
        # allowed because two sections on one page may share a headline.
        for region in heading_regions(text, name):
            for attrs, inner in re.findall(r"<h2([^>]*)>(.*?)</h2>", region, re.S):
                klass = re.search(r'class="([^"]*)"', attrs)
                if klass and set(klass.group(1).split()) & NON_SECTION_H2:
                    continue
                got = re.search(r'id="([^"]+)"', attrs)
                want = heading_slug(inner)
                label = re.sub(r"<[^>]+>", "", inner).strip()[:52]
                if not got:
                    fail("heading_without_id", f"{name}: '{label}'")
                elif got.group(1) != want and not re.fullmatch(
                    re.escape(want) + r"-\d+", got.group(1)
                ):
                    fail(
                        "heading_id_not_slug",
                        f"{name}: '{label}' carries #{got.group(1)}, want #{want}",
                    )

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

        # A link the reader cannot see is a link the reader cannot click.
        # .article-dek had no anchor rule, so 15 editorial links across 11
        # pages rendered in the dek's own colour with no underline.
        style = re.search(r"<style>(.*?)</style>", text, re.S)
        css = style.group(1) if style else ""
        for container in ("article-dek", "article-body", "card-dek"):
            linked = sum(
                len(re.findall(r"<a ", chunk))
                for chunk in element_contents(text, container)
            )
            if linked and f".{container} a" not in css:
                fail(
                    "unstyled_link_container",
                    f"{name}: {linked} link(s) in .{container} with no "
                    f"'.{container} a' rule",
                )

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
                        wiki_only = label in EXCEPTIONS["wikidata_only_entity"]
                        has_wiki = any(
                            "en.wikipedia.org/wiki/" in u for u in same
                        )
                        if not has_wiki and not wiki_only:
                            fail("entity_no_wikipedia", f"{name}: '{label}'")
                        if has_wiki and wiki_only:
                            fail(
                                "entity_wikipedia_unexpected",
                                f"{name}: '{label}' is documented as "
                                "Wikidata-only but carries a Wikipedia URL",
                            )
                        if not any("wikidata.org/wiki/Q" in u for u in same):
                            fail("entity_no_wikidata", f"{name}: '{label}'")
                    else:
                        fail("entity_no_sameas", f"{name}: '{label}'")
                authors = node.get("author") or []
                for person in authors if isinstance(authors, list) else [authors]:
                    if not isinstance(person, dict):
                        continue
                    who = person.get("name", "?")
                    if not person.get("url"):
                        fail("author_without_url", f"{name}: '{who}'")
                    if not person.get("@id"):
                        fail("author_without_id", f"{name}: '{who}'")
            elif kind == "CollectionPage":
                about = node.get("about") or []
                about = about if isinstance(about, list) else [about]
                if not any(
                    isinstance(t, dict) and t.get("sameAs") for t in about
                ):
                    fail("collection_about_ungrounded", name)
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

    # llms.txt carries three parallel lists of every dispatch: "Full index",
    # "Articles" and "Markdown versions". A dispatch added to one and not the
    # others is invisible to a reader of that list. On 2026-10-18 the newest
    # dispatch was in two of the three.
    for section, pattern in (
        ("Full index", r"blog\.dugong\.live/([a-z0-9\-]+)\.html"),
        ("Articles", r"blog\.dugong\.live/([a-z0-9\-]+)\.html"),
        ("Markdown versions", r"blog\.dugong\.live/md/([a-z0-9\-]+)\.md"),
    ):
        block = re.search(
            r"\n## " + re.escape(section) + r"\n(.*?)(?=\n## |\Z)", llms, re.S
        )
        if not block:
            fail("llms_section_missing", section)
            continue
        listed = set(re.findall(pattern, block.group(1)))
        for name in posts:
            if name[:-5] not in listed:
                fail("llms_list_incomplete", f"{section}: {name}")

    # Each topic-guide line in llms.txt states a dispatch count. It has to
    # agree with the guide page's own ItemList and its visible card grid.
    # The inventory guide said 16 against 17 from 2026-10-15 to 2026-10-19.
    for guide, claimed in re.findall(
        r"blog\.dugong\.live/(shopify-[a-z\-]+\.html)\) \((\d+) dispatches\)",
        llms,
    ):
        if not os.path.exists(guide):
            fail("llms_guide_missing", guide)
            continue
        text = read(guide)
        cards = len(set(re.findall(
            r'<a href="([a-z0-9\-]+\.html)" class="card"', text
        )))
        counts = [
            node.get("numberOfItems")
            for node in nodes(jsonld(text, guide))
            if node.get("@type") == "ItemList"
        ]
        listed = counts[0] if counts else None
        if int(claimed) != cards or (listed is not None and listed != cards):
            fail(
                "llms_guide_count",
                f"{guide}: llms.txt says {claimed}, ItemList says {listed}, "
                f"page shows {cards} cards",
            )

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


    # ----------------------------------------------- internal link graph
    # Added 2026-10-21. Two distinct failures found that day, both of which
    # left recent dispatches almost invisible inside the site's own link
    # graph while every format check passed:
    #   * six dispatches published 2026-10-15 to 2026-10-21 appeared in 2 or
    #     3 READ NEXT grids against 73 to 82 for every other dispatch,
    #     because the archive grid is written at publication and no later run
    #     goes back to extend it.
    #   * nine dispatches had no editorial link from inside any other
    #     article's prose at all, only card links.
    published = {}
    for name in rendered:
        for node in nodes(docs[name]):
            if node.get("@type") in ("BlogPosting", "Article") and node.get("datePublished"):
                published[name] = node["datePublished"][:10]
                break
    newest_pub = max(published.values()) if published else ""

    # Every archive-shaped READ NEXT grid must carry every dispatch newer
    # than its own newest card. A grid counts as archive-shaped when it holds
    # ten or more cards and its leading run of newest-first dates is at least
    # six long; the short topical grids on recent dispatches are curated and
    # exempt by shape.
    #
    # Tightened 2026-10-24. The first version tested the first ten dates and
    # exempted anything that failed, which let three pages through: Nos 119,
    # 120 and 121 carry a newest-first head of six or seven followed by a
    # curated tail, so the tenth date broke the sort and the whole grid was
    # read as curated. All three heads had in fact stopped at 2026-10-14 and
    # were missing every dispatch from Nº 128 on. Testing the leading run
    # instead of a fixed window catches that shape.
    collection_pages = {
        name for name in rendered
        if any(node.get("@type") in ("CollectionPage", "ProfilePage")
               for node in nodes(docs[name]))
    } | {"index.html", "404.html"}
    for name in rendered:
        # Topic guides, the author pages and the front page carry curated
        # topical lists rather than the chronological archive, so they are
        # exempt by kind rather than by shape.
        if name in collection_pages:
            continue
        text = read(name)
        start = text.find('<section class="related">')
        if start < 0:
            continue
        section = text[start:text.find("</section>", start)]
        hrefs = re.findall(r'<a href="([a-z0-9\-]+\.html)" class="card"', section)
        dates = [published.get(h) for h in hrefs]
        if len(hrefs) < 10 or any(d is None for d in dates):
            continue
        run = 1
        while run < len(dates) and dates[run] <= dates[run - 1]:
            run += 1
        if run < 6:
            continue
        stale = sorted(
            (d, h) for h, d in published.items()
            if h != name and h not in hrefs and d > dates[0]
        )
        if stale:
            fail(
                "readnext_archive_stale",
                f"{name}: archive newest card is {dates[0]}, missing "
                f"{len(stale)} newer dispatch(es), e.g. {stale[-1][1]}",
            )

    # Every dispatch needs at least one editorial link, meaning an anchor
    # inside another page's <article>. Card grids are navigation; a link in
    # running prose is the one that carries topical meaning. A dispatch
    # published within three days of the newest one is exempt, because the
    # pages that will point at it are usually written after it.
    editorial_in = defaultdict(int)
    for src in rendered:
        text = read(src)
        article = re.search(r"<article.*?</article>", text, re.S)
        if not article:
            continue
        for href in set(re.findall(r'href="([a-z0-9\-]+\.html)[^"]*"', article.group(0))):
            target = href
            seen = 0
            while target in stub_target and seen < 5:
                target = stub_target[target]
                seen += 1
            if target != src and target in published:
                editorial_in[target] += 1
    for name, when in sorted(published.items()):
        if editorial_in[name] or name in EXCEPTIONS.get("editorial_inbound_exempt", set()):
            continue
        if newest_pub and (date_days(newest_pub) - date_days(when)) <= 3:
            notes.append(f"{name} has no editorial inbound link yet, published {when}")
            continue
        fail("dispatch_no_editorial_inbound", f"{name} (published {when})")

    # ------------------------------------- rendition parity: READING callout
    # The md/ rendition is the alternate answer engines are pointed at, so a
    # companion-reading block that exists on the page and not in the md means
    # the two disagree about what the article links to.
    for name in posts:
        text = read(name)
        callout = re.search(
            r'<span class="callout-mark">&#9670; READING</span>\s*<span>(.*?)</span>',
            text, re.S,
        )
        md_path = os.path.join("md", name[:-5] + ".md")
        if not callout or not os.path.exists(md_path):
            continue
        on_page = set(re.findall(r'href="([a-z0-9\-]+\.html)"', callout.group(1)))
        md_text = read(md_path)
        md_line = re.search(r"^> \*\*\u25c6 READING\*\* (.*)$", md_text, re.M)
        if not md_line:
            fail("reading_callout_missing_in_md", name)
            continue
        in_md = set(re.findall(r"\]\(https://blog\.dugong\.live/([a-z0-9\-]+\.html)\)", md_line.group(1)))
        if on_page != in_md:
            fail(
                "reading_callout_divergence",
                f"{name}: page links {sorted(on_page)}, md links {sorted(in_md)}",
            )

    # --------------------- rendition parity: READING callout in llms-full.txt
    # Added 2026-10-24 (second pass). The check above compares the page with
    # the md and says nothing about llms-full.txt, which is the third
    # rendition and the one an answer engine is pointed at. On the tree as
    # found, 74 of 89 segments carried the callout as "> \u25c6 READING:" with every
    # URL stripped out, 4 more had lost the blockquote marker, 1 wrote
    # &#9670; into a plain-text file and 6 had no callout at all. Nine
    # editorial URLs survived in the whole file against 209 in the md
    # renditions, so the one block in llms-full.txt whose entire purpose is
    # its links was the one block with no links. The newest generator output
    # writes the md line verbatim, so that is the canonical form and every
    # other rendering is legacy.
    if os.path.exists("llms-full.txt"):
        full = read("llms-full.txt")
        marks = [(m.start(), m.group(1)) for m in
                 re.finditer(r"URL: https://blog\.dugong\.live/([a-z0-9\-]+)\.html", full)]
        for k, (pos, slug) in enumerate(marks):
            end = marks[k + 1][0] if k + 1 < len(marks) else len(full)
            md_path = os.path.join("md", slug + ".md")
            if not os.path.exists(md_path):
                continue
            canon = re.search(r"^> \*\*\u25c6 READING\*\* .*$", read(md_path), re.M)
            if not canon:
                continue
            found = [l for l in full[pos:end].split("\n") if "READING" in l]
            if len(found) != 1 or found[0] != canon.group(0):
                fail("reading_callout_llms_divergence",
                     f"{slug}: llms-full.txt does not carry the md READING line verbatim")

    # ------------------------------------ rendition parity: the short answer
    # llms-full.txt carries a "## The short answer" block for the recent
    # dispatches. On 2026-10-21 eleven of the twelve existed only there: not
    # on the page and not in the md, so the one paragraph written to be
    # quoted back as the answer was invisible to every crawler that reads
    # HTML. Whatever llms-full.txt claims the short answer is, the page and
    # the md have to say it too.
    if os.path.exists("llms-full.txt"):
        for part in re.split(r"\n---\n", read("llms-full.txt")):
            url = re.search(r"^URL: (\S+)", part, re.M)
            short = re.search(r"^## The short answer\s*\n\s*\n(.+?)(?=\n\n)", part, re.M | re.S)
            if not url or not short:
                continue
            name = url.group(1).rsplit("/", 1)[-1]
            if name not in set(rendered):
                continue
            needle = folded(re.sub(r"\s+", " ", short.group(1)).strip())[:120]
            if needle and needle not in visible_text(read(name)):
                fail("short_answer_not_on_page", name)
            md_path = os.path.join("md", name[:-5] + ".md")
            if os.path.exists(md_path) and needle and needle not in folded(read(md_path)):
                fail("short_answer_not_in_md", name)

    # ------------------------------- the short answer is the speakable answer
    # Added 2026-10-24. A short answer is the one paragraph per article that
    # an answer engine is meant to lift whole, so it has to be addressable:
    # wrapped in a container a selector can name, named in speakable, and
    # carried in the article's abstract. Before this pass the block was a bare
    # h2 plus paragraphs with no class, speakable pointed only at the title
    # and the FAQ, and no page carried an abstract, so the most extractable
    # paragraph on the page was the one piece of it no machine was told about.
    for name in rendered:
        text = read(name)
        if "<h2>The short answer</h2>" not in text:
            continue
        i = text.find("<h2>The short answer</h2>")
        head = text[max(0, i - 200):i]
        if 'class="short-answer"' not in head:
            fail("short_answer_unwrapped",
                 f"{name}: the short answer is not inside a .short-answer container")
        if text.count('id="short-answer"') != 1:
            fail("short_answer_unwrapped",
                 f"{name}: expected exactly one id=\"short-answer\"")
        post = None
        for node in nodes(docs[name]):
            if node.get("@type") in ("BlogPosting", "Article"):
                post = node
                break
        if post is None:
            continue
        selectors = (post.get("speakable") or {}).get("cssSelector") or []
        if ".short-answer" not in selectors:
            fail("short_answer_not_speakable",
                 f"{name}: speakable cssSelector does not name .short-answer")
        abstract = post.get("abstract")
        if not abstract:
            fail("short_answer_no_abstract", f"{name}: BlogPosting carries no abstract")
        else:
            needle = folded(re.sub(r"\s+", " ", abstract).strip())[:120]
            if needle not in visible_text(text):
                fail("short_answer_no_abstract",
                     f"{name}: abstract does not appear in the visible page")

    # ------------------------- the short answer closes before the next heading
    # Added 2026-10-31. The short answer is written into the md rendition and
    # llms-full.txt by script, and two scripts wrote it two ways: 25 of the 90
    # md files and 14 llms-full entries ran the block's last paragraph
    # straight into the following "## " heading with no blank line between
    # them. CommonMark lets an ATX heading interrupt a paragraph, so
    # python-markdown and marked both render it correctly and the defect hid
    # behind that. pandoc's default markdown reader does not: it emits
    # "<p>...last sentence. ## Next heading</p>", which swallows the heading
    # into the one paragraph written to be lifted whole as the answer and
    # loses the section boundary underneath it. The md renditions exist to be
    # read by answer engines, so the block has to end the same way in all 90.
    def short_answer_tail(text, label):
        lines = text.split("\n")
        if "## The short answer" not in lines:
            return
        i = lines.index("## The short answer")
        j = i + 1
        while j < len(lines) and not lines[j].startswith("## "):
            j += 1
        if j < len(lines) and lines[j - 1].strip() != "":
            fail("short_answer_tail",
                 f"{label}: the short answer runs into {lines[j][:48]!r} "
                 f"with no blank line between them")

    for md_path in sorted(glob.glob(os.path.join("md", "*.md"))):
        short_answer_tail(read(md_path), md_path)
    if os.path.exists("llms-full.txt"):
        for part in re.split(r"\n---\n", read("llms-full.txt")):
            url = re.search(r"^URL: \S+/(\S+)$", part, re.M)
            short_answer_tail(part, "llms-full.txt:" + (url.group(1) if url else "?"))

    # ---------------------------------------------- counts a page claims
    # Added 2026-10-24 (second run). The publishing run that shipped Nº 135
    # added it to the inventory guide's ItemList, its card grid and llms.txt,
    # and left the guide's own two visible counts behind: the masthead still
    # said 17 and the list heading said 3. The question index masthead and the
    # homepage's question count drifted the same way, the homepage by twelve
    # on 10-24 and by six again hours later. Every one of these numbers is
    # written by hand next to a list the generator already knows the length
    # of, so each is checked against that list.
    guide_totals = {}
    for name in rendered:
        text = read(name)
        head = re.search(r"&#9670; (\d+) DISPATCHES IN THIS GUIDE", text)
        if head is None:
            continue
        listed = None
        for node in nodes(docs[name]):
            if node.get("@type") == "ItemList":
                listed = len(node.get("itemListElement") or [])
                break
        cards = len(set(re.findall(
            r'<a\b[^>]*href="(?:/)?([a-z0-9\-]+\.html)"[^>]*class="card|'
            r'<a\b[^>]*class="card[^"]*"[^>]*href="(?:/)?([a-z0-9\-]+\.html)"', text)))
        mast = re.search(r">(\d+) DISPATCHES</span>", text)
        claims = {"list heading": int(head.group(1))}
        if mast:
            claims["masthead"] = int(mast.group(1))
        if listed is not None:
            guide_totals[name] = listed
            for where, value in claims.items():
                if value != listed:
                    fail("guide_count_claim",
                         f"{name}: {where} says {value}, the guide lists {listed}")
            if cards and cards != listed:
                fail("guide_count_claim",
                     f"{name}: {cards} dispatch cards against an ItemList of {listed}")

    if guide_totals and os.path.exists("shopify-automation-questions.html"):
        qi = read("shopify-automation-questions.html")
        total = sum(guide_totals.values())
        mast = re.search(r">(\d+) DISPATCHES</span>", qi)
        if mast and int(mast.group(1)) != total:
            fail("guide_count_claim",
                 f"shopify-automation-questions.html: masthead says "
                 f"{mast.group(1)} dispatches, the eight guides list {total}")
        questions = None
        for node in nodes(docs.get("shopify-automation-questions.html", [])):
            if node.get("@type") == "ItemList":
                questions = len(node.get("itemListElement") or [])
                break
        if questions is not None:
            qmast = re.search(r">(\d+) QUESTIONS", qi)
            if qmast and int(qmast.group(1)) != questions:
                fail("question_count_claim",
                     f"shopify-automation-questions.html: masthead says "
                     f"{qmast.group(1)}, the index lists {questions}")
            if os.path.exists("index.html"):
                home = re.search(r"lists all (\d+) questions", read("index.html"))
                if home and int(home.group(1)) != questions:
                    fail("question_count_claim",
                         f"index.html: says the index lists {home.group(1)} "
                         f"questions, it lists {questions}")

    # ------------------------------------------------------ read-time band
    # Added 2026-10-24 (second run). Both dispatches shipped that day were
    # labelled 10 min, putting them at 356 and 326 claimed words per minute
    # against 172 to 312 for the other 87. The read time is written by hand
    # beside the word count, so the pair is checkable.
    #
    # Widened 2026-10-25. The pattern matched only the entity spelling of the
    # ticker's two separators, so it read 56 of the 90 dispatches and walked
    # past the 34 back-catalogue pages that write the same two characters
    # literally. A ticker it cannot parse is now a failure, not a silent pass:
    # a check that reports nothing because it found nothing to read is the
    # same as no check at all.
    TICKER = re.compile(r"(?:&#9670;|\u25c6) (\d+) MIN READ "
                        r"(?:&middot;|\u00b7) ([\d,]+) WORDS")
    for name in posts:
        text = read(name)
        pair = TICKER.search(text)
        if pair is None:
            fail("read_time_band",
                 f"{name}: no parseable MIN READ / WORDS ticker")
            continue
        minutes, words = int(pair.group(1)), int(pair.group(2).replace(",", ""))
        if minutes <= 0:
            fail("read_time_band", f"{name}: claims {minutes} min")
            continue
        wpm = words / minutes
        if not (WPM_MIN <= wpm <= WPM_MAX):
            fail("read_time_band",
                 f"{name}: {words} words in {minutes} min is {wpm:.0f} words "
                 f"per minute, outside {WPM_MIN}-{WPM_MAX}")

    # ------------------------------------- the length claims agree with each other
    # Added 2026-10-25. A dispatch states its own length six times: both
    # ticker spans, the JSON-LD wordCount and timeRequired, the MIN READ span
    # in the byline, and the "- Word count:" and "N min read" lines in the md
    # rendition. Twelve disagreed. Every one was a page an earlier
    # short-answer pass had extended: the pass raised wordCount in the JSON-LD
    # and in the md and left both ticker spans on the old number, so the
    # reader was shown a count 87 to 307 words short of the article in front
    # of them. Worse, the band check above reads the ticker, so for four
    # months it had been certifying read times against the one rendition of
    # the count that was wrong: corrected, 2,584 words in 8 min is 323 words
    # per minute and 3,301 in 10 min is 330, both outside the band.
    for name in posts:
        text = read(name)
        spans = TICKER.findall(text)
        if not spans:
            continue
        if len(set(spans)) > 1:
            fail("length_claim_divergence",
                 f"{name}: the ticker spans disagree: {sorted(set(spans))}")
            continue
        minutes, words = int(spans[0][0]), int(spans[0][1].replace(",", ""))
        jwords = re.search(r'"wordCount":\s*(\d+)', text)
        jmin = re.search(r'"timeRequired":\s*"PT(\d+)M"', text)
        byline = re.search(r">(\d+) MIN READ</span>", text)
        if jwords and int(jwords.group(1)) != words:
            fail("length_claim_divergence",
                 f"{name}: the ticker says {words:,} words, JSON-LD "
                 f"wordCount says {int(jwords.group(1)):,}")
        if jmin and int(jmin.group(1)) != minutes:
            fail("length_claim_divergence",
                 f"{name}: the ticker says {minutes} min, JSON-LD "
                 f"timeRequired says PT{jmin.group(1)}M")
        if byline and int(byline.group(1)) != minutes:
            fail("length_claim_divergence",
                 f"{name}: the ticker says {minutes} min, the byline says "
                 f"{byline.group(1)}")
        md_path = os.path.join("md", name[:-5] + ".md")
        if os.path.exists(md_path):
            md_text = read(md_path)
            mwords = re.search(r"^- Word count: (\d+)$", md_text, re.M)
            mmin = re.search(r"(\d+) min read", md_text)
            if mwords and int(mwords.group(1)) != words:
                fail("length_claim_divergence",
                     f"{name}: the ticker says {words:,} words, the md "
                     f"rendition says {int(mwords.group(1)):,}")
            if mmin and int(mmin.group(1)) != minutes:
                fail("length_claim_divergence",
                     f"{name}: the ticker says {minutes} min, the md "
                     f"rendition says {mmin.group(1)}")

    # -------------------------------------------------- feed is not ahead
    # Added 2026-10-24 (second run). feed.xml went out with lastBuildDate at
    # 13:30 UTC and its two newest items at 13:30 and 12:00, against a real
    # time of 10:14. Aggregators suppress or mis-sort a future-dated item,
    # and a lastBuildDate in the future is simply untrue.
    import datetime as _dt, email.utils as _eu
    _now = _dt.datetime.now(_dt.timezone.utc)
    _feed_raw = read("feed.xml")
    for _tag in ("lastBuildDate", "pubDate"):
        for _raw in re.findall(r"<" + _tag + r">([^<]+)</" + _tag + r">", _feed_raw):
            try:
                _when = _eu.parsedate_to_datetime(_raw)
            except Exception:
                fail("feed_date_unparseable", f"{_tag}: {_raw}")
                continue
            if _when.tzinfo is None:
                _when = _when.replace(tzinfo=_dt.timezone.utc)
            if _when > _now:
                fail("feed_date_in_future",
                     f"{_tag} {_raw} is {(_when - _now).total_seconds() / 3600:.1f}h ahead")

    # ------------------------------------------------- homepage tag cloud
    # Added 2026-10-25. The #tags cloud on index.html is written at
    # publication, one short run of tags per dispatch, and no later run goes
    # back over it. Two things had drifted:
    #   * three labels were used twice, each time pointing at a different
    #     dispatch: "split shipments", "dimensional weight" and "order
    #     routing". The reader sees one word twice in the same cloud, and
    #     because the cloud encodes weight as font size, "dimensional weight"
    #     appeared at 1.4rem and 2.3rem at once, so the size contradicted
    #     itself. Same link text pointing at two destinations is also
    #     WCAG 2.4.4.
    #   * two live dispatches had no tag at all, so they were absent from the
    #     only topical index of the whole archive the homepage offers.
    if os.path.exists("index.html"):
        home = read("index.html")
        # Attribute-tolerant: the section gained aria-labelledby on
        # 2026-11-19 and a literal tag match silently stopped finding it.
        cloud = re.search(r'<section class="topics" id="tags"[^>]*>.*?</section>',
                          home, re.S)
        if cloud is None:
            fail("tag_cloud_missing", "index.html has no #tags cloud")
        else:
            pairs = re.findall(
                r'href="([^"]*)" class="topic"[^>]*>([^<]*)</a>', cloud.group(0))
            seen = defaultdict(set)
            for href, label in pairs:
                seen[label].add(href)
            for label, hrefs in sorted(seen.items()):
                if len(hrefs) > 1:
                    fail("tag_cloud_duplicate_label",
                         f"{label!r} points at {len(hrefs)} dispatches: "
                         + ", ".join(sorted(hrefs)))
            tagged = {href for href, _ in pairs}
            for name in posts:
                if name not in tagged:
                    fail("tag_cloud_missing_dispatch",
                         f"{name} has no tag in the homepage cloud")

    # ------------------------------------------ site name in link text
    # Added 2026-10-25. 404.html builds its "Latest dispatches" list from each
    # page's <title>. A title keeps the " | Dugong" suffix only when the
    # headline is short enough to leave room for it under the 60-character
    # cap, so copying the title verbatim produced a list where five of ten
    # entries carried the site name and five did not. The suffix belongs to
    # the tab, never to a headline rendered inside the page.
    for name in rendered:
        for bad in re.findall(r'>([^<>]*\| Dugong)</a>', read(name)):
            fail("site_name_in_link_text", f"{name}: {bad.strip()!r}")

    # ------------------------------- llms-full.txt is one segment per dispatch
    # Added 2026-10-27. llms-full.txt declares its own structure in its header:
    # "Each article begins with a level-one heading and a metadata block (URL,
    # author, dates)", and every article is closed by a "---" line. Four
    # dispatches had left the md rendition's own internal "---" separators in
    # their segment, which splits one article into several chunks where only
    # the first carries the title, URL and author. 5,399 words, including four
    # whole FAQ blocks and 24 question-and-answer pairs, sat after a separator
    # with no article attached, so a crawler segmenting on the documented
    # delimiter attributes them to nothing.
    #
    # It also blinded this file. The three llms-full checks above split on the
    # same "\n---\n" and key each part by its URL line, so on those four
    # dispatches every one of them stopped reading at the first internal
    # separator. The READING-callout check (10-24) and the short-answer check
    # (10-25) were both silently skipping the tail of four articles.
    if os.path.exists("llms-full.txt"):
        _lf_raw = read("llms-full.txt")
        _chunks = [c for c in re.split(r"\n---\n", _lf_raw) if c.strip()]
        # the first chunk is the file header; every other one must be an article
        for _chunk in _chunks[1:]:
            if not re.search(r"^URL: ", _chunk, re.M):
                _head = re.search(r"^#{1,3} (.+)$", _chunk, re.M)
                fail("llms_full_orphan_chunk",
                     "a chunk of %d words carries no URL: line, so it belongs "
                     "to no article (opens: %s)"
                     % (len(_chunk.split()),
                        (_head.group(1) if _head else _chunk.strip()[:60])))
        if len(_chunks) - 1 != len(posts):
            fail("llms_full_orphan_chunk",
                 "llms-full.txt splits into %d article chunks against %d "
                 "dispatches" % (len(_chunks) - 1, len(posts)))

    # ------------------------------- llms-full.txt keeps the md's editorial links
    # Added 2026-10-27, and the reason it is here is that a narrower version of
    # it has been passing since 10-24. That pass found llms-full.txt carrying
    # the READING callout with every URL stripped, repaired the callout and
    # added a check that reads the callout line. The stripping was never
    # confined to that line. On the tree this check was written against, the md
    # bodies carried 868 editorial links and llms-full carried 309, of which
    # 213 were inside the one line the 10-24 check reads. Outside it, 96 links
    # had survived out of roughly 655. The anchor text was intact everywhere;
    # only the URL was gone.
    #
    # llms-full.txt is the file answer engines are pointed at, and its internal
    # links are how one learns the site's own topical graph, so a rendition
    # that keeps the words and drops the citations is the worst of the three to
    # have wrong. Anchor text that llms-full paraphrases away cannot be matched
    # and is reported as a note rather than a failure.
    if os.path.exists("llms-full.txt"):
        _link = re.compile(r"\[([^\]]+)\]\((https?://[^)]+)\)")
        _lf_raw = read("llms-full.txt")
        _starts = [m.start() for m in
                   re.finditer(r"(?m)^# (?!trigger$|steps$).+\n\nURL: ", _lf_raw)]
        _seg = {}
        for _a, _b in zip(_starts, _starts[1:] + [len(_lf_raw)]):
            _s = _lf_raw[_a:_b]
            _u = re.search(r"^URL: (\S+)", _s, re.M)
            if _u:
                _seg[_u.group(1).rsplit("/", 1)[-1]] = _s
        _absent = 0
        for name in posts:
            _md_path = os.path.join("md", name[:-5] + ".md")
            if name not in _seg or not os.path.exists(_md_path):
                continue
            _md_body = read(_md_path).split("\n---\n", 1)[-1]
            _have = {u for _, u in _link.findall(_seg[name])}
            _plain = _link.sub(r"\1", _seg[name])
            for _anchor, _url in _link.findall(_md_body):
                if _url in _have:
                    continue
                if _anchor in _plain:
                    fail("llms_full_link_stripped",
                         "%s: llms-full.txt carries %r as plain text and has "
                         "dropped its URL %s" % (name, _anchor[:60], _url))
                else:
                    _absent += 1
        if _absent:
            notes.append("%d md links could not be located in llms-full.txt "
                         "because its prose paraphrases the anchor text; those "
                         "are a rendition difference, not a stripped URL"
                         % _absent)

    # ----------------------------------- the renditions agree on the body prose
    # Added 2026-10-27. Four narrow parity checks existed before this one: the
    # HowTo steps (10-18), the READING callout (10-21 and 10-24), the short
    # answer (10-24 and 10-25), and the FAQ text via the structured data. Those
    # are four blocks per article. The article's own body prose, which is most
    # of the words on the site, was read by nothing, and the /md/ rendition is
    # what an answer engine is pointed at, so a sentence it carries that the
    # page does not is a contradiction between two renditions of one article.
    #
    # What it found: one dispatch whose md said "behaviour" where the page said
    # "behavior", in otherwise identical sentences, and one whose llms-full
    # segment is a 2,153-word rendering of a 2,873-word article, with 11 of its
    # 16 body paragraphs absent. A single word is a small defect; a check that
    # cannot see a single word also cannot see the eleven paragraphs.
    for name in posts:
        _md_path = os.path.join("md", name[:-5] + ".md")
        if not os.path.exists(_md_path):
            continue
        _vis = visible_text(read(name))
        _body = read(_md_path).split("\n---\n", 1)[-1]
        _fence = False
        for _para in _body.split("\n\n"):
            _para = _para.strip()
            if _para.startswith("```"):
                _fence = _para.count("```") == 1
                continue
            if _fence or not _para:
                continue
            if _para.startswith(("#", ">", "|", "-")) or \
               _para.startswith(("Permalink", "Markdown rendition")):
                continue
            _flat = folded(re.sub(r"[*`]", "",
                                  re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", _para)))
            if len(_flat) < 80:
                continue
            if _flat[:110] not in _vis:
                fail("rendition_prose_divergence",
                     "%s: the md rendition carries a paragraph the page does "
                     "not say: %r" % (name, _flat[:90]))

    # ------------------------------- every class in the markup has a rule
    # Added 2026-10-31. The short answer shipped as a styled block that was
    # never styled. `class="short-answer"` was written into 91 dispatches
    # across three runs, the JSON-LD named `.short-answer` in `speakable` and
    # carried the paragraph in `abstract`, and no page ever defined a CSS rule
    # for it, so the one passage written to be lifted whole as the answer
    # rendered as ordinary body prose with no container, no rule and no label.
    # Every machine had been told the block was special and the reader had
    # not. This is the same shape as the `.article-dek` anchor defect found on
    # 2026-10-21: markup shipped ahead of the stylesheet. A class that appears
    # in the markup and nowhere in that page's `<style>` is the signature.
    for name in rendered:
        _text = read(name)
        _css = " ".join(re.findall(r"<style[^>]*>(.*?)</style>", _text, re.S))
        _css = re.sub(r"/\*.*?\*/", "", _css, flags=re.S)
        _styled = set(re.findall(r"\.([A-Za-z0-9_-]+)", _css))
        _markup = re.sub(r"<style[^>]*>.*?</style>", "", _text, flags=re.S | re.I)
        _markup = re.sub(r"<script[^>]*>.*?</script>", "", _markup, flags=re.S | re.I)
        _used = set()
        for _m in re.finditer(r'\sclass="([^"]+)"', _markup):
            _used.update(_m.group(1).split())
        for _cls in sorted(_used - _styled - EXCEPTIONS["unstyled_class"]):
            fail("unstyled_class",
                 f"{name}: .{_cls} is used in the markup and has no rule in "
                 f"this page's stylesheet")

    # ----------------------------- the homepage masthead names the newest post
    # Added 2026-10-31. index.html's hero carries three claims about the
    # newest dispatch: `.hero-issue` ("ISSUE Nº N"), `.hero-date`, and the
    # first `.stat-num`, which has equalled the issue number in every commit
    # since the hero was written. On 2026-10-31 all three were a week and an
    # issue behind: the masthead said Nº 136 and OCT 24 while Nº 137 had
    # shipped that morning, and the date had already been wrong before that,
    # because the run that shipped Nº 136 on 10-25 advanced the number and
    # left the date on 10-24. The hero is written at publication and no later
    # run goes back over it, the same drift shape as READ NEXT and the tag
    # cloud. A dispatch published the same day as this run is not yet required
    # to appear, so the check reads the newest dispatch the site actually has.
    if "index.html" in rendered and posts:
        _home = read("index.html")
        _newest, _newest_num, _newest_date = None, None, None
        for _name in posts:
            _d = re.search(r'article:published_time" content="([^"]+)"', read(_name))
            _n = re.search(r"DISPATCH N[^0-9<]{0,12}?(\d+)", read(_name))
            if not _d or not _n:
                continue
            _key = (_d.group(1), int(_n.group(1)))
            if _newest is None or _key > _newest:
                _newest, _newest_num, _newest_date = _key, int(_n.group(1)), _d.group(1)
        if _newest_num is not None:
            _issue = re.search(r'class="hero-issue">ISSUE N[^0-9<]{0,12}?(\d+)<', _home)
            if not _issue:
                fail("hero_masthead", "index.html: no parseable .hero-issue")
            elif int(_issue.group(1)) != _newest_num:
                fail("hero_masthead",
                     f"index.html: the hero says ISSUE Nº {_issue.group(1)}, the "
                     f"newest dispatch is Nº {_newest_num}")
            _stat = re.search(r'class="stat-num">(\d+)<', _home)
            if not _stat:
                fail("hero_masthead", "index.html: no parseable first .stat-num")
            elif int(_stat.group(1)) != _newest_num:
                fail("hero_masthead",
                     f"index.html: the hero stat says {_stat.group(1)}, the "
                     f"newest dispatch is Nº {_newest_num}")
            _hd = re.search(r'class="hero-date">([^<]+)<', _home)
            if not _hd:
                fail("hero_masthead", "index.html: no parseable .hero-date")
            else:
                _want = datetime.strptime(_newest_date, "%Y-%m-%d")
                _want = f"{_want.strftime('%b').upper()} {_want.day} \u00b7 {_want.year}"
                if " ".join(_hd.group(1).split()) != _want:
                    fail("hero_masthead",
                         f"index.html: the hero date says "
                         f"{' '.join(_hd.group(1).split())!r}, the newest "
                         f"dispatch Nº {_newest_num} published {_want!r}")

    # ------------------------------------------------- 404 latest dispatches
    # 404.html builds a "Latest dispatches" list of the ten newest dispatches.
    # The publishing run prepends the dispatch it just shipped and drops the
    # oldest, so a dispatch the run never added is gone for good rather than
    # late. Nº 137 shipped 2026-10-31 and was never added; the run that
    # shipped Nº 138 on 2026-11-02 prepended Nº 138 and pushed the window
    # past it, so the list jumped from 11-02 straight to 10-25 and the newest
    # dispatch but one was missing from the only index 404.html offers. Same
    # drift shape as the hero masthead, READ NEXT and the tag cloud: written
    # at publication, never revisited. Backfilled and checked 2026-11-02.
    if "404.html" in rendered and posts:
        _dated = []
        for _name in posts:
            _src = read(_name)
            _d = re.search(r'article:published_time" content="([^"]+)"', _src)
            _n = re.search(r"DISPATCH N[^0-9<]{0,12}?(\d+)", _src)
            if _d and _n:
                _dated.append((_d.group(1)[:10], int(_n.group(1)), _name))
        _dated.sort(reverse=True)
        _want = [_n for _, _, _n in _dated[:10]]
        _got = re.findall(r'<li><a href="/([a-z0-9\-]+\.html)"', read("404.html"))
        if not _got:
            fail("four_oh_four_latest", "404.html: no parseable dispatch list")
        else:
            for _name in _want:
                if _name not in _got:
                    fail("four_oh_four_latest",
                         f"404.html: {_name} is among the ten newest dispatches "
                         f"and is not in the list")
            for _name in _got:
                if _name not in _want:
                    fail("four_oh_four_latest",
                         f"404.html: {_name} is in the list and is not among "
                         f"the ten newest dispatches")

    # ------------------------------------------------------------ focus ring
    # Every rendered page brands its keyboard focus ring in --lime-deep. On
    # 2026-11-02, 404.html alone carried no :focus-visible rule at all, so its
    # sixteen links fell back to the user agent's own ring and a keyboard user
    # got a different, unbranded focus indicator on exactly one page of the
    # site. Markup shipped ahead of the stylesheet, the same shape as the
    # .short-answer and .article-dek defects before it.
    for _name in rendered:
        _src = read(_name)
        if not re.search(r":focus-visible[^{]*\{[^}]*outline", _src):
            fail("focus_ring",
                 f"{_name}: no :focus-visible rule setting an outline")

    # ------------------------------------------- a homepage card per dispatch
    # The homepage article grid carries one `a.card` per dispatch. The lead
    # essay was the single dispatch with no card: it had been reachable only
    # from the featured card and the tag cloud, and because the grid's type
    # filter reads the cards, the `essays` pill surfaced three cards for
    # essays that were never published and not the one real essay the site
    # has. Added 2026-11-02.
    if "index.html" in rendered and posts:
        _home = read("index.html")
        _grid = _home[_home.find('<div class="article-grid"'):]
        _carded = set(re.findall(r'<a class="card[^"]*" href="/?([a-z0-9\-]+\.html)"', _grid))
        for _name in posts:
            if _name not in _carded:
                fail("homepage_card",
                     f"{_name}: no card in the homepage article grid")

    # --------------------------------------------------- ticker month count
    # The homepage ticker claims "N NEW DISPATCH(ES) THIS MONTH". The run
    # recomputes it when it publishes and nothing touches it in between, so
    # the claim is true on publication days and drifts afterwards: it read 15
    # against an October that held 17, and on 2026-11-02, before the day's
    # run, it still read 15 while November held none. "This month" is the
    # reader's month, so the count is checked against today rather than
    # against the newest dispatch's month. That means this check fires on the
    # first of a month until the month's first dispatch ships, which is
    # correct: the claim really is false on those days. A run that finds it
    # red and is not publishing should rewrite the span to the true count.
    if "index.html" in rendered and posts:
        _home = read("index.html")
        _claim = re.search(r"(\d+)\s+NEW\s+DISPATCH(?:ES)?\s+THIS\s+MONTH", _home)
        if not _claim:
            fail("ticker_month", "index.html: no parseable ticker month count")
        else:
            _month = datetime.now().strftime("%Y-%m")
            _actual = 0
            for _name in posts:
                _d = re.search(r'article:published_time" content="([^"]+)"', read(_name))
                if _d and _d.group(1)[:7] == _month:
                    _actual += 1
            if int(_claim.group(1)) != _actual:
                fail("ticker_month",
                     f"index.html: the ticker says {_claim.group(1)} new "
                     f"dispatch(es) this month, {_month} holds {_actual}")

    # ------------------------------------------------------- reduced motion
    # Every rendered page shortens its animations and transitions under
    # `prefers-reduced-motion: reduce`. On 2026-11-04, 404.html alone carried
    # no such block, so its link and summary transitions ran at full duration
    # for a reader who had asked the operating system for less motion. Exactly
    # the shape of the :focus-visible gap found on the same page two days
    # earlier, and of .short-answer and .article-dek before it: a page gets
    # the markup and misses the stylesheet rule that goes with it.
    for name in rendered:
        if not re.search(r"@media[^{]*prefers-reduced-motion\s*:\s*reduce",
                         read(name)):
            fail("reduced_motion",
                 f"{name}: no @media (prefers-reduced-motion: reduce) block")

    # ------------------------------------------------- the skip link skips
    # 103 pages point `.skip-link` at `#main`, the `<article role="main">`
    # that sits below the masthead, so the first Tab lands a keyboard user
    # past the ticker and the nav. index.html pointed its own at
    # `#view-home`, the wrapper that *contains* the ticker, the header and
    # the nav, so the one control on the page whose whole purpose is to
    # bypass the navigation put the reader back above it. The target has to
    # open after the header closes; a page with no `<header>` (404.html,
    # whose first focusable element is already the content) has nothing to
    # skip and is not required to carry the link. Added 2026-11-04.
    for name in rendered:
        _src = read(name)
        _skip = re.search(r'<a[^>]*class="skip-link"[^>]*href="#([^"]+)"', _src)
        if not _skip:
            _skip = re.search(r'<a[^>]*href="#([^"]+)"[^>]*class="skip-link"', _src)
        _head_end = _src.find("</header>")
        if not _skip:
            if _head_end != -1:
                fail("skip_link",
                     f"{name}: has a <header> and no .skip-link to bypass it")
            continue
        _target = re.search(rf'id="{re.escape(_skip.group(1))}"', _src)
        if not _target:
            fail("skip_link",
                 f"{name}: .skip-link points at #{_skip.group(1)}, which no "
                 f"element on the page carries")
        elif _head_end != -1 and _target.start() < _head_end:
            fail("skip_link",
                 f"{name}: .skip-link points at #{_skip.group(1)}, which "
                 f"opens before </header>, so it skips nothing")

    # -------------------------------------------------------- house spelling
    # The site writes American forms, and overwhelmingly so: 1,222 uses of
    # `fulfillment` and 755 of `catalog` against none of the British spelling,
    # 236 `judgment` against one `judgement`. On 2026-11-04 the day's dispatch
    # shipped `fulfilment`, and a sweep found seven more slips sitting in the
    # three dispatches published since 10-31: four `colour`, one `behaviour`,
    # one `judgement`, one `customise` and one `apologise`. Each had travelled
    # into the md rendition, llms.txt, llms-full.txt and the feed along with
    # the page, so one typed word became up to five published ones. Checked
    # against the visible text, so a CSS comment that says "dek colour" is not
    # a finding. `cancelled` is deliberately absent from this table: it is the
    # house form, 260 uses to 11, and the eleven are Shopify's own trigger
    # names ("Order canceled"), which are quoted as the admin writes them.
    HOUSE_SPELLING = {
        "fulfilment": "fulfillment",
        "colour": "color",
        "behaviour": "behavior",
        "judgement": "judgment",
        "licence": "license",
        "catalogue": "catalog",
        "centre": "center",
        "labelled": "labeled",
        "travelling": "traveling",
        "organise": "organize",
        "recognise": "recognize",
        "customise": "customize",
        "optimise": "optimize",
        "prioritise": "prioritize",
        "summarise": "summarize",
        "apologise": "apologize",
        # Added 2026-11-18. "greyed" shipped twice on one dispatch against 23
        # uses of "grayed", and "neighbours" once against 6 of "neighbors".
        # Each had travelled into the md rendition and llms-full.txt with the
        # page, which is the 2026-11-04 shape: one typed word, up to five
        # published ones. "greyhound" does not match, the word boundary ends
        # the pattern at "grey".
        "grey": "gray",
        "neighbour": "neighbor",
        "neighbourhood": "neighborhood",
        # "analyse" is deliberately absent: the suffix pattern below
        # would read "analyses", the ordinary plural of "analysis", as a
        # British verb form. It fired on exactly that the first time the
        # table was run, and a check that cries wolf gets switched off.
    }
    _spell_targets = [(name, visible_text(read(name))) for name in rendered]
    for name in sorted(glob.glob("md/*.md")):
        _spell_targets.append((name, folded(read(name))))
    for name in ("llms.txt", "llms-full.txt", "feed.xml"):
        if os.path.exists(name):
            _spell_targets.append((name, folded(read(name))))
    for name, _text in _spell_targets:
        for _bad, _good in HOUSE_SPELLING.items():
            _n = len(re.findall(rf"\b{_bad}(?:s|d|ed|ing)?\b", _text))
            if _n:
                fail("house_spelling",
                     f"{name}: {_n} use(s) of {_bad!r}; the house spelling is "
                     f"{_good!r}")

    # ------------------------------- the questions carry their own addresses
    # Added 2026-11-04, found absent from this file on 2026-11-16 and written
    # again. _tools/README.md has documented these seven invariants since
    # 11-04 and the file did not implement one of them, so for twelve days the
    # README described a checker that did not exist. The site changes that pass
    # made all survived and were extended to dispatch No 140; only the checks
    # behind them were lost. Restored verbatim in behaviour, not in wording.
    #
    # Every FAQ answer sits in a .faq-item with id="faq-1".."faq-N" and its
    # paragraph at id="faq-N-answer". A Question node that names a question and
    # an answer and says nothing about where either one lives lets an engine
    # cite the page and nothing finer, on a page carrying up to seven others.
    for name in rendered:
        ids = page_ids.get(name, set())
        base = expected_url(name)
        for node in nodes(docs[name]):
            if node.get("@type") != "FAQPage":
                continue
            for index, question in enumerate(node.get("mainEntity") or [], 1):
                if not isinstance(question, dict):
                    continue
                want = f"{base}#faq-{index}"
                for field in ("@id", "url"):
                    got = question.get(field)
                    if got != want:
                        fail(
                            "question_without_anchor",
                            f"{name}: question {index} {field} is "
                            f"{'missing' if got is None else got}, want {want}",
                        )
                if f"faq-{index}" not in ids:
                    fail("question_anchor_not_in_page", f"{name}: #faq-{index}")
                answer = question.get("acceptedAnswer")
                if not isinstance(answer, dict):
                    continue
                want_a = f"{base}#faq-{index}-answer"
                for field in ("@id", "url"):
                    got = answer.get(field)
                    if got != want_a:
                        fail(
                            "answer_without_anchor",
                            f"{name}: answer {index} {field} is "
                            f"{'missing' if got is None else got}, want {want_a}",
                        )
                if f"faq-{index}-answer" not in ids:
                    fail("answer_anchor_not_in_page", f"{name}: #faq-{index}-answer")

    # ------------------------------- a list that names a URL must name a node
    # An index that lists a bare URL points at a document; the edge lands on a
    # page rather than on the node inside it. BreadcrumbList is excluded on
    # purpose: a breadcrumb's `item` is a bare URL by specification, and the
    # trail names positions rather than content.
    #
    # The resolver needs care. A dict holding nothing but an @id is a
    # reference, not a definition. The first version of this check collected
    # every @id it saw, which included the pointer under test, so a reference
    # vouched for itself and a ListItem pointing at a node that does not exist
    # passed.
    defined_ids = set()
    for name in rendered:
        for node in nodes(docs[name]):
            node_id = node.get("@id")
            if node_id and len(node) > 1:
                defined_ids.add(node_id)
            for value in node.values():
                for child in (value if isinstance(value, list) else [value]):
                    if isinstance(child, dict):
                        child_id = child.get("@id")
                        if child_id and len(child) > 1:
                            defined_ids.add(child_id)
                        for grand in child.values():
                            for leaf in (grand if isinstance(grand, list) else [grand]):
                                if isinstance(leaf, dict) and leaf.get("@id") and len(leaf) > 1:
                                    defined_ids.add(leaf["@id"])

    for name in rendered:
        for node in nodes(docs[name]):
            if node.get("@type") != "ItemList":
                continue
            for entry in node.get("itemListElement") or []:
                if not isinstance(entry, dict):
                    continue
                url = entry.get("url")
                if not url:
                    continue
                want = url if "#" in url else url + "#article"
                item = entry.get("item")
                got = item.get("@id") if isinstance(item, dict) else item
                label = (entry.get("name") or "")[:40]
                if got != want:
                    fail(
                        "listitem_without_item",
                        f"{name}: {label!r} -> {got or 'no item'}, want {want}",
                    )
                elif got not in defined_ids:
                    fail("listitem_item_unresolved", f"{name}: {got}")

    # ------------------------- a dispatch names the guide it belongs to
    # The guides assert membership downward through their ItemList; until
    # 2026-11-04 no dispatch asserted it upward. The breadcrumb names the
    # guide, but a breadcrumb is a navigation position, not membership, the
    # same way adjacency inside a @graph asserted nothing before 10-18.
    for name in rendered:
        page_nodes = list(nodes(docs[name]))
        article = next((n for n in page_nodes if n.get("@type") == "BlogPosting"), None)
        if article is None:
            continue
        crumb = next((n for n in page_nodes if n.get("@type") == "BreadcrumbList"), None)
        if crumb is None:
            continue
        guides = set()
        for entry in crumb.get("itemListElement") or []:
            target = entry.get("item")
            target = target.get("@id") if isinstance(target, dict) else target
            if not isinstance(target, str):
                continue
            leaf = target.split("#")[0].rsplit("/", 1)[-1]
            if leaf.startswith("shopify-") and leaf != name:
                guides.add(target.split("#")[0] + "#collection")
        parents = {
            p.get("@id")
            for p in (article.get("isPartOf") if isinstance(article.get("isPartOf"), list)
                      else [article.get("isPartOf")])
            if isinstance(p, dict)
        }
        for guide in sorted(guides - parents):
            fail("dispatch_not_in_guide", f"{name}: {guide}")

    # --------------------------- every page says what kind of page it is
    # Added 2026-11-16. Of the 107 rendered pages, the 2 author archives
    # declare a ProfilePage and the 9 guides declare a CollectionPage, each
    # referencing its own BreadcrumbList through `breadcrumb` and naming its
    # `mainEntity`. The 94 dispatches, which are the whole point of the site,
    # declared nothing: no page node, a BreadcrumbList referenced by nothing,
    # and a `mainEntityOfPage` holding a bare URL string, which names a
    # document rather than a node. Same defect the 11-04 pass fixed for 660
    # ListItem entries, one layer out.
    PAGE_TYPES = ("WebPage", "CollectionPage", "ProfilePage", "ItemPage", "AboutPage")
    for name in rendered:
        if name in EXCEPTIONS["page_node_exempt"]:
            continue
        page_nodes = list(nodes(docs[name]))
        if not page_nodes:
            continue
        base = expected_url(name)
        page = next((n for n in page_nodes if n.get("@type") in PAGE_TYPES), None)
        if page is None:
            fail("page_without_page_node", f"{name}: no {'/'.join(PAGE_TYPES[:3])} node")
            continue
        if page.get("url") != base:
            fail("page_node_url", f"{name}: url is {page.get('url')!r}, want {base}")

        # The breadcrumb has to be claimed, or it sits in the array asserting
        # nothing, which is what the FAQPage did before 10-18.
        crumb = next((n for n in page_nodes if n.get("@type") == "BreadcrumbList"), None)
        if crumb is not None:
            claimed = page.get("breadcrumb")
            claimed = claimed.get("@id") if isinstance(claimed, dict) else claimed
            if claimed != crumb.get("@id"):
                fail(
                    "breadcrumb_unreferenced",
                    f"{name}: page node claims {claimed or 'no breadcrumb'}, "
                    f"want {crumb.get('@id')}",
                )

        # mainEntity points at the one thing the page is about.
        subject = next(
            (n for n in page_nodes
             if n.get("@type") in ("BlogPosting", "ItemList", "Person")),
            None,
        )
        if subject is not None:
            got = page.get("mainEntity")
            got = got.get("@id") if isinstance(got, dict) else got
            if got not in defined_ids:
                fail(
                    "page_mainentity_unresolved",
                    f"{name}: mainEntity is {got or 'missing'}",
                )

        # A dispatch's page node has to agree with its article about dates, or
        # the site gains a second freshness claim that can drift from the
        # first, which is how every date defect in this file started.
        article = next((n for n in page_nodes if n.get("@type") == "BlogPosting"), None)
        if article is not None:
            for field in ("datePublished", "dateModified"):
                if page.get(field) != article.get(field):
                    fail(
                        "page_node_date_drift",
                        f"{name}: {field} {page.get(field)} on the page node, "
                        f"{article.get(field)} on the article",
                    )
            # A bare string names a document. It has to name the node.
            meop = article.get("mainEntityOfPage")
            got = meop.get("@id") if isinstance(meop, dict) else meop
            if got != page.get("@id"):
                fail(
                    "mainentityofpage_not_node",
                    f"{name}: mainEntityOfPage is "
                    f"{meop if isinstance(meop, str) else got!r}, want {page.get('@id')}",
                )

        primary = page.get("primaryImageOfPage")
        primary = primary.get("@id") if isinstance(primary, dict) else primary
        if primary is not None and primary not in defined_ids:
            fail("primaryimage_unresolved", f"{name}: {primary}")

    # ------------- the two liftable nodes carry an address and a provenance
    # Added 2026-11-18. Every dispatch carries a FAQPage and a HowTo, and
    # those are the two nodes on the page that an answer engine lifts on
    # their own. The article claimed both through `hasPart` since 10-18.
    # Neither claimed anything back: the FAQPage held `@id` and `mainEntity`
    # and nothing else, so 481 Question nodes with their own addresses hung
    # under a parent naming no page, no writer, no day and no topic, and the
    # HowTo held name, description, totalTime, step and inLanguage on 94 of
    # its 95. Same shape as the FAQPage before 10-18, the 660 `ListItem`
    # entries before 11-04, the 94 dispatches with no page node before 11-16
    # and the 398 anonymous entities before 11-17: the node exists, the edge
    # does not. Every value checked here is one the article on the same page
    # already asserts, or a reference to a node already defined in the same
    # graph, so a disagreement is a drift rather than a difference of
    # opinion. The anchors are checked against the markup because a `url`
    # naming a fragment that is not in the page is worse than no `url`.
    PART_ANCHOR = {"FAQPage": "faq-heading", "HowTo": "playbook"}
    PART_SHARED = ("inLanguage", "datePublished", "dateModified")
    for name in rendered:
        page_nodes = list(nodes(docs[name]))
        base = expected_url(name)
        article = next(
            (n for n in page_nodes if n.get("@id") == base + "#article"), None)
        if article is None:
            continue
        text = read(name)
        for part in page_nodes:
            anchor = PART_ANCHOR.get(part.get("@type"))
            if anchor is None or not part.get("@id"):
                continue
            kind = part["@type"]
            want_url = base + "#" + anchor
            if part.get("url") != want_url:
                fail(
                    "part_without_url",
                    f"{name}: {kind} url is {part.get('url') or 'absent'}, "
                    f"want {want_url}",
                )
            elif f'id="{anchor}"' not in text:
                fail(
                    "part_url_anchor_missing",
                    f"{name}: {kind} url names #{anchor}, which is not in the markup",
                )

            # The inverse of the hasPart the article has written since 10-18.
            claimed = part.get("isPartOf")
            claimed = claimed.get("@id") if isinstance(claimed, dict) else claimed
            if claimed != article.get("@id"):
                fail(
                    "part_isnotpartof_article",
                    f"{name}: {kind} isPartOf is {claimed or 'absent'}, "
                    f"want {article.get('@id')}",
                )

            # Provenance: present, and agreeing with the article it is part of.
            for field in PART_SHARED:
                if not part.get(field):
                    fail("part_without_provenance", f"{name}: {kind} has no {field}")
                elif part.get(field) != article.get(field):
                    fail(
                        "part_provenance_drift",
                        f"{name}: {kind} {field} is {part.get(field)!r}, "
                        f"{article.get(field)!r} on the article",
                    )
            for field in ("author", "publisher"):
                got = part.get(field)
                got = got.get("@id") if isinstance(got, dict) else got
                theirs = article.get(field)
                theirs = theirs[0] if isinstance(theirs, list) and theirs else theirs
                theirs = theirs.get("@id") if isinstance(theirs, dict) else theirs
                if not got:
                    fail("part_without_provenance", f"{name}: {kind} has no {field}")
                elif got != theirs:
                    fail(
                        "part_provenance_drift",
                        f"{name}: {kind} {field} is {got}, {theirs} on the article",
                    )
                elif got not in defined_ids:
                    fail("part_ref_unresolved", f"{name}: {kind} {field} -> {got}")

            # Google's HowTo documentation asks for an image; the page has one
            # and names it #primaryimage, so the reference costs nothing.
            if kind == "HowTo":
                got = part.get("image")
                got = got.get("@id") if isinstance(got, dict) else got
                if not got:
                    fail("part_without_provenance", f"{name}: HowTo has no image")
                elif got not in defined_ids:
                    fail("part_ref_unresolved", f"{name}: HowTo image -> {got}")

            # The topic, as the article states it, in the same order. A part
            # about something its own article is not about is a drift, and a
            # reference to an entity the site never defines is a dead edge.
            def ids_of(value):
                listed = value if isinstance(value, list) else [value]
                return [
                    e.get("@id") for e in listed
                    if isinstance(e, dict) and e.get("@id")
                ]
            mine = ids_of(part.get("about") or [])
            theirs = ids_of(article.get("about") or [])
            if not mine:
                fail("part_without_provenance", f"{name}: {kind} has no about")
            elif mine != theirs:
                fail(
                    "part_provenance_drift",
                    f"{name}: {kind} is about {len(mine)} entities against "
                    f"{len(theirs)} on the article"
                    + (f"; first difference at position "
                       f"{next(i + 1 for i, (a, b) in enumerate(zip(mine + [None] * len(theirs), theirs + [None] * len(mine))) if a != b)}"
                       if mine != theirs else ""),
                )
            else:
                for entity in mine:
                    if entity not in defined_ids:
                        fail("part_ref_unresolved", f"{name}: {kind} about -> {entity}")

    # ------------------- an index cannot predate the newest thing it lists
    # Added 2026-11-16. The existing date check asks whether a page's
    # dateModified agrees with its sitemap lastmod. Both can be stale
    # together, and on the homepage they were: `Blog.dateModified` and the
    # sitemap both read 2026-10-24 while the Blog node listed dispatches
    # published 11-02, 11-04 and 11-07 fourteen lines below. Three publishing
    # runs added a card, a hero masthead, a ticker count, a tag-cloud entry
    # and a `blogPost` entry to that page and none of them moved its date, so
    # the single most-crawled page on the site understated its own freshness
    # by two weeks. Agreement is not truth.
    #
    # Membership is written on publication day, which is what makes this
    # mechanical: a page cannot have listed a dispatch published on 11-07
    # while last changing on 10-24. The comparison is against `datePublished`
    # rather than `dateModified` for exactly that reason. A later edit to a
    # dispatch's own text does not oblige every index that lists it to move.
    for name in rendered:
        page_nodes = list(nodes(docs[name]))
        owner = next(
            (n for n in page_nodes
             if n.get("@type") in ("Blog", "ProfilePage", "CollectionPage")
             and n.get("dateModified")),
            None,
        )
        if owner is None:
            continue
        listed = set()
        for node in page_nodes:
            if node.get("@type") == "ItemList":
                for entry in node.get("itemListElement") or []:
                    if isinstance(entry, dict) and entry.get("url"):
                        listed.add(entry["url"].split("#")[0].rsplit("/", 1)[-1])
            if node.get("@type") == "Blog":
                for entry in node.get("blogPost") or []:
                    if isinstance(entry, dict):
                        ref = entry.get("url") or entry.get("@id") or ""
                        listed.add(ref.split("#")[0].rsplit("/", 1)[-1])
        newest, newest_name = "", ""
        for leaf in listed:
            when = published.get(leaf)
            if when and when > newest:
                newest, newest_name = when, leaf
        if newest and owner["dateModified"] < newest:
            fail(
                "index_date_before_newest_listed",
                f"{name}: {owner['@type']}.dateModified is "
                f"{owner['dateModified']} and it lists {newest_name} "
                f"published {newest}",
            )

    # ------------------- an anchor must not land underneath the sticky nav
    # Added 2026-11-16. Every rendered page except 404.html carries
    # `.nav { position: sticky; top: 0 }`, 66px tall above 820px and 89 to
    # 93px below it where the row wraps. No page declared scroll-padding-top,
    # so every fragment jump put the target's first ~92px behind that bar:
    # the `#main` skip link on 107 pages, the six `index.html#...` section
    # links in the footer of every page, and 470 `...#faq-N` links. Measured
    # before the fix, `#faq-1` and `#main` both settled with the target's top
    # edge at y=0 under a bar whose bottom edge was at y=92. WCAG 2.4.1.
    for name in rendered:
        text = read(name)
        if "position: sticky" not in text:
            continue
        if text.count("scroll-padding-top") < 2:
            fail(
                "no_scroll_padding_under_sticky_nav",
                f"{name}: sticky nav with "
                f"{text.count('scroll-padding-top')} scroll-padding-top rule(s), "
                "needs a base value and a >820px override",
            )

    # ------------------- the homepage's featured slot must be the newest post
    # Added 2026-11-16. `<section class="featured" id="latest">` is headed
    # "DISPATCH OF THE WEEK" and is where the "Latest" nav link on all 107
    # other pages points. It still linked Nº 47, published 2026-05-28, after
    # 47 later dispatches had shipped; the hero one screen above it read
    # "ISSUE Nº 141 / NOV 16". The publishing run writes a card, a ticker
    # count and a tag-cloud entry on publication day and has never touched
    # this block, so it can only go stale.
    if "index.html" in rendered:
        home = read("index.html")
        hit = re.search(r'<a href="([^"]+)" class="featured-card">', home)
        if not hit:
            fail("featured_card_missing", "index.html: no .featured-card link")
        else:
            newest_pages = sorted(n for n, d in published.items() if d == newest_pub)
            if hit.group(1) not in newest_pages:
                fail(
                    "featured_card_not_newest",
                    f"index.html: DISPATCH OF THE WEEK links {hit.group(1)} "
                    f"(published {published.get(hit.group(1), '?')}); newest is "
                    f"{', '.join(newest_pages)} ({newest_pub})",
                )

    # ------------------- every archive row must link a page that exists
    # Added 2026-11-16. The six rows under "FROM THE ARCHIVE", which is where
    # the "Archive" nav link on every page lands, were bare spans: numbers
    # 036 to 041 and titles ("A short history of if-this-then-that" and five
    # more) that appear nowhere else in the repository, in the feed, in
    # llms.txt or in /md/. Six dead rows describing six articles that were
    # never published, carrying no link for a reader to follow.
    if "index.html" in rendered:
        home = read("index.html")
        block = re.search(r'<ul class="archive-list">(.*?)</ul>', home, re.S)
        if not block:
            fail("archive_list_missing", "index.html: no .archive-list")
        else:
            rows = re.findall(r"<li\b.*?</li>", block.group(1), re.S)
            if not rows:
                fail("archive_list_empty", "index.html: .archive-list has no rows")
            for row in rows:
                label = re.search(r'class="arch-title"[^>]*>(.*?)</span>', row, re.S)
                label = re.sub(r"<[^>]+>", "", label.group(1)).strip() if label else "?"
                href = re.search(r'<a href="([^"#]+)', row)
                if not href:
                    fail("archive_row_without_link", f"index.html: '{label}'")
                elif not os.path.exists(href.group(1)):
                    fail(
                        "archive_row_dead_link",
                        f"index.html: '{label}' -> {href.group(1)} does not exist",
                    )


    # ------------------------------------------------- entity identity
    # 2026-11-17. The site grounded 398 entity references in Wikidata and
    # English Wikipedia and identified not one of them. Every `about` entry was
    # an anonymous `Thing` carrying a name string, so 'Shopify' on 104 pages
    # was 104 unrelated nodes and nothing in the graph said they were the same
    # company. The identifier was already inside each node, in its own
    # `sameAs`; it is now also its `@id`, which is the only property a consumer
    # merges on. Same shape as the FAQPage before 10-18, the 660 `ListItem`
    # entries before 11-04 and the 94 dispatches with no page node before
    # 11-16: the node exists, the identity does not.
    WIKIDATA = "https://www.wikidata.org/wiki/Q"
    ENWIKI = "en.wikipedia.org/wiki/"
    SITE_NODE = "https://blog.dugong.live/#"

    ent_names = defaultdict(set)   # wikidata uri -> {name}
    ent_ids = defaultdict(set)     # name -> {wikidata uri}
    ent_wiki = defaultdict(set)    # name -> {wikipedia url}
    page_entities = {}             # page -> [(name, wikidata uri)] in order

    for name in rendered:
        for node in nodes(docs[name]):
            if not isinstance(node, dict):
                continue
            is_post = node.get("@type") in ("BlogPosting", "Article")
            for key in ("about", "mentions"):
                value = node.get(key)
                if value is None:
                    continue
                listed = value if isinstance(value, list) else [value]
                seen_here = {}
                for ent in listed:
                    if not isinstance(ent, dict):
                        continue
                    label = ent.get("name", "?")
                    same = ent.get("sameAs")
                    if isinstance(same, str):
                        same = [same]
                    elif not isinstance(same, list):
                        same = []
                    wd = next(
                        (u for u in same
                         if isinstance(u, str) and u.startswith(WIKIDATA)),
                        None,
                    )
                    wp = next(
                        (u for u in same if isinstance(u, str) and ENWIKI in u),
                        None,
                    )
                    # An entity with no Wikidata URI is already a finding of
                    # entity_no_wikidata / entity_no_sameas above, and the
                    # eight topic-guide self-names are deliberately bare, so
                    # there is nothing for this check to say about either.
                    if wd is None:
                        continue
                    if ent.get("@id") != wd:
                        fail(
                            "entity_without_id",
                            f"{name}: '{label}' @id is "
                            f"{ent.get('@id') or 'absent'}, want {wd}",
                        )
                    ent_names[wd].add(label)
                    ent_ids[label].add(wd)
                    if wp:
                        ent_wiki[label].add(wp)
                    if wd in seen_here:
                        fail(
                            "entity_duplicated_in_list",
                            f"{name}: {wd} is named twice in one {key} list, "
                            f"'{seen_here[wd]}' and '{label}'",
                        )
                    seen_here[wd] = label
                    if is_post and key == "about":
                        page_entities.setdefault(name, []).append((label, wd))

    # The three contradictions this pass resolved, each of which the site could
    # have settled from its own evidence and never did. Two names resolved to
    # two Wikidata items while pointing at ONE Wikipedia article, so at most
    # one id could be right: 'Order fulfillment' read Q1473552 on 21 pages and
    # Q7100318 on one, 'Pricing' read Q2516951 on six and Q2334719 on one.
    # 'Wholesale' read /Wholesaling twice, including in its own topic guide,
    # and /Wholesale once. And three pages each declared one Wikidata entity
    # TWICE under two names, so one of the four or five entities each of those
    # pages claimed to be about was a repeat of another.
    for wd, labels in sorted(ent_names.items()):
        if len(labels) > 1:
            fail(
                "entity_id_two_names",
                f"{wd} is named {sorted(labels)} on different pages",
            )
    for label, ids in sorted(ent_ids.items()):
        if len(ids) > 1:
            fail(
                "entity_name_two_ids",
                f"'{label}' resolves to {sorted(ids)} on different pages",
            )
    for label, urls in sorted(ent_wiki.items()):
        if len(urls) > 1:
            fail(
                "entity_name_two_wikipedia",
                f"'{label}' resolves to {sorted(urls)} on different pages",
            )

    # The grounding has to reach the two renditions the site tells a model to
    # read INSTEAD of the page: /md/<slug>.md, named in every page's
    # `rel=alternate`, and the llms-full.txt segment. Both carried none of it
    # until this pass, so the one audience 398 grounded nodes were written for
    # was reading the rendition without them. The line is generated from the
    # page's own JSON-LD, so this check is what keeps the three in step.
    def entity_diff(where, listed, ents):
        """Name the first entity that disagrees, not the first 80 characters.
        Two lists that differ at entity four read as identical when the detail
        line is truncated, which is how a check earns the reputation of being
        noise."""
        have = listed.split("; ") if listed else []
        wanted = [f"{n} ({u})" for n, u in ents]
        at = next(
            (i for i, (a, b) in enumerate(zip(have, wanted)) if a != b),
            min(len(have), len(wanted)),
        )
        mine = have[at] if at < len(have) else "(nothing)"
        theirs = wanted[at] if at < len(wanted) else "(nothing)"
        return (
            f"{where}: {len(have)} entities listed against {len(wanted)} on "
            f"the page; first difference at position {at + 1}, "
            f"{mine!r} where the page says {theirs!r}"
        )

    for name, ents in sorted(page_entities.items()):
        md_path = os.path.join("md", name[:-5] + ".md")
        if not os.path.exists(md_path):
            continue
        want = "- Entities: " + "; ".join(f"{n} ({u})" for n, u in ents)
        found = re.search(r"^- Entities: .*$", read(md_path), re.M)
        if not found:
            fail("md_without_entities", f"{md_path}: no '- Entities:' line")
        elif found.group(0) != want:
            fail("md_entities_mismatch", entity_diff(md_path, found.group(0)[12:], ents))

    for name, ents in sorted(page_entities.items()):
        head = f"URL: https://blog.dugong.live/{name}\n"
        at = llms_full.find(head)
        if at < 0:
            continue  # absence is llms_full_missing, reported above
        header = llms_full[at:].split("\n\n", 1)[0]
        want = "Entities: " + "; ".join(f"{n} ({u})" for n, u in ents)
        got = [ln for ln in header.split("\n") if ln.startswith("Entities: ")]
        if not got:
            fail(
                "llms_full_without_entities",
                f"{name}: segment header carries no Entities line",
            )
        elif got[0] != want:
            fail("llms_full_entities_mismatch", entity_diff(name, got[0][10:], ents))

    # llms.txt is the file a model reads first, and it documents what the site
    # has made addressable: the section anchors since 11-02, the question and
    # answer anchors since 11-04. The entity identifiers are the same kind of
    # fact and belong in the same place, or a model has to discover them.
    if os.path.exists("llms.txt") and "Entity identifiers:" not in read("llms.txt"):
        fail("llms_without_entity_note", "llms.txt: no 'Entity identifiers:' line")

    # 2026-11-17. One `@id`, one value per property. `#aanya-rao` read jobTitle
    # 'Head of Research' on index.html against 'Head of Research, Dugong' on
    # her own page and on her essay, and carried no `worksFor` there while the
    # other two definitions did. `#organization`'s logo carried the caption
    # 'Dugong' on 100 pages and no caption on the eight topic guides. A shared
    # node is restated on every page that uses it, which makes it the one part
    # of the graph that can disagree with itself, and nothing was reading it.
    # Only site-level nodes are compared: a page-scoped `@id` is covered by
    # page_node_date_drift and the date checks above.
    scalar_defs = defaultdict(lambda: defaultdict(set))
    scalar_where = defaultdict(lambda: defaultdict(set))

    def collect_defs(obj, page):
        if isinstance(obj, dict):
            ident = obj.get("@id")
            if isinstance(ident, str) and ident.startswith(SITE_NODE) and len(obj) > 1:
                for prop, value in obj.items():
                    if prop in ("@id", "@type"):
                        continue
                    if isinstance(value, (str, int, float, bool)):
                        scalar_defs[ident][prop].add(value)
                        scalar_where[ident][prop].add(page)
            for value in obj.values():
                collect_defs(value, page)
        elif isinstance(obj, list):
            for value in obj:
                collect_defs(value, page)

    for name in rendered:
        collect_defs(docs[name], name)
    for ident in sorted(scalar_defs):
        for prop, values in sorted(scalar_defs[ident].items()):
            if len(values) > 1:
                fail(
                    "node_definition_conflict",
                    f"{ident}: {prop} is {sorted(values)!r} across "
                    f"{len(scalar_where[ident][prop])} pages",
                )


    # 2026-11-19. Since 11-02 every section heading inside an article carries
    # an `id`, so any passage of any dispatch can be cited rather than the
    # whole 2,500-word page. The two renditions the site tells a model to read
    # INSTEAD of the page - /md/<slug>.md, named in every page's
    # `rel=alternate`, and the llms-full.txt segment - carried **876 `## `
    # headings between them and not one anchor**. The only route from the
    # rendition to a section address was the construction rule llms.txt states
    # in prose, and that rule was wrong on 37 of the site's 766 section
    # anchors because it did not say that apostrophes are dropped. So the one
    # audience the addresses were made for either could not use them or, worse,
    # followed the published rule and built a dead link. Exactly the shape of
    # the entity grounding before 11-17: the site made something addressable
    # and said so nowhere a machine reads.
    #
    # Both renditions now carry a `Section anchors:` line in the `Name (URL)`
    # format and `; `-separated shape the `- Entities:` line has used since
    # 11-17, generated from the page's own markup so the three cannot drift.
    def anchor_diff(where, listed, wanted):
        """Name the first heading that disagrees and where it sits. Two lists
        of eleven long URLs read as identical when a detail line is truncated,
        which is the 11-17 lesson and the reason this is not a bare equality
        message."""
        have = listed.split("; ") if listed else []
        at = next(
            (i for i, (a, b) in enumerate(zip(have, wanted)) if a != b),
            min(len(have), len(wanted)),
        )
        mine = have[at] if at < len(have) else "(nothing)"
        theirs = wanted[at] if at < len(wanted) else "(nothing)"
        return (
            f"{where}: {len(have)} section anchors listed against "
            f"{len(wanted)} headings in the rendition; first difference at "
            f"position {at + 1}, {mine!r} where the page says {theirs!r}"
        )

    for name in posts:
        md_path = os.path.join("md", name[:-5] + ".md")
        if not os.path.exists(md_path):
            continue  # absence is md_missing, reported above
        md_text = read(md_path)
        pairs, ids = section_anchor_pairs(read(name), md_text)
        for heading, anchor in pairs:
            if anchor is None:
                fail(
                    "section_heading_without_anchor",
                    f"{name}: rendition heading {heading!r} resolves to no id "
                    f"on the page, so it cannot be addressed",
                )
            elif anchor not in ids:
                fail(
                    "section_anchor_not_in_page",
                    f"{name}: #{anchor} is listed for {heading!r} and is not "
                    f"an id in the markup",
                )
        wanted = [f"{h} ({BASE}{name}#{a})" for h, a in pairs if a]
        if not wanted:
            continue

        found = re.search(r"^- Section anchors: (.*)$", md_text, re.M)
        if not found:
            fail(
                "md_without_section_anchors",
                f"{md_path}: no '- Section anchors:' line, so none of its "
                f"{len(wanted)} headings carries the address the page has",
            )
        elif found.group(1) != "; ".join(wanted):
            fail("md_section_anchors_mismatch", anchor_diff(md_path, found.group(1), wanted))

        head = f"URL: {BASE}{name}\n"
        at = llms_full.find(head)
        if at < 0:
            continue  # absence is llms_full_missing, reported above
        header = llms_full[at:].split("\n\n", 1)[0]
        got = [ln for ln in header.split("\n") if ln.startswith("Section anchors: ")]
        if not got:
            fail(
                "llms_full_without_section_anchors",
                f"{name}: segment header carries no Section anchors line",
            )
        elif got[0][17:] != "; ".join(wanted):
            fail("llms_full_section_anchors_mismatch", anchor_diff(name, got[0][17:], wanted))

    # The rule llms.txt publishes has to be the rule the site applies. It is
    # prose, so what is made executable here is its worked examples: every
    # `"heading" is `#anchor`` pair in the Section anchors paragraph is checked
    # against heading_slug and against the markup. A documented rule nothing
    # reads is how the apostrophe clause came to be missing for seventeen days.
    if os.path.exists("llms.txt"):
        llms = read("llms.txt")
        para = next(
            (ln for ln in llms.split("\n") if ln.startswith("Section anchors:")),
            "",
        )
        if not para:
            fail("llms_without_section_anchor_note", "llms.txt: no 'Section anchors:' line")
        else:
            examples = re.findall(r'"([^"]+)" is `#(h-[a-z0-9-]+)`', para)
            if not examples:
                fail(
                    "llms_anchor_rule_unexampled",
                    "llms.txt: the section anchor rule states no worked example, "
                    "so nothing checks that the published rule is the real one",
                )
            headings = {}
            for page in rendered:
                for attr, inner in re.findall(r"<h2([^>]*)>(.*?)</h2>", read(page), re.S):
                    got = re.search(r'id="([^"]+)"', attr)
                    if got:
                        plain = html_unescape(re.sub(r"<[^>]+>", "", inner))
                        headings.setdefault(re.sub(r"\s+", " ", plain).strip(), set()).add(got.group(1))
            for heading, anchor in examples:
                if heading not in headings:
                    fail(
                        "llms_anchor_rule_example_absent",
                        f"llms.txt gives {heading!r} as an example heading and no "
                        f"page carries a section heading with that text",
                    )
                elif heading_slug(heading) != anchor:
                    fail(
                        "llms_anchor_rule_example_wrong",
                        f"llms.txt says {heading!r} is #{anchor}; the rule the "
                        f"site applies gives #{heading_slug(heading)}",
                    )
                elif anchor not in headings[heading]:
                    fail(
                        "llms_anchor_rule_example_wrong",
                        f"llms.txt says {heading!r} is #{anchor}; the markup "
                        f"gives it {sorted(headings[heading])!r}",
                    )

    # 2026-11-19. The nine `CollectionPage` nodes are the site's eight topic
    # guides and its question index. Eight carry `headline` and it is the
    # node's own `name`; the question index carried none, so the one index
    # whose whole job is to be lifted question by question was the one
    # collection with no headline. A property eight of nine siblings carry is
    # a convention, and a convention nothing reads is the drift this file
    # exists to catch.
    for name in rendered:
        for node in nodes(docs[name]):
            if node.get("@type") != "CollectionPage" or len(node) < 3:
                continue
            if "headline" not in node:
                fail(
                    "collectionpage_without_headline",
                    f"{name}: CollectionPage {node.get('@id')} carries no headline",
                )
            elif node["headline"] != node.get("name"):
                fail(
                    "collectionpage_headline_not_name",
                    f"{name}: CollectionPage headline {node['headline']!r} "
                    f"against name {node.get('name')!r}",
                )

    # 2026-11-19. A shared site node is restated on every page that uses it,
    # and most of those restatements are deliberately partial: a dispatch
    # names `#priya-singh` with a name, a url and a job title and that is
    # correct. A restatement that carries the person's biography is not
    # partial, it is a full copy, and a full copy that drops a property is a
    # thinner node for any consumer that reads only that page. `#priya-singh`
    # on index.html carried her description, her employer and her expertise
    # and **not `mainEntityOfPage`**, which her own page has always asserted.
    # node_definition_conflict, added 11-17, compares scalars and so reads a
    # missing reference as an absence rather than a disagreement; this is the
    # half of that check which was missing. Only Person nodes are read,
    # because a Person's `url` names a page in this repository and so there is
    # always an unarguable canonical definition to compare against.
    person_defs = defaultdict(dict)
    for name in rendered:
        for node in nodes(docs[name]):
            ident = node.get("@id")
            if node.get("@type") != "Person" or not isinstance(ident, str) or len(node) < 3:
                continue
            person_defs[ident][name] = node
    for ident in sorted(person_defs):
        where = person_defs[ident]
        home = next(
            (n for n, node in where.items()
             if isinstance(node.get("url"), str) and node["url"].rsplit("/", 1)[-1] == n),
            None,
        )
        if home is None:
            continue
        full = set(where[home]) - {"@id", "@type"}
        for name, node in sorted(where.items()):
            if name == home or "description" not in node:
                continue
            missing = sorted(full - set(node))
            if missing:
                fail(
                    "person_restatement_incomplete",
                    f"{name}: {ident} restates the full node and omits "
                    f"{missing!r}, which {home} asserts",
                )

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
