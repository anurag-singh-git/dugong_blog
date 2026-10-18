# SEO / GEO report - 2026-10-17

Scheduled autonomous run. Last SEO/GEO pass: 2026-10-16.

## Part 0 - The 10-16 backlog is live, today's is not

Good news first, because the last two reports opened with the opposite. `HEAD` is `0a4e1d8`,
committed 2026-10-17 09:30 +0530, and it is identical to `origin/main`. The 115-change backlog that
Part 0 of the 10-16 report was about has been committed and pushed. Everything from the 10-12,
10-13, 10-14 and 10-16 passes, plus dispatches Nº 128 and Nº 129, is now served from the repository.
Standing item 0 is closed.

What is pending is today. The working tree carries 101 changes: today's blog run (Dispatch Nº 130,
committed nowhere yet) plus this pass. None of it is live until someone pushes. I have not committed
or pushed: the commit history here is hand-written and this is a mixed blog-run and SEO diff. A
notification went out.

## Part 1 - Field-level audit, before any changes

Recomputed from the files: 178 HTML files, 96 rendered (84 dispatches including the lead essay, 8
topic guides, the question index, the author page, index.html and 404.html), 82 redirect stubs.

| Check | Result |
|---|---|
| JSON-LD parses, all rendered pages | 95 / 95 (404.html carries none, by design) |
| exactly one h1 | 96 / 96 |
| canonical == filename == og:url | 96 / 96 |
| meta description 70-165 and unique | PASS, 0 failures |
| description == og == twitter | all but index and 404 (standing item) |
| broken internal links / in-page anchors / cross-file anchors | 0 / 0 / 0 |
| duplicate element ids | 0 |
| sitemap 95 locs, 0 dupes, 0 ghosts, no stubs | PASS |
| feed 84 items, parses, 0 ghosts | PASS |
| every dispatch in feed, llms.txt, llms-full.txt, /md/ | 84 / 84 / 84 / 84 |
| orphan rendered pages | 0 (404.html excepted) |
| FAQPage questions with a non-empty acceptedAnswer | all |
| HowTo steps typed and named | all |
| BreadcrumbList / ItemList positions 1..n | all |
| mojibake, em dashes, en dashes | 0 |
| **title <= 60 and unique** | **1 FAIL** (Nº 130, 74 chars) |
| **sitemap lastmod agrees with the page's own dateModified** | **3 FAIL** |

Both failures came from today's blog run, and both are the same class of generator bug the 10-16
report described in Parts 2 and 3. That report predicted this would come back. It came back the next
day.

## Part 2 - Dispatch Nº 130 shipped a 74-character title

`<title>How to stop Shopify B2B prices dropping every time you run a sale | Dugong</title>`

Google truncates the title link around 60 characters, so "| Dugong" and the last two words of the
headline would never have been shown. The site has held 60 on all 95 previous rendered pages, and
the convention when a headline runs long is to drop the "| Dugong" suffix rather than let the title
overflow. Rewritten to 53 characters:

> How to stop Shopify B2B prices dropping during a sale

"during a sale" rather than "when you run a sale" keeps the query phrase and the how-to intent
inside the cap. The JSON-LD `headline`, `og:title` and `twitter:title` keep the full 65-character
sentence, which is correct: those are not truncated the way a SERP title link is.

## Part 3 - Three pages had their sitemap lastmod moved but not their own dateModified

Today's blog run bumped four sitemap `lastmod` values to 2026-10-17 and updated the content of each
page, but moved only one of the pages' declared `dateModified`:

| Page | sitemap said | page said | now |
|---|---|---|---|
| priya-singh.html | 2026-10-17 | 2026-10-16 | 2026-10-17 |
| shopify-automation-questions.html | 2026-10-17 | 2026-10-16 | 2026-10-17 |
| shopify-customer-and-wholesale-automation.html | 2026-10-17 | 2026-10-10 | 2026-10-17 |

A crawler takes the recrawl hint from one of those and the content date from the other; when they
disagree it learns to trust neither. All three genuinely changed today (each gained the Nº 130 card
and ItemList entry), so the sitemap was right and the pages were stale. Corrected on the pages.

The customer and wholesale guide was seven days stale on a page that had just gained a dispatch.

`the-death-of-the-drag-and-drop-builder.html` still has `lastmod` 2026-10-14 against `dateModified`
2026-05-28 and is still left alone on purpose: the URL first appeared on 10-14, the essay text has
not changed since May, and both statements are true. Carried from 10-16 and now recorded as a
documented exception in the checker rather than in prose.

## Part 4 - 3 of the site's 115 entity links were dead and 1 pointed at a disambiguation page

The largest GEO finding this run. Every BlogPosting carries an `about` array of `Thing` nodes with a
`sameAs` pointing at Wikipedia. That is the markup that lets a knowledge graph resolve what an
article is about. Nobody had ever checked that the targets exist.

All 115 distinct Wikipedia targets were resolved against the Wikipedia API. Four were wrong:

| Entity | Target | Problem | Now |
|---|---|---|---|
| Bulk operation | `/wiki/Bulk_operation` | **no such article** | Batch processing, `/wiki/Batch_processing` |
| Order management | `/wiki/Order_management_system` | **no such article** | Order processing, `/wiki/Order_processing` |
| Minimum order quantity | `/wiki/Minimum_order_quantity` | **no such article**, and no Wikidata item either | entity removed |
| Inventory management | `/wiki/Inventory_management` | resolves, but it is a **disambiguation page** ("Topics referred to by the same term") | `/wiki/Inventory_management_(business)` |

The three dead links were worse than having no `about` entity at all: they assert an entity
identity that cannot be resolved, on three pages that are otherwise fully marked up. The
disambiguation page is the subtler failure, because it resolves to a real Wikidata item whose
meaning is "this phrase is ambiguous", which is the opposite of what the property is for. It
appeared on three pages.

For "Minimum order quantity" there is no Wikipedia article and a Wikidata search returns nothing, so
rather than substitute a near-miss concept (Economic order quantity is a different thing) the entity
was dropped. That page keeps Shopify, Point of sale and E-commerce, which is the same count most
dispatches carry.

## Part 5 - Every entity now carries a Wikidata ID as well as a Wikipedia URL

Wikipedia URLs are readable but they are strings; Wikidata QIDs are the identifiers search and
answer engines actually key entities on, and they are language- and rename-independent. The site had
316 entity references and not one QID.

`sameAs` is now an array on all of them:

```
"sameAs": [
  "https://en.wikipedia.org/wiki/Shopify",
  "https://www.wikidata.org/wiki/Q7501150"
]
```

317 entity references across 85 files, 110 distinct QIDs. Every QID came from the `wikibase_item`
page property of the Wikipedia article itself rather than from a search, so the pairing is
authoritative by construction. It was then checked in the other direction: all 110 were fetched back
from the Wikidata API and each one's `enwiki` sitelink compared against the Wikipedia slug sitting
beside it in the same array. 110 / 110 matched, 0 mismatches.

Four QIDs are each reached by two different Wikipedia slugs, and all four are correct: Backorder and
Stockout both resolve to Q962928, Wholesale and Wholesaling to Q220695, Stock management and
Inventory management (business) to Q3761396, Volume discount and Discounts and allowances to
Q291046. Wikipedia redirects, one Wikidata item, which is exactly the behaviour that makes QIDs
worth adding.

## Part 6 - The underscore directories are on the live site, and were not disallowed

The 10-16 report said, in Part 5, that `_qa_tmp/` and `_to_delete/` "need no rule, Jekyll already
excludes any path beginning with an underscore." **That is wrong, and it is wrong because of a file
in this repository.**

`.nojekyll` exists at the repository root. GitHub Pages treats it as an instruction to skip the
Jekyll build entirely and serve the repository raw. There is no Jekyll, so there is no Jekyll
exclusion. Everything committed under an underscore path is fetchable on blog.dugong.live.

What is committed there: 36 files under `_qa_tmp/`, including whole-site `.tar.gz` snapshots at
roughly 3 MB each, and 14 files under `_to_delete/`. Plus `__deltest.tmp` at the root, which the
10-16 report had correctly flagged as servable.

Four `Disallow` prefixes added to **all 40 user-agent groups**, for the same reason the report
prefixes had to be: a crawler that matches a named group ignores the `*` group entirely, so a rule
under `*` alone would leave GPTBot, ClaudeBot, PerplexityBot and 37 others reading them.

A note was added to the top of robots.txt explaining the `.nojekyll` situation, so the next pass does
not repeat the mistake, and stating plainly that robots.txt asks crawlers not to fetch and does not
make a path private. See Part 9 item 2.

**The Disallow lines now come before `Allow: /` in every group.** This was not cosmetic. Under
RFC 9309 longest-match the order is irrelevant: `Disallow: /_qa_tmp/` is more specific than
`Allow: /` and wins either way. But crawlers that still use the older first-match-wins rule take the
first line that matches the path, and `Allow: /` matches everything, so with `Allow: /` first every
`Disallow` in the file was inert for them. That applied to the three report prefixes added on 10-16
as well, so this retroactively fixes those too.

Validated with two independent parsers, because robots.txt is the one change in this run that could
deindex the site: `protego`, and Python's stdlib `RobotFileParser` as a deliberately
first-match-wins second opinion. 850 assertions across 17 agents including `*`, Googlebot, Bingbot,
GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-User, PerplexityBot, Google-Extended,
Applebot, Amazonbot, meta-externalagent and an unknown agent string. Both parsers agree: every
article, every `/md/` file, sitemap.xml, feed.xml, llms.txt, llms-full.txt, every image, 404.html
and robots.txt itself allowed for every agent; every report path, `_qa_tmp`, `_to_delete`, `_tools`
and `__deltest.tmp` denied for every agent. Before the reordering the stdlib parser allowed all of
them, which is how the ordering problem was found.

## Part 7 - Organization knowsAbout, and a dateModified on the homepage

Two smaller markup additions, both head-only.

`Organization` is fully defined once, on index.html, and referenced by `@id` everywhere else. It
carried name, url, description, logo and `sameAs`, but nothing stating what the publisher is
authoritative about. `knowsAbout` added with the 12 topics the site actually covers, derived from
the eight topic guides rather than asserted: workflow automation, Shopify automation, e-commerce
operations, order management, inventory management, shipping and fulfillment, returns and refunds,
e-commerce fraud and risk, discounts and promotions, wholesale and B2B commerce, product catalog
operations, AI agents. The author `Person` node already had `knowsAbout`; the publisher did not.

The homepage was in the sitemap with a `lastmod` and declared no `dateModified` of its own, so its
freshness was asserted only in a file a reader never sees. `dateModified` added to the `Blog` node.
This surfaced as a note from the new checker, not from reading the page.

## Part 8 - A checked-in invariant checker, so this stops recurring

Parts 2 and 3 are the third and fourth generator bugs of this class in two days. The 10-16 report
recommended adding checks at source. `_tools/seo-check.py` is that, with `_tools/README.md`
explaining how and when to run it:

```
python3 _tools/seo-check.py
```

Exit 0 if every invariant holds, 1 otherwise, standard library only so it runs in either shell. It
covers everything in the Part 1 and Part 10 tables: title and description caps and uniqueness,
description matching og: and twitter:, `dateModified` against sitemap `lastmod` **on every page that
declares one, not only the dispatches**, the 20 BlogPosting fields, both halves of every entity
`sameAs`, FAQPage answers, HowTo steps, ItemList and BreadcrumbList positions, sitemap and feed
integrity, llms.txt / llms-full.txt / `/md/` coverage and the Markdown alternate link, internal
links and anchors, duplicate ids, mojibake, em and en dashes, and robots.txt per-group coverage.

The `dateModified` detail matters: today's drift was on a ProfilePage and two CollectionPages, so a
first version of the checker that only looked at Article nodes walked straight past it. That is why
it is worth saying that **the checker was tested against the pre-run snapshot rather than only
against the fixed tree.** Run on `_qa_tmp/seo-2026-10-17-before.tar.gz` it reports exactly the three
real defects this pass found: `title_too_long` on Nº 130, `lastmod_vs_datemodified` on the three
pages in Part 3, and `entity_no_wikidata` on all 316 entity references. Run on the tree as it stands
now it reports PASS. A checker that has only ever been run against a passing tree is worth nothing.

Deliberate exceptions live in an `EXCEPTIONS` dict at the top of the file, each with the reason in a
comment: index.html and 404.html keep hand-written og:/twitter: copy, the lead essay's two dates
legitimately differ, 404.html is noindex and unlinked by design. The README says, in as many words,
that a check firing on something correct is fixed by adding an exception with a reason and never by
loosening the check.

`_tools/` is disallowed in robots.txt and the leading underscore keeps it out of the sitemap, the
feed and llms.txt.

## Part 9 - Audit after the changes

| Check | Result |
|---|---|
| JSON-LD parses, all rendered pages | 95 / 95 |
| exactly one h1 | 96 / 96 |
| canonical == filename == og:url | 96 / 96 |
| title <= 60 and unique | **PASS, 0 failures** |
| meta description 70-165 and unique | PASS, 0 failures |
| description == og == twitter | all but index and 404 (documented exception) |
| sitemap lastmod agrees with dateModified | **PASS** (1 documented exception) |
| broken links / in-page anchors / cross-file anchors | 0 / 0 / 0 |
| duplicate element ids | 0 |
| entity sameAs carries Wikipedia **and** Wikidata | **317 / 317** |
| distinct QIDs verified round-trip against Wikidata | **110 / 110, 0 mismatches** |
| BlogPosting carries all 20 fields | 84 / 84 |
| FAQPage / HowTo / ItemList / BreadcrumbList integrity | PASS |
| sitemap 95 locs, feed 84 items, both parse | PASS |
| llms.txt / llms-full.txt / md coverage | 84 / 84 / 84 |
| orphan rendered pages | 0 |
| mojibake, em dashes, en dashes | 0 |
| robots.txt, two independent parsers, 850 assertions | **PASS** |
| `_tools/seo-check.py` on this tree | **PASS** |

**No render pass this run, and it is not needed.** Every HTML change was diffed against the pre-run
snapshot and classified by position: **1,617 changed lines across 88 files, all 1,617 inside
`<head>`, zero changes below it.** No CSS, no DOM, no copy a reader sees. The `<title>` change shows
in a browser tab and a SERP, not on the page. feed.xml, sitemap.xml, llms.txt, llms-full.txt and
every file under `md/` are byte-identical to where today's blog run left them. The 10-14 render pass
across 8 widths therefore still holds.

Snapshots: `_qa_tmp/seo-2026-10-17-before.tar.gz` and `_qa_tmp/seo-2026-10-17-after.tar.gz`.

## Part 10 - Measured this run, for the record

Two things worth having numbers for, neither of them a defect.

**Internal linking is dense, and new dispatches start at zero.** Every dispatch ends with a
related-grid listing nearly every other dispatch, so inbound internal links accumulate strictly by
age: a post published on day D is listed by every post published after it. Measured across the 84
dispatches, editorial (non-hub) inbound links run from 33 to 80 for everything older than three
days, and the three newest dispatches have **zero**:

- how-to-stop-shopify-b2b-prices-dropping-when-you-run-a-sale.html (Nº 130, today)
- how-to-handle-return-to-sender-orders-on-shopify.html (Nº 128)
- how-to-stop-reordering-shopify-stock-you-already-have-on-order.html

Each still has four inbound links from the homepage, its topic guide, the author page and the
question index, and sits in the sitemap at priority 0.9 with today's lastmod, so discovery is fine.
But the page that most needs internal PageRank has the least of it, for about three days, and then
the deficit closes on its own as later dispatches list it. Retrofitting today's post into 83
historical related-grids would fix it immediately at the cost of 83 files of below-the-head DOM
changes and a render pass. That is a design decision, not an SEO repair, so it is in Part 11 rather
than done.

**The lead essay has 2 editorial inbound links**, against 33 to 80 for every dispatch older than
three days. Standing item 7 from 10-16, now with a number. It is the only non-Shopify piece, so the
eight Shopify guides have no honest reason to link it and it is excluded from the dispatch
related-grids by topic. Still thin for the page the site calls its lead essay.

## Part 11 - Needs a decision

1. **Commit and push.** 101 pending changes: Dispatch Nº 130 and this pass. Until this happens none
   of it is SEO at all. This is the only item that blocks everything else.
2. **`_qa_tmp/` should probably be gitignored, not just disallowed.** Part 6 closed the crawler
   hole, but robots.txt is a request, not an access control. Whole-site tarballs and QA checksums
   are still publicly downloadable by anyone who knows or guesses a path, and they are in the git
   history either way. Adding `_qa_tmp/` to `.gitignore` and keeping snapshots locally would end it
   properly. Deleting what is already committed needs someone at the desk, and rewriting history is
   a bigger call than a scheduled run should make.
3. **`__deltest.tmp` (2 bytes) and `_to_delete/` are still in the tree.** Now disallowed, so no
   longer an SEO problem, but still committed. Deleting files on this machine needs a permission
   prompt and nobody is at the desk. Carried from 10-16.
4. **Google Fonts is a render-blocking third-party stylesheet on all 96 pages.** The only external
   resource the site loads, and the only Core Web Vitals lever left: zero images, inline CSS, almost
   no JS. `preconnect` to both font hosts is already there and the URL already carries
   `display=swap`, so the fix is to make the stylesheet non-blocking:
   ```
   <link rel="preload" as="style" href="...">
   <link rel="stylesheet" href="..." media="print" onload="this.media='all'">
   <noscript><link rel="stylesheet" href="..."></noscript>
   ```
   Not done, deliberately. It changes paint behaviour on every page and neither shell can reach
   blog.dugong.live or fonts.googleapis.com (both proxies answer 403 to CONNECT), so it could not be
   measured before or verified after. Worth a supervised run that can render and compare.
5. **og:image is still the same banner on all 96 pages.** Unchanged from 10-12, 10-14 and 10-16.
   Per-post share images would lift click-through from social and from the AI surfaces that show a
   thumbnail. Still a design call plus a batch render job.
6. **Organization `sameAs` still resolves nothing.** It lists `https://dugong.live`, which is already
   the node's `url`, so it does no entity-resolution work. This run searched again and found no
   public profiles for this Dugong: the results are "Dugong Global Services" and dugongx.com, both
   unrelated IT-services companies, and a "Dugong AI" health entity on Preqin. Real profiles
   (LinkedIn company page, X, GitHub, Crunchbase) are what tie a publisher to a known organization,
   and citing someone else's would be worse than leaving the field thin. **Needs someone to supply
   the real URLs.** This is now the largest remaining GEO gap on the site.
7. **Retrofit the newest dispatches into historical related-grids?** See Part 10. Immediate fix for
   the zero-inbound window on new posts, at the cost of 83 files of DOM change and a render pass, and
   it changes what "related" means on every old post. Owner's call.
8. **The lead essay's 2 editorial inbound links.** Part 10. Worth a look next time a dispatch touches
   builder fatigue or no-code limits.
9. **The 37 distinct external links are still unverified.** Both shells are behind proxies that
   refuse help.shopify.com and shopify.dev; raw curl and WebFetch both get 403 on CONNECT. Wikipedia
   and Wikidata were reachable through the browser pane this run, which is how Parts 4 and 5 got
   done, so the same route may work for the Shopify docs under supervision. Carried from 10-16.
10. **The blog run still writes content and counts but not dates or length caps.** Parts 2 and 3
    again. `_tools/seo-check.py` now catches all of it after the fact, which is a safety net rather
    than a fix. Two checks inside the generator would retire the category: reject a title over 60 or
    a description outside 70-165, and move `dateModified` on every page the run touches, not only the
    new post. **Add `python3 _tools/seo-check.py` to the end of the blog run** and it fails loudly
    the same day instead of waiting for an SEO pass.
11. **index.html and 404.html keep hand-written og:title and og:description** that differ from their
    h1 and meta description. Deliberate, both inside the caps, now recorded as an exception in the
    checker. Carried from 10-14 and 10-16.
12. **Aanya Rao still has no author page**, so her `author` node is the only one of 84 without a
    `url`. One dispatch does not make an archive worth indexing; her Person node is typed inline on
    the essay and named in llms.txt. Carried from 10-14 and 10-16.
13. **"Inventory management" on six dispatches points at `/wiki/Inventory_management_software`**
    (Q6059927), which is an article about software rather than the practice. It resolves and is
    defensible on pages about automating stock with software, but Q3761396 is the practice and is now
    used by the three pages fixed in Part 4. Worth making consistent per page, which needs someone to
    read the six and decide which sense each means.
