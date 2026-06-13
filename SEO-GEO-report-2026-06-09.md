# Dugong Field Notes — SEO/GEO improvement run

**Date:** 2026-06-09 · **Scope:** blog.dugong.live (7 posts + sitemap)
**Mode:** automated scheduled task (run without user present)

## Audit finding

The on-page foundation remains strong and was left intact: self-referential canonicals, OG/Twitter cards, valid BlogPosting / FAQPage / BreadcrumbList JSON-LD on every post, the Organization + WebSite + Blog `@graph` on the homepage, robots.txt allowing search and AI crawlers, a well-formed sitemap.xml, llms.txt, and the RSS feed added in the prior run.

The clearest remaining gap was **internal linking**, the exact item flagged as "open" in today's blog-run note. The two newest posts (Nº 53 "the order change that races your warehouse" and Nº 54 "the return that won't approve itself") had **zero inbound links** from the five older posts. Their "Read next" sections still pointed only at the original five dispatches. New content with no internal inbound links is slower for crawlers to discover and gets little internal authority, which hurts both ranking and the chance an answer engine surfaces it. Closing this is the highest-value change available without inventing content.

## Changes made

1. **Completed the internal link graph across all seven posts.** Every post now links to all six of its siblings in "Read next":
   - The five older posts (bad-address, high-risk-flag, overselling, wismo, shopify-automations) each gained two cards: Nº 54 (returns) and Nº 53 (order-change), inserted at the top of the grid so the newest content gets the most prominent inbound links.
   - The order-change post (Nº 53) gained a card to the returns post (Nº 54).
   - The returns post (Nº 54) gained a card to the high-risk-flag post, the one sibling it was still missing.
   Result: a complete 7-node link graph where each post points to the other six, no self-links anywhere.

2. **Refreshed freshness signals on the six edited posts.** `dateModified` bumped 2026-06-08 → 2026-06-09 on bad-address, high-risk-flag, overselling, wismo, shopify-automations, and order-change to match today's edits. `datePublished` left untouched on every page. (Returns was already 2026-06-09.)

3. **Synced sitemap `lastmod`.** The six edited post URLs bumped to 2026-06-09 so the sitemap matches each post's `dateModified`. Homepage and returns were already 2026-06-09.

## Verified

- **Link graph:** all 7 posts link to exactly 6 distinct siblings; 0 self-links.
- **HTML structure:** `<div>`/`</div>` balanced on every edited file (older posts 41/41, order-change 38/38, returns 38/38).
- **No broken links:** every local `.html` href across all posts and the homepage resolves to a real file (0 missing).
- **Structured data:** all 8 JSON-LD blocks (7 posts + index) still parse as valid JSON after the date edits.
- **XML:** feed.xml and sitemap.xml both parse as well-formed; sitemap lastmods confirmed at 2026-06-09 for the homepage and all 7 posts.
- **Style preference:** the inserted "Read next" cards introduce no em/en dashes; the card deks reuse existing copy and house typography (`&rsquo;`, `&ldquo;`), so the additions are visually consistent with the existing cards.

## Not done (deliberately)

- **No git commit / deploy.** Changes are staged in the working tree for review, consistent with every prior run.
- **robots.txt / sitemap do not list feed.xml.** Left as-is. Feeds are discovered via the `<link rel="alternate">` tags already present on every page; adding the feed to the sitemap is non-standard and unnecessary.
- **Decorative copy untouched.** The hero "13 NEW DISPATCHES THIS MONTH" banner and the visible WORDS tickers (which run slightly above measured body text but agree with their JSON-LD `wordCount`) are editorial calls, not SEO defects, and remain flagged for a human.
- **No fabricated author `sameAs` / external profiles.** Richer author entities would help E-E-A-T, but inventing profile URLs would be worse than omitting them.
