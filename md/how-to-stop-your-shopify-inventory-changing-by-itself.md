# How to stop your Shopify inventory changing by itself

> Shopify stock counts that rise, reset to zero, or refill sold-out items on their own. The AI playbook that puts a name and a timestamp on every unit that moves.

- Canonical: https://blog.dugong.live/how-to-stop-your-shopify-inventory-changing-by-itself.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-08-22
- Section: Research
- Word count: 2800
- Dispatch: Nº 112 · Research · 11 min read
- Full headline on page: How to stop your Shopify inventory *changing by itself*
- Keywords: shopify inventory changed by itself, inventory keeps changing, inventory reset to zero, inventory increasing on its own, stock count wrong, adjustment history, who changed my inventory, phantom inventory, inventory audit trail, AI inventory monitoring
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

The number is wrong on a Tuesday morning. The linen shirt in medium, the one you packed the last unit of on Saturday with your own hands, shows 41 available. You own one store, you did the year-end count yourself, and you know the true number is zero. You set it to zero, save, and get on with the day.

Thursday, it is 41 again. Nothing in the admin blinked. No app sent an email, no staff member owns up, no order or return touched the product. The count simply moved, the way it apparently has been moving for a while, because now that you are looking, other numbers are off too. And the store sells whatever the number says it has. Somewhere between Tuesday and Thursday your shop began cheerfully promising customers forty shirts that do not exist.

## A poltergeist with write access

This is not the overselling problem, or not at first. When [two channels race for the last unit](https://blog.dugong.live/how-to-prevent-overselling-on-shopify-across-channels.html), the count was right and the timing was cruel. This failure is stranger: the count itself moves, up or down, with no sale and no shipment behind it. Sold out products refill themselves. Full products zero out at night. The stock take you finished last week is quietly un-happening, one SKU at a time, and everything downstream of the number, the storefront badge, the ad spend, the reorder math, inherits the fiction.

What makes it expensive is what makes it maddening: you find out at the worst possible moment, from the outside. The refilled shirt sells and you refund an order you should never have received. The zeroed bestseller sits invisible all weekend while [the ads that point at it](https://blog.dugong.live/how-to-automatically-pause-ads-for-out-of-stock-products-on-shopify.html) keep spending. And because the change wore no error and rang no bell, you cannot even say when it happened, only that at some point the store stopped telling the truth.

## The community record

The reference thread was opened in May 2022 by a merchant whose counts kept climbing on their own: no restocks, no returns, no dropshipping, and for some items more units than she had ever ordered in the product's lifetime. She corrected them by hand and watched some climb back. The thread was still collecting new cases in February 2025, which makes it very nearly three years of merchants filing into the same room to describe the same ghost.

The details are the good part, because every detail is a clue. In January 2023 a toy shop owner reported that the ranges she definitely sold out of before Christmas were back in stock at their original numbers; her staff had told her the numbers were changing and she had not believed them until a whole range resurrected itself. A day later she posted her own diagnosis: the adjustments traced back to the wholesale marketplace she ordered the toys through, a purchasing connection quietly writing retail stock counts. In May 2023 another merchant described items with one unit showing more than forty. A month earlier, one wrote the sentence that should be printed on the problem: this has been ongoing for two years now and support are unable to assist, at least once a month, small inventory levels, often caught short. In August 2023 a merchant with a low stock [Flow](https://help.shopify.com/en/manual/shopify-flow) alert acquired an accidental monitoring system: every night at 9:20pm his digital products reset to zero. He set them back to 1000; the next night they were zero again, five nights running, alert emails each time. In September 2023 another discovered that duplicating a product had been doubling its inventory, and summarized the aftermath in one line: overselling, refunds, and Shopify's response just blames the user. By December 2024 a thrift store owner was turning away sales for items the system swore he still had, and a veteran of the thread offered the workaround he had settled on: show one less unit than you actually have. January 2025, a merchant finished a week of year-end counting and was out of sync again immediately, forty phantom products, the wholesale connection once more. In February 2025 a five-year merchant said the quiet part: if this cannot be sorted, I leave when the subscription is up.

A second thread, from May 2023, supplies the dark twin. A merchant woke to find the majority of the catalog reset to zero overnight. No inventory apps installed. Nobody on the team had touched it. And the adjustment history, the tool whose whole job is to answer this question, showed no evidence of the change. Support's advice was to come back with a list of affected products and the window of time in which the values changed, which is to say: do the forensics yourself, then we can talk. Ten months later the only update in the thread was a new merchant asking, was this resolved? Having the same issue today and no one can help. The satellite threads say the same thing at scale: why does my inventory keep resetting to zero on its own, active April 2025; why is my e-commerce inventory always incorrect, 23 replies and 632 views, active February 2025; inventory glitches in the Shopify app, 920 views. Shopify staff, in the main thread, stated the platform's position plainly: inventory numbers should not change without a user or an app making those changes. Which is true. It is also the problem.

> **◆ NOTE** The record, in the merchants' own words: counts higher than any quantity ever ordered. Sold out Christmas toys back at their original numbers, twice, a year apart, both times traced to a wholesale purchasing connection. One unit showing as more than forty. Zero resets at 9:20pm, five nights running. Ongoing for two years, support unable to assist. A catalog majority zeroed overnight with an adjustment history showing nothing. And the workaround a merchant reached after years: show one less unit than you actually have.

## Why counts move on their own

There is no ghost. There is a number with more authors than you think. A connected sales or purchasing channel is allowed to write inventory, and a wholesale marketplace that doubles as your supplier can push its idea of stock over yours, which is exactly what the toy shop caught. A dropshipping or product import app resyncs on its own schedule and restores whatever its remote source believes, the same clobbering behavior as [the supplier feed that zeroed your catalog](https://blog.dugong.live/how-to-sync-supplier-inventory-feeds-to-shopify.html). Duplicating a product can double counts. A bulk CSV import made for a price change silently carries an inventory column from the day it was exported. A POS tap, a staff edit, a [second store sync](https://blog.dugong.live/how-to-sync-inventory-between-two-shopify-stores.html) pointed the wrong way, a [bundle app doing component math](https://blog.dugong.live/how-to-sync-bundle-inventory-with-component-stock-on-shopify.html) at the wrong moment, an integration built on an old API writing Available when it meant On hand: every one of these is a hand on the same dial, and none of them is required to tell you it turned it.

Each cause is mundane. What they share is that from inside the admin they are invisible until you go looking, and the looking is the hard part.

## The admin shows the number, not the story

Shopify does keep receipts, in the adjustment history, and when it works it is exactly the right tool: date, activity, and a Created by column naming the staff member, app, or [sales channel](https://help.shopify.com/en/manual/online-sales-channels) behind every change. But it is built for spot checks, not audits. You read it one variant at a time, product by product, so sweeping a thousand-SKU catalog through it is a career. It reaches back 180 days, and for anything older you are sent to a separate report. Some of its labels close no case at all: Data correction, per the help docs, means an error correction that was made automatically, which names a machine and no motive. And in the zeroed-catalog thread the history showed nothing at all, which converts the tool's promise into its failure mode: when the record is the thing you doubt, a record with gaps is worse than none, because it argues the change never happened. It is the same shape as [the slipped decimal that sells all night](https://blog.dugong.live/how-to-catch-pricing-errors-on-shopify-before-orders-flood-in.html): the platform holds the current value with total confidence and holds the story of how it got there loosely.

## The stock take is the right idea in the wrong tool

Notice what every merchant in those threads independently built: a verification loop. Monthly counts, year-end counts, staff walking shelves with a tablet, the number in the system checked against the number in the world. That is the correct instinct, and it is the whole design, and it does not scale in the dimension that matters, which is time. A monthly count catches a Tuesday corruption up to twenty-nine days late, which on a store doing any volume is twenty-nine days of selling fiction, and it produces no attribution: you learn the count is wrong, never who made it wrong, so next month you are counting again. The merchant showing one less unit than he owns has, in effect, taxed every SKU he sells to insure against a system he cannot see into. The thrift shop declining sales it could have made is paying the same tax in the other currency.

## What the automation actually has to do

As a Dugong playbook, in plain prose:

```
# trigger
On every inventory adjustment,
and on a clock for the sweep

# steps
1. Baseline the flow: each SKU's
   normal movement, and who is
   allowed to write to it
2. Watch every adjustment as it
   lands: all variants, all
   locations, no 180 day limit
3. Match each change to its story:
   an order, a restock, a
   transfer, a named app
4. Flag the orphans in minutes:
   the change no story explains,
   evidence attached
5. Name the culprit: Created by
   plus the pattern; 9:20pm
   nightly means a schedule
6. Keep the ledger: your own
   audit trail, queryable, that
   never expires
7. Report weekly: what moved, what
   explained itself, which door
   the rest came through
```

Step three is the heart. Almost every adjustment in a healthy store has a story that closes: a sale decrements, a [return restocks](https://blog.dugong.live/how-to-automatically-restock-returns-on-shopify.html), a transfer arrives, an app you installed does the thing you configured it to do. The watcher's job is to ask, of each change, what explains this, and to file the explained ones silently. What remains is a short, damning list: the increment with no order anywhere near it, the sold out product that refills to its pre-sale count, the write from an app that has no business touching that SKU, the zero landing at 9:20pm sharp. On the day the toy shop's Christmas range resurrected, that list would have held forty entries with the same author and the same minute, a pattern that names its source better than any support ticket.

Step four is where the judgment lives, because the naive rule, alert on every unexplained change, drowns you the first week. A one-unit wobble on a fast mover during a busy hour is probably a timing artifact; the same wobble on a dead SKU at 3am is a signal; a forty-unit jump on a product whose lifetime order quantity is twelve is a siren regardless of the hour. Plausibility per SKU is exactly the kind of reading a person does effortlessly and a threshold cannot, the same judgment that runs through [every automation worth building](https://blog.dugong.live/best-shopify-automations-to-set-up.html): the rule is cheap, knowing when the rule applies is the work.

Step six pays off the day you need the past. Your own ledger of every adjustment, source attached, queryable by SKU or app or hour, is the difference between answering support's list of affected products and the window of time in an afternoon and abandoning the investigation the way the threads do. It also feeds the downstream workflows that currently inherit the fiction: [reorder points](https://blog.dugong.live/how-to-set-inventory-reorder-points-on-shopify.html) computed on corrupted counts buy stock you own, and [back in stock alerts](https://blog.dugong.live/how-to-set-up-back-in-stock-notifications-on-shopify.html) fired by a phantom refill email your most interested customers about products you cannot ship. A count you can trust is not one workflow; it is the floor under all of them.

The honest limit, stated plainly: none of this stops a misbehaving integration from writing to your store. If a channel or app is corrupting counts, the fix is disconnecting it, scoping its permissions, or making its vendor fix it, and only you can decide that. Nor can any tool restore a number that was overwritten before anyone was watching; the zeroed catalog with the silent history is gone as history. What changes is discovery time and evidence. Every case in the record was discovered late, by a stock take, a staff member's disbelieved report, or a customer holding a refund. A watched store discovers the same write in minutes, with the author attached, while the revert is still one click and the blast radius is still one SKU.

## Why this is a compiler problem, not an app problem

Inventory apps exist, and the threads recommend several, and most of them are another writer: one more hand on the dial, with its own sync schedule and its own idea of the truth. What this failure wants is not another author but a witness, and the definition of suspicious is specific to your store in a way no settings page survives. Which apps are allowed to write inventory at all, and to which locations? Is Faire supposed to touch retail stock, or only purchasing? How big a swing is plausible for this SKU, at this velocity, in this season? Does a POS adjustment at 2pm on a Saturday mean a sale floor correction or a mistake? Who gets paged for a zero reset on a bestseller, and does the answer change during a drop? Those are sentences about your operation. They should compile into the watcher as written, instead of being shaved down to whatever a threshold field happens to accept.

Run the Tuesday shirt again with the sentences compiled. Saturday, 11:41pm, an app writes 41 to a SKU whose true count is zero and whose lifetime order maximum is twelve. The write has no order, no transfer, no restock behind it; the author is a purchasing integration that is not on the list of permitted writers for retail stock. The alert lands at 11:44 with the SKU, the swing, the author, and the before-value; whoever is on duty revert-clicks it Sunday morning and files the app for a permissions review. The shirt never sells a unit that does not exist, the stock take you did last week stays done, and the ghost turns out to have a name, a schedule, and an uninstall button.

## The workflow worth building this week

Start with attribution on the products that hurt, today. Pick your twenty bestsellers, open each variant's adjustment history, and read the Created by column with a cup of coffee. Most merchants who do this meet at least one author they did not expect. For anything older than 180 days, pull the inventory adjustment changes report and filter by app. You are not fixing anything yet; you are finding out how many hands are on the dial.

Then write the permission list in plain language: which apps, channels, and people are supposed to write inventory, to which locations, and roughly how much movement is normal for your catalog's tiers. This list is the spec. Put the watcher on in observe mode for a week, let it match adjustments to stories, and read what it could not explain. Some of the orphans will be innocents, a timing quirk, a staff correction nobody mentioned; tune with those. The ones that remain are your ghost, pre-named.

Then say the brief the way you would hand it to a new hire. Watch every inventory change in the store. If a change has no order, return, or transfer behind it and did not come from someone on this list, tell me within the hour, with the SKU, the size of the change, who made it, and what the count was before. Zero resets and refills of sold out products are urgent, wake someone up. Keep a log of everything forever, and every Monday tell me what moved, what explained itself, and which door the rest came through. That is the whole paragraph. The compiler turns it into the workflow, and the next time a count changes at 9:20pm, you know by 9:21.

> **◆ READING** Two companion pieces if this one landed: [the supplier feed that zeroed your catalog](https://blog.dugong.live/how-to-sync-supplier-inventory-feeds-to-shopify.html), on the loudest version of an outside hand on your counts, and [the overselling problem no one automates](https://blog.dugong.live/how-to-prevent-overselling-on-shopify-across-channels.html), on what happens downstream once the number is wrong.

If you are a Shopify merchant with an inventory ghost story, the count that came back, the author you finally caught in the adjustment history, the stock take that un-happened, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Why does my Shopify inventory keep changing by itself?

Because something with write access is changing it, and nothing in the admin volunteers what. Shopify staff said it plainly in a June 2023 community reply: inventory numbers should not change without a user or an app making the change. In the documented cases the culprit was findable once someone looked. A wholesale marketplace connection wrote retail stock counts back into the store, which is how one merchant's sold out Christmas toys returned with their original numbers, twice, a year apart. A dropshipping app resynced on its own schedule. Duplicating a product, one merchant discovered, doubled its inventory. A bulk CSV import overwrote counts, a POS tap or staff edit went unlogged, an integration wrote Available when it meant On hand. The changes also cluster in patterns that name their source: the merchant whose digital products reset to zero at 9:20pm five nights running was watching a scheduled job, not a ghost. Start with the adjustment history on an affected variant and read the Created by column. If it names an app, you have your answer. If the history shows nothing at all, as it did for the store that woke to most of its catalog at zero, you are in the class of failure where the record itself missed, and the only reliable fix is watching adjustments as they happen instead of reconstructing them afterward.

Permalink: https://blog.dugong.live/how-to-stop-your-shopify-inventory-changing-by-itself.html#faq-1

### How do I find out what changed my Shopify inventory?

Open the product, pick the variant, and click View adjustment history. Every recorded change lists the date, the activity, and a Created by column naming the staff member, app, or sales channel that made it. Three limits matter. You can only view history one variant at a time, so auditing a catalog this way is a product by product march. The page reaches back 180 days; for anything older you need the Inventory adjustment changes report, which filters by SKU, location, staff member, app, and reason. And the labels are not always a story: an entry like Data correction is defined in Shopify's help docs as an error correction that was made automatically, which tells you a machine changed your number and little else. When merchants take unexplained changes to support, the request that comes back is a list of affected products and the window of time in which the values changed, which is exactly the evidence the admin makes laborious to gather. That is the case for keeping your own ledger: a watcher that records every adjustment as it lands, with its source attached, has the product list and the time window ready the day something goes wrong, and it does not expire at 180 days.

Permalink: https://blog.dugong.live/how-to-stop-your-shopify-inventory-changing-by-itself.html#faq-2

### Can AI catch unexplained Shopify inventory changes automatically?

Yes, because the job is attribution, and attribution is a reading task. An automation like Dugong subscribes to inventory adjustments as they happen and asks of each one the question you would ask: what explains this? A sale explains a decrement. A refund with restock explains an increment. A transfer received, a purchase order, a named app doing what you configured it to do, all stories that close. What is left are the orphans: the increment with no order anywhere near it, the zero reset at 9:20pm, the sold out product that quietly refills to its pre sale count. Those get flagged in minutes with the evidence attached, the SKU, the size of the swing, what wrote it, and what the count was before, so the fix is a revert and an app permissions review instead of a store wide recount. The honest limit: automation cannot stop a misconfigured integration from writing to your store. Disconnecting or fixing it is your call to make with that vendor. What changes is that you learn about the write the hour it happens, with the culprit named, instead of at the next stock take, or worse, from a customer who just ordered a product you do not own.

Permalink: https://blog.dugong.live/how-to-stop-your-shopify-inventory-changing-by-itself.html#faq-3

### Which apps and channels can change Shopify inventory without telling me?

Any of them with write access, and the list is longer than most merchants expect. A connected sales or purchasing channel is allowed to write inventory, which is how one toy shop's wholesale marketplace, doubling as its supplier, pushed its own idea of stock over hers and resurrected a sold out Christmas range. A dropshipping or product import app resyncs on its own schedule and restores whatever its remote source believes. Duplicating a product can double counts. A bulk CSV import made for a price change silently carries the inventory column from the day it was exported. Add a POS tap, a staff edit, a second store sync pointed the wrong way, a bundle app doing component math at the wrong moment, and an integration built on an old API writing Available when it meant On hand, and you have a number with more authors than you think. None of them is required to announce the edit. The way to find your store's culprits is the adjustment history's Created by column, checked on the SKUs that move, and an audit that matches every change against the sales that should explain it.

Permalink: https://blog.dugong.live/how-to-stop-your-shopify-inventory-changing-by-itself.html#faq-4

### How far back does Shopify's inventory adjustment history go?

180 days, viewed one variant at a time, and for anything older you are sent to a separate report. Within that window it records the date, the activity, and a Created by column naming the staff member, app, or sales channel behind every change, which makes it exactly the right tool for a spot check and a poor one for an audit: sweeping a thousand SKU catalog through it product by product is a career. Two of its limits matter in practice. Some labels close no case, since Data correction officially means an error correction that was made automatically, which names a machine and no motive. And in the documented zeroed catalog case the history showed nothing at all, so the record you were promised can have gaps precisely where you doubt it. Treat the history as evidence rather than the audit itself: the durable version is a ledger kept outside the window, where every movement is matched to an order, a return, or a named adjustment the hour it happens, and anything unexplained gets flagged while the trail is fresh.

Permalink: https://blog.dugong.live/how-to-stop-your-shopify-inventory-changing-by-itself.html#faq-5

---

Markdown rendition of https://blog.dugong.live/how-to-stop-your-shopify-inventory-changing-by-itself.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
