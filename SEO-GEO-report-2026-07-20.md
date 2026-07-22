# SEO / GEO report — 2026-07-20 (full-site pass)

**Scope:** Scheduled full-site SEO/GEO pass. No new post has been published since Dispatch Nº 85
(2026-07-18), so this run was audit-first: every HTML file and distribution surface was checked,
and the one substantive gap surfaced was fixed. One file edited (`best-shopify-automations-to-set-up.html`)
plus its sitemap `lastmod`.

## Audit baseline

Ran the full structural audit across all 77 HTML files and distribution surfaces. Everything was
already healthy:

| Check | Result |
|---|---|
| HTML files | 77 (38 posts incl. hub + 38 stubs + index) |
| sitemap.xml / feed.xml valid XML | PASS |
| sitemap loc count | 39 (homepage + 38 posts), 0 dangling |
| feed item count | 39, all resolve |
| JSON-LD parse (all files) | 0 errors |
| broken internal links site-wide | 0 |
| canonical matches filename (all posts) | 0 issues |
| stub redirects (noindex + meta-refresh + canonical) | 38 / 38 PASS |
| meta descriptions over 160 chars | 0 |
| `</head>` present on every file | PASS |
| llms.txt post coverage | 38 / 38 |
| internal-link graph min / avg / max inbound | 29 / 44.1 / 89 (no orphans) |
| og: and twitter: meta on every post | 39 / 39 |
| exactly one h1 per page | 39 / 39 |
| dateModified in JSON-LD | 38 / 38 posts |
| robots.txt AI-crawler allowances (GPTBot, ClaudeBot, PerplexityBot, etc.) | intact |

## Issue fixed — hub listicle had no list-type schema

Schema coverage across the pack was BlogPosting + BreadcrumbList + FAQPage on all 38 posts and
HowTo on 37. The single post without HowTo is the hub,
**best-shopify-automations-to-set-up.html**, which is correct (it is an essay/listicle, not a
how-to), but it carried no list-type markup at all. Its centerpiece is an explicitly ordered
list ("Four Shopify automations that pay back faster than tagging"), which is exactly the shape
answer engines extract for "best X" queries, so the page was leaving its strongest GEO signal
unmarked.

Fix: added an **ItemList** node to the page's existing JSON-LD `@graph` with `numberOfItems: 4`,
ascending order, and one `ListItem` per automation (VIP detection, refund triage with evidence
parsing, chargeback evidence assembly, abandoned-checkout intent classification). Each item's
name matches its section heading verbatim and each description is a one-sentence summary drawn
from that section's own prose. The node is anchored at `#list` on the page's canonical URL.

Also bumped the page's `<lastmod>` in sitemap.xml from 2026-07-18 to 2026-07-20 so crawlers see
the change; all other lastmod values were left at 2026-07-18 (accurate, since no other file was
touched).

## Verification (all passing)

| Check | Result |
|---|---|
| hub JSON-LD parses, @graph now BlogPosting + BreadcrumbList + FAQPage + ItemList | PASS |
| JSON-LD parse site-wide | 0 errors |
| broken internal links / canonical drift | 0 |
| meta descriptions over 160 | 0 |
| sitemap.xml / feed.xml valid XML | PASS |
| sitemap: 39 locs, 0 dangling, hub lastmod = 2026-07-20 | PASS |
| em/en dashes in added JSON-LD text | 0 |

## Open items

- **Undeployed working tree.** This run's edits (hub post, sitemap.xml, this report) sit
  uncommitted, consistent with prior runs. Nothing is live on blog.dugong.live until committed
  and pushed.
- Internal-link graph healthy (min inbound 29); no link work needed until the next post
  publishes.
- Known follow-up carried from QA (owner's call): index card deks are paragraph-length,
  inflating homepage row heights; a site-wide dek trim would resolve the root cause.
- Uncovered candidate topics carried forward: cross-product BOGO, automatic best-discount
  selection / preventing code stacking, loyalty-points automation.
