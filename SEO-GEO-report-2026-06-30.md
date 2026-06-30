# SEO / GEO report — 2026-06-30 (audit + fix pass)

**Scope:** blog.dugong.live — index + 25 posts + feed / sitemap / llms / robots / CNAME
**Mode:** automated scheduled run (autonomous, no user present)

## Result: fixed the recurring under-linking on three new posts and trimmed three over-length meta descriptions; everything else green

Since the last audit (06-28) three dispatches shipped without being fully wired into the site:
Nº 70 ("The price change you make one product at a time", 06-28), Nº 71 ("The payout that never
matches your sales", 06-29), and Nº 72 ("The pre-order that holds your whole order hostage", 06-30).
Each shipped with the same two defects the prior runs keep flagging at publish time: an over-length
meta description, and missing back-link cards in the existing posts' `.related-grid`. I fixed both.
No freshness timestamps were bumped (see "intentionally not changed").

## Defect 1: three new posts were under-linked (66 missing internal edges)

The site's standing invariant is a complete internal link graph — every post links to every other
via the body `.related-grid`. Before this run the 22 established posts were complete among
themselves, but the three new posts had not been propagated:

- `the-preorder-that-holds-your-order-hostage.html`: in-degree 1 (should be 24)
- `the-payout-that-never-matches-your-sales.html`: in-degree 2 (should be 24)
- `the-price-change-you-make-one-product-at-a-time.html`: in-degree 3 (should be 24)

**Fix:** inserted each new post's existing card block (the same `<a class="card">` markup already
used for it elsewhere, so title, dek, read time, date and author are house-consistent) into the
`.related-grid` of every post that was missing it — 66 card insertions across 24 files. The three
new posts' own grids were also completed so they link all 24 siblings.

**Post-fix graph:** out-degree and in-degree are now both uniform at 24 across all 25 posts. Every
body grid holds exactly 24 unique card anchors, no self-links, no duplicates. Zero broken internal
`.html` links.

## Defect 2: three new posts shipped with over-length meta descriptions

House band is 146–162 characters (so search snippets and answer-engine citations are not truncated).
The three new posts were outside it:

- price-change: 196 chars → trimmed to 160
- payout: 245 chars → trimmed to 160
- preorder: 304 chars → trimmed to 161

**Fix:** rewrote each `description` and the matching `twitter:description` (kept identical, as these
three posts already paired them) to a single band-length line that keeps both the pain and the
payoff, with no em or en dashes:

- payout: "Shopify nets each payout down by fees, refunds, and reserves, then pays in a batch, so it
  never matches your sales. The AI playbook that ties payouts to orders."
- preorder: "Shopify has no real pre-order, ship date, or cart split, so an in-stock item gets held
  by a pre-order in the same cart. The AI playbook that ships what is ready."
- price-change: "Shopify's bulk editor caps at 50 products, has no percentage math, and Flow cannot
  reprice, so you retype prices by hand. The AI playbook that reprices by rule."

The longer `og:description` and JSON-LD `description` fields were left untouched (og has no
truncation penalty; the house pattern keeps it expansive).

## Verification (post-fix re-sweep)

- **Meta descriptions:** all 25 present, all unique, all now inside 146–162 (0 out of band).
- **Link graph:** out=24 / in=24 uniform for all 25 posts; 24 unique cards per grid; 0 broken links.
- **JSON-LD:** all blocks on the three edited new posts, the 21 propagated posts, and index.html
  still parse; no schema field was changed.
- **No dash regressions:** the three rewritten descriptions contain zero em/en dashes.

## Site-wide audit (everything else clean)

**Content and meta**
- Post count: 25 on disk (24 June dispatches + the 2026-05-28 pillar essay).
- Titles: all 25 unique. H1: exactly one per post (25/25).
- Canonical, og:title, and twitter:card present on every post (25/25).
- Image alt text: no `<img>` missing an alt attribute across posts or index.

**Structured data (the GEO backbone)**
- Every post carries the full rich-result stack: `BlogPosting`, `FAQPage`, `BreadcrumbList`,
  `SpeakableSpecification`, `Person`, `Organization`, `ImageObject`, plus `HowTo` on the dispatches
  (the pillar essay intentionally omits HowTo). All JSON-LD parses on all 25 posts and on index.html.

**Discovery and freshness assets**
- Coverage cross-check — disk vs sitemap vs feed vs llms.txt vs index.html: all five sets identical
  at 25 posts, zero drift.
- sitemap.xml: valid XML; every post's `<lastmod>` matches that post's `dateModified` exactly
  (0 mismatches across 25 posts).
- feed.xml: valid XML. llms.txt references all 25 posts.
- robots.txt: `Allow: /` for `*` plus explicit allow for every major answer-engine crawler (GPTBot,
  OAI-SearchBot, ClaudeBot, PerplexityBot, Google-Extended, Applebot, Bingbot, CCBot, and more);
  Sitemap line present.
- og-image.png, favicon.png, favicon.svg, apple-touch-icon.png all present. CNAME = blog.dugong.live.

**Homepage counters (consistency)**
- Ticker "24 NEW DISPATCHES THIS MONTH" x2 matches the 24 posts with a June 2026 datePublished.
- Hero "ISSUE Nº 72" and archive "browse all 72 dispatches" agree with the newest dispatch
  (the pre-order post, datePublished 2026-06-30).

## Reviewed and intentionally not changed

- **dateModified / sitemap lastmod / feed lastBuildDate:** left as set by the publish commits. The
  back-link cards added today grow each post's related-links footer but do not change the article
  body, so bumping a freshness timestamp on 24 posts would send a false "all updated today" signal.
  Leaving them keeps sitemap lastmod == dateModified (still 0 mismatches).
- **twitter:description on older posts:** several established posts intentionally carry a slightly
  different twitter:description from their meta description (both in reasonable length). This is
  long-standing house variation, not a regression, so I did not mass-rewrite them.

## Recommendations (for a future run with a human in the loop)

1. **Automate back-link propagation and meta-length lint at publish time.** This run's two defects —
   under-linked new posts and over-length meta descriptions — are the same pair every recent audit
   has had to repair by hand. Adding both to the publish pipeline (insert the new card into every
   sibling grid on day zero; reject any meta description outside 146–162) would retire both as
   recurring findings.
2. **Organization / author `sameAs`.** Standing item: the `#organization` and `Person` (Priya Singh)
   nodes still have no `sameAs` array. Verified profile URLs would strengthen entity grounding for
   answer engines. Needs real URLs supplied — not safe to invent in an autonomous run.

## Note

All changes are staged in the working tree only; no git commit or deploy was performed, consistent
with prior runs.
