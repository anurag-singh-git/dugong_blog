# SEO / GEO report - 2026-11-18

Scheduled autonomous run, fired 10:36 UTC. `SEO-GEO-report-2026-11-17.md` and `_tools/README.md`
were read in full first, and the first thing this pass did was the thing the 11-16 pass said every
pass should do from now on: `grep` every check name the README claims straight out of
`seo-check.py`. **All of them were there.** That habit has now paid for itself twice.

`seo-check.py` passed on the tree as found. So this pass went looking for something no check reads,
and found it in the two nodes on every dispatch that exist to be lifted: the `FAQPage` and the
`HowTo`. The article has claimed both through `hasPart` since 10-18. **Neither claimed anything
back, and neither carried a URL, an author, a publisher, a date, a topic or, in one case, a
language.** That is Part 1 and it is the spine of the pass.

The publishing run finished before this pass began for the second day running, so there was no
collision and no rollback. The bridge held throughout. Part 5.

## Part 0 - The tree as found

`HEAD` = `1059055`, dated 2026-10-30, still the last commit, now nineteen days old. On arrival: 230
uncommitted paths, `seo-check.py` **PASS**, 110 rendered pages, 82 redirect stubs, 97 dispatches,
109 sitemap URLs, 97 feed items. Dispatch Nº 143, "How to catch the Shopify payments that never
became an order", had shipped at 10:20 to 10:25 UTC, eleven minutes earlier, and carried every
structure the 11-16 and 11-17 passes added with no hand edit.

## Part 1 - The two liftable nodes had no address and no provenance

A dispatch's `@graph` holds six nodes. Five of them are thoroughly furnished. Here is what the
other two held, across the whole archive:

| node | n | properties |
|---|---|---|
| `FAQPage` | 96 | `@type`, `@id`, `mainEntity`. **Nothing else** |
| `HowTo` | 95 | `name`, `description`, `totalTime`, `step`, and `inLanguage` on 94 of the 95 |

These are not incidental nodes. `FAQPage` and `HowTo` are the two types a search engine and an
answer engine lift **on their own**, away from the page, and this site has 499 `Question` nodes and
657 `HowToStep` nodes sitting under them. Since 11-04 every one of those 499 questions has carried
its own `@id` and its own `url`. Since 11-16 every dispatch has had a `WebPage` node naming its
canonical URL, its dates and its breadcrumb. Since 11-17 every concept the site writes about has
been a named Wikidata entity.

The parent holding the 499 addressable answers named **no page, no writer, no publisher, no day and
no subject**. A machine that lifted an answer could resolve the answer's own anchor and learn
nothing else about where the answer came from.

Both nodes now carry the following, and every single value is one that was already on the page:

```json
{
  "@type": "FAQPage",
  "@id": "https://blog.dugong.live/....html#faq",
  "url": "https://blog.dugong.live/....html#faq-heading",
  "inLanguage": "en",
  "isPartOf": { "@id": "https://blog.dugong.live/....html#article" },
  "about": [ { "@id": "https://www.wikidata.org/wiki/Q7501150" }, ... ],
  "author": { "@id": "https://blog.dugong.live/#priya-singh" },
  "publisher": { "@id": "https://blog.dugong.live/#organization" },
  "datePublished": "2026-11-18",
  "dateModified": "2026-11-18",
  "mainEntity": [ ... the 499 questions, untouched ... ]
}
```

and the `HowTo` the same, plus `image` at `#primaryimage`, which is the one property Google's own
HowTo documentation asks for and the only one of these that was absent on all 95.

**No new address is published and no new fact.** `#faq-heading` is the anchor the FAQ section's own
`aria-labelledby` has pointed at since the section was written, on all 96 pages. `#playbook` is the
anchor every one of the 657 `HowToStep` nodes already writes into its own `url`. The author,
publisher and primary image are references to nodes defined four lines above in the same `@graph`.
The entity references are the Wikidata IRIs the 11-17 pass made those entities' own `@id`s. The
dates and the language are copied from the article on the same page.

This is the fifth time in a month the site has turned out to have the node and not the edge: the
`FAQPage` no node referenced before 10-18, the 660 `ListItem` entries naming a URL and no node
before 11-04, the 94 dispatches declaring no page node before 11-16, the 398 anonymous entities
before 11-17. **The node exists, the edge does not.** It is worth saying plainly that this is now a
predictable enough failure mode to look for first.

### The one-off that proves it drifts

`inLanguage` was on 94 of the 95 `HowTo` nodes.
`how-to-fix-shopify-shipping-rates-that-ignore-product-dimensions.html` did not have it, on a page
nothing had touched in weeks. One property, written 94 times by hand and missed once, is the whole
argument for a check rather than a convention: the convention was already there and nothing read it.

## Part 2 - What was deliberately not written

The pass had a rule for itself: **every property added is either a reference to a node already
defined in the same graph, or a scalar the article on the same page already asserts.** Three things
were considered and dropped because they would have broken it.

A `name` on the `FAQPage`. Schema-wise it belongs, and composing one ("Common questions: " plus the
page name) would have meant publishing a string that exists nowhere on the site. Left out.

`supply` and `tool` on the `HowTo`. Google's documentation asks for them, and every candidate value
(Shopify Admin, a gateway's dashboard) would have been this pass inventing a claim about the
playbook. Left out.

Breadcrumb `ListItem` entries, which name `item` as a bare URL string rather than as a node. That
looks like exactly the defect the 11-04 pass fixed for the indexes, and it is **not** one: a string
URL is the form Google's breadcrumb documentation specifies, and the 11-04 check is written to skip
these on purpose. Left alone, and recorded here so a later pass does not "fix" it.

## Part 3 - Six invariants, planted and verified

Six check names, installed into `seo-check.py` and documented in four README rows:

| check | fires when |
|---|---|
| `part_without_url` | a part node's `url` is absent or is not the page plus its own anchor |
| `part_url_anchor_missing` | the `url` is right and the anchor is **not in the markup** |
| `part_isnotpartof_article` | the part does not claim its article back through `isPartOf` |
| `part_without_provenance` | `inLanguage`, `author`, `publisher`, `about`, either date, or the `HowTo`'s `image` is missing |
| `part_provenance_drift` | one of those disagrees with the article on the same page |
| `part_ref_unresolved` | a reference the part makes names no node the site defines |

`about` is compared as an **ordered list of `@id`s**, so a part about something its own article is
not about fails, and the message names the position:
`FAQPage is about 2 entities against 4 on the article; first difference at position 3`. That wording
is the 11-17 lesson applied; that pass shipped two messages which truncated both lists and printed
two different lists identically.

The resolution half needed the 11-04 care: a dict holding nothing but an `@id` is a reference, not a
definition, so a part's own `about` refs cannot vouch for themselves and the article's full entity
nodes are what has to define them. The check was written that way from the start because the 11-04
report says what happens when it is not.

**Every one of the six was verified fail-loud by planting its defect in a copy of the real tree and
running the real checker, at the end of the pass, after the last edit to the file.** Ten defects,
one per run, ten fired, exit code 1 each time. `_qa_tmp/seo-2026-11-18/plant-defects.py` is the
harness and takes the defect name as an argument, so the next pass can re-run any of them in one
command. This is the 11-16 lesson, which is worth repeating in full because it is the most expensive
thing this project has learned: **a report that says a check was added is not evidence that it
runs.**

No existing check was loosened and **no `EXCEPTIONS` entry was added.**

## Part 4 - Audit after the changes

| Check | Result |
|---|---|
| `_tools/seo-check.py` | **PASS**, 110 rendered pages, 82 stubs, 97 dispatches, 109 sitemap URLs, 97 feed items |
| `FAQPage` nodes carrying url / isPartOf / author / publisher / about / both dates | **96 of 96** (was 0 of 96) |
| `HowTo` nodes carrying the same, plus `image` | **95 of 95** (was 0 of 95) |
| `HowTo` nodes carrying `inLanguage` | **95 of 95** (was 94) |
| `Question` nodes now under a parent with a provenance | **499** |
| `HowToStep` nodes now under a parent with a provenance | **657** |
| invariants added | **6**, all verified fail-loud against planted defects in the tree |
| every check name the README claims is in the file | verified by `grep`, before and after |
| writer idempotent | verified, second run reports 0 files and 0 nodes changed on the final tree |
| `apply-checks.py` block identical to what is installed | verified by `diff` against the sandbox copy the plant tests ran against |
| JSON-LD round-trip byte-identical before any edit | verified on all 109 blocks first, so re-serialisation moves nothing |
| **lines changed outside a `ld+json` block, all 192 HTML files** | **0** |
| `md/`, `llms.txt`, `llms-full.txt`, `feed.xml`, `sitemap.xml`, `robots.txt` | **byte-identical**, 0 of 97 md files changed |
| render, 5 pages, 1280 and 390, DOM + geometry + visible text + full-page pixels | **identical, 10 of 10** |
| the same harness, control run (one tree against itself) | **identical, 10 of 10**, run first |
| prose, markup, classes, stylesheets, scripts changed | none |
| em dashes, en dashes, mojibake | 0 |
| duplicate element ids / broken links / anchors | 0 / 0 / 0 |
| total HTML weight | 13,398,251 to 13,568,762 bytes, **+1.273%** |
| the same, gzipped, which is what is served | 2,977,384 to 2,986,134, **+0.294%**, about **46 bytes per page** |

Forty-six gzipped bytes a page to give 499 answers and 657 steps a writer, a publisher, a date, a
language, a topic and an address. The raw cost is higher than 11-17's because an entity reference
spends three lines at `indent=2` and each dispatch now writes two sets of them; gzip charges almost
nothing for the repetition.

**Dates were deliberately not moved.** Every change sits inside a `ld+json` block, nothing a reader
sees is different, and the two dates written onto each part node are copies of the article's. So no
page's `dateModified` moved and no `lastmod` had to, which is the standard the 11-16 and 11-17
passes applied. `lastmod` versus `dateModified` and `index_date_before_newest_listed` both still
pass.

Changed paths: **230** in the working tree, of which **99 are this pass**: 96 page HTML files,
`_tools/seo-check.py`, `_tools/README.md` and this report. The rest are the 10-31 to 11-17 passes
and the Nº 138 to Nº 143 publishing runs, left exactly as they were. The pass's four scripts are in
`_qa_tmp/seo-2026-11-18/`, which `.gitignore` covers, along with a copy of the pre-pass tree that
every before/after number above is measured against.

## Part 5 - Operations

**No collision, for the second day running.** The publishing run shipped Nº 143 at 10:20 to 10:25
and this pass began at 10:36. Both orderings have now been seen; this one is the safe one and it
happens by luck rather than by design, which is still carried item 2.

**The bridge held.** The 11-17 drop is not a thing that has recurred, but the three habits that pass
named were followed anyway and cost nothing: both scripts were written into the tree before being
run, both are idempotent, and the pre-pass tree was copied before the first write. Re-applying the
whole pass is one command.

**The sandbox-first rule was followed.** Every write was dry-run end to end in a copy of the tree
outside the mounted folder, with the checker run against it, before anything was written to the
repository. The writer's first version had a real bug that this caught: it picked the first
`BlogPosting`-shaped dict in the graph, which on `index.html` is one of 97 bare references in the
`Blog` node. It now matches the node whose own `@id` is that page's `#article`.

## Part 6 - Needs a decision

1. **Commit and push. Six passes deep and nineteen days old.** 230 uncommitted paths. Nothing since
   `1059055` on 10-30 is live, which means **dispatches Nº 137 through Nº 143 are all written and
   none of them is on the site**, along with every structural change since 10-31. This has been item
   1 on 10-31, 11-02, 11-04, 11-16, 11-17 and again here. Seven articles and six passes of
   structured-data work are sitting on one disk. **No autonomous run has pushed, by deliberate
   precedent, and none should start without you saying so.** One `git add -A && git commit && git
   push` from a normal shell on the machine publishes all of it. Every other item on this list is
   worth nothing until it is done.
2. **`wikidata.org` and `en.wikipedia.org` are both refused by the egress proxy**, re-tested today
   on both network paths and through `WebFetch`: `connect_rejected`, 403 at the tunnel. So the three
   groundings the 11-17 pass corrected on internal evidence are **still not externally verified**.
   The three to confirm by hand: `Order fulfillment` -> Q1473552, `Pricing` -> Q2516951, `Wholesale`
   -> `/wiki/Wholesaling`. Allow-listing those two hosts would also let a future pass check that the
   111 entity IRIs resolve at all, which nothing has ever done.
3. **Organization `sameAs` still resolves nothing.** It lists `https://dugong.live`, the node's own
   `url`. **Needs someone to supply LinkedIn, X, GitHub or Crunchbase URLs.** After today this is
   starker, not softer: 111 concepts are identified, 499 answers and 657 steps now name the
   publisher, and the publisher is the one node in the graph that is grounded in nothing.
4. **Internal links inside article bodies still carry no fragment.** Carried from 11-04, 11-16 and
   11-17, and still the biggest lever left. Every target now exists: section anchors from 11-02,
   question and answer anchors from 11-04, page nodes from 11-16, entity IRIs from 11-17, and from
   today a `url` on the FAQ and playbook blocks of all 96 dispatches. All 829 links inside article
   bodies still land at the top of their target page. Pointing an existing link at the section or
   the answer that addresses it is a mechanical edit with no new prose, and choosing the target is
   editorial, which is why it keeps waiting.
5. **The lead essay still has no `FAQPage` and no `HowTo`**, the only one of 97 without either, so
   it is the one dispatch today's pass did not touch. Editorial.
6. **Nº 137 is filed in returns and refunds; its own cross-links point at shipping.** Unchanged
   since 10-31. A one-guide edit plus four counts, and it is a real topical-cluster error: the
   dispatch asserts membership of a guide its own links disagree with.
7. **Google Fonts is still a render-blocking third-party stylesheet on all 110 pages.** Unchanged.
   `render-diff.js` now makes the before/after provable, so this is a smaller ask than it was.
8. **og:image is still the same banner on all 110 pages.** Unchanged since 10-12. Worth more now
   that 95 `HowTo` nodes reference `#primaryimage` as the image of the playbook they describe: that
   reference resolves to one generic banner on every dispatch.
9. **Three of the twelve `ItemList` nodes carry no `description`**, found by today's property
   survey and deliberately not fixed, because writing one means writing prose. Noted so it is not
   lost.
10. **258 operational markdown files are still served from the site root**, now 260 including this
    one and today's blog run. `robots.txt` disallows all three prefixes in every group, and because
    of `.nojekyll` that request is the only thing between them and a crawler.
11. **`_qa_tmp/` keeps growing**, now 532MB with the tree, and `_to_delete/` still holds 14
    zero-byte probe files back to 2026-09-17. `.gitignore` covers both, so none of it can reach a
    commit or the live domain. Deleting needs you.
12. **QA's newsletter finding is still open and is still the most serious thing on this list.** The
    signup form in `index.html` has no `action`, no input `name`, and an `onsubmit` that calls
    `preventDefault()`, tells the reader `subscribed`, and sends the address nowhere, beside a
    `4,200 readers` claim nothing supports. Repeated here so it is not lost between two report
    series.
