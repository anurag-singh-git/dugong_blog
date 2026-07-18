# SEO / GEO report — 2026-07-16 (full-site pass)

**Scope:** Full-site SEO/GEO optimization pass. No new post was published by this run (blog-run
publishes the day's dispatch on its own flow). This pass audited all 73 HTML files plus the
distribution surfaces, confirmed the site is structurally healthy, and tightened the one real
weakness it surfaced: eight meta descriptions running past the SERP snippet limit.

## Audit baseline

Starting state: working tree clean (prior runs' edits are committed and live). Latest post is
Nº 83, sync-bundle-inventory (2026-07-15). Ran a full structural audit across every HTML file
and distribution surface before touching anything. Everything below was already healthy:

| Check | Result |
|---|---|
| HTML files | 73 (35 how-to posts + 36 pain-point stubs + index + best-shopify hub) |
| sitemap.xml / feed.xml valid XML | PASS |
| sitemap loc count | 37, 0 dangling, 0 posts missing |
| feed item count | 37, all resolve |
| JSON-LD parse (all files) | 0 errors |
| broken internal links site-wide | 0 |
| canonical matches filename (all posts) | 0 issues |
| stub redirects (noindex + meta-refresh + canonical) | 36 / 36 PASS |
| llms.txt post coverage | full |
| inbound internal-link min / avg / max | 25 / 33.2 / 36 (full pack parity, unchanged since 07-15) |
| em/en dashes in authored prose | 0 (only template-level: title suffix, RSS title, dispatch line, CTA band, CSS comments) |

Nothing had drifted since the 07-15 full-site pass. The internal-link graph is already at full
parity (the two newest posts that were starved on 07-15 are now at 35 and 36 inbound), so no
link work was needed this run.

## Issue fixed — eight meta descriptions over the SERP snippet limit

Eight post meta descriptions ran past the ~155 to 160 character limit Google uses for the desktop
snippet, so their value tail was being truncated in search. The 07-15 pass had left the 166 to 173
band "by design, revisit only if a future run tightens the whole band." This run tightened the whole
band. Each was rewritten keyword-first, self-contained, and quotable for answer engines, with zero
em/en dashes:

| Post | Before | After |
|---|---|---|
| automatically send invoices | 173 | 145 |
| schedule product publishing | 172 | 149 |
| split and route orders to multiple suppliers | 167 | 155 |
| set a minimum order amount | 166 | 158 |
| automatically tag orders | 162 | 152 |
| automatically request product reviews | 162 | 156 |
| automatically add a free gift with purchase | 162 | 157 |
| set up pre-orders without holding in-stock items | 161 | 148 |

The site-wide max meta length is now 160 (was 173); zero descriptions exceed 160. Each post's
`<meta name="description">` is independent of its og:description, twitter:description, and JSON-LD
description (those carry their own longer text), so tightening the meta tag introduced no
cross-tag inconsistency.

## Distribution surface updated

- **sitemap.xml:** bumped `<lastmod>` to 2026-07-16 for the eight genuinely-changed post files.
  Legitimate crawl-freshness signal. Still valid XML, 37 locs.

## Verification (all passing)

| Check | Result |
|---|---|
| sitemap.xml / feed.xml valid XML | PASS |
| max meta description length site-wide | 160 (was 173) |
| meta descriptions over 160 | 0 (was 8) |
| JSON-LD parse site-wide | 0 errors |
| div / anchor balance on all edited files | 0 mismatches |
| em/en dashes in edited metas | 0 |
| em/en dashes on added git-diff lines | 0 |
| broken internal links / canonical drift | 0 |

## Open items

- **Undeployed working tree.** All edits are in the working tree only — eight post files plus
  sitemap.xml. No git commit or push was performed (consistent with prior runs). Nothing is live on
  blog.dugong.live until committed and pushed. (`.DS_Store` also shows as modified; it is a system
  file and was not touched by this run.)
- Meta-description band is now fully within the SERP limit (max 160). No further tightening needed.
- Uncovered candidate topics carried forward for future dispatches: quantity/tiered volume discounts,
  cross-product BOGO, automatic best-discount selection / preventing code stacking, loyalty-points
  automation, gift-message/gift-wrap.
