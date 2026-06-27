# SEO / GEO report — 2026-06-27 (audit pass)

**Scope:** blog.dugong.live — index + 21 posts + feed / sitemap / llms / robots / CNAME
**Mode:** automated scheduled run (autonomous, no user present)

## Result: full-surface audit, site is healthy, no defects, no changes made

The working tree was clean at start (last commit `b362954 "blogs"`, no staged or unstaged
changes since the 06-25 run). I ran a complete SEO/GEO sweep across every standing invariant
the site is supposed to hold. Every check passed. Unlike recent runs, there was no new-post
under-linking to repair, because no post has shipped since 06-25 and that run's audit already
completed back-link propagation. I made no edits: there was nothing broken to fix, and inventing
changes (touching dateModified, adding a fake search endpoint, fabricating social links) would
have removed signal rather than added it.

## What was checked (all green)

**Content and meta**
- Post count: 21 on disk (20 June dispatches + the 2026-05-28 pillar essay).
- Meta descriptions: all 21 present, all unique, all inside the 146–162 house band.
- Titles: all 21 unique. H1: exactly one per post (21/21).
- Canonical: present on every post (21/21). Twitter card + og:title: present on every post (21/21).
- `lang`, `charset`, and `viewport` present on posts.

**Internal link graph**
- In-degree is uniform at 20 for all 21 posts (every post is linked from all 20 siblings via the
  `.related-grid`). No orphans, no asymmetry.
- Zero broken internal `.html` links across the whole site.

**Structured data (the GEO backbone)**
- Every post carries the full rich-result stack: `BlogPosting`, `FAQPage` (Question/Answer),
  `BreadcrumbList`, `SpeakableSpecification`, `Person`, `Organization`, `ImageObject`, plus
  `HowTo`/`HowToStep` on 20 of 21 (the pillar essay intentionally omits HowTo).
- All JSON-LD parses on all 21 posts and on index.html. index.html carries `WebSite`, `Blog`,
  and per-card `BlogPosting` + `Person` graph.
- Author entity (`Priya Singh`, jobTitle "Commerce Research, Dugong") is linked to the
  `#organization` node via `worksFor`; Organization resolves to https://dugong.live with logo.

**Discovery and freshness assets**
- sitemap.xml: valid XML; every post's `<lastmod>` matches that post's `dateModified` exactly
  (0 mismatches across 21 posts). Homepage lastmod 2026-06-25.
- feed.xml: valid XML, 22 items, lastBuildDate Thu 25 Jun 2026.
- llms.txt: present, references all 21 posts, intro and publisher block intact.
- robots.txt: `Allow: /` for `*` plus explicit allow for every major answer-engine crawler
  (GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot, Google-Extended, Applebot, Bingbot, CCBot,
  Amazonbot, Meta-ExternalAgent, DuckAssistBot, cohere, YouBot, and more); Sitemap line present.
- og-image.png, favicon.png, favicon.svg, apple-touch-icon.png all present. CNAME = blog.dugong.live.

**Homepage counters (consistency)**
- Ticker "20 NEW DISPATCHES THIS MONTH" x2 matches the 20 posts with a June 2026 datePublished.
- Hero "ISSUE Nº 68" and archive "browse all 68 dispatches" agree with the newest dispatch.

## Coverage cross-check

Disk vs sitemap vs feed vs llms.txt vs index.html: all five sets identical, 21 posts, zero drift.

## Reviewed and intentionally not changed

- **dateModified / sitemap lastmod / feed lastBuildDate:** left as set by the 06-25 run. No post
  content changed today, so bumping any freshness timestamp would send a false "updated today"
  signal to crawlers and answer engines.
- **WebSite `SearchAction` (sitelinks searchbox):** not added. The site has no on-page search
  endpoint, so a `potentialAction` SearchAction would point at a URL that does not exist and would
  be invalid markup. Not worth a malformed-schema risk.

## Recommendations (for a future run with a human in the loop)

1. **Organization `sameAs`.** The `#organization` node has name, url, and logo but no `sameAs`
   array. Adding verified links to Dugong's own profiles (X, LinkedIn, GitHub, etc.) would
   strengthen entity grounding for answer engines. Left undone here on purpose: in an autonomous
   run I cannot verify the real handles, and pointing `sameAs` at a wrong or dead URL hurts the
   entity rather than helping it. This needs the real URLs supplied.

2. **Author `sameAs` / `url`.** Same idea for the `Person` node (Priya Singh). A real author
   profile URL would add an E-E-A-T signal that answer engines increasingly weigh. Also needs a
   verified URL.

3. **Automate back-link propagation at publish time.** Standing recommendation from prior runs:
   the publish pipeline already updates the hero Nº, the dispatch stat, the archive "browse all N"
   link, and the ticker, but does not yet insert the new post's card into every existing post's
   `.related-grid` on day zero. Doing that in the publish step would keep in-degree uniform from
   the moment a post ships and retire the recurring "new post under-linked" finding for good. It
   did not surface today only because no post shipped since the last audit.

## Note

No edits were made and no git commit or deploy was performed, consistent with prior runs. The
working tree remains clean.
