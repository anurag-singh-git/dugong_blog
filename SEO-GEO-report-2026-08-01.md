# SEO / GEO report, 2026-08-01 (50 files edited)

**Scope:** Scheduled full-site SEO/GEO pass, the first since 07-31. In between, the 07-31 publish
run landed Dispatch Nº 96, "The pickup order that should have shipped"
(`how-to-change-a-shopify-order-from-local-pickup-to-shipping.html`), plus its pain-point stub.
The site now carries 99 HTML files: 50 rendered pages (49 posts plus index.html) and 49 redirect
stubs. This pass audited every page and every distribution surface, found the launch state of
Nº 96 fully clean, and then closed one long-standing entity-graph gap across all 49 posts.

## Headline: the publish template is now defect-free, including the mesh

The 07-31 report's recommendation #1 asked the publish step to insert new posts into the sibling
READ NEXT mesh at publish time. The 07-31 publish run did exactly that: Nº 96 launched with 49
inbound links from rendered pages (index plus all 48 siblings), a complete four-node schema, a
156-character meta description, hub-graph entry referencing `#priya-singh` by `@id`, and full
coverage on sitemap, feed, llms.txt, and every index surface (hero, ticker at 24 for July, card
grid with exactly one card-tall, topic cloud). Every defect class that has ever recurred at
publish time (over-length descriptions, incomplete hub entries, orphaned launches, stale
homepage counters) arrived closed. Recommendation #1 is retired.

## Improvement made: post-level author entities now resolve to `#priya-singh`

With zero defects to fix, this pass spent its budget on the entity-consolidation gap the audits
surfaced: every post's `BlogPosting.author` was an inline Person object with `name`, `jobTitle`,
and `worksFor`, but **no `@id`**. The consolidated Person node at
`https://blog.dugong.live/#priya-singh`, which carries the full `knowsAbout` list and
`worksFor` reference, lives in the index graph, and the hub's 48 `blogPost` entries reference it
by `@id`. The posts themselves never did, so a crawler or answer engine merging entities across
pages had no machine-readable signal that the author of any individual post is the same Priya
Singh entity the site defines. This is the same defect class as the hub-graph author
consolidation of 07-28, one level down.

Fix: added `"@id": "https://blog.dugong.live/#priya-singh"` to the author object on all 49
posts (48 dispatches plus the pillar essay, all bylined Priya Singh; the pinned Aanya Rao essay
lives in the index graph and keeps its distinct inline Person, per the standing 07-31 ruling).
The inline `name`, `jobTitle`, and `worksFor` properties were deliberately kept alongside the
`@id`, so each post remains self-contained while consumers that merge by `@id` can now unify all
49 author nodes with the site-level entity.

| | before | after |
|---|---|---|
| posts whose author node carries the `#priya-singh` `@id` | 0 / 49 | 49 / 49 |
| author blocks byte-identical across posts | yes | yes (single deterministic replacement) |

The edit was a single exact-string replacement, applied only where it occurred exactly once per
file (49 / 49), and JSON-LD re-parsed clean on every page afterward. Zero em or en dashes
introduced.

### Housekeeping: sitemap `lastmod`

All 49 posts were genuinely edited, so their `<lastmod>` values were bumped to 2026-08-01.
index.html was not touched and keeps 2026-07-31. Per-post `dateModified` was deliberately not
bumped: a schema-annotation change is metadata, not a content revision, same ruling as the
07-31 mesh insert.

## Baseline structural audit (post-fix, all passing)

| Check | Result |
|---|---|
| JSON-LD parse, all 50 rendered pages | 0 errors |
| broken internal hrefs, absolute self-domain links, stub refresh targets | 0 |
| canonical present, matches filename, equals og:url | 50 / 50 |
| stub redirects (noindex + canonical + live meta-refresh target) | 49 / 49 PASS |
| exactly one h1 per page | 50 / 50 |
| og: and twitter: meta, og:image, `lang`, img alt | 50 / 50 complete |
| duplicate titles / duplicate meta descriptions | 0 / 0 |
| meta descriptions present and 160 chars or under | 50 / 50 |
| tag balance, all 99 files | balanced |
| sitemap.xml: 50 locs, 0 dupes, 0 ghosts, valid XML, lastmod ≥ datePublished | PASS |
| feed.xml: 50 items, 0 duplicate guids, valid XML, lastBuildDate = newest item (Jul 31) | PASS |
| llms.txt post coverage | 49 / 49 |
| orphaned posts | 0 |

## GEO audit (post-fix, all passing)

| Check | Result |
|---|---|
| `@graph` per post (BlogPosting + BreadcrumbList + FAQPage) | 49 / 49 |
| HowTo schema with enumerated steps | 48 / 48 (pillar essay exempt, correctly) |
| FAQPage questions match visible `.faq-q` text | 49 / 49, exact string match |
| `speakable`, `about`, `mainEntityOfPage`, `image` on every post | 49 / 49 each |
| post author nodes resolve to `#priya-singh` by `@id` | 49 / 49 (was 0 / 49) |
| `dateModified` vs `article:modified_time` agreement | 0 mismatches |
| site-level graph (WebSite + Organization + Person + Blog), `@id` refs resolve | complete |
| hub `blogPost` entries fully populated | 50 / 50 |
| robots.txt AI-crawler allowances | 33 agents, sitemap referenced, unchanged from 07-28 |

## Checked and deliberately left alone

- **FAQ depth at exactly 3 per post.** Still the largest untapped GEO surface; still needs
  per-post editorial judgement an autonomous pass should not invent. Carried forward.
- **Author pages** (`/authors/priya-singh.html`). Considered building one this pass, since the
  recommendation has been carried since 07-28. Decided against doing it autonomously: it means
  authoring visible biographical content and choosing `sameAs` targets that do not currently
  exist, both owner calls. The `@id` consolidation done this pass delivers the
  machine-readable half of that recommendation (entity unification) without inventing a page;
  what remains for the owner is the human-readable half.
- **Pinned essay's 14-min chip vs 893 wordCount**, title lengths over 70 chars from the brand
  suffix, template-chrome `&mdash;` entities and CSS-comment dashes: all standing rulings,
  unchanged.
- **robots.txt** untouched; the 33-agent allowance list still reflects the crawler landscape as
  of this pass.
- Stray `.fuse_hidden*` files in the repo root are mount artifacts, untouched.

## Recommendations for the owner

1. **FAQ depth** remains the highest-value GEO opportunity: five or six questions per post would
   materially widen the citable surface. Worth a dedicated editorial session.
2. **Author page** for Priya Singh (and arguably Aanya Rao): the entity graph now unifies
   cleanly by `@id`, but the Person URL still points at the homepage. A real profile page with
   owner-chosen `sameAs` links would complete the E-E-A-T story. Human-readable half only;
   the schema half closed this pass.
3. **Undeployed working tree.** Everything since the 07-28 deploy state, now including the 07-31
   publish and this pass's 50 edits, remains uncommitted. Nothing on blog.dugong.live reflects
   any of it until committed and pushed. No commit or push was made, consistent with
   scheduled-run convention.

## Conclusion

First SEO/GEO pass on record to find zero defects: the 07-31 publish run executed every surface
correctly, including the sibling mesh that was the last inconsistently handled step. The pass
therefore closed the oldest open schema gap instead, unifying all 49 post author nodes with the
site-level `#priya-singh` entity by `@id`, then re-verified the full audit matrix clean.

**50 files edited: 49 posts (author `@id` consolidation), sitemap.xml (lastmod), and this
report.**
