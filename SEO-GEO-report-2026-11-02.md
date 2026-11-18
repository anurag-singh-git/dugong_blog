# SEO / GEO report - 2026-11-02

Scheduled autonomous run, fired 19:23 UTC for a 10:30 slot. First pass on the repository since
2026-10-31. `SEO-GEO-report-2026-10-31.md` and `_tools/README.md` were read in full first.

`seo-check.py` passed on the tree as found, so there was no backlog of known defects to work. This
pass went looking for one instead, and found a large one that no check had been reading: **not a
single section heading in any article carried an `id`**. 702 headings across 91 dispatches, and the
smallest thing anyone could link to on a 2,500-word page was the page. That is now fixed on all 102
pages that have section headings, with a shared slug function and an invariant behind it.

## Part 0 - The tree as found

`HEAD` = `1059055`, dated 2026-10-30, unchanged since the 10-31 report. **150 paths were already
uncommitted on arrival**: the 44 from the 10-31 pass and the 103 from the Nº 137 publishing run,
plus three more. So the 10-31 work is still not live, including dispatch Nº 137, which has now been
on disk and off the site for two days. Decision item 1 below is the same decision item 1 as last
time and it has aged.

`_tools/seo-check.py` **PASS** on the tree as found: 104 rendered pages, 82 redirect stubs, 91
dispatches, 103 sitemap URLs, 91 feed items. No dispatch published 11-01 or 11-02 and no run of any
kind in any of the three series since 10-31.

## Part 1 - Nothing in any article could be cited by section

The site is careful about addressability in two places and had never been careful about it in the
third. Each FAQ answer sits in a `.faq-item` with `#faq-1` through `#faq-N`, and the question index
links all 463 questions to those anchors. The paragraph written to be quoted as the answer sits at
`#short-answer`. Both of those were built deliberately, and both work.

The body of every article was not. On the tree as found, a dispatch carried exactly nine ids:
`#main`, `#playbook`, `#short-answer`, `#faq-heading` and `#faq-1` to `#faq-5`. Its six or seven
section headings, which is where the argument actually lives, had none:

```
<h2>Why pasting tracking by hand is a tax on every order</h2>
<h2>What Shopify actually does, and where it stops</h2>
<h2>Why the usual fixes don't hold</h2>
```

**702 headings, 91 dispatches, zero ids.** Why that matters, in the order the consequences bite:

1. **An answer engine citing this site cannot cite a section.** It can name the page. The whole
   point of the short-answer work the 10-24, 10-25, 10-27 and 10-31 passes spent four sessions on
   is that a machine should be able to lift the right passage and say where it came from. One
   passage per page was addressable. The other seven were not.
2. **Google's jump links and passage ranking have nothing to anchor to.** The "jump to" links that
   appear under a result are built from in-page anchors. A page with no section anchors forfeits
   them.
3. **It capped the one lever carried item 8 keeps measuring.** There are **829 internal links
   inside article bodies and not one of them carries a fragment** - not a single one, across 91
   dispatches. That is not editorial restraint, it is the absence of a target. Every editorial
   cross-link this site has ever written drops the reader at the top of another 2,500-word article
   to find the relevant part themselves. Raising outbound link *counts*, which is what item 8 asks
   about, was never going to be the whole fix while every link that already exists lands in the
   wrong place.
4. **The HTML and the md renditions disagreed.** `llms.txt` points answer engines at
   `/md/<slug>.md`, and a Markdown renderer generates a heading anchor for every `## ` it sees. So
   the md rendition of every dispatch was addressable by section and the HTML was not. The three
   renditions have been held identical on prose, word counts and the READING callout for a week;
   they were not identical on this.

The convention needed no inventing. `shopify-automation-questions.html` has used `h-` plus the
heading's slug since it was written, on all eight of its section headings. It was simply never
applied anywhere else.

**Written on all 102 pages that have section headings**: 702 article section headings on the 91
dispatches, plus 18 on the eight topic guides and two author archives, where the headings sit
outside an `<article>` and carry `class="section-eyebrow"`. With the question index's 8 already in
place, **728 of 728 section headings are now addressable**, every id unique on its page, no
collision with any pre-existing id, and no duplicate id anywhere on the site.

```
<h2 id="h-what-shopify-actually-does-and-where-it-stops">What Shopify actually does, and where it stops</h2>
<h2 id="h-why-the-usual-fixes-dont-hold">Why the usual fixes don't hold</h2>
```

**What the reader sees: nothing.** No prose changed, no class was introduced, no element was added
or moved. This is one attribute per heading. By the 10-18 policy and the precedent the 10-31 pass
set when it corrected 39 renditions without moving a date, **no date moved** and `sitemap.xml`,
`feed.xml`, the md renditions and `llms-full.txt` needed no edit. The sitemap and feed diffs in the
working tree are the 10-31 pass's and the publishing run's; this pass did not touch either file.

### The first version of the slug was wrong, and the reason is worth keeping

The obvious slug is the heading's words, lowercased and hyphenated. Applied mechanically it
produced these, and a dry run is where they were caught rather than a commit:

```
priya-singh.html                   #h-90-dispatches-by-priya-singh
shopify-inventory-automation.html  #h-18-dispatches-in-this-guide
shopify-returns-and-refunds-...    #h-6-dispatches-in-this-guide
```

Every one of those numbers is a rendered count, and this repository's own history is those counts
moving. The 10-24 pass added a whole invariant because a guide's masthead said 17 against 18 listed;
the 10-31 pass found the homepage hero an issue and a week behind. An anchor is a promise that a URL
keeps working. **An anchor with a live count in it is a dead link waiting for the next dispatch**,
and the dispatch after Nº 137 would have broken ten of them.

The house convention had already solved this and I had not read it closely enough: the question
index's headings read `&#9670; SHOPIFY INVENTORY AUTOMATION &middot; 93 QUESTIONS` and its id is
`#h-shopify-inventory-automation`. The ornament and the count are dropped. So `heading_slug` now
drops both shapes of rendered count, leading and trailing, and leading list ordinals as well, so a
numbered section is addressed by what it says rather than by where it currently sits:

| Heading | id |
|---|---|
| `&#9670; SHOPIFY INVENTORY AUTOMATION &middot; 93 QUESTIONS` | `h-shopify-inventory-automation` (matches the 8 already on disk) |
| `&#9670; 18 DISPATCHES IN THIS GUIDE` | `h-dispatches-in-this-guide` |
| `&#9670; 90 DISPATCHES BY PRIYA SINGH` | `h-dispatches-by-priya-singh` |
| `1. VIP detection that actually means something` | `h-vip-detection-that-actually-means-something` |
| `The 14% / 0.8% gap` | `h-the-14-0-8-gap` |
| `The $27 billion that never gets spent` | `h-the-27-billion-that-never-gets-spent` |

A digit that is part of what the heading *means* is kept, which is the distinction that matters: 3
anchors retain one and all 3 are meaningful. 14 ids were corrected from the first form to the
second inside this pass, before anything was final.

**One slug function, in one file.** `heading_slug` lives in `_tools/seo-check.py` and the writer
imports it from there rather than carrying its own copy. The 10-31 report's Part 2 is the argument
for this: two scripts wrote the short-answer block two ways across three passes, and the
disagreement survived because nothing compared them. The writer and the checker here cannot
disagree, because there is only one of them. The writer is also idempotent, verified by running it
twice: the second run reports no change.

### Documented where machines will read it

`llms.txt` tells answer engines how to find the md renditions. It now also tells them the anchor
convention, in the same register, so a model that wants to cite a section knows it can and knows how
the id is formed without having to fetch a page and infer it. The FAQ and short-answer anchors are
named there too, which had never been written down anywhere a crawler looks.

## Part 2 - The invariant, and the verification

| Check | Fires when | Status |
|---|---|---|
| `heading_without_id` | a section heading carries no `id` | new |
| `heading_id_not_slug` | a section heading's `id` is not the slug of its own words, counts and ordinals dropped | new |

Coverage is the `<article>` on a dispatch and the whole page on a topic guide or author archive,
where the headings sit outside one. `NON_SECTION_H2` lists the five h2 classes that are not section
headings and says why in a comment: `faq-q` is addressed by its `.faq-item` wrapper, and
`cta-title`, `featured-title`, `signup-title` and `author-name` are page furniture rather than
places in an argument. `404.html` is exempt for the same reason it is exempt from the orphan and
sitemap checks.

Verified fail-loud in both directions, which the README is right to insist on. Four defects planted
in a scratch copy outside the repository:

```
seo-check: FAIL - 4 problem(s) in 2 category(ies)

  heading_id_not_slug (2):
    - how-to-automate-returns-and-exchanges-on-shopify.html: 'The short answer'
      carries #h-section-3, want #h-the-short-answer
    - shopify-inventory-automation.html: '&#9670; 18 DISPATCHES IN THIS GUIDE'
      carries #h-18-dispatches-in-this-guide, want #h-dispatches-in-this-guide

  heading_without_id (2):
    - how-to-automatically-add-tracking-numbers-to-shopify-orders.html:
      'What the automation actually has to do'
    - shopify-inventory-automation.html: '&#9670; OTHER TOPIC GUIDES'
```

All four caught, each naming the page, the heading and the id it wanted, exit code 1, and silent on
the real tree. The second of those is the count regression specifically: putting a count back into
an anchor now fails. No existing check was loosened and no exception was added. The change is
strictly additional.

## Part 3 - Audit after the changes

| Check | Result |
|---|---|
| `_tools/seo-check.py` | **PASS**, 104 rendered pages, 82 stubs, 91 dispatches, 103 sitemap URLs, 91 feed items |
| section headings addressable | **728 of 728** (was 8), across 102 pages |
| section headings without an id | **0** (was 720) |
| ids written by this pass | 720: 702 article, 18 guides and author archives |
| ids carrying a live count | **0** (14 corrected inside the pass) |
| anchors retaining a meaningful digit | 3, all three correct |
| duplicate element ids, any page | 0 |
| writer idempotent | verified, second run reports no change |
| writer and checker share one slug function | yes, imported, not copied |
| JSON-LD parses | every block in all 104 html files |
| h2 count per page before and after | identical on all 102 |
| prose changed | none |
| dates moved | none, and none were due |
| `sitemap.xml` / `feed.xml` touched by this pass | no |
| em dashes, en dashes, mojibake | 0 across all 104 pages |
| broken internal links / in-page anchors / cross-file anchors | 0 / 0 / 0 |
| total HTML weight | 11,943,406 to 11,974,741 bytes, **+0.26%** |

Render: not visually verified, for the reason the 10-21 through 10-31 passes all give. The in-app
browser cannot open `file://` and cannot reach a server started in either shell. Structural
verification was used instead and is recorded above. The argument that it is sufficient here is
stronger than usual: the change is one attribute on an existing element, adds no class, no rule and
no node, and `id` has no rendered effect. The h2 count is identical on every page and the JSON-LD in
all 104 files still parses.

Changed paths: **158** in the working tree, of which **106 are this pass**: 102 page HTML files,
`llms.txt`, `_tools/seo-check.py`, `_tools/README.md` and this report. The other 52 are the 10-31
pass's and the Nº 137 publishing run's, left exactly as they were.

## Part 4 - Needs a decision

1. **Commit and push. This is now two passes deep and the oldest item here.** 158 uncommitted
   paths: 106 from today, 52 from 10-31 and the Nº 137 run. **Dispatch Nº 137 has been written for
   two days and is not on the site**, along with the short-answer work for all 91 dispatches and
   every anchor from today. Nothing since `1059055` on 10-30 is live.
2. **Carried item 8 can be reframed, and it is now cheap.** The measurement has not changed: median
   distinct dispatches linked from inside `.article-body` is 4 in June, 7 in July, 8 in August, 2 in
   September, 3 in October. But the finding above changes what to do about it. All 829 existing
   internal links land at the top of their target page, and now, for the first time, there is
   something finer to point at. Pointing an existing link at the section that answers it is a
   mechanical edit with no new prose, which is a much smaller ask than the "write prose into 15
   dispatches" this item has been declined for twice. Worth a decision on that narrower version.
3. **Make the publishing run's state legible.** Carried unchanged from 10-31, where it has evidence
   behind it: the Nº 137 run went six minutes mid-flight writing nothing and was indistinguishable
   from a dead run, and it writes `index.html`'s question count minutes before the index that count
   describes. A stub `blog-run-<date>.md` at the start of a run, or a lock file, closes both.
4. **Organization `sameAs` still resolves nothing.** It lists `https://dugong.live`, which is the
   node's own `url`. Still the one GEO gap no autonomous run can close.
   **Needs someone to supply LinkedIn, X, GitHub or Crunchbase URLs.**
5. **The lead essay still has no FAQPage.** Only one of the 91 without one. It now has a short
   answer, an abstract, a speakable selector and section anchors, so it is not invisible, but
   writing questions for a signed essay is an editorial call.
6. **Nº 137 is filed in returns and refunds; its own cross-links point at shipping.** Unchanged
   from 10-31. A one-guide edit plus four counts.
7. **Google Fonts is still a render-blocking third-party stylesheet on all 104 pages.** `preconnect`
   and `display=swap` are in place; making it non-blocking risks a flash of unstyled text and wants
   a supervised run with a render check.
8. **og:image is still the same banner on all 104 pages.** Unchanged since 10-12.
9. **The ticker's two separators are still written two ways.** Declined on 10-25 and again on 10-31
   as cosmetic, since an entity and its character parse to the same text node. Standing offer.
10. **250 operational markdown files are still served from the site root**, now including this one:
    91 `SEO-GEO-report-*`, 73 `blog-run-*` and 86 `QA-report-*`. `robots.txt` disallows all three
    prefixes in every group, and because of `.nojekyll` that request is the only thing between them
    and a crawler.
11. **`_qa_tmp/` is 169 MB** and `_to_delete/` holds 14 zero-byte probe files back to 2026-09-17.
    `.gitignore` covers `_qa_tmp/`, so nothing in it can reach a commit or the live domain.
    Deleting needs you: `device_bash` cannot delete inside a connected folder without a permission
    prompt and no one is at the desk to answer one.
12. **QA's newsletter finding is still open and is still the most serious thing on this list.** The
    10-25 QA report records that the signup form in `index.html` has no `action`, no input `name`
    and an `onsubmit` that calls `preventDefault()`, tells the reader `subscribed`, and sends the
    address nowhere, beside a `4,200 readers` claim nothing supports. **No QA pass has run in eight
    days**, so it has not been repeated by its own series. Repeating it here so it is not lost
    between two report series.
