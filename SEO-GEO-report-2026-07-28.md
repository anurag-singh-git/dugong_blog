# SEO / GEO report, 2026-07-28 (51 files edited)

**Scope:** Scheduled full-site SEO/GEO pass, run after today's publish run (Dispatch Nº 94,
"The order on hold that nobody releases"). The site now carries 95 HTML files: 48 canonical
posts, 47 pain-point redirect stubs, and index.html. This pass audited every page and every
distribution surface, found four defects, fixed all four, and verified the result.

## Headline: the publish run fixed itself

The single recurring defect class of the last several passes is gone. Today's publish run wired
Nº 94 into **sitemap.xml, feed.xml, llms.txt, index.html, and the sibling READ NEXT mesh** on its
own. No back-fill was needed on any distribution surface, and the new post arrived at 47 mesh
links rather than zero.

That closes recommendation #1 from the 07-26 and 07-27 reports. This pass could therefore spend
its budget on defects further down the stack, which is where the more interesting finding was.

## Issues found and fixed

### 1. 47 of 48 entries in the site-level `Blog` graph were near-empty stubs (fixed)

This is the substantive find of the run and it had been present, unexamined, for the life of the
site.

index.html carries the `WebSite` + `Organization` + `Blog` graph that answer engines read to build
a model of what this domain is and what it covers. The `Blog` node's `blogPost` array listed all
48 posts, so coverage looked complete to a counting check. But only one entry, the legacy
`#dispatch-47`, was actually populated. The other 47 carried four fields:

```
{ "@type": "BlogPosting", "@id": "...#article", "headline": "...",
  "url": "...", "datePublished": "...", "author": { "name": "Priya Singh" } }
```

No `description`, no `publisher`, no `image`, no `inLanguage`, no `dateModified`, no `wordCount`.
A crawler reading the hub got 47 headlines and nothing to reason about. The per-post pages carry
full markup, but the hub is what gets fetched first and what establishes topical authority for the
domain as a whole. Answer engines that build a site-level model from the entry point were seeing a
list of links, not a body of work.

All 47 were rebuilt to a complete entry:

| Field | before | after |
|---|---|---|
| `description` | 0 / 47 | 47 / 47 |
| `mainEntityOfPage` | 0 / 47 | 47 / 47 |
| `dateModified` | 0 / 47 | 47 / 47 |
| `publisher` | 0 / 47 | 47 / 47 |
| `image` | 0 / 47 | 47 / 47 |
| `inLanguage` | 0 / 47 | 47 / 47 |
| `wordCount` | 0 / 47 | 47 / 47 |

Every value was read from the target post's own JSON-LD or meta description rather than
hand-written, so the hub cannot drift from the articles.

**Descriptions use the 155-character meta description, not the 800-character JSON-LD one.** The
long-form variant would have added 39KB to the hub. The meta description adds 7KB, is what
actually appears in a SERP, and is the version already tuned to lead with the problem and land the
playbook clause.

### 2. Author was 47 anonymous copies instead of one entity (fixed)

Related to the above, and the reason it is worth calling out separately: the hub's author data was
47 detached `{"@type": "Person", "name": "Priya Singh"}` objects with no identifier. Nothing tied
them to each other or to the fuller `Person` records on the post pages.

Entity consolidation is how an answer engine decides an author is a real, consistent expertise
signal rather than a byline string. Forty-seven unlinked copies of a name establish nothing.

Added a single `Person` node to the graph at `https://blog.dugong.live/#priya-singh` carrying
`name`, `jobTitle`, `description`, `worksFor` (referencing the existing `#organization` node), and
a `knowsAbout` array of the five domains the corpus actually covers. All 47 entries now reference
it by `@id`.

This is both the better modelling and the lighter payload: one enriched node plus 47 references
costs less than 47 inline objects would have.

| | before | after |
|---|---|---|
| distinct author entities in hub graph | 0 (47 detached literals) | 1, with `@id` |
| `@id` cross-references in hub graph | 3 | 3, all resolving |
| unresolved `@id` references | 0 | 0 |

### 3. Meta description exceeded the 160-character limit (fixed)

Third run in a row. Nº 94 shipped at 170 characters and would have truncated in the SERP:

| | before | after |
|---|---|---|
| held-order release (Nº 94) | 170 chars | 158 |

The rewrite keeps the house problem-then-playbook shape and swaps a generic closing ("releases
them the hour the pallet lands") for the two mechanics the article actually argues are load
bearing, reserving before release and oldest-promise-first ordering. Both are better material for
an answer engine to quote. `og:description` and `twitter:description` are separate long-form
fields on this site and are not length-constrained, so they were left alone.

Every post now sits between 145 and 160 characters.

### 4. An FAQ schema question did not match its visible heading (fixed)

On `how-to-stop-discount-code-abuse-on-shopify.html`, the FAQPage markup read:

> Why does Shopify's limit to one use per customer not work?

while the visible `.faq-q` heading read:

> Why does Shopify's "limit to one use per customer" not work?

The quotation marks had been dropped from the schema, presumably to avoid escaping them inside the
JSON string. Google requires FAQ markup to correspond to content a visitor can see, and the two
surfaces disagreeing is the exact condition that gets rich results suppressed. Restored the quotes
in the schema with proper escaping. All 47 posts now match their visible headings exactly.

### 5. robots.txt was addressing retired and non-existent crawlers (fixed)

The file's default is `User-agent: * / Allow: /`, so nothing was actually being blocked and no
crawler lost access. But the explicit block, which is the file's stated purpose and the thing a
human reads to understand intent, had drifted:

- **`PerplexityBot-User` is not a real user agent.** Perplexity's user-initiated fetcher is
  `Perplexity-User`. The line addressed nobody.
- **`Claude-Web` is retired.** Anthropic's current agents are `ClaudeBot` (indexing, present),
  `Claude-User` (user-initiated fetch, absent) and `Claude-SearchBot` (search indexing, absent).
  Two of the three were missing.
- Several active answer-engine and retrieval agents had no explicit entry.

| | before | after |
|---|---|---|
| `User-agent` blocks | 24 | 33 |
| non-existent agents addressed | 1 | 0 |
| current Anthropic agents named | 1 of 3 | 3 of 3 |

Added `Claude-User`, `Claude-SearchBot`, `Perplexity-User`, `MistralAI-User`, `AI2Bot`, `Diffbot`,
`FirecrawlAgent`, `Timpibot`, `omgili`, `ImagesiftBot`. Kept `Claude-Web` for the transition.

Also added pointer comments for `llms.txt` and `feed.xml` beneath the `Sitemap:` directive. There
is no standard robots directive for either, so a comment is the honest form, and it is where an
operator or a crawler author looks first.

## Baseline structural audit (post-fix, all passing)

| Check | Result |
|---|---|
| JSON-LD parse, all 95 files | 0 errors |
| broken internal links site-wide | 0 |
| canonical present and correct on all pages | 95 / 95 |
| stub redirects (noindex + canonical + meta-refresh) | 47 / 47 PASS |
| exactly one h1 per page | 48 / 48 |
| og: and twitter: meta on every page | 48 / 48 |
| duplicate titles / duplicate meta descriptions | 0 / 0 |
| meta descriptions present and 160 chars or under | 48 / 48 |
| `lang` attribute on every page | 48 / 48 |
| `og:image` on every page | 48 / 48 |
| img alt attributes | 0 missing |
| orphaned posts | 0 |
| inbound links, min / avg / max | 30 / 55.3 / 427 |
| sitemap.xml: 48 locs, 0 stubs, 0 dangling, valid XML | PASS |
| feed.xml: 48 items, 0 duplicate guids, valid XML | PASS |
| llms.txt post coverage | 48 / 48 |
| index.html div / anchor / script balance | 251-251, 184-184, 2-2 |

## GEO audit (post-fix, all passing)

| Check | Result |
|---|---|
| `@graph` completeness per post (BlogPosting + BreadcrumbList + FAQPage) | 47 / 47 |
| HowTo schema with enumerated steps | 46 / 46 posts (hub essay exempt, correctly) |
| FAQPage questions matched by visible `.faq-q` content | 47 / 47, exact string match |
| `speakable` SpeakableSpecification present | 47 / 47 |
| author / publisher / headline / wordCount / inLanguage on every BlogPosting | complete |
| `dateModified` vs `article:modified_time` agreement | 0 mismatches |
| site-level graph on index (WebSite + Organization + Person + Blog) | complete, all `@id` refs resolve |
| hub `blogPost` entries fully populated | 48 / 48 (was 1 / 48) |
| llms.txt: descriptive multi-sentence entry per post | 48 / 48 |
| robots.txt AI-crawler allowances | 33 agents, 0 stale |
| `about` entity linking on Nº 94 | 5 entities (Shopify, Backorder, Order fulfillment, Inventory management, Stockout), 5 / 5 with `sameAs` |

Nº 94 carries 2,385 words, a 7-step HowTo, a 3-question FAQPage all visible on page, an 8-term
keyword set, and a 2-item BreadcrumbList. Its schema is complete on arrival, which is the first
time that has been true of a new post in this report series.

## Checked and deliberately left alone

- **Hub page weight.** index.html grew from 166KB to 194KB (+17%). The added content is highly
  repetitive JSON, which gzips at roughly 10:1, so the transfer cost is a few KB. Worth it for a
  complete site-level entity graph. Flagging it so the trend is visible if the corpus doubles.
- **`dateModified` not bumped on the two posts edited here.** A schema quote fix and a meta
  description rewrite are corrections, not content revisions. Bumping the article's modified date
  for them would misrepresent freshness.
- **Blanket sitemap `lastmod`.** All 48 read `2026-07-28`, set by the publish run. Unlike previous
  days this is defensible: the mesh insert genuinely modified all 47 sibling posts. Left as is.
- **FAQ depth at exactly 3 per post, all 47.** Still the largest untapped GEO surface. See below.
- **`SearchAction` on the `WebSite` node.** The site has no search endpoint. Marking one up would
  be false markup and a manual-action risk. Correctly absent.
- **Titles over 70 chars** from the "Dugong Field Notes" brand suffix, keyword portion
  front-loaded. Consistent with prior rulings.
- **Title separator encoding** (`&mdash;` entity on newer posts, literal character on older ones).
  Renders identically.
- **Hub ItemList at 4 items**, matching its editorial content, per prior ruling.
- **Template-level em/en dashes** (title separator, RSS link title, CSS comments) remain outside
  house-style enforcement. Zero em or en dashes in any content authored this run.

## Recommendations for the owner

1. **Add the hub-graph fields to the publish template.** The `blogPost` entry the publish run
   appends to index.html should carry the same 11 fields the 47 back-filled entries now have, and
   should reference the `#priya-singh` Person node rather than inlining a bare name. Otherwise
   tomorrow's Nº 95 reintroduces defect #1 as a population of one.
2. **Assert meta description length at authoring time.** Three consecutive runs have shipped an
   over-length description (205, 180, now 170). One character count in the publish step ends this
   defect class permanently. This is now the only recurring failure left.
3. **FAQ depth is the remaining GEO opportunity, and it is now the largest one by a distance.**
   Every post carries exactly three questions. Answer engines cite the page that covers the long
   tail of a question, and the corpus is uniformly shallow at the point where citation is decided.
   Five or six per post would materially widen the citable surface. This needs per-post editorial
   judgement about what merchants actually ask and accurate answers about Shopify's real behaviour,
   so it remains inappropriate for an autonomous pass to invent. It is worth a dedicated session.
4. **Consider an author page.** The `#priya-singh` Person node now exists as an entity but resolves
   to the site root. A real `/authors/priya-singh.html` with credentials and a post list would give
   the E-E-A-T signal somewhere to land, and would let the node carry a `sameAs`.
5. **Undeployed working tree.** Today's publish run and this pass are both uncommitted. Nothing on
   blog.dugong.live reflects any of it until committed and pushed. No commit or push was made,
   consistent with scheduled-run convention.

## Conclusion

The recurring distribution defect is fixed at source: the publish run wired Nº 94 into every
surface without help, for the first time. That freed this pass to look deeper, and it found that
the site-level `Blog` graph on the hub, the thing answer engines read first to decide what this
domain is authoritative about, had been carrying 47 four-field stubs and 47 detached author
literals since inception. Both are now complete and entity-consolidated.

Four defects found, four fixed, all verified. **51 files edited: index.html rebuilt with a
complete hub graph and a consolidated Person entity, Nº 94's meta description rewritten, one FAQ
schema question corrected, robots.txt modernised from 24 to 33 agents, plus 46 files carrying
today's mesh, this report, and sitemap.xml.**
