# How to spot serial returners on Shopify before you refund them again

> Shopify will tell you this return is hers. It will not tell you it is her seventh. The number that decides this refund is not on the order page.

- Canonical: https://blog.dugong.live/how-to-spot-serial-returners-on-shopify.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-11-17
- Section: Research
- Word count: 2525
- Dispatch: Nº 142 · Research · 9 min read
- Full headline on page: How to spot *serial returners* on Shopify before you refund them again
- Keywords: shopify serial returners, shopify return abuse, shopify return fraud detection, customer return rate shopify, shopify flow return abuser, shopify returns report by customer, wardrobing detection shopify, AI return abuse scoring
- Entities: Shopify (https://www.wikidata.org/wiki/Q7501150); Product return (https://www.wikidata.org/wiki/Q166778); Chargeback (https://www.wikidata.org/wiki/Q3307525); Business process automation (https://www.wikidata.org/wiki/Q5001911)
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

A return request lands on a Tuesday. Order 4417, two of the three items, reason given as not as described. You approve it, because it is a forty dollar refund and the customer has bought from you more than once.

What the order page does not say is that she has ordered nine times and sent back seven. Her lifetime spend still reads like a good customer. Her lifetime margin went negative in March.

Shopify will show you this return. It will not show you the other six, not on the order page, not on the customer page, not in any report you can filter. The number that should decide this refund exists in your data and nothing in the admin will put it in front of you.

## The short answer

Shopify's fraud tooling runs before the sale. The risk indicator scores an order for stolen card risk, the Fraud Filter app merchants used for rules was retired at the end of January 2025, and Shopify Protect covers chargebacks. Nothing native watches what happens after the refund button.

So return abuse is invisible by construction. There is no per customer return rate in the admin, and the store level returns figure in your own analytics counts pre-shipment size swaps as returns, which means it is wrong in the direction that flatters nobody.

The fix is one number per customer, kept current: value returned over value bought, with exchanges stripped out, read next to the timing and the wording of each request. That number is cheap to compute and it changes what you do next, which is the only test that matters.

## Shopify scores the sale and goes quiet after it

Shopify's built in fraud analysis marks an order low, medium or high risk. It is looking for a stolen card: billing and shipping that do not match, checkout behavior that looks automated, the signals that predict a chargeback. It runs once, at the moment of the sale, and it never looks again.

The app merchants used to write their own rules, Fraud Filter, was retired on 31 January 2025, with Shopify pointing merchants at Flow instead. Shopify Protect, the other piece people reach for, covers chargebacks on Shop Pay orders. Useful, and not this problem.

A merchant put the gap in one line in an April 2026 community reply: Fraud Filter only ever covered pre-purchase risk. Everything on the reverse side of the order, the part where the money actually leaves, has no native surface at all. Not a report, not a segment, not a flag.

The customer page is the clearest illustration. It carries orders placed and amount spent. It does not carry value returned. And customer segments, which will happily filter on order count and lifetime spend, have nothing for return behavior, so the one segment you want here is the one you cannot build. Which also means the usual answer, ban them, [does not work the way people think it does](https://blog.dugong.live/how-to-block-a-customer-on-shopify.html).

## The returns number in your own analytics is not returns

Before you build anything on top of Shopify's returns data, know what is in it.

In June 2026 the founder of an apparel brand [reported that the Analytics Returns metric counts every refund event](https://community.shopify.com/t/returns-metric-in-analytics-is-misleading-should-reflect-actual-returns-not-all-refund-events/637409), pre-shipment order edits for size adjustments included. His reported return rate was about 25 percent. His actual rate was about 3 percent. In one seven day stretch he had zero physical returns and Shopify reported minus 572 dollars, all of it size swaps made before anything shipped.

Shopify did split the metric in March 2026, into sales reversal and quantity returned. He called that a rename rather than a fix, and gave his reasons: the Returns over time report still used the old field, with a deprecation warning telling you to replace `returns` with `sales_reversals`, and the new figure still bundled edits, swaps, cancellations and physical returns into one line. Another member called it a legitimate analytics gap and said plainly that edits and returns are fundamentally different events.

This matters more than it looks. If you compute a per customer return rate from that field, it inherits the same error, and it inherits it hardest at the stores with the most generous exchange policy. In other words, exactly the stores with a return problem will get the least trustworthy number, and the first names at the top of their list will be loyal customers who swapped a size before dispatch.

## What the community built, and where it broke

The useful record here is not a help page. It is two and a half years of merchants converging on the same calculation in public.

It starts in March 2024, when a merchant [asked for a Flow notification](https://community.shopify.com/t/how-to-detect-a-potential-return-abuser-in-customer-orders/301424) on customers with three or more orders and net sales under 150 dollars, the shape of a serial returner. Shopify Support had already told them Flow cannot check all order history.

A reply gave two routes. The quick one reads `order.customer.numberOfOrders` and `amountSpent.amount` off the triggering order, with the catch that both include the order that just fired the workflow, so a return can push a customer over your threshold on its own. The real one uses [Get order data](https://help.shopify.com/en/manual/shopify-flow/reference/actions/get-order-data) in advanced mode, capped at 100 orders, querying the customer id with a return status of return requested, in progress or returned, and notifying when the count is above zero.

Within a week someone raised the flaw. Customers return some items from a multi-item order, so counting returned orders is not counting returned items. Fixing that needed the Run Code step and a loop summing return line item quantities.

In November 2024 a Shopify Plus merchant [built exactly that](https://community.shopify.com/t/shopify-flow-to-calculate-return-abusers/374798): units returned over the last 100 orders, units bought, a percentage, a tag on the customer. Their nested loop was wrong and the log output showed no counts. Another member fixed the loop. The merchant then abandoned units altogether and moved to refund dollars over gross sales, which is the more honest denominator. Their own framing is the line worth keeping: about 20 percent of some of their products are faulty, so refunds are routine, and separately some customers return 60 to 70 percent of what they buy. Those are two different problems that look identical in a count.

By October 2026 the thread had arrived at the refinement that makes it usable: compare refunded amount against total spend, and alert only when refunds exceed a chosen share, something like 40 percent, across three or more orders. That floor is what stops a single size exchange from triggering the whole machine.

Read that arc as a specification, because it is one. Dollars, not units. A ratio, not a count. A floor on order count. Exchanges excluded. Every store that needs this is rebuilding it by hand, in Run Code, from scratch.

## Four signals that separate abuse from a sizing problem

A 2026 community post [lays out the manual version](https://community.shopify.com/t/tips-for-identifying-serial-return-abuse-on-your-store/607321), and its signals are better than most vendor material.

**The ratio, with a floor.** Export returns for six months, sort by customer email, look closely at anyone above three returns, and treat a return to order ratio above 50 percent over 90 days as worth investigating. Use value rather than counts, and require enough orders that the percentage means something, or the top of your list will be people who ordered twice.

**The timing.** Requests filed one to three days after delivery, with a vague reason, are the classic wardrobing shape. There is a sharper version of the same tell: returns filed on a Monday or Tuesday against orders delivered the previous Thursday or Friday. That is a weekend with your product and an event that is now over.

**The story that changes.** One reason repeated across many customers is a product problem. Four different reasons from one customer, wrong size then not as described then damaged then changed my mind, is a person working out which one gets approved fastest.

**The double dip.** Cross reference returns against chargebacks for the same period. If a customer was refunded through the return and also won a chargeback on the same order, they were refunded twice, and that is not a pattern to monitor. That is money to go and [get back](https://blog.dugong.live/how-to-win-chargeback-disputes-on-shopify.html).

One control belongs next to all four. A product returning at roughly three times the rate of similar products is a listing problem, not a customer problem. Reshoot the photo, fix the size chart, rewrite the description. The post's own caveat applies to the rest of it: none of this is foolproof.

## What this costs on an ordinary month

The [2025 Retail Returns Landscape from NRF and Happy Returns](https://nrf.com/media-center/press-releases/consumers-expected-to-return-nearly-850-billion-in-merchandise-in-2025) puts total US returns at 849.9 billion dollars, 15.8 percent of annual sales, with an estimated 19.3 percent of online sales coming back and 9 percent of all returns fraudulent.

Put your own store through that. Fourteen hundred orders a month at a sixty two dollar average is about 86,800 dollars. At 19 percent, roughly 16,500 dollars comes back. Nine percent of that is about 1,480 dollars a month in refunds you should never have paid, before you count the outbound shipping you do not recover, the return label, the pick, the pack, the inspection, and the share of goods that cannot be resold at full price.

Call the real number somewhere between one and two thousand dollars a month. The amount is not the interesting part. The interesting part is that it is concentrated in about a dozen customers.

That concentration is the whole argument for automating this rather than legislating it. Tighten the returns policy for everyone and you charge fourteen hundred customers in conversion and goodwill to recover money from twelve. A per customer score lets you act on the twelve and leave the rest of the store alone.

## What Shopify Flow gets you, and where it stops

Flow does real work here and you should go and build it this week. Get order data in advanced mode will pull a customer's orders filtered on return status. [Conditions](https://help.shopify.com/en/manual/shopify-flow/reference/conditions) read nested fields. Run Code will loop the returns and sum quantities or refunded amounts. Tag the customer, post to a channel, done in an afternoon.

Then it stops, in four specific places.

Get order data returns at most 100 orders per query, so for a long standing customer you are scoring a sample, and Support's own line to that first merchant was that Flow cannot check all order history. The customer fields on an order created trigger include the triggering order, so your thresholds move underneath you. Flow is event driven, so it reacts to one return at a time and nothing ever hands you the worst twelve customers this month. And Flow reads fields, not sentences: it can match a string in a return reason, but it cannot tell whether six short notes from one person are one complaint or six excuses.

That last one is the whole problem. The counting was never the hard part.

## What the automation actually has to do

As a Dugong playbook, in plain prose:

```
# trigger
Return requested or refund created,
plus a weekly pass over customers

# steps
1. Score the customer, not the
   order
2. Separate an exchange from a
   return
3. Read the timing and the reason
   text
4. Cross check the refunds against
   the chargebacks
5. Change the offer, not the
   welcome
6. Tell fulfillment before the
   pick
7. Report the top of the list
   weekly
```

Step one is value returned over value bought, across the customer's whole history rather than their last hundred orders, with a floor on order count so the list means something. The output is a ranking, not a flag. You want twelve names, not a warning icon on four hundred orders that your team learns to scroll past.

Step two decides whether anyone trusts the number. A size swap made before dispatch is not a return, and Shopify's own metric bundles the two. Separate exchanges, order edits and cancellations from physical returns before you divide, or the first thing you will hand your support lead is a list of your best customers.

Step three is the part that was not practical before and is ordinary now. Days from delivery to request, the day of week pair, and whether the reason text tells the same story each time. Reading six short notes from one person and saying whether they cohere is a judgment, and it is the judgment that separates a sizing problem from a pattern.

Step four is refunds beside chargebacks for the same window. It is the highest value row on the whole list, because it is the one case where the right response is not a policy change but a recovery.

Step five is where most teams overreact. The answer is almost never a ban. Move that customer's future orders to manual payment capture so somebody reviews them before they ship. Offer store credit instead of a card refund. Withdraw free return shipping for that segment. Cap items per order where bracketing is the pattern. Each of those is reversible, each survives the customer asking why, and none of them needs you to be certain about intent.

Step six is the cheapest win and the one nobody wires up. When a flagged customer's order is picked, the pack gets photographed, the serial or tag recorded, a tamper seal added. Wardrobing dies on evidence, and the evidence has to be collected while the box is still open, which means fulfillment has to know at pick time rather than at refund time.

Step seven is one weekly list: top customers by value returned, their ratio, the direction it is moving, and what you did about them last time. Next to it, separately, the products returning at three times their category. One of those lists is a conversation with a customer. The other is a photographer.

## Do this before you close the laptop

Three things, about twenty minutes, no tooling required.

Export the last ninety days of orders, pivot refunded amount by customer email, sort descending. Read the top ten rows. Most merchants have never looked at that list and are surprised by how short it is.

Then take the top three names and read their return reasons in order, oldest first. If the story changes every time, you have your answer before you automate anything.

Last, check those same three names against your chargeback list in Payments. That cross reference takes two minutes and occasionally finds money.

> **◆ READING** Two companion pieces if this one landed: [the refund you gave for nothing](https://blog.dugong.live/how-to-handle-shopify-returns-the-customer-never-sends-back.html), on the returns that get approved and never arrive, and [the return that never goes back on the shelf](https://blog.dugong.live/how-to-automatically-restock-returns-on-shopify.html), on what happens to the stock after the box does come back.

If you run a store with a version of this story, the customer whose returns finally outran their orders, the weekend wardrobing you only spotted by the delivery dates, the refund that turned up next to a won chargeback, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### How do I find serial returners on Shopify?

There is no report for it, so you build the number yourself. The manual version takes about twenty minutes: export the last ninety days of orders, pivot refunded amount by customer email, and sort descending. The top ten rows are usually the whole problem, which is the detail that surprises merchants most. One community post sets out the same approach with thresholds: export returns for the last six months, sort by customer email, look closely at anyone with more than three returns, and treat a return rate above 50 percent as worth investigating. Two refinements matter before you act on the list. Use value rather than counts, because a customer returning one cheap item from every order is a different problem from one returning the expensive half of every order. And put a floor on order count, or a customer who ordered twice and returned once will sit at the top of your list at 50 percent and tell you nothing. The author of that community post adds the honest caveat: none of this is foolproof. It is a shortlist to read, not a verdict to enforce.

Permalink: https://blog.dugong.live/how-to-spot-serial-returners-on-shopify.html#faq-1

### Does Shopify have a return rate report per customer?

No. Shopify's admin will show you an individual return on an order, and it will show you store level returns in Analytics, but there is nothing between the two. The customer page carries orders placed and amount spent, not value returned, and there is no segment filter for return behavior, so you cannot build a serial returner segment the way you can build a repeat buyer segment. That gap is why the community keeps rebuilding the same calculation by hand in Shopify Flow's Run Code step. It also explains a pattern worth noticing: return abuse is not usually a tolerated cost at these stores, it is an unmeasured one. Merchants who finally run the export are commonly looking at a dozen customers and a four figure monthly number they had never seen in any dashboard, because no dashboard in the admin computes it.

Permalink: https://blog.dugong.live/how-to-spot-serial-returners-on-shopify.html#faq-2

### Why is my Shopify return rate so high in Analytics?

Probably because the metric is not counting what you think it is counting. In June 2026 the founder of an apparel brand reported that Shopify's Returns metric counts every refund event, including pre-shipment order edits for size adjustments, and that this put his reported return rate at about 25 percent against an actual rate of about 3 percent. In one seven day stretch he had zero physical returns and Shopify reported minus 572 dollars, all of it pre-shipment size swaps. Shopify split the metric in March 2026 into sales reversal and quantity returned, but he described that as a rename rather than a fix, noting that the Returns over time report still used the old field with a deprecation warning telling you to replace returns with sales reversals, and that the new figure still bundled edits, swaps, cancellations and physical returns together. Another member called it a legitimate analytics gap and said edits and returns are fundamentally different events. The practical consequence: if you intend to compute a per customer return rate from the same field, it will be wrong in the same direction, and it will be most wrong at exactly the stores with generous exchange policies. Separate exchanges, edits and cancellations from physical returns before you divide anything.

Permalink: https://blog.dugong.live/how-to-spot-serial-returners-on-shopify.html#faq-3

### Can Shopify Flow detect return abuse?

Partly, and it is worth building, but it will not finish the job. Flow's Get order data action in advanced mode can query a customer's orders filtered on return status, which merchants have used with a query on the customer id plus a return status of return requested, in progress or returned, and then notified when the count is above zero. Its conditions read nested fields, and its Run Code step can loop through returns and sum either returned quantities or refunded amounts. Four limits show up quickly in the community threads. Get order data returns at most 100 orders per query, so for a long standing customer that is a sample rather than a history. The customer fields available on an order created trigger, number of orders and amount spent, include the order that triggered the workflow, so thresholds drift. Flow is event driven, so nothing walks your customer list and hands you the worst twelve names this month. And Flow reads fields, not sentences, so it cannot tell whether a customer's six return reasons are one complaint or six different excuses. The original poster in one of those threads was told by Shopify Support that Flow cannot check all order history, which is the honest summary.

Permalink: https://blog.dugong.live/how-to-spot-serial-returners-on-shopify.html#faq-4

### Should I block a customer who returns too much on Shopify?

Usually not, for two reasons. The first is practical: blocking is weak on Shopify, since a block is tied to an email, and a new email and a new address defeat it in about a minute. The second is commercial: a customer who returns 60 percent of what they buy may still keep several hundred dollars a year, and banning them trades real revenue for a feeling of resolution. The better move, and the one merchants in the community threads actually recommend, is to change the offer rather than the welcome. Move that customer's future orders to manual payment capture so somebody reviews them before they ship. Offer store credit instead of a card refund. Withdraw free return shipping for that segment. Cap items per order where bracketing is the pattern. Each of those is reversible, each is defensible if the customer asks, and none of them requires you to be certain about intent. Save outright blocking for the cases where the refund and a won chargeback have landed on the same order, which is not a behavior pattern to manage but money to go and recover.

Permalink: https://blog.dugong.live/how-to-spot-serial-returners-on-shopify.html#faq-5

### Can AI detect return abuse on Shopify?

Yes, and this is one of the cleaner cases for it, because the hard part of the problem is reading rather than counting. Counting is the part Flow already half does. Reading is what has been missing: deciding whether this customer's returns are one product complaint or a changing story, which is the single signal that separates a sizing problem from a person. An automation like Dugong scores each customer on value returned over value bought across their whole order history rather than the last 100 orders, separates pre-shipment edits, exchanges and cancellations from physical returns before dividing, reads the delivery to request interval and the reason text together, and cross references refunds against chargebacks for the same window. It then acts proportionately: manual capture and store credit for the top of the list rather than a ban, and a note to fulfillment before the pick, so a flagged customer's order is photographed and serialised while the box is still open. That last step is the one that actually ends wardrobing, because the evidence has to exist before the parcel leaves. The honest limits: it cannot prove intent, it cannot stop a determined abuser from opening a new account, and it will put the occasional unlucky customer near the top of a list, which is exactly why the response at the top of the list should be a review and not a ban.

Permalink: https://blog.dugong.live/how-to-spot-serial-returners-on-shopify.html#faq-6

---

## Read next

- [The refund you gave for nothing](https://blog.dugong.live/how-to-handle-shopify-returns-the-customer-never-sends-back.html): Shopify has seven return triggers and none fire when nothing happens. The AI playbook that chases a quiet return, holds the money, and closes it honestly.
- [The chargeback you lose by default](https://blog.dugong.live/how-to-win-chargeback-disputes-on-shopify.html): Shopify auto-submits a thin chargeback response and the clock runs out, so you lose winnable disputes. The AI playbook that builds the evidence and files it.
- [The return that won't approve itself](https://blog.dugong.live/how-to-automate-returns-and-exchanges-on-shopify.html): Shopify makes you approve every return by hand and won't run a true exchange, so refunds leak revenue you already earned. The AI playbook that automates it.
