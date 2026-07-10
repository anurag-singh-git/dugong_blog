# SEO / GEO report — 2026-07-06

**Post:** How to automatically send invoices to Shopify customers
**File:** how-to-automatically-send-invoices-on-shopify.html
**Dispatch:** Nº 78 · Priya Singh · 2026-07-06

## Intent and keyword targeting

High-intent, unsolved pain point sourced from Shopify merchant communities. Primary phrases:

- Shopify send invoice automatically / Shopify automatic invoice
- Shopify PDF invoice / Shopify tax invoice
- Shopify VAT invoice / send invoice to customer Shopify
- Shopify B2B invoice tax number / Shopify order invoice email
- Shopify credit note refund

The H1 carries the how-to search phrasing ("How to automatically send invoices to Shopify customers").
The pain-point headline ("The invoice you send by hand") is used for the breadcrumb, HowTo name, the
`the-*` landing stub, and the featured index card, so both the searcher who types the solution query and
the merchant who feels the pain converge on the same page.

## On-page SEO

- Unique `<title>`, meta description, canonical, keywords, and author meta; robots index,follow with
  max-image-preview:large.
- Open Graph + Twitter card fully populated with invoice-specific copy.
- Canonical points to the self URL; the `the-invoice-you-send-by-hand.html` stub is noindex and redirects
  (canonical + meta-refresh + JS replace) to the canonical post.
- Internal linking: body links to reconcile-payouts (x2), tag-orders (x2), segment-repeat-customers,
  combine-orders, edit-order, cancel-unpaid, and the best-automations lead essay. Read-next grid links all
  30 siblings, no self-link. Reverse back-link added from reconcile-payouts (most related sibling).
- Added to sitemap.xml (priority 0.9), feed.xml (newest item), llms.txt (top of Articles), and index.html
  JSON-LD blogPost array + topics cloud.

## GEO (generative-engine optimization)

- JSON-LD `@graph`: BlogPosting + BreadcrumbList + FAQPage (3 Q&As) + HowTo (7 steps). All parse clean.
- FAQPage answers the three highest-frequency questions an answer engine will field: does Shopify auto-send
  an invoice, can Shopify collect a VAT/tax number at checkout, and how do most stores send invoices today.
- HowTo encodes the playbook as 7 discrete, quotable steps (read order → decide document → fill tax number
  → generate numbered PDF → auto-send → credit note on refund → escalate edge cases).
- `speakable` selectors on `.article-title` and `.faq`.
- llms.txt entry is a self-contained ~450-word summary an LLM can lift wholesale, crediting the parts
  Shopify does (order confirmation email; Shopify Tax EU/UK VAT invoice) and naming the exact limits
  (never emailed, region-locked, no regeneration after edit, no tax-number field at checkout).
- Accuracy: the post distinguishes receipt vs invoice vs tax invoice vs credit note, and correctly scopes
  the Shopify Tax VAT-invoice feature to EU/UK order-status-page display, avoiding the common
  overstatement that Shopify has no invoicing at all.

## Differentiation vs existing dispatches

Distinct from reconcile-payouts (that is bank-deposit reconciliation, this is the customer-facing
document), from tag-orders (metadata, not a document), and from cancel-unpaid (draft-order payment
requests, not post-purchase tax invoices). No keyword cannibalization: no existing post targets "invoice,"
"VAT invoice," or "credit note."
