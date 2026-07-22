# SEO / GEO report — 2026-07-20 (run 2, internal-link pass)

**Scope:** Second scheduled SEO/GEO pass of the day. The morning run (00:14) was audit-first and
fixed the hub's missing ItemList schema. Since then, Dispatch Nº 86
(`how-to-stop-discount-codes-applying-to-sale-items-on-shopify.html`) published in the overnight
blog run, so this pass focused on wiring the new post into the internal-link graph, which was the
one substantive gap the audit surfaced. 37 post files edited plus sitemap.xml.

## Audit baseline

Full structural audit across all 79 HTML files (39 posts incl. hub, 39 stubs, index) and
distribution surfaces:

| Check | Result |
|---|---|
| JSON-LD parse (all files) | 0 errors |
| broken internal links site-wide | 0 |
| canonical matches filename (all posts + index) | 0 issues |
| stub redirects (noindex + meta-refresh + canonical) | 39 / 39 PASS |
| meta descriptions missing / over 160 chars | 0 / 0 |
| exactly one h1 per page | 40 / 40 |
| og: and twitter: meta on every post | 40 / 40 |
| sitemap.xml: 40 locs, 0 dangling, new post present | PASS |
| feed.xml: 40 items, new post present | PASS |
| llms.txt post coverage | 39 / 39 |
| schema: BlogPosting + BreadcrumbList + FAQPage on all 39; HowTo on 38; ItemList on hub | PASS |
| dateModified in JSON-LD | 39 / 39 posts |
| robots.txt AI-crawler allowances | intact |

## Issue fixed — new post nearly orphaned in the link graph

The publish run added the new post to index, sitemap, feed, llms.txt, and one related grid
(tiered-volume-discounts), but not to the READ NEXT grids on the other posts. Result: **3 inbound
links vs a site average of 34.6**. Internal inbound links are the strongest on-site signal both
for crawler discovery/PageRank flow and for answer engines assessing topical authority, so the
site's newest page was its least discoverable.

Fix: inserted the new post's card (stub title "The discount code that double-dips your sale",
one-sentence dek, JUL 20 / P. Singh footer, matching the card already present on the
tiered-discounts post verbatim) as the first card in the READ NEXT grid of all 37 remaining post
pages, hub included. Bumped `<lastmod>` to 2026-07-20 in sitemap.xml for the 37 edited pages so
crawlers see the change. JSON-LD `dateModified` was left untouched on those pages, consistent
with prior runs (it tracks content revisions, not grid updates).

Non-issues noted and left alone: the legacy feed item "The death of the drag-and-drop builder"
links to the homepage with a `#dispatch-47` guid (resolves fine, predates the article era), and
the em-dash counts in post bodies are site boilerplate present since publication.

## Verification (all passing)

| Check | Result |
|---|---|
| new post inbound links | 3 → **40** (site max) |
| inbound graph min / avg / max | 26 / 35.6 / 40, no orphans |
| duplicate cards from the insert | 0 |
| JSON-LD parse site-wide | 0 errors |
| broken internal links / canonical drift | 0 |
| sitemap.xml / feed.xml valid XML | PASS |
| sitemap: 40 locs, 39 lastmod = 2026-07-20 | PASS |
| em/en dashes in inserted card text | 0 |

## Open items

- **Undeployed working tree.** These edits (37 posts, sitemap.xml, this report) sit uncommitted
  alongside the overnight publish and the morning run's edits, consistent with prior runs.
  Nothing is live on blog.dugong.live until committed and pushed.
- Known follow-up carried from QA (owner's call): index card deks are paragraph-length; a
  site-wide dek trim would resolve the homepage row-height issue at the root.
- Uncovered candidate topics carried forward: cross-product BOGO, automatic best-discount
  selection / preventing code stacking (partially covered by Nº 86 now), loyalty-points
  automation.
