# Dugong Field Notes — SEO/GEO improvement run

**Date:** 2026-06-17 · **Scope:** blog.dugong.live (index + 14 posts + sitemap/feed/llms/robots)
**Mode:** automated scheduled task, then a follow-up "do all the required fixes" pass

## Headline

This run did two things. First, it captured the ordered "AI playbook" each post lays out in prose
as `HowTo` structured data, the largest carried-over GEO opportunity from prior reports. Second, a
morning blog run published a 14th post mid-session (Dispatch Nº 61, "The meta description you write
one at a time"), so the pass also completed everything that post needed to be fully optimized and
discoverable: HowTo schema on the new post, and back-links to it from every older sibling. A minor
on-page fix was folded in as well: the homepage now has a single H1.

After this run, all 13 procedure posts (every post except the pillar overview) expose their
step-by-step playbook as `HowTo` schema, the internal link graph is complete at 13 siblings per
post, and the homepage heading hierarchy is clean.

## State during the run

The pass began against 13 posts. Standard defect classes were clean (meta lengths 146-160, complete
link graph, valid `BlogPosting` + `BreadcrumbList` + `FAQPage` per post, balanced HTML, valid XML).
The gap was step-level structured data, so `HowTo` was added to all 12 procedure posts. Partway
through, a concurrent blog run published Nº 61 and rewired the homepage, sitemap, feed, llms.txt,
and JSON-LD, and back-linked the new post from the two most related siblings (the sold-out and
shopify-automations posts). That left the standard new-post gaps to close.

## Changes made

**`HowTo` schema on all 13 procedure posts.** Each post's JSON-LD `@graph` gained a `HowTo` node
whose `step` array is built directly from the numbered lines visible in that post's playbook block.
Step `text` is the on-page wording; each step also carries a short `name` label, a `position`, and a
`url` pointing at the playbook anchor. The `HowTo` carries the post headline as `name`, the post's
own "The AI playbook that…" line as `description`, `inLanguage`, and `totalTime` matching the
declared reading time. Because steps mirror content readers already see, the markup is faithful, not
invented. Total: 89 steps across 13 posts (the new post added 7).

**Playbook anchors.** Added `id="playbook"` to the first `<pre>` in each of the 13 procedure posts
so the `HowTo` step `url` fragments resolve to the real on-page section.

**Completed the back-link graph for Nº 61.** Inserted the standard Nº 61 Read-next card (markup and
copy lifted verbatim from the card the sold-out post already carried) as the first card in the
Read-next grid of the 11 older posts that did not yet link it. After the edits every one of the 14
posts links to exactly 13 unique siblings, with the Nº 61 link present once per older post and no
self-links.

**Single H1 on the homepage.** The homepage carried two H1s: the hero title and the embedded
featured essay ("The death of the drag-and-drop builder"). The featured essay's title was changed
from `<h1 class="article-title">` to `<h2>`. The element is styled entirely by class (no bare `h1`
CSS rule exists), so the change is visually identical and leaves one H1 on the page.

**Skipped the pillar post.** `the-shopify-automations-no-one-builds.html` is an overview that lists
many automations rather than one ordered procedure, so it has no single playbook to model. It keeps
`BlogPosting` + `BreadcrumbList` + `FAQPage` and was left unchanged.

**Punctuation normalization.** Two `HowTo` step texts reproduced an em dash from on-page prose.
Since the JSON-LD is content authored in this run, the dashes were replaced with commas (meaning
unchanged) to honor the no-dash style. Post body prose was not touched.

No article body text, titles, dates, word counts, meta descriptions, FAQ content, or discovery
surfaces were otherwise changed.

## Verified

- **Counts.** 14 posts; 13 carry `HowTo` (pillar correctly excluded); sitemap 15 URLs and feed 15
  items (homepage + 14 posts), both well-formed XML.
- **Structured data.** Every `ld+json` block on all 14 posts and the index parses. The 13 procedure
  posts carry `['BlogPosting','BreadcrumbList','FAQPage','HowTo']`.
- **HowTo integrity.** 89 steps total; every step has `position`, `name`, and `text`; every step
  `url` ends in `#playbook` with a matching `id="playbook"` on the page; zero em or en dashes in any
  authored HowTo markup.
- **Link graph.** All 14 posts link exactly 13 unique siblings, zero self-links; Nº 61 is linked
  once from every older post.
- **HTML structure.** `<div>` balanced on every post and on index (152/152). Homepage now has
  exactly one H1.
- **Discovery surfaces.** All 14 posts appear in sitemap, feed, llms.txt, and the homepage.

## Decisions made autonomously

- **HowTo over generic ItemList.** The more specific type for an ordered, actionable procedure and
  what generative engines parse for "how do I…" answers. Steps map one-to-one to visible content.
- **Completed Nº 61 wiring rather than waiting a day.** Since the new post landed mid-session,
  closing its back-link graph and adding its HowTo now avoids the usual one-day follow-up.
- **Homepage H1 fix made, design untouched.** A duplicate H1 is a low-risk on-page SEO item; the
  fix is a tag change with no visual effect. The featured card layout and copy were left as-is.
- **No git commit or deploy.** All edits are staged in the working tree for review, consistent with
  prior runs.

## Suggested next

- **Fold HowTo + anchor into the blog-run step.** New posts ship with a visible playbook but no
  `HowTo`; generating the node and `id="playbook"` at authoring time would remove this follow-up,
  the same way full back-link insertion should move into the blog run.
- **Validate in a rich-results tester.** A human with browser access can confirm the `HowTo` and
  `FAQPage` markup on a couple of live URLs.
