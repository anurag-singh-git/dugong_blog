# Dugong Field Notes — SEO/GEO improvement run

**Date:** 2026-06-07 · **Scope:** blog.dugong.live (homepage + 5 posts)

## Audit finding

The foundation remains strong (canonicals, OG/Twitter cards, BlogPosting/FAQPage JSON-LD, robots.txt with AI crawlers allowed, sitemap.xml, llms.txt, complete internal link graph from the 2026-06-06 run). Two open items from the previous QA report were still outstanding, plus one new finding: **all five** post meta descriptions exceeded Google's ~160-char render limit (239–324 chars), not just the bad-address post.

## Changes made

1. **Tightened all 5 post meta descriptions to 156–159 chars.** Each keeps its primary keywords (Shopify, the pain point, "AI playbook") and now renders without truncation in search snippets. OG and Twitter descriptions left unchanged (those limits are looser and they were fine).

2. **Added the homepage lead essay to the JSON-LD @graph.** "The death of the drag-and-drop builder" (Dispatch Nº 47, Aanya Rao, 2026-05-28) is now the first `BlogPosting` in the Blog's `blogPost` array, with description, author + jobTitle, publisher, image, and date. Generative engines citing the homepage essay can now attribute it correctly — this closes the gap the previous QA run flagged.

3. **Refreshed freshness signals.** `dateModified` (all 5 posts) and sitemap `lastmod` (all 6 URLs) bumped to 2026-06-07 to match today's edits; `datePublished` untouched.

## Verified

- All meta descriptions ≤160 chars (156–159).
- All JSON-LD blocks across the 6 pages parse as valid JSON; homepage `blogPost` array now lists 6 entries with correct authors.
- `sitemap.xml` well-formed; `lastmod` matches `dateModified` on every post.
- llms.txt checked — already accurate and complete (no change needed).

## Not done (deliberately)

- No git commit/deploy — changes staged in the working tree for review, consistent with prior runs. (Note: the favicon additions from earlier today are also still uncommitted.)
- og:/twitter: descriptions left as-is (within platform limits).
- No external citations fabricated for in-post statistics.
