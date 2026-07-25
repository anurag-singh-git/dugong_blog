# SEO / GEO report, 2026-07-23 (internal-link pass)

**Scope:** Scheduled full-site SEO/GEO pass. Dispatch Nº 89 ("The customer you can't ban",
`how-to-block-a-customer-on-shopify.html`) published in this morning's blog run with its mesh
work explicitly deferred to this pass. The audit also caught that Nº 87 (duplicate customer
profiles) and Nº 88 (shipping delays), both published 2026-07-22 after that day's SEO pass ran,
never received a mesh pass of their own. This run wired all three into the full internal-link
graph and fixed two over-length meta descriptions. 41 post files edited plus sitemap.xml.

## Audit baseline

Full structural audit across all 85 HTML files (42 posts incl. hub, 42 stubs, index) and
distribution surfaces:

| Check | Result |
|---|---|
| JSON-LD parse (all files) | 0 errors |
| broken internal links site-wide | 0 |
| canonical matches filename (posts + index) | 0 issues |
| stub redirects (noindex + canonical + meta-refresh) | 42 / 42 PASS |
| exactly one h1 per page | 43 / 43 |
| og: and twitter: meta on every post + index | 43 / 43 |
| sitemap.xml: 43 locs, 0 dangling, valid XML | PASS |
| feed.xml: 43 items, valid XML | PASS |
| llms.txt post coverage | 42 / 42 |
| robots.txt AI-crawler allowances | intact |
| duplicate titles across posts | 0 |
| meta descriptions over 160 chars | **2 (fixed below)** |
| inbound link graph | **3 posts under-linked (fixed below)** |

## Issue 1 fixed, three posts under-linked in the graph

Nº 89 had **2 inbound links**, and Nº 87 and Nº 88 had **3 each**, against a site average of 33
and a max of 42. The 07-22 SEO pass ran at 19:21, before that evening's publish of Nº 88, so
neither 07-22 post was ever meshed, and Nº 89's publish run left the mesh to this pass by
design. Internal inbound links are the strongest on-site signal for crawler discovery and for
answer engines assessing topical authority, so the site's three newest pages were its least
discoverable.

Fix: inserted each post's READ NEXT card (taken verbatim from the card already present in its
reciprocal sibling: high-risk orders for Nº 89, segment-repeat-customers for Nº 87, WISMO for
Nº 88) into the READ NEXT grid of every post that lacked it. Cards sit newest-first at the top
of each grid (Nº 89, Nº 88, Nº 87). 41 post files edited; no duplicate cards created; no
self-links introduced.

## Issue 2 fixed, two meta descriptions over 160 characters

The two newest posts shipped with meta descriptions of 180 chars (Nº 89) and 174 chars (Nº 88),
against the house rule of 160 max, which risks SERP truncation mid-sentence. Trimmed both to
157 and 156 chars respectively, preserving the front-loaded keyword phrasing and house voice.
og:description and twitter:description are intentionally longer per site pattern and were left
untouched, as was JSON-LD.

## Sitemap

Bumped `<lastmod>` to 2026-07-23 for all 41 edited pages so crawlers see the change. All 43
sitemap URLs now carry lastmod 2026-07-23, which is accurate: every post was edited today, and
the homepage and Nº 89 were already dated by the publish run. JSON-LD `dateModified` left
untouched on grid-only edits, consistent with prior runs (it tracks content revisions, not grid
updates).

## Verification (all passing)

| Check | Result |
|---|---|
| Nº 89 / Nº 88 / Nº 87 inbound links | 2, 3, 3 → **42, 42, 42** (site max) |
| inbound graph min / avg / max | 26 / 35.9 / 42, no orphans |
| duplicate cards from the inserts | 0 |
| self-link cards | 0 |
| JSON-LD parse site-wide | 0 errors |
| broken internal links / canonical drift | 0 |
| div balance on every edited file | PASS |
| meta descriptions over 160 chars | 0 |
| em/en dashes in inserted card text and new meta descriptions | 0 |
| sitemap.xml / feed.xml valid XML (43 / 43 entries) | PASS |
| llms.txt coverage | 42 / 42 |
| robots.txt AI-crawler allowances | intact |

## Checked and left as-is

- Titles over 70 chars remain due to the "Dugong Field Notes" brand suffix; keyword portion is
  front-loaded, noted not changed, consistent with prior rulings.
- Template-level em/en dashes in CSS comments and ticker boilerplate are excluded from house
  style enforcement by long-standing convention.
- Hub ItemList remains at 4 items, matching its editorial content; sibling coverage is carried
  by the READ NEXT grid.

## Open items

- **Undeployed working tree.** This run's edits (41 posts, sitemap.xml, this report) sit
  uncommitted alongside the 07-23 publish run's files (Nº 89 post, stub, index, feed, llms.txt).
  Nothing is live on blog.dugong.live until committed and pushed; no commit or push was made,
  consistent with scheduled-run convention.
- Known follow-up carried from QA (owner's call): index card deks are paragraph-length; a
  site-wide dek trim would resolve the homepage row-height issue at the root.
- Uncovered candidate topics carried forward: cross-product BOGO, loyalty-points automation,
  gift-card automation, multi-store product sync (heavier vendor coverage, weigh against
  fresher gaps).
