# SEO / GEO report - 2026-10-18

Scheduled autonomous run. Last SEO/GEO pass: 2026-10-17. No blog run today.

## Part 0 - Nothing from the last two days is live, and this run proved it rather than inferring it

The 10-17 report opened by closing standing item 0 and opening a new one: 101 changes pending,
nothing pushed. Today there are 108, and the answer is no longer a guess. The browser pane can now
reach blog.dugong.live, which neither shell could on 10-16 or 10-17, so the live site was read
directly:

| Checked on the live site | What it shows |
|---|---|
| `https://blog.dugong.live/how-to-stop-shopify-b2b-prices-dropping-when-you-run-a-sale.html` | **"Page not found"**. Dispatch Nº 130 is not published. |
| `sitemap.xml` | homepage `lastmod` **2026-10-16**. The 10-17 sitemap is not live. |
| `robots.txt` | the **10-16 file**: `Allow: /` first in every group, and no rule for `_qa_tmp/`, `_to_delete/`, `_tools/` or `__deltest.tmp`. |

So, concretely, right now: yesterday's dispatch does not exist for a reader or a crawler; the 317
Wikidata QIDs added on 10-17 are not being served; the four dead or ambiguous entity links are still
being served; and the robots.txt ordering fix is not live, which means on the live file every
`Disallow` is inert for any crawler that uses first-match-wins, and the underscore directories carry
no rule at all.

I have not committed or pushed. The commit history here is hand-written, the diff is a mixed blog-run
and SEO diff, and the tree now also carries today's changes. This is the only item that blocks
everything else, and it is now three days old. A notification went out.

## Part 1 - The checker passed, and the site still had a four-figure markup defect

`_tools/seo-check.py` on the tree as found: **PASS, every invariant holds.** Recomputed from the
files: 178 HTML files, 96 rendered, 82 redirect stubs, 84 dispatches, 95 sitemap URLs, 84 feed items.
Titles, descriptions, dates, canonicals, entity `sameAs`, sitemap, feed, llms coverage, links,
anchors, robots.txt: all clean.

That is worth stating plainly because the rest of this report is about defects the checker did not
look for. A checker written on 10-17 catches the things that broke on 10-16 and 10-17. It says
nothing about the things that have been wrong since the generator was written. This run went looking
for the second kind, by comparing every structured-data claim against the text a reader actually
sees.

## Part 2 - Every HowTo block on the site was a paraphrase of the playbook rather than a copy of it

The largest finding this run, and it was on 82 of 82 pages.

Each dispatch shows the reader a numbered playbook in a `<pre id="playbook">` block. Each dispatch
also carries a `HowTo` node whose `step[].url` points at `#playbook`, which is that exact block. The
markup therefore tells a parser: the procedure is at this anchor. It then described a different
procedure.

Measured before any change, across 572 steps on 82 pages:

| | |
|---|---|
| step `text` values appearing verbatim on the page | **98 / 572** |
| step `text` values appearing nowhere on the page | **453** |
| step `name` values appearing nowhere on the page | **275** |

Not approximately. Nowhere. Take the alt-text dispatch: the page says *"Write a concise, accurate
line that describes what the photo shows, in the store's voice, under about 125 characters"* and the
markup says *"Write a concise accurate line"* for the name and a reworded sentence for the text.
Take the gift-message dispatch: the page says *"Capture the gift toggle, wrap choice, and message as
order attributes, not one buried note"*, the markup says *"Give the shopper a clear gift toggle,
wrap choice, and message field, and store the answer"*.

Why this matters more for GEO than for SEO. Google's structured data policy asks that marked-up
content be present on the page, and HowTo rich results have been retired anyway, so the Google-side
cost is small. The answer-engine cost is not. A model that ingests the page gets two versions of the
same procedure, one from the JSON-LD and one from the prose, differing in wording and sometimes in
count, with the markup asserting its steps live at an anchor whose contents contradict it. Markup
that disagrees with the page is a reason to trust neither.

The site already proves it knows the right pattern. **All 421 FAQ `acceptedAnswer` texts on 83 pages
appear verbatim in the visible page.** The FAQ generator copies. The HowTo generator rewrites. Same
file, same run, two different habits.

**Fixed by regenerating all 82 `step` arrays from the visible playbook.** Each step's `text` is now
the playbook line as written, whitespace normalised. Each step's `name` is a verbatim prefix of that
line: the first clause when it lands between 25 and 60 characters, otherwise the line truncated at a
word boundary at 60. Taking a prefix is what guarantees the name is on the page rather than merely
close to it. `position`, `url`, `totalTime` and the HowTo `description` are unchanged.

After: **566 / 566 step texts and 566 / 566 step names appear verbatim in the visible page.**

## Part 3 - Six pages claimed a seventh step that does not exist

A subset of Part 2, separated because it is a different kind of wrong. Six dispatches declared seven
steps against a six-step playbook:

```
how-to-add-a-gift-message-and-gift-wrap-at-checkout-on-shopify.html
how-to-automatically-hide-sold-out-variants-on-shopify.html
how-to-automatically-pause-ads-for-out-of-stock-products-on-shopify.html
how-to-schedule-product-publishing-on-shopify.html
how-to-set-up-tiered-volume-discounts-on-shopify.html
how-to-sync-bundle-inventory-with-component-stock-on-shopify.html
```

In each case the extra step is the playbook's `# trigger` line promoted into a step. On the sold-out
variant dispatch the markup's step 1 was *"Watch inventory at the variant level"*, which is the
trigger condition, not an instruction, and is step 1 of a seven-step procedure the page never shows.
A paraphrase is a wording problem. An extra step is a claim about the work that is false.

Resolved by Part 2: the step count now comes from the page, so these are 6 steps each.

## Part 4 - The @graph was a bag of nodes with no edges between them

Every dispatch ships one `@graph` holding a `BlogPosting`, a `BreadcrumbList`, a `FAQPage` and a
`HowTo`. Sitting next to each other in a JSON array asserts nothing. A graph needs edges, and there
were none: no article said the how-to or the FAQ was part of it.

Two things were missing, and the first caused the second.

**164 nodes had no `@id`.** 81 `FAQPage` and 83 `BreadcrumbList` nodes carried no identifier at all,
so there was no node to point at even if something had wanted to. `HowTo` had one on all 82 pages and
two `FAQPage` nodes had one, which is how the inconsistency surfaced: the convention existed and was
applied to one node type out of three.

Fixed. Every node now carries an `@id` on the page's own URL: `#article`, `#faq`, `#howto`,
`#breadcrumb`. **369 / 369 graph nodes site-wide.**

**No article claimed its parts.** `hasPart` added to every `BlogPosting`, referencing the page's
`HowTo` and `FAQPage` by `@id`:

```
"hasPart": [
  { "@id": "https://blog.dugong.live/....html#howto" },
  { "@id": "https://blog.dugong.live/....html#faq" }
]
```

83 of 84 dispatches now carry it. The lead essay has neither a how-to nor a FAQ, so it correctly
claims nothing.

## Part 5 - Five entity assertions were pointing at the wrong concept

The 10-17 pass resolved all 115 Wikipedia targets and found three dead links and one disambiguation
page. It did not check the other direction: whether a target that resolves is the thing the entity
is named after. Five were not. All five were re-verified through the Wikipedia and Wikidata APIs
this run, in both directions, the same way the QIDs were sourced on 10-17.

| Entity name | Was pointing at | Problem | Now |
|---|---|---|---|
| Inventory management (3 pages) | `/wiki/Inventory_management_software` | an article about **software**, under a name that means the **practice** | `/wiki/Inventory_management_(business)`, Q3761396 |
| Sales tax | `/wiki/Sales_taxes_in_the_United_States` | narrows a global concept to one country, on a page that also mentions the EU and never says "United States" | `/wiki/Sales_tax`, Q11055488 |
| Transactional email | `/wiki/Email_marketing` | **no article and no Wikidata item exists** for transactional email, and the substitute is the opposite category | entity removed |

The transactional email case is the 10-17 rule applied in reverse. That pass dropped "Minimum order
quantity" rather than substitute a near-miss concept. This was a near-miss substitute already in the
tree: a shipping-delay notification is the canonical example of an email that is *not* marketing. The
page keeps Shopify, Order fulfillment, Customer service and E-commerce, which is the count most
dispatches carry.

Verified: `Sales tax` is a live article, not a disambiguation page, `wikibase_item` Q11055488, and
Q11055488's `enwiki` sitelink is "Sales tax". `Inventory management (business)` round-trips to
Q3761396 the same way. `Transactional email` returns `missing: true` from the Wikipedia API and an
empty result set from `wbsearchentities` on Wikidata.

The other six name-versus-slug differences on the site were checked and left alone: Wholesale to
Wholesaling, Shipping to Freight transport, Promotion to Promotion (marketing), Tag to Tag
(metadata), Observability to Observability (software), Last mile to Last mile (transportation). Each
is a Wikipedia redirect or a parenthetical disambiguator resolving to the right item.

Entity references after this pass: **316, all carrying both a Wikipedia URL and a Wikidata QID**,
113 distinct Wikipedia targets, 109 distinct QIDs.

## Part 6 - The 37 external links are verified, three days after they were first flagged

Standing item 9 from 10-16 and 10-17, carried both times because both shells get 403 on CONNECT to
help.shopify.com and shopify.dev. The browser pane reaches both. Closed.

**All 28 distinct Shopify documentation URLs resolve to a real page with a sensible title.** That
includes `help.shopify.com/en/manual/shopify-flow`, which is linked from 50 pages and would have been
a 50-page defect had it moved.

Two take a redirect hop, neither broken:

- `shopify.dev/docs/api/admin-graphql/2026-10/enums/FulfillmentEventStatus` lands on `/latest/...`.
  Shopify is not serving the pinned 2026-10 path. One link on one page. Worth a decision: naming a
  version is good citation practice, but it costs a hop and lands on a document that may have moved on.
- `shopify.dev/docs/api/admin-graphql` lands on `/latest`. Normal.

The other nine distinct external hosts are the eight Wikipedia article links in body copy, all of
which are among the entity targets verified above, and the Google Fonts and dugong.live links.

## Part 7 - Five new invariants in the checker, tested against the failing tree

`_tools/seo-check.py` gains the checks that would have caught everything in Parts 2, 3 and 4, with
`_tools/README.md` updated to match:

| New check | Fires when |
|---|---|
| `howto_step_text_not_visible` | a step's `text` is not verbatim in the rendered page |
| `howto_step_name_not_visible` | a step's `name` is not verbatim in the rendered page |
| `howto_step_count` | markup step count differs from the visible playbook's |
| `node_without_id` | any node in a `@graph` has no `@id` |
| `article_haspart` | an article does not claim a `HowTo` or `FAQPage` on its own page |

Three helpers were added to support them: `visible_text()` strips scripts, styles and tags and folds
case and punctuation, so comparisons are against what a reader sees rather than against raw HTML;
`playbook_steps()` parses the numbered steps out of the `<pre id="playbook">` block, handling the
wrapped continuation lines; `folded()` normalises a single value the same way.

**Run against this morning's pre-change snapshot the extended checker reports exactly the defects
this pass found**, and nothing else:

```
article_haspart (84)
howto_step_count (6)
howto_step_name_not_visible (275)
howto_step_text_not_visible (453)
node_without_id (164)
```

It also reported `broken_link (288)` on that snapshot, which is an artifact of the tarball rather
than a defect: the before-snapshot was taken with `*.html *.xml *.txt md/` and so omitted
favicon.svg, favicon.png and apple-touch-icon.png. The after-snapshot includes them and the checker
runs clean on it standing alone. Noting it so the next run does not chase it.

No check was loosened and no exception was added. `EXCEPTIONS` is unchanged from 10-17.

## Part 8 - Audit after the changes

| Check | Result |
|---|---|
| `_tools/seo-check.py` on this tree | **PASS** |
| `_tools/seo-check.py` on the extracted after-snapshot | **PASS** |
| HowTo step `text` verbatim in the visible page | **566 / 566** |
| HowTo step `name` verbatim in the visible page | **566 / 566** |
| HowTo step count equals visible playbook count | **82 / 82** |
| FAQ `acceptedAnswer` verbatim in the visible page | 421 / 421 |
| graph nodes carrying an `@id` | **369 / 369** |
| articles claiming their HowTo and FAQPage | **83 / 83** (lead essay has neither) |
| entity refs carrying Wikipedia **and** Wikidata | 316 / 316 |
| entity name agrees with its target's sense | **316 / 316** |
| external Shopify documentation links resolving | **28 / 28** |
| JSON-LD parses, all rendered pages | 95 / 95 |
| title <= 60 and unique, description 70-165 and unique | PASS |
| sitemap lastmod agrees with dateModified | PASS (1 documented exception) |
| broken links / in-page anchors / cross-file anchors | 0 / 0 / 0 |
| mojibake, em dashes, en dashes | 0 |

**No render pass this run, and it is not needed.** Every change was diffed against the pre-run
snapshot and classified by position: **2,786 changed lines across 83 files, all 2,786 inside
`<head>`, zero below it.** sitemap.xml, feed.xml, llms.txt, llms-full.txt, robots.txt and every file
under `md/` are byte-identical to where the 10-17 pass left them. The 10-14 render pass across 8
widths still holds.

`dateModified` and sitemap `lastmod` were deliberately not moved. These are corrections to how the
page describes itself, not changes to what it says; the body text a reader sees is byte-identical.
Moving the dates would tell a crawler the content changed when it did not, and would break the
agreement the checker enforces.

Snapshots: `_qa_tmp/seo-2026-10-18-before.tar.gz` and `_qa_tmp/seo-2026-10-18-after.tar.gz`.

## Part 9 - Needs a decision

1. **Commit and push.** 108 pending changes across three days: Dispatch Nº 130, the whole 10-17 pass
   and this one. Part 0 is no longer an inference, it is a reading of the live site. Yesterday's
   dispatch 404s, the QIDs are not served, the entity repairs are not served, and the robots.txt
   ordering fix is not live. Nothing else in this list matters until this happens.
   Worth knowing what is in that 108: `how-to-stop-shopify-b2b-prices-dropping-when-you-run-a-sale.html`
   and its `/md/` twin are **untracked**, not modified, so Dispatch Nº 130 has never been committed at
   all. So is **the whole of `_tools/`**. The invariant checker written on 10-17, the one this report
   keeps citing, exists only on this machine and would be lost with it.
2. **The blog run paraphrases the playbook into the HowTo markup.** Parts 2 and 3 are not drift, they
   are how the generator has always worked, on every dispatch. The checker now fails the day it
   happens, but the generator should build the `step` array from the playbook block rather than write
   a second version of it. Until it does, every new dispatch arrives with the defect and has to be
   repaired after the fact. **Add `python3 _tools/seo-check.py` to the end of the blog run**, carried
   from 10-17 item 10 and now more useful than it was.
3. **The network situation has changed, and three standing items are affected.** The browser pane
   reaches blog.dugong.live, help.shopify.com, shopify.dev, Wikipedia and Wikidata. Both shells still
   get 403 on CONNECT. That is what closed item 9 this run and what let Part 0 be verified rather than
   assumed. It also means the Google Fonts work below can be measured.
4. **Google Fonts is still a render-blocking third-party stylesheet on all 96 pages.** The only
   external resource the site loads and the only Core Web Vitals lever left: no images, inline CSS,
   almost no JS. `preconnect` and `display=swap` are already there, so the remaining fix is the
   preload-and-swap pattern. Still not done. The reason has changed: it is no longer that the hosts
   are unreachable, it is that the change alters paint behaviour on every page and the browser pane
   can only render the live site, not this working tree, so it could be measured before and not
   verified after. Worth a supervised run.
5. **og:image is still the same banner on all 96 pages.** Unchanged since 10-12. Per-post share
   images would lift click-through from social and from the AI surfaces that show a thumbnail. A
   design call plus a batch render job.
6. **Organization `sameAs` still resolves nothing.** It lists `https://dugong.live`, which is already
   the node's `url`. Searched again this run and again found nothing: the results are unrelated IT
   services companies and an unrelated health entity. **Needs someone to supply real profile URLs**
   (LinkedIn company page, X, GitHub, Crunchbase). Still the largest remaining GEO gap on the site
   and the only one on this list that no run can close on its own.
7. **New dispatches start with zero editorial inbound links** for about three days, until later
   dispatches list them. Measured on 10-17 at 33 to 80 inbound for everything older than three days.
   Retrofitting into 83 historical related-grids would fix it immediately at the cost of 83 files of
   DOM change and a render pass, and it changes what "related" means on every old post. Owner's call,
   carried from 10-17.
8. **The lead essay has 2 editorial inbound links**, against 33 to 80 for every mature dispatch. It
   is the only non-Shopify piece and is excluded from the dispatch related-grids by topic. Carried.
9. **`_qa_tmp/` should be gitignored, not just disallowed.** Whole-site tarballs are committed and
   will be publicly downloadable the moment the 10-17 robots.txt goes live, since robots.txt is a
   request and not an access control. Two more were added today. Carried from 10-17.
10. **`__deltest.tmp` and `_to_delete/` are still committed.** Deleting files on this machine needs a
    permission prompt and nobody is at the desk. Carried from 10-16.
11. **`shopify.dev/docs/api/admin-graphql/2026-10/...` redirects to `/latest/`.** Part 6. One link,
    one page. Pin or follow, someone's call.
12. **Aanya Rao still has no author page**, so her `author` node is the only one of 84 without a
    `url`. Carried from 10-14.
13. **index.html and 404.html keep hand-written og:title and og:description.** Deliberate, inside the
    caps, recorded as a checker exception. Carried.
