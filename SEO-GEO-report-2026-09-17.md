# SEO / GEO report — 2026-09-17

Scheduled autonomous run. Last SEO/GEO pass: 2026-08-29. Nineteen days have elapsed and
the tree is unchanged since commit `dc01c14` (Aug 29, 17:18). This run therefore did two
things: a full re-audit including Dispatch Nº 116, which was published forty minutes
*after* the 08-29 audit ran and so had never been checked, and a round of substantive
GEO/SEO improvements, the first content-level changes any of these runs has made since
the baseline reached zero defects.

## Part 1 — Audit: zero defects

Every check recomputed from the files today, nothing carried forward.

Inventory: **141 HTML files** = 72 rendered (69 wired posts + index.html + 2 noindexed
rejected drafts) and 69 redirect stubs, plus sitemap.xml, feed.xml, llms.txt,
llms-full.txt, robots.txt, CNAME. Dispatches Nº 48 through Nº 116, contiguous, no
duplicates. Nº 116 is correctly wired everywhere: carded on index (as `card card-tall`),
in the sitemap, the feed, llms.txt, llms-full.txt, with a matching stub, and the hero
ticker reads ISSUE Nº 116.

| Check | Result |
|---|---|
| JSON-LD parses, all 72 rendered pages | 72 / 72, 0 errors |
| FAQ parity: visible == FAQPage JSON, questions AND answers, entity-decoded | 69 / 69 |
| FAQ counts: 5 on every post; 345 total | 69 / 69 |
| canonical == og:url == filename; og/twitter sets complete incl. og:image w/h/alt | 72 / 72 |
| exactly one h1; lang; viewport; img alt coverage | 72 / 72 |
| duplicate titles / meta descriptions; descriptions <= 160 chars | 0 / 0 / PASS |
| broken internal links across all rendered pages | 0 |
| author @id resolves to `#priya-singh` on all 69 posts | PASS |
| dateModified == article:modified_time == sitemap lastmod; future dates | 0 mismatches / 0 |
| sitemap.xml: valid XML, 70 locs (69 posts + root), 0 dupes, 0 ghosts | PASS |
| feed.xml: valid XML, 70 items, unique guids, weekday-correct pubDates, no future dates | PASS |
| llms.txt / llms-full.txt: all 69 posts, 0 ghosts, 0 dupes, fences balanced, no raw dashes | PASS |
| stubs: 69, bijective onto wired posts, noindexed, targets live | PASS |
| index: 70 BlogPosting nodes, WebSite + Organization + Person + Blog entities | PASS |
| rejects (2): noindexed, absent from sitemap / feed / llms / llms-full / index | PASS |
| tag balance, all 141 HTML files | 0 problems |
| live site reachable; robots.txt and Nº 116 serving correctly | PASS |

## Part 2 — Improvements applied

The technical baseline has been at zero defects for several runs, so this run moved past
defect repair into the gaps that were never closed. Four changes, 73 files.

### 1. Machine-readable dates (`<time datetime>`) — 207 elements

Publication dates were rendered as plain text (`JUN 11, 2026`, `AUG 29`) with no
machine-readable value anywhere in the visible DOM. The dates existed only in meta tags
and JSON-LD. Every visible date is now wrapped in a `<time datetime="YYYY-MM-DD">`
element:

- 71 post publication dates in `.article-meta`
- 72 card dates on index.html (`<span class="card-date">` became
  `<time class="card-date" datetime="...">`)
- 1 lead-essay date on index.html

Rendering is unchanged: `<time>` is inline like `<span>`, the class is preserved, and no
stylesheet rule in the codebase is `span`-qualified. Verified: 0 unbalanced or nested
`<time>` tags across all 141 files.

### 2. Visible "UPDATED" freshness signal — 63 posts

`dateModified` was published in `article:modified_time` and in the BlogPosting JSON-LD,
but nowhere a reader or a snippet-generating model could see it. 63 of the 71 posts carry
a modified date later than their publication date, in some cases by two months, and none
of them said so on the page. Each of those 63 now ends its meta row with, for example,
`UPDATED AUG 7, 2026`, wrapped in its own `<time>` element.

This surfaces data the site was already publishing; nothing was invented and no date was
changed. Recency is one of the few signals answer engines weigh directly when choosing
between two pages that say the same thing, and Google's own guidance is that a visible
date consistent with the structured-data date is what earns the date in the SERP.

### 3. Organization logo corrected — 72 files

`publisher.logo` pointed at `og-image.png`, the 1200x630 social banner. Google's
Organization guidance expects an actual logo image, and a 1.9:1 banner is not one: it is
what gets cropped or dropped in a knowledge panel. All 72 JSON-LD blocks now point at
`apple-touch-icon.png` (180x180, the square Dugong mark, comfortably over the 112x112
minimum) with a `caption` of "Dugong". `og-image.png` remains the article `image` and the
`og:image`, which is correct for both.

### 4. robots.txt — 7 crawler tokens added

Re-verified against current 2026 crawler references rather than carrying the 08-25/08-29
verdict forward. Every previously listed agent is still current. Seven tokens named in
the references were absent and are now explicitly allowed: `meta-externalfetcher`,
`FacebookBot`, `omgilibot`, `iaskspider`, `img2dataset`, `Webzio-Extended`,
`SemrushBot-OCOB`. The blanket `User-agent: * Allow: /` already covered them, so this is
belt-and-braces for crawlers that only read their own named block, which several do. The
site's GEO stance remains maximal citation eligibility: no training/search split.

### Dates deliberately not bumped

All four changes are markup and structured-data corrections, not content revisions.
Bumping `dateModified`, sitemap `lastmod`, or the feed's `lastBuildDate` for a markup
pass would be a false freshness claim, so none were touched. Every date on the site still
means what it says.

## Part 3 — For the owner

### 1. Three scheduled tasks are writing to this folder at the same time

Mid-run, at 16:10 UTC, two new files appeared in the folder that this run did not create:
`how-to-fix-duplicate-skus-on-shopify.html` and its stub `the-sku-two-products-share.html`.
That is the daily blog task publishing Dispatch Nº 117 while this GEO run was still
editing the same tree.

The task list explains it. Three tasks are active, all created 2026-09-09, all pointed at
this folder: the daily blog write (cron 11:00 Europe/Paris), this GEO task (11:30), and
the QA task (11:45). Their cron times are 45 minutes apart, but today all three fired
within one second of each other, at 16:00:25 UTC. So the blog agent and this agent spent
the run writing to the same files, and the QA agent was running too.

Nothing was lost this time. This run's index.html edits were verified intact after the
new post landed, because the blog run appends rather than regenerating. But that is luck,
not design: two agents doing read-modify-write on index.html, sitemap.xml, feed.xml and
llms.txt at the same time will eventually have one silently overwrite the other, and the
loser will be whichever wrote first. **Staggering the three tasks by an hour or more, or
chaining them so each fires only after the previous finishes, is worth doing before it
costs a publish.**

A related note on the gap this run opened with: there was no new dispatch between Nº 116
on Aug 29 and today, nineteen days, against a prior cadence of roughly one every one to
two days, and no `blog-run-*.md` or `QA-report-*.md` from any run in that window. Today's
runs are the first of the three to touch the folder since Sept 9. The likeliest
explanation is simply that these runs could not reach this computer on those days, since
a scheduled run only touches the folder while the desktop app is open and online. The
tasks themselves are clearly working. Still worth knowing that a three-week publishing gap
happened without anything announcing it, because cadence is what keeps a site in the crawl
rotation.

### Dispatch Nº 117 is not covered by the audit above

It landed after this run's audit had completed, exactly as Nº 116 did on 08-29. Its
wiring into index.html, sitemap.xml, feed.xml, llms.txt and llms-full.txt, and its own
FAQ parity, canonical, and structured data, are unverified by this run and will be picked
up by the next one. It also will not carry the `<time>` and UPDATED markup this run added
to the other 71 posts, since the blog-run template has not been changed; the next GEO run
will bring it in line.

### 2. The citation gap, the biggest remaining GEO lever

The posts are unusually well sourced in prose: dated Shopify community threads, named
staff answers, executive orders, specific statistics. Not one of those sources is linked.
Across all 69 posts the only outbound non-Dugong links are to Google Fonts.

For generative engines this is the most valuable thing left undone. Models weigh
verifiable sourcing heavily when deciding what to cite, and a page that links the primary
source it quotes is materially more likely to be surfaced than one that only mentions it.
The classic-SEO benefit is the same argument in E-E-A-T terms.

This was not attempted on this run, and deliberately so: it needs each URL verified
against the claim it supports, and a scheduled run with nobody watching is exactly the
wrong place to be generating links to documents it has not opened. A wrong citation is
worse than no citation. The right shape for it is a supervised pass, or a dedicated
scheduled task that handles a handful of posts per run and fetches every URL before it
writes it. Starting with the Shopify help-centre and community URLs, which are stable and
easy to verify, would cover most of what the posts lean on.

### Standing items, unchanged

3. **Delete the two rejected drafts** on a supervised run (standing since 08-02):
   `how-to-automatically-follow-up-on-unpaid-draft-order-invoices-on-shopify.html` and
   `how-to-send-payment-reminders-for-unpaid-draft-orders-on-shopify.html`. They remain
   noindexed and excluded from every surface, so they cost nothing meanwhile. Deletion in
   a connected folder needs an explicit permission grant, which is a supervised action.
4. **The llms-full converter fix at the blog-run workflow level** is still outstanding
   (standing since 08-23). All 69 current entries are clean; the next publish run will use
   the unpatched converter.
5. **The <= 160-character description check should be added to the blog-run skill**
   (standing since 08-25).

## Commit

**73 files edited by this run, 1 file created (this report).** The working tree also holds
Dispatch Nº 117 and its stub from the concurrent blog run. Nothing on blog.dugong.live
reflects any of it until pushed. No commit was made, per scheduled-run convention.
Suggested message:

    SEO/GEO 2026-09-17: machine-readable dates, visible updated dates, logo schema fix, robots.txt

Two housekeeping items before you commit. A stale empty `.git/index.lock` sits in the
repo: every git command run through this folder mount leaves one behind, because a
scheduled session cannot delete files. Remove it if git complains. And this run created a
`_to_delete/` folder holding one such stale lock, for the same reason; it can be deleted
outright.

## Verification method note

All counts recomputed from the files by script; FAQ parity checked question-and-answer,
entity-decoded and whitespace-normalized; feed pubDate weekdays validated against the
calendar; tag balance parsed on all 141 files; the full audit re-run after every edit and
still at zero defects; JSON-LD re-parsed on all 72 rendered pages after the logo change;
`<time>` balance and nesting checked across all 141 files; the live site spot-checked for
robots.txt and the Nº 116 page. The square logo was inspected visually before being
adopted as `publisher.logo`. `.fuse_hidden*` files are mount artifacts, ignored per
convention.
