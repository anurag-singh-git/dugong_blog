# SEO / GEO report - 2026-10-16

Scheduled autonomous run. Last SEO/GEO pass: 2026-10-14.

## Part 0 - Read this first: nothing since 15 October is live

The 10-14 report opened by confirming that the 10-12 and 10-13 work had reached crawlers. This one
has to open the other way.

`HEAD` is `8e5c9e3`, committed 2026-10-15 02:19 +0530, and it is identical to `origin/main`. The
working tree at the start of this run carried **93 modified files and 18 untracked ones**. GitHub
Pages serves from the repository, so every one of those changes is on this machine only.

What that means in practice, because the uncommitted set is not small:

- The whole 2026-10-14 SEO/GEO pass is undeployed. `shopify-automation-questions.html`,
  `priya-singh.html` and `the-death-of-the-drag-and-drop-builder.html` do not exist at
  blog.dugong.live. They are in the local sitemap, so a crawler that reads it is being pointed at
  three 404s.
- The 403 FAQ ids that gave every answer its own fragment are undeployed, so the question index's
  deep links would not resolve even if the page were there.
- Dispatch Nº 128 (2026-10-15) and Nº 129 (2026-10-16) are undeployed, along with the index, feed,
  sitemap, guide, author-page and question-index edits their blog runs made.
- Everything in this report is in the same position.

I have not committed or pushed anything. That needs a person: the commit history on this repo is
hand-written, and two days of mixed blog-run and SEO work is not a diff to squash blind. A
notification went out at the top of this run.

The rest of this report describes work done on disk.

## Part 1 - Field-level audit, before any changes

Recomputed from the files: 177 HTML files, 95 rendered (83 posts including the lead essay, 8 topic
guides, the question index, the author page, index.html and 404.html), 82 redirect stubs.

Everything the 10-14 report checked still passes, and two things do not:

| Check | Result |
|---|---|
| JSON-LD parses, all rendered pages | 95 / 95 |
| exactly one h1 | 95 / 95 |
| canonical == filename == og:url | 95 / 95 |
| title <= 60 and unique | PASS, 0 dupes |
| meta description 70-165 and unique | **1 FAIL** (dispatch Nº 129, 201 chars) |
| description == og == twitter | all but index and 404 (standing item) |
| broken internal links | 0 |
| broken in-page anchors, all 415 FAQ deep links | 0 |
| duplicate element ids | 0 |
| CSS brace and style-tag balance | 0 failures |
| replacement characters / mojibake | 0 |
| sitemap 94 locs, 0 dupes, 0 ghosts, no stubs | PASS |
| feed 83 items, parses, 0 ghosts | PASS |
| every post in feed, llms.txt, llms-full.txt | PASS |
| orphan rendered pages | 0 (404.html excepted, by design) |
| sitemap lastmod agrees with the page's own dateModified | **6 FAIL** |
| BlogPosting carries isAccessibleForFree | **0 / 83** |
| image objects carry width and height | 83 / 83 |

## Part 2 - Dispatch Nº 129 shipped a meta description 36 characters over the cap

Today's blog run wrote a 201-character description onto
`how-to-handle-return-to-sender-orders-on-shopify.html`. Google truncates around 160, so the last
sentence, which is the one carrying the value proposition, would never have been read. It also broke
the 70-165 invariant this site has held on all 95 pages.

Rewritten to 164 characters, keeping the hook and moving the exact query phrase to the end:

> The carrier turned the parcel around and the order still reads Fulfilled, because Shopify has no
> status for it. The AI playbook that catches every return to sender.

Replaced in all three places it appears on the page (`description`, `og:description`,
`twitter:description`). The long-form JSON-LD `description` on the BlogPosting and HowTo nodes is a
different, deliberately fuller string and was left alone. Nothing else on the site carried the old
text.

**This is a blog-run template bug, not a one-off.** The generator has no length check on the
description it writes. Worth adding one at source, or this comes back.

## Part 3 - Freshness signals that contradicted each other

Two related problems, both found by comparing a page's declared dates against what the page actually
contains.

**Stale `dateModified` on four pages.** Most guides are maintained correctly: their declared
`dateModified` matches the newest dispatch in their own ItemList exactly. Four did not, because the
blog run adds the new card and the ItemList entry but does not touch the date:

| Page | Declared | Newest dispatch it lists | Now |
|---|---|---|---|
| shopify-shipping-and-fulfillment-automation.html | 2026-09-19 | 2026-10-16 | 2026-10-16 |
| shopify-inventory-automation.html | 2026-10-12 | 2026-10-15 | 2026-10-15 |
| priya-singh.html | 2026-10-14 | 2026-10-16 | 2026-10-16 |
| shopify-automation-questions.html | 2026-10-14 | 2026-10-16 | 2026-10-16 |

The shipping guide was the worst of these: 27 days stale on a page that had gained two dispatches in
that window. Each new date is the publication date of the newest dispatch the page actually lists,
so it is derived from the page's own content rather than asserted.

**Six sitemap `lastmod` values disagreed with the page's own `dateModified`.** A crawler gets the
recrawl hint from one and the content date from the other, and when they conflict it learns to trust
neither. Five corrected to match:

- `/` 2026-10-14 to 2026-10-16 (the homepage changed today with Nº 129)
- `/shopify-inventory-automation.html` 2026-09-17 to 2026-10-15
- `/shopify-shipping-and-fulfillment-automation.html` 2026-10-14 to 2026-10-16
- `/shopify-automation-questions.html` 2026-10-14 to 2026-10-16
- `/priya-singh.html` 2026-10-14 to 2026-10-16

The sixth is left as it is on purpose. `the-death-of-the-drag-and-drop-builder.html` has
`lastmod` 2026-10-14 and `dateModified` 2026-05-28, and both are true: the URL first appeared on
10-14, the essay text has not changed since May. A recent `lastmod` on a URL no crawler has ever
seen is the useful hint. Noted here so the next pass does not "fix" it.

This is the same class of bug as Part 2: the blog run maintains content and counts but not dates.

## Part 4 - Every dispatch now has a Markdown twin

The largest GEO change in this run, and the first one aimed at the fetch step rather than the markup.

`llms-full.txt` is the file an answer engine is meant to read when it wants the actual text, and it
is **1.5 MB**. Most fetchers cap a response well below that. The file is newest-first, so what gets
cut is the archive: the older a dispatch, the less likely any engine has ever read its body. The
site was publishing a complete corpus that in practice could only be read from the front.

`/md/<slug>.md` now exists for all 83 dispatches. One file per article, 10 to 25 KB each, generated
from the shipped HTML so the text matches the page rather than a parallel draft. Each file carries:

- an H1 that is the JSON-LD `headline`, so the Markdown and the structured data agree
- the meta description as a blockquote
- a metadata header: canonical URL, author with the author-page URL, publication and update dates,
  section, word count, dispatch number, read time, keywords, publisher
- the complete article body, with headings, callouts as labelled blockquotes, playbook specs as
  fenced code blocks, and every in-prose link rewritten to an absolute `blog.dugong.live` URL
- the full answer to every FAQ question, each followed by `Permalink:` pointing at the `#faq-n`
  anchor on the HTML page, so an engine quoting an answer can cite the exact fragment
- a closing line naming the canonical URL as the thing to cite

Discovery is wired three ways:

1. `<link rel="alternate" type="text/markdown" href="/md/<slug>.md">` in the head of all 83 posts,
   inserted after the existing RSS alternate. `rel="alternate"` is not a canonical signal, and the
   `.md` files are deliberately **not** in sitemap.xml, so the HTML stays the one indexable address.
2. A new `## Markdown versions` section in llms.txt: the convention stated in prose (drop `.html`,
   fetch `/md/<slug>.md`) plus all 83 links in the same newest-first order as the full index.
3. A header line in llms-full.txt that names its own size and tells a truncating fetcher to read the
   per-article files instead.

Verified on the generated set: 83 files, 0 leaked HTML tags, 0 unescaped entities, 86 balanced code
fences, 592 internal links all resolving to files that exist, 415 FAQ permalinks all pointing at
anchors that exist, every file starting with an H1 and carrying its canonical URL.

The essay is in the set with no FAQ section, which is correct, it has none.

## Part 5 - Internal build logs are no longer crawlable

The repository root holds roughly 250 `QA-report-*.md`, `blog-run-*.md` and `SEO-GEO-report-*.md`
files. They have no YAML front matter, so Jekyll copies them verbatim rather than rendering them,
which means every one of them is a fetchable URL on the live domain. robots.txt said `Allow: /` and
nothing else. They are thin, repetitive, and they describe the editorial strategy of the site in
detail.

Three `Disallow` prefixes added to **all 40 user-agent groups**. This matters: a crawler that
matches a named group ignores the `*` group entirely, so putting the rules only under `User-agent: *`
would have left GPTBot, ClaudeBot, PerplexityBot and 37 others reading the logs. The explicit
AI-crawler allow list, which is the point of this file, is untouched.

Validated two ways, because a robots.txt mistake is the one change in this run that could deindex
the site: a longest-match implementation of RFC 9309 run against 7 agents and 16 paths, and
independently with `protego` against 9 agents and 13 paths. Both agree: articles, `/md/*`,
sitemap.xml, llms.txt, llms-full.txt, feed.xml and images allowed for every agent; the three report
prefixes disallowed for every agent. `_qa_tmp/` and `_to_delete/` need no rule, Jekyll already
excludes any path beginning with an underscore.

## Part 6 - isAccessibleForFree on all 83 dispatches

Every BlogPosting carried 19 of the 20 fields worth having and was missing this one. Without it,
nothing in the markup states that the content is not behind a paywall, which is a signal Google uses
and which matters more on a site whose articles are long and whose publisher sells software. Added
as `true` to the BlogPosting node only, anchored so it could not land on the HowTo node in the same
graph. All 83 re-parsed afterwards and the flag confirmed on the right node in each.

## Part 7 - Audit after the changes

| Check | Result |
|---|---|
| JSON-LD parses, all rendered pages | 95 / 95 |
| exactly one h1 | 95 / 95 |
| canonical == filename == og:url | 95 / 95 |
| title <= 60 and unique | PASS, 0 dupes |
| meta description 70-165 and unique | **PASS, 0 failures** |
| description == og == twitter | all but index and 404 (standing item 1) |
| broken internal links | 0 |
| broken in-page anchors | 0 |
| duplicate element ids | 0 |
| CSS brace and style-tag balance, 177 files | 0 failures |
| mojibake | 0 |
| sitemap parses, 94 locs, lastmod agrees with dateModified | PASS (1 documented exception) |
| feed parses, 83 items | PASS |
| orphan rendered pages | 0 |
| markdown alternates present, linked and indexed | 83 / 83 / 83 |
| robots.txt, two independent parsers | PASS |
| BlogPosting isAccessibleForFree | 83 / 83 |

**No render pass this run, and it is not needed.** Every HTML change was diffed against the
pre-run snapshot and classified by position: 173 changed lines across 87 files, **all 173 inside
`<head>`**, zero changes below it. No CSS, no DOM, no copy that a reader sees. The 10-14 render pass
across 8 widths therefore still holds. The device shell has no headless browser, so a render would
have needed the cloud container regardless.

Snapshots: `_qa_tmp/seo-2026-10-16-before.tar.gz` and `_qa_tmp/seo-2026-10-16-after.tar.gz`.

## Part 8 - Needs a decision

1. **Commit and push.** Standing item 0, above everything else in this list. 115 pending changes,
   two days of blog work and two SEO passes. Until this happens none of it is SEO at all.
2. **The blog run writes content and counts but not dates or length caps.** Parts 2 and 3 were both
   generator bugs, not drift. Two checks at source would retire this whole category: reject a meta
   description outside 70-165, and set `dateModified` plus the sitemap `lastmod` on every page the
   run touches, not just the new post.
3. **og:image is still the same banner on all 95 pages.** Unchanged from 10-14 and 10-12. Per-post
   share images would lift click-through from social and from the AI surfaces that show a thumbnail.
   Still a design call plus a batch render job; still worth doing deliberately rather than folding
   into a pass like this one.
4. **Organization `sameAs` resolves nothing.** It lists `https://dugong.live`, which is already the
   node's `url`, so it does no entity-resolution work at all. Real profiles (LinkedIn company page,
   X, GitHub, Crunchbase) are what let a search or answer engine tie the publisher to a known
   organization. A web search this run found no public profiles for Dugong to cite, and inventing
   URLs would be worse than leaving the field thin. Needs someone to supply the real ones.
5. **The guides and the two hub pages still carry no ticker bar.** Unchanged from 10-12 and 10-14:
   the ticker text is maintained by the blog run and a static copy on eleven pages would go stale.
6. **The 37 distinct external links are still unverified.** Both shells are behind proxies that
   refuse help.shopify.com and shopify.dev; this run also could not reach blog.dugong.live itself,
   which is why Part 0 is argued from git rather than from a fetch. Needs a supervised run with open
   egress.
7. **The lead essay has only 3 inbound internal links**, against 83 for the author page and 91 for
   the question index. It is the site's only non-Shopify piece, so the eight guides have no honest
   reason to link it, but 3 is thin for the page the site calls its lead essay. Worth a look next
   time a dispatch touches builder fatigue or no-code limits.
8. **`__deltest.tmp` (2 bytes) and `_to_delete/` are still in the tree.** Harmless, Jekyll excludes
   the underscore directory, but `__deltest.tmp` would be served. Deleting files on this machine
   needs a permission prompt and nobody is at the desk; left for a supervised run.
9. **index.html and 404.html keep hand-written og:title and og:description** that differ from their
   h1 and meta description. Deliberate, both inside the caps. Carried from 10-14.
10. **Aanya Rao still has no author page**, so her `author` node is the only one of 83 without a
    `url`. One dispatch does not make an archive worth indexing; her Person node is typed inline on
    the essay and named in llms.txt. Carried from 10-14.
