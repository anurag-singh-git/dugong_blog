# SEO / GEO report - 2026-10-19

Scheduled autonomous run. Last SEO/GEO pass: 2026-10-18. A blog run fired during this pass and
published Dispatch Nº 132; see Part 7 for how the two runs overlapped.

## Part 0 - The three-day blocker is closed, and the live site proves it

Standing item 1 from 10-16, 10-17 and 10-18 is resolved. The tree is clean, `git status` shows the
working copy at `7ac7ea3` with nothing ahead of `origin/main`, and the live site serves the work:

| Checked on the live site | What it shows |
|---|---|
| `robots.txt` | the **10-17 file**: `Allow: /` ordering fixed, and rules present for `_qa_tmp/`, `_to_delete/`, `_tools/` and `__deltest.tmp` |
| `how-to-catch-shopify-shipping-labels-you-never-used.html` | renders, published and modified 2026-10-18. Dispatch Nº 131 is live |

So the 317 QIDs, the HowTo repairs, the `@id` and `hasPart` work and the entity corrections from
10-17 and 10-18 are all being served. Nothing in this report is blocked on a push.

What is pending now is this run's own work plus the blog run's: 26 changed or new paths outside
`_qa_tmp/`. The commit history here is hand-written and the owner has been committing daily, so this
pass leaves the commit alone and flags it in Part 8.

## Part 1 - The checker passed, and four of its blind spots were worth looking at

`_tools/seo-check.py` on the tree as found: **PASS.** Recomputed: 97 rendered pages, 82 stubs, 85
dispatches, 96 sitemap URLs, 85 feed items.

So this run went looking in the places a checker written on 10-17 and extended on 10-18 does not
look. Two of its checks were measured against reality rather than against format, and both came back
clean, which is worth stating because it is the first time either has been tested:

| Measured | Result |
|---|---|
| `wordCount` against the words actually inside `<article>` | 85 / 85 within tolerance, **median deviation 5.5%** |
| `timeRequired` against that word count at 225 wpm | 85 / 85 plausible, none off by more than 1.8x |
| FAQ question and answer text repeated across pages | **0 duplicates in 427 questions and 427 answers** |
| `speakable` `cssSelector` values present in the page they point at | 95 / 95 |
| `ItemList` `numberOfItems` against the list's own length | 0 mismatches |
| hub `dateModified` against the newest dispatch each hub lists | 8 / 8 agree |
| orphan pages | 0 |

The HowTo defect found on 10-18 was markup disagreeing with the page. These are the same question
asked of the numbers, and the numbers are honest. The defects below are elsewhere.

## Part 2 - Dispatch Nº 131 was missing from one of the three lists in llms.txt

llms.txt carries three parallel lists of every dispatch: **Full index** (title, URL, author, date),
**Articles** (the same with a paragraph of annotation) and **Markdown versions** (the `/md/` twin).
Yesterday's dispatch was in two of them.

```
Full index         84 entries   <- missing how-to-catch-shopify-shipping-labels-you-never-used
Articles           85 entries
Markdown versions  85 entries
```

This is the file answer engines are pointed at first, by robots.txt and by the site's own copy. A
model that reads the Full index to enumerate the corpus gets 84 of 85 dispatches and has no way to
know it is short. Fixed; all three lists now carry 86 after the blog run.

## Part 3 - The inventory guide said 16 and the inventory guide said 17

The topic-guide block in llms.txt states a dispatch count per guide. Seven of eight agreed with their
page. The inventory guide read **16 in llms.txt** against **17 in its `ItemList`, 17 in its visible
card grid and 17 in its own eyebrow heading**. The miss dates to the 10-15 blog run, which added a
dispatch to the guide and to every other count but not to this line.

The cost is small and specific: a reader of llms.txt who totals the eight guides gets 83 against 84.
Fixed, and an invariant now ties the three numbers together, which is what caught the recurrence risk
when the blog run added Nº 132 to the order-management guide mid-pass. That one it got right.

## Part 4 - Aanya Rao has an author page, five months after she wrote the lead essay

Carried item 12 from 10-14, closed. Her `author` node was the only one of 86 on the site with no
`url`, so the one piece of named human authorship outside Priya Singh resolved to nothing. For an
answer engine weighing who wrote a claim, a `Person` with a name and a job title and no identity to
resolve is barely better than no author at all.

`aanya-rao.html` is built from the `priya-singh.html` template, so the chrome, the stylesheet and the
card grid are the site's own rather than new. It carries a four-node `@graph`:

| Node | What it says |
|---|---|
| `ProfilePage` `#profile` | the page, `isPartOf` the blog, `mainEntity` the person |
| `Person` `#aanya-rao` | name, url, jobTitle, description, `worksFor` the organization, five `knowsAbout` values |
| `BreadcrumbList` `#breadcrumb` | Field Notes → Aanya Rao |
| `ItemList` `#dispatches` | her one dispatch |

The `Person` `@id` is `https://blog.dugong.live/#aanya-rao`, which is the id the lead essay and
index.html already used, so the three now refer to one node rather than three lookalikes.

Wired in eight places: the lead essay's author node (`url` added), index.html's author node (`@id`
and `url` added), the lead essay byline (now a `rel="author"` link), the index author card, the
Priya Singh page, `sitemap.xml`, the llms.txt Authors section (her line was the only one of two that
was not a link) and `md/the-death-of-the-drag-and-drop-builder.md`, whose header follows the
`Author: Name (url)` convention every Priya file already used.

The page was rendered at 1440 and 390 and checked for overflow at both: none, one `h1`, 23 links,
JSON-LD parses.

While there, the author archive URL was added to all 86 author lines in llms-full.txt, which carried
name and role and no way to resolve either.

## Part 5 - A second disambiguation page, caught the other way round

The 10-17 pass resolved all 115 Wikipedia targets and found one disambiguation page. This run
verified 18 entity pairs through the Wikipedia API with `prop=pageprops`, which returns a
`disambiguation` flag the earlier resolve-and-check-it-is-alive pass did not read. One came back
flagged:

```
"title": "Click and collect",
"pageprops": { "disambiguation": "", "wikibase_item": "Q101423394",
               "wikibase-shortdesc": "Topics referred to by the same term" }
```

So `en.wikipedia.org/wiki/Click_and_collect` resolves, returns 200, and is not an article. It was the
entity target on two dispatches, both about local pickup. Wikidata's own label for Q101423394 is
"Wikimedia disambiguation page", which means the site was asserting that the thing its dispatch is
about is a disambiguation page.

The right item exists. `wbsearchentities` returns **Q15794580, "click and collect", described as
"shopping in which merchandise is purchased online and picked up at a local store"**.
`wbgetentities` on it returns `"sitelinks": {}` - no Wikipedia article in any language. There is a
2022 video game of the same name (Q135022190) and a "bricks and clicks" item carrying the phrase as
an alias (Q290759); neither is the concept.

This is not the 10-18 "Transactional email" case, where neither a Wikipedia article nor a Wikidata
item existed and the entity was removed. Here the concept is properly identified, just not on
Wikipedia. So the entity stays and carries Wikidata alone.

That breaks the invariant that every entity carries both, and the right response is to tighten the
invariant rather than loosen it. The rule is now: **Wikidata always; Wikipedia unless the entity is
in the documented `wikidata_only_entity` set, in which case a Wikipedia URL is itself a failure.** A
page on that list cannot quietly drift back to pointing at a disambiguation page.

Entity references after this pass: **358, all 358 carrying a Wikidata QID, 355 also carrying a
Wikipedia article**, 113 distinct names.

## Part 6 - The eight topic guides described themselves with an ungrounded noun

Every dispatch carries three to five `about` entities, each with a Wikipedia URL and a Wikidata QID.
Every topic guide carried exactly one, and it was a bare `Thing`:

```
"about": { "@type": "Thing", "name": "Shopify inventory automation" }
```

No `sameAs`, nothing to resolve. The guides are the pages a crawler reaches first and the pages that
define what each cluster of dispatches is about, and they were the least grounded pages on the site.
"Shopify inventory automation" has no Wikipedia article and should not get a fabricated one, so the
topical `Thing` stays as the primary subject and grounded entities were added beside it.

The entities were not invented. Each guide's `about` now carries the grounded entities that already
appear in the dispatches that guide lists, by a rule the checker can reproduce: **every entity used
by at least two of the guide's dispatches, capped at five, ordered by frequency and then by
site-wide rarity.** Every pair reused is one of the 316 verified on 10-17 and 10-18, and the 18 used
here were re-verified through the API this run.

| Guide | Grounded entities added |
|---|---|
| Order management | Shopify, E-commerce, Order fulfillment, Business process automation, Invoice |
| Inventory | Shopify, E-commerce, Inventory management, Inventory, Stock keeping unit |
| Shipping and fulfillment | Shopify, Order fulfillment, E-commerce, Click and collect, Dimensional weight |
| Discounts and promotions | Shopify, E-commerce, Discounts and allowances, Pricing, Promotion (marketing) |
| Returns and refunds | Shopify, Product return, E-commerce, Reverse logistics |
| Customer and wholesale | Shopify, Customer lifetime value, Wholesale, E-commerce |
| Catalog and storefront | Shopify, Search engine optimization, E-commerce, Alt attribute |
| Fraud and risk | Shopify, E-commerce, Business process automation |

The fraud guide gets three because only three entities clear the bar. The rule was not bent to pad
it: the next candidates each appear once, and the most distinctive of them by site-wide rarity is
"Affiliate marketing", which is not what that guide is about. Three true entities beat four with a
wrong one, which is the standard the 10-17 and 10-18 passes set.

## Part 7 - Fifteen editorial links that no reader could see

Found while verifying the new author page renders. The `.article-dek` paragraphs carry the
hand-written editorial links on the guides and the author pages, and the stylesheet has no `a` rule
for that container. Computed style, measured in a browser:

```
before:  color rgb(86,86,78)   = var(--text-dim), the dek's own colour
         text-decoration none
         border-bottom 0px
```

Identical to the surrounding prose in colour, weight and decoration. Not a low-contrast link, not a
subtle one: no affordance at all. `.article-body a` has had the right rule all along
(`var(--lime-deep)` plus a 1px underline), so this is one container that was never given it.

Fifteen links on eleven pages, and they are not decorative ones. They are each guide's link out to
its siblings, the author pages' links to the field study and the question index, and the index
author card's archive link. They pass to a crawler and are invisible to a person, so they have been
earning no clicks since they were written.

Fixed by adding `.article-dek a` and `:hover` rules matching `.article-body a`, to the ten pages that
have a dek link. Verified in a browser after: `rgb(79,112,0)` and a 1px bottom border on every one,
at 1440 and 390, no overflow at either width.

A new invariant generalises it: **any container class that holds links must have an anchor rule in
that page's stylesheet.** It needed a small tag-matching helper, `element_contents()`, because a
regex stops at the first closing tag and so undercounts links inside `.article-body`.

## Part 8 - Six new invariants, tested against this morning's tree

`_tools/seo-check.py` and `_tools/README.md` updated.

| New check | Fires when |
|---|---|
| `author_without_url` / `author_without_id` | an author node resolves to nothing |
| `collection_about_ungrounded` | a `CollectionPage` has no `about` entity carrying `sameAs` |
| `entity_wikipedia_unexpected` | an entity documented as Wikidata-only carries a Wikipedia URL |
| `llms_list_incomplete` | a dispatch is missing from any of llms.txt's three lists |
| `llms_guide_count` | a topic-guide count in llms.txt disagrees with the guide's ItemList or card grid |
| `unstyled_link_container` | a container holding links has no anchor rule in that page's stylesheet |

**Run against this morning's pre-change snapshot the extended checker reports exactly the defects
this pass found, and nothing else:**

```
author_without_url (1)
collection_about_ungrounded (8)
entity_wikipedia_unexpected (2)
llms_guide_count (1)
llms_list_incomplete (1)
unstyled_link_container (9)
```

No check was loosened. The `wikidata_only_entity` entry added to `EXCEPTIONS` is a tightening: an
entity on that list must carry Wikidata and must not carry Wikipedia.

## Part 9 - The blog run fired in the middle of this pass

At 17:03 UTC, while this pass was writing, the blog run published Dispatch Nº 132,
`how-to-stop-shipping-shopify-orders-with-payment-pending.html`. Both routines write the same tree.

This pass stopped writing and waited for it rather than racing it, then re-verified. Nothing was
lost in either direction: the blog run appended to llms.txt incrementally rather than regenerating
it, so the Part 2 and Part 3 repairs survived, and it picked up the llms-full.txt author-URL format
for its own entry without being told to. All eight hub `about` blocks, the author page and its eight
wirings were intact afterwards.

It is worth knowing this can happen, because the failure mode is silent. A blog run that regenerated
llms.txt instead of appending would have reverted Parts 2 and 3 with no error anywhere. **Worth
staggering the two schedules**, or having the blog run call the checker at the end, which is carried
item 2 from 10-18 and would at least make the collision loud.

## Part 10 - Audit after the changes

| Check | Result |
|---|---|
| `_tools/seo-check.py` on this tree | **PASS** |
| extended checker on the pre-change snapshot | fires on exactly the 22 defects above |
| author nodes carrying a `url` | **86 / 86** (was 85 / 86) |
| graph nodes carrying an `@id` | 381 / 381 |
| entity refs carrying a Wikidata QID | **358 / 358** |
| entity refs carrying a live Wikipedia article | **355 / 355 of those that should** |
| `CollectionPage` nodes with a grounded `about` | **9 / 9** (was 1 / 9) |
| dispatches present in all three llms.txt lists | **86 / 86** (was 85 / 86) |
| llms.txt guide counts vs ItemList vs card grid | **8 / 8** |
| links in `.article-dek` carrying a visible link style | **15 / 15** (was 0 / 15) |
| `wordCount` vs words inside `<article>` | 86 / 86, median deviation 5.5% |
| FAQ `acceptedAnswer` verbatim in the visible page | 433 / 433 |
| HowTo step text and name verbatim in the visible page | 572 / 572 |
| JSON-LD parses, all rendered pages | 99 / 99 |
| broken links / in-page anchors / cross-file anchors | 0 / 0 / 0 |
| orphan pages | 0 |

Render: the new author page and the Priya page were loaded in a browser at 1440 and 390, screenshot
and measured. No horizontal overflow, one `h1` each, dek links styled. The 10-14 render pass across
eight widths still holds for everything else; the only body changes this pass made were one anchor
around an existing byline name and two sentences inside existing paragraphs.

Dates: `dateModified` was not moved on the eight guides or the two pickup dispatches. Those changes
are to how the page describes itself, not to what it says, and the 10-18 policy on this is unchanged.
index.html, priya-singh.html and the two pages the blog run touched already read 2026-10-19.

Snapshots: `_qa_tmp/seo-2026-10-19-before.tar.gz` and `_qa_tmp/seo-2026-10-19-after.tar.gz`.

## Part 11 - Needs a decision

1. **Commit and push.** 26 paths outside `_qa_tmp/`: this pass, plus Dispatch Nº 132 and the blog
   run's wiring. Not the three-day emergency it was yesterday, but today's work is not live until it
   happens, and `aanya-rao.html`, `.gitignore` and the new dispatch are untracked rather than
   modified.
2. **`_qa_tmp/` is now gitignored, and 50 tarballs are already tracked.** `.gitignore` was added this
   run and stops the bleeding, but it does not untrack what is committed. **99 MB** of whole-site
   tarballs sit in the repo and are publicly downloadable from the live domain, because robots.txt is
   a request and not an access control. The fix is `git rm -r --cached _qa_tmp` in one commit; the
   history still carries them after that, which is a separate and larger decision. Carried from
   10-17 and 10-18 and now measured.
3. **Stagger the blog run and the SEO pass, or make the collision loud.** Part 9. The two routines
   wrote the same tree within the same minute today and got away with it. Adding
   `python3 _tools/seo-check.py` to the end of the blog run is the cheap half of this and is carried
   item 2 from 10-18.
4. **The blog run still paraphrases the playbook into the HowTo markup.** Carried from 10-18. The
   checker now fails the day it happens, and Nº 132 came through clean, so either the generator was
   fixed or it got lucky; worth confirming which.
5. **Google Fonts is still a render-blocking third-party stylesheet on all 99 pages.** The only
   external resource the site loads and the only Core Web Vitals lever left. Unchanged reason for not
   doing it autonomously: it alters paint behaviour on every page. This run did get a browser to
   render local pages, which is new, so a before-and-after measurement is now possible on the working
   tree rather than only on the live site. Still worth a supervised run.
6. **og:image is still the same banner on all 99 pages.** Unchanged since 10-12. A design call plus a
   batch render job.
7. **Organization `sameAs` still resolves nothing.** It lists `https://dugong.live`, which is already
   the node's `url`. **Needs someone to supply real profile URLs** (LinkedIn, X, GitHub, Crunchbase).
   Still the largest remaining GEO gap and the only one on this list no autonomous run can close.
8. **The lead essay now has 4 editorial inbound links**, up from 2 on 10-18, because the author page
   and the two author-card sentences point at it. Still against 33 to 80 for a mature dispatch, and
   still the only non-Shopify piece. Carried.
9. **New dispatches start with near-zero editorial inbound links** for about three days. Nº 132 is
   there now. Carried from 10-17 and 10-18.
10. **index.html says "131 dispatches published" and "ISSUE Nº 132"** against 86 pages that exist.
    The archive block lists issues 041, 037 and 036, which have no pages. This reads as a deliberate
    editorial conceit rather than a defect, so nothing was changed, but an answer engine asked how
    many dispatches the blog has will repeat the number on the page. **Owner's call** whether the
    framing is worth the claim.
11. **`__deltest.tmp` and `_to_delete/` are still committed.** Now gitignored, same untracking
    caveat as item 2. Deleting them on this machine needs a permission prompt and nobody is at the
    desk. Carried from 10-16.
12. **`shopify.dev/docs/api/admin-graphql/2026-10/...` redirects to `/latest/`.** One link, one page.
    Pin or follow, someone's call. Carried from 10-18.
13. **index.html and 404.html keep hand-written og:title and og:description.** Deliberate, inside the
    caps, recorded as a checker exception. Carried.
