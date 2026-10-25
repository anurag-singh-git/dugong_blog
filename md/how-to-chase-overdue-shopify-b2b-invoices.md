# How to chase overdue Shopify B2B invoices by company

> Four unpaid invoices from one account means four reminder emails and no single number. Overdue is not a status in Shopify, and there is no company balance to read.

- Canonical: https://blog.dugong.live/how-to-chase-overdue-shopify-b2b-invoices.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-10-25
- Section: Research
- Word count: 2967
- Dispatch: Nº 136 · Research · 11 min read
- Full headline on page: How to chase overdue Shopify B2B invoices *without emailing one order at a time*
- Keywords: shopify b2b overdue invoices, shopify net 30 payment terms, shopify payment reminders, shopify b2b unpaid orders, shopify company balance, shopify overdue order status, shopify flow payment schedule is due, AI accounts receivable automation
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

A trade account places a net 30 order on the first of the month. Shopify marks it payment pending and moves on.

Day 31 arrives. The order picks up an Overdue badge in your admin. Nothing else happens.

By the middle of the next month that one account has four open orders on the same terms, three of them past due, and your reminder settings have sent four separate emails about four separate order numbers to one person who has never once been shown the total.

Nobody on your side knows what that company owes you either. Not because nobody looked. Because there is nowhere to look.

## The short answer

Overdue is not a status you can query. The order financial status enum in the Admin API has eight values: pending, authorized, partially paid, paid, partially refunded, refunded, voided and expired. Overdue is not one of them. The badge in the admin is worked out from a due date that has gone past with a balance still open, so the thing you want to automate on is the absence of an event rather than an event.

Shopify's payment reminders are real and worth switching on: up to five per order, each set to the due date or up to thirty days after it. Nothing can be scheduled before the due date, so the polite heads-up that actually prevents a late payment is the one email the platform cannot send.

They are also per order. A company with four open invoices gets four reminders about four order numbers and never a statement. A merchant put it exactly that way in September 2026: four separate emails instead of one statement of what they owe.

And there is no company balance anywhere in Shopify. The Company object in the Admin API carries total spent and an order count. No outstanding balance, no credit limit, no aging. The one number every wholesale business runs on is the number Shopify does not keep.

The data is there one level down. Each payment schedule carries a due date, a completion date and a balance due. Sum the balance due per company where the due date has passed and the completion date is empty, and you have the statement nobody is sending.

So this is a clock and a group-by, not a listener. Read every open payment schedule once a day, roll the balances up by company, and send one message per account to the person who actually pays.

## Overdue is a date going by, and you cannot subscribe to that

Shopify's [deferred payments](https://help.shopify.com/en/manual/orders/deferred-payments) page is clear about the mechanics. You can put four kinds of terms on an order marked payment pending: due on receipt, due on fulfillment, a net term, or a fixed date. The net terms on offer are net 7, 15, 30, 45, 60 and 90. And then: if the order isn't paid by the due date, the order status becomes Overdue.

That reads like a state change. It is not one. Look at [OrderDisplayFinancialStatus](https://shopify.dev/docs/api/admin-graphql/latest/enums/OrderDisplayFinancialStatus) in the Admin API and you get eight values, none of them overdue. An unpaid net 30 order on day 5 and the same order on day 95 carry the identical financial status: pending. The admin draws the badge by comparing a date to the clock. No field flipped, no record was written.

Which matters, because every automation surface Shopify gives you is event-driven. Webhooks fire on change, Flow triggers fire on change. A due date passing is not a change, so there is no topic to subscribe to and no trigger to pick from a list. The failure you are chasing is defined by nothing happening.

The event side is shakier than you would hope even when something does change. In October 2024 a developer [changed an order's terms](https://community.shopify.com/t/change-in-order-payment-terms-does-not-trigger-order-update-webhook-or-show-in-get-order-response/362783) from due on receipt to net 90 in the admin, subscribed to both order create and order update, and received nothing. The REST API kept returning the old term while the admin showed the new one. One speculative reply, no staff answer, no accepted solution. Even an explicit edit to payment terms is not something you can rely on hearing about.

## The reminders Shopify does send, and the three things they cannot do

Switch them on before you build anything. Settings, Notifications, Orders, Payment reminder. Up to five, each set to the due date or up to thirty days after it, using your store's own template. They are not sent for orders with purchase options such as subscriptions, preorders or try before you buy. For a store with a handful of trade accounts that is most of the job done in ten minutes.

Then you hit the ceiling, in three places.

**They cannot fire early.** The earliest slot is the due date itself, which is the day the money is already late. A merchant writing up a manual net terms system in August 2026 named this as the gap: nothing fires before the due date, so the heads up email is still manual. If you have noticed that the accounts who pay on time are the ones whose bookkeeper got a nudge on day 25, you already know that slot is the valuable one.

**They cannot add up.** The reminder is attached to an order, so the unit of communication is an order. Four open invoices means four emails, each arguing for its own order number, none of them saying what the relationship is worth. In a [September 2026 thread](https://community.shopify.com/t/anyone-else-stuck-doing-wholesale-net-terms-invoicing-manually-since-b2b-opened-up-to-non-plus-plans/687136) on exactly this, one merchant described getting four separate emails instead of one statement of what they owe, and added that there is no per-company running balance in the admin at all. Five people replied with workarounds. No staff reply, nothing marked as a solution.

**And they go to the buyer.** The email on the order belongs to the person who chose the products, who is usually not the person who releases the payment. In November 2023 a merchant asked, in the long-running [Flow payment reminders thread](https://community.shopify.com/t/can-i-use-flow-to-send-out-payment-reminders-to-customers-with-payment-pending/142752), for an accounts payable field so a reminder could reach AP alongside the buyer. Nobody answered. In October 2025 another merchant in the same thread asked how to send reminders 7 and 14 days before a 30 day due date, because her customers were schools paying on purchase orders. Nobody answered that either.

## Flow has a trigger, and it fires on the one day you do not need it

This is the part people miss. The [Flow triggers reference](https://help.shopify.com/en/manual/shopify-flow/reference/triggers) does carry a trigger for this: *Payment schedule is due*. It exists, it works, and it fires the moment a schedule becomes due.

Which is day zero, the moment a native reminder already covers. There is no payment schedule is overdue trigger, nothing at day 7 or 14 or 30, and nothing for a schedule that is simply still sitting there. The company side is emptier: Flow's B2B triggers are company created, company location created, company contact created and company contact assigned permission. All four describe the shape of the account. Nothing in the list is about money the account owes you.

Then the delivery problem. Flow has never been able to email your customers. A Shopify voice in that reminders thread said so in August 2022, that Flow can only send emails to internal or specific addresses and not to customers, and said it again a year later: Flow is not implementing a generic system to email customers outside of partners and Shopify Email. The thread opened in August 2022 and was still collecting replies in September 2026 with no accepted solution.

So use the trigger for what it is good for. Treat *payment schedule is due* as the start of a clock: stamp the order the day it becomes due, and let something outside Flow do the counting and the sending.

## Nobody is keeping your receivable, Shopify included

Read the field list on the [Company object](https://shopify.dev/docs/api/admin-graphql/latest/objects/Company). Contacts, locations, draft orders, orders, an order count, metafields, a note, when they became a customer, and total spent. Total spent is money that has arrived. There is no balance, no credit limit, no days sales outstanding, no aging bucket. Nothing on the object knows this account is four weeks behind on eleven thousand dollars.

Which is why, in that September thread, the merchant who had been doing this longest called the per-company running balance the bit everyone ends up rebuilding in a spreadsheet. He is right, and that spreadsheet is the thing you are actually replacing. It is accurate on the Monday somebody builds it and wrong by Wednesday, because two payments landed and one new order went out on terms and the file does not know.

## The two objects that give you the statement

[PaymentTerms](https://shopify.dev/docs/api/admin-graphql/latest/objects/PaymentTerms) carries an `overdue` boolean, documented as whether the payment terms have overdue payment schedules, plus the term's name, its type and how many days it runs. That boolean is the one field in the platform that answers the question your admin badge is drawing, and it is reachable only through the API.

[PaymentSchedule](https://shopify.dev/docs/api/admin-graphql/latest/objects/PaymentSchedule) carries the dates and the money. `issuedAt` is when the invoice is sent, `dueAt` when the schedule is due, `completedAt` when it was paid or fulfilled, `balanceDue` the remaining balance to be captured, and `totalBalance` the remaining balance for the customer to pay or authorize.

That is the whole query. Per company, take the schedules where `completedAt` is empty, bucket them by how far `dueAt` is in the past, and sum `balanceDue` in each bucket. Not due yet, 1 to 7 days, 8 to 30, 31 to 60, over 60. Five numbers and a list of order names per account, which is a statement.

One trap. Sum the balance, not the order. A partially paid invoice still has an open schedule, so a count of overdue orders overstates how many accounts are in trouble and a sum of order totals overstates the money by whatever has already come in. `balanceDue` is the figure that survives a part payment, a credit note and an edited order. Build on it and your statement matches the bank.

## The one lever that stops an overdue account ordering again

An account that owes you money for ninety days can place another order this afternoon on the same terms, and Shopify will take it. As one merchant put it in September, nothing stops an overdue company placing new orders.

There is a native lever, and it is per company. Under Customers, then Companies, then that company's Checkout settings, there is an option to submit all orders as drafts for review. It does the right thing: new orders are parked for approval rather than refused, so the relationship survives and the credit decision comes back to you. The problem, as that August thread put it, is that someone has to switch it on and off by hand. In practice it gets switched on once, in frustration, and never switched off, and three months later a good account is wondering why its orders keep going to a queue.

Flipping that switch on a rule is the most valuable thing in this piece and the least written about. On when a company crosses your line, whatever your line is. Off the morning the balance clears. No argument in the sales meeting about whether to park the Henderson account, because the rule did it and the rule will undo it.

## What this costs on an ordinary month

Forty trade accounts, an average invoice of eighteen hundred, net 30, two orders a month each: about a hundred and forty thousand going out on terms. If a fifth of those invoices slip past due, and the ones that slip get chased nine days late instead of nudged three days early, you are carrying roughly twenty-eight thousand dollars twelve days longer than the terms you agreed. Every month, rolling.

That money is not lost. It is permanently one cycle behind, which is the same arrangement as an interest-free loan you did not decide to make, funded by your working capital at the exact moment you want to buy stock. Plus the Friday afternoon: somebody exports orders, filters to payment pending, cross-references the bank, works out which of the four Henderson invoices cleared, and writes the emails. An hour, most weeks, and the first thing dropped when trading is busy, which is when the receivable is biggest.

## What the automation actually has to do

As a Dugong playbook, in plain prose:

```
# trigger
Scheduled daily sweep, plus
payment schedule is due

# steps
1. Read the due date, not the
   order status
2. Roll every open balance up
   by company
3. Send one statement, not one
   email per order
4. Copy the person who pays,
   not just the buyer
5. Nudge before the due date,
   not only after
6. Hold new orders when an
   account crosses the line
7. Age the list and escalate
   the wording
```

Step one is the design decision. The order status says pending forever, and pending is true on day 2 and day 200. Read `dueAt` against today and `completedAt` to see whether it settled. Everything downstream is arithmetic on those two fields plus `balanceDue`.

Steps two and three are where this stops being a reminder app. Group the open schedules by company rather than by order, and send one message that opens with the total and lists the invoices under it, oldest first, with order names your customer can look up. A buyer who receives one number can forward one number to one colleague. A buyer who receives four emails forwards none of them.

Step four is the step that collects the money. Keep an accounts payable contact per company alongside the buyer, because Shopify has no field for it, and address the statement to both. That is the request sitting unanswered in the community since 2023, and for your own store it is a metafield and a mailing list away from solved.

Step five is the cheap one nobody does. A short note three days before the due date, saying the invoice is coming up and here is the link, moves a real share of payments from late to on time, because most late B2B payment is an invoice falling off a busy buyer's radar rather than anybody deciding not to pay. The platform cannot schedule it. Anything with a clock can.

Step six is credit control, and it needs a written line before you automate it: a balance over this much, or over this many days, parks new orders for review. Set the switch from the rule and clear it the day the balance clears. The point is not the blocking, it is that the blocking reverses itself without anybody having to remember to be fair.

Step seven is tone. The same wording for a three-day slip and a ninety-day slip trains everyone to ignore it. Three bands is enough: a reminder, a request, and a note that new orders are going to review until the balance clears. Send the third only once the switch is genuinely set, because a threat you do not carry out is worse than no threat.

## Why this is a workflow and not a checklist

Every step here is something a person can do. Reading a due date is easy. Adding up four invoices is easy. The reason it does not get done is that it has to be done on a day with nothing special about it, for accounts that have done nothing wrong yet, by somebody whose actual job is something else.

There is also no judgment in it. The judgment is two sentences you write once: how many days and how much money is your line, and who at each account receives the statement. After that it is a date comparison, a sum and an email, run every morning whether trading is busy or not.

The limits are honest ones. No automation makes a customer who has run out of money pay you. It cannot tell a buyer who is stalling from a buyer whose accounts system lost the invoice, which is why the first message should always assume the second. It has nothing to read if the terms were never put on the order, because without payment terms there is no due date. And if nobody at your end owns the receivable, the statement lands in an inbox nobody opens.

## Do this before you close the laptop

Three checks, ten minutes, no code.

Open Settings, Notifications, Orders, and look at Payment reminder. If the list is empty you have been chasing from memory, and five minutes here is the highest return in this article.

Filter your orders to payment pending and sort oldest first. Look at the date on the top row, then look down the company column and count how many rows share a name. The first number is how long your oldest invoice has been out. The second is how many emails that customer has been sent about it.

Then ask whoever writes the chasing emails how they know the total. If the answer is a spreadsheet, you have found where your receivable actually lives, and you know what the automation has to replace.

> **◆ READING** Two companion pieces if this one landed: [the invoice you send by hand](https://blog.dugong.live/how-to-automatically-send-invoices-on-shopify.html), on the document your business buyers keep asking for, and [the quote that goes quiet](https://blog.dugong.live/how-to-automatically-follow-up-on-unpaid-draft-orders-on-shopify.html), on the same silence one stage earlier, before the order exists.

If you sell on Shopify on terms and have a version of this story, the account that owed you four invoices and got four emails, the balance that lived in a spreadsheet, the good customer you parked and forgot to unpark, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Why doesn't Shopify show what a B2B customer owes in total?

Because nothing in the platform keeps that figure. The Company object in the Admin GraphQL API carries contacts, locations, draft orders, orders, an order count, metafields, a note, when they became a customer, and total spent. Total spent is money that has already arrived. There is no outstanding balance field, no credit limit, no days sales outstanding and no aging bucket, so the admin has nothing to display and the API has nothing to return. Merchants confirmed the same thing from the other direction in a September 2026 community thread: there is no per-company running balance in the admin at all, and the merchant with the longest experience of it called the running balance the bit everyone ends up rebuilding in a spreadsheet. The figure is derivable, just not stored. Each order's payment schedules carry a balance due and a due date, so summing the balance due for every schedule that has no completion date gives you the number, per company, in one query.

Permalink: https://blog.dugong.live/how-to-chase-overdue-shopify-b2b-invoices.html#faq-1

### Can Shopify send a payment reminder before the due date?

No. Payment reminders live under Settings, then Notifications, then Orders, then Payment reminder, and you can create up to five of them. Shopify documents the available timing as the payment due date, or up to thirty days after the due date. There is no option for a number of days before, which means the earliest message the platform can send arrives on the day the invoice is already late. The gap has been raised repeatedly. A merchant writing up a manual net terms system in August 2026 named it directly, saying nothing fires before the due date so the heads up email is still manual, and in October 2025 a merchant asked how to send reminders 7 and 14 days before a 30 day due date because her customers were schools paying on purchase orders, and got no answer. Anything with its own schedule can send that email. Shopify's reminders cannot. One thing worth noting while you are in there: reminders are not sent for orders with purchase options such as subscriptions, preorders or try before you buy.

Permalink: https://blog.dugong.live/how-to-chase-overdue-shopify-b2b-invoices.html#faq-2

### Does Shopify Flow have a trigger for an overdue invoice?

Not for overdue, no. Flow does carry a payment trigger called Payment schedule is due, which fires at the moment a schedule becomes due. That is day zero, which a native reminder already covers. There is no payment schedule is overdue trigger, nothing that fires at seven, fourteen or thirty days past due, and nothing for a schedule that is simply still open. This is a property of event-driven automation rather than a gap in Flow: a trigger can only fire on something happening, and a due date going past is a date being compared to a clock, not a record changing. Flow's B2B triggers are company created, company location created, company contact created and company contact assigned permission, all of which describe the shape of an account rather than the money it owes. There is also a delivery limit worth knowing before you plan around Flow, which is that it cannot email your customers. Shopify said so in the community in 2022 and again in 2023, that Flow is not implementing a generic system to email customers outside of partners and Shopify Email. Use Payment schedule is due to tag the order on the day it becomes due, then do the counting and the sending outside Flow.

Permalink: https://blog.dugong.live/how-to-chase-overdue-shopify-b2b-invoices.html#faq-3

### How do I find every overdue B2B order on Shopify?

In the admin, filter the orders list to payment pending and sort by oldest, which gets you the list but not the money. Through the API you can be exact. PaymentTerms carries an overdue boolean, documented as whether the payment terms have overdue payment schedules, and each PaymentSchedule carries issuedAt for when the invoice is sent, dueAt for when the schedule is due, completedAt for when it was paid or fulfilled, and balanceDue for the remaining balance to be captured. Take every schedule where completedAt is empty, group by company, bucket by how far dueAt is in the past, and sum balanceDue in each bucket. One caution: sum the balance, not the order. A partly paid invoice still has an open schedule, so counting overdue orders overstates how many accounts are behind, and summing order totals overstates the money by whatever has already arrived. Balance due is the figure that survives a part payment, a credit note and an edited order.

Permalink: https://blog.dugong.live/how-to-chase-overdue-shopify-b2b-invoices.html#faq-4

### Can you stop a Shopify customer ordering when they already owe you money?

Not automatically, but there is a lever. Shopify will happily accept a new order on terms from a company that is ninety days late, which merchants have pointed out plainly: nothing stops an overdue company placing new orders. The one native control is per company, under Customers, then Companies, then that company's Checkout settings, where you can require that all orders are submitted as drafts for review. It behaves well, parking new orders for your approval rather than refusing them outright, so the relationship survives and the credit decision comes back to you. The catch is that somebody has to switch it on and off by hand, which in practice means it gets switched on once in frustration and never switched off, and three months later a good account is wondering why its orders keep going to a queue. Driving that switch from a rule is the part worth automating: on when a company crosses your line, off the morning the balance clears.

Permalink: https://blog.dugong.live/how-to-chase-overdue-shopify-b2b-invoices.html#faq-5

### Can AI chase overdue Shopify B2B invoices?

Yes, and it is a good fit, because nothing in the job requires an opinion. An automation like Dugong reads the due date rather than the order status, since pending is equally true on day 2 and day 200. It rolls every open balance up by company so one account gets one statement instead of four reminders about four order numbers. It addresses that statement to an accounts payable contact as well as the buyer, which is a metafield plus a mailing list, because Shopify has no field for the person who actually pays. It nudges three days before the due date, the slot the platform cannot schedule, since most late payment is an invoice falling off a busy buyer's radar rather than a decision not to pay. It sets the submit orders as drafts switch when an account crosses a line you wrote down once, and clears it the morning the balance clears. And it ages the list so a three-day slip and a ninety-day slip do not read the same. The limits are honest. It cannot make a customer who has run out of money pay you, it cannot tell a staller from a lost invoice so the first message should assume the second, it has nothing to read if the terms were never put on the order, and if nobody at your end owns the receivable the statement lands in an inbox nobody opens.

Permalink: https://blog.dugong.live/how-to-chase-overdue-shopify-b2b-invoices.html#faq-6

---

## Read next

- [The invoice you send by hand](https://blog.dugong.live/how-to-automatically-send-invoices-on-shopify.html): Shopify emails a receipt, not an invoice, and has no field for a customer's tax number, so business buyers ask and you build it by hand. The AI playbook that sends the right invoice after every order.
- [The quote that goes quiet](https://blog.dugong.live/how-to-automatically-follow-up-on-unpaid-draft-orders-on-shopify.html): Shopify sends one draft order invoice and never a reminder, so quotes die in silence. The AI playbook that follows up, answers, and retires stale quotes.
- [How to stop Shopify B2B prices dropping every time you run a sale](https://blog.dugong.live/how-to-stop-shopify-b2b-prices-dropping-when-you-run-a-sale.html): A weekend sale on the storefront quietly cuts your wholesale prices too, because a catalog percentage is computed off the live price. The AI playbook that holds the B2B floor.
