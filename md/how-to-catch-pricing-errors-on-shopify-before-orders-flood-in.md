# How to catch pricing errors on Shopify before orders flood in

> A wrong price on Shopify goes live the second it saves and sells all night, no alarm anywhere. The AI playbook that catches misprices before orders flood in.

- Canonical: https://blog.dugong.live/how-to-catch-pricing-errors-on-shopify-before-orders-flood-in.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-08-12
- Updated: 2026-08-13
- Section: Research
- Word count: 2700
- Dispatch: Nº 106 · Research · 10 min read
- Full headline on page: How to catch *pricing errors* on Shopify before orders flood in
- Keywords: shopify pricing error, wrong price on shopify, price changed to 0, price change alert, shopify flow price trigger, product price history, bulk editor mistake, csv import prices, orders at wrong price, pricing guardrail
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

The bulk edit happens at 9:41 on a Tuesday night. Two hundred prices to update before a supplier increase lands, the admin open on the couch, one row per variant. Somewhere around row 140, a walnut coffee table that sells for $249 becomes $2.49, because a decimal point is a small key and it is late. The save takes a quarter second. Nothing asks whether you meant it. Nothing anywhere in Shopify ever asks whether you meant it.

The storefront updates instantly, which on every other night is the feature. At 11:20 someone posts the table to a deal forum. The first order arrives at 11:34, the tenth before 1 am, and while you sleep the listing migrates into two more communities that exist precisely to find prices like this one. At 7:05 you open the admin to 71 new orders, 64 of them for one product, each one carrying a payment fee, a promised shipping label, and a margin of roughly minus $220 a unit once the box leaves. Nothing malfunctioned. Every system did exactly what it was told at 9:41.

This is not a rare shape of night. In May 2010 a pricing engine capped nearly every product on 6pm.com, the discount sister site of Zappos, at $49.95. The error ran from midnight to 6 am Pacific, the hours nobody watches, and cost more than $1.6 million, which the company chose to honor in full. In December 2014 a fault in a repricing tool sent listings from roughly 2,000 Amazon UK sellers to one penny for about an hour in the thick of the December peak. One seller watched 675 costumes sell at 1p each and put her loss at £15,000 to £20,000. A toy seller took 1,600 orders in sixty minutes. Amazon cancelled what it could and said the rest out loud: orders that had already shipped could not be cancelled or reimbursed. The scale changes. The mechanism never does. A price is data, data can be wrong, and a wrong price transacts at exactly the speed of a right one.

## Every door into the price field is unlocked

Count the ways a price gets written in a working store. A staff member edits a variant in the admin. Someone runs the [bulk editor](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/bulk-editing) across a collection, the same editor whose limits push merchants into [retyping prices one product at a time](https://blog.dugong.live/how-to-bulk-edit-product-prices-on-shopify.html). A CSV import overwrites the catalog in one click. And the widest door of all, the API, which in practice means every app you have ever granted write scope: the supplier sync, the currency tool, the repricer, the sale scheduler you installed because [Shopify cannot start a sale by itself](https://blog.dugong.live/how-to-schedule-a-sale-on-shopify.html). All of them write to the same live field. All of them take effect the moment they save. None of them passes a checkpoint on the way, because there is no draft state for a price, no review queue, no publish step. The price field is production, and everyone deploys straight to it.

Each door has a signature failure. The admin and the bulk editor carry the slipped decimal and the extra zero, the $2.49 table and its mirror twin, the $2,490 one that simply stops selling. The CSV import has two of its own: a blank price cell that overwrites a live value, and the quiet violence of regional number formats. In July 2024 a merchant reported that exporting his products and re-importing them, changing nothing, multiplied every price by 100: €16,99 became €1699,00. He eventually traced it himself, a computer set to UK language with Dutch regional settings, Excel silently dropping the decimal separator on the way through, and posted the fix to his own thread before lunch. The sync door fails bigger. In October 2024 a merchant whose product data lives on his own server described what happens when an item disconnects from the feed: it publishes with a price of zero, and, in his words, customers can then purchase it. He asked for a workflow, trigger when a price changes, check whether it is zero, unpublish and email me. Simple, reasonable, and impossible, which may be why the thread collected zero replies. It is the same failure family as [the supplier feed that zeroes your catalog](https://blog.dugong.live/how-to-sync-supplier-inventory-feeds-to-shopify.html), except this time the zero has a checkout button.

The safety nets you would guess exist, do not. Shopify has a cost per item field on every variant, and the admin uses it to compute your margin, which means the platform knows to the cent that the table now sells at a 99 percent loss, and renders that number in quiet gray, and objects to nothing. A product priced at 0.00 sails through checkout. And a discount code stacks on top of a misprice as happily as on any other price, the same arithmetic that lets [codes double-dip your sale items](https://blog.dugong.live/how-to-stop-discount-codes-applying-to-sale-items-on-shopify.html), now applied to a number that was never supposed to exist.

## The change no trigger can see

The instinctive fix is an alert, and on Shopify alerts mean [Flow](https://help.shopify.com/en/manual/shopify-flow), so read Flow's product trigger list in full: product created, product deleted, product status updated, product variant added, product variant deleted, product variant back in stock, product variant out of stock, and product variant inventory quantity changed. Read it twice and the shape of the hole appears. Inventory that moves by one unit fires an event you can build a workflow on. A price that moves by a hundred dollars fires nothing.

Merchants have been asking for the missing trigger since September 2022, when a Plus merchant syncing prices from an external system wanted to react to the changes and staff replied that this would require a product updated trigger, which, unfortunately, did not exist at the moment. Two years later, in the same thread, a member of the Flow team put it plainer: there is no Shopify event for price updated. By the summer of 2026 the newest replies in that thread are app developers selling the missing trigger as a paid product, which is the surest sign a gap has stayed open long enough to become a market.

The do-it-yourself route hits the same wall from the other side. The products update [webhook](https://shopify.dev/docs/apps/build/webhooks) fires on every edit to any product field, but the payload does not say which field changed and does not carry the previous value, so a watcher has to store every price itself and diff each payload against its own records. The storing turns out to matter twice, because Shopify keeps no history of the price field at all: no version log, no undo, no old value anywhere in the admin, and the store activity log records logins and app installs, not product fields. The morning after a misprice, two questions decide everything, what was the price before, and who changed it, and the platform can answer neither.

> **◆ NOTE** A misprice is the one catalog error that performs better the worse it is. A typo in a title quietly costs you clicks. A price at one percent of intent generates the best conversion rate your store will ever record, straight into inventory you are paying to give away.

## Wrong prices travel at checkout speed

What makes this failure different from a mistyped title is the clock. A wrong description sits harmlessly wrong until someone reads it. A wrong price is executed against, by every visitor, at full speed, and the modern deal ecosystem is a distribution network for exactly these mistakes: forums, Telegram groups, and browser extensions that exist to detect an anomalous price and amplify it. Amazon's penny hour needed only sixty minutes to reach 1,600 orders for one seller. 6pm.com's window ran six hours because it opened at midnight, and the error still cleared $1.6 million. The damage is the leak rate multiplied by the detection delay, and since price edits cluster in the late evening, when humans do maintenance, the detection delay defaults to one full night of sleep.

The second clock is quieter and matters more. Legally, in most places, a displayed price is an invitation to treat rather than a binding offer, store terms commonly reserve the right to cancel orders placed on an obvious error, and cancelling with a refund and an honest apology is the standard resolution, with a lawyer's confirmation worth having for the big ones. But that option exists only while the orders are unshipped. Auto fulfillment, a 3PL that syncs every twenty minutes, a digital product that delivers itself, all of them close the window fast, and Amazon's sentence from 2014 is the epitaph: what has shipped cannot be cancelled or reimbursed. Which means the first job of any defense is not the apology email. It is stopping the warehouse before the warehouse makes the decision for you.

## What the automation actually has to do

Every input the defense needs already exists: the current catalog, the cost per item field, the compare-at price, the webhook that announces something changed, the order feed with its line prices, and the fulfillment hold that Shopify natively supports on the order side. What is missing is the worker who connects them. As a Dugong playbook, in plain prose:

```
# trigger
On every price write from any source,
and every incoming order

# steps
1. Snapshot the catalog: price,
   compare-at, and cost per variant,
   kept as the history Shopify lacks
2. Watch every write: diff each update
   against the snapshot, whichever
   door it came through
3. Judge the change: zero or near zero,
   below cost, past the drop threshold
   with no sale on the calendar
4. Quarantine first: unpublish or
   revert, alert with old price, new
   price, and source
5. Circuit-break the orders: hold
   fulfillment where the line price
   fails the same rules
6. Decide by policy: honor small
   damage, cancel large unshipped,
   message buyers inside the hour
7. Report the writes: who and what
   changes prices, near misses
   included, monthly
```

Steps one through three are the detection layer Shopify never shipped, and the third is where the judgment lives, because a useful alarm is a quiet one. A flat rule that flags every 30 percent drop fires on every flash sale and trains the team to ignore it by Thursday. The version that works knows your rhythms: a 70 percent drop is an anomaly in February and a plan on Black Friday, a zero price is always wrong except on the free gift SKU, clearance collections get more room than the new arrivals, and a price landing below the cost field is worth a message even when the percentage looks tame. Those are not settings. They are sentences about how your store prices things.

Steps four and five are the minutes that decide the size of the morning. Quarantine beats diagnosis: take the anomaly off the shelf first, or put the old price back, then ask the human which it was, because a wrong price that is live while you investigate is still selling. The order-side breaker catches what slipped through the gap: any order whose line price fails the same rules goes on fulfillment hold with a note, which converts the disaster from boxes in vans into rows on a screen. The alert that wakes you says the only three things that matter: what it was, what it became, and which door it came through, the admin, the import, or the app, so the fix targets the source instead of the symptom.

Steps six and seven turn the incident into policy. The decision itself, honor or cancel, is a brand call with real money on both sides: 6pm.com paid $1.6 million for a story it still gets told in, and a two-order slip at $2.49 is cheaper honored than explained. What the automation contributes is that the decision gets made by your written rule, fast, with every buyer messaged inside the hour, instead of by whichever staffer opens the admin first. And the monthly report answers the question the platform cannot: who changes prices in this store, through which doors, how often, and how close the last near miss came.

## Why this is a compiler problem, not an app problem

Price monitoring apps exist, and the good ones will show you a history and fire a webhook at a threshold. What they ship is a dashboard and a slider, and what the problem contains is a paragraph of judgment that differs at every store: which drops are plans and which are accidents, which SKUs are allowed to be free, what happens to the orders that got in, who gets woken and for how much, when honoring is cheaper than the cancellation storm. That paragraph cannot be expressed in checkboxes, which is the argument running through [the automations no one builds](https://blog.dugong.live/best-shopify-automations-to-set-up.html): the policy should compile into the workflow, instead of being shaved down to whichever settings the dashboard happened to expose.

Run the Tuesday night again with the paragraph compiled. The import saves at 9:41. At 9:42 the diff lands: 1 variant moved 99 percent with no sale scheduled, and the agent unpublishes the table, holds the two orders that arrived in the first minute, and sends one message: table was $249, saved as $2.49 via bulk edit, product unpublished, two orders held, recommend honoring both, total cost $493 against list. You tap yes from the couch. The price is back at 9:51, the two buyers get a cheerful note and their tables, the forum thread never gets written, and the whole incident costs less than the shipping on one of the 71 orders it replaced.

## The workflow worth building this week

Start with the audit Shopify will not volunteer. Export the catalog with price, compare-at price, and cost per item, and sort it three ways: anything at zero or under a dollar that is not meant to be, anything priced below its own cost field, and anything whose price sits above its compare-at price, which is either a data entry error or a sale that ended wrong. Most stores find something in the first ten minutes, and whatever you find has been live, findable, and purchasable for as long as you have not looked.

Then run the watcher in draft mode for two weeks: snapshot, diff, and alert, but revert nothing. You are auditing its judgment against yours. Did it flag the flash sale you meant, or stay quiet because the sale was on the calendar? Would the zero-price rule have caught the feed disconnect or tripped on the gift card? When its calls match yours, let the quarantine and the order holds run on the clean cases, and keep the judgment calls human, which is where they belonged all along.

Then say the brief out loud, the way you would hand pricing to a new hire. Keep a copy of every price and cost we have. Watch every change, whoever makes it, through whichever door. If a price hits zero, lands below cost, or drops past our threshold with no sale on the calendar, take the product down first and ask me second, and tell me the before, the after, and the source. Hold any order that got in at the wrong number. Honor the small ones, cancel the big ones before they ship, and message every buyer within the hour. Once a month, show me who changed prices and how close we came. That is the whole paragraph. The compiler turns it into the workflow, and the next slipped decimal costs you one tap on the couch instead of a morning you will be describing on a forum.

> **◆ READING** Two companion pieces if this one landed: [the price change you make one product at a time](https://blog.dugong.live/how-to-bulk-edit-product-prices-on-shopify.html), on doing intentional repricing without the risky tooling, and [the supplier feed that zeroed your catalog](https://blog.dugong.live/how-to-sync-supplier-inventory-feeds-to-shopify.html), on the sync failures that write garbage into a live store. Also worth reading: [the sale that starts the day after they buy](https://blog.dugong.live/how-to-handle-price-adjustment-requests-on-shopify.html), on what a deliberate price drop asks of you the morning after it goes live.

If you are a Shopify merchant with a pricing error story, the decimal that sold out a product overnight, the feed that published zeros, the morning you found the orders, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Do I have to honor orders placed at a wrong price on Shopify?

Usually not, but the decision has a deadline. In most jurisdictions a displayed price is treated as an invitation to treat rather than a binding offer, and most store terms of service reserve the right to cancel orders placed on an obvious pricing error, so the standard path is to cancel and refund the affected orders before fulfillment with a fast, plain apology. For a large incident, confirm the position with a lawyer rather than a blog post. The practical catch is that the choice only exists while the orders are unshipped: auto fulfillment, a 3PL sync, or a digital product can close the window in minutes, which is what happened to Amazon sellers in the 2014 penny glitch when stock left the warehouse before anyone could react. Reputation runs the other direction: 6pm.com honored $1.6 million of mispriced orders in 2010 and bought a customer service story with it. A sane written policy is to honor small damage, cancel large damage unshipped within the hour, and never let the warehouse make the call by default.

Permalink: https://blog.dugong.live/how-to-catch-pricing-errors-on-shopify-before-orders-flood-in.html#faq-1

### Can Shopify Flow alert me when a product price changes?

No. Flow's product triggers are product created, product deleted, product status updated, product variant added, product variant deleted, product variant back in stock, product variant out of stock, and product variant inventory quantity changed. Inventory moving by one unit fires an event; a price moving by any amount fires nothing. Merchants have asked for the trigger since 2022, when staff replied that a product updated trigger did not exist yet, and in late 2024 a Flow team member put it flatly: there is no Shopify event for price updated. The scheduled workaround, a daily workflow that queries products and checks prices, reads current state rather than the change, so it cannot tell a price that just moved from a sale that has run for three weeks, it lands up to 24 hours late, and it re-fires every run without a processed guard. The real version requires storing every price and diffing the products update webhook, which reports neither the changed field nor the previous value. That storage and compare layer, plus rules about which changes matter, is exactly the watcher worth delegating to an agent.

Permalink: https://blog.dugong.live/how-to-catch-pricing-errors-on-shopify-before-orders-flood-in.html#faq-2

### How do pricing errors happen on Shopify stores?

Through any of the five doors that write to the price field, none of which has a checkpoint. Manual edits and the bulk editor carry the classic slipped decimal, $249 saved as $2.49. CSV imports add two of their own: a blank price cell can overwrite a live value, and regional number settings can silently multiply, which is how one merchant's ordinary export and re-import turned €16,99 into €1699,00 because his computer mixed UK language with Dutch regional formatting and dropped the separator. Apps with write scope are the biggest door: a supplier sync that loses an item can publish a 0.00 price that customers can then purchase, as one merchant reported after his feed disconnected, and a repricer bug priced thousands of Amazon UK listings at a penny in an hour in 2014. Sale setup adds the swap, price and compare-at price entered backwards. Every one of these goes live the moment it saves, and Shopify keeps no price history and no undo to walk it back.

Permalink: https://blog.dugong.live/how-to-catch-pricing-errors-on-shopify-before-orders-flood-in.html#faq-3

### Does Shopify keep a history of product price changes?

No. There is no version log, no undo, and no old value anywhere in the admin, and the store activity log records logins and app installs rather than product fields. The morning after a misprice, the two questions that decide everything, what was the price before and who changed it, are questions the platform cannot answer. The do-it-yourself route hits the same wall: the products update webhook fires on every edit to any product field, but the payload does not say which field changed and does not carry the previous value, so a watcher has to store every price itself and diff each payload against its own records. That is why the playbook's first step is a snapshot of price, compare-at, and cost per variant, kept as the history Shopify lacks, with a monthly report of who changes prices and through which doors.

Permalink: https://blog.dugong.live/how-to-catch-pricing-errors-on-shopify-before-orders-flood-in.html#faq-4

### How do I audit my Shopify catalog for pricing errors?

Export the catalog with price, compare-at price, and cost per item, then sort it three ways: anything at zero or under a dollar that is not meant to be, anything priced below its own cost field, and anything whose price sits above its compare-at price, which is either a data entry error or a sale that ended wrong. Most stores find something in the first ten minutes, and whatever turns up has been live, findable, and purchasable for as long as nobody looked. Then run a watcher in draft mode for two weeks, snapshot, diff, and alert, reverting nothing, and audit its judgment against yours: did it flag the flash sale you meant, would the zero-price rule have caught the feed disconnect or tripped on the gift card. When its calls match yours, let the quarantine and the order holds run on the clean cases.

Permalink: https://blog.dugong.live/how-to-catch-pricing-errors-on-shopify-before-orders-flood-in.html#faq-5

---

Markdown rendition of https://blog.dugong.live/how-to-catch-pricing-errors-on-shopify-before-orders-flood-in.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
