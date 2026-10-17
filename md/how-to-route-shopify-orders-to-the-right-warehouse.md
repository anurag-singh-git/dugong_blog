# How to stop Shopify routing orders to the wrong warehouse

> Shopify picks a location by straight-line distance and never reads a shipping rate. The AI playbook that routes each order on landed cost, cutoff, and backlog.

- Canonical: https://blog.dugong.live/how-to-route-shopify-orders-to-the-right-warehouse.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-07-27
- Updated: 2026-08-15
- Section: Research
- Word count: 2450
- Dispatch: Nº 93 · Research · 10 min read
- Full headline on page: How to stop Shopify routing orders to the *wrong warehouse*
- Keywords: Shopify order routing, Shopify wrong fulfillment location, Shopify multi location fulfillment, Shopify ship from closest location, Shopify split shipment two locations, Shopify move fulfillment order, Shopify 3PL routing, Shopify order routing rules
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

An order comes in from New Jersey. Three items. Two of them sit in your Pennsylvania warehouse, an easy overnight run. The third is only in the Nevada 3PL. Shopify looks at the order, sees that no single location holds all three, splits it, and now you are paying for two shipments against one flat rate the customer paid once, and one of those shipments crosses the country to deliver a twelve dollar item. On Thursday the customer emails to ask where the rest of their order is, because they got one box and one tracking number and nobody told them there was a second.

The quieter version costs more over a year and never generates a ticket. A Friday evening order routes to the retail location eleven miles from the customer, which is the closest pin on the map and also a shop with two people on the floor that does not ship on weekends. It goes out Monday afternoon. Your warehouse two states away would have had it on a truck that night. Nothing failed. No alert fired. The order simply took three extra days and one of your store's units, which a walk-in would have bought at full margin with no shipping cost at all.

## What Shopify actually does, and where it stops

Credit first, because Shopify's routing is much better than the old fulfillment priority list it replaced. Under Settings, Shipping and delivery, Order routing, you get a strategy: a list of rules that run top to bottom, each one filtering the locations the next rule gets to see. The default is three rules in this order. Minimize split fulfillments, which prefers any location holding every item. Stay within the destination market. Ship from the closest location. You can reorder them, remove them, and add two more: ranked locations, where you group locations into tiers you define, and location [metafields](https://help.shopify.com/en/manual/custom-data/metafields), where you prioritize on a boolean or a number you have stored against each location.

That is a real routing engine and for a lot of stores the defaults are fine. The trouble starts with what none of those rules can read. **Not one of them looks at a shipping rate.** There is no rule for cheapest label, no rule for carrier zone, no rule for dimensional weight, no rule for the pick fee your 3PL charges that your own warehouse does not. Closest is measured as straight-line distance, and Shopify's own documentation is upfront that this is not driving distance, so the location that wins on the map regularly loses on the truck. Near a zone boundary, across a bay, or on the wrong side of a border, the nearest pin and the cheapest label are different answers.

Nothing in the ranking knows what time it is either. There is no concept of a cutoff, a weekend, a public holiday, or a warehouse that is two days behind because half the team has flu. The one capacity signal available is a location metafield, which means a number or a checkbox that a person types and then never touches again, and which will still say `has_capacity: true` on the Tuesday your 3PL stops answering the phone. It is the same failure mode as [a reorder point typed once](https://blog.dugong.live/how-to-set-inventory-reorder-points-on-shopify.html) against a catalog that moves every week.

> One ranking, applied identically to every order you will ever take. The cheapest way to ship an order changes with the order.

The split decision has the same shape. Put Minimize split fulfillments at the top and you have said, once and forever, that one box is always better, even when that box goes coast to coast to save a second label that would have traveled one zone. Take it out and you have said two boxes are fine, including on the order where the second box holds a four dollar accessory. Both answers are right some of the time. Shopify gives you one lever and asks you to hold it in one position through Black Friday and through July.

And routing happens once, at the moment the order is created. If the count at that location turns out to be wrong, if the store closes early, if the cutoff passes while the order sits in review, nothing goes back and reconsiders. The assignment is a decision made with the information available in the half second after checkout, and it is never revisited.

There is an escape hatch, and it is worth knowing it is closed for most people. Custom routing rules are real, they are implemented as [Shopify Functions](https://shopify.dev/docs/apps/build/functions) through the Order Routing Location Rule API, and they can do genuinely clever things. They are also Shopify Plus, by request, in early access, and they require you to be enrolled in the Partners program and deploy your own app. That is a fine answer for an enterprise team with engineers. It is not an answer for the store doing four hundred orders a day out of a warehouse and two showrooms.

## Why Flow gets close and then stops

[Shopify Flow](https://help.shopify.com/en/manual/shopify-flow) has a Move fulfillment order action, and it is more useful than people realize. If you already know the rule, Flow will run it: send anything over twenty kilos to the location with the pallet racking, keep engraved items at the workshop, push wholesale orders to the bulk site. That is genuine value and if you are moving those by hand today, build it this afternoon.

Two walls sit right behind it. The first is that the destination has to stock every line item in the fulfillment order or the run fails, which rules out precisely the mixed-basket orders that route badly in the first place. The second is timing. You cannot move a fulfillment order once a fulfillment service has the request in a submitted or accepted state, which is to say, once your 3PL actually has it. The window in which the fix is possible is the window before anyone notices there is something to fix.

Underneath both is the familiar limit. Flow evaluates static conditions on one order at a time. It cannot ask which of three labels is cheapest, or whether Columbus can still hit today's cutoff, or whether Reno is running a day behind, because those are questions about the world outside the order record. Flow can execute a routing decision. It cannot make one. That is the same structural wall behind [splitting an order across vendors](https://blog.dugong.live/how-to-automatically-split-and-route-shopify-orders-to-multiple-suppliers.html), which is this problem again with somebody else's warehouse.

## Why doing it by hand never keeps up

The manual version is a person on the fulfillment team scanning the morning's orders for ones that look wrong. They spot the Nevada split, pull up two rate quotes in the carrier account, message the warehouse to ask if it can still go out today, move the fulfillment order, and move on to the next. It works, and at thirty orders a day it is genuinely the right call. At three hundred it is arithmetic nobody has time for, so the only orders that get checked are the ones a customer already complained about, which means you are paying the cost and doing the work.

What makes it invisible is that Shopify has no report for this. There is nowhere in the admin that tells you what your routing cost last month against the best assignment available at the time. The loss does not arrive as an incident. It arrives as a shipping line that runs a bit higher than budget every month, spread across thousands of orders that each cost two or three dollars more than they had to, plus the split shipments that quietly generate [where is my order tickets](https://blog.dugong.live/how-to-reduce-where-is-my-order-wismo-tickets-on-shopify.html) because the customer got one box and no explanation.

And it degrades exactly when it matters. In peak, every location is backed up differently, stock is moving faster than counts can keep up, and the one static ranking you set in February is making four hundred decisions an hour on information from five months ago.

## What the automation actually has to do

The working version is not a better rule list. It is something that does, per order, the arithmetic a good fulfillment lead does in their head and only has time to do for the handful they notice. As a Dugong playbook, in plain prose, it looks like this:

```
# trigger
On order created, and again whenever anything
changes before a label is bought

# steps
1. Score every location that could send this order:
   real rate, carrier zone, cutoff, backlog, stock
   health
2. Decide split or single for this order, on landed
   cost and promised date, not one global setting
3. Respect what is not negotiable: oversized, hazmat,
   market, personalization, shop floor stock
4. Move the fulfillment order inside the window,
   before a fulfillment service accepts it
5. Re-check when reality moves: bad count, closed
   location, missed cutoff, storm
6. Tell the customer once, in one message, when an
   order genuinely does ship in two boxes
```

Step one is where the money is. For a given order, the eligible locations are usually two or three, and ranking them properly takes information Shopify's rules do not have: the actual rate for this weight and these dimensions to this zip from each origin, whether each location can still get it out today given its cutoff and its current queue, and what pulling this unit does to the location it leaves. Straight-line distance is a rough proxy for the first of those and blind to the other two.

Step two is the one that is impossible to express as a setting. The question is not do we allow splits. It is, for this order, does one shipment or two cost less all-in and land sooner. Two zone-two parcels frequently beat one zone-eight parcel, and just as frequently do not. It depends on weight distribution, the carrier contract, the dimensional rounding, and whether the customer chose express. That is a calculation, run per order, in the seconds between checkout and the warehouse queue. It is not a checkbox.

> **◆ NOTE** The trap is **treating the routing strategy as a setup task**. It gets configured in week one, when you have two locations and a rough idea of your carrier rates, and then it keeps making every decision for the next three years through a 3PL migration, a new market, a peak season, and a carrier contract renegotiation. Nothing in the admin ever tells you it has drifted out of date, because from Shopify's point of view it is working perfectly. It is applying your rules exactly as written.

## Why this is a compiler problem, not an app problem

Every question in this workflow depends on context that cannot be pre-ranked. Is the cheapest label worth an extra day here. Is this customer's second order this week, so should it wait an hour and go out with the first, the way [combined orders](https://blog.dugong.live/how-to-combine-multiple-orders-from-the-same-customer-on-shopify.html) do. Is this address even deliverable, which is a question for [address validation](https://blog.dugong.live/how-to-validate-shipping-addresses-on-shopify.html) before you commit a location to it. Is the stock at that location actually there, or is it the phantom count that causes [overselling across channels](https://blog.dugong.live/how-to-prevent-overselling-on-shopify-across-channels.html). Those answers depend on your margins, your season, your carrier contract, and how patient that particular customer is, and they move week to week.

Picture an outdoor gear brand with a 3PL in Reno, an owned warehouse in Columbus, and two showrooms. A Chicago customer orders a tent, a stove, and a set of pegs. Reno has all three, Columbus has two of them, the showroom nine miles away has the pegs. With the default strategy, Minimize split fulfillments hands the whole order to Reno and it travels sixteen hundred miles. With the playbook running, the two heavy items go from Columbus, which is one zone away and inside cutoff, the pegs are checked against the showroom and left there because that store sells four sets a week at full margin, so they come from Columbus too. One shipment, one zone, out tonight, about nine dollars cheaper, and the showroom keeps its stock. On the order where the arithmetic goes the other way, it splits, and the customer gets one email explaining both tracking numbers instead of [wondering where the rest of it is](https://blog.dugong.live/how-to-notify-customers-of-shipping-delays-on-shopify.html).

It also sits directly downstream of the numbers you feed the platform. Routing is only as good as your location-level counts, which is why [a supplier feed that lands wrong](https://blog.dugong.live/how-to-sync-supplier-inventory-feeds-to-shopify.html) shows up here as an order assigned to a warehouse that cannot actually pick it, and why a routing decision that assumed stock which does not exist ends up as [an order edited after the fact](https://blog.dugong.live/how-to-edit-a-shopify-order-after-its-been-placed.html).

## The workflow worth building this week

Start with the audit, not the automation, because you almost certainly do not know the size of this. Export last month's orders with the location each one shipped from, and for each order compute what the best eligible location would have cost. Two hundred orders is enough to see the shape. Most multi-location stores find the gap is somewhere between two and six dollars an order, concentrated in a handful of patterns that repeat: one lane, one product that only lives in the far warehouse, one showroom that keeps getting picked because it is close.

Then build the guardrail before the optimizer. A watcher that does nothing but flag orders where the assigned location is materially worse than the best alternative, and move them while the move is still allowed, captures most of the value with none of the risk. That is the same compounding logic behind [the Shopify automations no one builds](https://blog.dugong.live/best-shopify-automations-to-set-up.html): the boring guardrail earns more than the clever feature.

Describe it the way you would brief a new fulfillment lead on their first morning. For every order, look at which of our locations could actually send it, price the realistic options including the split, and pick the one that costs least without missing the delivery date we promised. Do not take the last unit off a shop floor for a twelve dollar accessory. Do not send anything to a location that cannot ship it today when one that can is a dollar more. Move it before the warehouse picks it, not after. If reality changes before the label prints, think again. And if an order truly has to go in two boxes, tell the customer once, properly, with both tracking numbers. That is the brief. The compiler handles the rates, the cutoffs, the fulfillment order mechanics, and the timing window, and your shipping line stops quietly absorbing a decision made in February.

> **◆ READING** If this resonates, two companion pieces: our dispatch on [the order you split across vendors by hand](https://blog.dugong.live/how-to-automatically-split-and-route-shopify-orders-to-multiple-suppliers.html), which is this problem when the warehouses belong to somebody else, and [the overselling problem no one automates](https://blog.dugong.live/how-to-prevent-overselling-on-shopify-across-channels.html), which is what happens when the count the router trusted was never true. Also worth reading: [the shipping rate that ignores your box](https://blog.dugong.live/how-to-fix-shopify-shipping-rates-that-ignore-product-dimensions.html), on what the label actually costs once the carrier measures the parcel you packed.

If you are a Shopify merchant running two or more locations, with a routing story, a spreadsheet where you check rates by hand, or a 3PL that keeps getting orders it should never have seen, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Why does Shopify ship from a far warehouse when a closer location has the item?

Usually because a rule above the distance rule already made the decision. Shopify's default routing strategy runs Minimize split fulfillments first, then Stay within the destination market, then Ship from closest location, and each rule filters the list the next one sees. A far location that stocks every line in the order outranks a near one that stocks three lines out of four, because the first rule has already eliminated the near one. Four other things send orders the long way. The closest location may have the option to fulfill online orders switched off. Its stock may exist but be committed to earlier orders. It may not be in the shipping profile that produced the rate the customer paid. And closest is measured as straight-line distance, which Shopify's own documentation says is not driving distance, so a location across a bay or a mountain range can win on the map and lose on the truck.

Permalink: https://blog.dugong.live/how-to-route-shopify-orders-to-the-right-warehouse.html#faq-1

### Can Shopify Flow change the fulfillment location of an order?

Partly. Flow has a Move fulfillment order action, and it works well for rules you already know, such as sending every order over a certain weight to the warehouse that stocks pallets. It has two hard limits. The destination has to stock every line item in that fulfillment order or the run fails outright, which rules out most of the interesting cases. And you cannot move a fulfillment order once a fulfillment service has the request in a submitted or accepted state, which is exactly the moment your 3PL already has it and the mistake is about to cost money. Flow also cannot compare carrier rates, measure driving distance, check a cutoff time, or ask whether a location is running behind today, so it can execute a routing decision but it cannot make one.

Permalink: https://blog.dugong.live/how-to-route-shopify-orders-to-the-right-warehouse.html#faq-2

### How do I stop Shopify splitting one order into two shipments?

Put the Minimize split fulfillments rule at the top of your order routing strategy in Settings, Shipping and delivery, Order routing. That tells Shopify to prefer any single location holding the whole order over a closer location holding part of it. The catch is that you have now answered the question once for every order you will ever take. Sometimes one box crossing the country costs more than two boxes traveling one zone each, and sometimes the customer would rather have two thirds of the order tomorrow than all of it on Friday. Shopify gives you one lever for a decision that has a different right answer depending on weight, zone, margin, and how badly that customer needs the item. Splitting is not the problem. Splitting without doing the arithmetic is.

Permalink: https://blog.dugong.live/how-to-route-shopify-orders-to-the-right-warehouse.html#faq-3

### Can Shopify order routing choose the cheapest shipping rate?

No. None of the available routing rules reads a shipping rate: there is no rule for cheapest label, carrier zone, dimensional weight, or the pick fee your 3PL charges that your own warehouse does not. Ship from closest location measures straight-line distance, and Shopify's own documentation is upfront that this is not driving distance, so near a zone boundary or across a bay the nearest pin and the cheapest label are different answers. The escape hatch exists but is closed to most stores: custom routing rules are implemented as Shopify Functions through the Order Routing Location Rule API, and they require Shopify Plus, early access by request, Partners enrollment, and deploying your own app. For everyone else, cost-aware routing means scoring the eligible locations per order on the real rate, the cutoff, and the backlog, then moving the fulfillment order inside the window, before a fulfillment service accepts it.

Permalink: https://blog.dugong.live/how-to-route-shopify-orders-to-the-right-warehouse.html#faq-4

### How much does wrong warehouse routing cost a Shopify store?

Usually two to six dollars an order, and it is invisible because Shopify has no report for it. Nothing in the admin compares what your routing cost last month against the best assignment available at the time, so the loss never arrives as an incident. It arrives as a shipping line that runs a bit over budget every month, plus split shipments that quietly generate where is my order tickets because the customer got one box and no explanation. The way to size it is an audit: export last month's orders with the location each one shipped from, and for each order compute what the best eligible location would have cost. Two hundred orders is enough to see the shape. Most multi-location stores find the gap concentrated in a handful of repeating patterns: one lane, one product that only lives in the far warehouse, one showroom that keeps getting picked because it is close on the map.

Permalink: https://blog.dugong.live/how-to-route-shopify-orders-to-the-right-warehouse.html#faq-5

---

Markdown rendition of https://blog.dugong.live/how-to-route-shopify-orders-to-the-right-warehouse.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
