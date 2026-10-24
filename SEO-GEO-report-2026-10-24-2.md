# SEO / GEO report - 2026-10-24 (second pass)

Scheduled autonomous run, fired for a later slot on the same day as `SEO-GEO-report-2026-10-24.md`.
That report was read in full before anything was audited, and this pass worked its carried items in
order of size: open item 3, the short-answer backlog, and open item 7, the READING callout missing
from `llms-full.txt`. Item 7 turned out to be six times larger than it was written down as, and
to be a different defect than the one described.

## Part 0 - The tree as found

`git status` showed 130 uncommitted paths and `HEAD` = `origin/main` = `eea0eb3`.
`_tools/seo-check.py` **PASS**: 102 rendered pages, 82 redirect stubs, 89 dispatches, 101 sitemap
URLs, 89 feed items, no notes.

So the tree already carried two unpushed layers: the 45 paths from the 02:27 pass and a blog run
that published two new dispatches, Nos 134 and 135, with their `/md/` renditions. Dispatch count
moved 87 to 89 and rendered pages 100 to 102. **Carried item 1 of the 02:27 report is still open
and now covers more.** Nothing from either pass is live.

Snapshot: none written. `HEAD` is the pre-change state for every tracked file, so `git diff` gives
an exact before-tree without adding a tarball to `_qa_tmp/`. One file, `llms-full.txt`, was copied
to the session scratch outside the repository before Part 2 rewrote 87 of its segments, so the
before and after could be diffed directly. Nothing was written into `_qa_tmp/`.

No blog-run collision during this pass. The two dispatches had already landed before it started.

## Part 1 - Fourteen more dispatches carry a short answer, and coverage is now contiguous

Carried item 3, and the same lever the 02:27 pass pulled twelve times. On the tree as found, 27 of
89 dispatches had a short answer. The method is the one that pass put on the record, followed
without variation: read the dispatch's full `/md/` rendition, draft a three-paragraph precis that
answers the headline question in the first sentence, states plainly what Shopify can and cannot do
natively, names the mechanism and stops. Every factual claim is one the article already makes.

**Written for 14, extending coverage contiguously backwards from Nº 108 to Nº 95.** Coverage is
now **41 of 89**, and the covered range Nº 95 to Nº 135 has **no gaps**.

| Dispatch | Nº | wordCount |
|---|---|---|
| `stop-fake-customer-accounts-and-spam-signups-on-shopify` | 108 | 2600 to 2800 |
| `fix-missing-hs-codes-on-shopify-before-customs-holds-your-orders` | 107 | 2800 to 3000 |
| `catch-pricing-errors-on-shopify-before-orders-flood-in` | 106 | 2700 to 2900 |
| `catch-shopify-orders-stuck-in-transit` | 105 | 2740 to 2900 |
| `automate-gift-card-delivery-and-reminders-on-shopify` | 104 | 2600 to 2800 |
| `automatically-restock-returns-on-shopify` | 103 | 2660 to 2900 |
| `handle-delivered-but-not-received-claims-on-shopify` | 102 | 2540 to 2700 |
| `automatically-follow-up-on-unpaid-draft-orders-on-shopify` | 101 | 2410 to 2600 |
| `sync-inventory-between-two-shopify-stores` | 100 | 2310 to 2500 |
| `automatically-capture-payments-on-shopify` | 99 | 2412 to 2600 |
| `let-customers-cancel-their-own-orders-on-shopify` | 98 | 2304 to 2500 |
| `automatically-clear-dead-stock-on-shopify` | 97 | 2173 to 2400 |
| `change-a-shopify-order-from-local-pickup-to-shipping` | 96 | 2362 to 2600 |
| `automatically-approve-wholesale-customers-on-shopify` | 95 | 2334 to 2500 |

Gates run on every draft before it was written to disk, as a script rather than by eye, because
the 02:27 report's gate list is a specification and worth executing:

| Gate | Result across all 42 paragraphs |
|---|---|
| paragraphs per block | 3, each 314 to 572 characters, inside the 190 to 700 house range |
| sentences of 55 characters or more appearing verbatim in the article | 0 |
| non-ASCII, em dashes, en dashes, smart quotes, HTML entities | 0 |
| inline HTML used | `<em>` and `<code>` only |

Written in all three renditions per page by one script, so the three cannot diverge by hand: the
page as `<div class="short-answer" id="short-answer">` holding an `<h2>The short answer</h2>`
placed immediately before the first substantive heading in `.article-body`, the `/md/` file as
`## The short answer` in the same position with `<em>` rendered as Markdown emphasis, and
`llms-full.txt` as a `## The short answer` block with emphasis stripped. `.short-answer` was added
to `speakable.cssSelector` between `.article-title` and `.faq`, and `BlogPosting.abstract` was
added carrying the first paragraph as plain text, both of which the 02:27 pass established and the
checker now requires.

Two corrections were made to the first two pages after inspecting the written output rather than
trusting the script: the opening `<div>` landed at eight spaces of indentation instead of four, and
one paragraph used `behaviour` where the site uses `behavior` 323 times to 0. Both fixed in all
renditions, and the script corrected before the remaining twelve ran.

**Dates moved on these 14**, by the 10-18 policy: a new section of original prose the reader has
not seen. `article:modified_time`, JSON-LD `dateModified`, `sitemap.xml` `lastmod`, the md
`- Updated:` line and the `llms-full.txt` `Updated:` field were carried to 2026-10-24 together, and
`wordCount` was raised in the JSON-LD, the ticker's two `N,N00 WORDS` spans and the md
`- Word count:` line, rounded to the nearest hundred. `feed.xml` carries only `pubDate` and needed
nothing.

48 of 89 dispatches still have no short answer. The next one is Nº 94.

## Part 2 - The READING callout in llms-full.txt had lost its links on 74 of 89 segments

Carried item 7, which the 02:27 report recorded as "llms-full.txt omits the READING callout for
three pages". The three pages are real. They are 6, and the omission is the smaller half of the
defect.

`llms-full.txt` is the rendition an answer engine is pointed at. Each dispatch's segment ends with
a `◆ READING` callout, which exists for exactly one reason: it is the block that names the two
companion dispatches and carries their URLs. Counted across all 89 segments, the file held **six
different renderings of it**:

| Rendering | Segments | What it costs |
|---|---|---|
| `> ◆ READING: ...` with every URL stripped to plain anchor text | 74 | the links |
| no callout at all | 6 | the links and the block |
| `◆ READING ...` with no blockquote marker | 4 | the block reads as body prose |
| `> **◆ READING** ...`, the md line verbatim | 3 | nothing, this is the correct form |
| the callout text present with the marker stripped entirely | 1 | the block reads as body prose |
| `> **&#9670; READING** ...`, an HTML entity in a plain-text file | 1 | mojibake for any reader that does not decode it |

**9 editorial URLs survived in the whole file, against 209 in the `/md/` renditions.** The one block
in `llms-full.txt` whose entire purpose is its links was the only block in the file without any.

The existing `reading_callout_divergence` check did not see this, and reading it explains why: it
compares the page's callout with the md's and says nothing about the third rendition. That is a
reasonable scope for a check written to catch a page-to-md disagreement, and it leaves the machine
rendition unguarded.

**Which form is canonical was not a judgment call.** The 3 correct segments are Nos 134, 135 and
one from 10-21, which is to say the newest generator output. Every other rendering is older. So
this is a back-catalogue migration to the generator's own current output, not a convention change.

**Fixed on all 87 non-canonical segments.** Each segment's callout was replaced with its `/md/`
READING line copied verbatim; where no callout existed, the md line was inserted before the
segment's closing inbox paragraph, or before its FAQ heading where the inbox paragraph was also
missing. The HTML entity was replaced with the character. Nothing was retyped: every line was read
from the md file that already held it.

| Measure | Before | After |
|---|---|---|
| segments carrying the md READING line verbatim | 3 of 89 | **89 of 89** |
| editorial URLs in llms-full.txt READING callouts | 9 | **209** |
| `&#9670;` entities in llms-full.txt | 1 | 0 |
| segments with no callout at all | 6 | 0 |

The 6 that had none: `catch-shopify-shipping-label-adjustments-before-they-eat-your-margin`,
`fix-shopify-committed-inventory-that-never-clears`,
`handle-shopify-returns-the-customer-never-sends-back`,
`handle-price-adjustment-requests-on-shopify`, `make-shopify-wholesale-customers-tax-exempt` and
the lead essay. The first four were also missing their closing inbox paragraph, so their segments
ended mid-article.

No dates moved for this part. A callout's link set is a pointer, not new prose, which is the
distinction the 10-18 policy draws and the 02:27 pass applied to the 33 pages it touched without
moving their dates. Only `llms-full.txt` changed.

## Part 3 - One invariant added

`_tools/seo-check.py` and `_tools/README.md` updated.

| Check | Fires when | Status |
|---|---|---|
| `reading_callout_llms_divergence` | a dispatch's `llms-full.txt` segment does not carry exactly one READING line equal to its `/md/` line, character for character | new |

Verified both directions, which is the part worth auditing. Run against the tree as found, with
only `llms-full.txt` swapped back to its pre-change copy and everything else current, the checker
reports:

```
seo-check: FAIL - 87 problem(s) in 1 category(ies)
  reading_callout_llms_divergence (87)
```

Exactly the 87 segments this pass changed, in exactly one category, and nothing else. On the
current tree it passes. No check was loosened, and this one is strictly additional: it guards a
rendition no check previously read.

## Part 4 - Audit after the changes

| Check | Result |
|---|---|
| `_tools/seo-check.py` | **PASS**, 102 rendered pages, 82 stubs, 89 dispatches, 101 sitemap URLs, 89 feed items |
| new checker against the pre-change `llms-full.txt` | fires on exactly 87 segments, 1 category |
| short answer on the page, in the md and in llms-full | **41 of 89** (was 27), contiguous Nº 95 to Nº 135, no gaps |
| short answer wrapped, speakable and carrying an abstract | 41 of 41 |
| `abstract` text present in the visible page | 41 of 41 |
| segments carrying the md READING line verbatim | **89 of 89** (was 3) |
| editorial URLs in llms-full READING callouts | **209** (was 9) |
| JSON-LD parses | 102 / 102 |
| `dateModified` vs `sitemap.xml` `lastmod` | agrees on all; the one difference is the lead essay, a documented `EXCEPTIONS` entry |
| md `- Updated:` vs page `dateModified` | agrees on all 89 |
| llms-full `Updated:` vs page `dateModified` | agrees on all 89 |
| tag balance, all 184 html files | 0 imbalances across div, p, section, article, details, span, h2, ul, li |
| em dashes, en dashes, mojibake across pages, md, llms-full, llms.txt, sitemap, feed | 0 |
| broken internal links / in-page anchors / cross-file anchors | 0 / 0 / 0 |
| duplicate element ids | 0 |
| total HTML weight | 11,177,334 to 11,519,433 bytes, **+3.06%** |

Render: not visually verified, for the same reason the 10-21 and 02:27 passes give. The in-app
browser cannot open `file://` and cannot reach a server started in either shell. Structural
verification was used instead and is recorded above. Every page change is an additional element of
a kind the page already contains in the same container: an `<h2>` and `<p>` elements inside
`.article-body`, wrapped in a `<div>` whose class the 02:27 pass already shipped on 27 pages with
no stylesheet rule and identical rendering. Part 2 touched no HTML at all.

Changed paths: **32**, all modifications apart from this report. 14 page HTML files, 14 `/md/`
renditions, `llms-full.txt`, `sitemap.xml`, `_tools/seo-check.py` and `_tools/README.md`.

## Part 5 - Needs a decision

1. **Commit and push.** The tree now holds three unpushed layers: the 45 paths from the 02:27 SEO
   pass, the blog run that published Nos 134 and 135, and the 32 from this pass. Nothing in any of
   them is live. The owner's `eea0eb3` closed the equivalent item from 10-21, so the loop works; it
   needs a hand again, and the backlog is larger than it was this morning.
2. **Organization `sameAs` still resolves nothing.** It lists `https://dugong.live`, which is
   already the node's own `url`. Still the one GEO gap no autonomous run can close.
   **Needs someone to supply LinkedIn, X, GitHub or Crunchbase URLs.**
3. **48 of 89 dispatches still have no short answer.** Down from 62 this morning and 74 on 10-21.
   Coverage is contiguous Nº 95 to Nº 135, so the next pass starts at Nº 94 with no bookkeeping.
   Fourteen a pass clears the rest in four runs.
4. **The blog run writes the short answer correctly now but the generator still needs checking
   against four invariants.** Nos 134 and 135 arrived with the container, the `speakable`
   selector, the `abstract` and a canonical READING callout, which is the first time that has
   happened. Whatever changed is right; it is worth making sure it was a generator change and not
   two lucky posts.
5. **The blog run still does not extend the READ NEXT archive.** Carried unchanged. 74 grids have
   now been fixed by hand across three passes. Whatever writes a new dispatch should prepend its
   card to every archive-shaped grid.
6. **Stagger the two routines, or make the collision loud.** Carried from 10-18, 10-19, 10-21 and
   this morning. No collision today either, still by luck. Adding `python3 _tools/seo-check.py` to
   the end of the blog run remains the cheap half.
7. **Median outbound editorial links per dispatch is still falling by month of publication.**
   Measured on links inside `.article-body`: 4 in June, 7 in July, 8 in August, 2 in September, 3
   in October. Inbound is healthy, median 54 pages linking to each dispatch across a range of 4 to
   84, so the newest posts are found; they just weave outward thinly. This is generator behaviour,
   not a backlog of pages, and it is the last large on-page lever left that a pass could move by
   hand. Doing it by hand would mean writing prose into 14 recent dispatches, so it is left for a
   decision rather than taken.
8. **Google Fonts is still a render-blocking third-party stylesheet on all 102 pages.** `preconnect`
   and `display=swap` are in place; making the stylesheet non-blocking risks a flash of unstyled
   text and still wants a supervised run with a render check.
9. **og:image is still the same banner on all 102 pages.** Unchanged since 10-12.
10. **241 operational markdown files are still served from the site root**: 88 `SEO-GEO-report-*`
    including this one, 70 `blog-run-*` and 83 `QA-report-*`. `robots.txt` disallows all three
    prefixes in every group, and because of `.nojekyll` that request is the only thing between them
    and a crawler. Still worth a decision rather than an autonomous commit, since this routine
    writes into that root.
11. **`_qa_tmp/` is now 145 MB of accumulated whole-site tarballs**, not the 108 MB the 10-19 and
    10-21 reports recorded. Today's blog run added `run-10-24` at 11 MB; neither SEO pass today
    added anything. Worth correcting the record on one point: `.gitignore` lists `_qa_tmp/`, so
    nothing in it can reach a commit or the live domain, and the exposure the earlier reports
    worried about is already closed. What is left is 145 MB of local disk that nothing reads,
    growing by roughly 11 to 15 MB per blog run. Deleting the directories older than the last two
    runs needs the owner, since `device_bash` cannot delete inside a connected folder without a
    permission prompt and no one is at the desk to answer one.
