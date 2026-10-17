# How to handle price adjustment requests on Shopify when your sale drops the day after they buy

> Shopify has no price adjustment feature, no Flow trigger for a price change and no refund action. The AI playbook that computes the difference and settles it.

- Canonical: https://blog.dugong.live/how-to-handle-price-adjustment-requests-on-shopify.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-10-10
- Section: Research
- Word count: 1820
- Dispatch: Nº 123 · Research · 7 min read
- Full headline on page: How to handle *price adjustment* requests on Shopify when your sale drops the day after they buy
- Keywords: shopify price adjustment, price drop refund shopify, refund the price difference, shopify partial refund, shopify price protection, shopify flow price change trigger, price adjustment policy, store credit refund
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

Your sale goes live Friday at nine. By twenty to ten there are nine emails saying the same thing in nine different tones: I bought this on Tuesday, it is 25 percent off today, can you refund me the difference.

Somebody now does this nine times. Find the order. Work out what the buyer actually paid, which is not the list price because they used a welcome code. Work out what the item costs today, which is not the list price either because the sale is an automatic discount. Subtract. Decide whether a Tuesday order is inside a window nobody has written down. Open the refund screen, override the amount, untick restock, add a note, reply. Four minutes each when nothing is strange, and something is usually strange.

A merchant put this to the Shopify Community in April 2025. They were calculating the price difference after each promo and issuing partial refunds by hand, and they asked whether anyone had found a more efficient or automated way to manage these post-purchase refund requests. The single reply agreed the task sounds simple, pointed out that discount codes and dynamic offers make it harder, asked two clarifying questions, and that was that. The thread is still open. That is the state of the art.

## Shopify has no price adjustment anything

There is no price adjustment feature, no price protection window, no policy field. What exists is the ordinary partial refund, and the mechanism is fine: open the order, click Refund, enter a quantity, then overwrite the *Refund amount* field in the Summary with the figure you actually mean, deselect *Restock items* because nothing is coming back, and submit. You can keep issuing further partial refunds until you reach the total available to refund, and you can send the money to the original payment method, to store credit, or split it across both.

So the refund works. Everything around it is missing, in three specific ways.

**Flow cannot see a price change.** The product triggers are product created, deleted, status updated, variant added, variant deleted, variant back in stock, variant out of stock, and variant inventory quantity changed. None fire on price. A long-running community thread says it plainly: there is no Shopify event for price updated. On 6 October 2026 a Shopify staffer added to that thread that the Flow team is testing a product updated trigger which can fire on selected product and variant fields including price, limited to testers, with no general availability announced. Until it ships, the native approach is a scheduled workflow that wakes up daily and goes looking.

**Flow cannot issue a refund.** The order actions are tags, note, cancel order, capture payment, mark as paid, archive, add a line item, send invoice, metafields and get order data. Refund exists only as a *trigger*, refund created, never as an action. There is no create gift card action and no store credit action either. The write is reachable only through Send Admin API request.

**Shopify keeps no price history.** The order line item records what the buyer paid, so that half is permanent. The product record holds only today's price. The moment the bulk edit that starts your sale finishes running, the before state is gone unless you captured it yourself.

Put those together and the native answer to *what did this customer overpay* is a person with two tabs open and a calculator.

## The number is harder than it looks

Four things make the arithmetic wrong more often than anyone expects.

**List price is not what they paid.** If the original order carried a code, Shopify allocated that discount across the line items. The honest comparison is per-unit price paid after allocated discounts against the per-unit price that same cart would pay today.

**List price is not what it costs today either.** Automatic discounts, volume breaks, market-specific pricing and B2B catalog prices do not live on the variant. A 25 percent automatic discount shows a $100 list price and charges $75.

**Some orders have already been adjusted.** The second promo of the month catches the same customer twice, and the second calculation has to run against the already-reduced effective price, not the original.

**Shipping thresholds move.** Take $20 off a $95 order that earned free shipping over $85 and you have quietly given away the shipping too.

Get this wrong in your favor and you look cheap in public. Get it wrong the other way across a 200-order sweep and the adjustment costs more than the promotion did.

## The costs nobody counts

The visible cost is the refund. Three more sit under it.

**You keep the fee on money you gave back.** With Shopify Payments, refunds do not return your credit card fees, and the same holds on a third-party gateway in a country where Shopify Payments is available. Only merchants on a third-party gateway in a country without Shopify Payments get transaction fees back proportionally, and only on refunds issued through the admin. Every adjustment is the difference plus processing you have already paid on it.

**It lands in your numbers as a refund, not as promo spend.** A price adjustment is a discount granted late, and Shopify files it under refunds. Your promotion looks cheaper than it was, your refund rate looks worse than it is, and nobody can tell you what the last sale actually cost.

**The requests you never see cost the most.** The customer who does not email returns the whole order and rebuys at the sale price, which costs you a label, a restock, a possibly scuffed unit and the processing twice. Or they open a dispute. Or they say nothing at all and simply wait for the next sale, forever.

Time matters too. Refunds are generally possible for up to 120 days after the order, with anything older depending on the customer's bank. A request sitting in a shared inbox for five weeks is not a free request.

## The playbook worth building

As a Dugong playbook, in plain language:

```
# trigger
Every price change, plus every
inbound price adjustment request

# steps
1. Snapshot prices daily and before
   any bulk price edit
2. Classify each drop: promotion,
   mispricing, or permanent reprice
3. Pull orders inside the window
   holding that variant
4. Compute the real per-unit delta,
   after allocated discounts on
   both sides
5. Apply the policy: window, floor,
   cap, exclusions, already adjusted
6. Settle: store credit by default,
   cash above the threshold, code
   where neither fits
7. Speak first, before the customer
   has to ask
8. Book it against the promotion,
   not against refunds
```

**Step two is the step that prevents a disaster.** Not every price drop is a sale. A typo correction from $249 to $24.90 and back, a currency rounding fix, a clearance markdown on a discontinued line, a supplier-driven reprice: all of them look identical to a rule that only reads a number. Refund against the typo and you refund most of the product.

**Step six decides what this costs you.** Store credit keeps the money in the business, and most customers take it when it is offered in the first reply with a straight explanation rather than after two rounds of argument. Cash to the original method is the right answer above whatever figure makes credit feel like a dodge, which for most baskets sits somewhere between twenty and fifty dollars.

**Step seven is the entire return on this build.** The same twelve dollars buys a completely different reaction depending on who speaks first. Sent unprompted on Friday morning it reads as a store that pays attention. Sent on Monday after two emails and a screenshot, it reads as a store that had to be pushed.

## The policy is the configuration

Most stores do not have a price adjustment problem. They have an undocumented one, which is why every request turns into a small negotiation and two people give different answers in the same week.

Write down five things and publish them. The window in days from the order date. The smallest difference worth processing. The largest you will adjust without a manager. The exclusions, meaning final sale, clearance, bundles, gift cards, wholesale and orders that already used a code. And what the customer receives. Published, that page stops a good share of the requests from arriving and pre-answers the rest. Written down, those same five numbers are the whole configuration of the automation. Everything after them is reading email and doing arithmetic.

## Where AI earns its place

Two judgement calls here, and neither of them is subtraction.

The first is on the way in. These requests never arrive as a clean form. They arrive as *the blue hoodie I got last week is cheaper now*, with a screenshot, sometimes about a variant the customer did not buy, sometimes about a competitor's price, sometimes from somebody who has asked three times this quarter. A model matches the sentence to the order and the line item, reads the screenshot, runs the real calculation on both sides, checks it against your policy and drafts the reply with the actual number in it. What reaches a human is a decision, not a search.

The second is on the way out, and it is the one worth paying for: judging whether a price movement is a promotion at all. That call wants context. Is a campaign running. Is this product discontinued. Is the drop plausible as a percentage for this category. Did it arrive alongside a bulk edit of 400 other variants. A threshold cannot see any of that, which is exactly why a threshold gets this confidently wrong.

Two things stay human. The policy itself, because it is a margin decision rather than an operational one. And any adjustment above your cap, which should land in a queue with the number already worked out and a one-line recommendation attached.

## Set it up this week

Export your current variant prices to a CSV today. That file is your first snapshot and it costs four minutes.

Then pull every partial refund from the last sixty days with no return attached and add them up. That number is what price adjustments already cost you, and in most stores nobody has ever looked at it.

Then write the five numbers down and publish them. The automation is straightforward once a policy exists. It is impossible while one does not.

> **◆ READING** Two companion pieces if this one landed: [The misprice that sells all night](https://blog.dugong.live/how-to-catch-pricing-errors-on-shopify-before-orders-flood-in.html), on catching the wrong price before it sells out, and [The discount code that double-dips your sale](https://blog.dugong.live/how-to-stop-discount-codes-applying-to-sale-items-on-shopify.html), on the stacking Shopify will happily allow during a promotion.

Running a sale with a price adjustment story, the BFCM morning that ate a day of support, the sweep that cost more than the promo, the policy you have never written down? The inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Does Shopify have a price adjustment feature?

No. There is no price adjustment setting, no price protection window and no policy field anywhere in the admin. What you have is the ordinary partial refund: open the order, click Refund, enter a quantity, then edit the Refund amount field in the Summary to the figure you actually want to give back, deselect Restock items so the unit is not added back to stock, and submit. You can keep issuing further partial refunds until you reach the total available to refund, and you can send the money to the original payment method, to store credit, or split it across both. The mechanism works. What is missing is everything around it: no way to notice the price drop that caused the request, no record of what the product used to cost, no policy enforcement, and no reporting that separates a price adjustment from a return.

Permalink: https://blog.dugong.live/how-to-handle-price-adjustment-requests-on-shopify.html#faq-1

### How do I refund the price difference on a Shopify order?

Open the order, click Refund, set the quantity on the line item involved, then overwrite the Refund amount field with the difference rather than the item price. Deselect Restock items, because nothing is coming back. Add an internal note naming the promotion, since nothing else on the order will record why the money moved. Then choose the original payment method or store credit as the destination. Two cautions. Your credit card fees are not returned on a refund with Shopify Payments, or on a third-party gateway in a country where Shopify Payments is available, so the adjustment costs you the difference plus processing you already paid on it. And refunds are generally possible for up to 120 days after the order, with older ones depending on the customer's bank, so a request that sits in a shared inbox is not free.

Permalink: https://blog.dugong.live/how-to-handle-price-adjustment-requests-on-shopify.html#faq-2

### Can Shopify Flow trigger when a product price changes?

Not today. Flow's product triggers cover product created, product deleted, product status updated, product variant added, product variant deleted, product variant back in stock, product variant out of stock and product variant inventory quantity changed. None of them fire on price. A long-running community thread puts it plainly: there is no Shopify event for price updated. In October 2026 a Shopify staff member on that thread said the Flow team is testing a product updated trigger that can fire on selected product and variant fields including price, available to testers only, with no general availability announced. Until it ships, the native workaround is a scheduled workflow that runs daily and looks for products changed since the last run. Note too that Flow has no refund action at all: refund created exists as a trigger, and the write has to go through Send Admin API request.

Permalink: https://blog.dugong.live/how-to-handle-price-adjustment-requests-on-shopify.html#faq-3

### What should a Shopify price adjustment policy say?

Five numbers, published where customers and staff can both read them. The window, in days from the order date, usually seven to fourteen. The minimum difference you will bother processing, so that a ninety cent adjustment does not consume four minutes of somebody's afternoon. The maximum you will adjust without a manager, which also becomes the cap your automation respects. The exclusions: final sale, clearance, bundles, gift cards, wholesale orders, and orders that already used a discount code. And what the customer actually receives, meaning store credit, a refund to the original payment method, or a code for next time. Those five numbers do two jobs at once. Published, they stop a good share of the requests from arriving and pre-answer the rest. Written down, they are the entire configuration of the automation.

Permalink: https://blog.dugong.live/how-to-handle-price-adjustment-requests-on-shopify.html#faq-4

### Can AI handle price adjustment requests on Shopify?

It can do the two parts that take judgement. On the way in, a request arrives as a sentence rather than a form: the blue hoodie I ordered last week is cheaper now, often with a screenshot, sometimes naming a variant the customer never bought. A model matches that to the right order and line item, reads the screenshot, computes the per-unit difference after allocated discounts on both sides, checks it against your policy, and drafts the reply with the real number in it. On the way out, the harder call is deciding whether a price movement is a promotion at all, because a typo correction, a currency rounding fix, a clearance markdown on a discontinued line and a supplier-driven reprice all look identical to a rule that only reads a number. Refund against a mispriced item and you refund most of its value. So keep two things human: the policy itself, and any adjustment above your cap.

Permalink: https://blog.dugong.live/how-to-handle-price-adjustment-requests-on-shopify.html#faq-5

---

Markdown rendition of https://blog.dugong.live/how-to-handle-price-adjustment-requests-on-shopify.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
