# Dugong Field Notes — SEO/GEO improvement run

**Date:** 2026-06-10 · **Scope:** blog.dugong.live (index + 7 posts)
**Mode:** automated scheduled task (run without user present)

## Audit finding

The on-page foundation is strong and was left intact: self-referential canonicals, OG/Twitter cards, valid BlogPosting / FAQPage / BreadcrumbList JSON-LD on every post, the Organization + WebSite + Blog `@graph` on the homepage, a complete 7-node internal link graph (each post links to its six siblings, no self-links), robots.txt allowing search and AI crawlers, well-formed sitemap.xml, llms.txt, and the RSS feed. Meta-description lengths are all within the SERP limit (100 to 159 chars), titles are unique, and there are no `<img>` tags to need alt text (the design uses CSS art and emoji glyphs).

Two concrete metadata gaps remained in the page `<head>`:

1. **No `article:modified_time` Open Graph tag on any post.** Every post carried `article:published_time` but none carried the matching `article:modified_time`, even though the JSON-LD already declared a `dateModified` of 2026-06-09 on all seven. The freshness signal existed in the structured data but not in the Open Graph metadata that social and answer-engine crawlers read first. This is the cleanest freshness win available without touching content.

2. **No image alt text on the Open Graph / Twitter card image** across all eight pages. The shared `og-image.png` (the "Workflows, thought through." brand banner) was referenced with width and height but no `og:image:alt` or `twitter:image:alt`. Adding accurate alt text improves accessibility and gives crawlers and AI answer engines a text description of the social preview image.

Neither fix requires inventing facts: the modified time mirrors the existing `dateModified`, and the alt text describes an image that already exists.

## Changes made

1. **Added `article:modified_time` to all 7 posts.** Inserted directly after each post's existing `article:published_time` tag, with the value copied from that post's JSON-LD `dateModified` (2026-06-09 on every post). Open Graph now exposes both publish and modified times, and they agree with the structured-data dates.

2. **Added `og:image:alt` and `twitter:image:alt` to all 8 pages** (index + 7 posts). The alt text accurately describes the brand banner: the heading "Workflows, thought through.", the tagline about AI-native workflow automation, and the blog.dugong.live URL shown on the card. The same image is shared across all pages, so one accurate description applies to each.

No `datePublished` / `dateModified`, sitemap `lastmod`, feed, llms.txt, or article content was changed. The edits only add metadata that reflects state already present on each page, so no freshness date was inflated.

## Verified

- **Coverage:** `article:modified_time` on 7/7 posts; `og:image:alt` and `twitter:image:alt` on 8/8 pages.
- **Date consistency:** on every post, `og:published_time` = schema `datePublished`, and the new `og:modified_time` = schema `dateModified` (2026-06-09). No mismatches.
- **Structured data:** all 8 JSON-LD blocks still parse as valid JSON after the head edits.
- **HTML structure:** `<div>` open/close balanced on every file (index 131/131; the four "41" posts 41/41; order-change and returns 38/38).
- **Style preference:** the new alt text contains no em/en dashes and uses house typography (`&ldquo;`/`&rdquo;`); confirmed zero em/en dashes across all added `image:alt` lines.

## Not done (deliberately)

- **No git commit / deploy.** Changes are staged in the working tree for review, consistent with every prior run.
- **No date bumping.** Since today's edits add metadata rather than change article content, `dateModified`, sitemap `lastmod`, and the feed were left at 2026-06-09 to keep freshness signals truthful.
- **No fabricated author `sameAs` / external profiles.** Richer author entities would help E-E-A-T, but inventing profile URLs would be worse than omitting them.
- **Decorative copy untouched.** The hero "13 NEW DISPATCHES THIS MONTH" banner and the visible WORDS tickers (which agree with each page's JSON-LD `wordCount`) are editorial calls, not SEO defects, and remain flagged for a human.
