# Dugong Field Notes — SEO/GEO improvement run

**Date:** 2026-06-06 · **Scope:** blog.dugong.live (5 posts + homepage)

## Audit finding

The blog's technical foundation was already strong: per-post canonical tags, OpenGraph + Twitter cards, `BlogPosting` / `Person` / `Organization` / `BreadcrumbList` / `FAQPage` JSON-LD, a clean `robots.txt` (AI crawlers explicitly allowed), `sitemap.xml`, and a well-written `llms.txt`. Word counts (4,300–5,900) and heading structure were healthy.

The one material weakness was **internal linking asymmetry**: because posts were published in sequence, each "Read next" block only linked to *older* articles. The two newest posts (`bad-address`, `high-risk`) received almost no inbound internal links, and the homepage's cornerstone essay was absent from `llms.txt`.

## Changes made

1. **Completed the internal link graph.** Every post's "Read next" block now links to all four sibling articles (was 1–3, chronological only). Each post now has 4 inbound internal links. This spreads link equity evenly and gives generative engines fuller related-context when citing any single post.

2. **Made the related-posts grid responsive.** `.related-grid` changed from a fixed 3-column layout to `repeat(auto-fit, minmax(248px, 1fr))` so the new 4-card set wraps cleanly. Footer layout left untouched.

3. **Refreshed freshness signals.** Bumped `dateModified` (JSON-LD) and `sitemap.xml` `lastmod` to 2026-06-06 for the three edited older posts so they match; `datePublished` left unchanged.

4. **Added the homepage essay to `llms.txt`.** "The death of the drag-and-drop builder" (Dispatch Nº 47) is the site's full lead essay but was missing from the AI-crawler index; it's now listed first.

## Verified

All JSON-LD blocks parse as valid JSON; `sitemap.xml` is well-formed; link graph confirmed complete (every post → 4 siblings); `dateModified` and `lastmod` match on all edited posts.

## Not done (deliberately)

- No git commit/deploy — changes are staged in the working tree for review.
- Did not fabricate external citations for the statistics in the posts (sources unknown).
- Left the homepage's two `<h1>` tags as-is (HTML5-valid; Google tolerates multiple h1s) to avoid CSS/visual regressions.
