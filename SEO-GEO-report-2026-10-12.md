# SEO / GEO report - 2026-10-12

Scheduled autonomous run. Last SEO/GEO pass: 2026-09-21. Three weeks of dispatches have landed
since (Nº 122 to Nº 125), and the Sep 21 standing item, nothing pushed since Sep 19, has been
cleared: `HEAD` is `055ca89`, in sync with `origin/main`, working tree was clean at the start of
this run, and `blog.dugong.live/sitemap.xml` served the same 78 locs with a 2026-10-11 `lastmod`
that the local file carried. The deploy pipeline is healthy.

Field-level SEO on this site is already finished work. All 77 wired posts carried a complete
BlogPosting (every one of eighteen fields checked, including `about`, `citation`, `speakable`,
`wordCount` and `timeRequired`), FAQPage with visible parity, HowTo, canonical, OG and Twitter
tags inside the length caps, 7.4 body-copy internal links on average and no orphans. There was
nothing left to patch at that level. What was missing was a layer above it, and that is what this
run built.

## Part 1 - Eight topic guides, the missing layer

Seventy-eight dispatches reached search and answer engines as a flat list behind one homepage.
There was no page on the site that could rank for or be cited on a head term: no URL said
"Shopify inventory automation", only 16 URLs that each said one failure mode inside it. The nav
already promised "Topics" and pointed at a keyword cloud whose links went straight back to
individual posts.

Eight guide pages now exist, each a real URL with its own title, description and schema:

| Guide | Dispatches |
|---|---|
| `shopify-order-management-automation.html` | 16 |
| `shopify-inventory-automation.html` | 16 |
| `shopify-shipping-and-fulfillment-automation.html` | 14 |
| `shopify-fraud-and-risk-automation.html` | 8 |
| `shopify-discounts-and-promotions-automation.html` | 7 |
| `shopify-customer-and-wholesale-automation.html` | 6 |
| `shopify-catalog-and-storefront-operations.html` | 6 |
| `shopify-returns-and-refunds-automation.html` | 5 |

Every one of the 78 wired posts is assigned to exactly one guide, so each post has a single
breadcrumb parent and no guide duplicates another's content. No new marketing copy was written
for the cards: each card carries that post's own og:title as its anchor text and its own meta
description as the dek, both already published on the page it links to. Each guide carries a
CollectionPage, a two-level BreadcrumbList and an ItemList naming every dispatch in order, plus
an `isPartOf` pointing at the Blog node. Titles run 40 to 49 characters, descriptions 149 to 165,
all unique against the existing 80.

The guides are wired in four directions:

1. **Homepage** gained a TOPIC GUIDES section above the existing topic cloud, and its Blog node
   gained `hasPart` naming all eight CollectionPages.
2. **Every post** gained one line at the end of READ NEXT, "more on <guide> →", which is both the
   reader's path up and the guide's inbound link. Each guide now has 13 to 24 inbound links across the tree.
3. **Every post's BreadcrumbList** became three levels, Field Notes → guide → post, so the
   breadcrumb Google renders under the result now names the topic.
4. **sitemap.xml** (87 locs, no dupes, no ghosts) and **llms.txt**, which gained a "## Topic
   guides" section above the full index so an answer engine reading the file sees the taxonomy
   before the 78-item list.

The guides reuse the homepage stylesheet verbatim, so they are native to the site; the only new
CSS is a four-line block marked `SEO 2026-10-12` that puts the cards in two columns and keeps the
link legible. Guides were deliberately left out of feed.xml: they are not dispatches.

## Part 2 - Two defects in today's dispatch, both fixed

Dispatch Nº 125 (committed inventory) was written by the daily blog run at 18:24 UTC, three
minutes into this pass. Two things came out of that run broken.

1. **Its abstract was truncated to a single character in both files answer engines read.**
   `llms.txt` carried `: T By Priya Singh, 2026-10-12.` and `feed.xml` carried
   `<description>T</description>`. Every other entry in both files carries a 1,000 to 3,000
   character summary. `llms-full.txt` was fine, 3,508 words. Both repaired with 1,413 characters
   assembled from copy already published on the page itself: the article dek followed by the
   page's own "The short answer" paragraph. No new claims were written. feed.xml still parses.

2. **It overflowed the viewport horizontally at 320 px.** An inline `<code>` holding
   `fulfillment_status:unfulfilled AND status:open AND sku:...` measured 312 px starting at a
   20 px gutter, pushing the document to 332 px against a 320 px viewport. Mobile usability is a
   ranking input and this is the kind of defect that only shows on the narrowest phones. Fixed
   across all 87 pages that carry the article stylesheet with one rule, marked `SEO 2026-10-12`,
   letting long inline code break rather than widen the page. Inline code only; `pre` is untouched.

## Part 3 - The two orphan drafts, resolved

Standing item 2 of the 2026-10-11 QA report: two noindex drafts, both dated 1 Aug, both claiming
Dispatch Nº 97 (which belongs to the dead-stock post), both with live URLs, nothing linking to
them, and both carrying old `| Dugong Field Notes` titles at 85 and 93 characters. They were the
only two titles in the tree past 60 characters and the only duplicate dispatch numbers.

Both are now redirect stubs pointing at
`how-to-automatically-follow-up-on-unpaid-draft-orders-on-shopify.html`, the live post covering
the same ground, using the identical template as the other 77 stubs. This consolidates them
instead of leaving two dead ends, and it is reversible: the originals are in git history and
copied to `_qa_tmp/orphan-drafts-2026-10-12/`. Deleting the files outright still needs a
supervised run; as stubs they are no longer a liability either way.

## Part 4 - Schema graph hygiene

Every post's `isPartOf` was a bare `{"@id": ".../#blog"}` referring to a Blog node defined only on
the homepage. Consumers resolve `@id` references within a single page's graph, so on 77 post pages
that reference resolved to a URI with no type and no name. It is now a typed node carrying
`@type`, `name` and `url`, so each post states which publication it belongs to without depending
on another page. Author and publisher were already defined inline and were not touched.

## Part 5 - Audit after the changes

Recomputed from the files: 168 HTML files, 80 redirect stubs, 88 rendered (78 wired posts, 8
guides, index, 404).

| Check | Result |
|---|---|
| JSON-LD parses, all rendered pages | PASS |
| BreadcrumbList is 3 levels, guide correct, positions 1-2-3 | 78 / 78 |
| `isPartOf` a typed Blog node | 78 / 78 |
| one `.hub-more` link and one marked CSS block per post | 78 / 78 |
| title <= 60, unique; meta description 70-165, unique | PASS, 0 dupes |
| og:description <= 165; description == og == twitter | PASS |
| canonical == filename == og:url; one h1 per page | PASS |
| broken internal links / dead stub targets | 0 / 0 |
| sitemap 87 locs, 0 dupes, 0 ghosts | PASS |
| every post in feed, llms.txt, llms-full.txt, index | PASS |
| every guide in llms.txt and on the homepage | 8 / 8 |
| headless render, 88 pages x 8 widths (320 to 1920), 704 renders | 0 horizontal overflow, 0 page errors, 0 text under 12 px at phone widths |
| guide tap target at 375 px | >= 24 px on all 8 |

The before-state of the whole tree is in `_qa_tmp/seo-2026-10-12-before.tar.gz`.

## Part 6 - Not changed, needs a decision

1. **The May 28 lead essay still has no URL.** Carried in every report since at least 09-21. "The
   death of the drag-and-drop builder", 820 words, Dispatch Nº 47, lives only inside index.html;
   its JSON-LD `url` is `https://blog.dugong.live/#view-post` and llms.txt points at the homepage.
   It cannot rank for its own query, cannot be cited on its own, and competes with the homepage's
   own subject. Giving it a page means moving content off the homepage, which is a judgement call
   about the homepage, so it is left for a supervised run. It is the single largest remaining win.
2. **25 of the 80 article pages load no webfont at all.** They declare the same `var(--body)` stack
   as the rest but carry no Google Fonts link and no preconnect, so they render in system fonts
   while the other 55 render in Hanken Grotesk and Inter. Not a ranking issue; it is a visible
   inconsistency, and the fix could go either way (add the link to 25, or drop it from 55 and gain
   the render-blocking request back). A design call, not a scripted one.
3. **og:image is the same banner on all 88 pages.** Per-post share images would lift click-through
   from social and from the AI answer surfaces that show a thumbnail. Generating 78 of them is a
   batch job worth doing deliberately.
4. **The guides carry no ticker bar.** Posts and the homepage have the scrolling strip above the
   nav; the guides start at the nav. Left off on purpose: the ticker text is maintained by the
   blog run and a copy on eight static pages would go stale. Worth folding into the blog run's
   template pass if the strip should be everywhere.
5. **Nothing is pushed.** This run's changes are local only. Nothing reaches a crawler until:
   `git add -A && git commit -m "Topic guides + SEO/GEO 2026-10-12" && git push`
   This session cannot delete files in the folder, which makes git lock-file handling unsafe
   unattended, so the push is left for a supervised run, as in previous passes.
