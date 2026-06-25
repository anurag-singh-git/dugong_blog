# SEO / GEO report — 2026-06-24

**Scope:** blog.dugong.live — index + 20 posts + feed / sitemap / llms / robots / CNAME
**Mode:** automated scheduled run (autonomous, no user present)

## Result: closed the link-graph asymmetry left open by today's publish

Today's blog run shipped Dispatch Nº 67 ("The unpaid order that never cancels itself") and wired it into
the homepage, sitemap, feed, llms.txt, and JSON-LD, and back-linked it from the two most topically related
siblings (overselling and restock-alert). It explicitly left the rest of the back-link propagation as an
open item. That left the new post under-linked: every other post had an internal in-degree of 19, while
Nº 67 sat at 2. An orphaned-but-listed page is exactly the kind of weak signal that suppresses a post in
both classic crawl-based ranking and answer-engine retrieval, so this run completed the propagation.

## Defect: new post Nº 67 was under-linked (in-degree 2 vs 19 everywhere else)

The site's standing invariant is a complete, uniform internal-link graph: every post's "Read next"
`.related-grid` carries a card for all 19 siblings, so in-degree is 19 across every post. After the 06-24
publish, 17 of the older posts still did not carry a card for Nº 67, so the new post was reachable from
index, sitemap, feed, llms.txt and JSON-LD but from only 2 of its 19 siblings.

**Fix:** inserted one back-link card for Nº 67 as the first card in the `.related-grid` of all 17 posts
that were missing it (every post except the two already done — overselling and restock-alert — and the new
post itself). The card mirrors the existing markup exactly (`tag-research`, "9 min", JUN 24, P. Singh) and
uses the post's own meta description as the dek so it reads correctly on every page. No dashes introduced,
consistent with the house style preference. Net effect: 17 files changed, one `<a class="card">` block
added to each, no other lines touched.

## Verification (post-fix re-sweep)

- **Link graph now uniform:** in-degree is 19 for all 20 posts (was: nineteen posts at 19, Nº 67 at 2).
  Nº 67 in-degree is now 19. Each edited post's `.related-grid` went from 18 cards to 19.
- **Structure intact:** `<div>`/`</div>` balanced on all 17 edited files; no imbalance anywhere.
- **JSON-LD:** parses on all 20 posts and on index.html (edits were in the article body, not in any
  schema block).
- **XML validity:** sitemap.xml and feed.xml both parse as valid XML.
- **No dash regressions:** the 17 inserted cards contain zero em/en dashes.

## Site-wide audit (everything else clean)

- **Post count:** 20 posts on disk (19 June dispatches + the 2026-05-28 pillar essay).
- **Counters consistent:** homepage ticker "19 NEW DISPATCHES THIS MONTH" x2 matches the 19 posts with a
  June 2026 `datePublished`; hero "ISSUE Nº 67", "browse all 67 dispatches", and hero date "JUN 24 · 2026"
  all agree with the newest post.
- **Coverage cross-check** (disk vs sitemap vs feed vs llms): all four sets identical, 20 posts, zero
  drift. sitemap and feed each carry 21 entries (20 posts + homepage / lead essay).
- **Meta descriptions:** all 20 unique, all inside the 146–162 house band.
- **Titles:** all 20 unique. **H1:** exactly one per post (20/20).
- **Canonical:** present on every post (20/20).
- **OG / Twitter cards:** twitter:card plus og:image:alt and twitter:image:alt present on every post
  (20/20).
- **Image alt text:** no `<img>` missing an alt attribute.
- **robots.txt:** `Sitemap:` line present and correct.
- **Discovery assets:** og-image.png, favicon.png, favicon.svg, apple-touch-icon.png all present; CNAME =
  blog.dugong.live.

## Reviewed and intentionally not changed

- **feed lastBuildDate (Wed, 24 Jun 2026) and sitemap lastmod:** left as set by today's blog run. No
  article body changed today beyond adding a navigation card, so the freshness timestamps already reflect
  the real 06-24 publish; touching them again would add no signal.
- **dateModified across posts:** untouched. Adding a "Read next" card is navigation wiring, not a content
  edit, so bumping every post's dateModified would send a misleading site-wide "20 posts updated today"
  freshness signal to crawlers and answer engines. The link-graph completion is the correct fix; a
  dateModified bump is not warranted.
- **Static "DISPATCH OF THE WEEK" / "NEW THIS WEEK" decorative copy:** left as-is, consistent with prior
  runs (phrasing, not a numeric claim).

## Recommendation

This is the third consecutive run where the same root cause surfaced: a new post ships and a secondary
surface is not propagated at publish time (06-21 meta-length gate, 06-22 related-grid, 06-23 ticker, and
now 06-24 the full sibling back-link set). The publish pipeline already updates the hero Nº, the dispatch
stat, the archive "browse all N" link, and now the ticker. The remaining gap is back-link propagation:
when a post is published, a card for it should be inserted into every existing post's `.related-grid` in
the same step, not left to the next day's audit. Automating that one insertion at publish time would keep
the link graph uniform on day zero and retire this recurring class of finding.

## Note

All changes are staged in the working tree only; no git commit or deploy performed, consistent with prior
runs.
