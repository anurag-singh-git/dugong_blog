# SEO / GEO report — 2026-06-16

**Post:** The sale you have to start by hand · `the-sale-you-start-by-hand.html` · Dispatch Nº 60

## Target intent

Primary query cluster: "Shopify schedule sale," "schedule price change Shopify," "Shopify sale
start and end time," "auto revert price after sale," "compare at price strikethrough," "flash
sale automation Shopify," "bulk sale scheduler." These are high-intent, problem-aware merchant
searches, and the recurring community threads confirm the gap is real and unmet natively.

## On-page SEO

- **Title (55 chars):** "The sale you have to start by hand — Dugong Field Notes."
- **Meta description (~152 chars):** leads with the native gap (can't schedule, revert, or run by
  rule) and the by-hand-at-midnight pain, ends on the AI playbook. Within the ~160 SERP limit.
- **Canonical** set to the live absolute URL; **robots** index,follow with large-image preview.
- **Keywords meta** covers schedule sale, scheduled price change, flash sale automation, compare
  at price, bulk price edit, sale scheduler, timed discount, automatic price revert.
- **Headings** map to the query journey: how big the timed sale is → what Shopify does and where
  it stops → why the usual fixes don't hold → what the automation has to do → compiler vs app →
  the workflow worth building.
- **Internal links:** the body links the overselling, sold-out, abandoned-cart, and Shopify-
  automations posts; two siblings now back-link the new post, tightening the topical cluster.

## GEO (generative-engine optimization)

- **FAQPage schema** with three questions phrased the way users ask an assistant: "Can Shopify
  schedule a sale to start and end automatically?", "Why not just use a discount code instead of
  changing prices?", "What goes wrong when you run a timed sale by hand?" Each answer is a
  self-contained, quotable paragraph an LLM can lift verbatim.
- **BlogPosting schema** with description, wordCount (1870), timeRequired (PT9M), author, and
  `about` entities (Shopify, Promotion (marketing), Business process automation) for entity
  grounding.
- **speakable** selectors on `.article-title` and `.faq`.
- **BreadcrumbList** for context.
- **llms.txt** carries a long, fact-dense entry (native gaps, the four workarounds and how each
  breaks, the flash-sale stats, and the seven-step playbook) so text-only crawlers get the full
  argument without parsing HTML.
- **Direct-answer framing:** the lede and the first sentence under each H2 state the claim plainly
  before elaborating, which favors extractive answer engines.

## Distribution surfaces updated

- sitemap.xml (14 URLs, new post at priority 0.9, homepage lastmod bumped)
- feed.xml (14 items, new post newest, lastBuildDate bumped)
- llms.txt (entry added after the lead essay)
- index.html (featured card, JSON-LD blogPost entry, topic-cloud tags, counts)

## Notes / next passes

- Complete back-links to Nº 60 from the remaining eleven siblings over subsequent runs.
- Consider a future post on scheduled storefront/theme or content changes (banners, homepage
  swaps) as a sibling to this pricing-schedule angle if community demand supports it.
