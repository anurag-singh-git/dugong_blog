# SEO / GEO report - 2026-10-24

Scheduled autonomous run, fired 02:27 UTC for a 09:30 slot. Last SEO/GEO pass: 2026-10-21. This
pass read `SEO-GEO-report-2026-10-21.md` before auditing anything and worked its carried items in
order of expiry: open item 12 fails the checker today, so it went first.

## Part 0 - The tree as found

`git status` clean, `HEAD` = `origin/main` = `eea0eb3`, `_tools/seo-check.py` **PASS** (100 rendered
pages, 82 stubs, 87 dispatches, 99 sitemap URLs, 87 feed items), with one note: Nº 133 still had no
editorial inbound link, on the last day of its three-day grace.

**Carried item 1 of the 10-21 report is closed by the owner.** Commit `eea0eb3` landed all 133 paths
from that pass. The live site was fetched during this pass and serves them:
`how-to-bulk-edit-variant-metafields-on-shopify.html` shows its short answer, and
`article:modified_time` reads 2026-10-21. So for the first time since 10-12 the tree, `origin/main`
and the live domain all agreed when a pass started.

No blog run fired during this pass, so no collision to report. That ends three consecutive days of
them, though nothing was done to prevent a fourth. Carried item 5 stands.

Snapshot: none written. `HEAD` was the pre-change state because the tree was clean, so `git diff`
and `git archive HEAD` give an exact before-tree without adding a tarball to `_qa_tmp/`. The 10-19
and 10-21 passes both reported that directory as 108 MB of accumulated whole-site tarballs; this is
the cheap half of not letting it grow again.

## Part 1 - Nº 133 had no editorial inbound link, and the grace window expired today

Carried item 12. `dispatch_no_editorial_inbound` exempts a dispatch for three days after
publication and reports it as a note instead. Nº 133 published 2026-10-21, so today was the last
note and tomorrow was the failure.

**Fixed.** Two inbound editorial links, using the house pattern the 10-21 pass established: the
`&#9670; READING` callout extended with an `Also worth reading: <link>, <reason>.` clause, written
in three places each (the page, its `/md/` rendition, its `llms-full.txt` entry).

| Source page | Reason given |
|---|---|
| `how-to-bulk-edit-meta-descriptions-on-shopify` | on the other catalog field the CSV export will not carry |
| `how-to-add-alt-text-to-shopify-product-images-in-bulk` | on the same bulk-fill problem one level down, at the variant |

Both sources are catalog-bulk-edit dispatches, which is the topic Nº 133 sits in. Anchor text is
`the variant field the product CSV leaves out`, taken from the page's own dek rather than invented.
Dispatches with zero editorial inbound links are now **0 of 86**, with no page inside a grace
window.

## Part 2 - Three READ NEXT grids had stopped growing on 2026-10-14, and the new check could not see them

Carried item 8. The 10-21 pass skipped `catch-shopify-flow-workflows-that-fail-silently` (Nº 120),
`restrict-shopify-products-from-shipping-to-certain-states` (Nº 119) and
`stop-taking-shopify-orders-when-you-hit-your-daily-capacity` (Nº 121) on the grounds that their
grid head was not newest-first, so the insert point was ambiguous.

Measured properly, the head **is** newest-first. All three run Nº 127, 126, 125, 124, 123, 122 and
then stop, with a curated topical tail underneath. They are the same defect Part 1 of 10-21 fixed on
71 pages: an archive grid written at publication, extended to 2026-10-14, and never extended again.

Worse, `readnext_archive_stale` was structurally unable to report them. The check tested whether the
**first ten** card dates ran newest first and exempted any grid that failed. On all three the
seventh to tenth cards are the curated tail, which breaks the sort, so the whole grid read as
curated and the stale head went unexamined.

**Both fixed.**

| Page | Dispatch | Cards before | Cards after | Archive summary |
|---|---|---|---|---|
| `catch-shopify-flow-workflows-that-fail-silently` | Nº 120 | 16 | 22 | 10 to 16 more |
| `restrict-shopify-products-from-shipping-to-certain-states` | Nº 119 | 18 | 24 | 12 to 18 more |
| `stop-taking-shopify-orders-when-you-hit-your-daily-capacity` | Nº 121 | 15 | 21 | 9 to 15 more |

Six cards prepended newest first on each, six kept visible, the remainder moved into
`<details class="related-more">`, and the summary count corrected. Every card was re-rendered from
the same target's existing card in `how-to-automatically-clear-dead-stock-on-shopify.html`, which
already carried all six in this exact grid template, so no copy was written and nothing was retyped
from tool output.

What it bought the six newest dispatches, measured on the whole tree:

| Dispatch | READ NEXT grids before | after |
|---|---|---|
| `bulk-edit-variant-metafields` (Nº 133) | 73 | 76 |
| `stop-shipping-shopify-orders-with-payment-pending` | 73 | 76 |
| `catch-shopify-shipping-labels-you-never-used` | 73 | 76 |
| `stop-shopify-b2b-prices-dropping-when-you-run-a-sale` | 73 | 76 |
| `handle-return-to-sender-orders` | 74 | 77 |
| `stop-reordering-shopify-stock-you-already-have-on-order` | 73 | 76 |

The check now measures the grid's **leading run** of newest-first dates and treats ten or more cards
with a run of six or more as archive-shaped. Run against the `HEAD` tree it reports exactly these
three and nothing else. The topic-guide and author-page exemption is unchanged and still by kind,
not by shape.

## Part 3 - Twelve more dispatches now carry a short answer

Carried item 7, the largest open GEO lever and the one the 10-21 pass set aside as editorial. On the
tree as found, 13 of 87 dispatches had a short answer, all of them from 2026-09-21 or later. The
other 74 had none anywhere: no page section, no `/md/` section, no `llms-full.txt` block.

**Written for 12, extending coverage contiguously backwards from Nº 121 to Nº 109.** Coverage is
now **25 of 87**.

| Dispatch | Nº | Paragraphs | wordCount |
|---|---|---|---|
| `catch-shopify-flow-workflows-that-fail-silently` | 120 | 3 | 2700 to 2900 |
| `restrict-shopify-products-from-shipping-to-certain-states` | 119 | 3 | 2300 to 2500 |
| `fix-shopify-shipping-rates-that-ignore-product-dimensions` | 118 | 3 | 2450 to 2650 |
| `fix-duplicate-skus-on-shopify` | 117 | 3 | 2500 to 2700 |
| `track-product-expiry-dates-on-shopify` | 116 | 3 | 2400 to 2600 |
| `put-your-shopify-store-on-vacation-mode-without-losing-sales` | 115 | 3 | 2500 to 2700 |
| `handle-shopify-pickup-orders-customers-never-collect` | 114 | 3 | 2600 to 2800 |
| `fix-order-confirmation-emails-not-sending-on-shopify` | 113 | 3 | 2600 to 2800 |
| `stop-your-shopify-inventory-changing-by-itself` | 112 | 3 | 2800 to 3000 |
| `catch-shopify-orders-that-never-sync-to-shipstation` | 111 | 3 | 2500 to 2700 |
| `catch-shopify-orders-with-missing-personalization-before-they-ship-blank` | 110 | 3 | 2400 to 2600 |
| `stop-cancelled-orders-showing-as-unfulfilled-on-shopify` | 109 | 3 | 2700 to 2900 |

How they were written, because this is the part worth auditing. Each one is a distilled précis of
the article it sits on, drafted only after reading that article's full `/md/` rendition, using
`how-to-stop-taking-shopify-orders-when-you-hit-your-daily-capacity` as the voice and position
template: answer the headline question in the first sentence, state plainly what Shopify can and
cannot do natively, name the mechanism, stop. Every factual claim is one the article already makes.
No Shopify behaviour, app, API field, limit or date appears in a short answer that does not appear
in the body.

Checked mechanically before anything was written to disk:

| Gate | Result |
|---|---|
| paragraphs per block | 3, each 209 to 581 characters, inside the 190 to 700 house range |
| sentences of 55 characters or more appearing verbatim in the article | 0, so none of it is duplicated body copy |
| em dashes, en dashes, smart quotes, non-ASCII, HTML entities | 0 |
| inline HTML used | `<em>` and `<code>` only |

Written in all three renditions per page: the page as an `<h2>The short answer</h2>` section placed
immediately after the opening paragraphs and before the first substantive heading, the `/md/` file
as `## The short answer` in the same position with `<em>` rendered as Markdown emphasis, and
`llms-full.txt` as a `## The short answer` block with emphasis stripped, which is that file's
convention. `wordCount` was raised in the JSON-LD, in the ticker's `N,N00 WORDS` span and in the md
`- Word count:` line, rounded to the nearest hundred as the house does. Read time was left alone:
200 words is under a minute at the rate these pages use, and `post-read` is also written into every
card on 100 other pages.

**Dates moved on these 12.** The 10-18 policy is that `dateModified` moves when what the page says
changes materially, and this is the case that policy is for: a new section of original prose the
reader has not seen, not a pointer or a card or a paragraph the site already published elsewhere.
`article:modified_time`, JSON-LD `dateModified`, `sitemap.xml` `lastmod`, the md `- Updated:` line
and the `llms-full.txt` `Updated:` field were all carried to 2026-10-24 together, which is the drift
`_tools/seo-check.py` was written to catch. `feed.xml` carries only `pubDate` and needed nothing;
`lastBuildDate` stays 10-21 because no feed content changed. The other 33 pages this pass touched
kept their dates, for the reason the 10-21 report gives.

62 of 87 dispatches still have no short answer anywhere. That remains open item 7, and the method
above is now on the record and repeatable.

## Part 4 - The short answer was the one thing on the page no machine had been told about

The largest finding of the pass, and it applied to all 13 pages that already had a short answer as
well as the 12 written today.

A short answer exists to be lifted whole. On the tree as found it was a bare `<h2>` plus paragraphs
with no class and no id, sitting in `.article-body` alongside every other heading. Meanwhile:

| Signal | What it pointed at |
|---|---|
| `speakable.cssSelector` | `.article-title` and `.faq`, on all 100 pages |
| `BlogPosting.abstract` | absent, on all 100 pages |
| any class or id on the short answer block | none, on all 13 pages that had one |

So the site named the title and the FAQ as its speakable content and said nothing at all about the
one paragraph per article written specifically to be quoted back as the answer. There was no
selector that could have named it even if someone wanted to.

**Fixed on all 25 pages that carry a short answer:**

1. The block is wrapped in `<div class="short-answer" id="short-answer">`, one per page. No
   stylesheet rule was added, because a block container inside `.article-body` renders identically
   and the block holds no anchors, so `unstyled_link_container` does not apply.
2. `.short-answer` added to `speakable.cssSelector`, between `.article-title` and `.faq`.
3. `BlogPosting.abstract` added, carrying the short answer's first paragraph as plain text.

`abstract` is Schema.org's own property for a short summary of a `CreativeWork`, so this is the
field a crawler reading the structured data would look in. Verified per page: the JSON-LD parses,
`abstract` is non-empty and over 100 characters, and its text appears in the visible page, which is
the invariant that keeps it from drifting into a second place where the answer exists and the page
does not.

## Part 5 - `_tools/README.md` said the opposite of the truth about its own directory

Found while reading the tooling, not looked for. The README's first paragraph read: "The leading
underscore keeps Jekyll from publishing this directory, so nothing here is reachable on the live
domain."

That is false, and `robots.txt` says so in its own header comment: the repository contains a
`.nojekyll` file, so GitHub Pages serves it raw and never runs Jekyll. `_tools/` is fetchable on the
live domain like any other path, which is exactly why `robots.txt` disallows it in every user-agent
group.

Nothing is exposed by it today. The risk was forward: a future run reading that sentence would
believe anything written under an underscore directory was unreachable, which is the belief that put
108 MB of whole-site tarballs in a served commit in the first place. Corrected, with the reason
recorded.

## Part 6 - Invariants added and tightened

`_tools/seo-check.py` and `_tools/README.md` updated.

| Check | Fires when | Status |
|---|---|---|
| `readnext_archive_stale` | an archive-shaped grid is missing a dispatch newer than its own newest card. A grid is archive-shaped when it holds ten or more cards and its leading run of newest-first dates is at least six long | tightened |
| `short_answer_unwrapped` | a page has a short answer that is not inside a `.short-answer` container, or does not carry exactly one `id="short-answer"` | new |
| `short_answer_not_speakable` | the article's `speakable.cssSelector` does not name `.short-answer` | new |
| `short_answer_no_abstract` | the article carries no `abstract`, or its `abstract` does not appear in the visible page | new |

Run against the `HEAD` tree, the final checker reports exactly the defects this pass found and
nothing else:

```
readnext_archive_stale (3)
short_answer_no_abstract (13)
short_answer_not_speakable (13)
short_answer_unwrapped (26)
```

26 rather than 13 on the last one because the container and the id are reported separately.
`dispatch_no_editorial_inbound` does not appear because Nº 133 was inside its grace window on that
tree, which is the check working as designed.

No check was loosened. The `readnext_archive_stale` change replaces a fixed ten-card window with the
grid's actual leading run, which is strictly more sensitive: it fires on three grids that previously
escaped and on nothing that previously passed.

## Part 7 - Audit after the changes

| Check | Result |
|---|---|
| `_tools/seo-check.py` | **PASS**, 100 rendered pages, 82 stubs, 87 dispatches, 99 sitemap URLs, 87 feed items |
| final checker on the `HEAD` tree | fires on exactly the 55 defects above |
| dispatches with zero editorial inbound links | **0 of 86** (was 1, and no page in a grace window) |
| short answer on the page, in the md and in llms-full | **25 of 87** (was 13) |
| short answer wrapped, speakable and carrying an abstract | **25 of 25** (was 0 of 13) |
| `abstract` text present in the visible page | 25 of 25 |
| READ NEXT grids per dispatch | 36 to 82 across all 86, median 50.5 |
| archive-shaped grids missing a newer dispatch | **0** (was 3) |
| `dateModified` vs `sitemap.xml` `lastmod` | agrees on all 99 |
| JSON-LD parses | 100 / 100 |
| tag balance, all 182 html files | **0 imbalances**, and 0 pages whose balance changed against `HEAD` (the one apparent `details` imbalance in `index.html` is the string `<details>` inside a JavaScript comment, present in `HEAD`, unchanged) |
| em dashes, en dashes, mojibake in the 45 changed files | 0 (the one dash pair in `seo-check.py` is the checker's own detection literal, present in `HEAD`) |
| broken links / in-page anchors / cross-file anchors | 0 / 0 / 0 |
| duplicate element ids | 0 |
| total HTML weight | 11,132,623 to 11,177,334 bytes, **+0.40%** |

Render: not visually verified this pass, for the same reason as 10-21. The in-app browser cannot
open `file://` and cannot reach a server started in either shell. Structural verification was used
instead and is recorded above. Every change is an additional element of a kind the page already
contains in the same container: an `<h2>` and `<p>` elements inside `.article-body`, a `<div>`
wrapping them, an `<a>` inside a `.callout` span that already holds anchors, and `.card` elements
inside a grid that already held fifteen or more. The 10-14 render pass across eight widths and the
10-21 blog-run QA change both still hold.

Changed paths: **45**, all modifications, no new or deleted files apart from this report. 27 page
HTML files, 14 `/md/` renditions, `llms-full.txt`, `sitemap.xml`, `_tools/seo-check.py` and
`_tools/README.md`. 1,055 insertions, 233 deletions.

## Part 8 - Needs a decision

1. **Commit and push.** 46 paths: 45 modified and this report. This pass did not commit, following
   the standing practice of every pass since 10-12. Nothing in Parts 1 to 6 is live until it
   happens. The owner's `eea0eb3` closed the equivalent item from 10-21, so the loop does work; it
   just needs a hand.
2. **Organization `sameAs` still resolves nothing.** It lists `https://dugong.live`, which is
   already the node's own `url`. Unchanged and still the one GEO gap no autonomous run can close.
   **Needs someone to supply LinkedIn, X, GitHub or Crunchbase URLs.**
3. **62 of 87 dispatches still have no short answer.** Down from 74. Part 3 records the method and
   the gates it was checked against, so the remaining 62 are now a known quantity of work rather
   than an open question. Roughly a dozen a pass keeps it inside a single run.
4. **The blog run still writes the short answer to llms-full.txt and nowhere else**, and now also
   needs to write the container, the `speakable` selector and the `abstract`. Four new checks fail
   the day it does not. The generator is the place to fix it.
5. **The blog run still does not extend the READ NEXT archive.** Parts 1 and 2 of 10-21 and Part 2
   today have now fixed 74 grids by hand. Whatever writes a new dispatch should prepend its card to
   every archive-shaped grid.
6. **Stagger the two routines, or make the collision loud.** Carried from 10-18, 10-19 and 10-21.
   No collision today, which is luck rather than a change. Adding `python3 _tools/seo-check.py` to
   the end of the blog run is still the cheap half.
7. **llms-full.txt omits the READING callout for three pages**: `shipping-label-adjustments`,
   `committed-inventory-that-never-clears`, `wholesale-customers-tax-exempt`. The page and the md
   both have it. Unchanged, and still a generator fix rather than a hand patch.
8. **Google Fonts is still a render-blocking third-party stylesheet on all 100 pages.** `preconnect`
   to both font hosts and `display=swap` are already in place, so the remaining cost is the
   stylesheet request itself. Making it non-blocking risks a flash of unstyled text, so this still
   wants a supervised run with a render check, not an unattended one.
9. **og:image is still the same banner on all 100 pages.** Unchanged since 10-12.
10. **240 operational markdown files are still served from the site root**: 87 `SEO-GEO-report-*`
    including this one, 70 `blog-run-*` and 83 `QA-report-*`. `robots.txt` disallows all three prefixes in
    every group, and because of `.nojekyll` that request is the only thing standing between them and
    a crawler. Moving them into a subdirectory would be a one-line robots change and a large rename;
    worth a decision rather than an autonomous commit, since this routine writes into that root.
11. **Median outbound editorial links per dispatch is still falling by month of publication**: 5.5
    in June, 9.0 in July, 9.5 in August, 4 in September, 4 in October. Inbound is now healthy on
    every dispatch, but the newest posts still weave outward about as thinly as they did when 10-21
    measured it. That is a generator behaviour, not a backlog of pages.
