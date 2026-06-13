# Dugong Field Notes — SEO/GEO improvement run

**Date:** 2026-06-08 · **Scope:** blog.dugong.live (homepage + 5 posts + config files)
**Mode:** automated scheduled task (run without user present)

## Audit finding

The on-page foundation is already strong and was left intact: self-referential canonicals, OG/Twitter cards, BlogPosting / FAQPage / BreadcrumbList JSON-LD, an Organization + WebSite + Blog `@graph`, robots.txt allowing search and AI crawlers, sitemap.xml, and llms.txt.

The clearest remaining gap was content discovery: every page footer advertises an **RSS** link, but no feed existed and the links pointed nowhere useful (`href="#"` on the homepage, `https://dugong.live` on the posts). No page declared a feed for crawlers or readers. An RSS feed is a standard discovery surface for both search and answer engines, so this was the highest-value missing asset. I also closed a copy inconsistency that the last two QA runs flagged but did not change.

## Changes made

1. **Created `/feed.xml` (RSS 2.0).** Full feed with all six dispatches (5 posts + the homepage lead essay), each with title, canonical link, permalink `guid`, `pubDate` (RFC-822), `dc:creator`, category, and the post's meta description. Channel block includes self-referencing `atom:link`, language, copyright, image, and `lastBuildDate`. The lead-essay item uses a non-permalink guid matching its homepage JSON-LD `@id` (`#dispatch-47`) so engines attribute it to the existing entity.

2. **Declared the feed on every page.** Added `<link rel="alternate" type="application/rss+xml" href="/feed.xml" />` to all six `<head>` blocks so browsers and crawlers can auto-discover it.

3. **Pointed the footer RSS links at the real feed.** All seven `RSS` links (2 on the homepage, 1 per post) now resolve to `/feed.xml` instead of `#` or the product domain.

4. **Listed the feed in `llms.txt`.** Added a `## Resources` section pointing answer engines at the RSS feed and sitemap for fresh content.

5. **Resolved the dispatch-count inconsistency.** The masthead reads "ISSUE Nº 52" but the homepage still said "48 dispatches published" and "browse all 48 dispatches" — flagged in the 06-06 and 06-07 QA runs. With the task instructing me to act and note reasonable choices: assuming the published count tracks the latest issue number, I set both spots to **52** so the visible facts agree (consistent signals help E-E-A-T / GEO credibility).

6. **Refreshed freshness signals.** `dateModified` (all 5 posts) and sitemap `lastmod` (all 6 URLs) bumped to 2026-06-08 to match today's edits. `datePublished` left untouched on every page.

## Verified

- `feed.xml` and `sitemap.xml` both parse as well-formed XML.
- All six JSON-LD `@graph` blocks still parse as valid JSON after the head edits.
- Every feed `<item>` link resolves to a real local file (5 posts); lead-essay item points to the homepage.
- Feed item count = 6; all `datePublished` values unchanged; `dateModified` / `lastmod` consistent at 2026-06-08.
- No stray "48" left in the homepage copy; head structure intact on all pages.

## Not done (deliberately)

- **No git commit / deploy** — changes staged in the working tree for review, consistent with prior runs. (Earlier uncommitted favicon work also remains in the tree.)
- **Word-count tickers** (e.g. "2,040 WORDS" vs ~1,400 rendered) left as-is. They match their JSON-LD `wordCount`, so the machine-readable and visible numbers agree; recutting visible body counts is an editorial call, not an SEO defect. Flagged again for a human.
- **No fabricated author `sameAs` / external profiles.** Richer author entities would help E-E-A-T, but inventing profile URLs would be worse than omitting them.
