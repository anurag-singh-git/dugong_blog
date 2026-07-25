# SEO / GEO report, 2026-07-24 (verification pass, no changes required)

**Scope:** Scheduled full-site SEO/GEO pass. No blog run has published today, so the site state
is exactly what the 2026-07-23 publish run (Nº 89), same-day internal-link pass (41 posts
meshed), and same-day QA sweep (1,512 card chips corrected) left behind. This run re-audited
all 85 HTML files (42 posts incl. hub, 42 redirect stubs, index) and every distribution
surface, then ran a deeper second tier of checks beyond the standard baseline. **Zero
substantive issues found. No files were edited.**

## Baseline structural audit (all passing)

| Check | Result |
|---|---|
| JSON-LD parse (all 85 files) | 0 errors |
| broken internal links site-wide | 0 |
| canonical matches filename (posts + index) | 0 issues |
| stub redirects (noindex + canonical + meta-refresh) | 42 / 42 PASS |
| exactly one h1 per page | 43 / 43 |
| og: and twitter: meta on every post + index | 43 / 43 |
| sitemap.xml: 43 locs, 0 dangling, all posts covered, valid XML | PASS |
| feed.xml: 43 items, valid XML | PASS |
| llms.txt post coverage | 42 / 42 |
| robots.txt AI-crawler allowances (GPTBot, ClaudeBot, Claude-Web, PerplexityBot, Google-Extended, CCBot, anthropic-ai, OAI-SearchBot) | intact |
| duplicate titles across posts | 0 |
| meta descriptions present, unique, 160 chars or under | PASS |
| self-links in body or READ NEXT grids | 0 |

## Second-tier checks run this pass (all passing)

Since the baseline came back clean, this run went deeper than the standard checklist:

| Check | Result |
|---|---|
| schema completeness per post via @graph (BlogPosting + BreadcrumbList + FAQPage) | 42 / 42 |
| READ NEXT card chips (date + read time) vs target post JSON-LD, 1,512 cards | 0 stale, QA's 07-23 fix holds |
| duplicate meta descriptions across posts + index | 0 |
| heading hierarchy (no h3 before first h2) | 43 / 43 |
| img alt attributes, posts + index | 0 missing |
| og:image resolves to an existing file, posts + index | 43 / 43 |
| em/en dashes in authored content (outside excluded template zones) | 0 |
| inbound link graph min / avg / max | 25 / 34.9 / 41, no orphans |

Note on the inbound graph: yesterday's report quoted 26 / 35.9 / 42 counting distinct link
placements; this pass counts distinct linking pages (multiple links from one post to the same
target count once), hence the slightly lower figures. Both views agree there are no orphans
and no under-linked posts: the floor (25 of 41 possible linking pages) is the multi-supplier
and schedule-publishing posts, both comfortably discoverable.

## Checked and left as-is

- **Title separator source encoding:** the 8 newest posts and one older post encode the brand
  separator in `<title>` as the `&mdash;` entity; the other 34 use the literal character. Both
  render identically to browsers, crawlers, and answer engines, so there is no SEO or GEO
  effect. Flagged for awareness only; normalizing would touch 34 files for zero rendered
  difference, so not done.
- Titles over 70 chars remain due to the "Dugong Field Notes" brand suffix; keyword portion is
  front-loaded, consistent with prior rulings.
- Template-level em/en dashes (title separator, RSS link title, ticker spans, CSS comments)
  remain excluded from house style enforcement by long-standing convention.
- Hub ItemList remains at 4 items, matching its editorial content, per prior ruling.
- Sitemap lastmod values (all 2026-07-23) are accurate: every post was edited by yesterday's
  mesh pass. No bump today since nothing changed.

## Open items (carried forward)

- **Undeployed working tree.** The 07-23 runs' edits plus this report sit uncommitted; nothing
  is live on blog.dugong.live until committed and pushed. No commit or push was made,
  consistent with scheduled-run convention.
- Known follow-up (owner's call): index card deks are paragraph-length; a site-wide dek trim
  would resolve the homepage row-height issue at the root.
- Uncovered candidate topics for future dispatches: cross-product BOGO, loyalty-points
  automation, gift-card automation, multi-store product sync (heavier vendor coverage, weigh
  against fresher gaps).

## Conclusion

The site is in its best measured state to date: every page indexed in sitemap and feed, full
schema coverage, a dense and current internal-link mesh, accurate card chips site-wide, and
all AI-crawler surfaces (robots.txt, llms.txt, feed.xml) intact. The correct action this pass
was no action, and that is what was taken.
