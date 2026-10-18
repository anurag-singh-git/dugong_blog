# _tools

Checked-in helpers for maintaining blog.dugong.live. The leading underscore
keeps Jekyll from publishing this directory, so nothing here is reachable on
the live domain.

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
| every `about` entity carries both a Wikipedia and a Wikidata `sameAs` | 3 of 115 Wikipedia targets turned out to be dead links and 1 pointed at a disambiguation page |
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

### Deliberate exceptions

`EXCEPTIONS` near the top of the file holds the handful of cases where a
check is intentionally not applied, each with the reason in a comment:
`index.html` and `404.html` keep hand-written og:/twitter: copy, the lead
essay's `lastmod` and `dateModified` legitimately differ, and `404.html` is
noindex and unlinked by design. Add to it only with a reason.

### If a check fires on something that is actually correct

Do not loosen the check. Either fix the page or add the page to the matching
`EXCEPTIONS` entry with a comment saying why it is intended. A checker that
has been relaxed to pass is worth nothing.
