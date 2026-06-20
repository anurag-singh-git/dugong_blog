# SEO / GEO report — 2026-06-20 (audit pass)

This run is a site-wide SEO/GEO audit, separate from the morning post-publish pass (Dispatch Nº 64,
"The image alt text no one writes"). Goal: catch site-level defects the per-post run can miss, and
fix any found. No new post written.

## Technical SEO assets — all clean

- **sitemap.xml** valid XML, 18 URLs (homepage + 17 posts). Every post on disk is present; no orphans,
  no entries pointing at missing files. Homepage lastmod 2026-06-20.
- **feed.xml** valid XML, 17 items, one per post. Matches disk exactly.
- **llms.txt** lists all 17 posts. Matches disk exactly.
- **robots.txt** allows all major search and answer-engine crawlers explicitly (GPTBot, OAI-SearchBot,
  ClaudeBot, PerplexityBot, Google-Extended, Applebot-Extended, Bingbot, CCBot, Amazonbot,
  Meta-ExternalAgent, DuckAssistBot, cohere, YouBot, Bytespider, and more), with the sitemap declared.
  No change needed.
- Coverage cross-check (disk vs sitemap vs feed vs llms): all four sets identical. Zero drift.

## Per-post audit (all 17 posts)

Checked title tag, meta description length + uniqueness, canonical self-reference, OG + Twitter cards,
JSON-LD validity, single-H1 rule, internal-link integrity, and image alt text.

- **H1:** exactly one per post (17/17).
- **Canonical:** present and self-referential on every post (17/17).
- **OG / Twitter image cards:** present on every post (17/17).
- **JSON-LD:** parses on every post. All carry BlogPosting + BreadcrumbList + FAQPage; 16 also carry
  HowTo (the pillar post "the-shopify-automations-no-one-builds" intentionally omits HowTo, correct
  for an overview piece).
- **Meta descriptions:** all unique, no duplicates across the catalogue.
- **Internal links:** site-wide scan of every local `.html` href across all 18 pages found 0 broken
  links.
- **Image alt text:** no images missing the alt attribute.

## Issue found and fixed

**The image alt text no one writes** (today's post) shipped with a 168-character meta description,
above the house SERP-safe ceiling (every sibling sits at 146–162). Google truncates around 155–160
characters, so the tail ("...and writes the line.") would have been cut in results. Notable that the
post about alt-text hygiene had the only on-page SEO defect in the set.

Fix: rewrote the meta description to 157 characters, keeping the searched phrase "image alt text"
front-loaded and the fix intact:

> Shopify never writes image alt text and has no bulk way to add it, so it sits blank across your
> catalog. The AI playbook that reads each photo and writes it.

Aligned the Twitter description to the same 157-char copy for channel consistency (was 161). The
richer 338-char og:description was left as-is (intended long social copy, within OG norms).

After the fix, all 17 meta descriptions sit in the 146–162 band.

## Verification

- New meta + Twitter description both 157 chars; key phrase front-loaded; no em/en dashes in authored
  copy.
- JSON-LD still parses (1 block); `<div>` balance 76/76 unchanged; sitemap.xml and feed.xml still
  valid XML.
- Full desc-length sweep re-run: 0 posts out of range.

## Result

One real defect found and corrected (over-length meta description on Nº 64). All other SEO/GEO
infrastructure verified clean. Changes staged in the working tree only; no commit or deploy performed,
consistent with prior runs.
