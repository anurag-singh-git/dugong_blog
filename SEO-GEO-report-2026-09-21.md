# SEO / GEO report - 2026-09-21

Scheduled autonomous run. Last SEO/GEO pass: 2026-09-20.

## Part 1 - Two dispatches are finished and not live

Checked live this run:

| Source | Result |
|---|---|
| `blog.dugong.live/sitemap.xml` newest `lastmod` | 2026-09-19 |
| local `HEAD` vs `origin/main` | both `093f9f1` (Sep 19) |
| working tree | 89 changed files, uncommitted |

The deploy pipeline is healthy (the 09-19 `.nojekyll` fix held). The problem this time is simply that
nothing has been pushed since Sep 19. Nº 120 (Flow silent failures) and Nº 121 (daily order capacity),
their sitemap, feed, llms entries and sibling mesh, and today's fixes are all sitting locally. No crawler
or answer engine can see them until this runs:

    git add -A && git commit -m "Nº 120, Nº 121 + SEO/GEO 2026-09-20/21" && git push

Housekeeping: a `git status` at the start of this run left a stale zero-byte `.git/index.lock` that
the sandbox cannot delete. It was moved to `_to_delete/git-index.lock-stale-2026-09-21`, so git is not
blocked. `_to_delete/` can be emptied by hand.

## Part 2 - Fixes made this run

1. **Nº 121 BlogPosting `description` was two descriptions glued together.** The dek and the meta
   description had been concatenated, so the structured-data summary repeated "Shopify has no daily
   order limit" twice. Trimmed to the dek. This is the field answer engines most often lift as the
   one-line summary, so the duplication mattered more than it looks. Only Nº 121 had it (checked all 74).
2. **og:description trimmed on 63 pages.** These carried the full llms.txt abstract, 1,300 to 2,700
   characters, into Open Graph. Facebook, LinkedIn, Slack and iMessage cut this off after one or two
   lines, mid-sentence, so every share preview was a truncated wall of text. Each now matches that
   page's meta description (all at or under 160 characters, already unique site-wide). Twitter
   descriptions were already short and are untouched. The long abstracts still live where they help
   GEO: BlogPosting `description`, llms.txt and llms-full.txt.

## Part 3 - Audit

Recomputed from the files: 77 rendered pages (74 wired posts + index + 2 noindexed rejected drafts),
74 redirect stubs.

| Check | Result |
|---|---|
| JSON-LD parses, all rendered pages | PASS |
| FAQ parity, visible vs FAQPage JSON (questions and answers) | 74 / 74 |
| canonical == filename; one h1; img alt | PASS |
| duplicate titles / meta descriptions; meta desc <= 160 | 0 / 0 / PASS |
| broken internal links | 0 |
| sitemap: 75 locs, 0 dupes, 0 ghosts; every post in feed, llms.txt, llms-full.txt, index | PASS |
| Nº 121: BlogPosting + Breadcrumb + FAQPage (5) + HowTo (7, `#playbook`), 4 citations, stub, 73-post mesh | PASS |

Nº 121 source check, re-verified live today: the Shopify Community thread is dated August 22, 2026
with the 20-orders-a-day example and the permalink, CSS and midnight-reset replies as quoted; the Flow
Scheduled time trigger is limited to once every 10 minutes and defaults to store time zone. Both match
the post.

## Part 4 - Noted, not changed

- 57 `<title>` tags run past 70 characters once " | Dugong Field Notes" is appended. Google shows
  roughly 60 and will rewrite or truncate. Worth a deliberate pass (drop the suffix on long titles, or
  shorten to "| Dugong") rather than a scripted one, because titles are the highest-stakes string on
  the page.
- Em dashes appear only inside CSS comments of the shared template (76 files). Invisible to readers
  and crawlers; left alone.
- Carried forward: multi-location inventory rebalancing (still thin); the homepage featured card still
  promotes the May 28 essay, which has no URL of its own.
