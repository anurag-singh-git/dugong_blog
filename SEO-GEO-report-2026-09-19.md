# SEO / GEO report - 2026-09-19

Scheduled autonomous run. Last SEO/GEO pass: 2026-09-18, yesterday. Yesterday's work did get
committed and pushed: `04c604b` on `main`, local and `origin/main` level, 89 files, and every
one of yesterday's 68 citation edits is in it. Then the run checked the live site, which is
where this report stops being routine.

## Part 1 - The site has not deployed since August 29

This is the whole report, really. Everything below it is maintenance on a tree nobody can read.

Yesterday's run found Nº 117 and Nº 118 returning 404 and put the cause down to uncommitted
work. That diagnosis is now ruled out. The work is committed, it is on GitHub, and the site
still does not have it.

Checked directly today, from both ends:

| Source | Nº 117 duplicate SKUs | Nº 118 shipping rates | Nº 119 state restrictions |
|---|---|---|---|
| `raw.githubusercontent.com/.../main/` | 200, correct title | present | n/a, written today |
| `blog.dugong.live` | **404** | **404** | **404** |

`git ls-remote origin main` returns `04c604b`, the same commit as local `HEAD`. The live
`sitemap.xml` still has `2026-08-29` as its newest `lastmod`. So the push worked and GitHub
Pages has not rebuilt from it. Three finished dispatches, the 09-17 markup pass and the 09-18
citation pass are all on GitHub and none of them are being served. Twenty-one days.

### What was done about it

A `.nojekyll` file was created in the repo root, empty, uncommitted.

The reasoning: this is plain static HTML with no Liquid, no front matter and no templating of
any kind, so it needs nothing Jekyll does, but Pages runs Jekyll by default when `.nojekyll` is
absent, and a failing Jekyll build is the most common reason a Pages site keeps serving an old
commit after a good push. The Sep 18 commit also introduced `_to_delete/`, a new
underscore-prefixed directory, which is exactly the kind of thing Jekyll treats as special.
`.nojekyll` makes Pages skip the build and serve the files as they are.

Be clear about the confidence here: this is the most likely cause, not a confirmed one. The
Pages build log is behind authentication and this run could not read it. If a commit and push
of `.nojekyll` does not bring the site back within a few minutes, the answer is in **Settings
> Pages** and in the **Actions** tab, on the most recent `pages-build-deployment` run, which
will name the actual failure.

    git add -A && git commit -m "Nº 119 + .nojekyll + SEO/GEO 2026-09-19" && git push

Until this is fixed, no SEO or GEO work on this site reaches a reader or a crawler. Everything
in Part 2 is stacked behind it.

## Part 2 - Audit: zero defects

Every check recomputed from the files today, nothing carried forward.

Inventory: **147 HTML files** = 75 rendered (72 wired posts + index.html + 2 noindexed rejected
drafts) and 72 redirect stubs, plus sitemap.xml, feed.xml, llms.txt, llms-full.txt, robots.txt,
CNAME, and the new .nojekyll. Dispatches Nº 48 through Nº 119, contiguous, no duplicates, no gaps.

Dispatch Nº 119, `how-to-restrict-shopify-products-from-shipping-to-certain-states.html`, needed
no retrofit. It arrived carded, sitemapped, fed, in both llms files, with a matching stub, with
`<time datetime>` markup, and with four verified Shopify citations already in prose and in its
`citation` array. The blog-run workflow has absorbed the citation practice on its own. That is
the second run in a row where the newest dispatch needed nothing.

| Check | Result |
|---|---|
| JSON-LD parses, all 75 rendered pages | 75 / 75, 0 errors |
| FAQ parity: visible == FAQPage JSON, questions AND answers, entity-decoded | 72 / 72 |
| FAQ counts: 5 on every post; 360 total | 72 / 72 |
| canonical == og:url == filename; og/twitter sets complete incl. og:image w/h/alt | 75 / 75 |
| exactly one h1; lang; viewport; img alt coverage | 75 / 75 |
| duplicate titles / meta descriptions; descriptions <= 160 chars | 0 / 0 / PASS |
| broken internal links, checked against every file in the tree | 0 |
| author @id resolves to `#priya-singh` on all 72 posts | PASS |
| dateModified == article:modified_time == sitemap lastmod; future dates | 0 mismatches / 0 |
| sitemap.xml: valid XML, 73 locs (72 posts + root), 0 dupes, 0 ghosts | PASS |
| feed.xml: valid XML, 73 items, unique guids, no future dates | PASS |
| llms.txt / llms-full.txt: all 72 posts, 0 ghosts, 0 dupes, fences balanced | PASS |
| llms-full.txt: 5 FAQ headings per section, all 72 sections, none truncated | PASS |
| stubs: 72, bijective onto wired posts, noindexed, targets live | PASS |
| index: all 72 posts carded; WebSite + Organization + Person + Blog entities | PASS |
| rejects (2): noindexed, absent from sitemap / feed / llms / llms-full / index | PASS |
| tag balance, all 147 HTML files | 0 problems |
| citation arrays match body citation anchors, both directions | 72 / 72 |

## Part 3 - Improvements applied

### 1. The citation layer now covers every post

Yesterday's pass left three posts with no citation, because the obvious target for all three,
the order-status-page help URL, redirects to a generic page whose title does not match. Today
found sources that do match, by going at the claim rather than at the page name. Four links
across the three posts, four URLs fetched and title-matched before use, none of them guessed:

| Post | Anchor | Source |
|---|---|---|
| order confirmation emails not sending | "Order confirmation email" | Setting up customer notifications |
| order confirmation emails not sending | "the sending domain is not authenticated" | Displaying your store's sending email |
| pickup orders customers never collect | "Ready for pickup notification" | Setting up pickup in store for online orders |
| cancelled orders showing as unfulfilled | "Cancel or refund an order" | Canceling orders |

The second one is the best of the four. That post lists five distinct causes for a missing
receipt and puts sender authentication first; Shopify's own page on the sending email covers
SPF, DKIM and DMARC and states the CNAME and `v=DMARC1; p=none` requirements directly. The
prose and the source now say the same thing in the same place.

The pickup link is the same kind of confirmation: the post claims Shopify sends one ready-for-
pickup email and never a reminder, and the linked page says a notification is sent when you
mark the order ready and says nothing about a second one, because there isn't one.

**Every one of the 72 posts now carries both the prose anchors and the matching `citation`
array.** 120 verified outbound citation anchors site-wide. Zero drift between the anchors and
the schema in either direction. No prose was rewritten for any of these; existing words became
anchors, nothing else.

### 2. Every post now has an inbound link from a sibling post

This was standing item 3 from yesterday, and it had grown: ten posts had no in-body link from
any other post, not four.

Nº 66 gift messages, Nº 85 review requests, Nº 108 missing personalization, Nº 110 vacation
mode, plus expiry dates, fake signups, duplicate SKUs, shipping dimensions, pickup orders, and
today's Nº 119.

Ten backlinks were added, one per orphan, each from the most closely related older post, placed
in that post's existing READING callout as a third companion line. The callout is the slot the
template already has for this, so nothing structural changed and no existing sentence was
touched; each addition is one new sentence naming the post and why it belongs next to this one.

| Donor | Now links to |
|---|---|
| missing personalization | the gift message that never reaches the box |
| segment repeat customers | the review request you never send |
| validate shipping addresses | the custom order that arrives blank |
| prevent overselling | the SKU two products share |
| route orders to the right warehouse | the shipping rate that ignores your box |
| local pickup to shipping | the pickup order that never leaves the shelf |
| schedule product publishing | the vacation your store won't let you take |
| missing HS codes | the order from a state you can't ship to |
| stop card testing | the customer list the bots built |
| clear dead stock | the expiry date your store can't see |

**Orphans: 10 before, 0 after.** In-body internal links per post went from 7.68 to 7.82. Every
post is now reachable from index.html *and* from at least one topically adjacent post, which is
what actually matters for crawl depth and for an answer engine following a thread.

The same ten sentences were mirrored into `llms-full.txt`, in the plain-text form the converter
uses, so the text file and the HTML still say the same thing. That file is what answer engines
read in bulk; letting it drift from the pages would be a quiet own goal.

### 3. Dates deliberately not bumped

Ten posts did gain a sentence today, which is a real content change and not a cosmetic one, so
this was a live question rather than a formality. Decision: no `dateModified`, no sitemap
`lastmod`, no feed `lastBuildDate` touched.

A one-line companion-reading pointer is not a substantive revision of the article, and marking
ten posts as freshly updated on the strength of it is precisely the freshness signal that gets
discounted, and deserves to be. Every date on the site still means what it says.

## Part 4 - For the owner

1. **Commit and push, then watch the Actions tab.** Part 1. This is the only item that is
   costing something today, and it has been costing it for three weeks.

2. **The three concurrent scheduled tasks, still unstaggered.** Flagged 09-17 and 09-18,
   unchanged. The blog write, this GEO task and the QA task all point at this folder. No
   collision again today, still luck rather than design. An hour apart, or chained, is cheap.

3. **Delete the two rejected drafts** on a supervised run. Standing since 08-02. Noindexed and
   excluded from every surface, so they cost nothing meanwhile. Worth folding in: `_to_delete/`
   now holds three empty stale-lockfile markers from earlier runs and they are tracked in git.

4. **The <= 160-character description check belongs in the blog-run skill.** Standing since
   08-25. Still passing on every post, still unenforced at write time.

5. **The good half of the citation work.** The platform surfaces are now done, all 72 posts.
   What is still unlinked is the better material: the dated community threads, the named staff
   answers, the House vote and the hemp deadline in Nº 119, the carrier tariff notices. These
   posts quote that record almost verbatim and cite none of it. It needs a post-by-post pass
   with every URL opened and matched to the claim, a handful of posts per run. It remains the
   single biggest GEO lever left, and it is now the only large one.

6. **Every post still shares one image.** `og-image.png` is the article image, the og:image and
   the twitter:image for all 72. Per-post images would help in Discover, in image search, and
   would give answer engines something to attach to a specific answer. Needs someone to make
   them; no run can invent them.

## Commit

**14 files edited by this run** (3 posts for citations, 10 posts for backlinks, llms-full.txt),
**2 files created** (`.nojekyll`, this report). The working tree also holds Dispatch Nº 119 and
its stub, and the sitemap / feed / index / llms updates that came with it. No commit was made,
per scheduled-run convention. Suggested message:

    Nº 119 + .nojekyll + SEO/GEO 2026-09-19: citations on the last 3 posts, 10 orphan backlinks

## Verification method note

All counts recomputed from the files by script. FAQ parity checked question-and-answer,
entity-decoded and whitespace-normalized. Tag balance parsed on all 147 files with a word-
boundary matcher, after an earlier pass produced false positives on attributes split across
lines. All four source URLs fetched this run and their titles matched against the claim being
linked before use. Anchor placement was dry-run first and each site inspected in context: all
four landed in the author's own prose, none inside a heading, an existing anchor, a code or pre
block, or a merchant quotation, which was the rule that had to be added mid-pass on 09-18. A
full backup of all 147 HTML files and the four generated files was taken before the first edit.
After the edits: JSON-LD re-parsed on all 75 rendered pages, the full audit re-run and clean,
anchors checked for nesting (0), citation arrays diffed against body anchors in both directions
on all 72 posts (0 drift, Wikipedia context links excluded as they are not citations), llms-full
sections re-counted for FAQ headings and length against their HTML bodies (0 truncated). The
live site and the GitHub remote were both checked directly for Nº 117, Nº 118, Nº 119 and
sitemap.xml. `.fuse_hidden*` files are mount artifacts, ignored per convention.
