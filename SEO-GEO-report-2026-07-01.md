# SEO / GEO report — 2026-07-01 (audit pass)

**Scope:** blog.dugong.live — index + 25 posts + feed / sitemap / llms / robots / CNAME
**Mode:** automated scheduled run (autonomous, no user present)

## Result: full audit, everything green. No defects found, no changes made.

No new dispatches have shipped since the 06-30 fix pass (still 25 posts on disk, git working
tree clean). Every invariant the recurring audit checks is currently satisfied, so this run is a
verification-only pass. Nothing needed repair.

## What was checked (and passed)

**Content and meta**
- Post count: 25 on disk (24 June dispatches + the 2026-05-28 pillar essay).
- Meta descriptions: all 25 present, all unique, all inside the 146–162 house band (0 out of band),
  no em/en dashes.
- Titles: all 25 unique. H1: exactly one per post (25/25).
- Canonical, og:title, twitter:card present on every post (25/25).
- Image alt text: no `<img>` missing an alt attribute across posts or index.

**Internal link graph (the GEO backbone)**
- Complete graph confirmed: out-degree 24 / in-degree 24 uniform across all 25 posts.
- Every body `.related-grid` holds exactly 24 unique card anchors — no self-links, no duplicates.
- Zero broken internal `.html` links across posts and index.

**Structured data**
- All JSON-LD parses on all 25 posts and on index.html (0 parse failures).
- Full rich-result stack present per dispatch: BlogPosting, FAQPage, BreadcrumbList,
  SpeakableSpecification, Person, Organization, ImageObject, HowTo (with HowToStep), plus
  entity-grounding `Thing` nodes carrying `sameAs` links to Wikipedia (e.g. Shopify,
  business-process-automation) — a solid GEO signal for answer engines.

**Discovery and freshness assets**
- Coverage cross-check — disk vs sitemap vs feed vs llms.txt vs index.html: all five sets identical
  at 25 posts, zero drift.
- sitemap.xml: valid XML; every `<lastmod>` matches that post's `dateModified` exactly
  (0 mismatches across 25 posts).
- feed.xml: valid XML; lastBuildDate 30 Jun 2026 (correct — no new content since).
- llms.txt references all 25 posts and carries the sitemap line.
- robots.txt: `Allow: /` for `*` plus explicit allow for every major answer-engine crawler
  (GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot, Google-Extended, Applebot, Bingbot, CCBot,
  Amazonbot, Meta-ExternalAgent, DuckAssistBot and more); Sitemap line present.
- og-image.png, favicon.png, favicon.svg, apple-touch-icon.png all present. CNAME = blog.dugong.live.

**Homepage counters (consistency)**
- Ticker "24 NEW DISPATCHES THIS MONTH" (x2) matches the 24 posts with a June 2026 datePublished.
- Hero "ISSUE Nº 72" and archive "browse all 72 dispatches" agree with the newest dispatch (Nº 72,
  the pre-order post, datePublished 2026-06-30).

## Reviewed and intentionally not changed

- **Freshness timestamps (dateModified / sitemap lastmod / feed lastBuildDate):** no article body
  changed this run, so bumping any freshness signal would be false. Left as set by the last publish
  commits (keeps sitemap lastmod == dateModified at 0 mismatches).

## Recommendations (for a future run with a human in the loop)

1. **Automate back-link propagation and meta-length lint at publish time.** The two defects that
   recur at every publish (under-linked new posts and over-length meta descriptions) were absent
   this run only because no new post shipped. Adding both checks to the publish pipeline would
   retire them permanently.
2. **Person / Organization `sameAs` on posts.** Standing item. Posts ground topic entities via
   `Thing.sameAs` (Wikipedia), and index.html's Organization carries `sameAs: https://dugong.live`,
   but the author (Priya Singh, `Person`) and the per-post `Organization` node still lack verified
   social/profile URLs. Supplying real profile URLs would strengthen author/publisher entity
   grounding for answer engines. Not safe to invent in an autonomous run.

## Note

No files were modified this run (audit only). No git commit or deploy was performed, consistent
with prior runs.
