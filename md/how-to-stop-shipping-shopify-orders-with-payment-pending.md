# How to stop shipping Shopify orders that say Payment pending

> An order can read Payment pending and still sit in your queue looking normal. The AI playbook that holds every one until the money lands.

- Canonical: https://blog.dugong.live/how-to-stop-shipping-shopify-orders-with-payment-pending.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-10-19
- Section: Research
- Word count: 2849
- Dispatch: Nº 132 · Research · 9 min read
- Full headline on page: How to stop shipping Shopify orders *that say Payment pending*
- Keywords: shopify payment pending, shopify pending payment order, fulfill shopify order pending payment, shopify order shipped not paid, shopify payment status expired, hold fulfillment awaiting payment, shopify collective payment pending, AI payment hold automation
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

Order 4417 came in on a Thursday afternoon. Two items, a real address, a customer who had bought twice before. It appeared in the unfulfilled queue between two other orders, it went onto the pick list with them, it got a label at eight the next morning and it left on the midday collection.

Nobody looked at the payment status. There was no reason to. It said Payment pending, the same two words Shopify shows while a perfectly normal bank transfer settles, and the badge sat in a column nobody reads when the order is already on the pick list.

Nine days later it turned to Expired. The goods were gone, the label was paid for, the customer stopped replying, and there was no event anywhere in the admin that said the word anybody needed to hear, which is that you just shipped a parcel for free.

## Unpaid is four different problems wearing one badge

Start with the vocabulary, because this is where most stores lose the thread. Shopify's [order status documentation](https://help.shopify.com/en/manual/fulfillment/managing-orders/order-status) defines Unpaid not as a status but as a grouping, and it contains four things: Authorized, Pending, Expired and Partially paid.

Those four are not the same risk at all. Authorized means the provider has verified the card and the funds are held for you until you capture them, so shipping against it is ordinary business. Pending means the provider has started processing and needs more time, so shipping against it is a bet. Expired means the window closed or the provider could not process the payment at all. Partially paid means you captured less than the total.

So the filter that looks like the answer is the filter that hides the problem. Pull up Unpaid and you get the safe case and the unsafe case in the same list, which is exactly why staff stop using it after a week and go back to working the unfulfilled queue instead. The unfulfilled queue is sorted by fulfillment status and says nothing at all about money.

## Shopify's own ready to fulfill gate never checks the money

This is the part that surprises people who assume the platform is quietly protecting them.

Shopify has a real gate before fulfillment, and it is documented on the [Fulfillment order ready to fulfill](https://help.shopify.com/en/manual/shopify-flow/reference/triggers/order-ready-to-fulfill) trigger. That trigger starts a workflow when an order has completed risk assessment and has inventory available for the order, after Shopify releases its own initial hold. Read the two conditions again. Risk assessment. Inventory availability. Payment is not in the sentence.

The same gap is in the setting most stores turn on and forget. In [order processing](https://help.shopify.com/en/manual/checkout-settings/order-processing) you can choose to automatically fulfill the order's line items, and the one escape hatch offered next to it is to automatically fulfill all orders, even those with a high risk of fraud. Shopify thought carefully enough about that checkbox to build a fraud override for it. There is no payment condition on it anywhere, so a pending order can be marked fulfilled by your own store settings while the money is still in flight.

And on the only page where Shopify does address the risk, the advice is a sentence to a human. [Pending payments](https://help.shopify.com/en/manual/fulfillment/managing-orders/payments/pending-payments) says you are not prevented from fulfilling these orders, and then asks you to wait until the payment status is Paid before fulfilling, to make sure you get paid. That is the whole control. Somebody reading a column at eight in the morning.

## Where Payment pending comes from, and why it is spreading

If you take card payments only, this reads like someone else's problem. The list of ways a pending order lands in your queue has been getting longer for three years.

Shopify's own description covers payments made by cryptocurrency, wire, barcodes and other alternatives to credit card payments, where the provider has started processing but needs more time, and says processing can take several days depending on the payment type. Then there are manual methods you set up yourself, bank deposit, money order, cash on delivery, where Shopify notes that a manual payment gateway sends no email at all and you have to read the order timeline to know what was sent. Then there are orders with payment terms, where the [deferred payments](https://help.shopify.com/en/manual/fulfillment/managing-orders/payments/deferred-payments) documentation has the status become Overdue when the due date passes, and Due the moment a payment is due today.

Then there is the one that caught a lot of stores off guard. On 19 June 2024 Shopify [changed the payment status for Collective supplier orders](https://changelog.shopify.com/posts/changes-to-shopify-collective-supplier-order-payment-status): orders received from retailers who do not use automatic payments are now marked Payment Pending rather than Paid. If you supply other merchants through Collective, a whole class of orders that used to arrive reading Paid now arrives reading pending, and the [supplier payments page](https://help.shopify.com/en/manual/online-sales-channels/shopify-collective/suppliers/payments) tells you plainly not to ship orders in Payment pending status, while also explaining that your funds do not transfer until after you fulfill. Those two instructions live together and the ordering between them is left to you.

Ten days ago, on 9 October 2026, a Collective supplier posted in the Shopify community asking how other suppliers prevent orders from shipping before payment is secured, and described the failure precisely: an order can still be marked Payment Pending while fulfillment workflows treat it as ready to process, and a single missed status check ships the goods. The thread has no replies. That is the state of the art on the open web: a question, a plug for an app, and silence.

## The clock nobody is counting

Pending is not a steady state. It has an expiry, and Shopify's guidance is that pending payments usually expire after about a week, with the exact date held by your payment provider rather than by Shopify. When it runs out the order status changes to Expired. If the payment fails outright, the customer gets an email saying the payment could not be processed with a Pay now link to retry, and if it succeeds they get a confirmation. You are not in either email.

Which means the window where this is still recoverable is roughly seven days wide, it opens the moment the order is created, and nothing in the admin counts down. There is no badge at day five, no report of pending orders by age, no warning on the fulfillment screen. On day eight the status word changes and a shipped parcel becomes a write off.

The pending state also takes your tools away while it lasts, which is the detail that makes staff improvise. Shopify lists what you may not be able to do on a pending order: edit the items, discounts or shipping address, restock the items, cancel the order, manually collect payment, or mark it as paid. The restrictions lift when the payment status changes. So the obvious instinct, cancel it and move on, is not available either. Shopify even advises contacting the payment provider before cancelling an expired order, in case the payment can still be captured.

## The hold reason Shopify built for this and never applies

Here is the part that makes this worth automating rather than worth complaining about.

Shopify has a fulfillment hold system, and holds carry a typed reason. The [FulfillmentHoldReason](https://shopify.dev/docs/api/admin-graphql/latest/enums/FulfillmentHoldReason) enum has eight values, and the first one in the list is AWAITING_PAYMENT, documented as the fulfillment hold is applied because payment is pending. It sits alongside HIGH_RISK_OF_FRAUD, INVENTORY_OUT_OF_STOCK and INCORRECT_ADDRESS.

So the lever exists, it is named after exactly this problem, and an order on hold is visible everywhere it needs to be. Shopify's own order status page says that while a fulfillment is On hold the inventory can be reserved and the order cannot be fulfilled until the hold is released, which is also the only state your 3PL, your warehouse app and your pick list all respect without being told anything new.

Nothing in Shopify applies it for you when a payment is pending. The reason was written, the plumbing was built, and the decision to use it was left in the admin, which is a sentence you could write about most of the quiet leaks in a store.

## Why Flow gets you most of the way and then stops

Flow can hold an order. The [Hold fulfillment](https://help.shopify.com/en/manual/shopify-flow/reference/actions/hold-fulfillment) action changes the order's status to On hold, takes a reason and reason notes, and can notify the merchant. Order created is on its list of compatible order level triggers, and an order level trigger holds every fulfillment order on the order. So the first half of this is a Flow anybody can build in ten minutes: on order created, if the payment status is pending, hold the fulfillment.

The release is where it comes apart, and it comes apart in three separate places.

The obvious release trigger is [Order paid](https://help.shopify.com/en/manual/shopify-flow/reference/triggers/order-paid), which starts a workflow when an order's payment status changes to paid. Its own documentation rules out two of the cases you care about: partially paid orders do not start a workflow with this trigger, and funds that are authorized but not captured do not either. A deposit against payment terms is a partial payment, so the trigger that is supposed to free your B2B order is documented as not firing on it.

Then there is the behaviour merchants have been reporting since 18 April 2022, in a thread titled [Order Paid trigger not working for payments completed after initial order was created](https://community.shopify.com/t/order-paid-trigger-not-working-for-payments-completed-after-initial-order-was-created/114741). The merchant found that only orders manually marked as Paid started the Order Paid automation, that payments collected later through the Collect Payment button did not, and that this did not use to behave this way previously. A Shopify staff member replied three days later to say thanks for reporting this, they would look into it and get back. There is no later staff answer on the thread. Collect Payment is precisely how a pending order gets paid.

And there is nothing on the bench that watches the money itself. A merchant asked in November 2023 how to make Flow find orders with a pending payment and tag them; the only reply suggested reading `displayFinancialStatus` for PENDING and querying with a `financial_status:PENDING` filter, pointed out that it was not clear when the check should even run, and the thread closed with no accepted answer. That is the honest shape of it. You can ask what the payment status is, at a moment you choose, and nothing will tell you when it changed.

Which is why the shape of the fix is a poll rather than a trigger, and Shopify quietly agrees. The Admin API now carries [orderPaymentStatus](https://shopify.dev/docs/api/admin-graphql/latest/queries/orderPaymentStatus), a query that retrieves the status of a deferred payment by its payment reference ID so you can monitor the processing status of payments, and returns the status, an error message, a translated error message and the transactions. It is built to be asked repeatedly. That is a polling loop with a schema.

## What this costs in a month

Run it on your own mix, because the rate depends entirely on how much of your volume is not a captured card. Take a store doing 900 orders a month at an 80 dollar average, where six percent of orders arrive pending, so 54 orders in flight. If one in ten of those pending orders never clears and half of those have already shipped, that is 2 or 3 parcels a month gone with the goods, the postage and the pick time, call it 250 dollars a month and 3,000 a year, on goods you would have kept by waiting two days.

The second cost is the one stores feel first and never book. Every pending order that your team is unsure about gets handled twice: once when somebody notices the badge and puts the picking slip aside, and again when somebody else finds it and has to work out whether the money arrived. That is the same tax as [an authorization nobody captured in time](https://blog.dugong.live/how-to-automatically-capture-payments-on-shopify.html), except this one is pointed in the opposite direction.

## What the automation actually has to do

As a Dugong playbook, in plain prose:

```
# trigger
Order created, order
transaction created, order
paid, plus a 30 minute sweep

# steps
1. Read the payment status, not
   the fulfillment status
2. Hold with AWAITING_PAYMENT the
   moment a pending order
   appears
3. Let authorized and paid orders
   through untouched
4. Poll the money and release the
   hold the hour it lands
5. Count the days to expiry and
   chase before the window
   shuts
6. Flag every release done by hand
   while payment is pending
7. Close out expired and failed
   payments the same day
```

Step one is the whole design in one line. The queue your team works from is sorted by fulfillment status, and the fact that matters lives on a different field. Everything downstream is just keeping those two fields in the same sentence.

Step two is the one that pays. Hold on arrival rather than warn on arrival, because a warning competes with a pick list and a hold does not. Use the typed reason rather than a tag, so the hold reads the same to your warehouse app, your 3PL and the person covering on Saturday.

Step three is what keeps the rest of it alive. If the automation holds authorized orders too, somebody will switch it off inside a week, and they will be right to. Authorized funds are held for you. Pending funds are not. The distinction is the product.

Step five is the step nobody builds by hand, because it needs a clock. Pending has an expiry of about a week and the exact date sits with the provider, so the automation tracks age from order creation, nudges the customer with the Pay now link while it still works, and tells you on day five rather than on day nine, when the only remaining options are a conversation with the provider and a write off.

Step six exists because every real store overrides this sometimes, and should. A trusted wholesale account on net terms can ship before the money lands. What you cannot afford is not knowing who did that, on which order, and whether the payment ever followed. Log the override as an event on the order, not as a memory.

The honest limits. A hold stops fulfillment, it does not stop a human pressing fulfil anyway, which is why step six is in the list rather than being a footnote. A pending order cannot be edited, restocked, cancelled or marked as paid while it is pending, so a failed one has to wait for Shopify to let go before you can clean it up. And the expiry date belongs to the payment provider, so your clock is an estimate from order creation until the provider tells you otherwise.

## Why this is a workflow, not a feature request

Three facts have to meet, and Shopify keeps them in three places with no relationship declared between them. The order knows its payment status and when that status last changed. The fulfillment order knows whether it is open, on hold or already gone. The provider knows the expiry date and whether the money is actually coming.

No single feature joins them. A payment status column would not stop the pick list. A hold would not know when to let go. A better Order paid trigger would not count the days to expiry. The only thing that closes this is something holding all three at once on a short clock, which is a workflow, and it has the shape every quiet leak in a store has: the information exists, the lever exists, and nothing stands between them.

## Do this before you close the laptop

Three checks, fifteen minutes, no code.

Filter your orders by payment status to anything other than Paid, then sort by date and look at the oldest ones. Open each and check the fulfillment status. Every order in that list that reads Fulfilled and has never been paid is a parcel you have already given away, and the count will tell you whether the rest of this is worth building.

Then open Settings, then Checkout, and read your order processing block. If automatically fulfill the order's line items is on, you are not making this decision at eight in the morning, your settings are making it at the moment of checkout, for every payment method you accept.

Then ask whoever picks on a Saturday what Payment pending means. If the answer is anything other than stop, the badge is not a control, it is decoration.

> **&#9670; READING** Two companion pieces if this one landed: [the payment that expires before you capture it](https://blog.dugong.live/how-to-automatically-capture-payments-on-shopify.html), on the same gap pointed the other way, and [the unpaid order that never cancels itself](https://blog.dugong.live/how-to-automatically-cancel-unpaid-orders-on-shopify.html), on what to do with the ones that never clear.

If you sell on Shopify and have a version of this story, the wire that never arrived, the Collective order you shipped on trust, the net 30 account that went quiet, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

## Common questions

### What does Payment pending mean on a Shopify order?

It means the payment provider has started processing the payment and needs more time, so no money has reached you yet. Shopify's documentation describes it as applying to payments made by cryptocurrency, wire, barcodes and other alternatives to credit card payments, and says processing can take several days depending on the payment type. It also covers manual methods you set up yourself, such as bank deposit, money order and cash on delivery, and orders that run on payment terms, where the status later becomes Due or Overdue. Pending is not the same as Authorized. Authorized means the provider verified the card and is holding the funds for you until you capture them, which is ordinary business to ship against. Pending means nothing is held and nothing is guaranteed. Shopify groups both of them, plus Expired and Partially paid, under the single label Unpaid, which is why the filter that looks like the answer puts the safe case and the unsafe case in the same list.

Permalink: https://blog.dugong.live/how-to-stop-shipping-shopify-orders-with-payment-pending.html#faq-1

### Can you fulfill a Shopify order with a pending payment?

Yes, and that is the problem. Shopify's pending payments page states that you are not prevented from fulfilling these orders, and then asks you to wait until the payment status is Paid before fulfilling, to make sure you get paid. Nothing enforces it. The documented gate before fulfillment, the Fulfillment order ready to fulfill trigger, fires when an order has completed risk assessment and has inventory available for the order, and payment is not one of its conditions. The automatic fulfillment setting in order processing is the same story: it offers one override, to automatically fulfill all orders even those with a high risk of fraud, and carries no payment condition at all. So a pending order can be marked fulfilled by your own store settings while the money is still in flight, and the only thing standing between that and a shipped parcel is somebody reading a badge in a column on a busy morning.

Permalink: https://blog.dugong.live/how-to-stop-shipping-shopify-orders-with-payment-pending.html#faq-2

### How long does a Shopify pending payment take to clear?

Shopify's guidance is that pending payments usually have an expiry date of about a week, and that your payment provider can confirm the exact expiry for a given payment. If the payment clears, the customer gets a confirmation email. If it fails, the customer gets an email saying the payment could not be processed with a Pay now link to retry. If it is not completed by the expiry date, the order status changes to Expired. Nothing in the admin counts those days down for you: there is no badge at day five, no report of pending orders by age and no warning on the fulfillment screen, so the recoverable window is roughly seven days wide and entirely invisible. Shopify also advises contacting the payment provider before cancelling an expired order, because the payment can sometimes still be captured, which is worth doing before you write anything off.

Permalink: https://blog.dugong.live/how-to-stop-shipping-shopify-orders-with-payment-pending.html#faq-3

### Can Shopify Flow hold an order until the payment clears?

Half of it, reliably. The Hold fulfillment action changes the order's status to On hold, takes a reason and reason notes, and works with Order created, which is an order level trigger and therefore holds every fulfillment order on the order. So holding a pending order on arrival is a workflow you can build in ten minutes. Releasing it is where Flow runs out. The natural release trigger, Order paid, documents two exclusions that matter here: partially paid orders do not start a workflow with it, and funds that are authorized but not captured do not either, which rules out deposits against payment terms. On top of that, merchants have reported since 18 April 2022 that the trigger does not fire for payments collected later through the Collect Payment button, only for orders manually marked as paid, and the Shopify reply on that thread is a promise to look into it with no follow up. Collect Payment is exactly how a pending order usually becomes paid.

Permalink: https://blog.dugong.live/how-to-stop-shipping-shopify-orders-with-payment-pending.html#faq-4

### Why can't I cancel or edit a Shopify order with a pending payment?

Because Shopify locks the order while the provider is still working. The pending payments page lists what may be unavailable: editing the order's items, discounts or shipping address, restocking items, cancelling the order, manually collecting payment, and marking the order as paid. Those restrictions lift when the payment status changes. This is the detail that pushes staff into improvising, because the obvious response to a payment that looks doubtful, cancel it and restock, is not on the table while it is pending. The practical sequence is to hold the fulfillment rather than try to cancel the order, wait for the status to move to Paid or Expired, and only then clean up. If it expires, contact the payment provider before cancelling, since Shopify notes the payment can sometimes still be captured.

Permalink: https://blog.dugong.live/how-to-stop-shipping-shopify-orders-with-payment-pending.html#faq-5

### Can AI stop Shopify orders shipping before the payment clears?

Yes, and it is a good fit for automation because it is a bookkeeping problem rather than a judgment call. An automation like Dugong reads the payment status rather than the fulfillment status on every new order, and holds the fulfillment with the typed reason AWAITING_PAYMENT the moment a pending order appears, which is a reason Shopify already defines as the fulfillment hold is applied because payment is pending. It lets authorized and paid orders through untouched, because authorized funds are held for you and holding them would get the whole thing switched off inside a week. Then it polls, using the orderPaymentStatus query that Shopify built to monitor the processing status of deferred payments, and releases the hold the hour the money lands. It counts the days to expiry and nudges the customer while the Pay now link still works, so you hear about it on day five rather than on day nine. And it logs every release done by hand while payment is pending, because overriding this for a trusted account is legitimate and forgetting that you did is what turns it into a write off. The honest limits: a hold stops fulfillment but not a determined human, a pending order cannot be edited or cancelled until Shopify lets go of it, and the real expiry date belongs to the payment provider, so the clock is an estimate until they say otherwise.

Permalink: https://blog.dugong.live/how-to-stop-shipping-shopify-orders-with-payment-pending.html#faq-6

---

## Read next

- [The payment that expires before you capture it](https://blog.dugong.live/how-to-automatically-capture-payments-on-shopify.html): Authorized is not paid: Shopify gives you 7 days to capture before the hold expires. The AI playbook that captures every order before the clock runs out.
- [The unpaid order that never cancels itself](https://blog.dugong.live/how-to-automatically-cancel-unpaid-orders-on-shopify.html): A customer picks bank transfer or cash on delivery, then goes quiet, and the dead order sits in your admin holding stock. The AI playbook that chases payment, then cancels and restocks on time.
- [The order on hold that nobody releases](https://blog.dugong.live/how-to-automatically-release-held-shopify-orders-when-stock-arrives.html): Shopify has no event for stock arriving on a held order, so paid orders age in the On hold queue for days. The AI playbook that releases them the hour the pallet lands.
