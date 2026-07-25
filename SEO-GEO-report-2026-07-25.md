# SEO / GEO report, 2026-07-25 (mesh pass, 45 files edited)

**Scope:** Scheduled full-site SEO/GEO pass, run after today's publish run (Dispatch Nº 91,
"The discount code that leaked to a coupon site"). The site now carries 89 HTML files: 44
canonical posts plus the hub essay, 44 pain-point redirect stubs, and index.html. This pass
audited every page and every distribution surface, found two real defects, fixed both, and
verified the result.

## Issues found and fixed

### 1. The two newest posts were effectively orphaned (fixed)

The site's internal-link convention is a near-total mesh: an established post carries 26 to 44
inbound links from siblings. Nº 90 (duplicate orders, published 07-24) and Nº 91 (discount code
abuse, published 07-25) each had **2**. The publish runs wire the index card and one reciprocal
sibling card and leave the rest to this pass, which is exactly the gap.

Two posts sitting at 2 inbound links while their peers sit at 37 is the single largest ranking
and discovery drag on the site. Crawl priority, internal PageRank flow, and the topical-cluster
signal that answer engines use to decide which page on a domain is authoritative for a query
all key off that graph.

Added a `READ NEXT` card for each new post to the related grid of every other post, skipping
self-links and the two grids that already carried one. **43 post files edited.**

| | before | after |
|---|---|---|
| Nº 90 inbound links | 2 | 44 |
| Nº 91 inbound links | 2 | 44 |
| site-wide inbound min / avg / max | 2 / 35.1 / 44 | 26 / 37.0 / 44 |
| orphans | 0 | 0 |

Card chips (read time, publish date, tag, author) were generated from each target post's own
JSON-LD rather than hand-copied, so they cannot drift from the source.

### 2. Two meta descriptions exceeded the 160-character limit (fixed)

Every other post on the site sits between 145 and 160 characters. The two newest ran long and
would have been truncated mid-sentence in the SERP, losing the click-driving second clause:

| Post | before | after |
|---|---|---|
| duplicate orders (Nº 90) | 212 chars | 160 |
| discount code abuse (Nº 91) | 202 chars | 153 |

Both rewrites keep the problem-then-playbook shape of the house pattern and land the "AI
playbook" clause inside the visible window. `og:description` and `twitter:description` are
separate fields on this site and are not length-constrained, so they were left alone.

### 3. Sitemap `lastmod` refreshed

41 tracked posts plus the 2 untracked new ones were edited by the mesh, so all 45 `lastmod`
values now read `2026-07-25`. Sitemap and feed both re-validated as XML.

## Baseline structural audit (post-fix, all passing)

| Check | Result |
|---|---|
| JSON-LD parse, all 89 files | 0 errors |
| broken internal links site-wide | 0 |
| canonical matches filename | 0 issues |
| stub redirects (noindex + canonical + meta-refresh) | 44 / 44 PASS |
| exactly one h1 per page | 45 / 45 |
| og: and twitter: meta on every page | 45 / 45 |
| duplicate titles / duplicate meta descriptions | 0 / 0 |
| meta descriptions present and 160 chars or under | 45 / 45 |
| sitemap.xml: 45 locs, 0 dangling, valid XML | PASS |
| feed.xml: 45 items, 0 duplicate guids, valid XML | PASS |
| llms.txt post coverage | 44 / 44 |
| robots.txt AI-crawler allowances (23 agents incl. GPTBot, ClaudeBot, OAI-SearchBot, PerplexityBot, Google-Extended, CCBot, Applebot-Extended, DuckAssistBot, Amazonbot) | intact |
| img alt attributes | 0 missing |
| self-links in body or READ NEXT grids | 0 |
| HTML div and anchor balance across edited files | 45 / 45 |

## GEO audit (all passing)

| Check | Result |
|---|---|
| `@graph` completeness per post (BlogPosting + BreadcrumbList + FAQPage) | 44 / 44 |
| HowTo schema with enumerated steps | 43 / 43 posts (hub essay exempt, correctly) |
| FAQPage schema questions matched by visible on-page `.faq-q` content | 44 / 44, zero count mismatches |
| `speakable` SpeakableSpecification present | 44 / 44 |
| author / publisher / headline / wordCount / inLanguage on every BlogPosting | complete |
| `dateModified` vs `article:modified_time` agreement | 0 mismatches |
| site-level WebSite + Organization + Blog graph on index | present, with `sameAs` |
| llms.txt: descriptive multi-sentence entry per post, not just a link list | 44 / 44 |
| READ NEXT card chips vs target post JSON-LD, 1,574 cards | 0 stale |

Google requires FAQPage markup to correspond to content a visitor can actually see, and that
correspondence holds exactly on all 44 posts. Answer engines get the same three questions in
both extractable schema and readable prose, which is the configuration that gets cited.

## Checked and deliberately left alone

- **`dateModified` not bumped on meshed posts.** Adding two related-content cards to a 40-card
  grid is not a substantive content revision. Bumping the article's own modified date for
  boilerplate would misrepresent freshness to both crawlers and answer engines. Sitemap
  `lastmod`, which describes the page rather than the article, was bumped instead.
- **Title separator encoding** (`&mdash;` entity on newer posts, literal character on older
  ones) renders identically everywhere. No SEO or GEO effect; normalizing would touch 34 files
  for zero rendered difference.
- **Titles over 70 chars** from the "Dugong Field Notes" brand suffix, keyword portion
  front-loaded. Consistent with prior rulings.
- **Hub ItemList at 4 items**, matching its editorial content, per prior ruling.
- **Template-level em/en dashes** (title separator, RSS link title, CSS comments) remain outside
  house-style enforcement. Zero em or en dashes in any content authored this run.

## Recommendations for the owner

1. **Fold the mesh into the publish run.** This is now the third pass in a week whose main job
   was back-filling links for a post the publish run left at 2 inbound. Wiring the new card into
   every sibling grid at publish time would collapse the window in which fresh content is
   least discoverable, which is precisely when it most needs crawl priority.
2. **Reconsider blanket `lastmod` bumps.** Two full-site bumps in three days is a pattern that
   can teach Google to discount the signal. Worth restricting to substantive content edits once
   the mesh moves into the publish run.
3. **FAQ depth is the largest remaining GEO opportunity.** Every post carries exactly three
   questions. Answer engines cite the page that covers the long tail of a question; going to
   five or six per post would materially widen the surface. This needs per-post editorial
   judgement about which questions merchants actually ask, so it is not appropriate for an
   autonomous pass.
4. **Undeployed working tree.** Everything from the 07-23 through 07-25 runs sits uncommitted.
   Nothing on blog.dugong.live reflects any of it until committed and pushed. No commit or push
   was made, consistent with scheduled-run convention.

## Conclusion

Two real defects, both on the newest content and both material: an orphaned pair of posts and
two truncating meta descriptions. Both fixed and verified. The link graph now has no post below
26 inbound links, every schema and distribution surface is complete and current, and the full
1,574-card chip set is accurate. **45 files edited: 43 posts meshed, sitemap.xml refreshed, plus
this report.**
