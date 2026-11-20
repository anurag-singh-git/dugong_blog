# SEO / GEO report - 2026-11-19

Scheduled autonomous run, fired 10:36 UTC. `SEO-GEO-report-2026-11-18.md` and `_tools/README.md`
were read in full first, and the first action of the pass was the habit the 11-16 pass installed and
the 11-18 pass said had paid for itself twice: `grep` every check name the README claims straight
out of `seo-check.py`. **All eleven were there.** The same grep was run again after this pass edited
both files, and all fifteen are there.

**Item 1 is closed.** `HEAD` is `7bb14c0`, committed 2026-11-18 at 19:51 and **equal to
`origin/main`**. The nineteen-day, six-pass backlog that led every one of these reports since 10-31
is live: dispatches Nº 137 through Nº 143 and every structural change from 10-31 to 11-18. Nothing
in the working tree now predates today.

`seo-check.py` passed on the tree as found, so this pass went looking for something no check reads.
It found it in the gap between what the site has made addressable and what the renditions a model is
told to read actually carry. That is Part 1 and it is the spine of the pass.

## Part 0 - The tree as found

On arrival: 87 uncommitted paths, all dated today, `seo-check.py` **PASS**, 111 rendered pages, 82
redirect stubs, 98 dispatches, 110 sitemap URLs, 98 feed items. Dispatch Nº 144, "How to catch the
Shopify products in the wrong shipping profile", had shipped at 10:10 to 10:23 UTC, thirteen minutes
before this pass began, and carried every structure the 11-16, 11-17 and 11-18 passes added with no
hand edit. No collision, for the third day running.

## Part 1 - 876 headings in the two renditions a model reads, and not one address

Since 2026-11-02 every section heading inside an article has carried an `id`. That change exists so
a passage can be cited instead of a whole 2,500-word page, and the 11-02 report called the absence
of those ids the cap on everything else. There are **766 of them** across the archive, 315 distinct.

The site does not tell a model to read the page. Every dispatch's `rel=alternate` names
`/md/<slug>.md`, and `llms.txt` points at the md renditions and at `llms-full.txt`. Here is what
those two renditions carried:

| rendition | `## ` headings | section anchors |
|---|---|---|
| the 98 md files | 876 | **0** |
| the 98 `llms-full.txt` segments | 876 | **0** |

Not one `#h-` string in any of the 98 md files. Not one anywhere in a 2.0MB `llms-full.txt`. The FAQ
answers sitting three lines further down the same files have each carried a `Permalink:` line since
they were written, so the renditions were already in the habit of publishing an address; the 766
section anchors were the ones left out.

### The rule the site publishes for building one is wrong

There was a route. `llms.txt` line 10 states the convention in prose: lowercase the heading's own
words, collapse non-alphanumeric runs to hyphens, prefix `h-`, and drop rendered counts and list
ordinals. It did not say that **apostrophes are dropped rather than hyphenated**, which
`heading_slug` has done since 11-02 and documents in its own docstring.

So the rule the site publishes turns "Why the usual fixes don't hold" into
`#h-why-the-usual-fixes-don-t-hold`, and the real anchor is `#h-why-the-usual-fixes-dont-hold`.
**37 of the 766 section anchors contain an apostrophe, across 32 pages**, with
`Why the usual fixes don't hold` alone appearing on 24. A model following the site's own
instructions built a dead link roughly one time in twenty, and a dead fragment is worse than no
fragment: it reads as a citation the page does not support.

### What is written now

Both renditions carry a `Section anchors:` line, in the `Name (URL)` format and `; `-separated shape
the `- Entities:` line has used since 11-17, placed immediately after it in both:

```
- Section anchors: The short answer (https://blog.dugong.live/....html#h-the-short-answer); Every
new product goes to general, and nothing moves it (https://blog.dugong.live/....html#h-every-new-
product-goes-to-general-and-nothing-moves-it); ... ; Common questions
(https://blog.dugong.live/....html#faq-heading); Read next
(https://blog.dugong.live/....html#related-heading)
```

**1,752 anchor URLs, 876 distinct, every one of them verified to resolve to an `id` that is already
in the markup.** Resolution is by the heading's own visible text for 765 of the 876, because the
renditions and the page write the heading identically; `Common questions` resolves to
`#faq-heading`, the anchor its section's `aria-labelledby` has always named and the `url` the
`FAQPage` node has carried since 11-18; `Read next` resolves to `#related-heading`. No new address
is published and no new prose. The `llms.txt` paragraph now states the apostrophe rule, gives it a
worked example, and says the anchors no longer have to be constructed at all.

The resolver lives in `seo-check.py` as `section_anchor_pairs` and the writer imports it, so the
page, the md and `llms-full.txt` cannot drift apart the way the two short-answer writers did.

## Part 2 - Two edges, found by surveying every node's property set

A property survey of all 110 `@graph` blocks turned up two single-node gaps, both fixed by copying a
value the site already asserts:

**`#priya-singh` on `index.html` carried her description, her employer and her expertise and not
`mainEntityOfPage`**, which her own page has asserted since it was written. A consumer reading only
the homepage got a Person with a `url` and no statement that any page is about her. The 11-17
`node_definition_conflict` check compares scalars, so it reads a missing reference as an absence
rather than a disagreement.

**The question index's `CollectionPage` carried no `headline`**, alone among the nine. On all eight
topic guides `headline` is present and is exactly the node's own `name`, so that is what was
written. The one collection whose entire purpose is to be lifted question by question was the one
without a headline.

## Part 3 - What was deliberately not written

The pass held itself to one rule: **every value written is either an address already in the markup
or a scalar the same page already asserts.** Four things were considered and dropped.

**A property-set equality check on shared site nodes.** This looked like the natural generalisation
of the `#priya-singh` finding until it was measured: `#blog` is restated on 110 pages and 109 of
those restatements are a `url` and a `name`, `#priya-singh` on 99 and 98 of those are three
properties. **A partial restatement is correct JSON-LD, not a defect**, so that check would have
fired on several hundred pages and been wrong on all of them. The check that shipped reads only a
restatement rich enough to carry the person's biography, which is a full copy by any reading.

**Retargeting internal links at section anchors**, carried item 4 since 11-04 and described there as
the biggest lever left. It was measured properly for the first time today: **871 in-article internal
links, 0 with a fragment, and 0 whose anchor text slugs to a heading that exists on the target
page.** There is no mechanical subset. Every one of the 871 needs an editorial choice of target, so
the item is not waiting on tooling and no autonomous pass should invent one.

**A count in the `llms.txt` prose.** The first draft of the corrected paragraph said "37 of the 766
section anchors are of that shape". Both numbers move with the archive, and this file's own lesson
about counts is that a number written beside a list it does not own is a dead claim waiting for the
next dispatch. The rule is stated without them.

**`name` on the `FAQPage` and `supply`/`tool` on the `HowTo`**, left out by the 11-18 pass for the
same reason they are left out today: writing one means publishing a string that exists nowhere on
the site.

## Part 4 - Thirteen invariants, planted and verified

| check | fires when |
|---|---|
| `md_without_section_anchors` | an md rendition has no `- Section anchors:` line |
| `md_section_anchors_mismatch` | the line disagrees with the page, naming the position and both values |
| `llms_full_without_section_anchors` | a segment header has no `Section anchors:` line |
| `llms_full_section_anchors_mismatch` | that line disagrees with the page |
| `section_heading_without_anchor` | a `## ` heading in a rendition resolves to no `id` on the page |
| `section_anchor_not_in_page` | an anchor is listed and is not an `id` in the markup |
| `llms_without_section_anchor_note` | `llms.txt` stops documenting section anchors at all |
| `llms_anchor_rule_unexampled` | the paragraph states the rule and gives no worked example |
| `llms_anchor_rule_example_absent` | an example names a heading no page carries |
| `llms_anchor_rule_example_wrong` | `heading_slug` or the markup disagrees with an example |
| `collectionpage_without_headline` | a `CollectionPage` carries no `headline` |
| `collectionpage_headline_not_name` | its `headline` is not its own `name` |
| `person_restatement_incomplete` | a `Person` restatement carrying the biography drops a property the canonical definition asserts |

A rule stated in prose cannot be executed, so what the three `llms_anchor_rule_*` checks make
executable is its **worked examples**: every `"heading" is #anchor` pair in the paragraph is resolved
against `heading_slug` and against the markup, and a paragraph with no example is itself a failure.
This is worth being honest about: **it would not have caught today's defect.** The one example the
paragraph already gave was correct, which is exactly why the missing apostrophe clause survived
seventeen days. What the check guarantees from now on is that the examples stay true, and the
apostrophe case is now one of them.

**All thirteen were verified fail-loud by planting their defect in a copy of the real tree and
running the real checker, at the end of the pass, after the last edit to either file.** Thirteen
runs, one defect each, thirteen fired, exit code 1 every time.
`_qa_tmp/seo-2026-11-19/plant-defects.py` takes the check name as an argument, so any one of them
can be re-run in a single command. No existing check was loosened and **no `EXCEPTIONS` entry was
added.**

The same checker was also run, before any of this pass's content changes, against a copy of the
pre-pass tree. It reported `md_without_section_anchors` on 98 files, `llms_full_without_section_anchors`
on 98, `collectionpage_without_headline` on 1 and `person_restatement_incomplete` on 1, and exited 1.
The checks read the real defects, not only planted ones.

## Part 5 - Audit after the changes

| Check | Result |
|---|---|
| `_tools/seo-check.py` | **PASS**, 111 rendered pages, 82 stubs, 98 dispatches, 110 sitemap URLs, 98 feed items |
| md renditions carrying a `Section anchors:` line | **98 of 98** (was 0) |
| `llms-full.txt` segments carrying one | **98 of 98** (was 0) |
| anchor URLs written | **1,752**, 876 distinct |
| those resolving to an `id` present in the markup | **1,752 of 1,752**, verified by a second script written independently of the writer |
| `CollectionPage` nodes carrying `headline` equal to `name` | **9 of 9** (was 8) |
| `Person` full restatements carrying the whole node | **3 of 3** (was 2) |
| invariants added | **13**, all verified fail-loud against planted defects in the real tree |
| every check name the README claims is in the file | verified by `grep`, before and after |
| writers idempotent | verified, second run on the final tree reports 0 md files, 0 segments and 0 files changed |
| `apply-checks.py` blocks identical to what is installed | verified, each present exactly once |
| HTML files changed | **2 of 111**: `index.html`, `shopify-automation-questions.html` |
| **lines changed outside an `ld+json` block, all 111 HTML files** | **0** |
| render, both changed pages, 1280 and 390, DOM + geometry + visible text + full-page pixels | **identical, 4 of 4** |
| the same harness, control run (one tree against itself), run first | **identical, 4 of 4** |
| `sitemap.xml`, `feed.xml`, `robots.txt` | **byte-identical** |
| pages whose `dateModified` moved | **0** |
| prose, markup, classes, stylesheets, scripts changed | none |
| em dashes, en dashes, mojibake introduced | 0 / 0 / 0 |
| duplicate element ids / broken links / anchors | 0 / 0 / 0 |
| total HTML weight | 13,737,172 to 13,737,303 bytes, **+0.001%**; gzipped, **+12 bytes for the whole site** |
| md renditions | 2,167,416 to 2,308,009 bytes, +6.487%; **gzipped +2.730%, about 173 bytes per dispatch** |
| `llms-full.txt` | 2,055,827 to 2,196,224 bytes; **gzipped +155 bytes per segment** |
| `llms.txt` | 306,627 to 306,992 bytes |

**About 328 gzipped bytes per dispatch, across both renditions, to make 876 passages citable by
address rather than reconstructable by a rule that was wrong.** The raw cost is the highest of the
recent passes because an absolute URL is repeated once per heading; gzip charges almost nothing for
the canonical URL's eleventh copy.

**Dates were deliberately not moved.** The two HTML edits sit inside `ld+json`, nothing a reader
sees is different, and the renditions gained a metadata line of the same kind the 11-17 pass added
without moving dates. So no page's `dateModified` moved and no `lastmod` had to.
`lastmod`-versus-`dateModified` and `index_date_before_newest_listed` both still pass.

Changed paths: **187** in the working tree, of which **105 are this pass**: 98 md files, 2 page HTML
files, `llms.txt`, `llms-full.txt`, `_tools/seo-check.py`, `_tools/README.md` and this report. The
other 82 are today's publishing run. The pass's five scripts are in `_qa_tmp/seo-2026-11-19/`, which
`.gitignore` covers, along with `site-before.tar.gz`, the pre-pass tree every before/after number
above is measured against.

## Part 6 - Operations

**The sandbox-first rule was followed.** Every write was dry-run end to end in a copy of the tree
outside the mounted folder, with the checker run against it, before anything was written to the
repository. Then the whole sequence was re-applied from a clean copy of the pre-pass tree in script
order and the result diffed against the first sandbox: identical apart from a `.pyc` timestamp. That
is what makes "one command re-applies this pass" a measured claim rather than a hope.

**The first version of the writer had a real bug the sandbox caught.** It carried its own copy of
the heading-to-anchor resolution, which is the mistake the two short-answer writers made and the
11-02 pass wrote a shared `heading_slug` to prevent. It now imports `section_anchor_pairs` from the
checker, and the refactor was verified by rebuilding the whole tree from scratch with it.

**Scripts were written into the tree before being run, both writers are idempotent, and the pre-pass
tree was copied before the first write.** The three habits the 11-17 drop named, followed again.

## Part 7 - Needs a decision

1. **`wikidata.org` and `en.wikipedia.org` are still refused**, re-tested today on **four** paths:
   the desktop shell, the cloud container's `curl`, `WebFetch` and `WebSearch`. The first three
   return `connect_rejected` or 403 at the tunnel; a web search for the three item ids returns
   nothing that confirms them. So the three groundings the 11-17 pass corrected on internal evidence
   are **still not externally verified**: `Order fulfillment` -> Q1473552, `Pricing` -> Q2516951,
   `Wholesale` -> `/wiki/Wholesaling`. Allow-listing those two hosts would also let a pass check that
   the 111 entity IRIs resolve at all, which nothing has ever done.
2. **Organization `sameAs` still resolves nothing.** It lists `https://dugong.live`, the node's own
   `url`. **Needs someone to supply LinkedIn, X, GitHub or Crunchbase URLs.** 111 concepts are
   identified, 499 answers and 657 steps name the publisher, 876 passages now have an address, and
   the publisher is still the one node in the graph grounded in nothing.
3. **Internal links inside article bodies still carry no fragment, and this is now a measured
   editorial job rather than a pending one.** 871 links, 0 with a fragment, **0 with a mechanical
   target** (Part 3). Every target exists; choosing which one each link means is writing, and that
   needs you. This is still the biggest single lever left on the site.
4. **QA's newsletter finding is still open and is still the most serious thing on this list.** The
   signup form in `index.html` has no `action`, no input `name`, and an `onsubmit` that calls
   `preventDefault()`, tells the reader `subscribed`, and sends the address nowhere, beside a
   `4,200 readers` claim nothing supports.
5. **The lead essay still has no `FAQPage` and no `HowTo`**, the only one of 98 without either. It is
   also the only dispatch with no `citation`. Editorial.
6. **Nº 137 is filed in returns and refunds; its own cross-links point at shipping.** Unchanged since
   10-31. A one-guide edit plus four counts, and a real topical-cluster error.
7. **Google Fonts is still a render-blocking third-party stylesheet on all 111 pages.** Unchanged.
   `render-diff.js` makes the before/after provable, so this is a smaller ask than it was.
8. **og:image is still the same banner on all 111 pages.** Unchanged since 10-12, and 96 `HowTo`
   nodes now reference `#primaryimage` as the image of the playbook they describe.
9. **Three of the twelve `ItemList` nodes carry no `description`.** Found by the 11-18 property
   survey, confirmed by today's, and still not fixed because writing one means writing prose.
10. **261 operational markdown files are still served from the site root**, including this one and
    today's blog run. `robots.txt` disallows all three prefixes in every group, and because of
    `.nojekyll` that request is the only thing between them and a crawler.
11. **`_qa_tmp/` is 347MB** and `_to_delete/` still holds 9 zero-byte probe files. `.gitignore`
    covers both, so none of it can reach a commit or the live domain. Deleting needs you.
12. **Today's work is uncommitted.** 187 paths, all dated today: dispatch Nº 144 and this pass.
    Unlike every report since 10-31 this is one day old, not nineteen, because item 1 was finally
    done last night. One `git add -A && git commit && git push` from a normal shell publishes it. **No
    autonomous run has pushed, by deliberate precedent, and none should start without you saying so.**
