# SEO / GEO report, 2026-07-22 (audit-only pass)

**Scope:** Scheduled full-site SEO/GEO pass. No new post has published since Dispatch Nº 86
(2026-07-20), and the 07-20 run 2 already wired Nº 86 into the full internal-link mesh, so this
pass was audit-first across all 79 HTML files (39 posts incl. hub, 39 redirect stubs, index) plus
sitemap.xml, feed.xml, llms.txt, and robots.txt. The audit surfaced **zero substantive issues**,
so no files were edited. This is the first pass since the working tree was committed and pushed,
so it also verified the live site.

## Deployment status (new since last report)

Every prior report carried an "undeployed working tree" open item. That is now resolved: git HEAD
(dda543b, 2026-07-22 19:18 IST) is in sync with origin/main and the working tree is clean, so all
accumulated work through the 07-20 runs (Nº 86 publish, link mesh, spelling normalization, hub
ItemList schema) is **live on blog.dugong.live**. Verified directly: live robots.txt matches the
repo byte-for-byte (all AI-crawler allowances serving), and live sitemap.xml serves as valid
application/xml.

## Audit results (all passing)

| Check | Result |
|---|---|
| HTML files | 79 (39 posts incl. hub, 39 stubs, index) |
| JSON-LD parse, all files | 0 errors |
| broken internal links site-wide | 0 |
| canonical matches filename (posts + index) | 0 issues |
| stub redirects (noindex + canonical + meta-refresh) | 39 / 39 PASS |
| meta descriptions on posts: missing / over 160 chars | 0 / 0 |
| exactly one h1 per post + index | 40 / 40 |
| og: and twitter: meta on every post + index | 40 / 40 |
| og:url matches canonical on every post | 39 / 39 |
| BlogPosting author, publisher w/ logo, mainEntityOfPage | 39 / 39 |
| schema: BlogPosting + BreadcrumbList + FAQPage all posts; HowTo 38; ItemList on hub | PASS |
| FAQPage: every post has 3+ questions | PASS |
| dateModified present in JSON-LD | 39 / 39 |
| internal-link graph min / avg / max inbound | 25 / 34.6 / 39, no orphans |
| hub links to sibling posts | 38 / 38 |
| sitemap.xml: 40 locs, 0 dangling, valid XML | PASS |
| feed.xml: 40 items, valid XML, lastBuildDate = newest item | PASS |
| llms.txt post coverage | 39 / 39 |
| robots.txt AI-crawler allowances (repo and live) | intact, identical |
| duplicate titles across posts | 0 |
| html lang attribute on every post | PASS |
| `</head>` present on every file | PASS |

## Checked and left as-is

- **Hub ItemList has 4 items.** This matches the article's editorial content ("Four Shopify
  automations that pay back faster than tagging"), not the site's 39 posts. Correct as-is; the
  hub's link coverage of all 38 siblings is carried by the READ NEXT grid and body links.
- **Sitemap lastmod:** 39 entries at 2026-07-20, one (tiered-volume-discounts) at 2026-07-18.
  Accurate: that post was the only one not edited in the 07-20 link pass because it already
  carried the Nº 86 card. No false freshness signals; left alone.
- **26 titles exceed 70 characters**, all due to the "Dugong Field Notes" brand suffix. The
  keyword-bearing portion is front-loaded, so SERP truncation only clips the brand. Churning 26
  titles would reset freshness signals for a marginal gain; noted, not changed.
- **~4 em/en dashes per post file** are site boilerplate (ticker template text), present since
  publication and excluded from house-style enforcement by long-standing convention.
- Stub pages intentionally have no meta description and canonical to their targets; that is the
  redirect design, not an error.

## Actions taken

None beyond verification: no file edits, no commit, no push. The audit found nothing to fix, and
editing healthy files would churn lastmod/dateModified signals for no benefit.

## Open items

- Known follow-up carried from QA (owner's call): index card deks are paragraph-length; a
  site-wide dek trim would resolve the homepage row-height issue at the root.
- Uncovered candidate topics carried forward for future dispatches: cross-product BOGO,
  loyalty-points automation, gift-card automation.
- Next substantive SEO/GEO work will be triggered by the next publish (wire the new post into the
  link mesh, sitemap, feed, llms.txt), per the established pattern.
