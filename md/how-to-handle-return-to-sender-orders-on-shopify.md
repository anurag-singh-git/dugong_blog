# How to handle return to sender orders on Shopify before the customer asks where it is

> The carrier turned the parcel around and the order still reads Fulfilled, because Shopify has no status for it. The AI playbook that catches every return to sender.

- Canonical: https://blog.dugong.live/how-to-handle-return-to-sender-orders-on-shopify.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-10-16
- Section: Research
- Word count: 2852
- Dispatch: Nº 129 · Research · 10 min read
- Full headline on page: How to handle return to sender orders on Shopify *before the customer asks where it is*
- Keywords: shopify return to sender, shopify RTS, shopify RTO, return to origin shopify, undeliverable package shopify, shopify refused delivery, shopify flow return to sender, restock returned to sender shopify, AI shipping automation
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

Day eleven, 9:14am, a one line email: hi, any update on my order? You open the order and everything looks finished. Fulfilled. Tracking number right there. The sale is in last week's numbers, the stock left your count a week and a half ago, and the carrier page, when you finally click through, has been saying the same thing since day three. Returning to sender.

Then somebody finds the box. It has been on the floor behind the printer for two days, which is roughly how long it has been back in the building, unopened, because no part of your store ever said it was coming.


## The short answer

Shopify has no status that means a parcel is coming back to you. The 2026-10 Admin GraphQL FulfillmentEventStatus enum has eleven values and none of them is returning to sender, the value exists only in the unstable version of the API, and the order stays Fulfilled while the box sits in your own receiving area.

Flow has no trigger that fires on a carrier turnaround and no condition to test against, voiding the original label is almost always impossible because voiding requires a label under 30 days old with no tracking events, and the community reship workarounds all distort either revenue or inventory. Shopify also files a return to origin as a customer return, which is why return rates in RTS-heavy markets are mostly couriers rather than products.

The playbook reads the carrier feed hourly, flags the turnaround the hour it happens, names the cause, emails the customer for a corrected address before they ask, applies one reship or refund rule, restocks on physical arrival, and reports RTS separately from returns.
## The word Shopify has not shipped

Here is the whole problem in one list. The [2026-10 Admin GraphQL](https://shopify.dev/docs/api/admin-graphql/2026-10/enums/FulfillmentEventStatus) `FulfillmentEventStatus` enum, the thing that describes where a shipment is, has eleven values: attempted delivery, carrier picked up, confirmed, delayed, delivered, failure, in transit, label printed, label purchased, out for delivery, ready for pickup. Read them again and look for the one that means the parcel is coming back to you. It is not there.

The closest candidate, failure, is documented as the fulfillment request failing, which is a different event entirely: that is your warehouse or your 3PL refusing the job, not a courier reversing a van. Delayed is for a parcel that is still trying. Attempted delivery fires and then fires again and tells you nothing about what happens after the third attempt.

The genuinely odd part is that Shopify has written the word down. In the unstable version of the same enum there is a `RETURNING_TO_SENDER` value, described as the fulfillment being returned to the sender, sitting beside a `BUYER_ACTION_REQUIRED` that would also be useful. Neither is in a stable version. So the concept exists in Shopify's vocabulary and not in anything you, your developer, or any app in the store can build on today. Everyone in this category is working around a value that has been drafted and not released.

Meanwhile the order object does what it was told. It went to Fulfilled when the label printed, and nothing after that is allowed to change its mind. An order whose contents are physically in your own receiving area reads exactly like an order sitting happily on a customer's kitchen table.

## Flow has nothing to fire on

The reasonable next thought is to automate around it with [Shopify Flow](https://help.shopify.com/en/manual/shopify-flow), and the reasonable next thought runs into the same hole. In August 2024 a merchant asked the simplest version of the question: he wanted an automation to run once an order is delivered, and asked which parameter to use. The community answer was the fulfillment event created trigger. Four days later he reported back that it does not work, because delivery happens around 48 hours after fulfillment, so by the time the carrier says anything the workflow has already run and finished. The person who suggested it asked whether a delivered event really fails to start the trigger. Nobody from Shopify answered. The thread stops there.

That is the trigger side. The condition side is worse, because even a trigger that fired on every scan would have nothing to compare against: there is no returning to sender status in the stable API for a Flow condition to test. This is the same shape as [the parcel that stops moving and never gets flagged](https://blog.dugong.live/how-to-catch-shopify-orders-stuck-in-transit.html), and it has the same root cause. Shopify models the moment you hand the box over. It does not model the days afterwards.

## Shopify calls it a return, and it is not one

When the box does come back, the admin offers you the returns flow, which is the wrong drawer. A customer return is a statement about a product. A return to origin is a statement about an address, a delivery window or a courier. Filing them together quietly poisons the only number anyone looks at.

A merchant made this case to Shopify in a May 2026 feature request, asking for a dedicated RTO status separate from customer-initiated returns, on the grounds that mixing them creates misleading return-rate data and makes performance analysis inaccurate. He asked for four things: a separate status, separate reporting, its own webhooks, and filters in Orders and Analytics. The replies are the useful part. One operations lead wrote that an RTO and a customer-initiated return are completely different events operationally, that reporting gets noisy and people start making wrong decisions off the same dashboard, and that manual tags work for a while but break down once order volume increases or multiple people touch fulfillment.

Then the number that should make you check your own dashboard. Another reply described a brand whose return rate looked alarming until they split the data, at which point about 60 percent of it turned out to be RTOs from bad pin codes rather than product issues. Splitting it stopped them discontinuing SKUs that were selling perfectly well. Three months later an app builder in the COD-heavy Indian market added the cleanest summary of the gap: RTO is not a returns problem, it is a fulfillment risk problem, and every app in this space, including his own, has to reconstruct the RTO signal from fulfillment and tracking events instead of getting a clean, structured status.

> **◆ NOTE** If your return rate has ever been used to kill a product, it is worth asking how much of it was ever about the product. An undelivered parcel, a refused delivery and an uncollected pickup all land in the same bucket as a genuine I did not like it, and only one of those is a reason to change the catalog.

## The workarounds, and what each one breaks

There is no reship button, so merchants have built their own, and the thread where they did it is six years long. January 2020: a package came back because the customer typed the wrong address, and the merchant wanted a new label without her reports showing two items sold where one was. Shopify Support answered twice. First, void the original label if you still can, fix the address on the order and buy a new one. Second, if the void window has closed, duplicate the order and apply a 100 percent discount, which keeps revenue honest and then needs a manual inventory adjustment, because the duplicate takes the stock again.

The void route mostly fails, and the Help Center says why. A label can be voided only if it is under 30 days old, has no tracking events at all, was not bought on USPS First Class Mail, and was not added to a manifest in the last 15 minutes. A parcel that traveled far enough for a courier to give up on it has tracking events by definition. You are paying for that label whatever happens, and you will pay for a second one.

So the community built the third way. Edit the original order, add a custom line item called something like Corrected Shipping Address, mark it as requiring shipping, fix the address, and buy a label against that item at the real weight. No zero dollar order, a fresh tracking number, reports roughly intact. It works, people in the thread confirm it still works years later, and the cost is that your customer receives a shipping confirmation for a line item that is not the thing they bought. In August 2024 a merchant looked at all of this and asked the question that belongs in the title of the feature request: why is this not a standard button.

One more wrinkle, and it is the one that catches accounting. A merchant in March 2024 described his process, mark the order returned, create a return with no label, restock, then either refund or reship free, and reported that Shopify had started deducting returned products from daily sales automatically even when they are not refunded, and flagging the order refund owed, which he said is untrue about 90 percent of the time because the goods went back out at no charge. The only reply, four months later, was another merchant saying he wished he had a solution and wished Shopify supported this natively.

## What the silence costs

Price one RTS honestly. Outbound freight, already spent, unvoidable. Return freight, charged by most carriers. A second label if you reship. Eleven days of a customer who has paid and has nothing, which is the part that becomes a chargeback or a public review. Units missing from your sellable count the whole time, so the [reorder math](https://blog.dugong.live/how-to-set-inventory-reorder-points-on-shopify.html) reads a shelf that is wrong and the storefront may sell stock that is sitting in a sealed box twelve feet from the packing bench. Then a refund request two months later, from a merchant's own numbers in the community: a 165 dollar order that cost 17.40 to ship, returned after two failed attempts, with the refund conversation starting nine weeks after the parcel came home.

None of those line items is the real cost. The real cost is the eleven days, because every single thing you would do about an RTS gets cheaper the earlier you do it. On day three the customer is still thinking about the order and will happily send you a corrected address. On day eleven they have asked for a refund and your reship has become an argument. The event is the same; the delay is what prices it.

## What the automation actually has to do

As a Dugong playbook, in plain prose:

```
# trigger
Every hour, every open
shipment's tracking feed,
plus a daily age sweep

# steps
1. Read the scans Shopify
   does not model, every
   carrier, every wording
2. Flag the turnaround the
   hour it happens: tag the
   order, note the timeline
3. Name the cause: bad
   address, refused,
   uncollected, customs
4. Email the customer first
   and ask for the corrected
   address while it matters
5. Apply your rule: reship
   at whose cost, or refund
   less the shipping
6. Reconcile the box on
   arrival, restock what is
   sellable, close the order
7. Report RTS on its own,
   by courier, by region, by
   repeat customer
```

Step one is the whole trick and it is unglamorous. Nobody can give you a status Shopify has not released, so you read the thing that does know: the carrier. The scan text is inconsistent across couriers and that is fine, because recognizing returning to sender, return to shipper, refused by recipient, unclaimed, undeliverable as addressed and a dozen regional variants as the same event is exactly the sort of judgment a language model is better at than a regular expression. The output is one boolean and one reason code, written back onto the order where the rest of your automation can see it.

Steps two and three turn that into something a person can act on. The tag lands on the order within the hour, the timeline gets a line saying what the carrier said and when, and the cause decides the route. A wrong address goes to the customer, immediately, because [the address was probably wrong at checkout](https://blog.dugong.live/how-to-validate-shipping-addresses-on-shopify.html) and you now have a second chance to fix it. A refused delivery goes to support, because refusal often means a dispute you have not heard about yet. An uncollected parcel at a pickup point is the same failure as [a local pickup nobody comes for](https://blog.dugong.live/how-to-handle-shopify-pickup-orders-customers-never-collect.html), and wants a reminder, not a refund. A customs rejection goes to whoever owns [paperwork](https://blog.dugong.live/how-to-fix-missing-hs-codes-on-shopify-before-customs-holds-your-orders.html), because it will happen again on the next order to that country.

Step four is where the money actually is. One email, on the day of the turnaround: your parcel is on its way back to us, here is the address we have, reply with a correction and we will send it straight out. Customers answer that email, because it arrives while they are still waiting for a box. The same email on day eleven gets a refund request, and it was the identical email. This is the same economics as [telling people about a delay before they ask](https://blog.dugong.live/how-to-notify-customers-of-shipping-delays-on-shopify.html), and it is the main reason to automate the detection rather than the paperwork.

Steps five and six keep the books straight. The reship or refund rule is yours, applied the same way every time, with the second label priced to your policy rather than to whoever is on chat that afternoon. Then the physical reconciliation, which matters more than it sounds: restocking should happen when somebody has opened the carton and looked, not when the scan appeared, because [restocking on faith](https://blog.dugong.live/how-to-automatically-restock-returns-on-shopify.html) is how you promise stock you do not have. What comes back damaged or opened gets written off rather than resold. The order closes with a real outcome attached, not a dangling fulfilled.

## Why this is a compiler problem, not an app problem

Everything above sounds like a feature, and that is exactly why it keeps not existing. Look at what step five requires: one store reships free once and refuses twice, one deducts the original shipping, one is COD-heavy and blocks the customer's third attempt entirely, one sells perishables and never reships at all. Step three has the same spread: in India the dominant cause is a bad pin code and the fix is address intelligence at checkout, in the US it is apartment numbers and porch refusals, in the EU it is uncollected parcels at pickup points, and for cross-border it is paperwork. Those are not settings on a toggle. They are paragraphs about your shop, and the paragraph is different in every building.

Which is why an app sells you its paragraph and you spend a quarter bending your operation to fit it. A compiler takes yours as written, the same principle behind [every automation worth building](https://blog.dugong.live/best-shopify-automations-to-set-up.html): describe the RTS policy the way you would explain it to a new hire on their first morning, and let the automation be that explanation, running hourly, in the one place where the carrier is still telling the truth and your store has stopped listening.

## Do this before you close the laptop

Two things, both quick. First, pull every order from the last 60 days that is marked fulfilled and has no delivery scan, then open the tracking for each one. Most stores find at least one parcel already home and unrecorded, and a couple still in motion in the wrong direction. That list is your actual RTS rate, which you have probably never seen, because it has been hiding inside your return rate.

Second, write the policy down in four sentences before you automate anything. When we reship free. When the customer pays for the second label. When we refund and what we deduct. Who we will not ship to a second time without a verified address. If you cannot write those four without a meeting, that is the finding, and the first hour of RTS detection will force the meeting anyway.

Then say the brief out loud the way you would say it to someone who starts on Monday. Watch every shipment. The hour a carrier turns one around, tag the order, tell me why, and email the customer for a corrected address. If they answer in two days, reship on our rule; if they do not, refund less shipping and close it. When the box lands, open it, restock what is good, write off what is not. And never, ever put these in the return numbers. The compiler turns that into the workflow, and day eleven stops being when you find out.

> **◆ READING** Two companion pieces if this one landed: [the parcel that stopped moving](https://blog.dugong.live/how-to-catch-shopify-orders-stuck-in-transit.html), on shipments that go quiet without ever coming back, and [delivered but not received](https://blog.dugong.live/how-to-handle-delivered-but-not-received-claims-on-shopify.html), on the opposite failure, where the carrier says it arrived and the customer says it did not. Also worth reading: [the shipping label you paid for and never used](https://blog.dugong.live/how-to-catch-shopify-shipping-labels-you-never-used.html), on the label bought for a parcel that never went anywhere.

If you are a Shopify merchant with a return to sender story, the box that sat behind the printer, the reship that broke your reports, the return rate that turned out to be couriers, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Does Shopify have a return to sender status?

No. The order keeps whatever status it had when the parcel left, which is Fulfilled, and the shipment keeps whatever the carrier last reported. The 2026-10 Admin GraphQL FulfillmentEventStatus enum has eleven values, ATTEMPTED_DELIVERY, CARRIER_PICKED_UP, CONFIRMED, DELAYED, DELIVERED, FAILURE, IN_TRANSIT, LABEL_PRINTED, LABEL_PURCHASED, OUT_FOR_DELIVERY and READY_FOR_PICKUP, and none of them means the box is on its way back to you. RETURNING_TO_SENDER appears only in the unstable version of the API, so the word exists in Shopify's vocabulary but not in any version a merchant or an app can rely on today. In practice a return to sender is invisible until the box physically arrives, which is why most stores find out from a customer email rather than from their own store. Catching it early means watching the carrier's tracking events yourself and treating the turnaround scan as the event Shopify does not model.

Permalink: https://blog.dugong.live/how-to-handle-return-to-sender-orders-on-shopify.html#faq-1

### Can Shopify Flow trigger when a package is returned to sender?

Not reliably, and not for this. The nearest thing on the Flow bench is the fulfillment event created trigger, and it is built around fulfillment being created rather than the carrier changing its mind later. In August 2024 a merchant asked how to automate on delivery and was pointed at that trigger, then reported back that it does not work, because delivery happens roughly 48 hours after fulfillment and the workflow never fires. No Shopify staff replied and the thread never reached an answer. Even if the trigger fired on every scan, there is no returning to sender status in the stable API for a condition to test, so the workflow would have nothing to match on. The working pattern is the other way round: read the carrier tracking feed on your own schedule, recognize the turnaround language in the scan, and write the result back onto the order as a tag and a timeline note so the rest of your automation has something to react to.

Permalink: https://blog.dugong.live/how-to-handle-return-to-sender-orders-on-shopify.html#faq-2

### What should I do when a Shopify order is returned to sender?

Decide three things in order, and decide them before the box arrives rather than after. First, cause: a wrong or incomplete address, a refused delivery, an uncollected parcel at a pickup point, or a customs rejection are four different problems with four different answers. Second, outcome: reship to a corrected address, or refund. Most policies reship once at your cost when the carrier or your own label was at fault, and ask the customer to cover the second label when the address was wrong, which is roughly what merchants in the community threads settled on, refund the product and deduct the original shipping cost plus any carrier return fee. Third, the record: restock the units when the box is physically back and checked, not when the scan appears, and keep the whole thing out of your customer return rate, because an undelivered parcel is a fulfillment failure, not a product someone disliked. The expensive part is never the decision, it is the eleven days before anyone noticed there was one to make.

Permalink: https://blog.dugong.live/how-to-handle-return-to-sender-orders-on-shopify.html#faq-3

### How do I reship a returned to sender order on Shopify without breaking my reports?

Shopify has no reship button, and the workarounds merchants trade all distort something. Shopify Support's own answer in January 2020 was to void the original label if it still qualifies and buy a new one after correcting the address, and otherwise to duplicate the order and apply a 100 percent discount, which keeps revenue honest but double counts the units and needs a manual inventory adjustment. The most upvoted community method is to edit the original order and add a custom line item titled something like Corrected Shipping Address, then buy a label against that item, which avoids a zero dollar order and produces a new tracking number, at the cost of the customer seeing a line item that is not their product. A merchant asked in August 2024 why this is not a standard button, which is the honest summary. Voiding usually fails anyway: the Help Center requires a label under 30 days old with no tracking events, not bought on USPS First Class Mail, and not manifested in the last 15 minutes, and a parcel that traveled far enough to be turned around has tracking events by definition. An automation can do the whole sequence consistently, correct the address, create the reship, carry the original order number forward in the note, and record the second label cost against the first order so the margin story stays true.

Permalink: https://blog.dugong.live/how-to-handle-return-to-sender-orders-on-shopify.html#faq-4

### Why does return to sender wreck my Shopify return rate?

Because Shopify files it as a return, and it is not one. A customer-initiated return says something about the product. A return to origin says something about an address, a delivery window or a courier. In a May 2026 feature request a merchant asked Shopify for a separate RTO status on exactly this ground, that mixing the two creates misleading return-rate data and makes performance analysis inaccurate. A reply in the same thread described a brand where about 60 percent of the headline return rate turned out to be RTOs from bad pin codes rather than product issues, and said splitting the data stopped them discontinuing SKUs that were actually selling well. Another reply, from someone building in the category, admitted that every app in this space has to reconstruct the RTO signal from fulfillment and tracking events instead of getting a clean, structured status. Until Shopify ships the status, the separation has to be yours: tag the order with the cause when the turnaround is detected, keep RTS out of the return numbers you report on, and report it where it belongs, next to delivery success by courier and by region.

Permalink: https://blog.dugong.live/how-to-handle-return-to-sender-orders-on-shopify.html#faq-5

### Can AI handle return to sender orders on my Shopify store?

Yes, and this is a gap worth automating because every part of it is reading and routing rather than judgment. An automation like Dugong watches the tracking feed for every open shipment, recognizes the turnaround however the carrier words it, and does within the hour what a person does eleven days late: tag the order, name the likely cause, email the customer before they email you, ask for a corrected address while they are still paying attention, and park the order in a queue with a clock on it. When the box lands it reconciles the physical arrival with the scan, restocks what is sellable, flags what is not, applies your reship or refund rule, charges or waives the second label, and keeps the event out of your return rate. The honest limits: nothing can inspect the carton, so somebody still opens it; carrier wording varies and a thin tracking feed will miss a scan, so the undelivered age sweep is the backstop; and the policy calls, who pays for the second label, how many attempts before you refund, which addresses you refuse to ship to twice, are yours to write. What the automation removes is the silence between the turnaround and the discovery.

Permalink: https://blog.dugong.live/how-to-handle-return-to-sender-orders-on-shopify.html#faq-6

---

Markdown rendition of https://blog.dugong.live/how-to-handle-return-to-sender-orders-on-shopify.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
