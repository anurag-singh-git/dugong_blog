# SEO / GEO report, 2026-08-03 (58 files edited, 2 created)

**Scope:** Scheduled full-site SEO/GEO pass, the first since 08-01. This was the busiest window
the site has ever had: the 08-03 daily publish run (Dispatch Nº 99, "The payment that expires
before you capture it") and the 08-03 QA sweep (87 edits across 30 files, including noindexing
the four orphan drafts) both executed in the same hour as this pass. All three runs finished
without clobbering each other; details in the concurrency note at the end. The site now carries
**111 HTML files**: 57 rendered (54 wired posts + index.html + 2 noindexed rejected drafts) and
54 redirect stubs.

## Headline: the orphan backlog is cleared; the site publishes Nº 100 and Nº 101

Since 08-02 the standing flag has been the four fully rendered but unwired orphan posts from the
interrupted 08-01 evening run: one two-store inventory-sync post and three near-duplicate takes
on unpaid draft orders, all stamped "Dispatch Nº 97" internally, all invisible to crawlers, all
carrying zero search value. The 08-02 recommendation was explicit: publish one of each topic
properly on a future run, and delete or noindex the rest. This pass executed that recommendation.

**Published, Dispatch Nº 100:** `how-to-sync-inventory-between-two-shopify-stores.html`
(2,310 words). Unique topic, complete template, mobile-ready, and its pain-point stub
(`the-last-unit-both-your-stores-just-sold.html`) had been sitting live but pointing at an
unwired page since 08-01, the one structural defect the morning audit found.

**Published, Dispatch Nº 101:** `how-to-automatically-follow-up-on-unpaid-draft-orders-on-shopify.html`
(2,410 words), chosen from the three draft-order variants. Selection rationale:

- The 46 KB `how-to-send-payment-reminders...` variant was disqualified on the QA sweep's
  finding from earlier today: zero media queries, not mobile-ready, confirmed earlier partial.
  Under mobile-first indexing that page should not be the survivor, whatever its prose merits.
- Between the two complete variants, the chosen post targets the broader head phrase ("unpaid
  draft orders" rather than "draft order invoices"), is the longer piece (2,410 vs 2,195 words),
  and its FAQ set covers the exact questions answer engines get asked, including "Can Shopify
  Flow follow up on unpaid draft orders?", the only variant with a Flow-scoped question.

**Rejected and left noindexed:** `...follow-up-on-unpaid-draft-order-invoices...` (narrower
duplicate) and `...send-payment-reminders...` (the partial). The QA sweep had already applied
reversible `noindex, follow` tags to all four orphans this morning; this pass removed the tags
from the two survivors as part of publishing (per the tag's own instruction comment) and left
the two rejects noindexed. Deleting them remains an owner call, per standing convention.

## What publishing properly involved

Both posts were re-identified before wiring: internal dispatch stamps renumbered from the stale
"Nº 97 / AUG 1" to Nº 100 and Nº 101 with AUG 3 dates across ticker (2 spans each), byline,
`article:published_time` / `article:modified_time`, and JSON-LD `datePublished` /
`dateModified`. The publish date was set to 2026-08-03, the day the posts actually became
visible, not the 08-01 authoring date; a page should not claim two days of existence it never
had. Ticker word counts (2,310 / 2,410) already matched their JSON `wordCount`, so no repeat of
the Nº 98 stale-ticker defect (which the daily run had itself repaired this morning).

Wiring, matching the Nº 98/99 launch pattern exactly:

| Surface | Change |
|---|---|
| sitemap.xml | 2 new URLs (0.9/monthly, lastmod 2026-08-03), inserted newest-first; 55 locs total |
| feed.xml | 2 new items at top (Nº 101 at 14:00, Nº 100 at 13:00 UTC); lastBuildDate advanced to 14:00; 55 items |
| llms.txt | 2 full-paragraph entries inserted after the lead essay, newest-first |
| index.html hero | ISSUE Nº 101 · AUG 3 · 2026, stat counter 99 → 101 |
| index.html ticker | 3 → 5 NEW DISPATCHES THIS MONTH (×2) |
| index.html hub graph | 2 new fully populated BlogPosting entries with `#priya-singh` author `@id`; 55 entries |
| index.html grid | new card-tall for Nº 101 (envelope glyph, INVOICE SENT ONCE · REMINDED NEVER), plain card for Nº 100; Nº 99's card-tall demoted to plain card, art removed; exactly one card-tall preserved |
| topic cloud | six new links: draft order follow-ups, unpaid invoices, quote reminders, two-store inventory sync, multi-store stock, oversell between stores |
| sibling mesh | both cards inserted at the top of the related grid in all 52 wired posts; winners cross-linked and given Nº 97, 98, 99 cards in their own grids |
| new stub | `the-quote-that-goes-quiet.html` (noindex redirect, named for the post's HowTo entity) |

Each launches with **54 inbound links from rendered pages** (52 wired posts + the other winner +
index), verified by grep, zero wired posts missing either card. Card deks, feed descriptions,
and llms.txt entries were written fresh in house style from each post's actual content (the
Savannah pendant quote, the net-30 reminder machinery one screen away, the 9:41 double-sold
hoodie, Shopify Collective's actual purpose), with the long dek reused verbatim across index
card, feed item, and llms entry per site convention. Zero em or en dashes in everything authored
this pass; new HTML chrome uses entities only.

Convention notes: mesh-only edits did not bump sibling `lastmod` or `dateModified` (08-02
precedent, reaffirmed by today's QA housekeeping ruling). The winners' `dateModified` equals
`datePublished`, launch state.

## Full audit matrix (post-publish, all passing)

| Check | Result |
|---|---|
| JSON-LD parse, all 57 rendered pages | 0 errors |
| broken internal hrefs / absolute self-domain a-hrefs | 0 |
| canonical present, = filename, = og:url | 57 / 57 |
| stub redirects (noindex + canonical + live target) | 54 / 54, all targets wired |
| exactly one h1; og: + twitter: sets; lang; img alt | 57 / 57 |
| duplicate titles / duplicate meta descriptions | 0 / 0 |
| meta descriptions present, 160 chars or under | 57 / 57 |
| tag balance, all 111 files | balanced |
| sitemap.xml: 55 locs, 0 dupes, 0 ghosts, valid XML | PASS |
| feed.xml: 55 items, 0 dupe guids, lastBuildDate = newest pubDate | PASS |
| llms.txt coverage of wired posts | 54 / 54 |
| orphaned wired posts | 0 |
| `@graph` (BlogPosting + BreadcrumbList + FAQPage + HowTo) on new posts | complete |
| FAQ JSON-LD byte-matches visible text (incl. both new posts) | PASS |
| author `@id` → `#priya-singh` on both new posts | PASS |
| ticker Nº / byline Nº / dates / word counts on both new posts | self-consistent |
| hub graph order: pinned, 101, 100, 99, 98 ... | PASS |
| robots.txt (33 AI-crawler allowances + sitemap ref) | unchanged |

The only rendered pages outside the wired set are the two noindexed rejects, which is the
intended end state.

## Concurrency note

Three scheduled tasks wrote to this folder inside one hour today: the daily publish
(13:41), the QA sweep (13:44), and this pass. This pass avoided damage twice by design: every
edit ran as an exact-string replacement with an occurrence-count assertion, computed in memory
and written only after all assertions passed. The first attempt aborted cleanly when the sitemap
gained Nº 99 mid-flight; the second aborted when QA's noindex tags appeared on the orphans; the
third executed against the settled state, and incorporated both runs' work (Nº 99 demotion, QA's
noindex-removal instruction, and the QA finding that disqualified the partial variant). The QA
report's suggestion stands and is seconded here: stagger the three schedules by an hour or more.

## Recommendations for the owner

1. **Delete the two rejected drafts** (`...draft-order-invoices...` and the 46 KB
   `...send-payment-reminders...`). They are noindexed and harmless, but they are also dead
   weight in the deploy directory, and deletion stays an owner action by convention.
2. **FAQ depth** (five or six questions per post instead of three) remains the largest untapped
   GEO surface, carried since 07-28. With Nº 100 and Nº 101 the citable FAQ pool is now 162
   questions across 54 posts; the pillar essay still has none.
3. **Author page for Priya Singh**: the entity graph unifies on `#priya-singh` everywhere
   including both new posts, but the URL still resolves to the homepage. The human-readable half
   of that recommendation is still open.
4. **Commit and deploy.** The working tree holds today's three runs (publish Nº 99, the QA
   sweep, and this pass's Nº 100 + Nº 101), all uncommitted per scheduled-run convention.
   Nothing on blog.dugong.live reflects any of it until pushed. Note the QA report's warning
   about a stale `.git/index.lock` that may need removing before the next commit.

## Conclusion

The pass turned the site's last structural liability into its two newest dispatches. The orphan
backlog that has been flagged since 08-01 is resolved end to end: two strong posts went from
invisible to fully meshed with 54 inbound links each, the two duplicates are noindexed rejects
awaiting deletion, the last stub-to-nowhere now points at a wired page, and the full audit
matrix reads clean across every rendered page and distribution surface.

**58 files edited: 52 wired posts (double mesh insert), the 2 published posts (renumbering,
dating, robots, grid backfill), index.html, sitemap.xml, feed.xml, llms.txt. 2 files created:
`the-quote-that-goes-quiet.html` and this report.**
