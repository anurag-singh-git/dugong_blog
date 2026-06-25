# SEO / GEO report — 2026-06-23

**Scope:** blog.dugong.live — index + 19 posts + feed / sitemap / llms / robots / CNAME
**Mode:** automated scheduled run (autonomous, no user present)

## Result: one real defect found and fixed — stale dispatch count on the homepage ticker

The homepage marquee ticker advertised "17 NEW DISPATCHES THIS MONTH", but 18 posts carry a
`datePublished` in June 2026. The count was accurate at 17 through the 06-21 publish, then Dispatch
Nº 66 ("The review request you never send") shipped on 06-22 and the ticker was not bumped, leaving it
short by one. This is a visible, factually wrong number on the most-crawled page of the site, the kind
of claim an answer engine can lift verbatim into a response, so it was corrected to 18.

## Defect: ticker undercounted June dispatches by one

The ticker uses the standard duplicated-track CSS marquee pattern, so the phrase appears twice
(lines 673 and 677 of index.html). Both spans read "17 NEW DISPATCHES THIS MONTH".

June 2026 posts by `datePublished` (18 total):

- 06-04 wismo, 06-05 overselling, 06-06 bad-address, 06-06 high-risk-flag, 06-08 order-change,
  06-09 return, 06-11 chargeback, 06-13 restock-alert, 06-13 sold-out, 06-14 abandoned-cart,
  06-15 reorder, 06-16 sale, 06-17 meta-description, 06-18 order-tag, 06-19 product-descriptions,
  06-20 image-alt-text, 06-21 repeat-customer, 06-22 review-request.

The only non-June post is the pillar essay (`the-shopify-automations-no-one-builds.html`, 2026-05-28),
correctly excluded from a "this month" count.

**Fix:** both ticker spans updated 17 → 18 with a single `replace_all` edit. Net diff: 1 file changed,
2 insertions, 2 deletions, no other lines touched.

## Verification (post-fix re-sweep)

- **Ticker:** "18 NEW DISPATCHES THIS MONTH" x2; "17 ..." x0.
- **Structure intact:** index.html `<div>` balance 167/167; both JSON-LD blocks still parse.
- **Other count surfaces unchanged and consistent:** "browse all 66 dispatches" archive link and the
  hero ISSUE Nº 66 / JUN 22 2026 still agree with the newest post (the 66 figure is the all-time
  dispatch count, distinct from the 18 published this month, both now correct).

## Site-wide audit (everything else clean)

- **Post count:** 19 posts on disk.
- **Internal-link graph:** complete and uniform. Every post's `.related-grid` carries all 18 siblings;
  in-degree is 18 across every post (no under-linked page). index.html links all 19 posts. The Nº 66
  back-link propagation flagged as an open item on 06-22 is now fully resolved across the catalogue.
- **Coverage cross-check** (disk vs sitemap vs feed vs llms): all four sets identical, 19 posts, zero
  drift. sitemap has 20 `<loc>` (19 posts + homepage); feed has 20 `<item>` (19 posts + lead essay).
- **XML validity:** sitemap.xml and feed.xml both parse as valid XML. robots.txt sitemap line intact.
- **Meta descriptions:** all 19 unique, all inside the 146–162 house band.
- **Titles:** all 19 unique.
- **H1:** exactly one per post (19/19).
- **Canonical:** present and equal to og:url on every post.
- **OG / Twitter cards:** present on every post including og:image:alt and twitter:image:alt (19/19).
- **JSON-LD:** parses on all 19 posts (BlogPosting + BreadcrumbList + FAQPage + HowTo; the pillar post
  intentionally omits HowTo, correct for an overview piece) and on index (WebSite + Organization + Blog,
  20 BlogPosting entries = lead essay + 19 posts).
- **Image alt text:** no `<img>` missing an alt attribute.
- **Dates:** datePublished and dateModified present and sensible on every post; dateModified >=
  datePublished holds everywhere.
- **Feed:** valid XML, lastBuildDate present (Mon, 22 Jun 2026).
- **En dashes:** zero across all 19 post files, consistent with the user style preference.
- **Discovery assets:** og-image.png, favicon.png, favicon.svg, apple-touch-icon.png all present.

## Reviewed and intentionally not changed

- **feed lastBuildDate and sitemap homepage lastmod (2026-06-22):** left as-is. No new content shipped
  today and no article body changed, so the freshness timestamps should continue to reflect the last
  real publish (06-22). Bumping them with no content change would send a misleading freshness signal.
- **Static "DISPATCH OF THE WEEK" / "NEW THIS WEEK" decorative copy:** left as-is, consistent with prior
  runs. These are phrasing, not numeric claims; the ticker fix above was made because it stated a
  specific count that had gone stale.
- **dateModified across posts:** untouched; no article-content edits were made.

## Recommendation

The ticker undercount is the same class of "new post shipped but a secondary surface not propagated" gap
flagged on 06-21 (meta-length gate) and 06-22 (related-grid). The publish pipeline already updates the
hero Nº, the "dispatches published" stat, and the "browse all N" archive link on publish; the
"N NEW DISPATCHES THIS MONTH" ticker should be added to that same set so the monthly count moves with
each publish (and resets on the first publish of a new month). That closes the last per-publish counter
that is currently updated by audit instead of at publish time.

## Note

Change staged in the working tree only; no git commit or deploy performed, consistent with prior runs.
