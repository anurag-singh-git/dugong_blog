# SEO / GEO report — 2026-06-25 (audit pass)

**Scope:** blog.dugong.live — index + 21 posts + feed / sitemap / llms / robots / CNAME
**Mode:** automated scheduled run (autonomous, no user present)

## Result: closed the link-graph asymmetry left open by today's publish

This morning's blog run shipped Dispatch Nº 68 ("The deleted product that 404s your customers") and wired
it into the homepage, sitemap, feed, llms.txt, and JSON-LD, plus two inbound back-links from the most
topically related siblings (meta-description and image-alt-text). The morning report explicitly left the
rest of the back-link propagation as a follow-up. That left the new post under-linked: every other post had
an internal in-degree of 20, while Nº 68 sat at 2. An orphaned-but-listed page is the kind of weak signal
that suppresses a post in both classic crawl-based ranking and answer-engine retrieval, so this run
completed the propagation.

## Defect: new post Nº 68 was under-linked (in-degree 2 vs 20 everywhere else)

The site's standing invariant is a complete, uniform internal-link graph: every post's "Read next"
`.related-grid` carries a card for all other siblings, so in-degree is uniform across every post. With 21
posts now on disk, that uniform value is 20. After this morning's publish, 18 of the older posts still did
not carry a card for Nº 68, so the new post was reachable from index, sitemap, feed, llms.txt and JSON-LD
but from only 2 of its 20 siblings.

**Fix:** inserted one back-link card for Nº 68 as the first card in the `.related-grid` of all 18 posts
that were missing it (every post except the two already done — meta-description and image-alt-text — and
the new post itself). The card mirrors the existing canonical markup exactly (`tag-research`, "9 min",
JUN 25, P. Singh) and uses the post's own meta description as the dek so it reads correctly on every page.
No dashes introduced, consistent with the house style preference. Net effect: 18 files changed, one
`<a ... class="card">` block (16 lines) added to each as a pure insertion, no other lines touched.

## Verification (post-fix re-sweep)

- **Link graph now uniform:** in-degree is 20 for all 21 posts (was: twenty posts at 20, Nº 68 at 2).
  Nº 68 in-degree is now 20. Each edited post's `.related-grid` now carries 20 cards.
- **Insertions only:** `git diff --numstat` shows 0 deletions on every edited post; the single Nº 68 card
  was added as the first grid card (the adjacent Nº 67 card visible in the diff is yesterday's still-staged
  audit work, not a regression — HEAD predates both runs).
- **Structure intact:** `<div>`/`</div>` balanced on all 21 posts; no imbalance anywhere.
- **JSON-LD:** parses on all 21 posts and on index.html (edits were in the article body, not in any
  schema block).
- **XML validity:** sitemap.xml and feed.xml both parse as valid XML.
- **No dash regressions:** the 18 inserted cards contain zero em/en dashes. (Pre-existing em dashes live
  only in the `<title>` brand suffix, the RSS `<title>`, and CSS comments — untouched template, not body.)

## Site-wide audit (everything else clean)

- **Post count:** 21 posts on disk (20 June dispatches + the 2026-05-28 pillar essay).
- **Counters consistent:** homepage ticker "20 NEW DISPATCHES THIS MONTH" x2 matches the 20 posts with a
  June 2026 `datePublished`; hero "ISSUE Nº 68" and archive "browse all 68 dispatches" both agree with the
  newest post.
- **Coverage cross-check** (disk vs sitemap vs feed vs llms vs index): all five sets identical, 21 posts,
  zero drift.
- **Meta descriptions:** all 21 unique, all inside the 146–162 house band.
- **Titles:** all 21 unique. **H1:** exactly one per post (21/21).
- **Canonical:** present on every post (21/21).
- **OG / Twitter cards:** twitter:card present on every post (21/21).
- **Image alt text:** no `<img>` missing an alt attribute across posts or index.
- **robots.txt / discovery assets:** Sitemap line present; og-image.png, favicon.png, favicon.svg,
  apple-touch-icon.png all present; CNAME = blog.dugong.live.

## Reviewed and intentionally not changed

- **feed lastBuildDate / sitemap lastmod:** left as set by this morning's blog run. No article body
  changed beyond adding a navigation card, so the freshness timestamps already reflect the real 06-25
  publish; touching them again would add no signal.
- **dateModified across posts:** untouched. Adding a "Read next" card is navigation wiring, not a content
  edit; bumping every post's dateModified would send a misleading site-wide "21 posts updated today"
  freshness signal to crawlers and answer engines.

## Recommendation

This is now the fourth-plus consecutive run where the same root cause surfaces: a new post ships and its
sibling back-link set is not fully propagated at publish time, leaving the new post under-linked until the
next day's audit. The publish pipeline already updates the hero Nº, the dispatch stat, the archive
"browse all N" link, and the ticker. The remaining gap is back-link propagation. Automating one insertion
at publish time — a card for the new post into every existing post's `.related-grid` in the same step —
would keep the link graph uniform on day zero and retire this recurring class of finding.

## Note

All changes are staged in the working tree only; no git commit or deploy performed, consistent with prior
runs.
