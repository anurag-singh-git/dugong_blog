# SEO / GEO report — 2026-07-08 (post #2, new dispatch)

**Post:** How to automatically add a free gift to the cart on Shopify (Dispatch Nº 80)
**URL:** https://blog.dugong.live/how-to-automatically-add-a-free-gift-with-purchase-on-shopify.html
**Pain-point stub:** the-free-gift-that-never-lands-in-the-cart.html

Note: an earlier run today (`SEO-GEO-report-2026-07-08.md`) was a full-site internal-linking pass, no
new post. This report covers the new daily dispatch published in this run.

## Target intent

High-intent, unmet demand from merchants running a gift-with-purchase promotion who find the native
tools cannot place the gift in the cart. Validated on the Shopify community and app ecosystem: the
threads state the gaps almost verbatim, and a dense cluster of gift/BOGO apps exists only because the
native platform cannot add the item.

Primary phrases: Shopify free gift with purchase; Shopify auto add free gift to cart; Shopify buy x
get y not adding to cart; Shopify gift with purchase threshold; Shopify free gift over amount / cart
value gift; Shopify BOGO auto add; Shopify free gift app; Shopify automatic gift.

Long-tail: "why does my Buy X Get Y not show the gift in the cart," "spend $100 get a free gift
Shopify," "add free gift on Apple Pay / wallet button," "remove free gift when cart drops below
threshold."

## On-page SEO

- Title tag leads with the high-intent phrasing + brand suffix; single H1 with lime-underline `<em>`
  on "free gift"; H2s map to the search questions.
- Meta description + OG/Twitter written to the pain, zero em/en dashes (user style).
- Canonical to the full-URL post; robots index,follow, max-image-preview:large.

## GEO (generative-engine optimisation)

- JSON-LD: BlogPosting + BreadcrumbList + FAQPage + HowTo, all valid.
- FAQPage answers the three literal community questions in quotable, self-contained paragraphs.
- HowTo mirrors the 7-step playbook with #playbook anchors; `speakable` on .article-title and .faq.
- llms.txt: full descriptive entry added at the top of Articles.
- feed.xml item carries the same long-form description for syndication/AI ingestion.

## Internal linking

- Body links: set-a-minimum-order-amount (x3, closest sibling), schedule-a-sale (x2), tag-orders,
  prevent-overselling, segment-repeat-customers, abandoned-cart, best-automations lead essay.
- Read-next grid links all 31 how-to siblings + the lead essay, led by promo/cart-related posts.
- Reverse back-link added to set-a-minimum-order-amount (first Read-next card).
- Two homepage topics-cloud entries point to the new post.

## Distribution surfaces updated

sitemap.xml (34 URLs), feed.xml (34 items), llms.txt, index.html (featured card-tall + JSON-LD + hero
counters + ticker + topics), pain-point stub.

## Verification

| Check | Result |
|---|---|
| sitemap.xml / feed.xml valid XML | PASS |
| sitemap URL count / feed item count | 34 / 34 (new post included) |
| dangling sitemap post-locs | 0 |
| JSON-LD parse (new post + index) | PASS |
| new post `<div>` balance | 124/124 |
| index.html `<div>` balance / card-tall count | 209/209 / 1 |
| relative self-link in body or grid | 0 |
| all sibling links resolve | PASS |
| em/en dashes in authored content | 0 (7 template-level only) |

## Open items

- Undeployed working tree: all changes staged only, no git commit/push this run (consistent with
  prior runs). Not live until committed and pushed.
- Reverse back-link mesh from other promotion/cart posts (schedule-a-sale, abandoned-cart,
  segment-repeat-customers) to this post left for a future pass.
- Uncovered candidate topics: quantity/tiered (volume) discounts, cross-product BOGO, automatic
  best-discount selection / preventing code stacking, loyalty-points automation, gift-message/gift-wrap.
