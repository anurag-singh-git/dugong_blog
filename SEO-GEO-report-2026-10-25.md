# SEO / GEO report - 2026-10-25

Scheduled autonomous run, fired 11:33 UTC for a 10:35 slot. `SEO-GEO-report-2026-10-24-2.md`
was read in full first, then today's `QA-report-2026-10-25.md`, so this pass would not re-do
the tag-cloud and 404 work that QA had already done this morning. Two things were worked:
carried item 3, the short-answer backlog, and one defect class that no check had been reading.
The second turned out to explain why four read times on the site had always passed a check
designed to catch exactly them.

## Part 0 - The tree as found

`git status` showed 90 uncommitted paths. `HEAD` = `origin/main` = `9be41c4`, so the owner's
commit cleared the three unpushed layers the 10-24 reports asked about. Thank you; the loop
works. What has accumulated since is today's own traffic: the 10:46 QA pass, the 10:59
publishing run that shipped dispatch Nº 136, and now this.

`_tools/seo-check.py` **PASS** on the tree as found: 103 rendered pages, 82 redirect stubs,
90 dispatches, 102 sitemap URLs, 90 feed items, no notes.

No snapshot was written into `_qa_tmp/`. Both parts below needed an exact before-tree to verify
a new check against, and `HEAD` is no longer that tree, so the 26 pages and 26 `/md/` renditions
this pass touched were copied to the session scratch outside the repository first. Nothing was
added to `_qa_tmp/`.

No blog-run collision. Nº 136 had landed 34 minutes before this pass began, and the tree was
quiet throughout.

## Part 1 - Fourteen more dispatches carry a short answer, and the range is now Nº 81 to Nº 136

Carried item 3, worked with the method the 10-24 passes put on the record and followed without
variation: read the dispatch's full `/md/` rendition, draft three paragraphs that answer the
headline question in the first sentence, state plainly what Shopify does and does not do
natively, name the mechanism and stop. Every factual claim is one the article already makes.

On the tree as found, 42 of 90 dispatches had a short answer. **Written for 14, extending
coverage contiguously backwards from Nº 94 to Nº 81.** Coverage is now **56 of 90**, and the
covered range Nº 81 to Nº 136 has **no gaps**.

| Dispatch | Nº | wordCount |
|---|---|---|
| `automatically-release-held-shopify-orders-when-stock-arrives` | 94 | 2385 to 2610 |
| `route-shopify-orders-to-the-right-warehouse` | 93 | 2450 to 2682 |
| `sync-supplier-inventory-feeds-to-shopify` | 92 | 2500 to 2710 |
| `stop-discount-code-abuse-on-shopify` | 91 | 2300 to 2513 |
| `catch-and-cancel-duplicate-orders-on-shopify` | 90 | 2200 to 2399 |
| `block-a-customer-on-shopify` | 89 | 2290 to 2509 |
| `notify-customers-of-shipping-delays-on-shopify` | 88 | 2130 to 2363 |
| `merge-duplicate-customer-profiles-on-shopify` | 87 | 2020 to 2254 |
| `stop-discount-codes-applying-to-sale-items-on-shopify` | 86 | 2010 to 2242 |
| `add-a-gift-message-and-gift-wrap-at-checkout-on-shopify` | 85 | 2090 to 2320 |
| `set-up-tiered-volume-discounts-on-shopify` | 84 | 1990 to 2215 |
| `sync-bundle-inventory-with-component-stock-on-shopify` | 83 | 2140 to 2371 |
| `automatically-pause-ads-for-out-of-stock-products-on-shopify` | 82 | 2240 to 2472 |
| `limit-purchase-quantity-per-customer-on-shopify` | 81 | 2810 to 3034 |

Gates were run on every draft as a script before anything was written to disk, because the
10-24 gate list is a specification and worth executing rather than eyeballing:

| Gate | Result across all 42 paragraphs |
|---|---|
| paragraphs per block | 3, each 349 to 497 characters, inside the 190 to 700 house range |
| sentences of 55 characters or more appearing verbatim in the article | 0 |
| non-ASCII, em dashes, en dashes, smart quotes, HTML entities | 0 |
| inline HTML used | `<em>` and `<code>` only |

One gate failure was caught and fixed before writing: the opening sentence of the Nº 86 draft
reproduced that article's own first FAQ answer word for word. Rewritten, re-gated, clean.

Written in all three renditions by one script so the three cannot diverge by hand: the page as
`<div class="short-answer" id="short-answer">` holding an `<h2>The short answer</h2>` placed
immediately before the first substantive heading in `.article-body`, the `/md/` file as
`## The short answer` in the same position with `<em>` as Markdown emphasis, and `llms-full.txt`
as a `## The short answer` block with emphasis stripped. `.short-answer` was added to
`speakable.cssSelector` between `.article-title` and `.faq`, and `BlogPosting.abstract` carries
the first paragraph as plain text.

Two whitespace corrections were made after inspecting the written output rather than trusting
the script: the page block landed with two blank lines above it and none below, where the house
form is one of each, and the `/md/` heading landed with two blank lines above it. Both corrected
on all 14 in all renditions, so the diff reads like the 42 pages that already carried the block.

**Dates moved on these 14**, by the 10-18 policy: a new section of original prose the reader has
not seen. `article:modified_time`, JSON-LD `dateModified`, `sitemap.xml` `lastmod`, the md
`- Updated:` line and the `llms-full.txt` `Updated:` field were carried to 2026-10-25 together.
`feed.xml` carries only `pubDate` and needed nothing.

34 of 90 dispatches still have no short answer. The next one is Nº 80, and coverage is still
contiguous, so the next pass needs no bookkeeping.

## Part 2 - The length a dispatch claims disagreed with itself on twelve pages, and the check could not see it

This is the part worth reading twice, because the defect was hiding behind a passing check.

A dispatch states its own length six times: both ticker spans, the JSON-LD `wordCount` and
`timeRequired`, the `N MIN READ` span in the byline, and the `- Word count:` and `N min read`
lines in the `/md/` rendition. **On twelve dispatches they disagreed.**

| Dispatch | Nº | JSON-LD and md said | the reader was shown | short |
|---|---|---|---|---|
| `make-shopify-wholesale-customers-tax-exempt` | 122 | 2,037 | 1,950 | 87 |
| `handle-price-adjustment-requests-on-shopify` | 123 | 1,963 | 1,820 | 143 |
| `handle-shopify-returns-the-customer-never-sends-back` | 124 | 2,250 | 2,075 | 175 |
| `fix-shopify-committed-inventory-that-never-clears` | 125 | 2,351 | 2,166 | 185 |
| `catch-shopify-shipping-label-adjustments...` | 126 | 2,584 | 2,277 | 307 |
| `catch-shopify-orders-where-half-the-order-never-ships` | 127 | 2,468 | 2,367 | 101 |
| `stop-reordering-shopify-stock-you-already-have-on-order` | 128 | 2,462 | 2,341 | 121 |
| `handle-return-to-sender-orders-on-shopify` | 129 | 2,852 | 2,680 | 172 |
| `stop-shopify-b2b-prices-dropping-when-you-run-a-sale` | 130 | 3,000 | 2,780 | 220 |
| `catch-shopify-shipping-labels-you-never-used` | 131 | 3,301 | 3,118 | 183 |
| `stop-shipping-shopify-orders-with-payment-pending` | 132 | 3,001 | 3,118 | +117 |
| `bulk-edit-variant-metafields-on-shopify` | 133 | 2,872 | 2,687 | 185 |

**Which number was right was not a judgment call.** Counting the words actually rendered inside
`.article-body` puts the JSON-LD within 0.5 percent on every one of the twelve, and the ticker
100 to 307 words out. Across all 90 dispatches the JSON-LD `wordCount` is within 5 percent of
the rendered count, which is ordinary editorial rounding; the ticker on these twelve was not
rounding, it was a different number.

**The cause is specific and already closed upstream.** Nos 122 to 133 are exactly the window in
which the publishing run shipped a short answer at publication but wrote the ticker from the
body count taken *before* the short answer was appended. On eleven of the twelve the gap equals
the short answer's own length to within the four words of its heading, which is the whole
proof. Nº 121 agrees, Nº 134 onward agrees, so the window is twelve consecutive dispatches
published 10-10 to 10-21 and the generator stopped doing it at Nº 134. This is a back-catalogue
repair, not a convention change. Nº 132 is the one exception and a separate slip: its ticker ran
117 words *high* and claimed 10 min against 9 everywhere else.

**And this is why it matters more than a wrong label.** The `read_time_band` check reads the
ticker. So for every one of these twelve it was dividing the stale, lower word count by the
claimed minutes, and certifying the result. Corrected, four of them are outside the 150 to 320
band the check exists to enforce:

| Dispatch | corrected words | claimed min | words per minute |
|---|---|---|---|
| `catch-shopify-shipping-label-adjustments...` | 2,584 | 8 | **323** |
| `catch-shopify-shipping-labels-you-never-used` | 3,301 | 10 | **330** |
| `stop-shipping-shopify-orders-with-payment-pending` | 3,001 | 9 | **333** |
| `stop-shopify-b2b-prices-dropping-when-you-run-a-sale` | 3,000 | 9 | **333** |

Two more, Nos 133 and 129, landed at 319 and 317, inside the band by a hair and above the entire
rest of the site, which runs 172 to 312.

**Fixed on all twelve.** The ticker now carries the JSON-LD count in both spans, and the read
time was raised on six pages to the smallest value that puts them inside the band, written to
all four places that state it. Nos 126 and 129 to 9 and 10 min, Nos 131, 132, 130 and 133 to 11,
10, 10 and 10. Afterwards the whole archive runs 172 to 308 words per minute, median 267, with
nothing above 310.

**No dates moved for this part.** A corrected count is a correction to a label, not a section of
prose the reader has not seen, which is the distinction the 10-18 policy draws and the
distinction the 10-24 pass applied when it fixed 87 READING callouts without moving a date.

## Part 3 - Two invariants, one of them a widening

`_tools/seo-check.py` and `_tools/README.md` updated.

| Check | Fires when | Status |
|---|---|---|
| `length_claim_divergence` | a dispatch's six statements of its own length do not all agree | new |
| `read_time_band` | ...and now also when the ticker cannot be parsed at all, in either character spelling | widened |

The widening is the part worth auditing, because it explains a second blind spot. The band
check's pattern matched only the entity spelling of the ticker's two separators, `&#9670;` and
`&middot;`. Thirty-four back-catalogue dispatches write the same two characters literally, which
renders identically and parses identically, and the pattern walked straight past them. **The
check was reading 56 of 90 dispatches and reporting a pass on the other 34 by never looking at
them.** None of the 34 is in fact out of band, which is luck. A ticker the check cannot parse is
now a failure rather than a silent pass, and the pattern reads both spellings, so coverage is
90 of 90.

Verified in both directions, which is the point of adding a check at all:

```
# against the pre-fix tree, only the 12 pages swapped back
seo-check: FAIL - 27 problem(s) in 1 category(ies)
  length_claim_divergence (27)

# against the current tree, with one ticker deliberately mangled and one
# literal-form page's read time pushed out of band
seo-check: FAIL - 5 problem(s) in 2 category(ies)
  length_claim_divergence (3):
  read_time_band (2):
    - how-to-block-a-customer-on-shopify.html: no parseable MIN READ / WORDS ticker
    - how-to-handle-high-risk-orders-on-shopify.html: 1550 words in 3 min is 517 words per minute, outside 150-320
```

Against the pre-fix tree it reports exactly the twelve pages, as 27 individual divergences, in
exactly one category, and nothing else. Note what the pre-fix run does *not* report:
`read_time_band` stays silent there, which is the whole finding. No check was loosened. Both
changes are strictly additional: one guards agreement nothing read before, the other removes a
silent-skip path and doubles the other's coverage.

The 34 literal-spelling tickers were **not** migrated to the generator's current entity form.
The precedent for a back-catalogue migration exists, from the 87 READING callouts on 10-24, but
it does not apply: an HTML entity and the character it denotes parse to the same text node, so
neither a reader nor a machine can tell these apart, and rewriting 34 files to change invisible
bytes would only enlarge a diff you still have to review. The blindness was the defect and the
check now carries it. Recorded below in case you would rather have the consistency.

## Part 4 - Audit after the changes

| Check | Result |
|---|---|
| `_tools/seo-check.py` | **PASS**, 103 rendered pages, 82 stubs, 90 dispatches, 102 sitemap URLs, 90 feed items |
| `length_claim_divergence` against the pre-fix tree | fires on exactly 12 pages, 27 entries, 1 category |
| `read_time_band` fail-loud and both spellings | verified on a mangled ticker and a literal-form page |
| band-check coverage | **90 of 90** dispatches (was 56) |
| short answer on the page, in the md and in llms-full | **56 of 90** (was 42), contiguous Nº 81 to Nº 136, no gaps |
| renditions in disagreement on the short answer | 0 of 56 |
| short answer wrapped, speakable and carrying an abstract | 56 of 56 |
| `abstract` text present in the visible page | 56 of 56 |
| six length claims agree, per dispatch | **90 of 90** (was 78) |
| claimed words per minute, whole archive | 172 to 308, median 267 |
| JSON-LD parses | 185 / 185 html files |
| `dateModified` vs `sitemap.xml` `lastmod` | agrees on all; the one difference is the lead essay, a documented `EXCEPTIONS` entry |
| md `- Updated:` and llms-full `Updated:` vs page `dateModified` | agrees on all 73 that carry the field; the other 17 have `dateModified` equal to `datePublished` and correctly omit it |
| tag balance, 14 tag types, all 185 html files | 0 imbalances |
| em dashes, en dashes, mojibake across pages, md, llms-full, llms.txt, sitemap, feed | 0 |
| broken internal links / in-page anchors / cross-file anchors | 0 / 0 / 0 |
| duplicate element ids | 0 |
| total HTML weight | 11,664,011 to 11,692,155 bytes, **+0.24%** |

Render: not visually verified, for the reason the 10-21, 10-24 and 02:27 passes give. The in-app
browser cannot open `file://` and cannot reach a server started in either shell. Structural
verification was used instead and is recorded above. Every Part 1 page change is an additional
element of a kind the page already contains in the same container, wrapped in a `<div>` whose
class has shipped on 42 pages with no stylesheet rule and identical rendering; Part 2 changed
digits inside spans that already existed. Note that today's QA pass *did* run a full render
sweep at five widths, two and a half hours before this one, which covers the layout these
changes sit inside.

Changed paths: **57**, all modifications apart from this report. 26 page HTML files, 26 `/md/`
renditions, `llms-full.txt`, `sitemap.xml`, `_tools/seo-check.py` and `_tools/README.md`.

## Part 5 - Needs a decision

1. **Commit and push.** 123 uncommitted paths: the 90 from this morning's QA pass and the Nº 136
   publishing run, plus the 33 new here. Nothing from today is live. `9be41c4` cleared the
   previous backlog, so the pattern is working; it needs a hand again.
2. **Organization `sameAs` still resolves nothing.** It lists `https://dugong.live`, which is
   already the node's own `url`. Still the one GEO gap no autonomous run can close.
   **Needs someone to supply LinkedIn, X, GitHub or Crunchbase URLs.**
3. **34 of 90 dispatches still have no short answer.** Down from 48 this morning, 62 yesterday
   and 74 on 10-21. Coverage is contiguous Nº 81 to Nº 136, so the next pass starts at Nº 80.
   Fourteen a pass clears the rest in under three runs.
4. **Carried item 4 is closed.** Nº 136, published today, arrived with the short-answer
   container, the `speakable` selector, the `abstract` and a canonical READING callout, and so
   did 134 and 135. Three consecutive posts is a generator change, not luck. Part 2 adds the
   evidence: the generator also stopped writing a stale ticker count at Nº 134, in the same
   window. Whatever shipped then was right.
5. **Carried item 5 looks closed too, and is worth a glance.** Nº 136 is linked from 80 pages
   against a median of 54 for the archive, so the publishing run now extends the READ NEXT
   grids rather than leaving each new dispatch outside the link graph. Three passes spent fixing
   74 grids by hand; worth confirming this was the generator and not this morning's QA pass.
6. **Stagger the two routines, or make the collision loud.** Carried from 10-18 onward. Today
   came closer than any previous day: the QA pass began at 10:46 and the publishing run fired at
   10:59 while it was mid-flight. QA handled it, by taking its backups after the run landed and
   re-verifying from scratch, but it handled it rather than being protected from it. Adding
   `python3 _tools/seo-check.py` to the end of the blog run remains the cheap half.
7. **Median outbound editorial links per dispatch is still falling by month of publication.**
   Measured inside `.article-body`: 4 in June, 7 in July, 8 in August, 2 in September, 3 in
   October, unchanged from yesterday's measurement. Inbound is healthy, so new posts are found;
   they weave outward thinly. Generator behavior, not a page backlog, and the last large on-page
   lever a pass could move by hand. Doing it by hand means writing prose into 15 recent
   dispatches, so it is left for a decision rather than taken.
8. **Google Fonts is still a render-blocking third-party stylesheet on all 103 pages.**
   `preconnect` and `display=swap` are in place; making the stylesheet non-blocking risks a
   flash of unstyled text and wants a supervised run with a render check.
9. **og:image is still the same banner on all 103 pages.** Unchanged since 10-12.
10. **The ticker's two separators are written two ways across the site**, as entities on 56
    dispatches and as literal characters on 34. Invisible to readers and machines alike, and the
    check now reads both, so this is consistency rather than a defect. Say the word and a pass
    migrates the 34 to the generator's current form; otherwise it stays as it is.
11. **247 operational markdown files are still served from the site root**: 88
    `SEO-GEO-report-*` including this one, 73 `blog-run-*` and 86 `QA-report-*`. `robots.txt`
    disallows all three prefixes in every group, and because of `.nojekyll` that request is the
    only thing between them and a crawler. Still worth a decision rather than an autonomous
    commit, since this routine writes into that root.
12. **`_qa_tmp/` is now 166 MB**, up from 145 MB yesterday; today's QA pass added
    `run-10-25`. `.gitignore` lists it, so nothing in it can reach a commit or the live domain.
    What is left is local disk that nothing reads, growing 11 to 21 MB a day. Deleting the
    directories older than the last two runs needs you, since `device_bash` cannot delete inside
    a connected folder without a permission prompt and no one is at the desk to answer one.
    Related: `_to_delete/` holds 14 zero-byte probe files going back to 2026-09-17, which is the
    same story in miniature.
13. **QA's newsletter finding is not an SEO item but it is the most serious thing open.**
    This morning's report records that the signup form in `index.html` has no `action`, no input
    `name` and an `onsubmit` that calls `preventDefault()`, tells the reader `subscribed`, and
    sends the address nowhere, beside a `4,200 readers` claim nothing supports. Repeating it here
    so it is not lost between two report series.
