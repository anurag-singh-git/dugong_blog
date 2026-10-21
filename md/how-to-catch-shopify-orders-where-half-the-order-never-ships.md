# How to catch Shopify orders where half the order never ships

> You shipped two of three items and the third fell out of every report. The AI playbook that finds every Shopify remainder, clears it, and tells the customer first.

- Canonical: https://blog.dugong.live/how-to-catch-shopify-orders-where-half-the-order-never-ships.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-10-14
- Section: Research
- Word count: 2468
- Dispatch: Nº 127 · Research · 8 min read
- Full headline on page: How to catch Shopify orders where *half the order never ships*
- Keywords: shopify partially fulfilled, shopify order half shipped, shopify unfulfilled line items report, shopify fulfillment order still open, shopify in progress fulfillment status, shopify flow partially fulfilled trigger, line_item_fulfillment_status shopifyql, shopify split shipment customer notification
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

The email arrives on day nine. Where is the rest of my order. You open it, and the story is right there: two items picked and shipped the morning after checkout, tracking says delivered, and the third line sitting exactly where it was. No failed sync, no error, no flag. The order is marked **Partially fulfilled**, which is Shopify agreeing that something is missing and then doing nothing else about it.

Shipping part of an order is usually the right call. Send what you have, follow with the rest, keep the customer moving. The problem is never the split. It is the follow. Shopify tracks a shipment beautifully. It does not track the remainder.


## The short answer

Two of the three items shipped the next morning. The third never moved, and Shopify marked the order Partially fulfilled, which is the platform agreeing that something is missing and then doing nothing about it. The remainder falls out of the reports you actually read, because report filters work at the order level and not the line item level. The AI playbook that sweeps for every open remainder nightly, ages it from the last shipment rather than the order date, names which of seven causes produced it, tells the customer what is still coming before they ask, and closes it honestly.
## What partially fulfilled actually means

Shopify's own definition is one sentence. The Help Center says you get the Partially fulfilled status when you fulfill part of the items in an order. The Admin API enum is no more generous: some of the items in the order have been fulfilled. That is the whole of it. A label on the order, with no owner and no clock.

Underneath, the model is more useful than the label. Shopify splits every order into fulfillment orders, which the developer documentation describes as either an item or a group of items in an order that are expected to be fulfilled from the same location. Shopify creates them automatically, you cannot create them by hand, and an order can carry several, including more than one at the same location. The same docs note that multiple fulfillments can exist for a single order when items either ship separately or from different locations.

So a half shipped order is not one ambiguous thing. It is one fulfillment order that is finished and at least one that is still open. The open one is a real piece of work sitting in your store. Nothing in the admin presents it as work.

## Eleven statuses, and four of them hide a job

The order display fulfillment status list has eleven values. Four of them mean something still has to ship, and all four read like a conclusion rather than a task. **Partially fulfilled**, some items gone. **On hold**, where every unfulfilled item in the order is paused. **Scheduled**, where every unfulfilled item is set to ship at a later time. And **In progress**, which is the one that catches people, because it means a request for fulfillment was sent to the fulfillment service, or you marked it in progress yourself while picking.

In progress is your 3PL confirming it received the job. It is not the 3PL doing the job. If you need evidence that the gap between those two is a real operational problem, Shopify Flow ships a trigger literally named fulfillment order fulfillment service failed to complete fulfillment. There is a fifth status worth watching too, Request declined, which means the fulfillment service rejected some of the items.

Nothing in the admin ages any of them. The status tells you what the order is. It never tells you how long it has been that way, which is the only part that matters.

## The reporting hole merchants keep finding

Here is the mechanical reason these orders go missing rather than merely getting forgotten. A merchant posted it precisely on 7 August 2026: when filtering reports by fulfillment status, the filter operates at the order level, not the line item level. Their example was order 2312, twenty five items, twenty four fulfilled, one unfulfilled, and it does not appear in the unfulfilled items report at all. No staff reply. No resolution. They also mentioned that the feedback link the support chatbot gave them returned a 404.

Two and a half months earlier, on 20 May 2026, another merchant filed the matching feature request: the ShopifyQL `FROM sales` dataset does not expose a `line_item_fulfillment_status` field for filtering. The only substantive reply said they did not expect ShopifyQL to add it any time soon, suggested the GraphQL Admin API `fulfillmentOrders` query as a workaround, and said they would vote for the request anyway. No staff answer there either.

Put those together and you get the perverse bit. The bigger the order, the more invisible the leftover. A single item order that never ships reads as Unfulfilled and turns up in every view you own. A twenty five item order with one item outstanding reads as Partially fulfilled and turns up in none of them.

People have been trying to work around this for years. In May 2024 a merchant asked how to isolate orders where one specific product was the unfulfilled line. The answer was a Flow with a for each loop, plus the useful caveat that Flow has no action that marks an order itself as fulfilled, only fulfillment orders. The thread ends with the original poster still asking how the loop behaves and a second merchant, three months later, asking whether it ever worked. Nobody replied.

## Seven ways an order goes out half done

Worth naming these, because the response is different for each and because most of them are not mistakes.

**One.** Stock sits at two locations, so Shopify creates a fulfillment order per location, and one location ships today while the other has not been picked. **Two.** A line is out of stock, oversold or on backorder. **Three.** A preorder or made to order item is riding along with in stock items. **Four.** Part of the order is on hold. Worth knowing that checkout upsell offers set a temporary hold automatically, and that releasing a hold returns the items to Unfulfilled, so a nine day old remainder can suddenly look like a brand new job. **Five.** A fulfillment service accepted the request and went quiet, or declined part of it. **Six.** A personalized or built to order line is waiting on production. **Seven.** Somebody shipped what was on the bench to clear the screen, and fully intended to come back to it.

Only two of those are errors. The rest are ordinary operations missing a follow through step, which is exactly why being more careful never fixes it.

## Your customer gets told half the story

The shipping confirmation is built around the fulfillment, not the order. The customer receives a tracking number for what left the building and no word at all about what stayed behind.

A merchant who said they often partially fulfill orders asked for the fix on 18 July 2024: a way to tweak the email templates to show the line items that are unfulfilled. One person replied, suggesting a test of the `fulfillment.fulfillment_line_items` variable, documented as a list of fulfillment line items to be fulfilled, and said testing was needed to know what it actually returns. Nobody ever confirmed. The thread is still open.

So the customer reads a shipping notification, sees tracking, and concludes the order is on its way. The light box is a surprise, and surprise is the expensive part. Best case it arrives as a where is my order ticket. Worst case it is a missing item claim or a card dispute, and you are now arguing about a parcel you can prove you sent, for an item you can prove you did not.

> **◆ FROM THE FORUMS** October 2023, a merchant with a two item order: one shipped, one cancelled by the vendor. Their questions were how to update the order status and why the customer was never notified of the cancellation. One reply, from another merchant, said refund the cancelled item, email the customer the reason, and write yourself an SOP. No staff answer. That is still the state of the art.

## The Flow trap on top

You would reasonably assume the Order fulfilled trigger means the order is fulfilled. It does not. Shopify's own page says the trigger starts a workflow when fulfillment of one or more line items in a fulfillment order is successful, and warns that it is possible for this trigger to start a workflow multiple times for the same order. The same page's meta description says it starts when all the line items in an order are fulfilled. The documentation contradicts itself, and the behavior is the first one.

Which means every workflow you hung off Order fulfilled is firing on the half order: the thank you email, the review request, the loyalty points, the accounting sync, the rate your delivery prompt. Some fire twice. You are asking for a review of a product that has not arrived.

And the trigger you actually want does not exist. Flow's fulfillment bench is long: fulfillment created, fulfillment event created, fulfillment order placed on hold, holds released, merged, split, moved, rescheduled, ready to fulfill, line items prepared for pickup or local delivery, fulfillment request submitted, accepted and rejected, cancellation request submitted, accepted and rejected, and the service failure one. Every single one needs something to happen. Your problem is that nothing is happening.

The one native route is the Scheduled time trigger: runs on a clock, at most once every ten minutes, repeating in days, weeks or months up to a year, carrying no order data of its own, so you add a get order data step and loop over the results. That is a nightly sweep that you build and maintain. It is the correct shape. It is just not a feature.

## What it costs while nobody counts

Run twelve hundred orders a month with five percent going out partially fulfilled and you have sixty open remainders a month. Most close in a day. Say ten do not. That is ten support threads you did not start, a handful of goodwill refunds, and ten orders that will never close.

The inventory cost is the one people miss. An unfulfilled line holds committed stock, so the unit is unavailable to sell while sitting against a sale that is never completing. Your product page says sold out and the shelf says otherwise, and the cause is three orders you half shipped in August. [The stock Shopify will not let you sell](https://blog.dugong.live/how-to-fix-shopify-committed-inventory-that-never-clears.html) is that problem from the other end.

## The playbook worth building

As a Dugong playbook, in plain language:

```
# trigger
Nightly, and four hours after
every fulfillment, over all
open orders

# steps
1. Sweep for any order with a
   fulfillment order still
   open, in progress, on hold
   or scheduled, holding at
   least one unfulfilled unit
2. Age each remainder from the
   last shipment, not from the
   order date
3. Name the cause: stock, hold,
   declined request, scheduled,
   split location, silent
   service, custom build
4. Route it to the one person
   who can clear that cause
5. Tell the customer which item
   is still coming, and a date
   you can keep
6. Escalate: flag at 24 hours,
   chase at 5 days, force a
   decision at 10
7. Close it: ship it, or cancel
   and refund the remainder,
   restock the unit, release
   the committed stock
8. Count leftover rate per SKU
   and per location, and hours
   from first to last shipment
```

**Step two is the one everyone skips.** Age these from the order date and the list lies to you, because the order looks handled: it shipped, it has tracking, it is nine days old and so is everything else from that week. Age from the last shipment and the number is honest. Nine days since anything moved on this order is a sentence nobody can argue with.

**Step five is where the money is.** Most of these never become tickets if the customer hears it from you first. One line naming the item and a date turns a complaint into a non event, and it costs you nothing but the sending.

## Three numbers to write down

The build is an afternoon. The decisions are what stall people, and all three are small. How many hours after a partial fulfillment the remainder gets flagged, which should be twenty four. How many days you wait before you stop waiting and refund, which should be ten. And the order value above which a human reads the case before anything is cancelled. Pick those three and the rest is configuration.

## Where AI earns its place

Three jobs here, and none of them is running a query.

**Reading the reason.** Finding the orders is mechanical. Knowing why each remainder is stuck is not, because the answer is scattered: a hold reason, the text of a declined fulfillment request, inventory at the assigned location, a note somebody typed into the timeline, sometimes a supplier email that never touched Shopify at all. A model reads all of it and names the cause, which is what makes routing possible.

**Writing the note.** Not a template with a merge field. The specific item, the honest date, and the tone of someone who already knew. That is the difference between a customer who waits and a customer who disputes.

**The small economic calls.** Whether a four dollar remainder is worth a nine dollar parcel of its own, or whether it should be refunded with an apology and a note on the SKU.

Keep two things human. Cancelling and refunding above whatever value you set, because that is money and a relationship. And anything that changes what the customer pays.

## Do this before you close the laptop

Filter your orders by Partially fulfilled, sort oldest first, and count the list. That number is your backlog and it has been sitting there the whole time. Then open the oldest three and find the remainder in each. In most stores one is waiting on stock that arrived weeks ago, one is waiting on a person who no longer works there, and one should have been refunded in September.

> **◆ READING** Two companion pieces if this one landed: [The order your warehouse never heard about](https://blog.dugong.live/how-to-catch-shopify-orders-that-never-sync-to-shipstation.html), on orders that never reach the 3PL at all, and [The preorder that holds your order hostage](https://blog.dugong.live/how-to-set-up-pre-orders-on-shopify-without-holding-in-stock-items.html), on splitting the wait from the ship on purpose.

Sitting on a pile of partially fulfilled orders nobody owns, a 3PL that accepts requests and goes quiet, or one SKU that leaves a remainder every time it sells? The inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Why does Shopify say my order is partially fulfilled?

Because some of the items shipped and some did not. Shopify's Help Center defines the status in one line: you get Partially fulfilled when you fulfill part of the items in an order. The Admin API enum says the same thing, that some of the items in the order have been fulfilled. Underneath, Shopify splits every order into fulfillment orders, which the developer documentation describes as either an item or a group of items in an order that are expected to be fulfilled from the same location, created automatically, with more than one possible per order and even more than one at the same location. A half shipped order is therefore one fulfillment order that is closed and at least one that is still open. The open one is real work. Nothing in the admin presents it as work, gives it an owner, or starts a clock on it, which is why these orders sit.

Permalink: https://blog.dugong.live/how-to-catch-shopify-orders-where-half-the-order-never-ships.html#faq-1

### How do I find Shopify orders with unfulfilled items when the order shows as partially fulfilled?

Not through the reports, and that is the trap. A merchant posted the mechanics on 7 August 2026: when filtering reports by fulfillment status, the filter operates at the order level, not the line item level. Their example was order 2312 with 25 items, 24 fulfilled and one unfulfilled, which never appears in the unfulfilled items report. No staff reply, no resolution. A second merchant filed a feature request on 20 May 2026 because the ShopifyQL FROM sales dataset does not expose a line_item_fulfillment_status field for filtering, and the only reply said not to expect ShopifyQL to add it soon and to use the GraphQL Admin API fulfillmentOrders query instead. So the practical answer is the API. Query each order's fulfillment orders, keep the ones whose status is still open or in progress, and read the unfulfilled quantity on their line items. The perverse part is that the bigger the order, the more invisible the leftover: a single item order that never ships reads as Unfulfilled and appears everywhere, while a 25 item order with one item left reads as Partially fulfilled and appears nowhere.

Permalink: https://blog.dugong.live/how-to-catch-shopify-orders-where-half-the-order-never-ships.html#faq-2

### Does Shopify tell the customer which items have not shipped yet?

No. The shipping confirmation is built around the fulfillment, not the order, so the customer gets a tracking number for what went out and no mention of what stayed behind. A merchant who said they often partially fulfill orders asked on 18 July 2024 for a way to tweak the email templates to show the line items that are unfulfilled. The one reply suggested testing the fulfillment.fulfillment_line_items variable, documented as a list of fulfillment line items to be fulfilled, and said testing was needed to know what it returns. Nobody confirmed it worked and the thread is still open. The result is predictable. A customer reads a shipping notification, sees tracking, and concludes the order is on its way, so the light box is a surprise. That surprise arrives as a where is my order ticket if you are lucky and as a missing item claim or a card dispute if you are not. Until Shopify changes the template, the fix is to send your own short note naming the item that is still coming and when.

Permalink: https://blog.dugong.live/how-to-catch-shopify-orders-where-half-the-order-never-ships.html#faq-3

### Can Shopify Flow alert me when an order is still partially fulfilled after a few days?

Not with an event trigger, because nothing is happening and Flow listens for things happening. The fulfillment bench is long: fulfillment created, fulfillment event created, fulfillment order placed on hold, holds released, merged, split, moved, rescheduled, ready to fulfill, line items prepared for pickup or local delivery, fulfillment request submitted, accepted and rejected, cancellation request submitted, accepted and rejected, and fulfillment service failed to complete fulfillment. None of them fires because a remainder has been sitting for nine days. There is also a trap worth knowing: the Order fulfilled trigger does not mean the order is complete. Shopify's own page says it starts a workflow when fulfillment of one or more line items in a fulfillment order is successful, and warns that it is possible for this trigger to start a workflow multiple times for the same order, while the same page's meta description says it starts when all the line items in an order are fulfilled. The behavior is the first one, so review requests, thank you emails, loyalty points and accounting syncs hung off Order fulfilled all fire on the half order. The only native route to an aging alert is the Scheduled time trigger, which runs on a clock at most once every ten minutes, repeats in days, weeks or months up to a year, and carries no order data, so you add a get order data step and a loop. That is a nightly sweep you build and maintain yourself.

Permalink: https://blog.dugong.live/how-to-catch-shopify-orders-where-half-the-order-never-ships.html#faq-4

### What is the difference between In progress and Partially fulfilled on a Shopify order?

Partially fulfilled means something physically shipped and something did not. In progress means nothing has shipped yet and a request for fulfillment has been sent to the fulfillment service, or you marked it in progress yourself while picking. In other words, In progress is your 3PL saying it received the job, not that it did the job. Both are easy to read as resolved. Of the eleven values in the order display fulfillment status list, four of them mean work is still outstanding while reading like a conclusion: Partially fulfilled, In progress, On hold, where every unfulfilled item in the order is paused, and Scheduled, where every unfulfilled item is set to ship later. Request declined is a fifth, and it means the fulfillment service rejected some of the items. Flow even carries a trigger called fulfillment order fulfillment service failed to complete fulfillment, which tells you how often a service accepts a request and then does not finish. Nothing in the admin ages any of these, so the difference that actually matters is not the label, it is how long it has carried it.

Permalink: https://blog.dugong.live/how-to-catch-shopify-orders-where-half-the-order-never-ships.html#faq-5

### Can AI manage partially fulfilled Shopify orders?

It fits this one well, because the hard part is reading scattered context rather than counting. Finding the orders is a query. Knowing why each remainder is stuck is not, since the reason is spread across a hold reason, the text of a declined fulfillment request, inventory at the assigned location, a note somebody typed into the timeline, and sometimes a supplier email that never touched Shopify. A model can read all of that, name which of seven causes applies, and route the order to the one person who can clear it. It can also write the customer note that names the exact item and gives a date you can keep, which is the single thing that stops most of these from becoming tickets. And it can make the small economic call on whether a four dollar remainder is worth a nine dollar parcel of its own. Keep two decisions human. Cancelling and refunding a remainder above whatever value you set, because that is money and a customer relationship. And anything that changes what the customer pays.

Permalink: https://blog.dugong.live/how-to-catch-shopify-orders-where-half-the-order-never-ships.html#faq-6

---

Markdown rendition of https://blog.dugong.live/how-to-catch-shopify-orders-where-half-the-order-never-ships.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
