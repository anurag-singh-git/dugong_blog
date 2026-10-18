#!/usr/bin/env python3
"""QA pass 2026-10-18 for blog.dugong.live. Run from the repository root."""
import re, glob, html, os, sys, json

DRY = "--dry" in sys.argv
changes = {}
def write(f, old, new):
    if old == new: return False
    changes[f] = changes.get(f, 0) + 1
    if not DRY: open(f, "w", encoding="utf-8").write(new)
    return True

pages = []
for f in sorted(glob.glob("*.html")):
    s = open(f, encoding="utf-8").read()
    if 'http-equiv="refresh"' in s: continue
    pages.append(f)

meta = {}
dispatch = {}
for f in pages:
    s = open(f, encoding="utf-8").read()
    m = re.search(r'<meta name="description" content="([^"]*)"', s)
    if m: meta[f] = " ".join(html.unescape(m.group(1)).split())
    m = re.search(r'article:published_time" content="([0-9-]+)"', s)
    if m: dispatch[f] = m.group(1)

log = lambda *a: print(*a)

# ---------------------------------------------------------------- F1
# card-dek longer than 45 words is truncated by the 5-line clamp. The site's
# own convention (every hub page) is dek == the target page's meta description.
def fix_deks(f, s):
    out, pos, changed = [], 0, 0
    pat = re.compile(r'<p class="card-dek">(\n(\s*))(.*?)\n\s*</p>', re.S)
    anchor = re.compile(r'<a\b[^>]*>')
    for m in pat.finditer(s):
        body = m.group(3)
        txt = " ".join(html.unescape(re.sub(r"<[^>]+>", "", body)).split())
        if len(txt.split()) <= 45:
            continue
        # nearest preceding <a ...> tag that is a card link
        href = None
        for am in anchor.finditer(s, max(0, m.start() - 4000), m.start()):
            tag = am.group(0)
            if 'class="card' in tag or "card-tall" in tag or "card-wide" in tag:
                h = re.search(r'href="([a-z0-9-]+\.html)"', tag)
                if h: href = h.group(1)
        if not href or href not in meta:
            continue
        new_body = html.escape(meta[href], quote=False)
        out.append(s[pos:m.start(3)])
        out.append(new_body)
        pos = m.end(3)
        changed += 1
    if not changed:
        return s
    out.append(s[pos:])
    return "".join(out)

# ---------------------------------------------------------------- F3
STALE = {}  # superseded by fix_stale_meta.py, which recomputes from the pages themselves
def fix_stale(f, s):
    for old, new in STALE.get(f, []):
        s = s.replace(old, new)
    return s

# ---------------------------------------------------------------- F4/F5/F6
CSS_BLOCK = """
/* QA-2026-10-18-CSS
   QA 2026-10-18: 24px minimum target size at every width, not only phones.
   The 2026-10-10 pass put this inside @media (max-width:560px), so header and
   footer links stayed at 23.2-23.5px on tablet and desktop. */
.nav-links a:not(.nav-cta), .foot-cols a, .foot-bot a {
  display: inline-flex; align-items: center; min-height: 24px;
}

/* QA 2026-10-18: the header nav used to vanish below 820px with nothing in its
   place, so phone and tablet readers had no way back to Latest, Topics or the
   Archive. Wrap it onto a second row instead of hiding it. */
@media (max-width: 820px) {
  .nav { flex-wrap: wrap; padding-top: 0.55rem; padding-bottom: 0.55rem; row-gap: 0.1rem; }
  .brand { order: 1; }
  .nav-cta { order: 2; margin-left: auto; }
  .nav-links { order: 3; width: 100%; gap: 1.5rem; justify-content: flex-start;
               font-size: 13.5px; padding-bottom: 0.1rem; }
  .nav-links a:not(.nav-cta) { display: inline-flex; }
}
@media (max-width: 380px) { .nav-links { gap: 1.1rem; font-size: 13px; } }

/* QA 2026-10-18: long API identifiers in deks and FAQ answers must break
   rather than widen the page. Added 2026-10-13 to 5 pages only. */
.faq-a, .article-dek, .card-dek { overflow-wrap: anywhere; }

/* QA 2026-10-18: READ NEXT had grown to 79 cards on the oldest dispatches,
   ~28,000px of card grid on a phone. The overflow now sits behind a
   disclosure, so every link is still in the page and crawlable. */
.related-more { max-width: var(--maxw); margin: 1.5rem auto 0; }
.related-more > summary {
  font-family: var(--mono); font-size: 0.78rem; letter-spacing: 0.08em;
  text-transform: uppercase; color: var(--text-dim); cursor: pointer;
  display: inline-flex; align-items: center; gap: 0.5rem; min-height: 24px;
  padding: 0.4rem 0.9rem; border: 1px solid var(--border-strong); border-radius: 999px;
  list-style: none; transition: color .2s, border-color .2s, background .2s;
}
.related-more > summary::-webkit-details-marker { display: none; }
.related-more > summary::after { content: "\\002B"; font-size: 1rem; line-height: 1; }
.related-more[open] > summary::after { content: "\\2212"; }
.related-more > summary:hover { color: var(--text); border-color: var(--text); background: var(--surface); }
.related-more > .related-grid { margin-top: 1.5rem; }
/* cards inside a closed disclosure never meet the IntersectionObserver that
   clears .reveal, so they would open at opacity 0. */
.related-more .reveal { opacity: 1; transform: none; }
"""

OLD_HIDE = "@media (max-width: 820px) { .nav-links a:not(.nav-cta) { display: none; } }"

def fix_css(f, s):
    if "QA-2026-10-18-CSS" in s: return s
    if OLD_HIDE in s:
        s = s.replace(OLD_HIDE, "/* superseded by the QA 2026-10-18 wrapping nav below */")
    # drop the now-duplicated 10-13 single-page rule so it is not declared twice
    s = s.replace("\n\n/* 2026-10-13 long API identifiers in FAQ answers must break rather than widen the page */\n"
                  ".faq-a, .article-dek, .card-dek { overflow-wrap: anywhere; }", "")
    i = s.rfind("</style>")
    if i == -1: return s
    return s[:i] + CSS_BLOCK + s[i:]

# ---------------------------------------------------------------- F7
def fix_hero_em(f, s):
    old = """.hero-title em { font-style: normal; position: relative; white-space: nowrap; color: var(--text); }
.hero-title em::after {
  content: ""; position: absolute; left: -.06em; right: -.06em; bottom: .08em;
  height: .34em; background: var(--lime); z-index: -1; border-radius: 3px; transform: rotate(-.6deg);
}"""
    new = """/* QA 2026-10-18: the absolutely positioned bar sat under the descenders
   instead of through the word. Same gradient treatment as .article-title em. */
.hero-title em { font-style: normal; position: relative; color: var(--text);
  background: linear-gradient(transparent 57%, var(--lime) 57%, var(--lime) 81%, transparent 81%);
  -webkit-box-decoration-break: clone; box-decoration-break: clone; }
.hero-title em::after { content: none; }"""
    return s.replace(old, new)

def fix_title_highlight(f, s):
    """The marker band was drawn from 62% to 96% of the inline box. Hanken
    Grotesk puts the baseline at 77% of that box, so the band sat almost
    entirely below the letters and read as a thick underline sliding off the
    text. 57%-81% runs through the lower half of the glyphs instead."""
    return s.replace(
      "linear-gradient(transparent 62%, var(--lime) 62%, var(--lime) 96%, transparent 96%)",
      "linear-gradient(transparent 57%, var(--lime) 57%, var(--lime) 81%, transparent 81%)")

# ---------------------------------------------------------------- F8
KEEP = 6
def split_cards(seg):
    out, i = [], 0
    while True:
        m = re.compile(r'<a href="[a-z0-9-]+\.html" class="card">').search(seg, i)
        if not m: break
        depth, j = 1, m.end()
        while depth and j < len(seg):
            nxt = re.compile(r'<a\b|</a>').search(seg, j)
            if not nxt: break
            depth += 1 if nxt.group(0) == "<a" else -1
            j = nxt.end()
        out.append((m.start(), j))
        i = j
    return out

def fix_related(f, s):
    m = re.search(r'<section class="related">(.*?)\n</section>', s, re.S)
    if not m: return s
    sec = m.group(0)
    gm = re.search(r'(<div class="related-grid">)(.*?)(\n  </div>)', sec, re.S)
    if not gm: return s
    inner = gm.group(2)
    spans = split_cards(inner)
    if len(spans) <= KEEP + 2: return s
    head = inner[:spans[KEEP][0]].rstrip("\n")
    rest = inner[spans[KEEP][0]:]
    n = len(spans) - KEEP
    new_grid = (gm.group(1) + head + "\n  </div>\n"
        f'  <details class="related-more">\n'
        f'    <summary>{n} more dispatches in the archive</summary>\n'
        f'    <div class="related-grid">{rest}</div>\n'
        f'  </details>')
    return s.replace(sec, sec.replace(gm.group(0), new_grid), 1)

# ---------------------------------------------------------------- F9
FOOT_OLD = """        <a href="index.html">Latest</a>
        <a href="index.html">Essays</a>
        <a href="index.html">Post-mortems</a>
        <a href="index.html">Interviews</a>"""
FOOT_NEW = """        <a href="index.html#latest">Latest</a>
        <a href="index.html#essays">Essays</a>
        <a href="index.html#post-mortems">Post-mortems</a>
        <a href="index.html#interviews">Interviews</a>"""
def fix_footer_links(f, s):
    if f == "index.html": return s
    return s.replace(FOOT_OLD, FOOT_NEW)

def fix_index_filter_ids(f, s):
    if f != "index.html": return s
    for tag, anchor in [("tag-essay", "essays"), ("tag-postmortem", "post-mortems"), ("tag-interview", "interviews")]:
        s = s.replace(f'<button type="button" class="pill" data-filter="{tag}"',
                      f'<button type="button" id="{anchor}" class="pill" data-filter="{tag}"')
    hook = """document.querySelectorAll("[data-filter-link]").forEach((link) => {"""
    add = """// QA-2026-10-18-JS
// QA 2026-10-18: footer links on the dispatch pages arrive as #essays,
// #post-mortems or #interviews; pre-select the matching filter on load.
(() => {
  const byHash = { "#essays": "tag-essay", "#post-mortems": "tag-postmortem", "#interviews": "tag-interview" };
  const applyHash = () => { const t = byHash[location.hash]; if (t) applyFilter(t); };
  applyHash();
  window.addEventListener("hashchange", applyHash);
})();

"""
    if "QA-2026-10-18-JS" not in s and hook in s:
        s = s.replace(hook, add + hook, 1)
    return s

# ---------------------------------------------------------------- F10
def fix_copy(f, s):
    return s.replace("to its pre sale count", "to its pre-sale count")

# ---------------------------------------------------------------- run
FIXES = [("deks", fix_deks), ("stale", fix_stale), ("hero", fix_hero_em),
         ("highlight", fix_title_highlight),
         ("related", fix_related), ("footer", fix_footer_links),
         ("indexfilter", fix_index_filter_ids), ("copy", fix_copy), ("css", fix_css)]
tally = {k: 0 for k, _ in FIXES}
for f in pages:
    orig = open(f, encoding="utf-8").read()
    s = orig
    for name, fn in FIXES:
        before = s
        s = fn(f, s)
        if s != before: tally[name] += 1
    if s != orig: write(f, orig, s)
log("files changed:", len(changes))
log("by fix:", json.dumps(tally))
