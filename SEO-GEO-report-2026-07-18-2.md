# SEO / GEO report — 2026-07-18 (full-site pass, second report of the day)

**Scope:** Full-site SEO/GEO optimization pass, run after this morning's publish of Dispatch Nº 85
(`how-to-add-a-gift-message-and-gift-wrap-at-checkout-on-shopify.html`) and the second QA sweep.
No new post was published by this run. The pass audited all 77 HTML files plus the distribution
surfaces, confirmed the site is structurally healthy, and fixed the one real weakness it surfaced:
the new Nº 85 post was orphaned in the internal-link graph (2 inbound links vs a pack average of
~33). This was the known handoff item the 07-18 QA sweep explicitly left for this run.

## Audit baseline

Ran a full structural audit across every HTML file and distribution surface before touching
anything. Everything below was already healthy:

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
| `</head>` present on every file | PASS (QA sweep's four fixes held) |
| llms.txt post coverage | 38 / 38 (Nº 85 present) |
| em/en dashes in Nº 85 authored prose | 0 (the 3 glyphs found are HTML/CSS comments, per convention) |

## Issue fixed — Nº 85 orphaned in the internal-link graph

The new post, **how-to-add-a-gift-message-and-gift-wrap-at-checkout-on-shopify** (published this
morning), had only **2 inbound internal links** (index + the free-gift post's reciprocal card)
while every other post sat at 25 to 38 (pack average ~33). Orphaned pages get crawled less often,
accumulate less internal PageRank, and are less likely to be retrieved and cited by answer
engines. This is the same situation Nº 84 was in before this morning's first SEO pass fixed it.

Fix: extracted the post's canonical read-next card verbatim from the free-gift post (the one page
that already carried it, so title, dek, tag, read time, date, and author stay consistent) and
inserted it as the first card in the `related-grid` of every sibling post and the hub page that
did not already link it — **36 files edited**. No grid received a duplicate card and no post links
to itself (both verified).

Result after the fix:

| Metric | Before | After |
|---|---|---|
| Nº 85 inbound links | 2 | 38 (now the pack max) |
| internal-link graph min / avg / max | 2 / 33.3 / 38 | 25 / 34.1 / 38 |

The post is now at full pack parity and no longer an orphan.

## Distribution surfaces

- **sitemap.xml:** no change needed. All 39 `<lastmod>` values already read 2026-07-18 from this
  morning's publish run and first SEO pass, so today's grid edits are already covered by the
  existing freshness signal. Verified still valid XML, 39 locs.
- **feed.xml / llms.txt:** already complete and correct for Nº 85; untouched.

## Verification (all passing)

| Check | Result |
|---|---|
| Nº 85 inbound links | 38 (was 2) |
| internal-link graph min inbound | 25 (was 2) |
| duplicate cards within any grid | 0 (index's 3 links to Nº 85 are the pre-existing featured card + two topic-cloud entries, by design) |
| grid self-links | 0 |
| div / anchor balance on all edited files | 0 mismatches |
| JSON-LD parse site-wide | 0 errors |
| broken internal links / canonical drift | 0 |
| meta descriptions over 160 | 0 |
| sitemap.xml / feed.xml valid XML | PASS |
| em/en dashes on added git-diff lines | 0 |

## Open items

- **Undeployed working tree.** This run's edits (36 post files plus this report) sit in the
  working tree alongside the pre-existing uncommitted QA items (QA-report-2026-07-18-2.md and the
  index.html glyph-size CSS line from the QA addendum). No git commit or push was performed,
  consistent with prior runs. Nothing is live on blog.dugong.live until committed and pushed.
- Internal-link graph is back at full parity (min inbound 25). No further link work needed until
  the next post is published.
- Known follow-up carried from the QA sweep (owner's call): index card deks are paragraph-length,
  inflating homepage row heights; a site-wide dek trim would resolve the root cause.
- Uncovered candidate topics carried forward for future dispatches: cross-product BOGO, automatic
  best-discount selection / preventing code stacking, loyalty-points automation. (Gift-message /
  gift-wrap was consumed by today's Nº 85.)
