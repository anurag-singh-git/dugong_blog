# SEO / GEO report, 2026-07-27 (48 files edited)

**Scope:** Scheduled full-site SEO/GEO pass, run after today's publish run (Dispatch Nº 93,
"The order that ships from the wrong warehouse"). The site now carries 93 HTML files: 46 canonical
posts, 46 pain-point redirect stubs, and index.html. This pass audited every page and every
distribution surface, found three defects, fixed all three, and verified the result.

Yesterday's pass was committed, so the working tree started clean apart from today's publish run.
That is an improvement on the prior state and makes the delta below attributable entirely to today.

## Issues found and fixed

### 1. The new post was missing from llms.txt (fixed)

Dispatch Nº 93, `how-to-route-shopify-orders-to-the-right-warehouse.html`, made it into
sitemap.xml, feed.xml and index.html at publish time. That is a partial recovery from yesterday,
where all three were missed. But **llms.txt was still not updated**.

llms.txt is the file GPTBot, ClaudeBot, PerplexityBot and OAI-SearchBot read to build a
site-level model of what this domain covers. A post absent from it does not exist as far as an
answer engine's understanding of the site is concerned, even if the HTML is crawlable.

| Surface | before | after |
|---|---|---|
| sitemap.xml locs | 47 | 47 (already correct) |
| feed.xml items | 47 | 47 (already correct) |
| llms.txt post entries | 45 / 46 | 46 / 46 |

The new entry follows the house pattern: a descriptive multi-sentence entry covering the native
gap (routing rules never read a shipping rate, closest means straight-line distance, capacity is
a hand-typed metafield, split-or-single is one global lever), the two boundaries merchants hit
(Flow can only move a fulfillment order where every line is stocked and only before a fulfillment
service accepts, and custom rules via the Order Routing Location Rule Function API are Plus, by
request, as a custom app), and what the playbook does. Inserted in newest-first order at the head
of the article list, byline and date included.

### 2. The new post was fully orphaned in the internal mesh (fixed)

Nº 93 carried **zero** mesh links from sibling posts while its peers sit between 27 and 101.
Only index.html, its own redirect stub, and the topic cloud pointed at it.

This is the third consecutive run with the same defect. The internal-link mesh is what drives
crawl priority, internal PageRank flow, and the topical-cluster signal answer engines use to
decide which page on a domain is authoritative for a query. A post at zero is the largest single
discovery drag available.

Added a `READ NEXT` card for Nº 93 to the related grid of all 45 sibling posts, inserted at the
head of each grid per the newest-first convention, skipping the self-link.

| | before | after |
|---|---|---|
| Nº 93 mesh links (from sibling posts) | 0 | 45 |
| Nº 93 total inbound links | 4 | 49 |
| site-wide inbound min / avg / max | 4 / 45.9 / 103 | 30 / 46.9 / 103 |
| mesh-only min / avg / max | 0 / 42.9 / 101 | 27 / 43.8 / 101 |
| orphans | 1 | 0 |

Card chips (read time `PT10M`, tag `research`, date `JUL 27`, author `P. Singh`) were taken from
the target post's own JSON-LD and index card rather than hand-copied, so they cannot drift. Card
dek reuses the corrected meta description, so the two surfaces stay in sync by construction.

### 3. Meta description exceeded the 160-character limit (fixed)

Every other post sits between 145 and 160 characters. Nº 93 ran to 180 and would have been
truncated in the SERP, cutting into the "AI playbook" clause that drives the click:

| | before | after |
|---|---|---|
| order routing (Nº 93) | 180 chars | 159 |

The rewrite keeps the problem-then-playbook shape of the house pattern and swaps a vague closing
("cheapest and fastest") for the three concrete scoring inputs the article actually argues for
(landed cost, cutoff, backlog), which is also better material for an answer engine to quote.
`og:description` and `twitter:description` are separate long-form fields on this site and are not
length-constrained, so they were left alone.

### 4. Sitemap `lastmod` refreshed

47 files were edited by this pass, so all 47 `lastmod` values now read `2026-07-27`. Sitemap and
feed both re-validated as well-formed XML.

## Baseline structural audit (post-fix, all passing)

| Check | Result |
|---|---|
| JSON-LD parse, all 93 files | 0 errors |
| broken internal links site-wide | 0 |
| canonical matches filename | 0 issues |
| stub redirects (noindex + canonical + meta-refresh) | 46 / 46 PASS |
| exactly one h1 per page | 47 / 47 |
| og: and twitter: meta on every page | 47 / 47 |
| duplicate titles / duplicate meta descriptions | 0 / 0 |
| meta descriptions present and 160 chars or under | 47 / 47 |
| duplicate READ NEXT cards introduced | 0 |
| self-links in body or READ NEXT grids | 0 |
| new-post card present exactly once, first in grid, on all 45 siblings | 45 / 45 |
| sitemap.xml: 47 locs, 0 dangling, valid XML | PASS |
| feed.xml: 47 items, 0 duplicate guids, valid XML | PASS |
| llms.txt post coverage | 46 / 46 |
| robots.txt AI-crawler allowances (24 agents incl. GPTBot, ClaudeBot, OAI-SearchBot, PerplexityBot, Google-Extended, CCBot, Applebot-Extended, DuckAssistBot, Amazonbot) | intact |
| img alt attributes | 0 missing |
| HTML div and anchor balance across edited files | 46 / 46 |

## GEO audit (all passing)

| Check | Result |
|---|---|
| `@graph` completeness per post (BlogPosting + BreadcrumbList + FAQPage) | 46 / 46 |
| HowTo schema with enumerated steps | 45 / 45 posts (hub essay exempt, correctly) |
| FAQPage schema questions matched by visible on-page `.faq-q` content | 46 / 46, zero count mismatches |
| `speakable` SpeakableSpecification present | 46 / 46 |
| author / publisher / headline / wordCount / inLanguage on every BlogPosting | complete |
| `dateModified` vs `article:modified_time` agreement | 0 mismatches |
| site-level WebSite + Organization + Blog graph on index | present, with `sameAs` |
| llms.txt: descriptive multi-sentence entry per post | 46 / 46 |
| `about` entity linking on Nº 93 (Shopify, order fulfillment, third-party logistics, distribution center, warehouse management system, Dugong) | 6 entities with `sameAs` |

Nº 93's HowTo carries six enumerated steps and its FAQPage carries three questions, all three of
which appear verbatim as visible `.faq-q` headings. Google requires FAQ markup to correspond to
content a visitor can see, and that correspondence holds exactly across all 46 posts.

## Checked and deliberately left alone

- **`dateModified` not bumped on meshed posts.** Adding one related-content card to a 45-card
  grid is not a substantive content revision. Bumping the article's modified date for boilerplate
  would misrepresent freshness to crawlers and answer engines. Sitemap `lastmod`, which describes
  the page rather than the article, was bumped instead.
- **Repeated in-body links between related posts** (a handful of pairs link two to five times in
  prose). These are contextual editorial links, not duplicated cards, and reinforce topical
  clusters rather than diluting them. Not a defect.
- **Titles over 70 chars** from the "Dugong Field Notes" brand suffix, keyword portion
  front-loaded. Consistent with prior rulings.
- **Title separator encoding** (`&mdash;` entity on newer posts, literal character on older ones)
  renders identically. No SEO or GEO effect.
- **Hub ItemList at 4 items**, matching its editorial content, per prior ruling.
- **Template-level em/en dashes** (title separator, RSS link title, CSS comments) remain outside
  house-style enforcement. Zero em or en dashes in any content authored this run.

## Recommendations for the owner

1. **The publish run still does not wire llms.txt or the sibling mesh.** Today it handled sitemap,
   feed and index correctly, which is progress over yesterday. The two remaining gaps are the same
   two that have needed manual back-fill on every recent run. Both are mechanical: append one
   llms.txt entry, insert one card at the head of each sibling grid. Wiring them at publish time
   removes the only recurring defect class this pass sees.
2. **Meta description length is not being checked at authoring time.** Two runs in a row have
   shipped an over-length description (205, then 180). A single character-count assertion in the
   publish step would catch it before the page is live.
3. **FAQ depth remains the largest untapped GEO opportunity.** Posts carry three to four questions
   each. Answer engines cite the page that covers the long tail of a question, and five or six per
   post would materially widen the citable surface. This needs per-post editorial judgement about
   what merchants actually ask, so it is not appropriate for an autonomous pass.
4. **Reconsider blanket `lastmod` bumps.** Full-site bumps most days is a pattern Google can learn
   to discount. Worth restricting to substantive content edits once the publish run does its own
   wiring.
5. **Undeployed working tree.** Today's publish run and this pass are both uncommitted. Nothing on
   blog.dugong.live reflects any of it until committed and pushed. No commit or push was made,
   consistent with scheduled-run convention.

## Conclusion

Three defects, all on the newest content and all material: a post missing from llms.txt, a fully
orphaned post, and a truncating meta description. All fixed and verified. Every post now sits at
27 or more mesh links, sitemap and feed and llms.txt are complete and current, and every schema
surface validates. **48 files edited: 45 posts meshed, the new post's meta description rewritten,
plus llms.txt and sitemap.xml.**
