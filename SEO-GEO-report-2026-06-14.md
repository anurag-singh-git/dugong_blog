# Dugong Field Notes — SEO/GEO improvement run

**Date:** 2026-06-14 · **Scope:** blog.dugong.live (index + 11 posts + sitemap/feed/llms/robots)
**Mode:** automated scheduled task (run without user present)

## Headline

Two real defects left behind by today's publish of Dispatch Nº 58 ("The abandoned cart
that gets one email") were found and fixed: an over-length meta description on the new post,
and an incomplete internal link graph (nine older posts did not yet back-link to Nº 58).
Both are the same class of issue prior QA passes have caught after a new dispatch lands, and
both are now closed. After this run every post links to all ten siblings and every meta
description is within the SERP limit.

## State at start of run

The daily blog run had already published Dispatch Nº 58 and wired it into the homepage card
grid, the homepage `Blog` JSON-LD (12 entries), `sitemap.xml` (12 URLs), `feed.xml`
(12 items), and `llms.txt`, and bumped the dispatch counts to 58. It had also back-linked
Nº 58 from the two most topically related siblings (the restock post and the WISMO post).
The discovery surfaces were therefore correct and were left untouched (re-editing them would
only risk duplicates). An audit of the 11 post files surfaced the two gaps below.

## Changes made

1. **Trimmed the Nº 58 meta description from 192 to 160 characters.** The new abandoned-cart
   post shipped with a `<meta name="description">` of 192 characters, over the ~160 limit
   every other page on the site respects (and the same defect QA fixed on Nº 57 yesterday).
   Rewritten without losing meaning to 160 chars: "Shopify sends one generic abandoned
   checkout email and stops: no sequence, no personalization, often no contact saved. The AI
   playbook that recovers more carts." No dashes introduced. All eleven meta descriptions are
   now in the 146–160 range.

2. **Completed the internal link graph for Nº 58.** Inserted the standard abandoned-cart
   Read-next card (markup and copy verbatim from the card the restock post already uses) as
   the first card in the Read-next grid of the nine older posts that did not yet link to it:
   the-bad-address, the-chargeback, the-high-risk-flag, the-order-change, the-overselling,
   the-return, the-shopify-automations, the-sold-out, and the-wismo... (wismo and restock
   already linked it). After the edits every one of the eleven posts links to exactly ten
   unique siblings, with the Nº 58 link present exactly once per post and no self-links.

No article body text, titles, `datePublished` values, or word counts were changed.

## Verified

- **Link graph.** All 11 posts link to exactly 10 unique siblings each; no self-links; the
  Nº 58 link appears exactly once per older post.
- **Meta descriptions.** All 11 in the 146–160 character range (the new post now 160, down
  from 192).
- **Structured data.** Every `ld+json` block on all 11 posts parses as valid JSON after the
  edits (1 block per post).
- **HTML structure.** `<div>` open/close balanced on every post (58/58 each after the card
  insertions; the +3 vs the prior 55 is the card's three nested divs, matching the pattern
  used for the Nº 57 back-link pass).
- **XML.** `sitemap.xml` (12 URLs) and `feed.xml` (12 items) both parse as well-formed XML
  and both include Nº 58.
- **Discovery surfaces.** `llms.txt`, `sitemap.xml`, `feed.xml`, and the homepage all
  reference the abandoned-cart post; homepage archive link reads "browse all 58 dispatches."
- **Style preference.** Zero em or en dashes in any text this run authored (the inserted
  Read-next card and the rewritten meta description are both dash-free, confirmed by scan).
  The en dashes that remain in some older post bodies pre-date the no-dash style and were not
  touched; rewriting that authored prose is an editorial change, not an SEO/GEO fix.

## Decisions made autonomously (no user present)

- **Freshness fields left as-is.** Today's blog run edited the restock and WISMO posts (to
  add the Nº 58 back-link) but deliberately did not bump their `dateModified` /
  `article:modified_time` off 2026-06-13. To stay consistent with that house behavior and to
  avoid freshness inflation, this run did not bump `dateModified` on the nine posts it edited
  with the same kind of link-card addition. The homepage, sitemap homepage entry, and feed
  `lastBuildDate` already read 2026-06-14, and the new post's own dates are 2026-06-14.
- **No git commit or deploy.** All edits are staged in the working tree for review, consistent
  with every prior run.

## Suggested next (for a human or a future run)

- The recurring pattern is that each new dispatch ships with an over-length meta description
  and only partial back-links, then gets cleaned up the next day. Folding the meta-length check
  and the full back-link insertion into the blog-run step itself would remove this daily
  follow-up entirely.
- `HowTo` or step `ItemList` schema for the ordered "AI playbook" sequences each post already
  describes in prose remains the largest un-captured GEO opportunity (carried over from prior
  runs). It is an additive structured-data change worth a dedicated pass.
