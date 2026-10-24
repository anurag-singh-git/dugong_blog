# How to catch Shopify inventory transfers that never get received

> Stock can sit on your own shelves, paid for and counted, and still be unsellable. Shopify will not tell you, because nothing went wrong. Something simply stopped.

- Canonical: https://blog.dugong.live/how-to-catch-shopify-inventory-transfers-that-never-get-received.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-10-24
- Section: Research
- Word count: 3560
- Dispatch: Nº 135 · Research · 13 min read
- Full headline on page: How to catch Shopify inventory transfers that *never get received*
- Keywords: shopify inventory transfer not received, shopify transfer stuck in progress, shopify incoming inventory not available, shopify receive inventory transfer, shopify flow inventory transfer trigger, shopify purchase order incoming inventory, shopify unreceived transfer alert, AI inventory transfer monitoring
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

A pallet lands at the back door on a Thursday. Somebody signs for it, cuts the wrap, and stacks the boxes where the boxes go. The stock is now in the building. It is counted, it is paid for, and it is twenty feet from the person who will pack it.

Nobody opens the transfer in the Shopify admin and clicks Receive.

From that moment your store is holding inventory it cannot sell. Not because of a sync bug, not because an app fell over, not because anything failed. The transfer is still sitting at In progress, which is a perfectly healthy status, and Shopify has no opinion about how long a transfer should stay there.

Three weeks later somebody notices that a best seller has been sold out on the website since the Thursday the stock arrived.

## The short answer

Incoming inventory is not available inventory. Shopify's own definition is that incoming stock is on its way to your location from inventory transfers or apps, and that it is not available to sell until it has been received and its state has been changed to Available. So a transfer nobody finished receiving is stock you own, standing in your own stockroom, that your storefront will not sell.

Partial receiving is where this actually happens. Shopify documents that if you only receive some items, the transfer stays In progress until you receive the remaining ones. Somebody counts the first two cartons, gets called away, and the rest never gets a second look.

Shopify Flow has eighty-three triggers and exactly two of them concern transfers: Inventory transfer ready to ship, and Inventory transfer completed. Both fire when things go right. Nothing fires when a transfer stops moving, because stopping is not an event.

Webhooks do not help either. The transfer event topics fire on field changes, and the field you care about is status. A stalled transfer never changes status, so there is nothing to subscribe to. This one needs a clock, not a listener.

The number to watch is on the API object and nowhere in the admin: total quantity minus received quantity, per transfer, filtered to transfers older than the lead time for that route. That is the count of units you have bought and cannot sell.

And if your reorder reports keep telling you to buy stock you already bought, that is the same hole from the other side. Incoming is derived from shipments, not from purchase orders, so an open purchase order contributes nothing to incoming at all.

## Incoming is not available, and Shopify is explicit about it

Most of the confusion here dissolves the moment you read Shopify's [inventory states](https://help.shopify.com/en/manual/inventory-and-locations/fundamentals/inventory-states) page slowly. There are five states and they do not overlap the way people assume.

Incoming is inventory "that's on its way to your location from inventory transfers or apps", and it "isn't available to sell until it has been received and its state has been changed to Available". Available is inventory "that you can sell", and the page adds, in so many words, that it "doesn't include inventory that's considered Incoming". On hand is "all inventory units that you have at a location", made up of the total of [Committed](https://blog.dugong.live/how-to-fix-shopify-committed-inventory-that-never-clears.html), Unavailable and Available.

Read those three definitions together and the shape of the problem appears. Incoming is not in Available, and On hand is defined without it. An unreceived transfer therefore sits outside every number your store sells against. The boxes are physically present and administratively absent.

This is also why nothing looks broken. Your [oversell protection](https://blog.dugong.live/how-to-prevent-overselling-on-shopify-across-channels.html) is working exactly as designed: it is refusing to sell stock the system has not been told you have. The sold-out badge is correct. The inventory number is correct. The only wrong thing in the whole system is a click that did not happen at the receiving door, and there is no field anywhere in Shopify that records a click that did not happen.

## In progress covers two completely different situations

A transfer has six statuses in the API. The [InventoryTransferStatus](https://shopify.dev/docs/api/admin-graphql/latest/enums/InventoryTransferStatus) enum lists DRAFT, "created but not yet finalized"; READY_TO_SHIP, "created, but not yet shipped"; IN_PROGRESS, "in progress, with a shipment currently underway or received"; TRANSFERRED, "completely received at the destination"; CANCELED; and OTHER, for a status outside the current set.

Look at the definition of IN_PROGRESS again. A shipment currently underway, *or received*. One status, two stories. A transfer that left the supplier this morning and a transfer that landed three weeks ago with fourteen units never counted are the same status, in the same list, with the same badge.

That is the whole reason this problem is invisible rather than merely annoying. Shopify's [receive inventory](https://help.shopify.com/en/manual/products/inventory/transfers/receive-inventory) page is clear about how a transfer gets stuck there: "If you only receive some items, then the transfer remains In progress until you receive the remaining items." After all items are received the status changes to Transferred. Until then it does not, and nothing in the admin counts the days.

Receiving also has a subtlety worth knowing before you build anything. Rejecting a line is recorded on the transfer but, in Shopify's words, "doesn't change inventory quantities at any location". A rejected unit is resolved without ever becoming stock. So a transfer can reach Transferred with nothing added to your shelves, and a transfer can sit at In progress with most of the stock already on them. Status alone tells you less than it looks like it does.

## Flow has two transfer triggers and both are good news

The [Shopify Flow triggers](https://help.shopify.com/en/manual/shopify-flow/reference/triggers) reference lists eighty-three triggers in a single section. Two of them touch transfers: Inventory transfer ready to ship, and Inventory transfer completed. There is nothing for purchase orders, nothing for receiving, nothing for incoming inventory.

Both of the triggers you do get fire on the happy path. Ready to ship fires at the start, completed fires at the end, and the failure mode we are talking about is the gap between them stretching out forever. You can build a workflow that congratulates you when a transfer finishes. You cannot build one that notices when a transfer does not.

This is a general property of trigger-based automation and worth naming, because it explains a whole family of Shopify problems. Event systems can only tell you about things that happen. Every operational failure that consists of a step being skipped is therefore invisible to them. Anything you want to catch by absence needs something that wakes up on its own and looks.

## You cannot subscribe to nothing happening

Developers reach for webhooks here and find out the same thing the hard way. The [inventory transfer event topics](https://shopify.dev/docs/api/events/latest/inventory-transfer) are field-shaped: there is a parent topic for the object, and then topics for destination, line items, line item total quantity, tags, metafields, and status. Status is the one that matters, and it "fires when the status field on the InventoryTransfer object changes".

A transfer that stalls does not change status. That is the definition of stalling. There is no topic for a transfer that has been In progress too long, because the platform has no idea what too long means in your business, and no topic can fire on an absence of change.

The history on this is messier than the docs suggest, which is worth knowing if you are tempted to lean on webhooks anyway. In May 2025 an app developer reported that [inventory webhooks were not firing during transfers](https://community.shopify.com/t/webhooks-not-triggering-on-inventory-transfers-request-for-resolution/414425) at all: stock levels moved in the admin, and `inventory_levels/update` and `inventory_items/update` produced nothing at his endpoint. A reply told him the new Transfers does send those webhooks as expected. On 13 June he came back to say the test still did not fire, and that Shopify Support had confirmed transfers do not trigger inventory webhooks and had logged a feature request.

In December 2025 another developer subscribed to `inventory_transfers/add_items`, `inventory_transfers/cancel` and `inventory_transfers/complete`, received only the cancel topic, and found that it [fired when the transfer was marked as received](https://community.shopify.dev/t/inventory-transfers-webhook-behavior-payloads-and-bugs/26946). He also asked where the payload documentation for these topics lives, since the topics appear in the Admin API docs and their payloads do not appear on the webhooks page. Seven months later he closed the thread himself as a misconfiguration at his end. The documentation question was never answered.

None of that means webhooks are useless on transfers. It means the thing you are building is a scheduled query that runs every morning, and the webhooks are a nice-to-have on top. Get the order of those two wrong and you will spend a week on plumbing that cannot physically detect your problem.

## The two numbers that actually answer the question

The [InventoryTransfer object](https://shopify.dev/docs/api/admin-graphql/latest/objects/InventoryTransfer) carries both halves of the arithmetic, and neither one appears as a column anywhere in the admin. `totalQuantity` is a non-null integer, "the total quantity of items being transferred". `receivedQuantity` is a non-null integer, "the total quantity of items accepted, rejected, or marked as canceled in the transfer".

Subtract one from the other and you have the number this whole article is about: units committed to a transfer that nobody has resolved. Sum it across every transfer that is not TRANSFERRED or CANCELED and you have the size of the hole, in units, for the first time.

Note the exact wording of receivedQuantity before you trust the subtraction. It counts accepted, rejected and canceled together. It is a count of lines that have been dealt with, not a count of stock that arrived. A transfer whose every line was rejected reads as fully received by this measure, which is correct for "has anyone looked at this" and wrong for "did we get the stock". If you want the second question, you have to walk the line items.

The other thing to notice is what the object does not carry. `dateCreated` is there, and it is the only clock. There is no expected arrival date on the object, and Shopify's [transfers](https://help.shopify.com/en/manual/products/inventory/transfers) page says nothing about expected arrival either. So the lead time has to come from you. A transfer between two of your own locations in the same city is late after two days. A container from overseas is not late at six weeks. One threshold for the whole store will either drown you in false alarms or stay quiet for a month, and both of those end the same way, with everybody ignoring the alert.

## Why your overdue list will be quietly shorter than the truth

Here is the trapdoor for anybody who builds this properly, and it is not documented anywhere a merchant would look.

The origin and destination on a transfer are not locations. They are `LocationSnapshot` objects: a copy of the name and address as they were, held deliberately so historical data survives a location being renamed or deleted later. Both are nullable, and so is the live Location inside each one.

In May 2026 a developer found [destination coming back nil](https://community.shopify.dev/t/inventory-transfer-complete-webhook-transfer-has-no-destination/34054) on transfers he had just been notified about, and later found origin nil on transfers whose status was TRANSFERRED, often enough that deleted locations seemed an unlikely explanation. Shopify staff answered on 25 May that the behavior is expected: since the 2026-01 API change, transfers can be created without an origin or a destination, so a nil destination is valid, while a nil destination.location means the live location is deleted or not accessible to the app. The nil origins on completed transfers were never explained, and the thread is still open.

The practical consequence is small and expensive. If your morning report groups unreceived transfers by destination location and your query joins through the live location, every transfer with a nil destination disappears from the report. It does not error. It does not warn. The list is simply shorter, and a list that is shorter than the truth is worse than no list, because you will believe it. Group by the snapshot name, keep an explicit bucket for the ones with no destination, and put the count of that bucket at the bottom of the mail where somebody will see it.

## The purchase order half of the same hole

If you buy stock rather than move it between your own shelves, you meet this problem from the other direction first, and we have written about that half on its own: [the reorder you always make too late](https://blog.dugong.live/how-to-stop-reordering-shopify-stock-you-already-have-on-order.html).

On 24 July 2026 a merchant posted that his custom reports, which use incoming quantities to work out what to buy, [were recommending stock that was already on order](https://community.shopify.com/t/purchase-order-incoming-inventory-not-working/654650). His sentence is the one everybody recognizes: his reports kept telling him to procure what was already in process.

The explanation came from another merchant on the same day, and it is the single most useful fact in that thread. Incoming is derived from inventory shipments, not from purchase orders. An open purchase order does not contribute to incoming, because, as he put it, there is literally nothing for Shopify to count. He also noted that the Admin GraphQL API had no PurchaseOrder object as of 2026-07, so you cannot join the two yourself either.

The workaround the thread landed on is to create the linked transfer when the purchase order is confirmed and mark it in transit straight away, even before anything ships, so that incoming appears and the reorder maths stops double-counting. It works. It also means your transfers list is now full of transfers that are in transit and are not in transit, which is exactly the noise that makes an overdue report useless.

Three days later the same merchant found the next edge: transfers do not update when the purchase order changes. In September 2026 another merchant [asked for that sync to be automatic](https://community.shopify.com/t/purchase-orders-and-transfers/682404), having added items to a purchase order by email after the fact and had to edit both records by hand, and noted that once a transfer is marked in transit there is no way back. A third merchant in that thread put the rule better than the documentation does: one record per arrival. If you take one line from this section, take that one.

## What this costs on an ordinary Tuesday

Take a two-location store that runs six transfers a week. Say one a week stalls part-received, which is conservative for anybody who has watched their own receiving door, and say it stalls with eighteen units outstanding at an average retail price of thirty-four dollars.

That is about six hundred dollars of stock dark for however long it takes somebody to notice. But the lost margin is the small half. The units that stall are the ones that moved enough to need transferring, so the sold-out badge lands on your best sellers rather than your slow ones. [Back-in-stock emails](https://blog.dugong.live/how-to-set-up-back-in-stock-notifications-on-shopify.html) do not fire, because the variant never came back in stock. The reorder report reads the gap as demand and tells you to buy more of something sitting in your own stockroom. And the customer who wanted it on Thursday bought it somewhere else on Thursday, which is the line item you will never see in any report.

Multiply by the number of locations, which is also the number of places an order can be [routed to and then not shipped from](https://blog.dugong.live/how-to-route-shopify-orders-to-the-right-warehouse.html), and by the number of weeks before anyone checks. The reason this one is worth automating is not the size of any single incident. It is that the clock keeps running and nothing in the system is holding a stopwatch.

## What the automation actually has to do

As a Dugong playbook, in plain prose:

```
# trigger
Scheduled daily sweep, plus
transfer ready to ship and
transfer completed

# steps
1. Write down a lead time
   for every route
2. Count unreceived units,
   not open transfers
3. Separate a transfer in transit
   from one that landed
4. Chase the person at the
   destination, not the buyer
5. Group by the snapshot and
   keep a null bucket
6. Close the partials, because
   the status will not
7. Send one list every morning,
   oldest money first
```

Step one is the step that decides whether anybody keeps the alert switched on. Lead time is per route, not per store: shelf to shelf in the same building is late tomorrow, a supplier two provinces away is late in a week, a container is late in a month. Write the number down next to each route once, in a sentence, and the false alarms stop.

Steps two and three are the measurement. Count unreceived units rather than open transfers, because one transfer with four hundred units outstanding and twelve transfers with one each are very different mornings, and a count of transfers makes them look the same. Then separate the two situations that share the In progress status by using the shipment dates rather than the transfer status, so a shipment that has not left yet is chased differently from one that has already landed. Those are two different phone calls to two different people.

Step four is the one that makes the automation welcome instead of resented. The person who can fix an unreceived transfer is standing at the destination with a box cutter, not sitting in an office approving purchase orders. Mail the destination. Name the transfer, the units outstanding and how long it has been open, and say what to click. A nudge that reaches somebody who cannot act is how alerts get filtered to a folder.

Steps five and six are the two things that will silently rot an otherwise good report. Group by the snapshot, keep the null bucket visible, and re-open the question on partials on a schedule, because the status field will keep saying In progress politely and forever. A transfer that has been eighty percent received for nine days is the most common shape of this failure and the least likely to be noticed, because it looks like progress.

Step seven is about whether a human acts. Sort by money and by age, put the oldest and largest at the top, and send one short list. A list of four transfers gets cleared before the first coffee. A list of sixty gets archived, and then the next one gets archived unread.

The honest limits. No automation can walk to the stockroom and count what is in the boxes, and you should be suspicious of anything that offers to auto-receive a transfer on a timer, because that writes stock you have not verified into the number your storefront sells against, which is a worse problem than the one you started with. A single-location store with no transfers does not need any of this. And if receiving is genuinely nobody's job, the alert will land in an empty inbox, so settle that first and automate second.

## Why this is a workflow and not a checklist

A checklist works when the work is rare and the person is the same person every time. Receiving is neither. It happens on the days the delivery happens to come, it is done by whoever is nearest to the door, and the moment it goes wrong is the moment somebody got interrupted, which is the exact moment a checklist is not being read.

And the gap has been open long enough to stop waiting on it. The webhook thread from May 2025 ends with a feature request logged. The payload documentation question from December 2025 was never answered. The nil destination thread from May 2026 is still open. The purchase order incoming thread from July 2026 has no staff reply and no accepted answer. The auto-sync request from September 2026 is a request. Two forums, four years, and the fix in every thread is a workaround somebody built themselves.

With Dugong you describe this one in a sentence. Every morning, list the transfers that are not finished, with the units outstanding and the days open, late by the lead time for that route, grouped by where they were going, and mail it to the person at that location. That is the specification. Everything after it is plumbing, and plumbing is what automation is for.

## Do this before you close the laptop

Three checks, ten minutes, no code.

Open your transfers list, filter to In progress, and sort by oldest. The date at the top of that sort is the answer to a question you have never asked, and most people are surprised by it.

Open the oldest one and compare the received count to the total. If it is a partial, you have just found the shape of your own version of this problem, and you can stop reading about the general case.

Then ask whoever is at your busiest destination location who is supposed to click Receive. If you get two different answers from two people, the automation is the second thing to fix.

> **◆ READING** Two companion pieces if this one landed: [the reorder you always make too late](https://blog.dugong.live/how-to-stop-reordering-shopify-stock-you-already-have-on-order.html), on the incoming stock your reorder point never reads, and [the stock Shopify counts and will not let you sell](https://blog.dugong.live/how-to-fix-shopify-committed-inventory-that-never-clears.html), on the other way units go missing from the number your storefront sells against.

If you sell on Shopify and have a version of this story, the pallet that sat unreceived for a month, the best seller that was sold out in your own stockroom, the reorder you made twice, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Why is my Shopify inventory not available after a transfer?

Because an unreceived transfer counts as incoming, and incoming is not available. Shopify's inventory states page defines incoming inventory as stock that's on its way to your location from inventory transfers or apps, and says plainly that it isn't available to sell until it has been received and its state has been changed to Available. The same page defines available inventory as inventory you can sell and adds that it doesn't include inventory that's considered incoming. On hand is defined as the total of your committed, unavailable and available inventory, which also leaves incoming out. So stock that is physically in your building but sitting on a transfer nobody finished receiving is outside every number your storefront sells against. Nothing is broken. Your oversell protection is doing exactly what it was built to do, which is refuse to sell units the system has not been told you have. The fix is to receive the transfer. The problem is that nothing in Shopify will tell you a transfer has been waiting to be received for three weeks.

Permalink: https://blog.dugong.live/how-to-catch-shopify-inventory-transfers-that-never-get-received.html#faq-1

### What does In progress mean on a Shopify transfer?

It means less than you would expect, and that is the heart of this problem. The Admin API enum defines IN_PROGRESS as a transfer in progress with a shipment currently underway or received. That single status therefore covers a transfer that left the supplier this morning and a transfer that arrived three weeks ago with fourteen units nobody counted. They sit in the same list with the same badge. Shopify's receive inventory page explains how a transfer gets stuck there: if you only receive some items, the transfer remains In progress until you receive the remaining items, and the status only changes to Transferred once everything has been received. There is also a wrinkle worth knowing before you build on the status. Rejecting a line is recorded on the transfer but does not change inventory quantities at any location, so a transfer can reach Transferred without a single unit reaching your shelves. If you need to know what actually arrived rather than what has been dealt with, you have to read the line items.

Permalink: https://blog.dugong.live/how-to-catch-shopify-inventory-transfers-that-never-get-received.html#faq-2

### Does Shopify Flow have a trigger for a transfer that was never received?

No. The Shopify Flow triggers reference lists eighty-three triggers, and two of them concern transfers: Inventory transfer ready to ship, and Inventory transfer completed. There is no trigger for purchase orders, for receiving, or for incoming inventory. Both of the transfer triggers you do get fire on the happy path, one at the beginning and one at the end, and the failure you are trying to catch is the gap between them never closing. This is a property of event-driven automation rather than a gap in Flow specifically. A trigger can only fire on something that happens, so any operational failure that consists of a step being skipped is invisible to triggers by construction. You can still use the two triggers you have, as the open and close of a clock: record the moment a transfer becomes ready to ship, clear that record when it completes, and have something else look at what is left over. The looking is the part Flow cannot do for you.

Permalink: https://blog.dugong.live/how-to-catch-shopify-inventory-transfers-that-never-get-received.html#faq-3

### Can you get a webhook when a Shopify transfer is overdue?

No, and it is worth understanding why rather than searching for the right topic name. The inventory transfer event topics are field-shaped: a parent topic for the object, plus topics for destination, line items, line item total quantity, tags, metafields and status. The relevant one fires when the status field on the transfer changes. A transfer that has stalled has not changed status, which is precisely what stalling means, so no topic can fire. There is also no platform concept of overdue, because Shopify does not know your lead times. The practical history is a little rough too. In May 2025 an app developer reported that inventory level and inventory item webhooks were not firing during transfers at all, and came back in June to say that Shopify Support had confirmed transfers do not trigger inventory webhooks and had logged a feature request. In December 2025 another developer subscribed to the add items, cancel and complete transfer topics, received only cancel, and saw it fire when the transfer was marked as received. Build the scheduled query first. Treat webhooks as an optimization.

Permalink: https://blog.dugong.live/how-to-catch-shopify-inventory-transfers-that-never-get-received.html#faq-4

### Why doesn't my Shopify purchase order show as incoming inventory?

Because incoming is derived from inventory shipments, not from purchase orders. This came up on the Shopify community in July 2026, when a merchant found that his reorder reports were recommending stock that was already on order, and said his reports kept telling him to procure what was already in process. Another merchant gave the answer in the same thread: incoming is not derived from the purchase order at all, so there is literally nothing for Shopify to count. He also noted that the Admin GraphQL API had no PurchaseOrder object as of version 2026-07, which means you cannot join the two sides yourself either. The workaround the thread settled on is to create the linked transfer as soon as the purchase order is confirmed and mark it in transit immediately, before anything ships, so that incoming appears and the reorder maths stops double-counting. That works, with two costs. Your transfers list now contains transfers that are in transit and are not in transit, which makes an overdue report noisy. And transfers do not update when the purchase order changes, so adding a line to the order leaves the transfer wrong until somebody edits it by hand. One record per arrival is the rule that keeps this tidy.

Permalink: https://blog.dugong.live/how-to-catch-shopify-inventory-transfers-that-never-get-received.html#faq-5

### Can AI monitor Shopify inventory transfers and chase the unreceived ones?

Yes, and this is a particularly good fit for automation, because every judgment involved is arithmetic rather than opinion. An automation like Dugong starts from a lead time per route, which you write down once, because shelf to shelf in the same building is late tomorrow and a container is not late at six weeks. It then counts unreceived units rather than open transfers, by subtracting received quantity from total quantity on each transfer, since one transfer holding four hundred units and twelve holding one each are very different mornings. It separates a shipment that has not left from one that has already landed, because those are two different phone calls. It groups by the location snapshot rather than the live location and keeps a visible bucket for transfers with no destination, since Shopify allows transfers without one and a join through the live location silently drops them. It re-opens partials on a schedule, because the status field will keep saying In progress politely and forever. And it mails one short list each morning to the person at the destination, oldest and largest first, because a list of four gets cleared and a list of sixty gets archived. The limits are honest ones. Nothing can count the boxes for you, auto-receiving on a timer writes unverified stock into the number your storefront sells against and is worse than the original problem, and if receiving is nobody's job in particular then the alert lands in an empty inbox.

Permalink: https://blog.dugong.live/how-to-catch-shopify-inventory-transfers-that-never-get-received.html#faq-6

---

## Read next

- [The reorder you always make too late](https://blog.dugong.live/how-to-stop-reordering-shopify-stock-you-already-have-on-order.html): Incoming reads zero while the pallet sits at the supplier, so the report tells you to buy it again. The AI playbook that tracks every open Shopify purchase order.
- [The stock Shopify will not let you sell](https://blog.dugong.live/how-to-fix-shopify-committed-inventory-that-never-clears.html): Committed is read-only and Shopify will not tell you which orders hold it. The AI playbook that finds the stuck orders and gets your shelf selling again.
- [The overselling problem no one automates](https://blog.dugong.live/how-to-prevent-overselling-on-shopify-across-channels.html): Selling stock you no longer have is the Shopify pain point merchants dread most, because it is the hardest to take back. The AI playbook that keeps inventory honest in real time.
