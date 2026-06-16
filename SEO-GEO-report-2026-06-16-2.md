# Dugong Field Notes — SEO/GEO improvement run

**Date:** 2026-06-16 (second run) · **Scope:** blog.dugong.live (index + 13 posts + sitemap/feed/llms/robots)
**Mode:** automated scheduled task (run without user present)

## Headline

One real defect remained after today's publish of Dispatch Nº 60 ("The sale you have to start
by hand," `the-sale-you-start-by-hand.html`): the internal link graph was incomplete. Ten older
posts did not yet back-link to Nº 60. This is the same class of issue every prior pass has caught
after a new dispatch lands, and it is now closed. After this run every one of the 13 posts links
to all 12 of its siblings, exactly once each, with no self-links.

## State at start of run

The morning blog run had already published Nº 60 and wired it into the homepage card grid, the
homepage `Blog` JSON-LD, `sitemap.xml` (14 URLs), `feed.xml` (14 items), and `llms.txt`, and bumped
the dispatch count to 60. It had also back-linked Nº 60 from the two most topically related siblings
(the abandoned-cart post and the sold-out-products post). Those discovery surfaces were correct and
were left untouched. An audit of the 13 post files surfaced the one gap below.

Audit results at start:
- Meta descriptions: all 13 in the 146–160 character range. No fix needed.
- JSON-LD: 1 valid `ld+json` block per post, all parse. No fix needed.
- Link graph: 3 posts linked all 12 siblings; 10 posts linked only 11, each missing exactly the
  link to Nº 60.

## Changes made

**Completed the internal link graph for Nº 60.** Inserted the standard Nº 60 Read-next card
(markup and copy lifted verbatim from the card the sold-out post already uses) as the first card
in the Read-next grid of the ten older posts that did not yet link to it: the-bad-address,
the-chargeback, the-high-risk-flag, the-order-change, the-overselling, the-reorder, the-restock,
the-return, the-shopify-automations, and the-wismo. The abandoned-cart and sold-out posts already
linked Nº 60 and were not touched. After the edits every one of the 13 posts links to exactly 12
unique siblings, with the Nº 60 link present exactly once per post and no self-links.

No article body text, titles, `datePublished` values, word counts, or schema blocks were changed.

## Verified

- **Link graph.** All 13 posts link to exactly 12 unique siblings each; zero self-links; the Nº 60
  link appears exactly once per older post.
- **Meta descriptions.** All 13 within the 146–160 character SERP-safe range.
- **Structured data.** Every `ld+json` block on all 13 posts parses as valid JSON after the edits
  (1 block per post).
- **HTML structure.** `<div>` open/close balanced on every post (64/64 each after the card
  insertions; +3 vs the prior 61 is the inserted card's three nested divs, matching the established
  pattern).
- **XML.** `sitemap.xml` (14 URLs) and `feed.xml` (14 items) both parse as well-formed XML and both
  include Nº 60.
- **Discovery surfaces.** `llms.txt`, `sitemap.xml`, `feed.xml`, and the homepage all reference the
  sale post; homepage reads "all 60 dispatches" and links all 13 post files.
- **Style preference.** Zero em or en dashes in the inserted cards (confirmed by scan). Older
  pre-existing dashes in some post bodies pre-date the no-dash style and were not touched, as
  rewriting authored prose is an editorial change, not an SEO/GEO fix.

## Decisions made autonomously (no user present)

- **Freshness fields left as-is.** Consistent with house behavior, `dateModified` /
  `article:modified_time` were not bumped on the ten posts that received the back-link card. The
  homepage, sitemap homepage entry, and feed `lastBuildDate` already read 2026-06-16, and Nº 60's
  own dates are 2026-06-16.
- **Separate report file.** Today's morning blog run already wrote `SEO-GEO-report-2026-06-16.md`,
  so this pass writes `SEO-GEO-report-2026-06-16-2.md` to avoid overwriting, matching the `-2`
  convention used on prior double-run days.
- **No git commit or deploy.** All edits are staged in the working tree for review, consistent with
  every prior run.

## Suggested next (for a human or a future run)

- The recurring pattern persists: each new dispatch ships with only partial back-links, then gets
  completed the next pass. Folding full back-link insertion into the blog-run step itself would
  remove this daily follow-up entirely.
- `HowTo` / step `ItemList` schema for the ordered "AI playbook" sequences each post describes in
  prose remains the largest un-captured GEO opportunity (carried over from prior runs). It is an
  additive structured-data change worth a dedicated pass.
