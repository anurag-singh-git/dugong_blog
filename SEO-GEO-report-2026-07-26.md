# SEO / GEO report, 2026-07-26 (48 files edited)

**Scope:** Scheduled full-site SEO/GEO pass, run after today's publish run (Dispatch Nº 92,
"The supplier feed that zeroed your catalog"). The site now carries 91 HTML files: 45 canonical
posts plus 45 pain-point redirect stubs and index.html. This pass audited every page and every
distribution surface, found four defects, fixed all four, and verified the result.

## Issues found and fixed

### 1. The new post was invisible to every crawler that does not read index.html (fixed)

Dispatch Nº 92, `how-to-sync-supplier-inventory-feeds-to-shopify.html`, was published today and
wired into index.html, but was **absent from sitemap.xml, feed.xml, and llms.txt**. This is a
worse failure mode than the orphaning seen in prior runs. Those three files are the primary
discovery path for the crawlers that matter most here:

- **sitemap.xml** is what Googlebot and Bingbot poll for new URLs. A post missing from it is
  discovered only when a crawler happens to re-fetch a linking page.
- **feed.xml** is what syndication and several AI crawlers read to detect fresh content.
- **llms.txt** is the file GPTBot, ClaudeBot, PerplexityBot and friends use to understand what
  the site covers. A post missing from it does not exist as far as an answer engine's
  site-level model of this domain is concerned.

All three were repaired:

| Surface | before | after |
|---|---|---|
| sitemap.xml locs | 45 | 46 |
| feed.xml items | 45 | 46 |
| llms.txt post entries | 44 / 45 | 45 / 45 |

The feed item reuses the post's own JSON-LD `description` rather than a hand-written summary, so
it cannot drift from the article. The llms.txt entry follows the house pattern: a descriptive
multi-paragraph entry covering the native gap, the failure modes, and what the playbook does,
not a bare link. Sitemap entry inserted after the homepage in newest-first order with the
site's standard `monthly` / `0.9` values.

### 2. The new post was fully orphaned in the internal mesh (fixed)

Nº 92 carried **zero** inbound links from sibling posts while its peers sit at 25 to 44. Only
index.html and its own redirect stub pointed at it.

The site's internal-link convention is a near-total mesh, and that graph is what drives crawl
priority, internal PageRank flow, and the topical-cluster signal answer engines use to decide
which page on a domain is authoritative for a query. A post at zero is the single largest
discovery drag available.

Added a `READ NEXT` card for Nº 92 to the related grid of all 44 sibling posts, inserted at the
head of each grid per the newest-first convention, skipping the self-link.

| | before | after |
|---|---|---|
| Nº 92 inbound links | 2 | 46 |
| Nº 92 mesh links (from sibling posts) | 0 | 44 |
| site-wide inbound min / avg / max | 2 / 37.2 / 46 | 27 / 38.2 / 46 |
| mesh-only min / avg / max | 0 / 35.2 / 44 | 25 / 36.2 / 44 |
| orphans | 1 | 0 |

Card chips (read time `PT10M`, tag `research`, date `JUL 26`, author `P. Singh`) were taken from
the target post's own JSON-LD rather than hand-copied, so they cannot drift.

### 3. Meta description exceeded the 160-character limit (fixed)

Every other post sits between 145 and 160 characters. Nº 92 ran to 205 and would have been
truncated mid-clause in the SERP, cutting the "AI playbook" half that drives the click:

| | before | after |
|---|---|---|
| supplier feed (Nº 92) | 205 chars | 155 |

The rewrite keeps the problem-then-playbook shape of the house pattern and lands the playbook
clause inside the visible window. `og:description` and `twitter:description` are separate fields
on this site and are not length-constrained, so they were left alone.

### 4. Sitemap `lastmod` refreshed

45 files were edited by this pass, so all 46 `lastmod` values now read `2026-07-26`. Sitemap and
feed both re-validated as well-formed XML. `lastBuildDate` on the feed advanced to match.

## Baseline structural audit (post-fix, all passing)

| Check | Result |
|---|---|
| JSON-LD parse, all 91 files | 0 errors |
| broken internal links site-wide | 0 |
| canonical matches filename | 0 issues |
| stub redirects (noindex + canonical + meta-refresh) | 45 / 45 PASS |
| exactly one h1 per page | 46 / 46 |
| og: and twitter: meta on every page | 46 / 46 |
| duplicate titles / duplicate meta descriptions | 0 / 0 |
| meta descriptions present and 160 chars or under | 46 / 46 |
| duplicate READ NEXT cards introduced | 0 |
| self-links in body or READ NEXT grids | 0 |
| sitemap.xml: 46 locs, 0 dangling, valid XML | PASS |
| feed.xml: 46 items, 0 duplicate guids, valid XML | PASS |
| llms.txt post coverage | 45 / 45 |
| robots.txt AI-crawler allowances (24 agents incl. GPTBot, ClaudeBot, OAI-SearchBot, PerplexityBot, Google-Extended, CCBot, Applebot-Extended, DuckAssistBot, Amazonbot) | intact |
| img alt attributes | 0 missing |
| HTML div and anchor balance across edited files | 45 / 45 |

## GEO audit (all passing)

| Check | Result |
|---|---|
| `@graph` completeness per post (BlogPosting + BreadcrumbList + FAQPage) | 45 / 45 |
| HowTo schema with enumerated steps | 44 / 44 posts (hub essay exempt, correctly) |
| FAQPage schema questions matched by visible on-page `.faq-q` content | 45 / 45, zero count mismatches |
| `speakable` SpeakableSpecification present | 45 / 45 |
| author / publisher / headline / wordCount / inLanguage on every BlogPosting | complete |
| `dateModified` vs `article:modified_time` agreement | 0 mismatches |
| site-level WebSite + Organization + Blog graph on index | present, with `sameAs` |
| llms.txt: descriptive multi-sentence entry per post | 45 / 45 |
| `about` entity linking on Nº 92 (Shopify, inventory management, SKU, dropshipping, EDI) | 5 entities with `sameAs` |

Google requires FAQPage markup to correspond to content a visitor can actually see, and that
correspondence holds exactly on all 45 posts. Answer engines get the same questions in both
extractable schema and readable prose, which is the configuration that gets cited.

## Checked and deliberately left alone

- **`dateModified` not bumped on meshed posts.** Adding one related-content card to a 40-card
  grid is not a substantive content revision. Bumping the article's modified date for boilerplate
  would misrepresent freshness to crawlers and answer engines. Sitemap `lastmod`, which describes
  the page rather than the article, was bumped instead.
- **Title separator encoding** (`&mdash;` entity on newer posts, literal character on older ones)
  renders identically. No SEO or GEO effect.
- **Titles over 70 chars** from the "Dugong Field Notes" brand suffix, keyword portion
  front-loaded. Consistent with prior rulings.
- **Hub ItemList at 4 items**, matching its editorial content, per prior ruling.
- **Template-level em/en dashes** (title separator, RSS link title, CSS comments) remain outside
  house-style enforcement. Zero em or en dashes in any content authored this run.

## Recommendations for the owner

1. **The publish run has regressed, and this is now urgent.** Prior passes back-filled *links*
   for a new post. Today's run left the post out of the sitemap, the feed, and llms.txt as well.
   That is a distribution failure, not a polish item: had this pass not run, Nº 92 would have
   been effectively unindexed. Wiring sitemap, feed, llms.txt, and the sibling mesh at publish
   time is the single highest-value change available to this pipeline, and it is mechanical.
2. **Reconsider blanket `lastmod` bumps.** Full-site bumps on most days is a pattern Google can
   learn to discount. Worth restricting to substantive content edits once the publish run does
   its own wiring.
3. **FAQ depth remains the largest GEO opportunity.** Posts carry three to four questions each.
   Answer engines cite the page covering the long tail of a question; five or six per post would
   materially widen the citable surface. Needs per-post editorial judgement about which questions
   merchants actually ask, so it is not appropriate for an autonomous pass.
4. **Undeployed working tree.** Today's publish run and this pass are both uncommitted. Nothing
   on blog.dugong.live reflects any of it until committed and pushed. No commit or push was made,
   consistent with scheduled-run convention.

## Conclusion

Four defects, all on the newest content and all material: a post missing from all three
distribution surfaces, a fully orphaned post, and a truncating meta description. All fixed and
verified. Every post now sits at 25 or more mesh links, sitemap and feed and llms.txt are
complete and current, and all schema surfaces validate. **48 files edited: 44 posts meshed, the
new post's meta description rewritten, plus sitemap.xml, feed.xml, llms.txt and this report.**
