# Dugong Field Notes — SEO/GEO follow-up run

**Date:** 2026-06-18 (second pass) · **Scope:** blog.dugong.live (15 posts + index + sitemap/feed/llms/robots)
**Mode:** automated scheduled task, "do all the required fixes" follow-up to the morning run

## Headline

The morning run published Dispatch Nº 62 ("The order tag you set by hand") and wired its discovery
surfaces (sitemap, feed, llms.txt, homepage) plus full structured data, but back-linked it from only
the two most related siblings. This pass closed the back-link graph: every older post now links Nº 62.
After this run the internal link graph is complete again at 14 siblings per post across all 15 posts.

## State at start of pass

- Nº 62 already carried complete structured data: `BlogPosting` + `BreadcrumbList` + `FAQPage` +
  `HowTo` (7 steps) in its JSON-LD `@graph`, with the `id="playbook"` anchor present and resolving.
- Nº 62 already appeared in sitemap.xml (16 URLs), feed.xml (16 items), llms.txt, and the homepage.
- Only 2 of 14 older siblings back-linked Nº 62 (the order-change post with a contextual dek and the
  pillar overview with a field-study dek). The other 12 siblings linked 13 of 14 siblings, missing
  Nº 62. So the link graph was incomplete by 12 edges.

## Changes made

**Completed the back-link graph for Nº 62.** Inserted a standard Nº 62 Read-next card as the first
card in the related-grid of the 12 older posts that did not yet link it. The card uses the house card
markup (research tag, 9 min read, title, dek, JUN 18 / P. Singh footer) and a self-contained,
non-relative dek written for the no-dash style:

> Order tags route fulfillment, segments, and downstream flows, but Shopify Flow tags on one
> condition and cannot read the note, so they get set by hand. The AI playbook that reads the whole
> order and tags it.

The two siblings that already carried a tailored, contextual Nº 62 card (order-change and the pillar)
were left as-is so their more specific copy is preserved. After the edits, every one of the 15 posts
links exactly 14 unique siblings, Nº 62 is linked once from every other post, and no post links
itself in a Read-next card.

No article body text, titles, dates, word counts, meta descriptions, FAQ content, structured data, or
discovery surfaces were changed in this pass. The only edit per file is the single inserted card.

## Verified

- **Link graph.** All 15 posts link exactly 14 unique siblings; zero self-links in Read-next cards;
  Nº 62 back-linked from all 14 other posts.
- **Structured data.** Every `ld+json` block on all 15 posts and the index still parses. Nº 62 keeps
  `['BlogPosting','BreadcrumbList','FAQPage','HowTo']` with 7 HowTo steps and a resolving
  `#playbook` anchor.
- **HTML structure.** `<div>` balanced on all 12 edited posts (70/70 each).
- **Style.** Zero em or en dashes in the 12 inserted cards.
- **Discovery surfaces.** sitemap.xml and feed.xml are well-formed XML, 16 URLs / 16 items each
  (homepage + 15 posts).

## Decisions made autonomously

- **Standard dek for the 12, tailored deks left intact.** A single self-contained dek keeps the card
  consistent across siblings and reads correctly regardless of which post it sits on; the two
  pre-existing contextual cards were already better-targeted, so they were preserved.
- **Card inserted as first related card.** Matches the house pattern of leading the Read-next grid
  with the newest dispatch, the same placement used for Nº 61 in the prior run.
- **No git commit or deploy.** All edits are staged in the working tree for review, consistent with
  prior runs.

## Suggested next

- **Move full back-link insertion into the morning blog run.** The new post already ships with HowTo
  and the playbook anchor; folding the 14-sibling back-link insertion into authoring time would
  remove this daily follow-up entirely.
