# How to track product expiry dates on Shopify before the stock goes bad

> Shopify counts your stock but never dates it: no expiry field, no batch tracking, and Flow cannot read date metafields. The AI playbook that sells it in time.

- Canonical: https://blog.dugong.live/how-to-track-product-expiry-dates-on-shopify.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-08-29
- Updated: 2026-10-24
- Section: Research
- Word count: 2600
- Dispatch: Nº 116 · Research · 10 min read
- Full headline on page: How to track product expiry dates on Shopify *before the stock goes bad*
- Keywords: shopify expiry date tracking, shopify product expiration dates, track expiry dates shopify, shopify batch tracking, shopify lot number tracking, shopify flow date metafield, discount expiring products shopify, shopify best before date, AI inventory automation
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

The pallet lands on a Tuesday. Sixty jars of the bestselling collagen blend, fresh from the co-packer, best before next June. Forty older jars are already on the shelf, best before November. You receive the delivery the only way Shopify knows how: 40 becomes 100.

And somewhere inside that addition, the one fact that decides whether you sell those jars or bin them, which jars go bad first, stops existing. The admin will tell you how many, all day, to the unit, across every location. It will never tell you how long.

## The short answer

Record each delivery as its own batch, with quantity, lot number, and best-before date, then read those dates on a daily schedule. Shopify gives you nowhere to put them. Inventory is a single quantity per variant per location, with no expiry field, no batch or lot dimension behind the number, and no date in any inventory report.

The community workaround is a date metafield on the product, and it fails on the second delivery. One product holds one metafield while a shelf holds two batches, so the fresher date overwrites the older one and the oldest stock ages out wearing a newer label. Shopify Flow cannot rescue it either. Staff have said repeatedly that you cannot use metafields with Get product data and cannot query by date metafields, so the alert everyone asks for cannot be built there.

What works is a batch ledger swept every morning for days remaining, per batch and per location. That is what makes the rest possible: tiered alerts at sixty, thirty, and ten days, markdowns that run on the calendar instead of memory, the listing pulled when the last good batch ages out, oldest dates picked first, and a recall that becomes a lookup of which orders drew from one lot rather than an email to every customer.

## The field that does not exist

Shopify inventory is a single quantity per variant per location. That is the whole model. There is no expiry field on a variant, no batch or lot dimension behind the number, no date column in any inventory report, and no concept anywhere in the system that two units of the same SKU might differ from each other in any way that matters. For apparel this is fine; a medium black tee from March is a medium black tee from July. For food, supplements, cosmetics, coffee, candles with a scent shelf life, pet treats, anything with a printed date, the model is blind in exactly the dimension that determines whether the inventory is an asset or a liability.

The community's standard answer is a metafield: create a date field on the product, type the best-before date in by hand each time stock arrives. And that answer has a flaw you can see from the loading dock. A product has one metafield. A shelf usually holds two batches. The Tuesday pallet arrives, someone dutifully updates the field to next June, and the forty November jars are now wearing a June label. The oldest stock in the building just became invisible on the day it needed watching most. The count stays perfectly accurate the whole time, the way [a count can be accurate](https://blog.dugong.live/how-to-stop-your-shopify-inventory-changing-by-itself.html) while everything it stands for is wrong.

## The community record

Merchants have been asking Shopify to read that date for years, and the answers are unusually well documented, because they came from Shopify staff. In October 2023 a merchant described the routine exactly, each new batch of stock, the product's expiration date manually updated in the metafield, and asked for the obvious next step: have [Shopify Flow](https://help.shopify.com/en/manual/shopify-flow) send an email ten days before the date. Staff replied three days later: this is not currently possible, but Flow is working on better support for [metafields](https://help.shopify.com/en/manual/custom-data/metafields). Stay tuned.

In June 2024 a grocery seller asked again, with the full spec this time: notifications at ten days, five days, and two days before the date, plus automatic discounts on the way down. Staff answered the same day and named the recipe that should work, a scheduled trigger, Get product data, an internal email, and then the wall it hits: you cannot yet use metafields with Get product data. When another merchant asked whether that was on the roadmap, the reply drew the boundary honestly: it's not a Flow limitation, the API we use, as well as all partners, doesn't support it. Any date for that? I don't have a date yet, but I know it's being actively talked about.

In January 2025 a merchant with over six thousand dated products asked whether the workflow could even be built. The staff answer had moved one inch: a recent API change made querying products by metafield value possible, but you cannot yet query by dates. The suggested workaround is its own genre of sentence: convert the date metafield into a single line text metafield, so the date can be matched as a string. Otherwise, you would have to periodically scan all six thousand, and there is no straight-forward way to do that on a daily basis.

By February 2025 the question and answer had compressed to their final form. Merchant: I want a Flow that checks whether the expiration date is close and sends an email. Staff: you cannot query by date metafields currently, so not sure that use case is possible. The next reply in the thread was an app vendor offering a reporting tool, which is how these threads always end: the platform declines, the workaround economy fills in. In another thread a dietary supplements seller went looking for lot-code tracking, the thing a recall requires, and was pointed the same direction: the apps.

> **◆ NOTE** The record, compressed: an alert ten days before a metafield date, asked October 2023, this is not currently possible. Ten, five, and two day notices plus automatic markdowns, asked June 2024, you cannot yet use metafields with Get product data, and it is not a Flow limitation, the API does not support it. Six thousand dated products, January 2025, you cannot yet query by dates, and no straight-forward way to scan daily. February 2025, you cannot query by date metafields currently, so not sure that use case is possible. Every thread ends the same way: an app link.

## What the invisible date costs

While the date sits unreadable in a metafield, it keeps charging you. The first cost is the write-off cliff. Short-dated stock is not worthless, it is worth less, on a schedule: a batch with sixty days left sells happily at twenty percent off, at ten days it needs sixty off or a donation receipt, and at zero it is a disposal fee. Every day the date goes unwatched, value slides down that curve unattended, which is how perfectly sellable inventory becomes [the dead stock your dashboard never mentions](https://blog.dugong.live/how-to-automatically-clear-dead-stock-on-shopify.html), except worse: dead stock can at least wait for you. Dated stock cannot.

The second cost ships in a box. With no batch dimension, nothing connects the order being packed to the jars being grabbed, so whoever picks takes the nearest one, and the nearest one is usually the newest, because deliveries get stacked in front. First in, last out, the exact reverse of what dated goods need. The November jars wait at the back while June jars ship, until the day a customer opens a package and photographs the date on the lid. In food and supplements that photograph is a refund, a one-star review, and depending on your category and your retail partners, a conversation with a regulator.

The third cost has a lot number on it. Recalls arrive as lots: the co-packer emails that lot 24118 failed a stability test, please notify affected customers. Shopify has no record of which orders contain lot 24118, because it never knew the lot existed. Your recall notice therefore goes to everyone who bought the product in six months, which is the most expensive email a small brand can send.

> The count answers how many you can sell. The date answers how *long*. Shopify only ever asks the first question.

## What the automation actually has to do

As a Dugong playbook, in plain prose:

```
# trigger
On every delivery you log,
plus a daily sweep of every
batch still on the shelf

# steps
1. Record every batch as it
   lands: quantity, lot
   number, best-before date
2. Sweep daily and read every
   date, the query Flow
   cannot run
3. Tier the alerts: sixty,
   thirty, ten days, each to
   the right person
4. Mark down on schedule:
   short-dated stock into
   clearance while it sells
5. Pull the listing when the
   last good batch ages out,
   buy button included
6. Keep lot-to-order records
   so a recall is a lookup,
   not an apology tour
7. Report weekly: expiring
   value, sold through
   versus written off
```

Step one is where the truth enters the building, and it is the only step that asks anything of a human. Receiving becomes one sentence: sixty units, lot 24118, best before June 12. The automation files it as a batch record, a [metaobject](https://help.shopify.com/en/manual/custom-data/metaobjects) under the hood, attached to the variant, so the November forty and the June sixty finally exist as two facts instead of one number. This is the difference between a date field and a batch ledger, and it is the difference the single-metafield workaround can never cross.

Steps two and three are the request from the threads, built the way the threads could not build it. The sweep runs every morning, reads every batch, and does arithmetic Flow cannot: days remaining, per batch, per location. Sixty days out, the note goes to whoever plans promotions, while the stock still has full-price life in it. Thirty days, to whoever runs markdowns. Ten days, to whoever decides between the discount ladder's last rung and the donation pile. The thresholds are yours; a baked goods seller lives on a two-day clock, a supplements brand whose retail partners refuse anything under ninety days needs the alert at one twenty.

Step four turns the alert into money. The markdown ladder runs on the calendar, not on memory: [the sale starts itself](https://blog.dugong.live/how-to-schedule-a-sale-on-shopify.html) when a batch crosses each rung, the product moves into the short-dated collection, [the price changes without an evening of spreadsheet surgery](https://blog.dugong.live/how-to-bulk-edit-product-prices-on-shopify.html), and, the half everyone forgets, it reverses: when the short-dated batch sells out and June stock is what remains, the price comes back up the same night. Step five is the guardrail at the bottom. When the last good batch ages out, the listing goes down or [the variant hides](https://blog.dugong.live/how-to-automatically-hide-sold-out-variants-on-shopify.html) before the next order can sell what you would have to refund, and the expired units get written out of the count so [the reorder math](https://blog.dugong.live/how-to-set-inventory-reorder-points-on-shopify.html) sees the shelf as it really is. [Returns get the same test](https://blog.dugong.live/how-to-automatically-restock-returns-on-shopify.html): a jar that comes back inside its window restocks to its batch, one past it never does.

Step six is the insurance nobody wants to need. Every order gets stamped with the lot it drew from, in first-expiring-first-out order, with a pick note telling the warehouse which batch to actually grab. The day the co-packer's email arrives, lot 24118 is a query: forty-one orders, these customers, this date range. The recall email goes to forty-one people instead of two thousand, and the apology is specific instead of general. The honest limits, stated plainly: nothing reads the label through the shrink wrap, so the one-line habit at receiving is load-bearing. The automation prints the pick note but cannot rotate jars; first-out discipline on the shelf still belongs to hands. And the policy questions, how close to the date you stop selling, what gets donated, what your category's rules demand, are judgments that stay yours.

## Why this is a compiler problem, not an app problem

The expiry apps all implement someone's policy. The trouble is that expiry policy is a paragraph, and the paragraph is different in every building. A coffee roaster's date is a freshness window and a marketing asset: roasted on, best within thirty days, discount never, clear to the subscription box instead. A supplements brand lives by the ninety-day rule its retailers impose and needs lots on every order. A grocery seller has a food bank partner who collects on Thursdays, so the ten-day rung of the ladder is not a discount, it is a pickup booking. A cosmetics brand tracks period-after opening and cares about the manufacture date, not a printed expiry at all. Those are sentences about your shop, and they should compile into the automation as written, the same principle that runs [every automation worth building](https://blog.dugong.live/best-shopify-automations-to-set-up.html). An app sells you its paragraph. A compiler runs yours.

Run the Tuesday again with the sentences compiled. The pallet lands; receiving types one line; the store now knows it holds forty November jars and sixty June jars, and the pick notes start saying November first. In September the sixty-day sweep flags the November batch and the promotion plan gets a line item. In October the ladder moves it to thirty percent off and the batch sells through eleven days before the date, at margin instead of as a write-off. The listing never sells an expired unit, the count the reorder reads is true, and the lot ledger sits there costing nothing, waiting for the email you hope never comes. Jars binned: zero. Times anyone looked at a date on a lid: also zero.

## The workflow worth building this week

Start with the dates you already have. Walk the shelf once and log what is actually there, batch by batch, lot and best-before, the honest version of the walk you do before a stocktake. It takes an afternoon and it is the last time a human does it in bulk; from then on the ledger is fed one delivery at a time. Then write your ladder down in your own words: when we discount, by how much, when we stop selling, where the last rung goes. If you have never had the policy conversation, the first sixty-day alert will force it, which is the alert working.

Then say the brief the way you would tell a new warehouse hire. Every delivery I log gets a batch: quantity, lot, best-before. Check every batch every morning. Tell marketing at sixty days, mark down at thirty, tell me at ten. Ship oldest date first and note the lot on the order. Never let an expired batch sell: hide the listing if it is the last one, and put the price back when fresh stock takes over. Once a week, show me what is expiring, what we saved, and what we lost. That is the whole paragraph. The compiler turns it into the workflow, and the store finally learns the second question: not just how many, but how long.

> **◆ READING** Two companion pieces if this one landed: [the dead stock your dashboard never mentions](https://blog.dugong.live/how-to-automatically-clear-dead-stock-on-shopify.html), on finding and clearing the inventory that stopped moving, and [the reorder you always make too late](https://blog.dugong.live/how-to-set-inventory-reorder-points-on-shopify.html), on buying the next batch before the shelf runs dry.

If you are a Shopify merchant with an expiry story, the pallet that aged out behind a fresher label, the recall email you had to send to everyone, the spreadsheet that died in Q4, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Does Shopify track product expiration dates?

No. Shopify inventory is a single quantity per variant per location: the admin can tell you that you have forty jars, but there is no field for how long those jars are good, no batch or lot dimension behind the number, and no report anywhere that mentions a date. The standard community answer is to create a date metafield on the product and type the best-before date in by hand, and it works until the second batch arrives. A product has one metafield and a shelf usually holds two batches, so the fresher delivery overwrites the older date and the oldest stock quietly ages out wearing a newer label. Real expiry tracking needs one record per batch, quantity plus lot number plus best-before date, kept in sync as stock sells through. Apps in the Shopify App Store add this as a separate system; an AI automation like Dugong can keep the batch records in your own store's metaobjects, one per delivery, so every quantity on the shelf keeps its own date.

Permalink: https://blog.dugong.live/how-to-track-product-expiry-dates-on-shopify.html#faq-1

### Can Shopify Flow send an alert before a product expires?

Not natively, and Shopify staff have confirmed it repeatedly in the community threads. In October 2023 a merchant asked Flow to email ten days before a metafield date and staff replied that this is not currently possible. In June 2024 a grocery seller asked for ten, five and two day notices and staff named the missing piece: you cannot yet use metafields with Get product data, and it is not a Flow limitation, the underlying API does not support it. In January 2025 staff explained that a recent API change made querying products by metafield value possible, but you cannot yet query by dates, and that scanning six thousand products daily has no straight-forward path. In February 2025 the answer was still: you cannot query by date metafields currently, so not sure that use case is possible. The workarounds merchants traded, storing the date as plain text so it can be matched as a string, tagging products by hand, an inventory-trigger JavaScript hack offered with the caveat would need to test, all route around the same missing query. An automation that reads product data on its own daily schedule and does its own date arithmetic does not need that query to exist.

Permalink: https://blog.dugong.live/how-to-track-product-expiry-dates-on-shopify.html#faq-2

### How do I track batch or lot numbers on Shopify?

There is no native batch or lot field anywhere in Shopify: not on the variant, not on the inventory level, not on the order line. For supplement, food, and cosmetics sellers that is a compliance problem as much as a stock problem, because a recall arrives as a lot number and Shopify cannot tell you which orders contain that lot. The workable pattern is one batch record per delivery, kept in metaobjects: quantity received, lot number, best-before date, and a running count of what remains as orders sell the batch down in first-expiring-first-out order. Each shipped order gets annotated with the lot it drew from. Maintained by hand this is a spreadsheet that dies the first busy week; maintained by an automation it turns a recall from an email to every customer into a lookup that returns exactly the orders affected, and it gives every alert, markdown, and listing decision a real date to work from.

Permalink: https://blog.dugong.live/how-to-track-product-expiry-dates-on-shopify.html#faq-3

### How do I automatically discount products that are close to expiry on Shopify?

Decide the ladder while the stock is still fresh, then let the dates run it. A typical policy: at sixty days remaining, move the batch's product into a short-dated collection and take twenty percent off; at thirty days, forty percent; at ten days, sixty percent or the donation pile, whichever your category allows. Shopify will not run this ladder for you: discounts do not read metafields, Flow cannot query the dates, and the native tools leave you editing prices by hand the week everything converges. An automation runs it on the calendar: it computes days remaining per batch every morning, applies the markdown when a batch crosses each rung, moves the product in and out of the clearance collection, and reverses the price when a fresh batch becomes the one on sale. The point of the ladder is that short-dated stock recovers most of its value at sixty days and almost none at five, so the profit lives in the trigger firing on time, not in the size of the discount.

Permalink: https://blog.dugong.live/how-to-track-product-expiry-dates-on-shopify.html#faq-4

### Can AI track expiry dates and clear short-dated stock on my Shopify store?

Yes, and this is a case where the automation does something the platform genuinely cannot. An automation like Dugong records a batch every time stock lands, quantity, lot, best-before date, then sweeps every batch daily and does the date arithmetic Shopify Flow cannot: sixty, thirty, and ten day alerts to the right person, markdowns applied on schedule, the listing pulled when the last good batch ages out, a first-expiring-first-out note for whoever picks orders, lot numbers stamped onto orders for recall lookups, and a weekly report of expiring value against what sold through. The honest limits: nothing reads the physical label, so batches must be logged when deliveries land, a one line habit at receiving; the automation can print pick notes but cannot rotate jars on a shelf, so physical first-out discipline stays with whoever packs; and the policy questions, how close to the date you stop selling, what gets donated versus binned, are category judgments that belong to you. What the automation removes is the part that fails silently: remembering, every day, to go look at the dates.

Permalink: https://blog.dugong.live/how-to-track-product-expiry-dates-on-shopify.html#faq-5

---

Markdown rendition of https://blog.dugong.live/how-to-track-product-expiry-dates-on-shopify.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
