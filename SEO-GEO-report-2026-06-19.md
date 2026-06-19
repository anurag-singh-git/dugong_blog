# Dugong Field Notes — SEO/GEO improvement run

**Date:** 2026-06-19 · **Scope:** blog.dugong.live (index + 15 posts + sitemap/feed/llms/robots/CNAME)
**Mode:** automated scheduled task (autonomous; no user present)

## Headline

The blog arrived at this run fully optimized: complete structured data, a complete 14-sibling
internal link graph, in-range unique meta on every page, clean discovery surfaces, and HowTo schema
on all 13 procedure posts. The audit turned up one real, un-addressed gap. Every page declared its
`BlogPosting` image as a bare URL string and its publisher `logo` as an `ImageObject` with no
dimensions. Google's Article and logo structured-data guidance recommends explicit image dimensions,
and answer engines use a typed image object with size to decide what to surface and quote. This run
upgraded both across all 16 pages. Nothing else needed fixing.

## State at start of pass

- All 16 pages (index + 15 posts) parse their JSON-LD cleanly. The 13 procedure posts carry
  `BlogPosting` + `BreadcrumbList` + `FAQPage` + `HowTo` (+ `SpeakableSpecification` and Wikipedia
  `sameAs` entity links on `about`); the pillar post correctly omits `HowTo`.
- Meta descriptions all unique and within range (100–162 chars). One H1 per page. Titles unique.
- Internal link graph complete: every post links exactly 14 unique siblings, zero self-links.
- `dateModified` matches sitemap `lastmod` on every post. sitemap.xml and feed.xml are well-formed,
  16 URLs / 16 items each. robots.txt allows the full set of AI/answer-engine crawlers and points at
  the sitemap. llms.txt references all 15 posts plus the lead essay with rich per-post summaries.
- **Gap found:** the `BlogPosting.image` was a plain string (`"image": "…/og-image.png"`) and the
  publisher `logo` `ImageObject` had `url` only, no `width`/`height`.

## Changes made

**Typed article image with explicit dimensions (16 pages).** Replaced the bare-string
`"image": "https://blog.dugong.live/og-image.png"` with a full `ImageObject` carrying the real asset
dimensions:

> `"image": { "@type": "ImageObject", "url": "https://blog.dugong.live/og-image.png", "width": 1200, "height": 630 }`

**Publisher logo dimensions (16 pages).** Added `"width": 1200, "height": 630` to the publisher
`logo` `ImageObject` on every post and the homepage. og-image.png is genuinely 1200×630, verified
from the file header, so the declared dimensions are faithful, not invented.

These are the dimensions Google's structured-data documentation recommends supplying, and a typed,
sized image object gives generative engines a cleaner signal for what image represents the page. The
edit is mechanical, reversible, and changes no visible content, prose, dates, word counts, meta, FAQ
text, HowTo steps, or discovery surfaces.

## Verified after the change

- **JSON-LD.** All 16 pages still parse. Each page now exposes exactly two `ImageObject` nodes
  (publisher logo + article image), both with `width`/`height`.
- **Dimensions present.** `"width": 1200` confirmed in all 16 files.
- **HTML structure.** `<div>` balanced on every page (index and all 15 posts).
- **Style.** No em or en dashes introduced (dimensions are numeric literals).
- **Discovery surfaces.** sitemap.xml and feed.xml still well-formed XML, 16 URLs / 16 items.
- **Untouched, re-confirmed clean.** Meta lengths 100–162, single H1 per page, complete 14-sibling
  link graph with zero self-links, `dateModified` == sitemap `lastmod`, HowTo on all 13 procedure
  posts, robots.txt crawler allow-list and sitemap line.

## Decisions made autonomously

- **ImageObject over bare string.** The documented best form for Article `image`; supplying real
  dimensions improves rich-result eligibility and gives answer engines a typed image to anchor on.
- **Kept the existing og-image asset as both article image and logo.** Declaring true dimensions is
  safe and additive; swapping in a different/square logo asset would be a design decision requiring a
  new file, so it was left to a human. (See suggested next.)
- **No new post authored.** Authoring is the separate blog-run task's job; today carried no new
  dispatch, so the post count stays at 15 and discovery surfaces were not re-dated.
- **No git commit or deploy.** All edits are staged in the working tree for review, consistent with
  every prior run.

## Suggested next

- **Fold typed-ImageObject `image` + logo dimensions into the blog-run template.** New posts ship
  with the bare-string image; generating the `ImageObject` at authoring time removes this from future
  audits, the same way HowTo and full back-link insertion were flagged to move into the blog run.
- **Consider a dedicated square logo asset.** The Organization `logo` reuses the 1200×630 banner; a
  purpose-built squarish logo would better match Google's logo guidance. Needs a new asset, so it is
  a human/design call, not an automated fix.
- **Older posts predating the no-dash preference** still carry em/en dashes in body prose
  (bad-address, high-risk, overselling, shopify-automations, wismo). Rewriting risks altering meaning,
  so it stays an editorial decision out of scope for an automated pass.
- **Validate in a rich-results tester.** A human with browser access can confirm the new sized
  `ImageObject`, plus the existing HowTo and FAQPage, on a couple of live URLs.
