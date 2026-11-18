# SEO / GEO report - 2026-11-04

Scheduled autonomous run, fired 04:28 UTC. `SEO-GEO-report-2026-11-02.md` and `_tools/README.md`
were read in full first. `seo-check.py` passed on the tree as found, so this pass went looking for a
defect no check was reading and found one in the structured data: **the site addressed its 469 FAQ
questions everywhere except inside the 91 pages that own them**. That is fixed, along with two other
edges the graph asserted in one direction only, and there are seven new invariants behind all three.

The run also collided with the daily publishing run, which fired into the same folder at the same
time and rolled the whole site back from a snapshot mid-pass. Part 0 is that story, because it
changes what carried item 3 is worth.

## Part 0 - The tree as found, and a collision

`HEAD` = `1059055`, dated 2026-10-30, still the last commit. On arrival: 165 uncommitted paths,
`seo-check.py` **PASS**, 104 rendered pages, 91 dispatches.

At 04:40 UTC, mid-pass, the daily blog run began publishing dispatch Nº 139 into the same working
tree. Its own report records what happened next: it took a whole-site snapshot before its first
write, failed its QA pass, and **rolled the entire site back from that snapshot**. The snapshot
predated this pass's first write, so the rollback silently reverted 102 files of work that had
already been written and verified. The run's report says "nothing was half-written", which is true
of the run's own output and false of everything else in the folder.

The damage was visible and total: of 91 pages carrying the new answer anchors, 1 survived. The work
was re-applied after the publishing run finished at 04:45:31, which cost nothing but time because
the writer is idempotent, and the second application covered Nº 139 as well. Both runs' output is
now in the tree and the checker passes on all of it.

Two things follow. First, **the publishing run does not write these edges**, so Nº 140 will arrive
without them; the invariants added below are what will catch that, and the builder at
`_qa_tmp/build-n139.py` is where the fix belongs. Second, carried item 3, "make the publishing run's
state legible", has stopped being a tidiness request. A lock file would have made this pass wait.
Without one, two autonomous runs wrote the same 100 files in the same minute and one of them
restored a snapshot over the other's work with no error, no warning and no record.

One check fired against the publishing run while it was half-finished: `ticker_month`, reading 1 new
dispatch this month against a November holding 2. It was rewritten to 2 here, then rolled back with
everything else, and the run's own rebuild wrote the correct value. It reads 2 now and passes.

## Part 1 - The questions had addresses everywhere except where they live

Every FAQ answer on this site sits in a `.faq-item` with `id="faq-1"` through `id="faq-N"`. The
question index links all 469 questions to those anchors and writes the full URL of each one into its
`ItemList`. The anchors work, the index works, and the convention has been in place since the index
was written.

Inside the 91 `FAQPage` blocks, **not one `Question` node carried an `@id` or a `url`**:

```
{
  "@type": "Question",
  "name": "Does Shopify automatically fulfill orders and add tracking numbers?",
  "acceptedAnswer": { "@type": "Answer", "text": "Only in narrow cases. ..." }
}
```

That node is what Google reads for the FAQ rich result and what an answer engine lifts when it
quotes one of these answers. It named a question and an answer and said nothing about where either
one lives, on a site that already knew the address and had already written it down in a different
file. An engine citing it could name the page and nothing finer, on a page carrying up to seven
other questions.

This is the same shape as the heading ids of 11-02, one layer further in. There the address did not
exist; here it existed, in the index, and the node that owns it had never been told.

**Written on all 92 pages with an FAQ**: 475 `Question` nodes now carry `@id` and `url` at their own
`#faq-N` anchor, and 475 `Answer` nodes carry `#faq-N-answer`. The answer identifier is not a
promise made in JSON about markup that does not exist: `id="faq-N-answer"` is written onto the
matching `<p class="faq-a">` in the same pass, so both identifiers resolve in the DOM, and an
invariant checks that they do.

```
{
  "@type": "Question",
  "@id": "https://blog.dugong.live/...-tracking-numbers-to-shopify-orders.html#faq-1",
  "url": "https://blog.dugong.live/...-tracking-numbers-to-shopify-orders.html#faq-1",
  "name": "Does Shopify automatically fulfill orders and add tracking numbers?",
  "acceptedAnswer": {
    "@type": "Answer",
    "@id": "https://blog.dugong.live/...-tracking-numbers-to-shopify-orders.html#faq-1-answer",
    ...
```

**What the reader sees: nothing.** One attribute on a paragraph that already existed, and JSON in the
head. No prose changed, no class was introduced, no element was added or moved. By the 10-18 policy
and the 11-02 precedent, no date moved, and `sitemap.xml`, `feed.xml`, the md renditions and
`llms-full.txt` needed no edit. `llms.txt` now documents the answer-anchor convention beside the
section-anchor convention it has carried since 11-02, in the same register, so a model that wants to
cite one answer knows the identifier without fetching the page to infer it.

## Part 2 - Two edges the graph asserted in one direction only

The 10-18 pass established the rule this site keeps relearning: adjacency is not an edge, and the
edge has to be written. Two more were missing.

**A list that names a URL does not name a node.** `index.html`'s `Blog` node has referenced
`#article` ids since it was written. Nothing else did. The eight topic guides, the two author
archives and the question index listed **652 items by bare URL**, so every edge from an index to the
thing it indexes landed on a page rather than on the node inside it. All 660 `ListItem` entries now
carry `item` pointing at the node they list: `#article` for a dispatch, `#faq-N` for a question, the
latter resolving against the identifiers Part 1 created.

**A guide collects its dispatches; no dispatch said it belonged.** `isPartOf` on every `BlogPosting`
named the Blog and stopped. The breadcrumb names the topic guide, but a breadcrumb asserts a
navigation position, not membership. 92 dispatches now name their guide's `CollectionPage` in
`isPartOf` alongside the Blog, so the topical cluster is a graph in both directions rather than a
list the guides keep to themselves. The lead essay belongs to no guide and correctly names only the
Blog.

## Part 3 - The invariants, and the verification

| Check | Fires when |
|---|---|
| `question_without_anchor` | a `Question`'s `@id` or `url` is not its own `#faq-N` |
| `question_anchor_not_in_page` | that `#faq-N` is not an element id on the page |
| `answer_without_anchor` | an `Answer`'s `@id` or `url` is not its own `#faq-N-answer` |
| `answer_anchor_not_in_page` | that `#faq-N-answer` is not an element id on the page |
| `listitem_without_item` | a `ListItem` names a URL and no `item`, or an `item` that disagrees with it |
| `listitem_item_unresolved` | a `ListItem`'s `item` points at a node that exists nowhere on the site |
| `dispatch_not_in_guide` | a dispatch's breadcrumb names a guide its `isPartOf` does not |

Verified fail-loud, in a scratch copy outside the repository. Six defects planted, six caught, each
naming the page and the value it wanted, exit code 1, and silent on the real tree:

```
seo-check: FAIL - 6 problem(s) in 5 category(ies)

  answer_anchor_not_in_page (1):
    - how-to-fix-duplicate-skus-on-shopify.html: #faq-3-answer
  answer_without_anchor (1):
    - how-to-block-a-customer-on-shopify.html: answer 2 url is missing, want ...#faq-2-answer
  dispatch_not_in_guide (1):
    - how-to-win-chargeback-disputes-on-shopify.html: ...shopify-fraud-and-risk-automation.html#collection
  listitem_without_item (2):
    - priya-singh.html: '...' -> ...#ghost, want ...#article
    - shopify-returns-and-refunds-automation.html: '...' -> no item, want ...#article
  question_without_anchor (1):
    - how-to-automatically-tag-orders-on-shopify.html: question 1 @id is missing, want ...#faq-1
```

**The seventh check was wrong the first time, and the reason is worth keeping.** A seventh defect,
a `ListItem` whose `url` and `item` agreed with each other and pointed at a node that does not
exist, passed. The resolver built its set of known identifiers by collecting every `@id` in every
document, which included the pointer under test: **the reference vouched for itself**. A dict holding
nothing but an `@id` is a reference, not a definition, and is now excluded from the known set. With
that fixed the seventh defect fails loud:

```
  listitem_item_unresolved (1):
    - shopify-automation-questions.html: ...how-to-find-shopify-products-with-no-cost-per-item.html#faq-99
```

No existing check was loosened and no exception was added. The change is strictly additional.

## Part 4 - Render verified, for the first time since 10-21

Every pass from 10-21 to 11-02 recorded the same caveat: the render could not be checked, because
the in-app browser cannot open `file://` and cannot reach a server started in either shell. That is
still true of the in-app browser. It is not true of the cloud container, which carries Chromium and
a matching Playwright.

So the pages were rendered and compared pixel by pixel. For each page, the current file and a
mechanically stripped copy of itself with this pass's additions removed were loaded headless, with
animations frozen so the masthead ticker does not read as a difference, and screenshotted full
length at desktop and phone width:

| Page | 1280px | 390px |
|---|---|---|
| `how-to-fix-shopify-flow-emails-that-never-send.html` (Nº 139) | 1280x17201, **identical** | 390x27642, **identical** |
| `how-to-automatically-add-tracking-numbers-to-shopify-orders.html` | 1280x14710, **identical** | 390x23833, **identical** |
| `shopify-inventory-automation.html` | 1280x4763, **identical** | 390x8847, **identical** |
| `priya-singh.html` | 1280x15445, **identical** | 390x34769, **identical** |

Not one pixel differs on any of the eight renders. The first comparison, run before animations were
frozen, showed a 12-pixel band at the top of two pages and nothing else, which was the ticker
marquee at a different phase. That is worth recording for the next pass: **freeze animation before
diffing this site, or the masthead will report a false positive on every page.**

This removes the standing caveat. A future pass that does change something visible can verify it.

## Part 5 - Audit after the changes

| Check | Result |
|---|---|
| `_tools/seo-check.py` | **PASS**, 106 rendered pages, 82 stubs, 93 dispatches, 105 sitemap URLs, 93 feed items |
| questions carrying their own address | **475 of 475** (was 0) |
| answers carrying their own address | **475 of 475** (was 0) |
| `#faq-N-answer` ids written into the markup | 475, every one resolving |
| `ListItem` entries naming the node they list | **660 of 660** (was 0) |
| dispatches naming their topic guide in `isPartOf` | **92 of 92** that have one |
| writer idempotent | verified, second run reports no change, three separate applications |
| duplicate element ids, any page | 0 |
| JSON-LD parses | every block in all 106 html files |
| JSON-LD round-trip byte-identical before editing | verified on all 104 blocks first, so re-serialization moves nothing |
| prose changed | none |
| dates moved | none, and none were due |
| `sitemap.xml` / `feed.xml` / md renditions touched by this pass | no |
| em dashes, en dashes, mojibake | 0 across all 106 pages |
| broken internal links / in-page anchors / cross-file anchors | 0 / 0 / 0 |
| render, desktop and phone, 4 pages | pixel-identical |
| total HTML weight | 12,267,762 to 12,621,297 bytes, **+2.88%** |
| the same, gzipped, which is what is served | 2,805,694 to 2,824,561, **+0.67%**, about 178 bytes per page |

The uncompressed figure is the largest any pass has added, and it is worth naming rather than
burying: the additions are long absolute URLs repeated twice per question. They compress to almost
nothing, which is why both numbers are here.

Changed paths: **169** in the working tree, of which **107 are this pass**: 103 page HTML files,
`llms.txt`, `_tools/seo-check.py`, `_tools/README.md` and this report. The rest are the 10-31 and
11-02 passes and the Nº 138 and Nº 139 publishing runs, left exactly as they were.

## Part 6 - Needs a decision

1. **Commit and push. Three passes deep and five days old.** 169 uncommitted paths. Nothing since
   `1059055` on 10-30 is live, which now means **dispatches Nº 137, Nº 138 and Nº 139 are all
   written and none of them is on the site**, along with every structural change since 10-31. This
   has been item 1 on 10-31, on 11-02 and again here.
2. **Two autonomous runs collided today and one silently reverted the other.** Carried item 3 has
   evidence now. A lock file written at the start of a run and removed at the end, or a stub
   `blog-run-<date>.md`, would have made this pass wait rather than work into a folder that was
   about to be rolled back. The rollback was the right call for the publishing run; it had no way to
   know anything else was in the folder.
3. **The publishing run does not write the edges added today, or the heading ids added on 11-02.**
   Nº 139 arrived without them and was fixed by hand here. The builder is
   `_qa_tmp/build-n139.py`, it is gitignored, and this pass did not touch it. Either it imports the
   writers or every future dispatch needs a pass like this one behind it. The invariants at least
   make the omission loud.
4. **Carried item 2 from 11-02 is unchanged and still the biggest lever left.** 829 internal links
   inside article bodies, not one carrying a fragment. Section anchors existed from 11-02; question
   and answer anchors exist from today. Pointing an existing link at the section or the answer that
   addresses it is a mechanical edit with no new prose. Still wants a decision, because choosing the
   target is editorial.
5. **Organization `sameAs` still resolves nothing.** It lists `https://dugong.live`, the node's own
   `url`. **Needs someone to supply LinkedIn, X, GitHub or Crunchbase URLs.** The one GEO gap no
   autonomous run can close.
6. **The lead essay still has no FAQPage**, the only one of 93 without one. Writing questions for a
   signed essay is an editorial call.
7. **Nº 137 is filed in returns and refunds; its own cross-links point at shipping.** Unchanged
   since 10-31. A one-guide edit plus four counts.
8. **Google Fonts is still a render-blocking third-party stylesheet on all 106 pages.** Making it
   non-blocking risks a flash of unstyled text, and now that the render can actually be checked, this
   is a smaller ask than it was. Still wants a decision, because the failure mode is visible to
   readers.
9. **og:image is still the same banner on all 106 pages.** Unchanged since 10-12.
10. **253 operational markdown files are still served from the site root**, now including this one.
    `robots.txt` disallows all three prefixes in every group, and because of `.nojekyll` that request
    is the only thing between them and a crawler.
11. **`_qa_tmp/` is over 169 MB** and `_to_delete/` still holds 14 zero-byte probe files back to
    2026-09-17. This pass added four small scratch folders under `_qa_tmp/` for the render
    comparison. `.gitignore` covers `_qa_tmp/`, so none of it can reach a commit or the live domain.
    Deleting needs you: `device_bash` cannot delete inside a connected folder without a permission
    prompt, and no one is at the desk to answer one.
12. **QA's newsletter finding is still open and is still the most serious thing on this list.** The
    signup form in `index.html` has no `action`, no input `name`, and an `onsubmit` that calls
    `preventDefault()`, tells the reader `subscribed`, and sends the address nowhere, beside a
    `4,200 readers` claim nothing supports. **No QA pass has run in ten days.** Repeated here so it
    is not lost between two report series.
