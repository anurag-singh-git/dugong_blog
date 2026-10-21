# SEO / GEO report - 2026-10-21

Scheduled autonomous run, fired 13:19 UTC for a 09:30 slot. Last SEO/GEO pass: 2026-10-19 (second
pass). Per carried item 5 of that report, this pass read `SEO-GEO-report-2026-10-19-2.md` before it
audited anything, which was the right call for a second reason this time: a blog run fired in the
middle of the pass. See Part 0.

## Part 0 - The tree as found, and the blog run that fired at 13:35

`git status` clean, `HEAD` = `origin/main` = `c93f708`, `_tools/seo-check.py` **PASS** (99 rendered
pages, 82 stubs, 86 dispatches, 98 sitemap URLs, 86 feed items).

**Carried items 2 and 11 of the 10-19 second pass are closed.** The owner's commit `c93f708` landed
the 65 staged deletions, so the 108 MB of whole-site tarballs under `_qa_tmp/` and `_to_delete/` and
the `__deltest.tmp` probe are out of the served commit. `git check-ignore` still attributes them to
`.gitignore` and `git add -A --dry-run` does not re-add them. The working tree still holds the files
on disk, which was the deliberate half of that fix.

At **13:35 UTC**, while this pass was measuring, a blog run published **Dispatch Nº 133**,
`how-to-bulk-edit-variant-metafields-on-shopify.html`, and shipped a QA legibility change that
raised the 12px micro-label floor from 560px to 1024px across every page. 112 paths. For about two
minutes the checker reported **FAIL**: Nº 133 was in no llms.txt list, absent from `sitemap.xml`,
and the catalog guide's count disagreed with its own ItemList. All three resolved on their own by
13:38 when the run finished writing, so this was a mid-write window rather than a defect. This pass
stopped writing, waited, and re-verified before continuing, the same way the 10-19 pass did.

That collision is now the third in three days of record, and this time the two runs were editing the
same READ NEXT grids. Nothing was lost in either direction, which is luck rather than design.

## Part 1 - The READ NEXT archive had stopped growing on 2026-10-14

Every dispatch carries a READ NEXT section: six visible cards plus a `<details class="related-more">`
archive. Measured on the tree as found, that archive is "every other dispatch, newest first", and it
had not been extended since **2026-10-14**.

What that cost, measured per dispatch:

| Dispatch | Published | READ NEXT grids listing it | Total inbound links |
|---|---|---|---|
| `how-to-bulk-edit-variant-metafields-on-shopify` | 10-21 | 2 | 11 |
| `how-to-stop-shipping-shopify-orders-with-payment-pending` | 10-19 | 2 | 11 |
| `how-to-catch-shopify-shipping-labels-you-never-used` | 10-18 | 2 | 11 |
| `how-to-stop-shopify-b2b-prices-dropping-when-you-run-a-sale` | 10-17 | 2 | 11 |
| `how-to-handle-return-to-sender-orders-on-shopify` | 10-16 | 3 | 12 |
| `how-to-stop-reordering-shopify-stock-you-already-have-on-order` | 10-15 | 2 | 11 |
| every other dispatch | - | **73 to 82** | **82 to 91** |

So six dispatches, a week of publishing, were sitting almost entirely outside the site's own link
graph. They were in their topic guide, on the author page and in the sitemap, so nothing was
unreachable, but they received about an eighth of the internal links every other dispatch receives.
This is invisible to every format check, which is why five passes went over the tree without seeing
it. It is not a content problem and not a markup problem; the grid is written once at publication and
no later run goes back to extend it.

**Fixed on 71 pages.** The six missing cards were prepended newest first, six cards kept visible, the
remainder moved into `<details>`, and the summary count corrected (`73 more dispatches` to `79 more
dispatches`, and so on per page). The card markup was re-rendered from each target's own card on its
topic guide into the grid template, so no copy was invented and nothing was retyped from tool output.

Deliberately not touched:

| Left alone | Count | Why |
|---|---|---|
| topic guides, author pages, `index.html`, `404.html` | 13 | curated topical lists, not the chronological archive |
| recent dispatches' grids holding under 10 cards | 13 | curated topical trios, which is the convention for dispatches published since 10-11 |
| `catch-shopify-flow-workflows-that-fail-silently`, `restrict-shopify-products-from-shipping-to-certain-states`, `stop-taking-shopify-orders-when-you-hit-your-daily-capacity` | 3 | their grid head is not newest-first, so the insert point is ambiguous. Open item 8 |

After: every dispatch appears in 73 to 82 grids. The only link target under five is the lead essay,
which is an essay rather than a dispatch and is excluded from the archive by design.

The cost is page weight. Total HTML went from 10,645,004 to 11,110,049 bytes, **+4.4%**; the mean
rendered page from 58,812 to 61,044. Almost all of it is inside the collapsed `<details>`, which is
where the existing 73 cards already lived.

## Part 2 - Nine dispatches had no editorial inbound link at all

Separate from the cards, and the better signal of the two: an anchor inside another page's
`<article>`, in running prose. Counted across all rendered pages, resolving redirect stubs:

| Measured | Result |
|---|---|
| editorial links inside `<article>` across the site | 780 |
| dispatches with zero editorial inbound links | **9** |
| median editorial inbound per dispatch | 3 |
| best | 35 (`prevent-overselling-on-shopify-across-channels`) |
| editorial links pointing at a redirect stub rather than the canonical URL | **0** |

Also worth recording, because it points at the generator rather than at any one page: median
*outbound* editorial links per dispatch by month of publication runs 5.5 (June), 9.0 (July), 9.5
(August), 4 (September), 4 (October). The corpus stopped weaving new dispatches in, in both
directions, around mid-September.

**Fixed for 8 of the 9.** Each got two inbound editorial links from topically adjacent pages, using
the house's own existing pattern: the `&#9670; READING` callout extended with an `Also worth
reading: <link>, <reason>.` clause, which is exactly how
`how-to-automatically-clear-dead-stock-on-shopify.html` already carries its third companion piece.
16 source pages, each updated in three places (the page, its `/md/` rendition, and its
`llms-full.txt` entry), 12 of which had an llms-full READING line to extend; the other 3 are open
item 6.

| Dispatch that had none | Now linked from |
|---|---|
| `catch-shopify-orders-where-half-the-order-never-ships` | `never-sync-to-shipstation`, `stop-cancelled-orders-showing-as-unfulfilled` |
| `catch-shopify-shipping-labels-you-never-used` | `shipping-label-adjustments`, `return-to-sender-orders` |
| `handle-price-adjustment-requests` | `discount-codes-applying-to-sale-items`, `catch-pricing-errors` |
| `handle-shopify-returns-the-customer-never-sends-back` | `automatically-restock-returns`, `delivered-but-not-received-claims` |
| `stop-reordering-shopify-stock-you-already-have-on-order` | `sync-supplier-inventory-feeds`, `committed-inventory-that-never-clears` |
| `stop-shipping-shopify-orders-with-payment-pending` | `automatically-capture-payments`, `follow-up-on-unpaid-draft-orders` |
| `stop-shopify-b2b-prices-dropping-when-you-run-a-sale` | `make-shopify-wholesale-customers-tax-exempt`, `set-up-tiered-volume-discounts` |
| `stop-taking-shopify-orders-when-you-hit-your-daily-capacity` | `vacation-mode-without-losing-sales`, `set-a-minimum-order-amount` |

Dispatch Nº 133 was left alone on purpose: it was published four hours ago, the pages that will point
at it are usually written after it, and the new checker reports it as a note rather than a failure
for three days. Anchor text follows each source page's own capitalisation.

## Part 3 - The short answer existed only in llms-full.txt

The largest GEO finding of the pass, and it was hiding in plain sight.

`llms-full.txt` carries a `## The short answer` block for the 13 newest dispatches: one paragraph,
written to be lifted whole as the answer to the question in the headline. Exactly the paragraph a
featured snippet or an AI Overview wants.

**On the tree as found, 11 of the 12 existed only there.** Not on the page. Not in the `/md/`
rendition that `<link rel="alternate" type="text/markdown">` points answer engines at. Only
`how-to-stop-taking-shopify-orders-when-you-hit-your-daily-capacity.html` showed it to a reader, as
an `<h2>The short answer</h2>` section sitting after the opening paragraphs and before the first
substantive heading.

So the site's single most extractable paragraph per article was visible only to a crawler that
fetches a 1.5 MB text file, and invisible to Google, to every crawler that reads HTML, and to the
Markdown alternate the site itself advertises for this purpose.

**Propagated to the other 12** (the 11, plus Nº 133, which arrived mid-pass with the same gap), using
the one page that already had it as the template: same `<h2>`, same position, split into paragraphs
of 190 to 700 characters to match the surrounding body. No copy was written for this; the text is the
paragraph the site already publishes. `wordCount` in each JSON-LD and `- Word count:` in each md were
raised by the words added.

| Page | paragraphs | wordCount |
|---|---|---|
| `stop-shipping-shopify-orders-with-payment-pending` | 3 | 2849 to 3001 |
| `catch-shopify-shipping-labels-you-never-used` | 2 | 3118 to 3301 |
| `stop-shopify-b2b-prices-dropping-when-you-run-a-sale` | 4 | 2780 to 3000 |
| `handle-return-to-sender-orders` | 3 | 2681 to 2852 |
| `stop-reordering-shopify-stock-you-already-have-on-order` | 1 | 2341 to 2462 |
| `catch-shopify-orders-where-half-the-order-never-ships` | 1 | 2367 to 2468 |
| `catch-shopify-shipping-label-adjustments` | 4 | 2277 to 2584 |
| `fix-shopify-committed-inventory-that-never-clears` | 2 | 2166 to 2351 |
| `handle-shopify-returns-the-customer-never-sends-back` | 2 | 2075 to 2250 |
| `handle-price-adjustment-requests` | 2 | 1820 to 1963 |
| `make-shopify-wholesale-customers-tax-exempt` | 1 | 1950 to 2037 |
| `bulk-edit-variant-metafields` (Nº 133) | 5 | 2687 to 2872 |

The other 74 dispatches have no short answer anywhere. That is open item 7 and it is a writing job,
not an autonomous one.

## Part 4 - Three md renditions disagreed with the page they render

Found by the new parity check, each in exactly one file:

| File | Defect | Fix |
|---|---|---|
| `md/how-to-catch-shopify-shipping-labels-you-never-used.md` | the READING block was wrapped across six lines indented 8 spaces, so Markdown renders it as a code fence and neither link parses | collapsed to one line |
| `md/how-to-bulk-edit-variant-metafields-on-shopify.md` | the companion-pieces sentence was present with no `> **&#9670; READING**` marker, so it reads as a stray paragraph | marker added |
| `md/how-to-stop-shipping-shopify-orders-with-payment-pending.md` | `&#9670;` written into a Markdown file, where HTML entities do not render and the reader sees the entity | replaced with the character |

That was the only HTML entity in all 87 md files, and the only indented-block and only
missing-marker case. `llms-full.txt` separately omits the READING callout for three pages; open item
6.

## Part 5 - Four new invariants, validated against this morning's tree

`_tools/seo-check.py` and `_tools/README.md` updated.

| New check | Fires when |
|---|---|
| `readnext_archive_stale` | an archive-shaped READ NEXT grid is missing a dispatch newer than its own newest card |
| `dispatch_no_editorial_inbound` | a dispatch has no anchor pointing at it from inside any other page's `<article>`. Exempt, and reported as a note, for three days after publication |
| `reading_callout_divergence` / `reading_callout_missing_in_md` | the READING callout's link set on the page and in the md disagree |
| `short_answer_not_on_page` / `short_answer_not_in_md` | llms-full.txt calls something the short answer and the page or the md does not say it |

**Run against the pre-change snapshot the extended checker reports exactly the defects this pass
found, and nothing else:**

```
dispatch_no_editorial_inbound (5)
reading_callout_divergence (1)
reading_callout_missing_in_md (1)
readnext_archive_stale (71)
short_answer_not_in_md (11)
short_answer_not_on_page (11)
```

Five rather than nine on `dispatch_no_editorial_inbound` because four of the nine were inside the
three-day grace window on that snapshot, which is the check working. The snapshot also reports 297
`broken_link` entries; those are an artifact of the snapshot tarball holding only `*.html`, `*.txt`,
`*.xml` and `md/`, so every `favicon.svg` and `og-image.png` reference looks broken inside it.

No check was loosened. The topic-guide exemption on `readnext_archive_stale` is by **kind** - a page
carrying a `CollectionPage` or `ProfilePage` node - and not by relaxing the shape test, because a
topic guide genuinely should not list every dispatch.

## Part 6 - robots.txt

Carried item 3 of the 10-19 second pass. 40 `Disallow: /__deltest.tmp` lines removed, one per
user-agent group, because that file is gone from the repository and from disk. The `_qa_tmp/` and
`_to_delete/` rules were kept as belt and braces against a future run committing them again, with a
comment recording that they are no longer load-bearing. Also removed the one em dash in the file,
which the house style bans and the checker only looks for in HTML.

## Part 7 - Audit after the changes

| Check | Result |
|---|---|
| `_tools/seo-check.py` | **PASS**, 100 rendered pages, 82 stubs, 87 dispatches, 99 sitemap URLs, 87 feed items |
| extended checker on the pre-change snapshot | fires on exactly the 100 defects above |
| dispatches appearing in fewer than 5 READ NEXT grids | **0** (was 6) |
| READ NEXT grids per dispatch | **73 to 82** across all 87 (was 2 to 82) |
| median READ NEXT inbound | **50** (was 47) |
| dispatches with zero editorial inbound links | **1**, published today (was 9) |
| short answer on the page and in the md where llms-full.txt has one | **13 / 13** (was 1 / 12) |
| READING callout parity, page vs md | **87 / 87** (was 84 / 87) |
| HTML entities in md files | **0** (was 1) |
| editorial links pointing at a redirect stub | 0 |
| `wordCount` vs words inside `<article>` | median deviation **5.5%**, unchanged. One page over 15% and it is `index.html`, whose count is a page-level claim rather than an article count, pre-existing |
| tag balance, all 182 html files, before and after | **0 imbalances either side**, and 0 pages whose balance changed |
| JSON-LD parses | 100 / 100 |
| broken links / in-page anchors / cross-file anchors | 0 / 0 / 0 |
| orphan pages | 0 |
| total HTML weight | 10,645,004 to 11,110,049 bytes, +4.4% |

Render: not visually verified this pass. The in-app browser cannot open `file://` and cannot reach a
server started in either shell, so the 10-19 method was unavailable. Structural verification was
used instead and is recorded above: every change is an additional element of a kind the page already
contains in the same container (a `<p>` and an `<h2>` inside `.article-body`, an `<a>` inside a
`.callout` span that already holds anchors, a `.card` inside a grid that already held 73), all 182
files parse tag-balanced, and the checker's `unstyled_link_container` and `duplicate_id` checks pass.
The 10-14 render pass across eight widths and today's blog-run QA change both still hold.

Live site: fetched during this pass, which the 10-19 second pass could not do.
`how-to-stop-shipping-shopify-orders-with-payment-pending.html` is live and serves the 10-19 state:
no short answer, no archive count in READ NEXT, `dateModified` 2026-10-19. So the 10-19 work is
being served and **none of today's is**.

Dates: `dateModified` was not moved anywhere. The 10-18 policy is that dates move when what the page
says changes materially; a companion-reading pointer, a card in an archive and a paragraph the site
already publishes elsewhere are not that. Carrying 100 pages to today's date would also be a bulk
freshness signal over changes a reader would barely notice. Open item 10 if the owner disagrees.

Snapshots: `_qa_tmp/seo-2026-10-21-before.tar.gz` (pre-everything),
`_qa_tmp/seo-2026-10-21-before-after-blogrun.tar.gz` (after the blog run, before Parts 1, 2 and 4)
and `_qa_tmp/seo-2026-10-21-after.tar.gz`. All three are gitignored.

## Part 8 - Needs a decision

1. **Commit and push.** 133 paths: 129 modified, 4 untracked (Nº 133, its md,
   `blog-run-2026-10-21.md`, and this report). This pass did not commit, for the same reason every pass since 10-12
   has not. Nothing is live until it happens, and Part 7 confirms by fetch that the live site is
   still on 10-19.
2. **Organization `sameAs` still resolves nothing.** It lists `https://dugong.live`, already the
   node's own `url`. This pass searched the web for Dugong's real profiles and found nothing that is
   this company, so this is confirmed as the one remaining GEO gap no autonomous run can close.
   **Needs someone to supply LinkedIn, X, GitHub or Crunchbase URLs.**
3. **The blog run writes the short answer to llms-full.txt and nowhere else.** Part 3 fixed the 13
   that exist; the generator is what keeps producing the gap, and the new checker now fails the day
   it recurs rather than catching it five weeks later.
4. **The blog run does not extend the READ NEXT archive.** Part 1 fixed 71 pages by hand. Whatever
   writes a new dispatch should prepend its card to every archive-shaped grid, or the gap reopens
   tomorrow. The new checker fails on it now.
5. **Stagger the two routines, or make the collision loud.** Carried from 10-18 and 10-19. Today the
   blog run fired at 13:35 into a tree this pass was measuring, and the two were editing the same
   grids. Adding `python3 _tools/seo-check.py` to the end of the blog run is still the cheap half.
6. **llms-full.txt omits the READING callout for three pages**: `shipping-label-adjustments`,
   `committed-inventory-that-never-clears`, `wholesale-customers-tax-exempt`. The page and the md both
   have it. Not fixed, because llms-full.txt is generated and patching it by hand would be undone;
   the generator is the place.
7. **74 of 87 dispatches have no short answer anywhere.** The 13 that do are the newest. Writing 74
   is an editorial job and should not be done unattended, but it is now the single largest remaining
   GEO lever: one extractable paragraph per article, in the position answer engines read first.
8. **Three READ NEXT grids have a head that is not newest-first** and were skipped in Part 1. Worth
   one look to see whether they are deliberately curated or drifted.
9. **Google Fonts is still a render-blocking third-party stylesheet on all 100 pages.** Unchanged,
   and still worth a supervised run.
10. **og:image is still the same banner on all 100 pages.** Unchanged since 10-12.
11. **238 operational markdown files are still served from the site root**: 85 `SEO-GEO-report-*`, 70
    `blog-run-*`, 82 `QA-report-*`, plus this one. Carried unchanged from 10-19. robots.txt disallows
    all three prefixes in every group; nothing stops a crawler that ignores it.
12. **Nº 133 has no editorial inbound link.** Expected on day one, and the checker will start failing
    on it on 10-24 if nothing points at it by then.
