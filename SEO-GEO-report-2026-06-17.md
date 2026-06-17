# Dugong Field Notes — SEO/GEO improvement run

**Date:** 2026-06-17 · **Scope:** blog.dugong.live (index + 13 posts + sitemap/feed/llms/robots)
**Mode:** automated scheduled task (run without user present)

## Headline

No morning blog run shipped today, so the baseline was the fully-closed state from yesterday's
second pass: 13 posts, complete internal link graph, valid schema, balanced HTML. The standard
defect classes were all clean on audit, so this pass spent its effort on the single largest
carried-over GEO opportunity that every prior report has flagged and deferred: the ordered "AI
playbook" each post lays out in prose was visible to readers but invisible to machines. This run
captured those sequences as `HowTo` structured data. Twelve of the thirteen posts now expose their
step-by-step procedure as schema, 82 steps in total, each mapped to the on-page playbook block.

## State at start of run

Audit of index + 13 posts + discovery surfaces found no defects:

- Meta descriptions: all 13 posts in the 146–160 character SERP-safe range; homepage at 100. No fix.
- Internal link graph: every post links exactly 12 unique siblings, zero self-links. No fix.
- Structured data: 1 `ld+json` block per post, all parse; each carried `BlogPosting` +
  `BreadcrumbList` + `FAQPage`. Canonical, Open Graph, and Twitter tags present on all 13. No fix.
- HTML structure: `<div>` balanced on every post (64/64) and on index (149/149). No fix.
- XML: `sitemap.xml` (14 URLs) and `feed.xml` (14 items) both well-formed and current. No fix.
- `llms.txt`: 13 article entries present. No fix.

The gap was the absence of step-level structured data. Each post renders its playbook as a visible
`<pre><code>` block with a numbered sequence (6 or 7 steps), but nothing told a search or generative
engine that those lines are an ordered procedure.

## Changes made

**Added `HowTo` schema to the 12 procedure posts.** Each post's existing JSON-LD `@graph` gained a
fourth node, a `HowTo` object whose `step` array is built directly from the numbered lines already
visible in that post's playbook block. Step `text` is the on-page wording verbatim; each step also
carries a short `name` label, a `position`, and a `url` pointing at the playbook anchor. The `HowTo`
itself carries the post headline as `name`, the post's own "The AI playbook that…" line as
`description`, `inLanguage`, and `totalTime` matching the post's declared reading time. Because the
steps mirror content the reader already sees, the markup is faithful, not invented.

**Anchored the playbook block.** Added `id="playbook"` to the first `<pre>` element in each of the
12 posts so the `HowTo` step `url` fragments resolve to the real on-page section.

**Skipped the pillar post.** `the-shopify-automations-no-one-builds.html` is an overview that lists
many automations rather than describing one ordered procedure, so it has no single playbook to
model. It keeps its `BlogPosting` + `BreadcrumbList` + `FAQPage` and was left unchanged. Forcing a
`HowTo` onto a non-procedural post would be the kind of mismatched markup that hurts trust.

**One punctuation normalization.** A single `HowTo` step on the high-risk-flag post reproduced an em
dash from the on-page prose. Since the JSON-LD is content authored in this run, the dash was
replaced with a comma (meaning unchanged) to honor the no-dash style. The post body prose was not
touched.

No article body text, titles, `datePublished`/`dateModified` values, word counts, meta
descriptions, FAQ content, link graph, or discovery surfaces were changed.

## Verified

- **Structured data.** All 13 posts: every `ld+json` block parses. The 12 procedure posts now carry
  `['BlogPosting','BreadcrumbList','FAQPage','HowTo']`; the pillar post correctly carries the three
  without `HowTo`. Index unchanged (`WebSite`,`Organization`,`Blog`).
- **HowTo integrity.** 82 steps across 12 posts; every step has `position`, `name`, and `text`, and
  every step `url` ends in `#playbook` with a matching `id="playbook"` present on the page.
- **Link graph.** All 13 posts still link exactly 12 unique siblings, zero self-links.
- **HTML structure.** `<div>` still balanced on every post (64/64) and index (149/149); adding
  `id="playbook"` and JSON-LD nodes changed no div counts.
- **Meta descriptions.** All 13 still within 146–160 characters.
- **XML.** `sitemap.xml` and `feed.xml` still well-formed; counts unchanged (14/14).
- **Style preference.** Zero em or en dashes in any authored `HowTo` markup across all 12 posts
  (confirmed by scan). The `→` arrows that appear in a few step texts are verbatim from the on-page
  playbook prose, kept for fidelity with the visible content.

## Decisions made autonomously (no user present)

- **HowTo over generic ItemList.** `HowTo` is the more specific type for an ordered, actionable
  procedure and is what generative engines parse for "how do I…" answers, which is the GEO target
  here. Steps map one-to-one to visible content, satisfying the on-page-correspondence requirement.
- **Freshness fields left as-is.** Consistent with house behavior, `dateModified` /
  `article:modified_time` were not bumped for the additive schema change.
- **Surgical insertion, no reformatting.** The `HowTo` node was inserted into each `@graph` without
  reserializing the existing markup, keeping the diff limited to the new content.
- **No git commit or deploy.** All edits are staged in the working tree for review, consistent with
  every prior run.

## Suggested next (for a human or a future run)

- **Fold HowTo into the blog-run step.** New posts ship with a visible playbook but no `HowTo`. Add
  the node and the `id="playbook"` anchor at authoring time so this no longer needs a follow-up pass,
  the same recommendation made about back-links.
- **Validate in a rich-results tester.** A human with browser access can confirm the `HowTo` and
  `FAQPage` markup against Google's and Schema.org's validators on a couple of live URLs.
- **Back-link automation still open.** The recurring "new dispatch ships with partial back-links"
  pattern remains the other standing item for the blog-run step to absorb.
