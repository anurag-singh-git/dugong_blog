# SEO / GEO report - 2026-11-16

Scheduled autonomous run, fired 18:53 UTC. `SEO-GEO-report-2026-11-04.md` and `_tools/README.md`
were read in full first. `seo-check.py` passed on the tree as found, so this pass went looking for
something no check was reading, and the first thing it found was that **seven of the checks the
README says exist were not in the checker at all**. That is Part 1, and it is the most important
finding here, because it is a failure of the method rather than of the site.

Three defects in the site follow, all of them the same shape the 10-18 pass named and this site
keeps relearning: the node exists, the edge does not.

The daily publishing run collided with this pass again, at 19:05 UTC. Part 5 is that story, and it
ends better than 11-04 did.

## Part 0 - The tree as found

`HEAD` = `1059055`, dated 2026-10-30, still the last commit. On arrival: 173 uncommitted paths,
`seo-check.py` **PASS**, 107 rendered pages, 94 dispatches. Nothing had run since the Nº 140
publishing run of 11-07, nine days earlier.

## Part 1 - The README described a checker that did not exist

The 11-04 pass added seven invariants, documented them in `_tools/README.md`, and verified them
fail-loud against planted defects. The report records the verification output. On arrival today:

```
$ grep -c question_without_anchor  _tools/seo-check.py   -> 0
$ grep -c answer_without_anchor    _tools/seo-check.py   -> 0
$ grep -c listitem_without_item    _tools/seo-check.py   -> 0
$ grep -c dispatch_not_in_guide    _tools/seo-check.py   -> 0
```

Not one of the seven was in the file. The README's last six rows have described them since 11-04.

The cause is almost certainly the collision that pass reported: the publishing run rolled the whole
tree back from a snapshot mid-pass, and the re-application afterwards covered the site writers and
missed the checker. The site changes were idempotent and were re-applied correctly, which is why
they are all still here and were all extended to Nº 140:

| 11-04 change | State today, before this pass |
|---|---|
| `Question` nodes carrying `@id` and `url` at their own `#faq-N` | **481 of 481** |
| `Answer` nodes carrying `#faq-N-answer`, with the id in the markup | **481 of 481** |
| `ListItem` entries naming the node they list via `item` | **593 of 593** |
| dispatches naming their topic guide in `isPartOf` | **93 of 93** that have one |

So the site was right and the guard was gone. For twelve days the project's central artefact, the
file whose whole purpose is that a defect cannot recur quietly, claimed in its own documentation to
be watching four things it was not watching. One dispatch shipped in that window.

All seven are now implemented and verified. The lesson is narrower than "runs collide", and it is
written into the README beside them: **a report saying a check was added is not evidence that it
runs. Run it against a planted defect, in the tree, at the end of the pass.** This pass did that,
and it is the reason the gap was found at all.

## Part 2 - The 94 dispatches were the only pages that never said what they are

Of the 107 rendered pages, the 2 author archives declare a `ProfilePage` and the 9 topic guides
declare a `CollectionPage`. Each one references its own `BreadcrumbList` through `breadcrumb` and
names its `mainEntity`. The 94 dispatches, which are the entire point of the site, declared
nothing. Each carried a `BlogPosting`, a `BreadcrumbList`, an `FAQPage` and a `HowTo`, and:

* **no page node of any kind.** Nothing in the graph said "this is a web page", so there was no node
  for the site's `WebSite` to contain and nothing for a crawler to treat as the document.
* **the `BreadcrumbList` was referenced by nothing.** 94 breadcrumb trails sat in the `@graph`
  asserting no relationship to the page they describe, exactly as the `FAQPage` did before 10-18.
* **`mainEntityOfPage` held a bare URL string.** That names a document, not a node. It is the same
  defect the 11-04 pass fixed for 660 `ListItem` entries, one layer further out, and on 94 pages
  rather than 11.

**Written on all 95 dispatches** (94 plus Nº 141, see Part 5). Each now carries a `WebPage` at
`#webpage`:

```
{
  "@type": "WebPage",
  "@id": "https://blog.dugong.live/...-product-prices-on-shopify.html#webpage",
  "url": "https://blog.dugong.live/...-product-prices-on-shopify.html",
  "name": "How to bulk edit product prices on Shopify",
  "inLanguage": "en",
  "isPartOf": { "@type": "WebSite", "@id": "https://blog.dugong.live/#website", ... },
  "primaryImageOfPage": { "@id": "...#primaryimage" },
  "mainEntity": { "@id": "...#article" },
  "datePublished": "2026-06-28",
  "dateModified": "2026-10-27",
  "breadcrumb": { "@id": "...#breadcrumb" }
}
```

and `BlogPosting.mainEntityOfPage` now points at it rather than restating the URL. The article's
`image` gained an `@id` at `#primaryimage` so `primaryImageOfPage` resolves against a definition
rather than a promise.

The node carries **no `description`**, deliberately. The article it names as `mainEntity` has one,
and restating 650 characters of it on a second node buys nothing a crawler cannot reach in one hop.

**The same check then found three index pages.** `aanya-rao.html`, `priya-singh.html` and
`shopify-automation-questions.html` each had a `BreadcrumbList` their own page node never claimed,
while the 8 topic guides had claimed theirs since they were written. Fixed in the same pass.

## Part 3 - The homepage understated its own freshness by two weeks

`index.html` carried `"dateModified": "2026-10-24"`. Fourteen lines below it, the same `Blog` node
listed a dispatch published **2026-11-07**, and two more published 11-04 and 11-02.

The sitemap agreed with the page, at `2026-10-24`. That is why nothing fired: the existing check
asks whether a page's `dateModified` agrees with its sitemap `lastmod`, and both were stale
together. **Agreement is not truth.**

Three publishing runs had each added a card, a hero masthead, a ticker count, a tag-cloud entry and
a `blogPost` entry to that page without moving its date. The most-crawled page on the site, the one
every crawler reaches first and recrawls most often, told them it had not changed in two weeks.
Every other index page was correct to the day, which is what makes this drift rather than policy:

```
priya-singh.html                   dateModified 2026-11-07   newest listed, published 2026-11-07
shopify-discounts-and-promotions   dateModified 2026-11-07   newest listed, published 2026-11-07
shopify-inventory-automation       dateModified 2026-11-02   newest listed, published 2026-11-02
index.html                         dateModified 2026-10-24   newest listed, published 2026-11-07
```

Corrected to `2026-11-07` in the `Blog` node and in `sitemap.xml`, the day the page actually last
changed. The publishing run then shipped Nº 141 ninety minutes later and moved both to `2026-11-16`,
which is also correct. **The fix was superseded within the hour; the invariant is the durable part.**

**A note on how this check is drawn, because the obvious version is wrong.** The first version
compared an index page's `dateModified` against the newest `dateModified` among the dispatches it
lists, and reported six pages. Five of those six were correct: a later edit to a dispatch's own
prose does not oblige every index that lists it to move. The check compares against the newest
member's **`datePublished`** instead, because membership is written on publication day and so
cannot be argued with. A page cannot have listed a dispatch published on 11-07 while last changing
on 10-24. Six findings became one, and the one is real.

## Part 4 - The invariants, and the verification

Seven restored, eight new.

| Check | Fires when |
|---|---|
| `question_without_anchor` | a `Question`'s `@id` or `url` is not its own `#faq-N` *(restored)* |
| `question_anchor_not_in_page` | that `#faq-N` is not an element id on the page *(restored)* |
| `answer_without_anchor` | an `Answer`'s `@id` or `url` is not its own `#faq-N-answer` *(restored)* |
| `answer_anchor_not_in_page` | that `#faq-N-answer` is not an element id *(restored)* |
| `listitem_without_item` | a `ListItem` names a URL and no `item`, or one that disagrees *(restored)* |
| `listitem_item_unresolved` | a `ListItem`'s `item` points at a node that exists nowhere *(restored)* |
| `dispatch_not_in_guide` | a dispatch's breadcrumb names a guide its `isPartOf` does not *(restored)* |
| `page_without_page_node` | a rendered page declares no `WebPage`, `CollectionPage` or `ProfilePage` |
| `page_node_url` | the page node's `url` is not the page's own canonical |
| `breadcrumb_unreferenced` | a `BreadcrumbList` its own page node does not claim |
| `page_mainentity_unresolved` | a page node's `mainEntity` is missing or points nowhere |
| `page_node_date_drift` | the page node and the article disagree on either date |
| `mainentityofpage_not_node` | `mainEntityOfPage` is a bare string, or is not the page node |
| `primaryimage_unresolved` | `primaryImageOfPage` points at a node that exists nowhere |
| `index_date_before_newest_listed` | an index page's `dateModified` predates the newest dispatch it lists |

Verified fail-loud in a scratch copy outside the repository. **Fifteen defects planted, fifteen
caught**, each naming the page and the value it wanted, exit code 1, and silent on the real tree:

```
seo-check: FAIL - 19 problem(s) in 17 category(ies)

  answer_anchor_not_in_page (1):
    - how-to-win-chargeback-disputes-on-shopify.html: #faq-3-answer
  breadcrumb_unreferenced (1):
    - how-to-stop-card-testing-attacks-on-shopify.html: page node claims no breadcrumb, want ...#breadcrumb
  index_date_before_newest_listed (1):
    - index.html: Blog.dateModified is 2026-10-24 and it lists ...-billing-the-old-price.html published 2026-11-07
  mainentityofpage_not_node (1):
    - how-to-segment-repeat-customers-on-shopify.html: mainEntityOfPage is 'https://...', want ...#webpage
  page_node_date_drift (1):
    - how-to-set-a-minimum-order-amount-on-shopify.html: dateModified 2020-01-01 on the page node, 2026-10-27 on the article
  page_without_page_node (1):
    - how-to-validate-shipping-addresses-on-shopify.html: no WebPage/CollectionPage/ProfilePage node
  ...
```

Nineteen problems against fifteen planted defects is the resolver working as designed: removing one
`Question`'s `@id` also broke the question index's `ListItem` pointing at it, and moving one page
node's date also broke the existing `lastmod` check. Each knock-on finding is true.

No existing check was loosened. Two `EXCEPTIONS` entries were added, both tightenings rather than
loosenings: `page_node_exempt` holds `index.html`, whose page node is correctly the `Blog` itself,
and `404.html`, which carries no JSON-LD and is noindex by design. `WebPage` was added to
`GRAPH_NODE_TYPES` so the standing `@id` check covers it.

## Part 5 - The publishing run collided again, and this time it inherited the work

At 19:05 UTC the daily run began publishing Nº 141 into the same working tree, rewriting all 190
HTML files. Its own report records that it took a whole-site snapshot and used it **twice** to roll
back after two failed first passes, which is the exact mechanism that silently reverted 102 files of
this pass's work on 11-04.

It did not happen this time. Checked immediately and again after the run finished at 19:11:

* `_tools/seo-check.py` and `_tools/README.md` intact, with all fifteen checks.
* `Blog.dateModified` and the sitemap moved 10-24 to 11-07 by this pass, then to 11-16 by the run.
* **95 of 95 dispatches carry a `WebPage` node, including Nº 141.**

That last line is the useful part. `build-n141.py` was started from `build-n140.py` and builds a new
dispatch from the shape of an existing one, so because this pass had already written the node onto
all 94 pages **before** the run templated Nº 141, the new dispatch inherited it: correct `@id`,
correct `url`, correct dates, correct `breadcrumb`, `mainEntityOfPage` pointing at the node. The
checker passes on it without a hand edit.

This is luck with a transferable lesson, and it answers carried item 3 in a way that pass could not:
**a structural change written to every page before the next publishing run gets picked up for free,
because the builder clones a page rather than a template.** A change written after the run, or to
only some pages, does not. The ordering is worth preserving.

Two caveats stand. The run could as easily have rolled back over this work as inherited it, and
nothing in the folder would have said so. Carried item 2, the lock file, is unchanged and is still
the right fix.

## Part 6 - Audit after the changes

| Check | Result |
|---|---|
| `_tools/seo-check.py` | **PASS**, 108 rendered pages, 82 stubs, 95 dispatches, 107 sitemap URLs, 95 feed items |
| dispatches carrying a page node | **95 of 95** (was 0) |
| rendered pages carrying a page node | 106 of 106 that should (`index.html` is the `Blog`, `404.html` has no JSON-LD) |
| `BreadcrumbList` nodes claimed by their own page node | **106 of 106** (was 9) |
| page nodes naming `mainEntity` | 106 of 106 |
| `mainEntityOfPage` as a node reference | **95 of 95** (was 0) |
| `primaryImageOfPage` resolving to a definition | 95 of 95 |
| `Question` / `Answer` nodes fully addressed | 487 / 487, extended to Nº 141 |
| `ListItem` entries naming the node they list | 676 of 676 |
| invariants in the checker | **15 added or restored**, all verified fail-loud |
| writer idempotent | verified, second run reports no change |
| JSON-LD round-trip byte-identical before editing | verified on all 106 blocks first, so re-serialization moves nothing |
| **lines changed outside a `ld+json` block, all 190 files** | **0** |
| prose, markup, classes, stylesheets, scripts changed | none |
| render, 5 pages, desktop and phone, animations frozen | **pixel-identical, 10 of 10** |
| em dashes, en dashes, mojibake | 0 across pages, md renditions, llms files and the feed |
| duplicate element ids / broken links / anchors | 0 / 0 / 0 |
| `sitemap.xml` | `/` lastmod corrected; `feed.xml`, md renditions and `llms-full.txt` untouched |
| `llms.txt` | untouched. This pass added graph plumbing, not a new citable address, so there is nothing a model needs told |
| total HTML weight | 12,923,219 to 13,037,419 bytes, **+0.88%** |
| the same, gzipped, which is what is served | 2,887,634 to 2,897,239, **+0.33%**, about 89 bytes per page |

The render was verified the way 11-04 established: each page beside a mechanically stripped copy of
itself, loaded headless at 1280 and 390 with every animation and transition frozen, screenshotted
full length and compared byte for byte. **Freeze animation before diffing this site** still holds,
or the masthead marquee reports a false positive on every page.

The byte-region check is stronger than the render check for a change of this kind and is new here:
for all 190 HTML files, every line this pass changed was shown to sit between a
`<script type="application/ld+json">` and its closing tag. Not one byte of markup, prose, style or
script moved anywhere on the site.

Changed paths: **176** in the working tree, of which **109 are this pass**: 106 page HTML files,
`sitemap.xml`, `_tools/seo-check.py`, `_tools/README.md` and this report. The rest are the 10-31,
11-02 and 11-04 passes and the Nº 138 to Nº 141 publishing runs, left exactly as they were.

## Part 7 - Needs a decision

1. **Commit and push. Four passes deep and seventeen days old.** 176 uncommitted paths. Nothing
   since `1059055` on 10-30 is live, which now means **dispatches Nº 137, Nº 138, Nº 139, Nº 140 and
   Nº 141 are all written and none of them is on the site**, along with every structural change
   since 10-31. This has been item 1 on 10-31, 11-02, 11-04 and again here. Five articles and four
   passes of structured-data work are sitting on one disk. **No autonomous run has pushed, by
   deliberate precedent, and none should start without you saying so.** This is the one item on this
   list that makes every other item worth nothing until it is done.
2. **Two autonomous runs collided again today.** This pass survived; 11-04 did not. A lock file
   written at the start of a run and removed at the end, or a stub `blog-run-<date>.md`, is still
   the fix. Carried from 11-04 item 2 and from 10-24.
3. **A report claiming a check was added is not evidence that it runs.** Seven invariants were
   documented and absent for twelve days. The habit that fixes it is cheap and is now written into
   the README: plant a defect, run the checker, paste the output. Every pass from here should end
   with `grep -c` on the names it claims to have added.
4. **Carried item 4 from 11-04 is unchanged and still the biggest lever left.** Internal links
   inside article bodies, not one carrying a fragment. Section anchors exist from 11-02, question
   and answer anchors from 11-04, and from today every page is itself an addressable node. Pointing
   an existing link at the section or the answer that addresses it is a mechanical edit with no new
   prose. Still wants a decision, because choosing the target is editorial.
5. **Organization `sameAs` still resolves nothing.** It lists `https://dugong.live`, the node's own
   `url`. **Needs someone to supply LinkedIn, X, GitHub or Crunchbase URLs.** The one GEO gap no
   autonomous run can close, and the cheapest entity-grounding win on the list.
6. **The lead essay still has no FAQPage**, the only one of 95 without one. Editorial.
7. **Nº 137 is filed in returns and refunds; its own cross-links point at shipping.** Unchanged
   since 10-31. A one-guide edit plus four counts.
8. **Google Fonts is still a render-blocking third-party stylesheet on all 108 pages.** The render
   can now be checked properly, so this is a smaller ask than it was. Still wants a decision,
   because the failure mode is a flash of unstyled text and is visible to readers.
9. **og:image is still the same banner on all 108 pages.** Unchanged since 10-12.
10. **255 operational markdown files are still served from the site root**, now including this one.
    `robots.txt` disallows all three prefixes in every group, and because of `.nojekyll` that
    request is the only thing between them and a crawler.
11. **`_qa_tmp/` keeps growing** and `_to_delete/` still holds 14 zero-byte probe files back to
    2026-09-17. This pass added three scratch folders under `_qa_tmp/`. `.gitignore` covers it, so
    none of it can reach a commit or the live domain. Deleting needs you: `device_bash` cannot
    delete inside a connected folder without a permission prompt, and no one is at the desk.
12. **QA's newsletter finding is still open and is still the most serious thing on this list.** The
    signup form in `index.html` has no `action`, no input `name`, and an `onsubmit` that calls
    `preventDefault()`, tells the reader `subscribed`, and sends the address nowhere, beside a
    `4,200 readers` claim nothing supports. **No QA pass has run in twelve days.** Repeated here so
    it is not lost between two report series.

## Part 8 - robots.txt, checked and left alone

`robots.txt` names 38 user-agent groups, explicitly allows every major answer-engine crawler
(GPTBot, OAI-SearchBot, ClaudeBot, Claude-SearchBot, PerplexityBot, Google-Extended,
Applebot-Extended, Bingbot, CCBot, DuckAssistBot, Meta-ExternalAgent and the rest), repeats the
three report disallows in every group because a named group ignores the `*` group, declares the
sitemap, and points at `llms.txt`, `llms-full.txt` and the feed in its trailing comments. Nothing
to add. Recorded so a later pass does not spend time rechecking it.
