# SEO / GEO report — 2026-07-15 (full-site pass)

**Scope:** Full-site SEO/GEO optimization pass. No new post published by this run (the day's post,
Nº 83 sync-bundle-inventory, was already published by the blog-run flow and carries its own report,
`SEO-GEO-report-2026-07-15.md`). This pass audited all 73 committed HTML files and fixed the two
real weaknesses it surfaced: the two newest posts were badly under-linked internally, and two meta
descriptions ran past the SERP snippet limit.

## Audit baseline

Ran a full structural audit across all HTML files (37 full posts + 36 pain-point stubs) before
touching anything. Everything below was already healthy:

| Check | Result |
|---|---|
| sitemap.xml / feed.xml valid XML | PASS |
| sitemap loc count | 37 (homepage + 36 posts), 0 dangling |
| feed item count | 37, all resolve |
| full posts missing from sitemap | 0 |
| JSON-LD parse (all files) | 0 errors |
| broken internal links site-wide | 0 |
| canonical matches filename (all posts) | 0 issues |
| stub redirects (noindex + canonical) | 36 / 36 PASS |
| llms.txt post coverage | 36 / 36 |
| em/en dashes in authored prose or structured data | 0 (the only dashes are inside HTML comments) |

## Issue 1 — the two newest posts were starved of internal links

The read-next grids in each post are the site's main internal-link surface. Across the established
set most posts pull ~31 inbound links. The two most recently published posts were sitting far below
that because they had not yet been added to sibling grids:

| Post | Inbound before | Inbound after |
|---|---|---|
| sync bundle inventory with component stock (Nº 83) | 2 | 35 |
| automatically pause ads for out-of-stock products (Nº 82) | 3 | 35 |

Fix: extracted each post's canonical read-next card verbatim from a post that already carried it
(so markup and styling are unchanged) and inserted it as the first card in every sibling grid that
did not already link to it — 34 grids for the bundle post, 33 for the pause-ads post. This brings
both to full pack parity (35 inbound, site max is 36). No grid received a duplicate card and no post
links to itself (both verified). This raised the site-wide inbound minimum from 2 to 25 and lifted
the average from 31.4 to 33.2.

## Issue 2 — two over-length meta descriptions truncating in search

The two newest posts carried meta descriptions well past the ~155 to 160 character SERP limit, so
their value tail was being cut off. Rewrote both to a keyword-first, self-contained line that fits
the snippet and stays quotable for answer engines:

| Post | Before | After |
|---|---|---|
| sync bundle inventory (Nº 83) | 195 | 152 |
| pause ads for out-of-stock (Nº 82) | 187 | 152 |

Both rewrites keep the primary keyword up front and contain zero em/en dashes (user style). The four
remaining descriptions in the 166 to 173 range were left as-is, consistent with prior runs' standing
judgment: they are only marginally long, keep the primary keyword in the first clause, and read
strongly.

## Distribution surface updated

- **sitemap.xml:** bumped `<lastmod>` to 2026-07-15 for the 36 genuinely-changed post files (grid
  edits plus the two meta edits) and the homepage. Legitimate crawl-freshness signal. Still valid
  XML, 37 locs.

## Verification (all passing)

| Check | Result |
|---|---|
| div balance on all files | 0 mismatches |
| anchor balance on all files | 0 mismatches |
| duplicate cards within any grid | 0 |
| grid self-links | 0 |
| broken internal links site-wide | 0 |
| JSON-LD parse site-wide | 0 errors |
| two target inbound counts | 35 / 35 (were 2 / 3) |
| site-wide inbound min / avg | 25 / 33.2 (was 2 / 31.4) |
| edited meta description lengths | 152 / 152 (were 195 / 187) |
| em/en dashes introduced (git diff added lines) | 0 |
| sitemap.xml / feed.xml valid XML | PASS |
| sitemap + llms.txt cover all full posts | PASS |

## Open items

- **Undeployed working tree.** All edits are in the working tree only. No git commit or push was
  performed (consistent with prior runs). Nothing is live on blog.dugong.live until committed and
  pushed.
- The four meta descriptions in the 166 to 173 range remain marginally long by design. Revisit only
  if a future run tightens the whole band.
- Uncovered candidate topics carried forward for future dispatches: quantity/tiered volume discounts,
  cross-product BOGO, automatic best-discount selection / preventing code stacking, loyalty-points
  automation, gift-message/gift-wrap.
