# _tools

Checked-in helpers for maintaining blog.dugong.live.

The leading underscore does **not** hide this directory. The repository has a
`.nojekyll` file, so GitHub Pages serves it raw and never runs Jekyll, which
means `_tools/` is fetchable on the live domain like any other path. robots.txt
disallows it in every user-agent group and says so in its own header comment.
Corrected 2026-10-24; the earlier wording here claimed the opposite and would
have led a later run to commit something here believing it was unreachable.

## seo-check.py

The field-level invariant checker. Run it from the repository root at the end
of every blog run and every SEO/GEO pass, before committing:

```
python3 _tools/seo-check.py          # full output
python3 _tools/seo-check.py --quiet  # first 10 entries per failing category
```

Exit code 0 means every invariant holds; 1 means at least one does not. No
dependencies beyond the Python standard library, so it runs in either shell.

It checks the things the daily run has actually broken before, which is the
reason it exists rather than a general-purpose linter:

| Invariant | Why it is here |
|---|---|
| `<title>` <= 60 chars and unique | Dispatch Nº 130 shipped a 74-char title on 2026-10-17 |
| meta description 70-165 chars, unique, matching og: and twitter: | Dispatch Nº 129 shipped a 201-char description on 2026-10-16 |
| every page's `dateModified` agrees with its sitemap `lastmod` | Drifted on 4 pages on 10-16 and 3 more on 10-17, each time because the run updated content and counts but not dates |
| every `about` entity carries a Wikidata `sameAs`, and a Wikipedia one unless listed in `wikidata_only_entity` | 3 of 115 Wikipedia targets turned out to be dead links and 2 pointed at disambiguation pages |
| JSON-LD parses; one h1; canonical == filename == og:url | Standing audit |
| BlogPosting carries all 20 fields worth having | Standing audit |
| FAQPage questions all have a non-empty acceptedAnswer | Standing audit |
| HowTo steps are typed and named | Standing audit |
| BreadcrumbList and ItemList positions run 1..n | The run renumbers these by hand |
| sitemap has no duplicates, ghosts or redirect stubs, and lists every rendered page | Standing audit |
| feed item count equals the dispatch count, no ghost links | Standing audit |
| every dispatch is in llms.txt, llms-full.txt and /md/, and links its Markdown alternate | Added 10-16, easy to forget on a new post |
| every HowTo step's `text` and `name` appears verbatim in the visible page | On 2026-10-18 every one of the 82 HowTo blocks was a paraphrase: 453 of 572 step texts appeared nowhere on the page |
| HowTo step count equals the visible `<pre id="playbook">` step count | 6 pages claimed a seventh step the reader never sees |
| every node in a `@graph` carries an `@id` | 81 FAQPage and 83 BreadcrumbList nodes had none, so nothing could reference them |
| the article claims its HowTo and FAQPage via `hasPart` | Adjacency in a `@graph` array asserts no relationship; the edge has to be written |
| no broken internal links, in-page anchors or cross-file anchors | Standing audit |
| no duplicate element ids, no mojibake, no em or en dashes | House style |
| robots.txt declares a Sitemap and disallows the three report prefixes in every user-agent group | A named group ignores the `*` group, so this has to be per-group |
| every `author` node carries a `url` and an `@id` | Aanya Rao wrote the lead essay and had no author page for five months, so her author node was the only one of 86 that resolved to nothing |
| every `CollectionPage` `about` includes at least one entity with a `sameAs` | The 8 topic guides each described themselves with a bare `Thing` name while the dispatches underneath them carried 316 grounded entity references |
| every dispatch appears in all three llms.txt lists | Dispatch Nº 131 was in "Articles" and "Markdown versions" and missing from "Full index" |
| each llms.txt topic-guide count equals the guide's ItemList and its visible card count | The inventory guide read 16 in llms.txt and 17 everywhere else for four days |
| no container holding links lacks an anchor rule in that page's stylesheet | `.article-dek` had no `a` rule, so 15 editorial links on 11 pages rendered in the dek colour with no underline and read as plain text |
| every archive-shaped READ NEXT grid carries every dispatch newer than its own newest card. A grid is archive-shaped when it holds ten or more cards and its *leading run* of newest-first dates is at least six long | On 2026-10-21 six dispatches published 10-15 to 10-21 sat in 2 or 3 grids against 73 to 82 for every other dispatch. The grid is written at publication and no later run went back to extend it, so each new post stayed outside the site's own link graph. Tightened 2026-10-24: the first version tested the first ten dates and exempted any grid that failed, which let Nos 119, 120 and 121 through. Each has a newest-first head of six or seven followed by a curated tail, so the tenth date broke the sort and the whole grid read as curated, while the head had in fact stopped at 2026-10-14 |
| every dispatch has at least one editorial inbound link, meaning an anchor inside another page's `<article>` | Nine dispatches had none on 2026-10-21. Card grids are navigation; a link in running prose is the one that carries topical meaning. A dispatch published within three days of the newest is exempt and reported as a note |
| the READING callout's link set matches the md rendition's | The md alternate is what answer engines are pointed at. On 2026-10-21 one page's md carried the block indented as a code fence with no links parsed, one carried the sentence with no blockquote marker, and one wrote `&#9670;` into a Markdown file |
| the short answer sits in a `.short-answer` container with a single `id="short-answer"`, is named in the article's `speakable` selectors, and is carried in a `BlogPosting.abstract` that appears in the visible page | Added 2026-10-24. The block was a bare `h2` plus paragraphs with no class, `speakable` named only `.article-title` and `.faq`, and no page carried an `abstract`, so the one paragraph written to be lifted whole as the answer was the single piece of the page no machine had been told about |
| whatever llms-full.txt calls "The short answer" appears on the page and in the md | 11 of the 12 short answers existed only in llms-full.txt. The one paragraph written to be quoted back as the answer was invisible to every crawler that reads HTML |
| every count a page writes next to a list it owns agrees with that list: each topic guide's masthead and `N DISPATCHES IN THIS GUIDE` heading against its ItemList and card count, the question index masthead against the eight guides, and the homepage's question count against the index | Added 2026-10-24 (second run). The run that shipped Nº 135 added it to the inventory guide's ItemList, card grid and llms.txt and left the guide's own two visible counts behind: the masthead said 17 and the list heading said 3 against 18 actually listed. The question index said 87 dispatches against 88, and the homepage's question count drifted twice in one day, by twelve in the morning and by six again by mid-morning |
| claimed words divided by claimed minutes falls between 150 and 320 | Added 2026-10-24 (second run). Both dispatches shipped that day were labelled 10 min, putting them at 356 and 326 claimed words per minute against 172 to 312 for the other 87. 13 and 12 min put them at 274 and 272, in line with the two 3,000-word dispatches already at 11 min |
| no `pubDate` or `lastBuildDate` in feed.xml is in the future | Added 2026-10-24 (second run). The feed went out with lastBuildDate at 13:30 UTC and its two newest items at 13:30 and 12:00, against a real time of 10:14. Aggregators suppress or mis-sort a future-dated item, and a lastBuildDate in the future is simply untrue |
| llms-full.txt carries each dispatch's READING callout as the md writes it, verbatim | Added 2026-10-24, second pass. The page-to-md check above says nothing about the third rendition, and that is the one an answer engine is pointed at. 74 of 89 segments carried the callout as `> ◆ READING:` with every URL stripped, 4 had lost the blockquote marker, 1 wrote `&#9670;` into a plain-text file and 6 had no callout at all. 9 editorial URLs survived in the whole file against 209 in the md renditions, so the one block in llms-full.txt that exists for its links was the only block without any |

### Deliberate exceptions

`EXCEPTIONS` near the top of the file holds the handful of cases where a
check is intentionally not applied, each with the reason in a comment:
`index.html` and `404.html` keep hand-written og:/twitter: copy, the lead
essay's `lastmod` and `dateModified` legitimately differ, `404.html` is
noindex and unlinked by design, and `wikidata_only_entity` lists entities
whose concept has a Wikidata item but no English Wikipedia article. That last
one is a tightening rather than a loosening: an entity on that list must
carry Wikidata and must **not** carry a Wikipedia URL, because the only
candidate pages are disambiguation pages or near-miss concepts. Add to it only
with a reason, and only after checking both APIs in both directions.

### If a check fires on something that is actually correct

Do not loosen the check. Either fix the page or add the page to the matching
`EXCEPTIONS` entry with a comment saying why it is intended. A checker that
has been relaxed to pass is worth nothing.
