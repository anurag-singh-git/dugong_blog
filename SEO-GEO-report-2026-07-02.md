# SEO / GEO report — 2026-07-02 (internal-link mesh completion pass)

**Mode:** automated scheduled task (autonomous; no user present)
**Scope:** technical SEO/GEO audit of the whole site + fix the one real gap found

## What this run did

This was a maintenance/optimization pass, not a new-post run. The site was audited end to end,
one concrete gap was found and fixed, and everything was re-verified.

## Audit findings (before changes)

On-page SEO and GEO are already complete on all 26 posts:

- Every post has a unique title, meta description, canonical, OG + Twitter cards, and clean
  heading hierarchy (exactly one H1 each).
- Every post carries full structured data: BlogPosting, FAQPage, BreadcrumbList, and speakable.
  All 25 how-to posts also carry HowTo schema; the lead essay (best-shopify-automations) correctly
  omits HowTo, as it is a listicle rather than a procedure.
- All JSON-LD blocks parse cleanly across every post.
- No images are missing alt text (the posts use no `<img>` tags; art is inline SVG/glyphs).
- sitemap.xml and feed.xml are valid XML, each covering all 27 URLs (homepage + 26 posts).
- sitemap, feed, llms.txt, and index.html all reference every post. No orphans, no missing entries.
- Zero broken internal `.html` links across the whole site.

**The one real gap:** internal link mesh incomplete for the newest post.

The site's established structure is a complete mesh: every post's "Read next" block links every
sibling (24 cards per older post). When the newest post (the card-testing attack, Nº 73, published
2026-07-01) was added, only 1 of 25 siblings (the high-risk-flag post) was updated to link back to
it. The other 24 posts still had 24-card blocks and did not link the newest post. That starves the
newest, hardest-to-rank page of internal link equity and slows its discovery/crawl, and it breaks the
uniform mesh the rest of the site relies on.

## Change made

Added the card-testing "Read next" card to all 24 posts that were missing it, inserted as the first
card in each post's `related-grid` (newest-first, matching how the high-risk post was already wired).
The card markup is byte-for-byte the canonical card already used on the high-risk post: same slug,
title, dek, tags, read-time, and date.

Result: the newest post now receives internal links from all 25 siblings (was 1), and every post on
the site again has a uniform 25-card Read-next mesh.

Files changed: 24 post HTML files (the two that already linked the newest post were skipped).
No changes to sitemap.xml, feed.xml, llms.txt, robots.txt, or index.html — those were already
consistent and correct.

## Verification (all passing)

- Back-links to the newest post: 25 of 25 siblings (was 1 of 25).
- Card counts: every post now has exactly 25 cards in its Read-next block (uniform mesh restored).
- No self-links introduced in any post.
- All `<div>` tags balanced in every edited file.
- Zero broken internal `.html` links site-wide after the edit.
- JSON-LD still parses cleanly on all 26 posts (the edit only touched body HTML, not schema).
- Diff audit: the only content added was the card block, appearing exactly 24 times; no other lines
  changed.
- User style preference honored: zero em/en dashes in any added line (verified against the diff).
  The em/en dashes that remain in these files are all pre-existing template regions (CSS comments,
  the dispatch-number ticker), unchanged and cross-page-consistent.

## Open items left for review (not changed)

- Nothing outstanding on internal linking. The mesh is now complete and uniform.
- All changes are staged in the working tree only; no git commit or deploy was performed, consistent
  with prior runs.
