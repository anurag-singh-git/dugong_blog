# SEO / GEO report — 2026-07-18 (full-site pass)

**Scope:** Full-site SEO/GEO optimization pass. No new post was published by this run. This pass
audited all 75 HTML files plus the distribution surfaces, confirmed the site is structurally
healthy, and fixed the one real weakness it surfaced: the newest post was orphaned in the
internal-link graph (2 inbound links vs a pack average of 32.7).

## Audit baseline

Ran a full structural audit across every HTML file and distribution surface before touching
anything. Everything below was already healthy:

| Check | Result |
|---|---|
| HTML files | 75 (36 how-to posts + 37 pain-point stubs + index + best-shopify hub) |
| sitemap.xml / feed.xml valid XML | PASS |
| sitemap loc count | 38, 0 dangling |
| feed item count | 38, all resolve |
| JSON-LD parse (all files) | 0 errors |
| broken internal links site-wide | 0 |
| canonical matches filename (all posts) | 0 issues |
| stub redirects (noindex + meta-refresh + canonical) | 37 / 37 PASS |
| meta descriptions over 160 chars | 0 (max 160, held from 07-16 pass) |
| llms.txt post coverage | full (newest post present) |
| em/en dashes in authored prose | 0 |

## Issue fixed — newest post orphaned in the internal-link graph

The latest post, **how-to-set-up-tiered-volume-discounts-on-shopify** (published 07-16), had only
**2 inbound internal links** while every other post sat at 25 to 37 (pack average 32.7). Orphaned
pages get crawled less often, accumulate less internal PageRank, and are less likely to be
retrieved and cited by answer engines. This is the single highest-value SEO/GEO fix available on
the site right now.

Fix: inserted the post's standard related-post card into the `related-grid` of every how-to post
and the hub page that did not already link it — **35 files edited**. The card markup is copied
verbatim from the one page that already carried it, so title, dek, tag, read time, date, and author
are consistent across the pack. One post (free-gift-with-purchase) already linked it and was left
untouched.

Result after the fix:

| Metric | Before | After |
|---|---|---|
| tiered-volume-discounts inbound links | 2 | 37 (now the pack max) |
| internal-link graph min / avg / max | 2 / 32.7 / 37 | 25 / 33.7 / 37 |

The post is now at full pack parity and no longer an orphan.

## Distribution surface updated

- **sitemap.xml:** bumped `<lastmod>` to 2026-07-18 for the 37 genuinely-changed post files
  (the 35 that gained the card, plus best-shopify and the tiered post itself). Legitimate
  crawl-freshness signal. Still valid XML, 38 locs.

## Verification (all passing)

| Check | Result |
|---|---|
| tiered-volume-discounts inbound links | 37 (was 2) |
| internal-link graph min inbound | 25 (was 2) |
| sitemap.xml / feed.xml valid XML | PASS |
| max meta description length site-wide | 160 |
| meta descriptions over 160 | 0 |
| JSON-LD parse site-wide | 0 errors |
| div / anchor balance on all edited files | 0 mismatches |
| broken internal links / canonical drift | 0 |
| em/en dashes on added git-diff lines | 0 |

## Open items

- **Undeployed working tree.** All edits are in the working tree only — 35 post files plus
  sitemap.xml, on top of the still-uncommitted 07-16 pass (8 metas, index, llms.txt, feed) and the
  untracked 07-16 tiered post and its stub. No git commit or push was performed (consistent with
  prior runs). Nothing is live on blog.dugong.live until committed and pushed. (`.DS_Store` also
  shows as modified; it is a system file and was not touched by this run.)
- Internal-link graph is back at full parity (min inbound 25). No further link work needed until the
  next post is published.
- Uncovered candidate topics carried forward for future dispatches: cross-product BOGO, automatic
  best-discount selection / preventing code stacking, loyalty-points automation, gift-message /
  gift-wrap automation.
