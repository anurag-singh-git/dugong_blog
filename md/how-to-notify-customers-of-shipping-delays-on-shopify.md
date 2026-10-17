# How to notify customers of shipping delays on Shopify automatically

> Shopify emails your customer when the order ships, never when it stalls, and Flow only alerts your staff. The AI playbook that sends the delay email itself.

- Canonical: https://blog.dugong.live/how-to-notify-customers-of-shipping-delays-on-shopify.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-07-22
- Updated: 2026-08-12
- Section: Research
- Word count: 2130
- Dispatch: Nº 88 · Research · 10 min read
- Full headline on page: How to notify customers of *shipping delays* on Shopify automatically
- Keywords: Shopify notify customers of shipping delay, Shopify shipping delay email, Shopify delayed order notification, Shopify bulk email unfulfilled orders, Shopify Flow email customer unfulfilled order, Shopify order delay email, Shopify fulfillment delay notification, Shopify email customers with open orders
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

Every store has a version of this order. Placed on a Tuesday against a promise of two to four business days. The supplier's batch arrived short, or the carrier missed a pickup, or the one person who packs boxes got the flu, and now it is day seven and the order is still sitting in the unfulfilled column. The customer has heard from you once, at checkout, when everything was still fine. The next email Shopify knows how to send them is the shipping confirmation, and that email cannot exist until the thing that is not happening happens. So the exact stretch of time when your customer most needs to hear from you is the stretch when your store is structurally incapable of speaking.

The forum threads on this have been accumulating for years, and they all ask for the same small mercy in different words. "How to notify customers that shipping will be late." "I need to send a custom message to customers about a shipping delay." "How can I notify customers about shipping delays during vacation?" And the one that gets all the way to engineering terms: a Flow that automatically emails the customer when an order is still unfulfilled after seven days. Nobody is asking for anything clever. They want to say we are late, here is why, here is the new date, before the customer has to ask. The platform does not have a way to say it.

## What Shopify actually does, and where it stops

Give the platform its due first, because what it does, it does reliably. Shopify's transactional emails fire at their two moments without fail: the order confirmation the second the order is placed, and the shipping confirmation the second a fulfillment is created with a tracking number. You can edit both templates, brand them, soften the language. Between those two moments, though, there is nothing. No delay notice template anywhere in the notifications settings. No trigger that fires when an order ages past the promise it was sold with. As far as the platform is concerned, an order that shipped in two days and an order that shipped in nineteen had the same conversation with the customer.

The first wall is the missing bulk path. The Orders page will happily filter to open, unfulfilled orders, and a merchant closing for a two-week holiday or staring at a supplier failure naturally reaches for that filter expecting an email button behind it. There is none. The native options are opening each order and contacting its customer one at a time, or exporting the filtered list to a CSV and mailing it through some external platform, which the community threads recommend to each other precisely because there is nothing better. Both are workarounds you do once during a crisis, and neither is a process anyone runs every week.

The second wall is crueler because it gets so close. [Shopify Flow](https://help.shopify.com/en/manual/shopify-flow), the platform's own automation tool, can genuinely find your late orders: a scheduled trigger can sweep daily for paid orders still unfulfilled after seven days, and a Wait action can hold a workflow for up to thirty days watching a single order age. And then, with the guilty orders identified, Flow's one native email action is called Send internal email. It writes to your staff. There is no action that sends a customer-facing email, so the automation tool can assemble a perfect daily list of every promise your store is breaking and has no way to tell the one person each promise was made to. Marketing tools cannot close the gap either: Shopify Email campaigns reach only the customers who opted into marketing, and a delay notice is not marketing, it is transactional. The guest buyer who never ticked the consent box is exactly the person refreshing their inbox.

> Shopify will tell your customer the moment their order ships. It has no way to tell them it hasn't.

What the silence costs arrives on a schedule. Around day five, the polite where-is-my-order ticket, the genre that already eats [a fifth of a store's support queue](https://blog.dugong.live/how-to-reduce-where-is-my-order-wismo-tickets-on-shopify.html) in a normal week and over half during a sale. Around day ten, the cancellation request, timed with exquisite cruelty for the moment the box is finally about to ship. After that, the item-not-received chargeback, [the dispute you lose by default](https://blog.dugong.live/how-to-win-chargeback-disputes-on-shopify.html) if nobody assembles the evidence, filed by a customer who would have waited happily had anyone told them why. And trailing the whole mess, the one-star review that never mentions the product, because the product was fine. It names the silence. Customers forgive late. What they do not forgive is finding out they were forgotten.

## Why doing it by hand never keeps up

The by-hand version starts noble and dies of arithmetic. Scan the Orders page each morning, open everything older than the promise, work out what actually happened to each one, and write a sensible email per order through the contact option on the order page. Twenty minutes for a handful. But delays do not arrive in handfuls, they arrive in clumps, and always at the worst time: the week of the sale, the season the supplier slipped, the days you are shorthanded. The cause of the backlog and the cause of the silence are the same thing, which is that everyone is busy, so the emails that most need sending are the ones nobody has time to send.

The blast version is faster and worse. Export the filter, send one apology to everyone with an open order, and you have just told the customer whose order ships this afternoon that it is delayed, told the customer nineteen days deep the same soothing nothing as the customer two days in, and promised no specific date to anyone, because one template cannot hold four hundred different truths. A delay email that does not know why the order is late, or when it will ship now, is barely better than the silence. Sometimes it is worse, because it spends the store's credibility on saying nothing.

## What the automation actually has to do

The real job is not one email. It is a watch, a diagnosis, an honest sentence, and a follow-through, per order, forever: know what every open order was promised, notice the ones that slip before the customer does, work out what actually went wrong and for how many orders, tell each affected customer the specific truth with a new date, and keep the new promise or write again. As a Dugong playbook, in plain prose, it reads like this:

```
# trigger
On a daily sweep of every open order, and whenever
   a fulfillment stalls, a supplier goes quiet, or a
   line item runs out of stock

# steps
1. Watch each order against its real promise: the
   shipping profile's ship time, the preorder date,
   the supplier lead time
2. Catch the slip early: unfulfilled past the
   promise, a label with no carrier scan, a batch
   that stopped moving
3. Diagnose cause and scope: one stuck order, one
   supplier's queue, or the whole store on pause
4. Write the delay email per order: what happened,
   the new honest date, and options when the wait
   is long
5. Tag the order, brief support, and email again
   with the truth if the new date slips too
6. Escalate the VIPs, the high values, the second
   slips, and anyone already angry
```

Six lines. The compiler fills in the rest: reading the promise off the shipping profile instead of a hard-coded seven days, so the express orders get flagged on day three and the made-to-order pieces are left in peace until their real date; writing each email from the order itself, this product, this cause, this new date; offering options when the delay is long enough to deserve them, keep waiting, swap for the in-stock color, or take the refund now; tagging the order so [everything downstream routes correctly](https://blog.dugong.live/how-to-automatically-tag-orders-on-shopify.html) and support sees the context before the ticket arrives; and watching the new date like it watched the first one, because a second silence after a first apology reads as contempt.

> **◆ NOTE** The trap is **the generic blast**. One soothing template sent to everyone with an open order teaches customers that your emails carry no information, and the second broken promise costs more trust than the first. A delay email only works when it is specific: this order, this cause, this new date. If the honest new date is unknown, say that, and say when you will know. Specificity is the apology.

## Why this is a compiler problem, not an app problem

There are notification apps, and a store drowning in where-is-my-order tickets should look at them. But the hard part of a delay notice is not the sending, it is the judgment stacked underneath it: is this order actually late, or does its shipping profile say Friday; is this a one-order problem or the leading edge of a supplier failure that will swallow four hundred orders by Thursday; what date can we honestly promise now; is this delay long enough that the email should offer a swap or a refund instead of only patience; and which of these customers, the VIP, the one on their second slip, the one already in the support queue, should hear from a human instead of a template. Those answers change per order and per week, which is what a fixed rule handles badly and a person cannot keep up with at volume.

It also sits in the middle of a web this desk keeps mapping. Upstream, the delays are born in [the order you split across vendors by hand](https://blog.dugong.live/how-to-automatically-split-and-route-shopify-orders-to-multiple-suppliers.html), where one quiet supplier stalls a whole batch, and in [the tracking number you paste by hand](https://blog.dugong.live/how-to-automatically-add-tracking-numbers-to-shopify-orders.html), where fulfillment lags because the numbers do. Sideways, [the preorder that holds your order hostage](https://blog.dugong.live/how-to-set-up-pre-orders-on-shopify-without-holding-in-stock-items.html) is a shipping delay you sold on purpose and still have to narrate. Downstream, every delay email you send before the customer writes in is one fewer of [the WISMO tickets that eat your afternoon](https://blog.dugong.live/how-to-reduce-where-is-my-order-wismo-tickets-on-shopify.html) and one fewer dispute for [the chargeback desk](https://blog.dugong.live/how-to-win-chargeback-disputes-on-shopify.html) to fight.

Picture an apparel store in a container-delay summer. The supplier's shipment misses the boat, and four hundred open orders quietly go from on time to ten days late. The sweep catches the slip the morning the batch stops moving, sorts the four hundred into next-batch, swappable, and truly stuck, and sends each customer their own version of the truth, with a swap offer on the sixty orders where the other colorway is on the shelf. Support's week stays ordinary. The chargebacks never materialize. And thirty-one customers take the swap, which is thirty-one boxes that ship the same day from stock the store already owned.

## The workflow worth building this week

If you dropship, print on demand, run preorders, depend on one supplier, or ever take a vacation, which is every merchant eventually, this gap is already costing you money labeled as something else: support hours spent answering questions an email should have preempted, chargebacks filed by customers who only wanted a date, refunds issued to buyers who would have waited. It pairs naturally with [the WISMO tickets that eat your afternoon](https://blog.dugong.live/how-to-reduce-where-is-my-order-wismo-tickets-on-shopify.html), which handles the customers who ask, while this playbook reaches the ones who have not asked yet, and with [the tracking number you paste by hand](https://blog.dugong.live/how-to-automatically-add-tracking-numbers-to-shopify-orders.html), which shortens the silence from the other end. It feeds the same flywheel as [the Shopify automations no one builds](https://blog.dugong.live/best-shopify-automations-to-set-up.html), where the compounding work is the communication nobody has time for.

Describe it the way you would brief a careful assistant: watch every open order against what we promised, tell me the moment a batch goes quiet, email each affected customer the real reason and an honest new date, offer a swap or a refund when the wait gets long, keep the new promise or write again, and bring me the VIPs and the second slips yourself. That is the whole brief. The compiler does the watching, the diagnosing, the writing, and the following up. Your customers stop discovering their order is late by asking, because the store that owes them a box is also the first to say so.

> **◆ READING** If this resonates, two companion pieces: our dispatch on [the WISMO tickets that eat your afternoon](https://blog.dugong.live/how-to-reduce-where-is-my-order-wismo-tickets-on-shopify.html), which handles the questions this playbook prevents, and [the tracking number you paste by hand](https://blog.dugong.live/how-to-automatically-add-tracking-numbers-to-shopify-orders.html), where the fulfillment lag that causes half these silences gets fixed at the source.

If you are a Shopify merchant who has lived through a supplier failure with a full order book, or you have a delay email that actually worked, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### How do I notify customers of a shipping delay on Shopify?

There is no native delay notification. Shopify sends the order confirmation at checkout and the shipping confirmation when a fulfillment is created, and nothing in between, so the manual path is opening each late order and contacting the customer one at a time, or exporting the orders to a CSV and mailing them through an external platform. Neither scales during the exact moments delays happen, which is why merchants automate the whole loop: watch every open order against its promised ship time, catch the ones that slip, and send a specific, honest delay email per order with a new date, before the customer writes in to ask.

Permalink: https://blog.dugong.live/how-to-notify-customers-of-shipping-delays-on-shopify.html#faq-1

### Can Shopify Flow email customers about a delayed order automatically?

No. Flow can find the late orders: a scheduled trigger can query paid orders that are still unfulfilled after seven days, and the Wait action can hold a workflow for up to thirty days. But Flow's only native email action is Send internal email, which writes to your own staff, not to the customer. So the platform's automation tool can build a perfect daily list of every order you are late on and has no way to tell the one person who cares. Closing that last step, the customer-facing email itself, requires either an app or an automation layer that can send transactional email on the order's behalf.

Permalink: https://blog.dugong.live/how-to-notify-customers-of-shipping-delays-on-shopify.html#faq-2

### Can I bulk email all customers with open orders on Shopify?

Not natively. The Orders page will filter to open, unfulfilled orders, but there is no email button behind the filter, so a store closing for a holiday or hit by a supplier failure cannot message everyone still waiting in one action. Shopify Email does not solve it either, because campaigns only reach customers who opted into marketing, and a delay notice is transactional: the guest buyer who never ticked the marketing box is exactly the person anxiously waiting. The workaround is exporting the filtered orders to CSV and sending through an external email tool, which works once and is nobody's process for every week.

Permalink: https://blog.dugong.live/how-to-notify-customers-of-shipping-delays-on-shopify.html#faq-3

### What happens if I don't tell customers about a shipping delay?

The costs arrive on a schedule. Around day five comes the polite where-is-my-order ticket, the genre that already eats a fifth of a store's support queue in a normal week and over half of it during a sale. Around day ten comes the cancellation request, timed with exquisite cruelty for the moment the box is finally about to ship. After that comes the item-not-received chargeback, a dispute you lose by default if nobody assembles the evidence, filed by a customer who would have waited happily had anyone told them why. And trailing the whole mess is the one-star review that never mentions the product, because the product was fine. It names the silence. Customers forgive late. What they do not forgive is finding out they were forgotten, which is why the delay notice is worth sending before anyone has to ask for it.

Permalink: https://blog.dugong.live/how-to-notify-customers-of-shipping-delays-on-shopify.html#faq-4

### Is one mass apology email to every open order good enough?

It is faster than writing per-order emails, and it is usually worse. One blast to everyone with an open order tells the customer whose box ships this afternoon that it is delayed, gives the customer nineteen days deep the same soothing nothing as the customer two days in, and promises no specific date to anyone, because one template cannot hold four hundred different truths. A delay email that does not know why this order is late, or when it will ship now, is barely better than the silence, and sometimes worse, because it spends the store's credibility on saying nothing. The version that earns patience is per order: know what each open order was promised, catch the ones that slip before the customer does, tell each affected customer the specific reason and a new date, and then keep the new promise or write again.

Permalink: https://blog.dugong.live/how-to-notify-customers-of-shipping-delays-on-shopify.html#faq-5

---

Markdown rendition of https://blog.dugong.live/how-to-notify-customers-of-shipping-delays-on-shopify.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
