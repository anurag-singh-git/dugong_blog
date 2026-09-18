# SEO / GEO report - 2026-09-18

Scheduled autonomous run. Last SEO/GEO pass: 2026-09-17, yesterday. The tree still sits on
commit `dc01c14` (Aug 29) with yesterday's 73-file pass and today's Dispatch Nº 118
uncommitted on top of it. This run did three things: a full re-audit including Nº 117 and
Nº 118, which the 09-17 run could not cover; a check of what the live site is actually
serving, which turned up the finding at the top of Part 3; and the first instalment of the
outbound-citation work that has been the standing number-one GEO item since 08-29.

## Part 1 - Audit: zero defects

Every check recomputed from the files today. Nothing carried forward from yesterday.

Inventory: **145 HTML files** = 74 rendered (71 wired posts + index.html + 2 noindexed
rejected drafts) and 71 redirect stubs, plus sitemap.xml, feed.xml, llms.txt,
llms-full.txt, robots.txt, CNAME. Dispatches Nº 48 through Nº 118, contiguous, no
duplicates, no gaps.

Nº 117 and Nº 118 are both fully wired: carded on index, in the sitemap, the feed,
llms.txt and llms-full.txt, each with a matching stub, and both already carry the
`<time datetime>` markup the 09-17 run added to the older posts. The 09-17 report expected
them to need retrofitting; they do not. Whatever produced them picked up the current
template, so no catch-up edit was needed.

| Check | Result |
|---|---|
| JSON-LD parses, all 74 rendered pages | 74 / 74, 0 errors |
| FAQ parity: visible == FAQPage JSON, questions AND answers, entity-decoded | 71 / 71 |
| FAQ counts: 5 on every post; 355 total | 71 / 71 |
| canonical == og:url == filename; og/twitter sets complete incl. og:image w/h/alt | 74 / 74 |
| exactly one h1; lang; viewport; img alt coverage | 74 / 74 |
| duplicate titles / meta descriptions; descriptions <= 160 chars | 0 / 0 / PASS |
| broken internal links, checked against every file in the tree, not just HTML | 0 |
| author @id resolves to `#priya-singh` on all 71 posts | PASS |
| dateModified == article:modified_time == sitemap lastmod; future dates | 0 mismatches / 0 |
| sitemap.xml: valid XML, 72 locs (71 posts + root), 0 dupes, 0 ghosts | PASS |
| feed.xml: valid XML, 72 items, unique guids, weekday-correct pubDates, no future dates | PASS |
| llms.txt / llms-full.txt: all 71 posts, 0 ghosts, 0 dupes, fences balanced | PASS |
| stubs: 71, bijective onto wired posts, noindexed, targets live | PASS |
| index: 72 BlogPosting nodes, WebSite + Organization + Person + Blog entities | PASS |
| rejects (2): noindexed, absent from sitemap / feed / llms / llms-full / index | PASS |
| tag balance, all 145 HTML files | 0 problems |
| `<time>` balance and nesting, all 145 files | 0 problems |

## Part 2 - Improvements applied: the citation layer

The standing note since 08-29 has been that these posts are unusually well sourced in
prose and link none of it, and that closing the gap needs every URL opened before it is
written, which is why no previous run attempted it. This run had web access, so it did the
verifiable half of the job.

**What was added: 112 outbound links to 21 official Shopify sources, across 68 of the 71
posts.** Every one of those 21 URLs was fetched during this run before it was used. The
page had to return 200 and the returned title had to match the thing being linked. Six
candidate URLs failed that test and were dropped rather than guessed at; they are listed
below so the next run does not re-test them blindly.

### How the links were placed

Only the first mention of each named Shopify surface in a post is linked, one link per
source per post, and only inside `<div class="article-body">`. Matches were skipped inside
headings, existing anchors, code, pre, blockquote, and, after a first pass showed two bad
placements, inside any quoted span. That last rule matters: a link inside a merchant's
quoted forum question reads as if the quote were the citation, which it is not. Two links
were removed for exactly that reason and the pass was re-run from a clean copy.

Nothing in the prose was rewritten. Not one word changed. The only change to the visible
page is that certain existing words are now anchors, and `.article-body a` was already
styled, so they render in the site's lime treatment with no CSS change.

### The 21 verified sources

| Links | Source |
|---:|---|
| 48 | help.shopify.com/en/manual/shopify-flow |
| 8 | help.shopify.com/en/manual/payments/shopify-payments |
| 7 | help.shopify.com/en/manual/shopify-admin/productivity-tools/bulk-editing |
| 7 | help.shopify.com/en/manual/payments/shop-pay |
| 7 | help.shopify.com/en/manual/fulfillment/managing-orders/create-orders |
| 5 | shopify.dev/docs/api/liquid |
| 5 | help.shopify.com/en/manual/online-sales-channels |
| 3 | help.shopify.com/en/manual/customers/customer-accounts |
| 3 | shopify.dev/docs/apps/build/webhooks |
| 3 | help.shopify.com/en/manual/custom-data/metafields |
| 3 | help.shopify.com/en/manual/promoting-marketing/create-marketing/abandoned-checkouts |
| 3 | shopify.dev/docs/apps/build/functions |
| 2 | help.shopify.com/en/manual/custom-data/metaobjects |
| 1 each | admin-graphql, DeliveryCarrierService, delivery-customization Function API, shopify-tax, products/bundles, sell-in-person, ai-powered-tools/shopify-magic, customers/customer-segmentation |

The Carrier Service API and Delivery Customization links both landed in Nº 118, and both
documents happen to confirm the claims that post makes about them, which is the whole point
of the exercise.

### Machine-readable half: `citation` in the JSON-LD

The same 68 posts now carry a `citation` array on their BlogPosting node, one `WebPage`
entry per source linked in that post, with the source's real title and URL. This is
schema.org's own property for "a citation or reference to another creative work", and it
states in structured data exactly what the prose now states in anchors. Verified: the
citation list on every post matches the set of citation anchors in that post's body
exactly, in both directions, with no drift.

### Three posts got nothing

`how-to-fix-order-confirmation-emails-not-sending-on-shopify.html`,
`how-to-handle-shopify-pickup-orders-customers-never-collect.html` and
`how-to-stop-cancelled-orders-showing-as-unfulfilled-on-shopify.html` name no Shopify
surface that has a doc page matching this run's verification bar. All three are about
customer notifications, and the obvious target, the order-status-page help URL, redirects
to a generic "Store notifications" page whose title does not match. Forcing a weak link
into three posts was not worth it. They are the natural first candidates for the next
instalment.

### Six URLs tested and rejected

Do not reuse these without re-testing; each failed today:

- `shopify.dev/docs/apps/build/checkout/delivery-shipping/delivery-customizations` returns 404. The live doc is `shopify.dev/docs/api/functions/latest/delivery-customization`, which is what was used.
- `help.shopify.com/.../create-marketing/abandoned-cart` redirects to a generic marketing index. The real page is `.../create-marketing/abandoned-checkouts`.
- `help.shopify.com/.../create-marketing/shopify-email` now resolves to a page titled "Shopify Messaging". Probably a rebrand, but the title does not match "Shopify Email", so it was dropped.
- `help.shopify.com/.../shopify-payments/shopify-protect` redirects to the Shopify Payments hub.
- `help.shopify.com/en/manual/promoting-marketing/shopify-forms` redirects to a generic marketing index.
- `help.shopify.com/.../notifications/order-status-page` redirects to "Store notifications".

Also checked and deliberately not used: `shopify.com/plus` is live but is a sales page, not
a primary source, so linking it as a citation would be misleading.

### Dates deliberately not bumped

Same reasoning as the 09-17 run. No prose changed, so no `dateModified`, sitemap `lastmod`
or feed `lastBuildDate` was touched. Re-dating 68 posts on one afternoon would also look
exactly like the mass re-date that search engines discount. Every date on the site still
means what it says.

## Part 3 - For the owner

### 1. Two published dispatches are returning 404 on the live site

This is the one thing on the list that is costing something right now.

`blog.dugong.live` is serving the Aug 29 commit. Checked directly today:

- `how-to-fix-duplicate-skus-on-shopify.html` (Nº 117, written Sep 17): **404**
- `how-to-fix-shopify-shipping-rates-that-ignore-product-dimensions.html` (Nº 118, written Sep 18): **404**
- `how-to-track-product-expiry-dates-on-shopify.html` (Nº 116, Aug 29): loads fine
- the live `llms.txt` still tops out at the May 28 lead essay and the live sitemap's newest `lastmod` is Aug 29

So the local tree and the live site have been diverging for twenty days. Two finished
dispatches, yesterday's 73-file markup pass, and today's 68-file citation pass are all
sitting uncommitted: **77 modified files and 10 untracked files** against `dc01c14`. Local
`main` and `origin/main` are level, so nothing is stuck mid-push. The work simply has never
been committed.

Nothing is lost and nothing is broken. It just is not published. One commit and one push
puts twenty days of work live at once.

    git add -A && git commit -m "Nº 117-118 + SEO/GEO: verified primary-source citations" && git push

A cadence gap this long is worth avoiding for its own sake, separate from the two missing
posts. Sites that publish every day or two and then go quiet for three weeks get crawled
less often, and the recrawl lag is paid on the next post too, not just the ones that were
missed.

### 2. The three concurrent scheduled tasks, still unstaggered

Flagged on 09-17 and unchanged. The daily blog write, this GEO task and the QA task all
point at this folder and all fired within a second of each other on 09-17 despite cron
times 45 minutes apart. Today's run saw no collision, but that is still luck rather than
design. Staggering them by an hour, or chaining each to fire after the previous finishes,
is cheap insurance against one agent silently overwriting another's edits to index.html,
sitemap.xml, feed.xml or llms.txt.

### 3. Nine posts have no inbound link from any other post

Internal linking is otherwise healthy: 5.72 in-body links per post, and every post is
reachable from index.html, so none of these is a true orphan. But nine get no link from a
sibling post:

Nº 114, 115, 116, 117, 118, plus Nº 66, 85, 108, 110.

Five of those are just the newest five: posts link backward, so the recent ones have not
been cited yet, and that corrects itself. The other four are genuinely stranded and have
been for months. The durable fix belongs in the blog-run workflow: when a dispatch ships,
add one backlink to it from the most closely related older post. That costs one sentence
per publish and keeps the internal graph from thinning at the edges.

### Standing items, unchanged

4. **Delete the two rejected drafts** on a supervised run (standing since 08-02). They stay
   noindexed and excluded from every surface, so they cost nothing meanwhile.
5. **The llms-full converter fix at the blog-run workflow level** (standing since 08-23).
6. **The <= 160-character description check should be added to the blog-run skill**
   (standing since 08-25).
7. **The rest of the citation work.** This run linked the platform surfaces, which are the
   mechanical, verifiable half. The other half is the good half: the dated community
   threads, the named staff answers, the executive orders and the carrier tariff notices
   that these posts quote almost verbatim and still do not link. That needs a post-by-post
   pass with every URL opened and matched to the claim it supports, roughly a handful of
   posts per run. It is the single biggest GEO lever left.
8. **Every post shares one image.** `og-image.png` is the article image, the og:image and
   the twitter:image for all 71. A per-post image would help in Discover and in image
   search, and gives answer engines something to attach to the specific answer. Needs
   someone to make the images; no run can invent them.

## Commit

**68 files edited by this run, 1 file created (this report).** The working tree also holds
everything from the 09-17 run and Dispatches Nº 117 and Nº 118. No commit was made, per
scheduled-run convention, but see Part 3 item 1: this is the run where not committing
starts to cost something. Suggested message:

    SEO/GEO 2026-09-18: 112 verified primary-source citations + citation schema on 68 posts

## Verification method note

All counts recomputed from the files by script. FAQ parity checked question-and-answer,
entity-decoded and whitespace-normalized. Feed pubDate weekdays validated against the
calendar. Tag balance parsed on all 145 files. Every one of the 21 source URLs fetched this
run and its title matched against the entity before use; six candidates failed and were
dropped. After the edits: JSON-LD re-parsed on all 74 rendered pages, the full audit re-run
and still at zero defects, anchors checked for nesting and for placement inside headings,
quotes, code and blockquote (0 of each), and the `citation` arrays diffed against the body
anchors in both directions on all 68 posts. A full backup of all 145 HTML files was taken
before the first edit and the pass was restored and re-run once from that backup after the
quoted-placement rule was added. The live site was checked directly for Nº 116, Nº 117,
Nº 118, sitemap.xml and llms.txt. `.fuse_hidden*` files are mount artifacts, ignored per
convention.
