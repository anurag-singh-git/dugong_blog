# SEO / GEO report — 2026-07-03 (internal-link mesh completion pass)

**Mode:** automated scheduled task (autonomous; no user present)
**Scope:** technical SEO/GEO audit of the whole site + close the one open gap carried over from 2026-07-02

## What this run did

This was a maintenance/optimization pass, not a new-post run. The site was audited end to end,
the single open item flagged in the 2026-07-02 new-post run was fixed, and everything was re-verified.

The 2026-07-02 run shipped post Nº 74 ("The second order that arrives before the first ships,"
how-to-combine-multiple-orders-from-the-same-customer-on-shopify.html) and explicitly left the
back-link mesh for it to a follow-up pass: only 1 of 26 siblings linked to the new post. This run
completes that mesh and confirms the rest of the site is already optimized.

## Audit findings (before changes)

On-page SEO and GEO are already complete across all 27 posts:

- Every post has a unique title, meta description, canonical, OG + Twitter cards, and clean heading
  hierarchy (exactly one H1 each). Canonical and og:url match each post's filename with no mismatches.
- Every post carries full structured data: BlogPosting, FAQPage, and BreadcrumbList. All 26 how-to
  posts also carry HowTo schema; the lead essay (best-shopify-automations) correctly omits HowTo, as
  it is a listicle rather than a procedure. All JSON-LD blocks parse cleanly (28 files scanned,
  0 parse errors).
- sitemap.xml and feed.xml are valid XML, each covering all 28 URLs (homepage + 27 posts).
- sitemap, feed, llms.txt, and index.html all reference every post. No orphans, no missing entries.
- Zero broken internal `.html` links across the whole site.
- Pain-first landing stubs are correctly set to noindex + canonical + meta-refresh redirect and are
  excluded from the sitemap, so they capture felt-symptom queries without duplicate-content risk.
- robots.txt carries a full, explicit allow-list for the major AI/answer-engine crawlers (GPTBot,
  OAI-SearchBot, ClaudeBot, PerplexityBot, Google-Extended, Applebot-Extended, CCBot, Bytespider,
  Meta-ExternalAgent, and others) plus the sitemap reference. GEO crawler access is fully open.

**The one real gap:** internal link mesh incomplete for the newest post (Nº 74).

The site's established structure is a complete mesh: every post's "Read next" block links every
sibling. When Nº 74 was added on 2026-07-02, only 1 of 26 siblings (the order-change post) was updated
to link back to it. The other 25 posts still had 25-card blocks and did not link the newest post. That
starves the newest, hardest-to-rank page of internal link equity and slows its discovery/crawl, and it
breaks the uniform mesh the rest of the site relies on.

## Change made

Added the Nº 74 "Read next" card to all 25 posts that were missing it, inserted as the first card in
each post's `related-grid` (newest-first, matching how the order-change post was already wired). The
card markup is byte-for-byte the canonical card already used on the order-change post: same slug,
title ("The second order that arrives before the first ships"), dek, research tag, 9-min read-time,
and JUL 2 date.

Result: Nº 74 now receives internal links from all 26 siblings (was 1), and every post on the site
again has a uniform 26-card Read-next mesh.

Files changed: 25 post HTML files (the order-change post, which already linked Nº 74, and Nº 74 itself
were skipped). No changes to sitemap.xml, feed.xml, llms.txt, robots.txt, or index.html — those were
already consistent and correct (their current diff-vs-last-commit reflects the prior run's uncommitted
Nº 74 wiring, not this pass).

## Verification (all passing)

- Back-links to Nº 74: 26 of 26 siblings (was 1 of 26).
- Card counts: every one of the 27 posts now has exactly 26 cards in its Read-next block (uniform mesh).
- No self-links introduced in any post.
- All `<div>` tags balanced in every edited file.
- Zero broken internal `.html` links site-wide after the edit.
- JSON-LD still parses cleanly on all 27 posts + index (the edit only touched body HTML, not schema).
- Diff audit: the only content this pass added is the canonical Nº 74 card block; no other lines changed.
- User style preference honored: zero em/en dashes in the inserted card (verified programmatically).

## Open items left for review (not changed)

- Nothing outstanding on internal linking. The mesh is now complete and uniform.
- All changes are staged in the working tree only; no git commit or deploy was performed, consistent
  with prior runs.
