# How to set up pre-orders on Shopify without holding in-stock items

> Shopify has no real pre-order, ship date, or cart split, so an in-stock item gets held by a pre-order. The AI playbook that ships what is ready now.

- Canonical: https://blog.dugong.live/how-to-set-up-pre-orders-on-shopify-without-holding-in-stock-items.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-06-30
- Updated: 2026-10-27
- Section: Research
- Word count: 2770
- Dispatch: Nº 72 · Research · 9 min read
- Full headline on page: How to set up *pre-orders* on Shopify without holding in-stock items
- Keywords: Shopify preorder, Shopify pre-order app, Shopify mixed cart preorder, preorder and in-stock items together, Shopify split order preorder, Shopify partial fulfillment preorder, Shopify continue selling when out of stock, Shopify backorder, Shopify oversold preorder, tag preorder orders, Shopify preorder ship date
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

A pre-order is supposed to be the good problem. Demand showed up before the stock did, the customer paid you anyway, and you get to fund the next run with money already in the bank. Then the order lands in your admin and the good problem turns into a quiet mess. The customer bought one item you have and one you do not, in the same cart, and Shopify hands you a single order with two delivery dates trapped inside it. Ship it whole and the thing on your shelf waits weeks for the thing in the factory. Split it and you are doing surgery by hand, one order at a time, while more of them arrive. The sale was easy. Everything after the sale is the part nobody warned you about.

This is one of the most common complaints from merchants who run any kind of pre-order or backorder, and it always sounds the same. Someone sells a pre-order item, watches in-stock items get held hostage behind it, and asks the obvious question: how do I ship the part that is ready and keep the rest open without managing every order by hand. The replies point at a checkbox that lets you oversell, a manual partial fulfillment buried in the order screen, and a shelf of paid apps whose whole job is the pre-order Shopify will not run for you. The merchant is not asking for anything strange. They want the obvious thing: take an order with a now item and a later item, send the now item now, and look after the later one until it can go. The platform that took the money leaves that to a person.

> Shopify will happily sell you a pre-order. It just *will not run* the weeks between the sale and the shipment.

## The short answer

Shopify has no real pre-order, only a continue selling when out of stock checkbox on each variant. It shows the same Add to Cart button as everything else, carries no expected ship date, collects no deposit against a later balance, and tags neither the order nor the line item, so the sale lands in your admin looking like any in-stock sale.

Nothing separates a mixed cart either. An in-stock item and a pre-order item check out as one order with two timelines inside it, and the default outcome is the worst one available: the whole order waits on the slowest line in it. Partial fulfillment is the correct handling and exists only as a manual step taken one order at a time.

Flow can tag an order holding an out-of-stock item and stops there. It has no action that ships the ready lines, charges a held balance later, fulfills the pre-order line the day stock lands, or switches the toggle back off once the run is committed. Forgetting that last one is how a controlled pre-order decays into *plain overselling*.

## Why one cart with two delivery dates breaks Shopify

The thing that makes a pre-order hard is not the selling, it is the timeline. A normal order has one moment that matters: it ships, it is done. A pre-order has a stretch of time between purchase and delivery where something has to be managed, and a mixed cart has two of those timelines running at once inside a single order. The in-stock line wants to ship today. The pre-order line cannot ship for weeks. Shopify models an order as one thing with one status, so the two timelines collide, and the default outcome is the worst one: the whole order waits on the slowest line in it.

The customer feels this immediately. They bought a hoodie they expected in two days and a jacket they knew was coming later, and now the hoodie is late too, with no explanation, because it is riding along behind the jacket. To them it does not look like a pre-order working as intended. It looks like their whole order is stuck. That is the moment the support ticket gets written, and it is the moment a perfectly profitable pre-order starts costing you trust and time you did not budget for.

## What Shopify actually gives you, and where it stops

Shopify is happy to take a pre-order. It just will not manage one. The gap shows up in three places merchants hit fast.

First, **there is no real pre-order, only a toggle that oversells**. The single native lever is a checkbox on each variant called continue selling when out of stock. Tick it and a shopper can keep buying after stock hits zero. That is the whole feature. It shows the same Add to Cart button as everything else, so the customer is never told the item ships later. It carries no expected ship date. It does not collect a deposit and charge the balance later. And it does not tag the order or the line item as a pre-order, so the sale lands in your admin looking exactly like an in-stock order, with nothing on it to say part of this cannot ship yet. You have permission to sell air. You have no tooling to manage the promise you just made.

Second, **nothing splits a mixed cart for you**. When a customer checks out with an in-stock item and a pre-order item together, Shopify keeps them in one order and does nothing to separate them by availability. The correct handling is a partial fulfillment: ship the in-stock line now and leave the pre-order line open until it can go. Shopify can do partial fulfillment, but only as a manual step you take order by order, clicking into the order, choosing the lines that are ready, and shipping just those. Nothing flags which orders need it, nothing tells the customer the order is arriving in two parts, and nothing holds the open line and remembers to come back to it when the stock lands. The capability exists. The judgment and the follow through are yours.

Third, **Flow cannot run the lifecycle**. [Shopify Flow](https://help.shopify.com/en/manual/shopify-flow), free on every plan, can react when an order is created, tag it, and send a notification, so you can use it to mark an order that contains an out-of-stock item. That is the easy slice. Flow has no action that splits the cart and fulfills only the in-stock lines, charges a held pre-order balance later, watches incoming inventory and fulfills the pre-order line the moment it arrives, emails the customer a real ship date, or turns the continue selling toggle back off when the run sells out. It can tell you a pre-order came in. It cannot carry that pre-order from purchase to delivery, which is the entire job. This is the same wall we hit in [the order tag you set by hand](https://blog.dugong.live/how-to-automatically-tag-orders-on-shopify.html): Flow can label the order, but labeling is the start of the work, not the work.

> **◆ DATA** The tell that this is a real gap is the size of the shelf built to fill it. The Shopify App Store carries a whole category of pre-order apps, each one adding the things the platform left out: a Pre-order button instead of Add to Cart, an expected ship date on the product page, a partial charge now and the rest later, an automatic tag on the order, and a back in stock handoff. Merchants pay monthly for them precisely because the native toggle stops at permission to oversell. When an app category exists only to turn one platform's checkbox into an actual pre-order, the platform has told you where its automation ends.

## Why the usual fixes don't hold

Once pre-orders start to hurt, merchants reach for one of a few workarounds. Each one helps and each one breaks in a predictable spot.

**"I will just tick continue selling."** This is the native path, and it sells the pre-order, but it sells it silently. The customer gets a normal Add to Cart, no ship date, and an order confirmation that looks like any other, so they expect their parcel in days and are surprised when it does not come. Worse is the other end of the run. When the stock finally arrives, the toggle is still on, so the store keeps selling past the units you have, and the orders keep coming in untagged with the customer unaware anything is a pre-order. Forgetting to switch it back off is how a controlled pre-order turns into plain overselling, which is its own pain we covered in [the overselling problem no one automates](https://blog.dugong.live/how-to-prevent-overselling-on-shopify-across-channels.html).

**"I will list the pre-order as a separate product."** Some merchants dodge the mixed cart by making a distinct pre-order listing so it is obviously different. It helps the customer understand, and then it splinters everything else. Now you have two listings for one product, your inventory and reporting are split across them, the reviews and the search ranking are divided, and when stock lands you have to merge demand back into the real product and retire the placeholder. You traded a confusing cart for a messy catalog, and the work just moved upstream.

**"I will ship everything together."** The simplest rule, hold the whole order until the pre-order item is ready, is exactly the held hostage problem stated as a policy. The in-stock item the customer could have had this week sits in your stockroom for a month, your storage fills with picked but unshipped orders, and every customer who bought one ready item and one later item is now waiting on both. It is tidy for you and slow for everyone who paid you.

**"I will partially fulfill each one by hand."** This is the honest answer and the one that does not scale. For every mixed order you open it, pick out the lines that are ready, ship those, leave the rest open, and then remember, weeks later, to come back when stock arrives and fulfill the remainder. One or two a week is fine. A launch that takes three hundred pre-orders turns into a spreadsheet of who is waiting on what, and the open lines that fall through the cracks become the angry emails asking where the rest of the order is. It is the same race against the warehouse we wrote about in [the order change that races your warehouse](https://blog.dugong.live/how-to-edit-a-shopify-order-after-its-been-placed.html), just stretched across weeks.

## What the automation actually has to do

The real job is not "let people buy out of stock." It is "when an order contains a pre-order line, label it, ship the in-stock lines now, hold the pre-order line with its promised date, keep the customer informed, fulfill the held line the moment stock lands, stop selling when the run is gone, and bring a human anything strange." That is labeling, splitting, communicating, and timing, run across every order for weeks at a time. As a Dugong playbook, in plain prose, it reads like this:

```
# trigger
On an order with a pre-order or backorder line,
   or an item bought past zero stock

# steps
1. Label the order and the specific line items
   as pre-order, with the promised ship window
2. Split the order: fulfill the in-stock lines
   now, hold the pre-order lines open
3. Tell the customer what ships now and what
   ships later, with a real date
4. Watch incoming stock and fulfill each held
   line the day it lands, oldest order first
5. Update the customer if the date slips, and
   confirm when the held part ships
6. Stop selling once the run is fully committed,
   so it does not keep overselling
7. Hold oversells beyond the run, mixed refunds,
   and bad date slips for review
```

Seven lines. The compiler fills in everything underneath: reading the order and spotting which lines are pre-order, partially fulfilling the ready lines and keeping the rest open, sending a confirmation that sets the right expectation instead of a generic one, watching the inbound purchase order or the inventory feed and firing the held shipment the day stock arrives, working oldest order first so the earliest buyer is served first, and flipping selling off when the committed units run out. The merchant never sat with a spreadsheet of three hundred open pre-order lines trying to remember who was still waiting. They described how a careful fulfillment lead would run a pre-order, and let the compiler do the volume and the calendar.

> **◆ NOTE** The pre-order that does damage is the one that goes quiet. A customer who bought a now item and a later item and hears **nothing** assumes the whole order is broken, and a pre-order with no ship date feels like a charge with no product. A run left selling after the units are gone oversells real stock and turns buyers into a refund queue. The job is not "let the sale through," it is "make and keep a promise: this part ships now, that part ships on this date, and if either changes you hear from us first." Automation that can take the order but cannot keep the promise should not be running your pre-orders.

## Why this is a compiler problem, not an app problem

There are capable pre-order apps, and for a store with a steady pattern and one product launching at a time they are a reasonable answer, which again proves the native gap is real. But the thing that makes a pre-order safe to automate is not adding a Pre-order button, it is the judgment around the weeks that follow: knowing which lines in a mixed cart can ship now, deciding whether to hold the whole order or split it, setting an expectation the customer will accept, working the queue oldest first when a partial restock lands, and knowing when to stop selling and when to pull a human in because an order oversold past the run or a date slipped badly. Those are decisions about a particular order on a particular day, and the right answer shifts with every restock and every delay, which means a fixed rule was never going to hold.

A natural-language compiler fits because a pre-order was never really a checkout problem. It is a *promise kept over time* wearing a button's clothes. Taking the money is the easy part, which is why the toggle does it. The hard part is everything after: split what is ready from what is not, tell the customer the truth about both, hold the open line for weeks without forgetting it, ship it the day stock lands, and stop the run before it oversells. You can write that brief in a paragraph. You could never hold it across hundreds of orders and a calendar of restocks by hand. It sits in the same family as [the restock alert that never fires](https://blog.dugong.live/how-to-set-up-back-in-stock-notifications-on-shopify.html), where demand is waiting on inventory you have not connected to it, and [the unpaid order that never cancels itself](https://blog.dugong.live/how-to-automatically-cancel-unpaid-orders-on-shopify.html), where an order sits in limbo holding stock until someone deals with it.

## The workflow worth building this week

If your pre-orders hold in-stock items hostage, if a launch means an evening of partial fulfillments and a spreadsheet of who is still waiting, or if you have ever left continue selling on too long and oversold the run, this is the automation to set up before the next drop, because every pre-order you babysit by hand is time you will not get back and one forgotten open line away from a where-is-my-order ticket you could have prevented. It pairs naturally with the inventory work we have written about, like [the overselling problem no one automates](https://blog.dugong.live/how-to-prevent-overselling-on-shopify-across-channels.html) and [the reorder you always make too late](https://blog.dugong.live/how-to-set-inventory-reorder-points-on-shopify.html), and it feeds the same flywheel as [the Shopify automations no one builds](https://blog.dugong.live/best-shopify-automations-to-set-up.html), where the work that compounds is the part merchants never get to.

Describe it the way you would brief a careful fulfillment lead: when an order has a pre-order line, ship what is in stock now, hold the rest with a real ship date, keep the customer in the loop, fulfill the held part the day stock lands, stop selling when the run is gone, and bring me anything that oversold or slipped. That is the whole brief. The compiler does the labeling, the splitting, the messaging, and the timing. You keep your evenings, and you stop being the slowest step between a sale you already made and a parcel the customer is waiting on.

> **◆ READING** If this resonates, two companion pieces: our dispatch on [the overselling problem no one automates](https://blog.dugong.live/how-to-prevent-overselling-on-shopify-across-channels.html), where a run left selling too long sells stock you do not have, and the field study on [the Shopify automations no one builds](https://blog.dugong.live/best-shopify-automations-to-set-up.html), where the work that actually compounds is a sliver of what merchants wire up.

If you are a Shopify merchant who has wired up pre-orders that ship the ready part now and fulfill the rest the day stock lands, or you have a story about the launch where a hundred open pre-order lines went sideways, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Does Shopify support pre-orders without an app?

Not really. The only native lever is the Continue selling when out of stock checkbox on a variant, which lets a shopper buy an item once its stock hits zero. But it shows the same Add to Cart button as anything else, so the customer is never told the item is a pre-order, it carries no expected ship date, and it does not tag the order or the line item as a pre-order, so the order lands in your admin looking like a normal in-stock sale. There is no native Pre-order button, no badge, no deposit-now-charge-later, and no way to set a delivery window, which is why the Shopify App Store has a whole shelf of pre-order apps. If you want a customer to knowingly buy something that ships later, the native toggle is not it.

Permalink: https://blog.dugong.live/how-to-set-up-pre-orders-on-shopify-without-holding-in-stock-items.html#faq-1

### What happens to a mixed cart with in-stock and pre-order items on Shopify?

Shopify lets a customer put an in-stock item and a pre-order item in the same cart and check out as a single order, and it does nothing to separate them. There is no automatic split by availability, so the order arrives whole, and if you ship it as one parcel the in-stock item waits weeks for the pre-order item to arrive. The correct handling is partial fulfillment: ship the in-stock line now and leave the pre-order line open until stock lands. But that is a manual step you take order by order in the admin, and nothing in Shopify reminds you to do it, tells the customer the order is shipping in two parts, or holds the pre-order line for the day it can finally go out.

Permalink: https://blog.dugong.live/how-to-set-up-pre-orders-on-shopify-without-holding-in-stock-items.html#faq-2

### Can Shopify Flow manage pre-orders?

No. Shopify Flow can react when an order is created, tag it, and send a notification, so you can use it to mark an order that contains an out-of-stock item. But Flow has no action that splits a mixed cart and fulfills only the in-stock lines, charges a held pre-order later, watches incoming inventory and fulfills the pre-order the moment it lands, emails the customer a real ship date, or turns the continue selling toggle back off when the run sells out so the store stops overselling. It can tell you a pre-order came in. It cannot run the pre-order from purchase to delivery, which is the part that actually takes the work.

Permalink: https://blog.dugong.live/how-to-set-up-pre-orders-on-shopify-without-holding-in-stock-items.html#faq-3

### How do I ship the in-stock items now and the pre-order items later on Shopify?

The mechanism is partial fulfillment, and it exists, but only as a manual step taken order by order: open the order, select the lines that are ready, ship just those, and leave the pre-order lines open. Shopify does not flag which orders need the split, does not tell the customer the order is arriving in two parts, and does not remember to come back to the open line when stock lands, so at launch volume the manual path becomes a spreadsheet of who is still waiting on what. The automated version runs the same motion continuously: label the pre-order lines with their promised window, fulfill the ready lines immediately, tell the customer what ships now and what ships later with a real date, then watch incoming stock and fulfill the held lines the day it arrives, oldest order first, updating anyone whose date slips.

Permalink: https://blog.dugong.live/how-to-set-up-pre-orders-on-shopify-without-holding-in-stock-items.html#faq-4

### Is the continue selling when out of stock setting safe to use for pre-orders?

It is the only native lever, and it is a blunt one: permission to oversell with no tooling for the promise you just made. The shopper sees a normal Add to Cart button with no hint the item ships later, no expected ship date, and no deposit now with the balance later, and the order lands in the admin untagged, indistinguishable from an in-stock sale. The riskier end is the close of the run. The toggle does not turn itself off when stock arrives or when the incoming run is fully committed, so a store that forgets it keeps selling past the units it will actually receive, still silently, still untagged. That is how a controlled pre-order decays into plain overselling. If the toggle is doing the selling, something else has to do the labeling, the customer messaging, the split fulfillment, and the shutoff, because the checkbox does none of it.

Permalink: https://blog.dugong.live/how-to-set-up-pre-orders-on-shopify-without-holding-in-stock-items.html#faq-5

---

Markdown rendition of https://blog.dugong.live/how-to-set-up-pre-orders-on-shopify-without-holding-in-stock-items.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
