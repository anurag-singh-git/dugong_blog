# How to fix Shopify orders with no phone number before the label fails

> Three orders will not print a label this morning, and six more will print one no courier can act on. The field at checkout says optional, and that is the whole story.

- Canonical: https://blog.dugong.live/how-to-fix-shopify-orders-with-no-phone-number-before-the-label-fails.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-11-16
- Section: Research
- Word count: 2194
- Dispatch: Nº 141 · Research · 8 min read
- Full headline on page: How to fix Shopify orders with *no phone number* before the label fails
- Keywords: shopify order no phone number, could not create label shopify, shopify recipient phone number required, require phone number shopify checkout international only, shopify shipping label failed missing phone, pickup point label blocked phone, shopify flow tag order missing phone, AI order data check before fulfillment
- Entities: Shopify (https://www.wikidata.org/wiki/Q7501150); Shipping label (https://www.wikidata.org/wiki/Q7498793); Last mile (transportation) (https://www.wikidata.org/wiki/Q6494801); Business process automation (https://www.wikidata.org/wiki/Q5001911)
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

Friday morning, forty-one orders to get out. Thirty-eight print a label. Three come back with the same message: could not create label.

All three are going abroad. The addresses are fine. What they are missing is a phone number, which nobody at your store failed to collect, because the field at checkout says optional and every one of those customers read it correctly.

So those three orders sit in the queue looking exactly like the thirty-eight that shipped, because Shopify has no status that means this one cannot be labeled. Someone finds them on Monday, or the customer finds them on Wednesday.

## The short answer

Shopify's checkout phone field has three states, and none of them fit a store that ships internationally. Do not include, optional, or required, applied to every country and market you sell to. There is no per country rule without a checkout app on Shopify Plus.

So you either tax every domestic checkout with a field it does not need, or you accept that a share of your international orders will arrive without the one thing their carrier insists on. Most stores pick the second, correctly, and then build nothing to cover it.

The fix is a check that runs between the order landing and the label printing: does this order carry what its destination actually needs, and if not, can the number be recovered from somewhere else on the order before anyone emails the customer. It usually can.

## The setting is all or nothing, which is why nobody turns it on

Shopify's [checkout form options](https://help.shopify.com/manual/checkout-settings/checkout-form-options) give the shipping address phone field three states. Do not include. Optional, which is the default on new stores. Required, which the documentation describes as the setting for when your payment provider or shipping carrier needs a phone number.

That is the whole control surface, and the same page says plainly that these customer information settings apply to every country and market you sell to. To vary a checkout field by country you need an app that customizes checkout, and those are a Plus capability.

Merchants have been asking for the per country version for years. In [one thread](https://community.shopify.com/t/is-it-possible-to-make-a-phone-number-field-mandatory-for-some-countries-and-not-others-in-checkout/219916) a reply laid out steps for a country setting inside form options, and three separate merchants came back to say they could not find it in their own admin, the last of those in October 2024. A reply in June 2026 concluded that a paid app is the only route. A [second thread](https://community.shopify.com/t/require-phone-number-on-checkout-for-international-customers-only/37653) asks for the same thing in the title.

One workaround in those threads is honest about what it is: leave the field optional and rewrite its label in your theme content to explain that international orders need a number. That asks politely. It enforces nothing.

## Two ways this fails, and the quiet one costs more

The visible failure is the one from Friday morning. Error `030009` is a carrier validation error, usually returned by FedEx, and [the most common trigger is a missing or malformed recipient phone](https://www.shippypro.com/blog/en/shopify-shipping-label-errors). Malformed matters as much as missing. The number needs its country code, and the digit count has to fit the destination, so a ten digit US number on a parcel to Germany fails exactly like a blank field.

Its neighbors are worth knowing while you are in there. A blank first or last name gets rejected outright. An address line over the carrier's limit fails, which is 35 characters for DHL and UPS and 32 for Evri. And some carriers want a valid phone on your own origin address under Settings and then Locations, where one blank field fails every label you try to buy rather than one.

At least that failure announces itself. The quiet one does not. The label buys, the label prints, and the number simply is not on it.

A merchant shipping about twenty international orders a month [described the result](https://community.shopify.com/t/international-shipping-labels-shopify-causing-thousands-in-loss-due-to-missing-info/255572): parcels reach the destination country and stop there, held at the local post office, with nobody able to reach the recipient to arrange the handover. They compared their Shopify label against one from another provider that carried the number, reshipped orders at their own cost, counted the loss in thousands, and said support dismissed it twice. That is one store's account of its own carrier mix rather than a universal rule. The shape of it is the part to take seriously: you pay for the goods, you pay for two labels, and the customer tells people you lost their order.

## The pickup point hole that no setting will close

This is the version that should bother you most, because it is a Shopify integration failing against a Shopify setting.

Merchants shipping to pickup points with Mondial Relay [report that the pickup flow skips the standard shipping address form](https://community.shopify.com/t/critical-issue-with-mondial-relay-pickup-point-orders-labels-blocked-due-to-missing-phone-number/646148), which is the only form the required phone setting governs. So the field stays optional no matter what the admin says. Shopify Shipping then refuses the label, with the message that a recipient phone number is required for pickup point labels.

And pickup point orders cannot be edited, so even when the customer emails the number back, there is nowhere to put it.

In a [parallel thread](https://community.shopify.com/t/phone-number-required-for-pickup-delivery/661699) a merchant puts it in one line: for pickup point delivery it has become optional, so most customers simply do not enter it. Their cart attribute workaround failed because customers could delete the prefilled number. Support spent more than an hour on it and attributed the problem to the carrier, which the merchant disputed, since the integration is Shopify's own.

The workarounds cost real money. One merchant priced manual labels on the carrier portal at about 5.99 euro against about 3.30 euro on Shopify's negotiated rate, and another migrated their carrier account by hand to get to 4.51. As of the end of August 2026 the thread records only that the report was forwarded to Shopify's product team. No fix, no timeline.

It is worth understanding why the carrier will not bend on this. A pickup point network needs the number to tell the buyer the parcel has arrived, not merely to attempt a delivery, which is why one pickup app's documentation [simply tells merchants to set the field to required](https://atlaspickuppoints.com/docs/faq/recommended-store-settings) and accept the cost elsewhere.

## The number is often already on the order

Before any of the expensive remedies, the cheap one. A Shopify order can carry a phone number in three places: on the shipping address, on the billing address, and on the customer record, because the checkout contact method can be a phone number instead of an email.

The label reads the shipping address. Only the shipping address. Which means an order can show a phone number in the admin, to a human looking at the order page, and still fail at the label.

This is common enough that order tagging apps document it as a standard recipe: [tag the order with the shipping phone, and fall back to the billing phone when the shipping one is empty](https://app.loopedin.io/order-tagger/kb/popular-use-cases-for-shopify-order-tags/tag-orders-with-the-billing-phone-number-if-the-shipping-phone-number-is-empty). Read that as a finding rather than a feature. The number you are about to email a customer for is frequently sitting one field away.

## What this costs on an ordinary month

Take a store doing fourteen hundred orders a month with fifteen percent going abroad. That is two hundred and ten international parcels. With the field optional, say half of them arrive with no phone on the shipping address, so a hundred and five.

Most of those deliver without incident, because most routes never need the number. Say five percent end badly: five parcels. Each one costs the goods, the outbound label, the replacement label, and twenty minutes of somebody's afternoon. On a forty-six dollar item and an eighteen dollar label that is around four hundred dollars a month in hard cost, before the refund you give to keep the review clean.

Four hundred dollars is not the interesting part. The interesting part is that none of it lands in any report. There is no line called orders we could not label. The only trace is three rows in a fulfillment queue that look identical to the rows that shipped.

## What Shopify Flow gets you, and where it stops

Flow can do the detection, and you should go and build this today. Its [conditions](https://help.shopify.com/en/manual/shopify-flow/reference/conditions) read nested fields, with the shipping address given as the documented example, and it has an empty or does not exist operator that returns true for a blank or null value. An order created trigger, that condition, and an add tag action is a ten minute build that puts a visible marker on every order missing a number.

Then it stops. Flow cannot ask the customer for the number, because its one email action only reaches customers subscribed to marketing, which is [its own long story](https://blog.dugong.live/how-to-fix-shopify-flow-emails-that-never-send.html). It cannot write a number back onto the shipping address when one arrives. It cannot tell whether this particular destination and shipping method even need one, so it flags the Denver order next to the pickup point order in Lyon. And it can do precisely nothing about an order Shopify will not let anyone edit.

Flow gives you the flag. Everything after the flag is still a person with a browser.

## What the automation actually has to do

As a Dugong playbook, in plain prose:

```
# trigger
Order created or updated,
plus a sweep of the fulfillment queue

# steps
1. Check every order for the
   fields its label needs
2. Look in the other two phone
   fields first
3. Ask the customer once, where
   they read
4. Write the number onto the
   shipping address
5. Hold the order, not the whole
   queue
6. Require the number where it
   earns its keep
7. Report the misses every week
```

Step one is a rule per destination and shipping method, not a blanket check for a blank field. A domestic ground parcel usually does not care. An express international parcel, a pickup point delivery and a handful of countries care very much. Flagging everything trains your team to ignore the flag.

Step two is the fallback, and it resolves more of these than anything else in the list. Shipping address, then billing address, then the customer record, then any earlier order from the same customer. Only a genuine blank across all four is worth a message.

Step three is one message, sent on the channel the customer actually reads, saying what you need and why, with a link that takes them one tap to reply. Not a support ticket. Not an email that sounds like a newsletter. The reply rate on this is the difference between the playbook working and the playbook being a report nobody acts on.

Step four is the part teams skip. The number has to land on the shipping address, because that is where the label looks. A phone number recorded in a help desk thread, or typed into the order notes, has not solved anything.

Step five keeps the warehouse moving. Hold the affected order and let the other thirty-eight print. The common failure mode is a batch that errors out in the middle and a picker who starts the whole run again.

Step six is where the checkout setting finally earns a decision. If your weekly report shows the misses concentrated in one market or one shipping method, scope a checkout rule to that case, or make the field required and accept the conversion cost knowingly. For pickup point orders, upstream is the only place this is solvable at all.

Step seven is the number that keeps it from drifting back. Misses per week, split by country and shipping method, with the recovery rate next to it. If that number is rising, something changed in your mix, and you will see it in a week rather than in a quarter of chargebacks.

## Do this before you close the laptop

Three things, about fifteen minutes, no tooling required.

Open Settings, then Checkout, and read what your shipping address phone field is actually set to. A surprising number of merchants have never looked, and are running whatever the store shipped with.

Then open Settings, then Locations, and check that every location you ship from has a phone number on it. That one takes thirty seconds and fails every label when it is wrong.

Last, filter last month's orders to the ones going abroad and count how many have no phone on the shipping address. That count is the size of your exposure, and until you have it this whole problem stays theoretical.

> **◆ READING** Two companion pieces if this one landed: [the bad address that ships anyway](https://blog.dugong.live/how-to-validate-shipping-addresses-on-shopify.html), on the other field that quietly breaks a delivery, and [the parcel customs sends back](https://blog.dugong.live/how-to-fix-missing-hs-codes-on-shopify-before-customs-holds-your-orders.html), on the customs data that stops a parcel after the label was the easy part.

If you ship internationally from Shopify and have a version of this story, the parcel held in a sorting office for a month, the pickup point order you could not label, the number that was on the billing address the whole time, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Why does my Shopify shipping label fail with “Could not create label”?

Most often because the order has no usable phone number. The error code 030009 is a carrier validation error, usually returned by FedEx, and a missing or malformed recipient phone is the most common trigger. Malformed matters as much as missing: the number needs the country code, and the digit count has to fit the destination country, so a ten digit US number typed into an order going to Germany fails the same way a blank field does. The same family of failures covers a blank first or last name, which FedEx and others reject outright, and an address line over the carrier's character limit, which is 35 for DHL and UPS and 32 for Evri. There is also an origin side worth checking once: some carriers want a valid phone number on your own location under Settings and then Locations, and a blank there fails every label rather than one. The catch-all message, there was a problem buying shipping labels, usually resolves to one of those. The useful habit is to stop treating this as a label problem. It is an order data problem that shows up at the label, which is the latest and most expensive moment to find it.

Permalink: https://blog.dugong.live/how-to-fix-shopify-orders-with-no-phone-number-before-the-label-fails.html#faq-1

### Can I require a phone number at Shopify checkout for international orders only?

Not natively. Shopify's checkout customer information settings have three states for the shipping address phone field, which are do not include, optional and required, and optional is the default on new stores. The help documentation is explicit that these settings apply to every country and market you sell to, and that varying checkout fields by country needs an app that customizes checkout, which is a Shopify Plus capability. Merchants have asked for the per country version repeatedly. In one community thread a reply described a country setting inside checkout form options, and three separate merchants came back to say they could not find it in their own admin, the last of those in October 2024, with a June 2026 reply concluding that an app is the only route. The practical consequence is a choice with no good side: require the field and every domestic checkout pays for a problem that is mostly international, or leave it optional and accept that a share of your international orders arrive without the one field their carrier needs. Most stores pick optional, which is the right call, and then build nothing to cover the gap, which is not.

Permalink: https://blog.dugong.live/how-to-fix-shopify-orders-with-no-phone-number-before-the-label-fails.html#faq-2

### Where does Shopify get the phone number for a shipping label?

From the shipping address on the order, which is not the only place a phone number lives. A Shopify order can carry a phone on the shipping address, a different phone on the billing address, and another on the customer record, because the checkout contact method can be a phone number rather than an email. The label reads the shipping address, so an order can look like it has a phone number in the admin and still fail at the label. This is routine enough that order tagging apps document it as a standard use case: tag the order with the shipping phone when it exists, and fall back to the billing phone when it does not. That fallback is the cheapest fix in this whole article, because the number you are about to email a customer for is often already on the order, one field across. Check the billing address and the customer record before you contact anyone.

Permalink: https://blog.dugong.live/how-to-fix-shopify-orders-with-no-phone-number-before-the-label-fails.html#faq-3

### Why can't I buy a label for a pickup point order without a phone number?

Because pickup point carriers need the number to tell the buyer the parcel has arrived, not just to attempt a delivery, so they refuse the label without it. The sharp version of this is a Shopify native integration failing against a Shopify setting. Merchants shipping with Mondial Relay report that the pickup point flow skips the standard shipping address form, which is the only thing the required phone setting applies to, so the number stays optional no matter what the admin says. Shopify Shipping then refuses the label with the message that a recipient phone number is required for pickup point labels. Worse, pickup point orders cannot be edited, so the number cannot be added afterwards even when the customer sends it. One merchant described support spending over an hour on it and attributing the problem to the carrier, which they disputed since the integration is Shopify's own; another reported buying labels manually on the carrier portal at about 5.99 euro against about 3.30 euro on Shopify's negotiated rate. As of the end of August 2026 the thread records only that the report was forwarded to Shopify's product team, with no fix and no timeline. Until that changes, the only moves are catching it at checkout with a checkout rule, or catching it in the fulfillment queue before anyone tries to buy the label.

Permalink: https://blog.dugong.live/how-to-fix-shopify-orders-with-no-phone-number-before-the-label-fails.html#faq-4

### Does requiring a phone number at Shopify checkout hurt conversion?

Shopify's own defaults suggest it is a real cost rather than a free win. Optional is the default on new stores, and the help documentation frames required as the setting for when your payment provider or shipping carrier needs a phone number, which is the language of a tradeoff rather than a recommendation. Every extra required field at checkout is one more place a shopper can stall, and a phone number is a field many people hesitate over because they assume it means sales calls. That is exactly why merchants keep asking for the per country version: they want the field enforced for the orders that cannot ship without it and left alone for the ones that can. Two things make the tradeoff easier. First, if you sell mostly domestically and your domestic carrier does not need a number, you are buying very little by requiring it everywhere. Second, if one market or one shipping method accounts for most of your failures, a checkout rule scoped to that case, or a plainly worded label on the optional field explaining why international orders need a number, gets you most of the benefit without taxing every checkout.

Permalink: https://blog.dugong.live/how-to-fix-shopify-orders-with-no-phone-number-before-the-label-fails.html#faq-5

### Can AI fix Shopify orders that are missing a phone number?

It can clear most of them before anyone notices, which is the part that is not happening today. Shopify Flow will get you the flag: its conditions read nested fields such as the shipping address, and its empty or does not exist operator is true for a blank or null value, so a workflow can tag an order whose shipping phone is missing. That takes ten minutes and is worth building. What Flow cannot do is everything after the flag. An automation like Dugong checks each order against what its destination and shipping method actually require rather than flagging every blank field, recovers the number from the billing address or the customer record first, and only then asks the customer, once, through a channel they will actually read. When a number comes back it writes it onto the shipping address, where the label reads it, instead of leaving it in a support thread. It holds the affected order rather than the whole batch, so the warehouse never buys a label that was going to fail. And it reports the weekly miss count by country and shipping method, which is the number that tells you whether a checkout rule is worth the conversion it costs. The honest limits: it cannot invent a number that exists nowhere on the order, it cannot make a customer reply, and it cannot edit a pickup point order that Shopify will not let anyone edit. For that last case the only winning move is upstream, at checkout.

Permalink: https://blog.dugong.live/how-to-fix-shopify-orders-with-no-phone-number-before-the-label-fails.html#faq-6

---

## Read next

- [The bad address that ships anyway](https://blog.dugong.live/how-to-validate-shipping-addresses-on-shopify.html): Shopify warns about a bad address, you ship anyway, and the package bounces back. The AI playbook that catches undeliverable addresses before the label prints.
- [The parcel customs sends back](https://blog.dugong.live/how-to-fix-missing-hs-codes-on-shopify-before-customs-holds-your-orders.html): De minimis is gone and every parcel needs the HS codes your catalog never carried. The AI playbook that classifies products before customs bills your customer.
- [The parcel that comes back to you](https://blog.dugong.live/how-to-handle-return-to-sender-orders-on-shopify.html): Shopify has no status that means coming back to you, so the order still says fulfilled while the box sits behind the printer. The AI playbook that catches every return to sender the same hour.
