# SEO / GEO report — 2026-07-08

**Scope:** Full-site SEO/GEO optimization pass. No new post published today (latest is
Dispatch Nº 79, how-to-automatically-split-and-route-shopify-orders-to-multiple-suppliers.html,
2026-07-07). This run focused on fixing an internal-linking gap that was leaving the two newest
posts badly under-linked.

## Headline finding — newest posts were internally orphaned

Established posts receive ~30 inbound internal links from sibling read-next grids. The two most
recent posts had almost none:

| Post | Inbound internal links (before) | After |
|---|---|---|
| Nº 79 — split & route orders to suppliers (07-07) | 1 | 8 |
| Nº 78 — auto-send invoices (07-06) | 2 | 9 |

The read-next grids on this site are curated ~26-card subsets, not exhaustive sibling lists, so a
new post only becomes discoverable through siblings when those grids are updated. That update had
not happened for Nº 78 or Nº 79. Low internal inbound linking hurts crawl discovery, dilutes
PageRank flow to the newest content, and reduces the odds an answer engine surfaces the pages. Note:
prior reports described "reverse back-links" for these posts, but those were single read-next grid
cards (one each), not the broader cross-linking established posts enjoy.

## Fixes applied

Added each newest post's read-next grid card to the 7 most topically-related siblings (skipping any
that already carried it):

- **Nº 79 (split & route)** added to: combine-orders, pre-orders, reorder-points, prevent-overselling,
  tag-orders, wismo-tickets, edit-order. These are the order-level and fulfilment-routing siblings
  where a reader is most likely to want the multi-supplier routing playbook next.
- **Nº 78 (invoices)** added to: tag-orders, segment-repeat-customers, combine-orders, edit-order,
  cancel-unpaid, minimum-order-amount, chargeback-disputes. These are the order-metadata and
  B2B/finance siblings where the invoicing playbook is the natural next read.

Card markup was copied verbatim from the canonical cards already in use (identical tag class, read
time, dek, date, author), so styling and layout are unchanged. Cards were inserted as the first card
in each grid to favour freshness/discovery.

Also bumped `sitemap.xml` `<lastmod>` to 2026-07-08 for the 11 edited posts (they genuinely changed
today) as a legitimate crawl-freshness signal. sitemap remains valid XML.

## Verification

| Check | Result |
|---|---|
| HTML tag balance (div/anchor) on all 11 edited files | balanced, 0 mismatch |
| JSON-LD parse, site-wide (65 HTML files) | 0 errors |
| Broken internal links, site-wide | 0 |
| sitemap.xml / feed.xml valid XML | PASS |
| sitemap URL count | 33 (homepage + 32 posts) |
| feed item count | 33, newest = split-route, pubDate Tue 07 Jul 2026 |
| stub ↔ post parity | 32 posts / 32 stubs, 0 dupes, all targets exist |
| canonical matches filename (all main posts) | PASS |
| em/en dashes in inserted content | 0 |
| index.html hero / counters | ISSUE Nº 79 · browse all 79 · 7 NEW DISPATCHES THIS MONTH (matches 7 July feed items) |
| llms.txt coverage | newest post present, 31 how-to links |

## Carried / open items

- **Undeployed working tree (important).** The 07-06 and 07-07 work — including the Nº 78 and Nº 79
  posts themselves, plus index.html, sitemap.xml, feed.xml and llms.txt — is uncommitted in the
  working tree, as are today's edits. None of it is live until committed and pushed (blog.dugong.live
  is served from this repo). No git commit or push was performed this run, consistent with prior
  runs' behaviour; deploy is left to the normal manual flow. Recommend committing and pushing so the
  accumulated optimization work actually reaches crawlers.
- Nº 79 now has 8 inbound sibling links and Nº 78 has 9. Established posts sit near 30; these will
  keep climbing as future posts add them to grids. No further forced injection this run — 8-9 is a
  natural, design-consistent level.
