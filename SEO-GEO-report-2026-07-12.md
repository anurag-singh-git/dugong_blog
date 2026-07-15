# SEO / GEO report — 2026-07-12

**Scope:** Full-site SEO/GEO optimization pass. No new post published by this run. This run fixed
the two remaining structural weaknesses surfaced by a full-site audit: six badly under-linked posts
and the two remaining over-length meta descriptions. A concurrent blog-run process was observed
publishing a new post during this run (see Concurrency note).

## Audit baseline (all healthy)

Ran a full structural audit across all 69 committed HTML files before touching anything:

| Check | Result |
|---|---|
| sitemap.xml / feed.xml valid XML | PASS |
| sitemap loc count | 35 (homepage + 34 posts), 0 dangling |
| feed item count | 35, all resolve |
| stub ↔ post parity | 34 / 34 |
| JSON-LD parse (all files) | 0 errors |
| broken internal links site-wide | 0 |
| canonical matches filename (all posts) | 0 issues |
| stub redirects (noindex + meta-refresh + canonical) | 34 / 34 PASS |
| llms.txt post coverage | 34 / 34 |
| robots.txt AI/answer-engine allow list | present and broad (GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot, Google-Extended, Applebot, Bingbot, CCBot, and more) |

## Issue 1 — six posts badly under-linked internally

The read-next grids embedded in each post are the site's main internal-link surface. Across the
established set, most posts sit in nearly every sibling grid and pull ~34 inbound links. Six posts
were being omitted from 19 to 23 sibling grids each (versus the ~4-omission site norm), starving
them of crawl discovery and internal PageRank:

| Post | Inbound before | Inbound after |
|---|---|---|
| split / route orders to multiple suppliers | 11 | 25 |
| auto-send invoices | 12 | 25 |
| set a minimum order amount | 12 | 25 |
| schedule product publishing | 13 | 26* |
| limit purchase quantity per customer (Nº 81) | 14 | 26* |
| free gift with purchase (Nº 80) | 15 | 25 |

Fix: inserted each post's canonical read-next card (copied verbatim from an existing instance, so
markup and styling are unchanged) as the first card in sibling grids that did not already carry it.
Injection was done in two passes: first into topically-matched siblings (fulfillment, cart-value,
merchandising, drops, risk clusters depending on the post), then a broadening pass to reach a mid-pack
target of 25 inbound each. No grid received a duplicate card and no post links to itself (both verified).
Grids that already carried a card were skipped. This raised the site-wide inbound minimum from 11 to
25 and lifted the average from ~30 to 32.4.

*schedule-product-publishing and limit-purchase-quantity show 26 because the concurrently-published
new post also links to them.

## Issue 2 — two over-length meta descriptions truncating in search

Two posts still carried meta descriptions past the ~155 to 160 character SERP snippet limit, so their
value tail was being cut off. These were the two the prior run had flagged but left. Rewrote both to a
keyword-first, self-contained line that fits the snippet and stays quotable for answer engines:

| Post | Before | After |
|---|---|---|
| combine multiple orders | 217 | 155 |
| stop card-testing attacks | 176 | 155 |

The eight remaining descriptions in the 161 to 173 range were left as-is, consistent with the prior
run's judgment: they are only marginally long, keep the primary keyword in the first clause, and read
strongly. Both rewrites keep the primary keyword up front and contain zero em/en dashes (user style).

## Distribution surface updated

- **sitemap.xml:** bumped `<lastmod>` to 2026-07-12 for the 27 genuinely-changed post files (grid
  edits plus the two meta edits, overlapping set). Legitimate crawl-freshness signal. Still valid XML,
  35 locs.

## Verification (all passing)

| Check | Result |
|---|---|
| div balance on all changed files | 0 mismatches |
| anchor balance on all changed files | 0 mismatches |
| duplicate cards within any grid | 0 |
| grid self-links | 0 |
| broken internal links site-wide | 0 |
| JSON-LD parse site-wide | 0 errors |
| six target inbound counts | 25 to 26 (were 11 to 15) |
| site-wide inbound min / avg | 25 / 32.4 (was 11 / ~30) |
| edited meta description lengths | 155 / 155 (were 217 / 176) |
| em/en dashes introduced (git diff added lines) | 0 |
| sitemap.xml / feed.xml valid XML | PASS |

## Concurrency note

A separate blog-run process was writing to the repo during this pass. It created a new, still-untracked
post, `how-to-automatically-pause-ads-for-out-of-stock-products-on-shopify.html` (Nº 82), at 20:21, and
was holding `.git/index.lock`. That post is not yet in sitemap.xml, feed.xml, or llms.txt, and its
read-next grid is still partial — all expected for a post mid-publish. This SEO pass deliberately did
**not** touch that file or add it to any distribution surface, to avoid racing the blog-run that owns it.
None of my 27 edits overlap that file. My edits were re-verified intact after the concurrent write.

## Open items

- **Undeployed working tree.** All edits are in the working tree only. No git commit or push was performed
  (consistent with prior runs; a concurrent process was also holding the git lock). Nothing is live on
  blog.dugong.live until committed and pushed.
- **New post Nº 82 (pause-ads) needs its normal publish finish** by the blog-run flow: sitemap, feed,
  llms.txt, hero/ticker/archive counters, and full read-next grid. Left to that process.
- The six raised posts now sit at 25 to 26 inbound. They will continue climbing toward full pack parity
  (~34) as future posts add them to grids. No further forced injection this run.
- Uncovered candidate topics for future dispatches (carried forward): quantity/tiered volume discounts,
  cross-product BOGO, automatic best-discount selection / preventing code stacking, loyalty-points
  automation, gift-message/gift-wrap.
