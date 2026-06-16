# Dugong Field Notes — SEO/GEO improvement run

**Date:** 2026-06-13 (second run of the day) · **Scope:** blog.dugong.live (10 posts)
**Mode:** automated scheduled task (run without user present)

## Headline

This run adds two machine-readable signals that the site did not have on any post:
`speakable` (a SpeakableSpecification) and `about` entity grounding. Both target answer
engines and voice surfaces specifically, and both build on the visible-FAQ work that the
earlier 2026-06-13 run shipped. Every change is a pure JSON-LD addition: no body text,
titles, dates, descriptions, or word counts were touched, and nothing was fabricated.

## Starting state (audited)

The working tree was clean and committed at the start of this run (no concurrent publish
in progress). Since the morning reports, a second blog run had published a tenth post,
**"The sold-out products that sink your collection"** (Nº 57), and wired it fully into the
homepage, sitemap (11 `<loc>`: homepage + 10 posts), feed, and llms.txt. The internal link
graph, FAQ sections, canonical/OG/Twitter tags, and robots.txt answer-engine allowlist were
all already in place from prior runs.

Each post's JSON-LD already carried `BlogPosting`, `BreadcrumbList`, `FAQPage`, `Organization`,
`Person`, and `ImageObject` nodes. Two recognized GEO signals were absent everywhere:
`speakable` and `about`. Those are the gaps this run closed.

The "AI playbook" sequences each post describes are written as prose, not as ordered `<ol>`
steps (confirmed: zero `<ol>` elements across all 10 posts). Adding `HowTo`/`ItemList` step
schema, suggested by the prior run, would require inventing a numbered step list that does not
exist in the body. That is an editorial rewrite, not an SEO fix, so it was deliberately not done.

## Changes made

1. **Added `speakable` (SpeakableSpecification) to all 10 posts.** Each post's `BlogPosting`
   node now carries:

   ```json
   "speakable": {
     "@type": "SpeakableSpecification",
     "cssSelector": [".article-title", ".faq"]
   }
   ```

   Both selectors point at content that already exists and is already visible on the page: the
   `<h1 class="article-title">` headline and the on-page `.faq` "Common questions" section that
   the earlier run surfaced. This tells answer engines and voice assistants which parts of the
   page are best suited to be read aloud or lifted into a spoken answer, without changing any
   visible content.

2. **Added `about` entity grounding to all 10 posts.** Each `BlogPosting` node now declares the
   three real-world entities every post is genuinely about, each linked to its authoritative
   Wikipedia page via `sameAs`:

   ```json
   "about": [
     { "@type": "Thing", "name": "Shopify", "sameAs": "https://en.wikipedia.org/wiki/Shopify" },
     { "@type": "Thing", "name": "E-commerce", "sameAs": "https://en.wikipedia.org/wiki/E-commerce" },
     { "@type": "Thing", "name": "Business process automation", "sameAs": "https://en.wikipedia.org/wiki/Business_process_automation" }
   ]
   ```

   This is entity-based grounding: it lets search and generative engines disambiguate what the
   blog covers and connect it to known entities in their knowledge graphs, which strengthens
   topical authority and the odds of being cited for Shopify-automation queries. The three
   entities apply truthfully to every post (all 10 are field notes on automating Shopify
   e-commerce operations), so the same set was used site-wide. The `Business process automation`
   target was fetched and confirmed live this run; `Shopify` and `E-commerce` are long-standing
   stable Wikipedia articles.

No `dateModified` / `article:modified_time` values were changed. They already read 2026-06-13
on every post (set by the earlier run), which still matches every `sitemap.xml` `lastmod`
(2026-06-13) and the feed `lastBuildDate`, so no freshness signal was inflated or made
inconsistent.

## Verified

- **Pure additions, nothing removed.** `git diff` shows 90 insertions, 0 deletions across the
  10 post files (9 added lines each). No existing line was modified.
- **JSON-LD still valid.** Every `application/ld+json` block on all 10 posts parses as valid
  JSON after the edits (one block per post).
- **Exactly one of each new property per post.** All 10 posts have `speakable` × 1, `about` × 1,
  and `SpeakableSpecification` × 1. The `cssSelector` targets (`.article-title`, `.faq`) each
  exist exactly once in every post, so both selectors resolve.
- **HTML structure unchanged.** `<div>` open/close balance is identical to before on every post
  (52/52, or 55/55 on the three longer FAQ posts). No markup was opened or closed.
- **Style preference honored.** No em or en dashes were introduced. The only hyphen in the new
  text is the standard spelling "E-commerce" (a normal hyphen-minus, not an en/em dash).
- **No concurrent-run collision.** Discovery files (`sitemap.xml`, `feed.xml`, `llms.txt`,
  `index.html`, `robots.txt`) were not touched; they were already complete for all 10 posts.

## Not done (deliberately)

- **No `HowTo` / `ItemList` step schema.** The posts have no ordered step lists in the body;
  generating one would fabricate structure. Left for an editorial pass.
- **No git commit or deploy.** The 10 post edits are staged in the working tree for review,
  consistent with every prior run. A concurrent git process held `.git/index.lock`; no git
  operations were attempted.
- **No homepage schema change.** The homepage already carries `WebSite`, `Blog`, and
  `Organization`. A `SearchAction` was considered and skipped because the site has no on-site
  search to point it at (it would be a misleading signal).
- **No fabricated author/Organization `sameAs`.** Inventing social-profile URLs to boost
  E-E-A-T is worse than omitting them; left for a human with the real handles.

## Suggested next (for a human or a future run)

- If the "AI playbook" in each post is rewritten as an explicit numbered step list in the body,
  that ordered content could then carry honest `HowTo` schema, which answer engines lift readily.
- Add real `sameAs` profiles to the `Organization` and author `Person` nodes once authentic URLs
  are available, to firm up E-E-A-T.
- Consider a per-post primary `about` entity (e.g. "Inventory control" or "Chargeback") layered
  on top of the three shared ones, for finer-grained topical targeting.
