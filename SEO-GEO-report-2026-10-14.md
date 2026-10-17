# SEO / GEO report - 2026-10-14

Scheduled autonomous run. Last SEO/GEO pass: 2026-10-12. The 10-12 and 10-13 work is now live:
`HEAD` was `8e5c9e3`, in sync with `origin/main`, working tree clean at the start of this run, so
the topic guides, the webfont fix and the spelling pass all reached crawlers. That clears standing
item 5 of the 10-12 report and standing item 8 of the 10-13 QA report.

Field-level SEO on this site has been finished work for two passes. The three items this run took
on are the ones every recent report has carried forward as architecture rather than markup, plus
one new one: the site answered 403 questions and had no page that said so.

**The tree moved under this run.** The blog-generation session published dispatch Nº 127,
`how-to-catch-shopify-orders-where-half-the-order-never-ships.html`, at 21:18 UTC, partway
through. Every change below was a read-modify-write against the live file, nothing was clobbered
in either direction, and the new dispatch was folded into all of it before the final audit: it
carries the FAQ ids, the question-index link, the linked byline, the author URL in its JSON-LD,
and both CSS fixes. All figures below are the settled 175-file tree.

## Part 1 - The lead essay finally has a URL

Carried as "the single largest remaining win" in every report since at least 09-21. "The death of
the drag-and-drop builder", Dispatch Nº 47, 820 words, Aanya Rao, 2026-05-28, existed only as a
hidden `<div id="view-post">` inside index.html, shown by a JS view toggle. Its JSON-LD `url` was
`https://blog.dugong.live/#view-post`, llms.txt and feed.xml both pointed at the homepage, and the
two posts that cite it in prose linked to `index.html`. It could not rank for its own query, could
not be cited on its own, and its 820 words competed with the homepage's own subject.

Why this did not need the supervised run it was waiting for: the essay was never visible homepage
content. It was a second view behind a click, so moving it to its own page removes nothing a reader
sees. The homepage is 15,017 characters lighter and renders identically.

`the-death-of-the-drag-and-drop-builder.html` is now a real page built from the standard article
template, so it is byte-identical to the other 80 posts in head, nav, ticker, related and footer.
Not one word of the essay was rewritten; the only copy change is the trailing period dropped from
the h1, so the headline matches the JSON-LD and the homepage card, which every other post holds to.
It carries a full BlogPosting (headline, description, dates, articleSection, keywords, wordCount
820, timeRequired PT4M, image, three `about` Things, speakable, typed author and publisher) and a
two-level BreadcrumbList. Two levels, not three: the eight guides are all Shopify operations and
this essay belongs to none of them, so inventing a parent would have been worse than the honest
shape.

Wired in six directions: the homepage featured card (the `data-nav` toggle is gone, it is an
ordinary link), the homepage Blog node's own BlogPosting entry, sitemap.xml, feed.xml (`<link>` and
a permalink `<guid>` in place of the `#dispatch-47` fragment), both llms.txt entries, and the two
in-prose citations in the field-study and WISMO posts, which pointed at index.html and now point at
the essay. **llms-full.txt gained the essay's complete 811-word text**, which it had never carried:
the file's own header said the essay "lives at https://blog.dugong.live/ and is summarized in
llms.txt". An answer engine reading that file can now quote the piece instead of a summary of it.

## Part 2 - A question index, the site's 403 answers in one place

Eighty dispatches end with the questions merchants actually ask about that failure mode, answered
in full on the page: 403 of them, every one unique, every one a long-tail query someone types. None
of them had an address. The only way to reach the answer to "why does my Shopify product show sold
out when I have stock on the shelf" was to already be on the right post.

Two changes fix that. First, **every FAQ item on all 80 posts now carries a stable id**, `faq-1`
through `faq-n`, so each answer has its own fragment. Nothing visible changed; 403 new anchor
targets exist.

Second, `shopify-automation-questions.html` lists all 403, grouped into the eight topic guides and,
within a guide, by dispatch newest first. Every question is a link straight to the paragraph that
answers it. No answer text is duplicated onto the hub, so it competes with nothing: it is an index,
and the answers stay on the pages that earned them. Schema is a CollectionPage, a two-level
BreadcrumbList and an ItemList naming all 403 questions with their deep links, which is the shape an
answer engine can read in one fetch.

It is reachable from 89 places: the homepage topic-guides section, all eight guides, and the end of
every post's FAQ block, where it reads "every question this blog answers →". In sitemap.xml and in
llms.txt, which gained a "## Question index" section above the full index.

## Part 3 - An author entity that resolves

Every post's author was `{"@id": ".../#priya-singh"}` pointing at a homepage section. Correct, but
thin: 80 dispatches by one researcher, and no page a search or answer engine could resolve the
author to. Author provenance is what E-E-A-T is made of and what AI answers cite.

`priya-singh.html` is an author archive: the bio already published in the homepage ABOUT THE AUTHOR
block, verbatim, nothing invented, over all 80 dispatches newest first with each card carrying that
post's own og:title and meta description. Schema is a ProfilePage whose `mainEntity` is the existing
Person `@id`, so this is the same entity the 80 posts already reference, not a second one. The
Person node gained `url`, `mainEntityOfPage` and two more `knowsAbout` terms.

Every post's byline name is now a `rel="author"` link to it, and its JSON-LD author node gained the
matching `url`, so the markup and the visible page agree. 81 inbound links. The homepage author
block links to it too, and llms.txt gained an "## Authors" section naming both Priya Singh and Aanya
Rao with their pages.

## Part 4 - Two mobile defects, both found by render and both fixed

1. **The question index overflowed the viewport at every phone width**, 222 px at 320. The guide
   section headings ("◆ SHOPIFY SHIPPING AND FULFILLMENT AUTOMATION · 82 QUESTIONS") inherit
   `flex-shrink: 0` from the site's `.section-eyebrow`, which is fine for the short eyebrows
   everywhere else and not fine for these. Overridden inside `.qa-section` only; the rest of the
   tree is untouched.
2. **`.hub-more` was a 20 px tap target on all 81 pages that carry it**, and the new byline link
   would have been 16 px. Both are now 24 px, via `line-height` so the underline still sits under
   the text rather than 4 px below it. Marked `SEO 2026-10-14` in the stylesheet of every file it
   touches. This also removes a pre-existing WCAG 2.5.8 miss that predates this run.

## Part 5 - Audit after the changes

Recomputed from the files: 175 HTML files, 92 rendered (81 posts, 8 guides, the question index, the author
page and index.html), 83 stubs (81 redirect stubs, 404.html, and the one that shipped with
dispatch Nº 127).

| Check | Result |
|---|---|
| JSON-LD parses, all rendered pages | 92 / 92 |
| exactly one h1 | 92 / 92 |
| JSON-LD headline == h1 | all posts |
| canonical == filename == og:url | 92 / 92 |
| description == og == twitter | all but index and 404 (standing item 1) |
| title <= 60 and unique | PASS, max 60, 0 dupes |
| meta description 70-165 and unique | PASS, 100 to 165, 0 dupes |
| broken internal links | 0 |
| broken in-page anchors, including all 403 new FAQ deep links | 0 |
| duplicate element ids | 0 |
| webfont stylesheet present | 92 / 92 |
| CSS brace and style-tag balance after the patches, 175 files | 0 failures |
| replacement characters / mojibake | 0 |
| sitemap 92 locs, 0 dupes, 0 ghosts, parses | PASS |
| feed.xml parses; stubs absent from sitemap, feed, llms | PASS |
| every post in feed, llms.txt, llms-full.txt | PASS |
| orphan pages (no inbound links) | 0 |
| headless render, 10 pages x 8 widths (320 to 1920) | 0 horizontal overflow, 0 page errors, 0 text under 12 px, 0 tap targets under 24 px |

The 10 rendered pages are the three new ones, index.html, a guide, three posts spanning the
template variants, and the new dispatch. Before and after snapshots are in
`_qa_tmp/seo-2026-10-14-before.tar.gz` and `_qa_tmp/seo-2026-10-14-after.tar.gz`.

## Part 6 - Not changed, needs a decision

1. **og:image is still the same banner on all 92 pages.** Per-post share images would lift
   click-through from social and from the AI surfaces that show a thumbnail. 81 images is a batch
   job with a design call in it (what goes on the card), and the renderer lives in the cloud
   container rather than on this machine, so it is worth doing deliberately rather than folding
   into a pass like this one.
2. **The guides and the two new hub pages carry no ticker bar.** Unchanged from 10-12: the ticker
   text is maintained by the blog run and a static copy on eleven pages would go stale. Worth
   folding into the blog run's template pass if the strip should be everywhere.
3. **The 37 distinct external links are still unverified.** Both shells are behind proxies that
   refuse help.shopify.com and shopify.dev. Carried from the 10-13 QA report, including the
   `cancelling-orders` URL that appears to redirect to its parent. Needs a supervised run with open
   egress.
4. **index.html and 404.html keep hand-written og:title and og:description** that differ from their
   h1 and meta description. Deliberate, both inside the caps.
5. **Aanya Rao has no author page.** One dispatch does not make an archive worth indexing. Her
   Person node is typed inline on the essay and named in llms.txt, which is enough for entity
   resolution; revisit if she writes more.
