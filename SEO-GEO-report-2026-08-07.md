# SEO / GEO report, 2026-08-07 (10 files edited, 1 created)

**Scope:** Scheduled full-site SEO/GEO pass, the first since 08-03. Three scheduled tasks wrote
to this folder inside one window again today: the QA sweep (13:24, nav-fix propagation to all
54 posts), this pass (FAQ deepening and the author entity fix), and the daily publish (13:33,
Dispatch Nº 102). All three merged cleanly; verification details in the concurrency note. The
site now carries **113 HTML files**: 58 rendered (55 wired posts + index.html + 2 noindexed
rejected drafts) and 55 redirect stubs.

## Baseline audit: clean

The pass opened with the full audit matrix re-derived from scratch against the settled
`f848267` tree. Result: zero defects across all surfaces. The owner's "changes for mobile view"
commit was inspected and is CSS-only (nav overflow and signup-row fixes on index.html), touching
no metadata surface. The one item the sweep flagged, a feed guid reading
`https://blog.dugong.live/#dispatch-47`, is the pinned essay's deliberate non-permalink guid
(`isPermaLink="false"`), valid RSS and not a ghost; today's QA sweep independently recorded the
same conclusion. With nothing to repair, the pass went to the two oldest carried
recommendations instead of recertifying an already-clean tree.

## Improvement 1: FAQ deepening begins, 3 to 5 questions on the eight head posts

FAQ depth has been flagged as the largest untapped GEO surface on every report since 07-28 and
executed by none of them. This pass started the program on the eight highest-value head-term
pages: the pillar (best-shopify-automations) plus overselling, card testing, abandoned cart,
payment capture, high-risk orders, deleted-product 404s, and chargeback disputes. Each gained
two questions, taking them from three to five.

The sixteen new Q&As were authored fresh in house style, grounded strictly in each post's own
researched body content so no unsourced claim enters the citable pool. Questions target the
phrasings answer engines actually receive, including two more Flow-scoped questions (can Flow
capture payments, can Flow create redirects on product deletion), the question class the 08-03
selection rationale singled out as GEO-effective. Answers run 130 to 190 words, quantified where
the post is quantified (the 14% / 0.8% automation gap, the 7-day authorization window and 1.75%
late-capture charge, the $443B false-decline versus $48B fraud asymmetry, the 3% to 8% single-
reminder recovery rate), with zero em or en dashes and straight apostrophes throughout.

Mechanics, asserted before write on every file: visible `.faq-item` blocks inserted at the end
of each `faq-list` in exact house markup; matching Question nodes appended to each FAQPage
`mainEntity` in the compact single-line JSON style; JSON text byte-identical to visible text;
JSON-LD re-parsed; tag balance re-verified; visible and JSON counts both equal 5. The FAQ
section sits outside `<article>`, and today's QA sweep confirmed `wordCount` counts body copy
only, so tickers and `wordCount` are untouched and stay self-consistent.

**Dating convention note:** unlike mesh housekeeping, this is a substantive content change, so
the eight posts' `dateModified` and `article:modified_time` were advanced to 2026-08-07 and
their sitemap `lastmod` bumped to match (index.html likewise, for improvement 2). `datePublished`,
feed pubDates, and llms.txt bylines are untouched. The citable pool now stands at **181
questions across 55 posts** (8 posts at five, 47 at three, including today's Nº 102).

## Improvement 2: the #priya-singh entity anchor now resolves to a real author section

Every Person node on the site unifies on `@id: https://blog.dugong.live/#priya-singh`, but the
fragment resolved to nothing on the homepage; the human-readable half of the author-page
recommendation has been open since 08-02. index.html now carries an ABOUT THE AUTHOR section
with `id="priya-singh"` (avatar mark, name, role, and a bio consistent with the JSON-LD Person
description, linking the pillar study and the RSS feed), placed between the archive and the CTA
band in the home view, styled with new `.author-*` rules appended to the stylesheet using
existing design tokens only. The full Person node on index gained a matching `url` property.
E-E-A-T surfaces that previously dead-ended now land somewhere real: the entity graph, the
visible byline, and the anchor all agree on who Priya Singh is.

## Concurrency note: three writers, one window, zero losses

Mid-pass, the tree changed under this run twice. The QA sweep finished at 13:24 having edited
all 54 wired posts (nav CSS propagation); because this pass reads each file immediately before
computing its exact-string edits, the FAQ insertions landed on top of QA's fix, and all eight
edited posts verify as carrying both. The daily publish then created Nº 102 at 13:29 and wired
it through 13:33; this pass paused, polled until writes settled, then re-verified everything.
Post-settle checks confirm the merge was lossless in all three directions: the eight deepened
posts retain five FAQs plus QA's nav fix plus the publish run's Nº 102 mesh card in the correct
newest-first position; index.html retains the author section and Person url beneath the publish
run's hero and hub-graph advance to Nº 102; sitemap.xml holds this pass's ten lastmod bumps
plus the publish run's new 56th loc. The standing recommendation to stagger the three schedules
is hereby carried for a third report running.

## Full audit matrix (post-settle, all passing)

| Check | Result |
|---|---|
| JSON-LD parse, all 58 rendered pages (incl. index @graph) | 0 errors |
| FAQ JSON-LD byte-matches visible text, all 55 posts incl. 8 deepened | PASS |
| FAQ counts: visible == JSON on every post | 55 / 55 |
| canonical = filename = og:url; og/twitter sets complete | 58 / 58 |
| exactly one h1; lang; viewport; img alt | 58 / 58 |
| duplicate titles / meta descriptions; descriptions <= 160 chars | 0 / 0 / PASS |
| broken internal links / absolute self-domain hrefs | 0 |
| sitemap.xml: 56 locs = 55 wired + index, 0 dupes, 0 ghosts, valid XML | PASS |
| feed.xml: 56 items, unique guids, lastBuildDate = newest (Aug 7 12:00 UTC) | PASS |
| llms.txt: 55 article entries, all wired, uniform bylines | PASS |
| stubs: 55, bijective onto wired posts, noindex + live targets | PASS |
| sibling mesh presence and order incl. Nº 102 edges | 0 missing, 0 violations |
| index hub graph: 56 BlogPosting entries, pinned then newest-first | PASS |
| future dates / em dashes in body copy / bare ampersands | 0 |
| tag balance, all 113 files | balanced |
| rejects (2): noindexed, unwired, absent from all surfaces | PASS |

## Recommendations for the owner

1. **Continue the FAQ tranches.** Eight posts per pass at two added questions each reaches all
   55 posts in six more passes. Next tranche by the same head-term logic: WISMO, returns,
   address validation, back-in-stock, pre-orders, duplicate orders, discount abuse, reorder
   points.
2. **Stagger the three schedules** by an hour or more. Today was the second three-writer window
   in five days; the merge held because every writer used exact-string edits with assertions,
   but the pattern spends its luck each time.
3. **Delete the two rejected drafts**, unchanged standing recommendation since 08-02.
4. **Commit and deploy.** The working tree holds today's three runs: QA's nav propagation
   (54 posts), this pass (8 posts + index + sitemap), and the publish run (Nº 102 + wiring),
   58 modified files and 4 new ones, all uncommitted per scheduled-run convention. Nothing on
   blog.dugong.live reflects any of it until pushed.

## Conclusion

The two oldest carried recommendations finally moved. The FAQ program is no longer untapped:
the eight pages most likely to be cited by answer engines now field five questions each, with
sixteen new grounded, quantified, byte-verified Q&As in the pool. The author entity that every
page has pointed at for weeks now resolves to a real section. And a three-writer window that
could have shredded the afternoon instead merged losslessly, verified in all three directions.

**10 files edited: the 8 deepened posts, index.html, sitemap.xml. 1 file created: this
report.**
