# SEO / GEO report — Dugong Field Notes (2026-06-21)

**Post:** Dispatch Nº 65 — "The repeat customer your store treats like a stranger"
`the-repeat-customer-your-store-treats-like-a-stranger.html`

## Target intent

Shopify merchants searching for how to recognise and act on repeat / VIP / lapsing customers:
auto-tag customers, customer segmentation, VIP tagging, find repeat buyers, win-back churning
customers, Shopify Flow customer tag limits. The heading leads with the felt pain ("treats like a
stranger") and carries the searched phrase "repeat customer."

## On-page SEO

- **Title tag:** "The repeat customer your store treats like a stranger — Dugong Field Notes" (matches
  the house pattern).
- **Meta description:** ~163 chars, inside the SERP-safe band, states the native gap and the fix,
  uniquely worded versus every other post.
- **Canonical:** self-referential to the live HTTPS URL.
- **Keywords meta / OG / Twitter:** populated and consistent; OG/Twitter titles and a fuller OG
  description set for share cards.
- **Heading hierarchy:** single H1 article title; H2 section heads; FAQ questions as H2 inside the FAQ
  block, consistent with siblings.
- **Internal links:** body links the order-tag post (closest sibling), the abandoned-cart post, and the
  "automations no one builds" field study; Read-next links 17 siblings + index. Two siblings now
  back-link this post as their first Read-next card, and the topics cloud adds two entries.

## GEO (generative / answer-engine optimisation)

- **FAQPage schema** with three questions phrased the way users ask them ("Can Shopify automatically tag
  customers?", "How do I find repeat or VIP customers in Shopify?", "Why isn't tagging customers by total
  spend enough?"), each answered in a self-contained, quotable paragraph.
- **HowTo schema** with the 7-step playbook, so an answer engine can lift the procedure directly.
- **BlogPosting + BreadcrumbList** schema with `about` entities (Shopify, Market segmentation, Customer
  lifetime value) and a `speakable` selector on the title and FAQ.
- **Quotable, fact-led prose:** the recency/frequency/monetary framing, the "two customers, same six
  hundred dollars" contrast, and the "VIP who went quiet is your most recoverable customer" line are
  written as standalone claims an LLM can cite.
- **llms.txt:** a long, self-contained entry added at the top of the Articles list so models crawling the
  plain-text index get the full argument and the playbook without parsing HTML.

## Discoverability wiring

- Added to `sitemap.xml` (priority 0.9, lastmod 2026-06-21); homepage lastmod bumped.
- Added to `feed.xml` as the newest item with a full descriptive summary; `lastBuildDate` bumped.
- Featured as the `card-tall` on the homepage; JSON-LD `blogPost` array updated (now 19 entries).

## Distinctness check vs existing catalog

Distinct from the order-tag post (per-order tagging from one order's contents) because this is
customer-lifecycle segmentation read across a customer's whole history. Distinct from the abandoned-cart
and restock posts (which act on a single event) because this maintains a living label on the customer.
No keyword cannibalisation: the primary phrases (customer segmentation, VIP tag, repeat customer,
auto-tag customers) are not the primary target of any existing dispatch.

## Sources

- https://www.appifycommerce.com/blog/10-customer-tagging-rules-every-shopify-store-needs-2026/
- https://speedboostr.com/tag-customers-in-shopify/
- https://www.getmesa.com/blog/shopify-tags/
- https://easysellapp.com/blogs/wiki/shopify-customer-tags-segmentation-guide
- https://www.drip.com/blog/shopify-customer-segmentation
