# SEO / GEO report — 2026-06-22

**Scope:** blog.dugong.live — index + 18 posts + feed / sitemap / llms / robots / CNAME
**Mode:** automated scheduled run (autonomous, no user present)

## Result: one real defect found and fixed — newest post was under-linked

The internal-link graph had broken when Dispatch Nº 65 ("The repeat customer your store treats
like a stranger") published on 2026-06-21. The new post linked out to all 17 older posts, but only
3 of those older posts were updated to link back to it. The other 15 never got a related-grid card
for Nº 65, so the newest post sat at in-degree 3 while every other post was at 18. That under-links
the freshest, most important page for both crawlers (link equity) and answer engines (a post almost
nothing references reads as low-authority).

## Defect: incomplete related-grid propagation for Nº 65

Every post carries a `.related-grid` of `<a class="card">` tiles, one per other post, newest first,
forming a complete link graph across the catalogue. When Nº 65 shipped, the publish step added its
card to only `index.html`, `the-abandoned-cart-that-gets-one-email.html`, and
`the-order-tag-you-set-by-hand.html`. The remaining 15 posts still had 16 cards instead of 17.

**Fix:** inserted the canonical Nº 65 card at grid position 0 (newest-first, matching the two posts
that already had it) in all 15 missing posts:

- the-bad-address-that-ships-anyway.html
- the-chargeback-you-lose-by-default.html
- the-high-risk-flag-that-makes-you-guess.html
- the-image-alt-text-no-one-writes.html
- the-meta-description-you-write-one-at-a-time.html
- the-order-change-that-races-your-warehouse.html
- the-overselling-problem-no-one-automates.html
- the-product-descriptions-youll-never-finish-writing.html
- the-reorder-you-always-make-too-late.html
- the-restock-alert-that-never-fires.html
- the-return-that-wont-approve-itself.html
- the-sale-you-start-by-hand.html
- the-shopify-automations-no-one-builds.html
- the-sold-out-products-that-sink-your-collection.html
- the-wismo-tickets-that-eat-your-afternoon.html

The inserted card reuses the exact markup, dek, tag, read-time, and dateline already live in the
correct posts, so no copy drift was introduced. Each edit was applied with a single-anchor guard
(`<div class="related-grid">`, verified to occur exactly once per file) and skipped on any post that
already carried the card.

## Verification (post-fix re-sweep)

- **Related-grid cards:** 17 on every post (18/18), up from 16 on the 15 patched files.
- **Internal-link graph:** in-degree now uniform at 18 across all posts (17 sibling posts + the
  homepage). Nº 65 went from 3 to 18. Distribution collapsed to a single value, i.e. a complete graph.
- **Broken links:** 0 relative internal links broken across all 19 pages.
- **Structure intact:** `<div>` open/close balance 79/79 on every patched file; JSON-LD still parses
  on all 19 pages; no duplicate ids introduced.
- **Discovery surfaces unaffected:** sitemap.xml, feed.xml, and llms.txt each still cover exactly the
  18 posts on disk, zero drift; robots.txt sitemap line intact.
- **Diff:** 15 files changed, 240 insertions, 0 deletions (15 × the 16-line card block). No other lines
  touched.

## Site-wide audit (everything else clean)

- **Coverage cross-check** (disk vs sitemap vs feed vs llms): all four sets identical, 18 posts, zero drift.
- **Meta descriptions:** all 18 unique, all inside the 146–162 house band.
- **Titles:** unique across the catalogue.
- **H1:** exactly one per post (18/18).
- **Canonical:** present, self-referential, HTTPS, equal to og:url on every post.
- **OG / Twitter cards:** present on every post, including og:image:alt and twitter:image:alt (18/18).
- **JSON-LD:** parses on all 19 pages; posts carry BlogPosting + BreadcrumbList + FAQPage + HowTo
  (pillar post intentionally omits HowTo, correct for an overview piece); index carries WebSite +
  Organization + Blog.
- **Image alt text:** no `<img>` missing an alt attribute.
- **Em / en dashes:** body copy clean on all 18 posts (7 template em-dashes each, 0 en-dashes),
  confirming the prior legacy-post cleanup held.
- **Dates:** datePublished and dateModified present and sensible on every post; dateModified >=
  datePublished holds everywhere.
- **Feed:** valid XML, lastBuildDate present, pubDates descending.
- **Index cross-surface:** hero Nº 65 and "browse all 65" agree with the highest dispatch number; the
  Nº 47 references are the pinned lead essay by design, not a count discrepancy.
- **Discovery assets:** og-image.png, favicon.png, favicon.svg, apple-touch-icon.png all present.

## Reviewed and intentionally not changed

- **dateModified on the 15 patched posts** was left as-is. The related-grid is navigation chrome, not
  authored article body, so refreshing it is not an article-content update; bumping dateModified would
  send a misleading freshness signal to crawlers. This matches the conservative metadata approach of
  prior runs.
- **wordCount metadata** is author-declared and approximate; left untouched, consistent with baseline.

## Recommendation

The publish pipeline added the new post's related-grid card to only 3 of 18 surfaces on 2026-06-21,
which is the same class of "shipped but reported as complete" gap flagged on 06-21 for the meta-length
gate. Worth adding a post-publish assertion to the pipeline: after a new dispatch ships, confirm its
slug appears in the related-grid of every other post (target in-degree = N-1 across the catalogue)
before the run is considered done. That would catch incomplete graph propagation at publish instead of
in the next day's audit.

## Note

Changes staged in the working tree only; no git commit or deploy performed, consistent with prior runs.
