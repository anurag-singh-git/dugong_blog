# SEO / GEO report — 2026-06-18

**Post:** The order tag you set by hand
**URL:** https://blog.dugong.live/the-order-tag-you-set-by-hand.html
**Dispatch:** Nº 62 · Author: Priya Singh · Published 2026-06-18

## Target intent

The post is built around the searcher who is feeling the pain directly: someone hand-tagging orders
every morning and looking for a way to stop. The headline names the use case in the searcher's own
frustration ("the order tag you set by hand") rather than a feature name, which is the house pattern.

Primary queries targeted:

- auto tag orders Shopify / automatically tag orders Shopify
- Shopify Flow order tagging multiple conditions
- tag orders for fulfillment routing
- tag order based on order note / line item properties
- order tags is invalid (error)
- Shopify order tagging automation

## On-page SEO

- **Title:** "The order tag you set by hand — Dugong Field Notes" (pain-led, brand suffix consistent).
- **Meta description:** present, in the house SERP-safe range, leads with the limitation and the fix.
- **Canonical:** self-canonical to the absolute URL.
- **Headings:** single H1; H2s map the buyer journey (why a tag is never just a tag → what Shopify
  does and where it stops → why the usual fixes don't hold → what the automation has to do → why it is
  a compiler problem → the workflow worth building). FAQ questions are H2s.
- **Keywords meta + JSON-LD keywords** aligned to the target queries.
- **Internal links:** 14 sibling links in Read-next; in-body contextual links to the field study
  (tagging is 14% of workflows) and the high-risk-flag post. Two siblings now back-link here, so the
  link is reciprocal in the most relevant cluster.
- **Images:** shared OG/Twitter image with descriptive alt; no new raster assets required.

## GEO (generative-engine optimization)

- **FAQPage + HowTo + BlogPosting + BreadcrumbList** JSON-LD, all parsing clean.
- **Speakable** selector covers the title and FAQ.
- Three FAQ answers are written as self-contained, liftable paragraphs that directly answer the
  highest-intent questions an answer engine is likely to quote: "Can Shopify automatically tag
  orders?", "Why do my Shopify order tags come out inconsistent or invalid?", and "Can Shopify Flow
  tag an order based on the order note or line item properties?".
- The 7-step HowTo gives an answer engine a clean, ordered procedure to summarize.
- The llms.txt entry is a long, fact-dense, self-contained summary so a model reading the corpus can
  represent the post without fetching the page.

## Distribution / indexation

- Added to sitemap.xml (priority 0.9) and feed.xml (newest item); homepage lastmod bumped.
- Topics cloud now points two tags at the post ("order tags", "order routing").
- robots.txt unchanged (already allows crawl + points to sitemap).

## Facts grounded in research (not invented)

- Shopify Flow is free on every plan and tags well on a single condition; multi-condition tagging
  requires stacking workflows.
- Flow can reference note attributes / line item custom attributes but cannot interpret a free-text
  note.
- "order tags is invalid" errors arise from invalid characters or length; tag casing fractures
  segments.
- Admin API does not allow editing line item properties on an existing order, only order-level tags
  and notes.
- Tags are the connective tissue for routing, downstream flows, segments, exports, and email
  platforms.

## Style compliance

- No em or en dashes in authored prose (body, dek, meta, FAQ, cards, feed item, llms entry). Remaining
  em dashes are template-level only and consistent across all posts.
