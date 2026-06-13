# Dugong Field Notes — SEO/GEO improvement run

**Date:** 2026-06-11 · **Scope:** blog.dugong.live (index + 8 posts + sitemap)
**Mode:** automated scheduled task (run without user present)

## Audit finding

This morning's blog run published Dispatch Nº 55, "The chargeback you lose by default,"
and wired it into the index, sitemap, llms.txt, feed, and JSON-LD. It left one gap, which
that run flagged itself: the new post was reachable from the homepage and the machine-readable
files, but **no existing post linked back to it**. The internal "Read next" graph had not been
updated, so the freshest content sat outside the post-to-post link structure that search and
answer engines follow to gauge topical relationships and authority.

A full pass over the eight posts showed the link graph was actually short in two places:

1. **The new chargeback post (Nº 55) had zero inbound links from sibling posts.** All seven
   older posts still pointed only at the original six siblings. The newest dispatch was an
   internal-linking orphan apart from the homepage card.

2. **The pillar post, "The Shopify automations no one builds," was missing from three posts'
   Read-next blocks** (the chargeback post, the order-change post, and the returns post). Those
   three carried only five Read-next cards instead of the six the other posts had. This was a
   pre-existing gap, not introduced today, but it weakened the link equity flowing to the one
   post most useful as a topic hub.

Neither fix invents anything. Both cards describe posts that already exist, using copy drawn
from each post's own title, dek, read time, date, and author.

## Changes made

1. **Completed the internal link graph.** Every post now links to all seven of its siblings,
   with no self-links. Specifically:
   - Added a "chargeback you lose by default" Read-next card to the seven posts that lacked it
     (bad-address, high-risk-flag, order-change, overselling, returns, shopify-automations,
     wismo). The new post now has eight inbound links: seven sibling posts plus the homepage.
   - Added a "Shopify automations no one builds" Read-next card to the three posts that were
     missing the pillar (chargeback, order-change, returns).
   - The new cards use the standard `.card` markup and slot in first inside each
     `.related-grid`, so the newest and the hub posts surface at the top of Read-next.

2. **Refreshed truthful freshness signals on the seven genuinely edited older posts.** Because
   each of those pages actually changed today (a new internal-link card was added), bumped each
   post's JSON-LD `dateModified` and its `article:modified_time` Open Graph tag from 2026-06-09
   to 2026-06-11, and bumped the matching `sitemap.xml` `lastmod` to 2026-06-11. The chargeback
   post was left at its existing 2026-06-11 date since it was already published today.

No article body text, titles, meta descriptions, word counts, `datePublished` values, the feed,
llms.txt, or robots.txt were changed. The only date moved is `dateModified` / modified-time /
`lastmod`, and only on pages that were in fact modified today, so no freshness signal is inflated.

## Verified

- **Link graph:** all eight posts now link to exactly seven unique siblings with zero self-links.
- **Inbound to Nº 55:** eight pages now link to the chargeback post (7 posts + index), up from
  one (index only).
- **No broken links:** every relative `.html` href across all nine pages resolves to an existing
  file. The only non-resolving strings are the absolute `https://blog.dugong.live/...` self
  canonicals and `og:url`, which are correct by design.
- **Date consistency:** on each edited post, `article:modified_time` equals the JSON-LD
  `dateModified` (2026-06-11) and the `sitemap.xml` `lastmod` agrees. No mismatches.
- **Structured data:** all nine JSON-LD blocks still parse as valid JSON after the edits.
- **HTML structure:** `<div>` open/close balanced on every file. All posts now converge to 44/44
  (the six-card posts gained one card, the two five-card posts gained two), index 134/134.
- **XML:** `sitemap.xml` and `feed.xml` both parse as well-formed XML.
- **Style preference:** zero em or en dashes in any inserted card text; house typography kept.

## Not done (deliberately)

- **No git commit / deploy.** Changes are staged in the working tree for review, consistent with
  every prior run. (The chargeback, order-change, and returns post files remain untracked, as
  they were before this run.)
- **No homepage card changes.** The index already features the chargeback post; no edit needed.
- **Decorative copy untouched.** The hero "13 NEW DISPATCHES THIS MONTH" banner and the visible
  WORDS tickers remain editorial calls flagged for a human, not SEO defects.
- **No fabricated author profiles.** Richer author `sameAs` entities would help E-E-A-T, but
  inventing profile URLs is worse than omitting them.
