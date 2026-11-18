# SEO / GEO report - 2026-11-17

Scheduled autonomous run, fired 10:36 UTC. `SEO-GEO-report-2026-11-16.md` and `_tools/README.md`
were read in full first, and the first thing this pass did was the thing the 11-16 pass said every
pass should do from now on: `grep -c` every check name the README claims. **All fifteen were there**,
so the 11-16 restoration held and that lesson has now paid for itself once.

`seo-check.py` passed on the tree as found. So this pass went looking for something no check reads,
and found the site's entity grounding: 398 references to 114 concepts, every one of them grounded in
Wikidata and English Wikipedia, and **not one of them identified**. That is Part 1 and it is the
spine of the pass.

Two things went wrong operationally and both are in here: the daily publishing run had finished
eleven minutes before this pass began, which is the first time in five passes that the collision
*didn't* happen, and then the desktop bridge dropped for twenty-three minutes in the middle, which
is a new failure mode and nearly reproduced the 11-04 disaster by a different route. Part 6.

## Part 0 - The tree as found

`HEAD` = `1059055`, dated 2026-10-30, still the last commit, now eighteen days old. On arrival: 181
uncommitted paths, `seo-check.py` **PASS**, 109 rendered pages, 82 redirect stubs, 96 dispatches,
108 sitemap URLs, 96 feed items. Dispatch Nº 142 had shipped at 10:22 to 10:25 UTC, eleven minutes
earlier.

## Part 1 - 398 grounded entities and no identities

Every dispatch names four or five concepts in its `about` array and grounds each one in two
authorities:

```json
{
  "@type": "Thing",
  "name": "Shopify",
  "sameAs": [
    "https://en.wikipedia.org/wiki/Shopify",
    "https://www.wikidata.org/wiki/Q7501150"
  ]
}
```

That node is anonymous. It has no `@id`, and `@id` is the only property a consumer merges on. So
`Shopify` appeared on **104 pages as 104 unrelated nodes**, `E-commerce` on 46 as 46,
`Business process automation` on 25 as 25, and nothing anywhere in the graph said that any two of
them were the same thing. A crawler reading the whole site came away with 398 one-off strings rather
than 114 concepts the site has an opinion about.

The identifier was already inside each node, one line below the name, in its own `sameAs`. It is now
also its `@id`:

```json
{
  "@type": "Thing",
  "@id": "https://www.wikidata.org/wiki/Q7501150",
  "name": "Shopify",
  "sameAs": [
    "https://en.wikipedia.org/wiki/Shopify",
    "https://www.wikidata.org/wiki/Q7501150"
  ]
}
```

**No new address is published.** The IRI is one the site had already asserted 398 times; it has
simply been moved into the slot that means *this is the thing*, rather than the slot that means
*this is also written about over there*. That is the whole change, and it is the same shape the site
keeps relearning: the FAQPage that no node referenced before 10-18, the 660 `ListItem` entries
naming a URL and no node before 11-04, the 94 dispatches that declared no page node before 11-16.
**The node exists, the edge does not.**

Written on all 395 remaining references, across 105 pages: 96 dispatches, 8 topic guides and the
question index.

Eight entities deliberately get no `@id`, and the check is written so it never asks for one: the
topic guides each name their own subject area (`Shopify inventory automation` and seven more) as a
bare `Thing` with no `sameAs` at all. Those are the guide's own words for a part of a Shopify
operation and no external authority has an item for them.

## Part 2 - Three contradictions that had to be settled before an `@id` could be assigned

You cannot identify a node whose identity the site has not decided, and it turned out the site had
not decided three of them. Each one was settleable from the site's own evidence, and each had been
sitting there unread because the existing entity check asks only whether a node carries *a* Wikidata
URL and *a* Wikipedia URL, never whether two nodes agree.

**One name, two Wikidata items.** `Order fulfillment` read `Q1473552` on 21 pages and `Q7100318` on
one. `Pricing` read `Q2516951` on six and `Q2334719` on one. In both pairs **the Wikipedia URL is
identical**, and one Wikipedia article has exactly one Wikidata item, so at most one id in each pair
can be right and the one used once against twenty-one is a typo that travelled. Corrected to the
majority.

**One name, two Wikipedia URLs.** `Wholesale` carried `/wiki/Wholesaling` twice, including in its
own topic guide, and `/wiki/Wholesale` once, both for `Q220695`. Normalised to the majority.

**One page, one entity, twice.** Three dispatches each declared the same Wikidata item two times
under two names:

| page | item | named |
|---|---|---|
| `...release-held-shopify-orders-when-stock-arrives.html` | Q962928 | `Backorder` and `Stockout` |
| `...shopify-committed-inventory-that-never-clears.html` | Q3761396 | `Inventory management` and `Stock management` |
| `...set-up-tiered-volume-discounts-on-shopify.html` | Q291046 | `Discounts and allowances` and `Volume discount` |

One of the four or five entities each of those pages claimed to be about was a restatement of
another, which dilutes the page's own topic signal and hands a machine two labels for one
identifier. Merged to one node each, with **the minority name kept as `alternateName`** so no
editorial wording is lost and the second phrasing still reaches a reader's index.

Worth noticing: all three were invisible while the nodes were anonymous, and became hard
contradictions the moment the nodes carried an `@id`. That is the argument for identifying them,
not an argument against.

**A caveat that has to stay in the record.** `wikidata.org` is refused by the egress proxy on every
network path a run has: the cloud container's `curl`, the desktop shell's `curl`, and `WebFetch` all
got 403 from the proxy or a site failure. So these three are **internal-consistency fixes, not
externally verified ones**. The majority groundings were verified against both APIs by the 10-19
pass, which is why majority-wins is the right rule here, but a pass with network should still
confirm `Q1473552` and `Q2516951` directly. Carried item 5.

## Part 3 - The renditions the site points models at carried none of it

Every page says this, in its own `<head>`:

```html
<link rel="alternate" type="text/markdown" href="/md/how-to-bulk-edit-product-prices-on-shopify.md"
      title="Markdown version for answer engines" />
```

and `llms.txt` repeats it, and `llms-full.txt` exists for the same reason. Those two renditions are
what the site *tells a model to read instead of the page*.

Neither contained the string `wikidata`. Not once, in any of the 96 md files, or anywhere in the
1.98 MB of `llms-full.txt`. The HTML spent 398 nodes grounding entities for machines, and the one
audience those nodes were written for was being handed the rendition without them.

Each md rendition now carries one line in its header block, after `- Keywords:`:

```
- Entities: Shopify (https://www.wikidata.org/wiki/Q7501150); Pricing (https://www.wikidata.org/wiki/Q2516951); Price (https://www.wikidata.org/wiki/Q160151); Batch processing (https://www.wikidata.org/wiki/Q661613)
```

and each `llms-full.txt` segment the same, after its `Published:` line. Both are generated from the
page's own JSON-LD, so the three renditions cannot drift, and a check now holds them together.

Format follows the house: `Name (URL)`, exactly as the `- Author:` and `Publisher:` lines in the
same block already write a name beside a URL. Entities are separated by `; ` rather than `, `
because a name may itself end in parentheses, as `Last mile (transportation)` does. Deliberately
**not** Markdown link syntax: these are 395 new addresses and writing them as links would put them
into the md-link checks, which exist to compare *editorial* links across renditions.

`llms.txt` gained one line, beside the `Section anchors:` line it has carried since 11-02, because
this is the same kind of fact and belongs in the same place:

> Entity identifiers: every dispatch names the concepts it is about and grounds each one in Wikidata
> and English Wikipedia. Each entity node in a page's JSON-LD carries its Wikidata URI as its own
> `@id`, so the same concept referenced on two pages is one identified entity rather than two
> strings that happen to match, and the per-article Markdown repeats the list on an `- Entities:`
> line. Shopify is https://www.wikidata.org/wiki/Q7501150 on all 104 pages that name it.

The 11-16 pass left `llms.txt` alone and was right to: it had added graph plumbing, not a new
citable address. This pass did add one, 395 times, so the file gets told.

## Part 4 - One `@id`, two values

A site-level node is restated on every page that uses it, which makes it the one part of the graph
that can disagree with itself, and nothing had ever read it.

* **`#aanya-rao`** read `jobTitle` **'Head of Research'** on `index.html` against **'Head of
  Research, Dugong'** on her own page and on her essay, and carried no `worksFor` on `index.html`
  while both other definitions did. One Person, two job titles.
* **`#organization`**'s logo carried `caption: "Dugong"` on 100 pages and no caption on the 8 topic
  guides. One ImageObject, described two ways.

Both aligned to the canonical definition. And then the new check found a third one **by itself**,
which is the best evidence a check can offer for its own existence: **`#priya-singh`** carried her
full 320-character biography on her own page and a one-line abridgement on `index.html`, so the same
Person had two descriptions. Aligned to the canonical one, on the page the node's own `url` names.
`#aanya-rao` on `index.html` carries no description at all, which is an absence rather than a
contradiction, and is left alone.

## Part 5 - The invariants, and the verification

Eleven new.

| Check | Fires when |
|---|---|
| `entity_without_id` | an `about`/`mentions` entity's `@id` is not the Wikidata URI in its own `sameAs` |
| `entity_name_two_ids` | one entity name resolves to two Wikidata items across the site |
| `entity_id_two_names` | one Wikidata item is given two names across the site |
| `entity_name_two_wikipedia` | one entity name resolves to two Wikipedia URLs |
| `entity_duplicated_in_list` | one `about` list names the same Wikidata item twice |
| `md_without_entities` | a dispatch's md rendition has no `- Entities:` line |
| `md_entities_mismatch` | it has one and it disagrees with the page |
| `llms_full_without_entities` | a dispatch's `llms-full.txt` segment header has no `Entities:` line |
| `llms_full_entities_mismatch` | it has one and it disagrees with the page |
| `llms_without_entity_note` | `llms.txt` carries no `Entity identifiers:` line |
| `node_definition_conflict` | one site-level `@id` holds two values for one scalar property |

Verified fail-loud in a scratch copy outside the repository. **Eleven defects planted, all eleven
categories fired**, 16 problems in 11 categories, each naming the page and the value it wanted, exit
code 1, and silent on the real tree:

```
seo-check: FAIL - 16 problem(s) in 11 category(ies)

  entity_duplicated_in_list (1):
    - how-to-set-a-minimum-order-amount-on-shopify.html: .../Q7501150 is named twice in one
      about list, 'Shopify' and 'Shopify (ops)'
  entity_name_two_ids (1):
    - 'Shopify' resolves to ['.../Q7100318', '.../Q7501150'] on different pages
  entity_without_id (2):
    - how-to-handle-high-risk-orders-on-shopify.html: 'Shopify' @id is
      https://blog.dugong.live/#not-an-entity, want https://www.wikidata.org/wiki/Q7501150
    - how-to-win-chargeback-disputes-on-shopify.html: 'Shopify' @id is absent, want .../Q7501150
  md_entities_mismatch (3):
    - md/how-to-set-a-minimum-order-amount-on-shopify.md: 3 entities listed against 4 on the
      page; first difference at position 4, '(nothing)' where the page says 'Shopify (ops) (...)'
  node_definition_conflict (1):
    - https://blog.dugong.live/#priya-singh: jobTitle is ['Commerce Research',
      'Commerce Research, Dugong'] across 97 pages
  ...
```

Sixteen problems against eleven planted defects is the resolver working as designed, the same way
the 11-16 verification ran nineteen against fifteen: regrounding one page's `Shopify` also puts that
page's md and `llms-full.txt` lines out of step with it, and duplicating an entity does the same.
Each knock-on finding is true.

**Two of the eleven were wrong on the first attempt and that is the part worth recording.**
`llms_full_without_entities` did not fire, and the reason was not the check: the *plant* was broken,
because the `Entities:` line is the last line of a segment header and the pattern that deleted it
expected a trailing newline inside the block it was given. And the first version of the two
`*_entities_mismatch` messages truncated both lists to 80 characters, so two lists differing at
entity four printed as identical. Both fixed, the message now naming the position and the two values
(`3 entities listed against 4 on the page; first difference at position 4`). A check that fires
with an unreadable message is most of the way to being a check nobody trusts. **Planting the defect
is what found both.**

No existing check was loosened. **No `EXCEPTIONS` entry was added**, which is the better outcome than
one: `node_definition_conflict` fired once on the real tree, on `#priya-singh`'s two descriptions,
and the answer was to make the site consistent rather than to excuse it.

## Part 6 - What went wrong operationally

**The collision did not happen, for the first time in five passes.** The daily run shipped Nº 142 at
10:22 to 10:25 and this pass began at 10:36, so the ordering that the 11-16 report identified as the
lucky one held by accident again: the publishing run finished first, and every structural change this
pass wrote landed on a tree that already included Nº 142. Nº 142 carries the entity `@id`s, the
`- Entities:` line and the `llms-full.txt` line like every other dispatch, with no hand edit.

**The desktop bridge dropped for twenty-three minutes, 10:52 to 11:15 UTC, in the middle of the
pass.** This is new and it is worth more attention than the collisions, because of exactly where it
landed: the site writers had already run and the checker had **not** yet been extended. Had the
bridge not come back, this pass would have ended with 395 entity identities written across 106 pages
and not one invariant guarding them, **the precise failure the 11-16 pass called the worst available
to this project**, arrived at from a completely different direction.

Three things made the recovery clean, and all three are worth keeping as habits:

1. **Both writers are idempotent and were saved in the tree before being run**, in
   `_qa_tmp/seo-2026-11-17/`. Re-applying the whole site change is one command, whether the loss is a
   bridge drop or a publishing run's rollback.
2. **The remaining work was prepared in the cloud container while the bridge was down**, as scripts
   rather than as intentions, so the moment it returned there was nothing left to re-derive.
3. **The pre-pass tree was copied before the first write.** Every before/after number in Part 7,
   including the byte-region proof, is measured against that copy rather than asserted.

Carried item 2 from 11-04 and 11-16, the lock file, is unchanged and still right. It would not have
helped here.

## Part 7 - Audit after the changes

| Check | Result |
|---|---|
| `_tools/seo-check.py` | **PASS**, 109 rendered pages, 82 stubs, 96 dispatches, 108 sitemap URLs, 96 feed items |
| grounded entity references | 398 before, **395** after (3 merged away) |
| carrying their Wikidata URI as `@id` | **395 of 395** (was 0 of 398) |
| the name-to-entity mapping | before: **116 distinct (name, id) pairs over 114 names and 113 items**, neither a function nor injective. After: **111 names, 111 items, one to one** |
| nodes carrying `alternateName` | 3, the merged minority names |
| md renditions with an `- Entities:` line matching their page | **96 of 96** (was 0) |
| `llms-full.txt` segments with one | **96 of 96** (was 0) |
| `llms.txt` | one `Entity identifiers:` line added beside `Section anchors:` |
| site-level nodes defined one way everywhere | **5 of 5** (`#organization`, `#website`, `#blog`, `#priya-singh`, `#aanya-rao`); 3 conflicts fixed |
| invariants added | **11**, all verified fail-loud against planted defects |
| every check name the README claims is in the file | verified by `grep -c`, 11 of 11, after installing |
| both writers idempotent | verified, second run reports 0 changes on the final tree |
| `apply-checks.py` block identical to what is installed | verified by diff, modulo the template's own escaping |
| JSON-LD round-trip byte-identical before any edit | verified on all 108 blocks first, so re-serialisation moves nothing |
| **lines changed outside a `ld+json` block, all 191 HTML files** | **0** |
| md changed lines that are not the new `- Entities:` line | **0** |
| `llms-full.txt` / `llms.txt` changed lines that are not the new line | **0 / 0** |
| render, 4 pages, 1280 and 390, DOM + geometry + visible text + full-page pixels | **identical, 8 of 8** |
| the same harness, control run (one tree against itself) | **identical, 8 of 8** |
| prose, markup, classes, stylesheets, scripts changed | none |
| em dashes, en dashes, mojibake across pages, md, llms files, feed, sitemap | **0** |
| duplicate element ids / broken links / anchors | 0 / 0 / 0 |
| `sitemap.xml`, `feed.xml` | untouched. Nothing a reader sees changed, so no page's `dateModified` moved and no `lastmod` had to |
| total HTML weight | 13,195,560 to 13,218,861 bytes, **+0.177%** |
| the same, gzipped, which is what is served | 2,935,359 to 2,937,104, **+0.059%**, about **9 bytes per page** |
| md renditions | 2,094,671 to 2,115,676 bytes |
| `llms-full.txt` | 1,984,365 to 2,005,178 bytes |

Nine bytes per page served, for 395 entity identities, because the Wikidata URI already appears two
lines below in the same `sameAs` array and gzip charges almost nothing for the second copy. That is
the cheapest structural change this project has shipped.

**A note on dates, because this pass deliberately moved none.** Every HTML change sits inside a
`ld+json` block; the md and `llms-full.txt` changes are one metadata line in a header block that
already holds ten. Nothing a reader sees is different, which is the standard the 11-16 pass applied
when it wrote a `WebPage` node onto 95 dispatches without touching their dates. The
`lastmod`-versus-`dateModified` check and `index_date_before_newest_listed` both still pass.

**The render check had to be rebuilt, and the 11-16 recipe is why.** That report's lesson was
"freeze animation before diffing this site, or the masthead marquee reports a false positive on
every page". It is half the story, and the half that is missing cost this pass an hour. This site has
**two** animation families: the marquee, and the `.reveal` entrance transition that every article
paragraph and heading carries. And a freeze injected after `load` does not fix either, because it
stops the animation wherever it had got to and that phase is not reproducible. Measured: with the
post-load freeze, **rendering one file twice reported 4 of 8 page-widths different and 116 of 1185
elements off by a single pixel**, with identical DOM and identical visible text. The working version
injects the freeze with `addInitScript`, before the first paint, and names the resting state of both
families.

That harness is now checked in as **`_tools/render-diff.js`**, with the whole story in its header
comment and in the README, so the next pass gets a render check that works instead of rebuilding a
broken one. It compares four channels and takes a `--control` flag, and the README says plainly:
**always run the control first**, because on this site a harness that cannot report one tree
identical to itself cannot report two trees identical to each other, and the failure looks exactly
like a real regression.

Changed paths: **225** in the working tree, of which **208 are this pass**: 106 page HTML files, 96
md renditions, `llms-full.txt`, `llms.txt`, `_tools/seo-check.py`, `_tools/README.md`, the new
`_tools/render-diff.js`, and this report. The rest are the 10-31 to 11-16 passes and the Nº 138 to
Nº 142 publishing runs, left exactly as they were.

## Part 8 - Needs a decision

1. **Commit and push. Five passes deep and eighteen days old.** 225 uncommitted paths. Nothing since
   `1059055` on 10-30 is live, which now means **dispatches Nº 137 through Nº 142 are all written and
   none of them is on the site**, along with every structural change since 10-31. This has been item 1
   on 10-31, 11-02, 11-04, 11-16 and again here. Six articles and five passes of structured-data work
   are sitting on one disk. **No autonomous run has pushed, by deliberate precedent, and none should
   start without you saying so.** One `git add -A && git commit && git push` from a normal shell on
   the machine publishes all of it. This is the one item that makes every other item worth nothing
   until it is done.
2. **The bridge can drop mid-pass, and it did today.** Carried item 2's lock file does not address
   this. What does address it is what saved this pass: writers saved into the tree before they are
   run, and idempotent, so any interruption costs one command rather than a pass. Worth making a
   standing rule rather than a habit that happened to hold.
3. **`wikidata.org` is unreachable from every network path a run has.** The cloud container's
   `curl`, the desktop shell's `curl` and `WebFetch` all failed at the proxy. That means no
   autonomous run can verify an entity grounding against the authority it cites, and three
   groundings were corrected today on internal evidence alone. Either allow-list `wikidata.org` and
   `en.wikipedia.org`, or accept that entity corrections are majority-rule until someone checks by
   hand. **The three to confirm: `Order fulfillment` -> Q1473552, `Pricing` -> Q2516951,
   `Wholesale` -> /wiki/Wholesaling.**
4. **Carried item 4 from 11-04 and 11-16 is unchanged and is still the biggest lever left.** Internal
   links inside article bodies, not one carrying a fragment. Section anchors exist from 11-02,
   question and answer anchors from 11-04, page nodes from 11-16, and from today every concept the
   site writes about is a named entity. Pointing an existing link at the section or the answer that
   addresses it is a mechanical edit with no new prose. Still wants a decision, because choosing the
   target is editorial.
5. **Organization `sameAs` still resolves nothing.** It lists `https://dugong.live`, the node's own
   `url`. **Needs someone to supply LinkedIn, X, GitHub or Crunchbase URLs.** This is now the *only*
   ungrounded entity left in the graph, which makes it conspicuous: 111 concepts the site writes
   about are identified, and the publisher is not. Cheapest entity-grounding win on the list and the
   one no autonomous run can close.
6. **The lead essay still has no FAQPage**, the only one of 96 without one. Editorial.
7. **Nº 137 is filed in returns and refunds; its own cross-links point at shipping.** Unchanged
   since 10-31. A one-guide edit plus four counts.
8. **Google Fonts is still a render-blocking third-party stylesheet on all 109 pages.** The render
   can now be checked properly and reproducibly, so this is a smaller ask than it was. Still wants a
   decision, because the failure mode is a flash of unstyled text and is visible to readers.
9. **og:image is still the same banner on all 109 pages.** Unchanged since 10-12.
10. **258 operational markdown files are still served from the site root**, now including this one.
    `robots.txt` disallows all three prefixes in every group, and because of `.nojekyll` that
    request is the only thing between them and a crawler.
11. **`_qa_tmp/` keeps growing** and `_to_delete/` still holds 14 zero-byte probe files back to
    2026-09-17. This pass added one folder under `_qa_tmp/` holding two writers, two verification
    scripts and four pre-pass page copies. `.gitignore` covers it, so none of it can reach a commit
    or the live domain. Deleting needs you.
12. **QA's newsletter finding is still open and is still the most serious thing on this list.** The
    signup form in `index.html` has no `action`, no input `name`, and an `onsubmit` that calls
    `preventDefault()`, tells the reader `subscribed`, and sends the address nowhere, beside a
    `4,200 readers` claim nothing supports. **A QA pass did run on 11-16**, so this is thirteen days
    old rather than unexamined. Repeated here so it is not lost between two report series.
