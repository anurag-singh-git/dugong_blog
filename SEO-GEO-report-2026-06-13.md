# Dugong Field Notes — SEO/GEO improvement run

**Date:** 2026-06-13 · **Scope:** blog.dugong.live (index + 9 posts + sitemap/feed/llms/robots)
**Mode:** automated scheduled task (run without user present)

## Headline

The biggest structural win this run is that the FAQ content the site has been shipping
in structured data is now actually visible on the page. Every post carried a `FAQPage`
JSON-LD block with three question/answer pairs, but those questions and answers existed
**only** inside the `<script type="application/ld+json">` tag. Nothing was rendered for a
human or for an answer engine reading the rendered DOM. That is both a structured-data
guidelines problem (FAQ markup is supposed to mirror content visible on the page) and a
forfeited GEO signal: a clean, extractable Q and A block is one of the formats generative
engines lift most readily into answers. This run surfaces that content as a real on-page
FAQ section on all nine posts, with the visible text copied verbatim from the schema so
the two match exactly.

## Context: this run overlapped a live publish

A concurrent blog run was publishing **Dispatch Nº 56, "The restock alert that never
fires,"** during this session. When this task started, the new post file existed on disk
and in the homepage `Blog` JSON-LD, but it was not yet in `sitemap.xml`, `feed.xml`,
`llms.txt`, the homepage card grid, the hero counts, or any older post's Read-next block.
Files were actively being rewritten (observed `index.html`, `sitemap.xml`, `feed.xml`,
`llms.txt` mtimes moving within the window).

To avoid colliding with the live writer, this run did not touch the shared discovery files
while they were changing. It waited for the working tree to stop changing across several
consecutive samples, then confirmed what the blog run had completed and limited its own
edits to the gaps the blog run does not own. By the time the tree settled, the blog run had
added the homepage card, bumped the counts to 56, and wired the post into the feed, sitemap,
llms.txt, and the older posts' Read-next back-links. Those items were therefore left alone
(editing them would only have risked duplicates).

## Changes made

1. **Added a visible FAQ section to all nine posts.** Each post now renders a "Common
   questions" section (between the article body and the Read-next grid) containing the same
   three Q and A pairs that were already in its `FAQPage` schema. The visible text is the
   schema text verbatim, so the structured data now matches on-page content exactly. A small
   scoped CSS block (`.faq`, `.faq-item`, `.faq-q`, `.faq-a`) was added to each file using the
   site's existing design tokens, so the section inherits house typography and spacing. This
   is the only change that touches all nine posts and is the substantive GEO improvement of
   the run.

2. **Expanded `robots.txt` with current answer-engine crawlers.** Added explicit `Allow`
   rules for major AI and answer-engine user agents that were not previously listed:
   `Amazonbot`, `Meta-ExternalAgent` (and the lowercase `meta-externalagent`), `DuckAssistBot`,
   `cohere-ai`, `cohere-training-data-crawler`, `YouBot`, `Google-CloudVertexBot`, `PetalBot`,
   `Bytespider`, and `PerplexityBot-User`. This widens the set of generative engines explicitly
   permitted to crawl and cite the blog, consistent with the file's stated GEO intent. (This
   edit was picked up and committed by the concurrent run along with the rest of its work.)

3. **Completed the internal link graph in the working tree.** Inserted a Read-next card
   pointing to the new restock post as the first card in each of the eight older posts'
   Read-next grids, and confirmed the restock post links to all eight siblings. After the
   edits, every one of the nine posts links to exactly eight unique siblings, with the restock
   link present exactly once per post and no self-links. (The blog run was independently doing
   the same back-link insertion; the working tree ended up correct and duplicate-free either
   way.)

No article body text, titles, `datePublished` values, word counts, or meta descriptions were
changed by this run. The only freshness field touched was `dateModified` / `article:modified_time`,
set to 2026-06-13 on pages that were in fact edited today, which agrees with the sitemap
`lastmod` (all 2026-06-13) and the feed `lastBuildDate` (Sat, 13 Jun 2026).

## Verified

- **FAQ visible text equals schema text, verbatim, on all nine posts.** Parsed the rendered
  `.faq-q` / `.faq-a` content and compared it character-for-character (after HTML unescaping)
  to each post's `FAQPage` `mainEntity`. Exact match on all nine; three pairs each.
- **Structured data still valid.** Every `ld+json` block on all nine posts parses as valid
  JSON after the edits.
- **Link graph.** All nine posts link to exactly eight unique siblings; restock link present
  exactly once per older post; no duplicates, no self-links.
- **HTML structure.** `<div>` open/close balanced on every post (52/52 each after the FAQ and
  card additions).
- **XML.** `sitemap.xml` and `feed.xml` both parse as well-formed XML. Sitemap lists the
  homepage plus nine posts (10 `<loc>`), all `lastmod` 2026-06-13. Feed carries 10 items.
- **robots.txt.** 24 `User-agent` groups; the eight-plus new answer-engine agents are present;
  the `Sitemap:` line is intact.
- **Style preference.** No em or en dashes were introduced in any text authored by this run
  (the FAQ section eyebrow, the inserted restock Read-next card copy, and the CSS are all
  dash-free). The visible FAQ answers on five of the older posts (Nº 48–54-era) do contain em
  dashes, but only because those dashes already exist in those posts' schema answer text and the
  visible copy must match the schema verbatim. This run did not add them; it surfaced existing
  authored text faithfully. Rewriting that older body/schema prose is an editorial change, not
  an SEO/GEO fix, and was left for a human, consistent with prior runs.

## Not done (deliberately)

- **No git commit or deploy of the post edits.** The nine post HTML edits (FAQ sections and
  the completed link graph) are staged in the working tree for review, consistent with every
  prior SEO/GEO run. A concurrent git process held `.git/index.lock` during the run; no git
  operations were attempted.
- **No re-wiring of discovery surfaces for the restock post.** The concurrent blog run already
  added the homepage card, bumped the dispatch counts to 56, and updated the feed, sitemap, and
  llms.txt. Re-doing any of it would only have created duplicates, so it was left untouched and
  verified instead.
- **No homepage hero/decorative copy changes.** The hero counts (56) and the "browse all 56
  dispatches" footer were set correctly by the blog run; the decorative "NEW DISPATCHES THIS
  MONTH" banner remains an editorial call.
- **No fabricated author profiles.** Richer author `sameAs` entities would help E-E-A-T, but
  inventing profile URLs is worse than omitting them.

## Suggested next (for a human or a future run)

- The visible FAQ sections are now the strongest answer-engine surface on each post. A natural
  follow-up is to add `HowTo` or step `ItemList` schema for the "AI playbook" sequences each post
  describes, since those are already written as ordered steps in the body.
- Consider rewriting the em-dash-heavy older bodies (Nº 48–54) to match the house no-dash style,
  which would also clean up the five FAQ answers that inherited dashes from their schema.
