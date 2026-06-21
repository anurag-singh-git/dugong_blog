# SEO / GEO report — 2026-06-21 (audit and cleanup pass)

This run is a same-day second pass, separate from the morning pipeline that published Dispatch Nº 65
("The repeat customer your store treats like a stranger") and wrote the primary
`SEO-GEO-report-2026-06-21.md`, `blog-run-2026-06-21.md`, and `QA-report-2026-06-21.md`. Goal: catch
site-level and on-page defects the primary run missed, and fix them. No new post written.

Note on concurrency: the morning pipeline was still writing files while this audit ran (sitemap.xml,
feed.xml, llms.txt, index.html, and the new post were all being rewritten during the pass). Each
edit below was applied with an exact-match guard and re-verified after a settle delay, so nothing
clobbered or was clobbered by the concurrent process.

## Issues found and fixed

**1. New post meta description over the SERP-safe ceiling (Nº 65).** The post shipped at 202 chars,
which the morning pipeline trimmed to 167. The house band is 146 to 162 (Google truncates around 155
to 160), so 167 still risked a cut tail in results, and the primary report's claim of "~163, inside
band" did not match the file. Trimmed to 155 by dropping the redundant "as everyone", keeping the
searched phrase "repeat customer" front-loaded and the fix intact:

> Shopify can't tell a repeat buyer from a first-timer without a manual tag, so VIPs get the same
> blast. The AI playbook that segments customers by behavior.

The twitter:description carried the same 167-char copy and was aligned to the new 155-char line for
channel consistency. The richer og:description (318 chars, intended long social copy) was left as-is.

**2. Em-dashes in authored body prose on five legacy posts.** The house style, followed by every post
from mid-June on, uses no em-dashes or en-dashes in body copy (the only dashes in a clean post are the
two template datelines, plus structural ones in the title tag, the RSS link label, and HTML/CSS
comments). Five older posts predated that style and still carried em-dashes through their prose and
their mirrored JSON-LD text:

- the-bad-address-that-ships-anyway.html (Nº 52)
- the-high-risk-flag-that-makes-you-guess.html (Nº 53)
- the-overselling-problem-no-one-automates.html (Nº 51)
- the-shopify-automations-no-one-builds.html (pillar, Nº 47-era)
- the-wismo-tickets-that-eat-your-afternoon.html (Nº 50)

Fix: converted clause-joining em-dashes to commas and numeric-range en-dashes (5–10%, $80–$120, and so
on) to hyphens, in both the visible body and the matching schema strings so the two stay in sync. The
shared template separators were protected and left untouched: the title tag separator
("— Dugong Field Notes"), the RSS link label ("Dugong Field Notes — RSS"), the HTML and CSS comments,
and the dispatch dateline ("Nº NN — DATE"). After the fix each of the five files carries exactly seven
em-dashes, all template, matching a clean post; visible body em-dashes dropped to the two dateline
instances and en-dashes to zero.

## Site-wide audit (all 18 posts) — otherwise clean

- **sitemap.xml** valid XML, full coverage (18 posts + homepage), no orphans, no entries pointing at
  missing files.
- **feed.xml** valid XML, every post present.
- **llms.txt** lists all 18 posts including Nº 65; matches disk exactly.
- **robots.txt** allows all major search and answer-engine crawlers explicitly; sitemap declared.
- **Coverage cross-check** (disk vs sitemap vs feed vs llms): all four sets identical, zero drift.
- **Meta descriptions:** all 18 unique, all now inside the 146 to 162 band.
- **Titles:** unique across the catalogue.
- **H1:** exactly one per post (18/18).
- **Canonical:** present, self-referential, HTTPS, and consistent with og:url on every post.
- **OG / Twitter cards:** present on every post, including og:image:alt and twitter:image:alt (18/18).
- **JSON-LD:** parses on every post; all carry BlogPosting + BreadcrumbList + FAQPage + HowTo (the
  pillar post intentionally omits HowTo, correct for an overview piece).
- **Image alt text:** no images missing the alt attribute.
- **Internal links:** site-wide scan of every local href across all 19 pages found 0 broken links.
  Every post has 17 inbound internal links and is linked from the homepage; no orphans.
- **Dates:** datePublished and dateModified present and sensible on every post; Nº 65 dated 2026-06-21.

## Verification

- New meta and twitter description both 155 chars, key phrase front-loaded, no em/en dashes; change
  re-read from disk after a settle delay to confirm it persisted against the concurrent writer.
- Five legacy posts: div balance unchanged (76/76 each), JSON-LD still parses, meta lengths unchanged
  and in band, visible body em-dashes reduced to the two template datelines, en-dashes to zero.
- Full re-sweep after all edits: 0 per-post issues, 0 duplicate metas, 0 broken links, sitemap and
  feed still valid XML, full coverage across sitemap/feed/llms.

## Result

Two real defects corrected: an over-length meta description on Nº 65 (167 to 155) and em-dash style
drift in five legacy posts brought in line with house style. All other SEO/GEO infrastructure verified
clean. Changes staged in the working tree only; no commit or deploy performed, consistent with prior
runs.

## Recommendation

The morning pipeline shipped Nº 65 with a 167-char meta and reported it as in-band. Worth tightening
the pipeline's meta-length gate to the 146 to 162 house ceiling so over-length descriptions are caught
before publish rather than in a second pass.
