# SEO / GEO report - 2026-09-20

Scheduled autonomous run. Last SEO/GEO pass: 2026-09-19.

## Part 1 - The deploy is fixed

The item that dominated the last three reports is closed. Checked live this run:

| Source | Result |
|---|---|
| `blog.dugong.live/sitemap.xml` newest `lastmod` | 2026-09-19 |
| `blog.dugong.live/how-to-restrict-shopify-products-from-shipping-to-certain-states.html` | 200, real page, "Dispatch Nº 119" |
| local `HEAD` vs `origin/main` | both `093f9f1` |

The `.nojekyll` file added on 09-19 was the right diagnosis. GitHub Pages is rebuilding from pushes
again, and the three dispatches that spent three weeks returning 404 are being served. Nothing
further is needed here beyond committing the current tree.

## Part 2 - Dispatch Nº 120 target surface

Primary query cluster, all low-competition and currently owned by forum threads and help docs
rather than editorial:

- shopify flow not working
- shopify flow workflow failed
- shopify flow completed but not working
- shopify flow error notification
- shopify flow run history
- shopify flow rate limited
- workflow failed silently shopify

What is on page one for these today: two Shopify Help Center pages, three Shopify community or
developer-forum threads, two app-vendor diagnostic pages. No publisher has written the connective
argument, which is that the four documented behaviours compound. The post is built to be that
argument, and it states each behaviour with the number attached, which is what gets quoted.

## Part 3 - GEO surface

Generative engines quote specifics. This dispatch carries, in the body and repeated in the FAQ:

- Five run statuses with their exact documentation definitions, including Completed defined as
  the single word "done"
- 14 days of run retention, stated twice (storage and search)
- 30 days and one notification per workflow version for the error trigger
- 1,000 workflows, 40 wait steps, 90 days of wait, 36 hours per section, 50 kB per config field,
  100 objects per Get data action
- Four dated community threads (September 26, 2024; April 1 to 3, 2025; May 29 to 30, 2025;
  February 3 to 9, 2026) with near-verbatim quotes and two Shopify staff answers
- One changelog date (March 24, 2026) and one Shopify blog date (December 12, 2025)

Structured data: BlogPosting with `citation` (5 sources), `about` (Observability (software),
Business process automation, Shopify), `speakable` on `.article-title` and `.faq`; BreadcrumbList;
FAQPage with 5 questions byte-matching the visible FAQ; HowTo with 7 steps anchored to `#playbook`.
The llms.txt entry and the full llms-full.txt text landed this run, both newest-first.

The FAQ questions are written as the questions people actually type, not as headings: "Why does
Shopify Flow say Completed when my workflow did not work?", "How long does Shopify Flow keep
workflow run history?", "How do I tell if a Shopify Flow workflow has stopped running entirely?".
Each answer opens with the answer and then the evidence, which is the shape assistants extract.

## Part 4 - Internal linking

- Nº 120's card is now at the top of the related grid in all 72 prior wired posts.
- Nº 119's mesh was never run yesterday. Repaired this run: its card is now present exactly once in
  all 72 siblings, up from 4 files.
- Six topic-cloud entries added: flow monitoring, silent failures, workflow runs for Nº 120, and
  state restrictions, shipping profiles, checkout validation for Nº 119.
- Nº 120's own grid points at supplier feeds, inventory drift, state restrictions, shipping
  dimensions, duplicate SKUs, ShipStation sync, confirmation emails, overselling, and the pillar.
  The first two are the strongest topical pairs: both are dispatches about an automation that ran
  and still produced the wrong result.

## Part 5 - Carried forward

- Multi-location inventory rebalancing. Still thin, still in demand.
- Missing COGS / cost-per-item and profit reporting. Analytics-vendor editorial is thick; would
  need an angle they do not have.
- Resale-certificate expiry for B2B tax exemption. Examined this run and dropped: four app sites
  and two 2026 guides already cover it, which fails the thin-content test.
- The homepage featured card, still promoting a May 28 essay that has no URL of its own.
