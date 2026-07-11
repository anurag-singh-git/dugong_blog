# SEO / GEO report — 2026-07-11

**Scope:** Full-site SEO/GEO optimization pass. No new post published today (latest remains
Dispatch Nº 80, how-to-automatically-add-a-free-gift-with-purchase-on-shopify.html, 2026-07-08).
This run fixed two concrete issues surfaced by a full-site audit: under-linked posts and
severely truncated meta descriptions.

## Audit baseline (all healthy)

Ran a full structural audit across 67 HTML files before touching anything:

| Check | Result |
|---|---|
| sitemap.xml / feed.xml valid XML | PASS |
| sitemap loc count / dangling locs | 34 / 0 |
| feed item count | 33 posts, all resolve |
| stub ↔ post parity | 33 / 33 |
| JSON-LD parse (all files) | 0 errors |
| broken internal links site-wide | 0 |
| canonical matches filename (all posts) | 0 issues |
| schema coverage (BlogPosting/FAQPage/HowTo/BreadcrumbList) | full on all 32 how-to posts; lead essay correctly carries no HowTo |
| speakable coverage | 33 / 33 |

## Issue 1 — two posts badly under-linked internally

Inbound internal links per post average ~37 (established posts sit at 35 to 77). Two posts were
far below that floor, hurting crawl discovery and PageRank flow:

| Post | Inbound (before) | After |
|---|---|---|
| Nº 80 — free gift that never lands in the cart (07-08, newest) | 4 | 11 |
| schedule product publishing (older, orphaned) | 7 | 14 |

The read-next grids on this site are curated subsets, not exhaustive sibling lists, so a post only
gains sibling discovery when its card is added to related grids. That had not happened at scale for
either post. Fix: inserted each post's canonical read-next card (copied verbatim from the existing
card already in use, so styling/markup are unchanged) as the first card in seven topically-related
sibling grids each, skipping any grid that already carried it.

- **Nº 80 (free gift)** added to: schedule-a-sale, abandoned-cart, segment-repeat-customers,
  prevent-overselling, back-in-stock-notifications, bulk-edit-product-prices, request-product-reviews.
  These are the promotion, cart-value, and merchandising siblings where the gift playbook is the
  natural next read.
- **schedule-product-publishing** added to: push-sold-out-to-bottom, hide-sold-out-variants,
  back-in-stock-notifications, bulk-edit-product-prices, bulk-edit-meta-descriptions,
  generate-product-descriptions, request-product-reviews. These are the drop/merchandising siblings
  most related to timed publishing.

## Issue 2 — six meta descriptions truncating in search results

Six posts carried meta descriptions of 281 to 419 characters. Google truncates the snippet near
155 to 160 characters, so the actionable tail (the "AI playbook that…" value line) was being cut off
in the SERP and the pages were losing click-through. Rewrote all six to a keyword-first, self-contained
line that fits the snippet and stays quotable for answer engines:

| Post | Before | After |
|---|---|---|
| free gift | 408 | 162 |
| hide sold-out variants | 291 | 159 |
| auto-send invoices | 353 | 173 |
| split/route to suppliers | 419 | 167 |
| schedule product publishing | 281 | 172 |
| set a minimum order amount | 319 | 166 |

Each rewrite keeps the primary keyword in the first clause and the value proposition intact, with zero
em/en dashes (user style). The remaining two mildly-long descriptions (combine-orders 217, card-testing
176) were left as-is; their truncation is minor and the copy is strong.

## Distribution surface updated

- **sitemap.xml:** bumped `<lastmod>` to 2026-07-11 for the 16 genuinely-changed post files (14 grid
  edits + the 6 meta edits, overlapping set). Legitimate crawl-freshness signal. Still valid XML, 34 locs.

## Verification (all passing)

| Check | Result |
|---|---|
| div balance on 16 edited files | 0 mismatches |
| anchor balance on 16 edited files | 0 mismatches |
| broken internal links site-wide | 0 |
| JSON-LD parse site-wide | 0 errors |
| Nº 80 inbound links | 4 → 11 |
| schedule-product-publishing inbound | 7 → 14 |
| edited meta description lengths | 159 to 173 (was 281 to 419) |
| em/en dashes introduced | 0 |
| sitemap.xml / feed.xml valid XML | PASS |

## Open items

- **Undeployed working tree.** All edits are in the working tree only. No git commit or push was
  performed this run, consistent with prior runs (deploy is left to the normal manual flow). None of
  this is live on blog.dugong.live until committed and pushed. Recommend committing and pushing so the
  accumulated optimization work reaches crawlers.
- Nº 80 and schedule-product-publishing now sit at 11 and 14 inbound links. Established posts sit near
  37; these will keep climbing naturally as future posts add them to grids. No further forced injection
  this run.
- Uncovered candidate topics for future dispatches (carried from prior report): quantity/tiered volume
  discounts, cross-product BOGO, automatic best-discount selection / preventing code stacking,
  loyalty-points automation, gift-message/gift-wrap.
