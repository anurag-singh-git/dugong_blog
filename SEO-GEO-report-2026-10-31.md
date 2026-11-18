# SEO / GEO report - 2026-10-31

Scheduled autonomous run, fired 20:32 UTC for a 10:30 slot, so this is the first pass on the
repository since 2026-10-25. `SEO-GEO-report-2026-10-25.md` was read in full first, along with
`_tools/README.md`. Two things were worked: carried item 3, the short-answer backlog, which is
now **closed**, and one rendition defect in the md and `llms-full.txt` copies of that block that
no check had been reading. A publishing run also fired into the middle of this pass and spent
twenty minutes looking as though it had died half-published. It had not. That is written up in
Part 0 because the false alarm is the part worth reading.

## Part 0 - The tree as found, and the publishing run that fired into this pass

`git status` was **clean** on arrival and `HEAD` = `1059055`, dated 2026-10-30, so the owner's
commit cleared everything the 10-25 reports asked about. Thank you; the loop works.

`_tools/seo-check.py` **PASS** on the tree as found: 103 rendered pages, 82 redirect stubs, 90
dispatches, 102 sitemap URLs, 90 feed items.

Two things about the gap since 10-25 are worth recording.

**A pass ran on 10-27 and wrote no report.** Commit `1059055` carries 33 files that are
unmistakably a short-answer pass: 14 dispatch pages, their 14 `/md/` renditions, `llms-full.txt`,
`sitemap.xml` and a 123-line addition to `_tools/seo-check.py`. Short-answer coverage was 56 of 90
when the 10-25 report closed and 70 of 90 when this pass opened, which is exactly those 14. There
is no `SEO-GEO-report-2026-10-27.md` on disk or in the history. The work landed and the account of
it did not, so this report is the only place the 10-27 batch is written down. Its 14 are listed in
Part 1 for that reason.

**No run of any kind happened 10-28 through 10-30.** No report in any of the three series, and no
dispatch published between Nº 136 on 10-25 and Nº 137 today. Worth a glance at the schedules.

**The publishing run collision, and why it looked worse than it was.** At 20:46, mid-pass, dispatch
Nº 137, `how-to-handle-wrong-item-shipped-claims-on-shopify`, appeared on disk. For the next five
minutes it was half-published in the worst possible way: page and `/md/` file present, linked from
`index.html`, and **absent from `sitemap.xml`, `feed.xml`, all three `llms.txt` lists,
`llms-full.txt`, the Priya Singh archive, the question index and every one of the eight topic
guides**, with 74 archive READ NEXT grids unextended and `index.html` claiming 463 questions
against 457 listed. No `blog-run-2026-10-31.md`. Every signal said the run had died between
shipping the page and registering it, which is the failure mode carried item 6 has been warning
about since 10-18, so a notification went out saying so and this pass began rebuilding the
registration by hand.

**It had not died. It was slow.** The run resumed at 20:51 and finished at 20:53:43, registering
Nº 137 across every surface itself, including an editorial inbound link written into
`how-to-automate-returns-and-exchanges-on-shopify`. The hand-built `llms-full.txt` entry this pass
had prepared was thrown away unused. Net effect on the tree: nothing. Net effect worth keeping:

- **A six-minute silence in the middle of a publishing run is indistinguishable from a dead run.**
  There is no lock, no marker file and no "in progress" signal, so the only way to tell is to wait
  and see. A pass that had been less patient would have written a second copy of every registration
  entry on top of the run's own.
- This is carried item 6 with the argument now made for it. A lock file, or simply writing
  `blog-run-<date>.md` as a stub at the *start* of a run rather than the end, would have cost the
  run one line and saved this pass twenty minutes and the owner one false alarm.
- The run's own ordering is worth a look while you are in there. It writes `index.html`, including
  the question count, several minutes **before** the question index that count refers to, so there
  is a real window in which the homepage states a number the site cannot support.

Nothing in this pass was built on the registration work, and the two writers did not collide: all
44 paths this pass wrote are intact, verified paragraph by paragraph in Part 3, including the one
file the publishing run also edited.

## Part 1 - The short-answer backlog is closed: 91 of 91

Carried item 3, worked with the method the 10-24 and 10-25 passes put on the record and followed
without variation: read the dispatch's full `/md/` rendition, draft three paragraphs that answer
the headline question in the first sentence, state plainly what Shopify does and does not do
natively, name the mechanism and stop. Every factual claim is one the article already makes.

On the tree as found, 70 of 90 dispatches carried a short answer. **Written for the remaining 20**,
Nº 66 down to Nº 47, which is the whole tail of the back catalogue. Nº 137 arrived today carrying
its own. Coverage is now **91 of 91 with no gaps**, and this item needs no bookkeeping in the next
report because there is nothing left to carry.

| Dispatch | Nº | wordCount | min |
|---|---|---|---|
| `automatically-request-product-reviews-on-shopify` | 66 | 2370 to 2586 | 9 |
| `segment-repeat-customers-on-shopify` | 65 | 2320 to 2541 | 9 |
| `add-alt-text-to-shopify-product-images-in-bulk` | 64 | 2390 to 2601 | 9 |
| `generate-shopify-product-descriptions-with-ai` | 63 | 2220 to 2411 | 9 |
| `automatically-tag-orders-on-shopify` | 62 | 2120 to 2317 | 9 |
| `bulk-edit-meta-descriptions-on-shopify` | 61 | 2090 to 2286 | 9 |
| `schedule-a-sale-on-shopify` | 60 | 2170 to 2361 | 9 |
| `set-inventory-reorder-points-on-shopify` | 59 | 2130 to 2330 | 9 |
| `set-up-an-abandoned-cart-email-sequence-on-shopify` | 58 | 2250 to 2446 | 9 |
| `push-sold-out-products-to-the-bottom-of-a-shopify-collection` | 57 | 2130 to 2316 | 9 |
| `set-up-back-in-stock-notifications-on-shopify` | 56 | 2010 to 2207 | 9 |
| `win-chargeback-disputes-on-shopify` | 55 | 1930 to 2119 | 9 |
| `automate-returns-and-exchanges-on-shopify` | 54 | 1820 to 2019 | 9 |
| `edit-a-shopify-order-after-its-been-placed` | 53 | 1700 to 1890 | 9 |
| `validate-shipping-addresses-on-shopify` | 52 | 1500 to 1683 | 7 |
| `handle-high-risk-orders-on-shopify` | 51 | 1550 to 1761 | 9 |
| `prevent-overselling-on-shopify-across-channels` | 50 | 1600 to 1799 | 8 |
| `reduce-where-is-my-order-wismo-tickets-on-shopify` | 49 | 1320 to 1503 | 6 |
| `best-shopify-automations-to-set-up` | 48 | 1650 to 1866 | 8 |
| `the-death-of-the-drag-and-drop-builder` | 47 | 820 to 1007 | 4 |

For the record, since no report covers them, the 14 the 10-27 pass wrote were Nos 67 to 80:
`automatically-add-a-free-gift-with-purchase`, `automatically-add-tracking-numbers`,
`automatically-cancel-unpaid-orders`, `automatically-hide-sold-out-variants`,
`automatically-send-invoices`, `automatically-split-and-route-orders-to-multiple-suppliers`,
`bulk-edit-product-prices`, `combine-multiple-orders-from-the-same-customer`,
`fix-404-errors-from-deleted-products`, `reconcile-shopify-payouts-with-your-sales`,
`schedule-product-publishing`, `set-a-minimum-order-amount`, `set-up-pre-orders-without-holding-in-stock-items`
and `stop-card-testing-attacks`.

Gates were run on all 60 paragraphs as a script before anything was written to disk, because the
10-24 gate list is a specification and worth executing rather than eyeballing:

| Gate | Result across all 60 paragraphs |
|---|---|
| paragraphs per block | 3, each 218 to 495 characters, inside the 190 to 700 house range |
| sentences of 55 characters or more appearing verbatim in the article | 0 |
| non-ASCII, em dashes, en dashes, smart quotes, HTML entities | 0 |
| inline HTML used | `<em>` and `<code>` only |

One gate failure was caught and fixed before writing, which is the second time in three passes
the gate has earned its place: the third paragraph of the Nº 48 draft reproduced 102 characters of
that article's own fourth FAQ answer word for word. Rewritten, re-gated, clean.

**Two judgment calls in this batch worth your eye, because neither is a how-to dispatch.**

Nº 48 is a field study and Nº 47 is the signed lead essay, not merchant questions about what
Shopify does natively, so the house form had to bend. Both were written as the short answer to
the page's own title rather than to a Shopify capability question: for Nº 48, why the automations
merchants build are not the ones that pay back, with the 14 percent against 0.8 percent split; for
Nº 47, why the canvas is failing, with the 31 percent node growth against 9 percent work growth and
the 43 percent of nodes that were only grammar. Every figure is the essay's own. Nº 47 is the one
to read first if you disagree with the call, since it is 187 new words in an 820-word essay under
someone's name, and reverting one file is the whole cost of disagreeing.

Written in all three renditions by one script so the three cannot diverge by hand: the page as
`<div class="short-answer" id="short-answer">` holding an `<h2>The short answer</h2>` placed
immediately before the first substantive heading in `.article-body`, the `/md/` file as
`## The short answer` in the same position with `<em>` as Markdown emphasis and `<code>` as
backticks, and `llms-full.txt` as a `## The short answer` block with emphasis stripped and
backticks kept. `.short-answer` was added to `speakable.cssSelector` between `.article-title` and
`.faq`, and `BlogPosting.abstract` carries the first paragraph as plain text.

**Dates moved on all 20**, by the 10-18 policy: a new section of original prose the reader has not
seen. `article:modified_time`, JSON-LD `dateModified`, `sitemap.xml` `lastmod`, the md `- Updated:`
line and the `llms-full.txt` `Updated:` field were carried to 2026-10-31 together. One of the 20, the lead
essay, had no `- Updated:` line in the md because `dateModified` equalled `datePublished`; it
gained one. `feed.xml` carries only `pubDate` and needed nothing.

**No read time was raised.** All 20 land between 195 and 289 claimed words per minute after the
addition, against the 150 to 320 band. The whole archive now runs 195 to 308, median 270.

**One documented exception lapsed and was retired.** `EXCEPTIONS["lastmod_vs_datemodified"]` held
`the-death-of-the-drag-and-drop-builder.html` on the stated ground that the essay's URL first
appeared 2026-10-14 while the essay text had not changed since 2026-05-28. Nº 47 gained a short
answer today, so both dates moved to 2026-10-31 together and the exception has nothing left to
excuse. The key is kept, empty, with the reason written next to it, because the same situation
recurs the next time a URL is republished without its text changing. `seo-check.py` passes with
the set empty, which is the proof the dates genuinely agree rather than being excused.

## Part 2 - The short answer ran into the next heading in 39 renditions, and pandoc ate it

This is the part worth reading twice, because the defect was invisible to the two parsers most
people would reach for to test it.

The block is written into the `/md/` rendition and into `llms-full.txt` by script, and over three
passes two scripts wrote it two ways. On the tree as found, **25 of the 90 md files and 14
`llms-full.txt` entries ran the block's last paragraph straight into the following `## ` heading
with no blank line between them.** The 10-27 batch wrote the blank line; the 10-24 and 10-25
batches did not, which is how one block came to have two shapes.

**Why it looked like nothing.** CommonMark lets an ATX heading interrupt a paragraph, so the
heading is still a heading and the page still reads correctly. Tested directly:

```
python-markdown: '<p>Para text ends here.</p>\n<h2>Next heading</h2>\n<p>More text.</p>'
marked:          '<p>Para text ends here.</p>\n<h2>Next heading</h2>\n<p>More text.</p>'
```

**Why it is not nothing.** pandoc's default markdown reader does not treat it that way:

```
pandoc -f markdown -t html
in:  Para ends here.\n## Next heading\n\nMore.
out: <p>Para ends here. ## Next heading</p>
     <p>More.</p>
```

The heading is swallowed into the paragraph, and the paragraph it is swallowed into is the one
paragraph on the page written to be lifted whole as the answer. The `/md/` renditions exist for
exactly one purpose, which is to be read by machines that are pointed at them, and pandoc is not
an exotic choice of reader. The section boundary underneath the short answer went with it.

**Fixed on all 39**, 25 md files and 14 `llms-full.txt` entries, by inserting the one blank line.
No prose changed, so no date moved: this is the same distinction the 10-25 pass drew when it
corrected twelve word counts without moving a date.

For the record, this pass took the opposite decision from the 10-25 pass on the ticker's two
separator spellings, and the difference is the point. That one was declined because an HTML entity
and the character it denotes parse to the same text node, so no reader and no machine could tell
them apart, which made it a cosmetic diff. This one is a difference a real parser acts on. The test
for a back-catalogue migration is whether anything downstream can see it, not whether it looks
untidy.

## Part 3 - One invariant, and the verification

`_tools/seo-check.py` and `_tools/README.md` updated.

| Check | Fires when | Status |
|---|---|---|
| `short_answer_tail` | the short answer's last paragraph runs into the next `## ` heading with no blank line, in a `/md/` file or an `llms-full.txt` entry | new |

Verified in both directions, which is the point of adding a check at all. Against the pre-fix
shape, reconstructed in a scratch copy outside the repository:

```
# blank line removed from one md file
  short_answer_tail (1):
    - md/how-to-validate-shipping-addresses-on-shopify.md: the short answer runs into
      "## What Shopify actually does (and doesn't)" with no blank line between them

# and removed from one llms-full.txt entry as well
  short_answer_tail (2):
    - md/how-to-validate-shipping-addresses-on-shopify.md: ...
    - llms-full.txt:how-to-win-chargeback-disputes-on-shopify.html: the short answer runs
      into '## How big the bill actually is' with no blank line between them
```

It reads both renditions, names the heading it collided with, and is silent on the fixed tree. No
check was loosened. The change is strictly additional.

## Part 4 - Audit after the changes

| Check | Result |
|---|---|
| `_tools/seo-check.py` | **PASS**, 104 rendered pages, 82 stubs, 91 dispatches, 103 sitemap URLs, 91 feed items |
| short answer on the page, in the md and in llms-full | **91 of 91** (was 70), no gaps |
| the 60 new paragraphs present verbatim in all three renditions | 180 of 180 checks |
| renditions in disagreement on the short answer | 0 of 91 |
| short answer wrapped, speakable and carrying an abstract | 91 of 91 |
| `abstract` text present in the visible page | 91 of 91 |
| `short_answer_tail` across md and llms-full | **0 of 91** (was 39 renditions) |
| `short_answer_tail` fail-loud | verified on both renditions in a scratch tree |
| six length claims agree, per dispatch | 91 of 91 |
| claimed words per minute, whole archive | 195 to 308, median 270 |
| JSON-LD parses | every block in all 104 html files |
| `dateModified` vs `sitemap.xml` `lastmod` | agrees on all, with the `EXCEPTIONS` set now empty |
| md `- Updated:` and llms-full `Updated:` vs page `dateModified` | agrees |
| em dashes, en dashes, mojibake across the 44 paths this pass wrote | 0 |
| broken internal links / in-page anchors / cross-file anchors | 0 / 0 / 0 |
| duplicate element ids | 0 |
| total HTML weight | 11,715,480 to 11,943,406 bytes, **+1.95%**, of which Nº 137 is most |

Render: not visually verified, for the reason the 10-21, 10-24 and 10-25 passes give. The in-app
browser cannot open `file://` and cannot reach a server started in either shell. Structural
verification was used instead and is recorded above. Every page change in Part 1 is an additional
element of a kind the page already contains, in the same container, wrapped in a `<div>` whose
class has now shipped on 90 other pages with no stylesheet rule and identical rendering; Part 2
changed whitespace in Markdown files only and touched no HTML at all.

Changed paths: **147** in the working tree, of which **44 are this pass**: 20 page HTML files, 20
`/md/` renditions plus the 25 md whitespace fixes that overlap them, `llms-full.txt`, `sitemap.xml`,
`_tools/seo-check.py`, `_tools/README.md` and this report. The other 103 are the Nº 137 publishing
run's, which this pass did not write and has left exactly as the run left them.

## Part 5 - Needs a decision

1. **Commit and push.** 147 uncommitted paths: 44 from this pass and 103 from the Nº 137
   publishing run. Nothing from today is live, including the new dispatch. `1059055` cleared the
   previous backlog, so the pattern is working; it needs a hand again.
2. **Carried item 3 is closed and can come off the list.** 91 of 91.
3. **Make the publishing run's state legible, which is carried item 6 with evidence behind it
   now.** The run wrote nothing for six minutes mid-flight and was indistinguishable from a dead
   run that had shipped a page and skipped every registration surface. One line at the start of a
   run, a stub `blog-run-<date>.md` or a lock file, removes the ambiguity. Relatedly, the run
   writes `index.html` and its question count several minutes before the question index that count
   describes, so the homepage briefly states a number the site cannot support.
4. **The 10-27 pass wrote no report.** Its work is in `1059055` and is reconstructed in Part 1, but
   a pass that commits 33 files and no account of them is worth knowing about, and 10-28 to 10-30
   produced no run of any kind in any of the three series.
5. **Organization `sameAs` still resolves nothing.** It lists `https://dugong.live`, which is
   already the node's own `url`. Still the one GEO gap no autonomous run can close.
   **Needs someone to supply LinkedIn, X, GitHub or Crunchbase URLs.**
6. **Nº 137 went into the returns and refunds guide; its own cross-links point the other way.**
   The publishing run filed it under `shopify-returns-and-refunds-automation`, which is defensible:
   the settlement is a return with an exchange item, plus a restock. But both dispatches its
   READING callout names, `catch-shopify-orders-where-half-the-order-never-ships` and
   `catch-shopify-shipping-label-adjustments`, sit in shipping and fulfillment, and the mechanism
   the piece actually turns on is the order's expected weight against the carrier's scanned weight,
   which is a fulfillment check. Moving it is a one-guide edit plus four counts. Left as filed.
7. **The lead essay has no FAQPage.** It is the only dispatch of the 91 without one, and the only
   one besides the Nº 48 field study without a HowTo, which is reasonable for an essay. It now
   carries a short answer, an abstract and a speakable selector, so it is no longer invisible to an
   answer engine, but a FAQPage on the site's thesis page is the kind of thing that gets quoted.
   Writing questions for a signed essay is an editorial call rather than an autonomous one.
8. **Median outbound editorial links per dispatch is still falling by month of publication.**
   Re-measured this pass inside `.article-body`, counting distinct dispatch pages linked: 4 in
   June (range 2 to 7, n=24), 7 in July (5 to 12, n=24), 8 in August (4 to 11, n=20), 2 in
   September (2 to 2, n=5), 3 in October (2 to 10, n=16). That reproduces the 10-25 figures
   exactly, so the trend is real and has not moved. Inbound is healthy, so new posts are found;
   they weave outward thinly. Generator
   behavior, not a page backlog, and the last large on-page lever a pass could move by hand. Doing
   it by hand means writing prose into 15 recent dispatches, so it is left for a decision.
9. **Google Fonts is still a render-blocking third-party stylesheet on all 104 pages.**
   `preconnect` and `display=swap` are in place; making the stylesheet non-blocking risks a flash
   of unstyled text and wants a supervised run with a render check.
10. **og:image is still the same banner on all 104 pages.** Unchanged since 10-12.
11. **The ticker's two separators are still written two ways**, as entities on some dispatches and
    as literal characters on others. Invisible to readers and machines alike, and the band check
    reads both, so this is consistency rather than a defect. Declined again on 10-31 for the reason
    in Part 2. Say the word and a pass migrates them.
12. **249 operational markdown files are still served from the site root**: 90 `SEO-GEO-report-*`
    including this one, 73 `blog-run-*` and 86 `QA-report-*`. `robots.txt` disallows all three
    prefixes in every group, and because of `.nojekyll` that request is the only thing between them
    and a crawler. Still worth a decision rather than an autonomous commit, since this routine
    writes into that root.
13. **`_qa_tmp/` is 169 MB and has barely grown since 10-25**, which fits: no QA pass has run
    since.
    `.gitignore` lists it, so nothing in it can reach a commit or the live domain. Deleting the
    directories older than the last two runs needs you, since `device_bash` cannot delete inside a
    connected folder without a permission prompt and no one is at the desk to answer one. Related:
    `_to_delete/` holds 14 zero-byte probe files going back to 2026-09-17.
14. **QA's newsletter finding is still open and is still the most serious thing on this list.**
    The 10-25 QA report records that the signup form in `index.html` has no `action`, no input
    `name` and an `onsubmit` that calls `preventDefault()`, tells the reader `subscribed`, and
    sends the address nowhere, beside a `4,200 readers` claim nothing supports. Repeating it here
    so it is not lost between two report series, and noting that no QA pass has run in six days to
    repeat it itself.
