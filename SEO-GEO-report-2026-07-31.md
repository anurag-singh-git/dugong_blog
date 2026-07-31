# SEO / GEO report, 2026-07-31 (50 files edited)

**Scope:** Scheduled full-site SEO/GEO pass, the first since 07-28. In between, the 07-30 publish
run landed Dispatch Nº 95, "The wholesale application that sits all weekend"
(`how-to-automatically-approve-wholesale-customers-on-shopify.html`), plus its pain-point stub.
The site now carries 97 HTML files: 48 canonical posts, 48 redirect stubs, and index.html. This
pass audited every page and every distribution surface, found two defects, fixed both, and
verified the result.

## Headline: the publish template kept its 07-28 promise on the hub, then dropped the mesh

Recommendation #1 from the 07-28 report asked the publish step to write a complete hub-graph
entry for new posts. It did. Nº 95 arrived in the index `Blog` graph with all eleven fields and an
`@id` reference to the consolidated `#priya-singh` Person node. Its meta description shipped at
156 characters, inside the limit, which also retires the over-length-description defect class
that ran for three consecutive publishes (205, 180, 170 chars). Both recurring publish defects
are closed.

But the 07-30 run skipped a step the 07-28 run had performed: inserting the new post into the
sibling READ NEXT mesh. Nº 95 sat at exactly one inbound link, from its own noindex redirect
stub. Zero editorial pages linked to it. For crawl discovery and for the internal-authority
signal that answer engines weigh, the newest post on the site was an orphan in all but name.

## Issues found and fixed

### 1. Nº 95 had zero sibling mesh links (fixed)

The 07-30 blog-run notes list index.html, sitemap.xml, feed.xml, and llms.txt as touched, and all
four were correct. The 47 sibling posts were not touched, so none of their `related-grid`
sections carried the new dispatch.

Prepended Nº 95's card to the top of the READ NEXT grid on all 47 sibling posts, matching the
exact card markup, ordering convention (newest first), and metadata the 07-28 insert used for
Nº 94: pain-point title, the 156-character meta description as dek, `research` tag, 9-minute
read chip (matches the post's own `timeRequired` of PT9M), JUL 30 date, P. Singh byline.

| | before | after |
|---|---|---|
| inbound links to Nº 95, rendered pages | 1 (index only) | 48 (index + 47 siblings) |
| siblings carrying the Nº 95 card | 0 / 47 | 47 / 47 |

Zero em or en dashes in the inserted card; the dek is the post's own meta description verbatim,
so the surfaces cannot drift.

### 2. The hub graph's one remaining incomplete entry, `#dispatch-47` (fixed)

The 07-28 rebuild brought 47 of 48 `blogPost` entries to eleven fields but left the legacy
pinned-essay entry ("The death of the drag-and-drop builder", by Aanya Rao) untouched because it
was already the most complete entry at the time. Against the new standard it was missing two
fields: `dateModified` and `wordCount`.

Added both: `dateModified` set to its `datePublished` (2026-05-28; the essay has not been
revised) and `wordCount` 893, counted from the essay's actual inline article body. Its author
stays as the inline Aanya Rao Person object rather than a `#priya-singh` reference, which is
correct: it is the one piece on the site with a different byline, and the visible byline agrees.

The hub graph is now 49 / 49 complete entries (48 posts + pinned essay).

### Housekeeping: sitemap `lastmod`

The mesh insert genuinely modified 47 sibling posts, and the graph fix modified index.html, so
their `<lastmod>` values were bumped to 2026-07-31. Nº 95 keeps its honest 2026-07-30. Same
ruling as 07-28: a blanket bump is defensible only when the files were actually edited, and this
time they were. Per-post `dateModified` was deliberately not bumped; a related-cards insertion is
navigation chrome, not a content revision, and bumping it would misrepresent freshness.

## Baseline structural audit (post-fix, all passing)

| Check | Result |
|---|---|
| JSON-LD parse, all 49 rendered pages | 0 errors |
| broken internal links site-wide | 0 |
| canonical present, matches filename, equals og:url | 49 / 49 |
| stub redirects (noindex + canonical + meta-refresh, live targets) | 48 / 48 PASS |
| exactly one h1 per page | 49 / 49 |
| og: and twitter: meta on every rendered page | 49 / 49 |
| duplicate titles / duplicate meta descriptions | 0 / 0 |
| meta descriptions present and 160 chars or under | 49 / 49 |
| `lang` attribute, og:image, img alt coverage | complete |
| tag balance on all edited files (incl. multiline `<a` forms) | balanced |
| sitemap.xml: 49 locs, 0 dupes, 0 ghosts, valid XML | PASS |
| feed.xml: 49 items, 0 duplicate guids, valid XML, lastBuildDate = newest item | PASS |
| llms.txt post coverage, descriptive entry per post | 48 / 48 |
| orphaned posts | 0 |

## GEO audit (post-fix, all passing)

| Check | Result |
|---|---|
| `@graph` per post (BlogPosting + BreadcrumbList + FAQPage) | 48 / 48 |
| HowTo schema with enumerated steps | 47 / 47 (hub essay exempt, correctly) |
| FAQPage questions match visible `.faq-q` text | 48 / 48, exact string match |
| `speakable` SpeakableSpecification | 48 / 48 |
| `about` entity linking present on posts | 48 / 48 |
| `dateModified` vs `article:modified_time` agreement | 0 mismatches |
| site-level graph (WebSite + Organization + Person + Blog), `@id` refs resolve | complete |
| hub `blogPost` entries fully populated | 49 / 49 (was 48 / 49) |
| new-post hub entry references `#priya-singh` by `@id` | yes, publish template fixed |
| robots.txt AI-crawler allowances | 33 agents, 0 stale, unchanged from 07-28 |

Nº 95 itself arrived clean: complete four-node schema, 156-char meta description, 3-question
FAQ visible on page, 9 related cards, and full coverage on sitemap, feed, llms.txt, and the
index hero, ticker, card grid, and topic cloud. Its only defect was the missing sibling mesh,
now fixed.

## Checked and deliberately left alone

- **Read-time vs word count on the pinned essay.** The essay's visible chip says 14 min against
  893 counted words. The chip is editorial chrome dating from launch; `wordCount` in the graph
  now reports the true count. Flagged for the owner rather than silently rewriting a visible
  design element.
- **FAQ depth at exactly 3 per post.** Still the largest untapped GEO surface; still needs
  per-post editorial judgement an autonomous pass should not invent. Carried forward.
- **Titles over 70 chars** from the brand suffix, keyword portion front-loaded. Consistent with
  prior rulings.
- **Template-level em/en dashes** in shared CSS comments and `&mdash;` chrome entities remain
  outside house-style enforcement. Zero em or en dashes in content authored this run.
- **robots.txt** untouched; the 07-28 modernisation (33 agents) still reflects the current
  crawler landscape as of this pass.

## Recommendations for the owner

1. **Add the sibling mesh insert to the publish step.** The 07-28 run did it; the 07-30 run did
   not. It is the one distribution surface the publish template still handles inconsistently, and
   it is the difference between a new post launching with 47 inbound links and launching with
   none. Everything else the template now does correctly on its own.
2. **FAQ depth** remains the highest-value GEO opportunity: five or six questions per post would
   materially widen the citable surface. Worth a dedicated editorial session.
3. **Author page** for `/authors/priya-singh.html` (and arguably one for Aanya Rao) so the
   Person entities resolve somewhere and can carry `sameAs`. Carried forward from 07-28.
4. **Undeployed working tree.** The 07-28 publish and SEO pass, the 07-30 QA fix and publish, and
   this pass are all uncommitted. Nothing on blog.dugong.live reflects any of it until committed
   and pushed. No commit or push was made, consistent with scheduled-run convention.

## Conclusion

Both recurring publish-time defect classes from the last report series are confirmed closed: the
hub-graph entry arrived complete and the meta description arrived inside 160 characters, with no
back-fill needed. The regression was the sibling mesh, which left Nº 95 with a single inbound
link from its own stub; it now has 48. The hub graph reached full completeness with the
`#dispatch-47` back-fill.

Two defects found, two fixed, all verified. **50 files edited: 47 sibling posts carrying the
Nº 95 mesh card, index.html (hub-graph completion), sitemap.xml (lastmod), and this report.**
