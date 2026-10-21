# How to handle Shopify returns when the customer never sends the item back

> Shopify has seven return triggers and none fire when nothing happens. The AI playbook that chases a quiet return, holds the money, and closes it honestly.

- Canonical: https://blog.dugong.live/how-to-handle-shopify-returns-the-customer-never-sends-back.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-10-11
- Section: Research
- Word count: 2250
- Dispatch: Nº 124 · Research · 8 min read
- Full headline on page: How to handle Shopify returns when the customer *never sends the item back*
- Keywords: shopify return never sent back, close shopify return in progress, cancel inactive returns shopify flow, return_status open shopify, shopify return label never used, refund before return received, shopify open returns, return abuse shopify
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

Filter your orders by return status this afternoon and count the ones that still say *return in progress*. In most stores doing a few hundred orders a month the number is between eight and thirty, and a third of them are older than the month they were opened.

Each one is the same small story. A customer asked, you approved it because arguing costs more than the item, you emailed a label. Some posted the box the next morning. Some meant to and it is still in the hallway. Some never intended to. And a few posted it, it arrived, and it is on your receiving shelf with the label peeled off and nobody able to say which order it belongs to.

From inside the Shopify admin all four look exactly the same: a return, still open, no movement.


## The short answer

Shopify can close a quiet return but it cannot notice one. All seven Flow return triggers fire on a status change somebody makes, so a return that simply stops moving fires nothing, and the cancel return action shipped on 16 August 2024 only works on returns that were never refunded, restocked, marked as returned or labeled, which excludes most of the ones you want to close. Build the watching yourself.

Age every open return from its first carrier scan rather than the approval date, separate never shipped from stalled in transit from arrived but unprocessed on your own bench, reconcile inbound parcels against open returns daily, chase on a dated ladder at seven, fourteen and twenty-one days, hold the refund until the first scan, flag exchanges shipped against returns that never landed, then close the remainder as shrinkage and count the pattern per customer and per address. The judgment, telling three identical-looking silences apart and matching an orphan box to the right return, is why this belongs with an agent rather than a condition builder.
## Nothing happening is not an event

This is the mechanical reason the pile grows. Flow has seven return triggers: return requested, return approved, return declined, return processed, return closed, return cancelled and return reopened. Every one of them fires when somebody changes a status. A return that goes quiet changes nothing, so nothing fires, so nothing tells you.

A merchant put this to the Shopify Community on 20 September 2024. They wanted a Flow that automatically closed orders still sitting at return in progress more than thirty days after they were created. The first reply told them to use a *get order data* step with a query on return status and a created-at cutoff, then loop over the results and close them. The merchant asked how you actually enter that query inside Flow. Nobody answered that part. A second reply pointed at a template. The thread is two years old and still has no working query in it.

## Shopify did ship something, and it is worth knowing

On 16 August 2024 Shopify added all six of those return triggers to Flow, plus a *cancel return* action and three templates. One template is called *cancel inactive returns*. The changelog entry says, in its own words, that the action helps when buyers do not send products back. So Shopify knows about this exact problem and has given you the broom.

Set that template up. It is twenty minutes and it stops your returns list lying to you. Then be clear about what it did, which is tidy a list. Four things it does not do, and all four cost money.

**Cancelling is one way.** A cancelled return cannot be reopened. You create a second one. So the parcel that was only slow, the one that turns up on day thirty-four because a sorting hub lost a week, now has no return to attach to, and the customer who did the right thing gets an email about a return they already completed.

**The gate blocks the returns you care about most.** Shopify will only cancel an open return if it has not been refunded, restocked, marked as returned, labeled, or had a fulfillment cancelled. Read that list again. If you created a label, which is the whole reason you expected a box, the easy cancel is already off the table.

**Cancelling does nothing to the money.** If you refunded on approval, closing the record changes nothing except the color of a badge. You are still out the item and still out the cash, and now the evidence is tidied away.

**Flow cannot do the money side anyway.** The return actions are cancel return, close return and reopen return. There is no refund action anywhere in Flow, and no inventory adjustment action either. Anything beyond those three has to go through *send admin API request*.

## A trap in the query itself

If you build the scheduled version, check your result count by hand before you point a cancel action at it.

In November 2024 a developer reported this on the community forum. An unfiltered query returned an order whose return status was `IN_PROGRESS`, holding a return whose status was `OPEN`. Filtering with `return_status:open` returned nothing at all. Filtering with `return_status:in_progress` returned the right order, and the response came back carrying a warning that `in_progress` is not an accepted value. Nobody replied. The thread is still open.

So one documented value silently matches nothing and the value that works tells you it is wrong. A workflow built on the first one runs every night, finds zero returns, reports success, and lets the pile grow for a quarter.

## The three silences

The real work is not closing old returns. It is telling apart three situations that look identical and have nothing else in common.

**Never shipped.** No carrier scan has ever happened on that label. This is the only one of the three where the customer can still fix it, and it is the one where a reminder on day seven recovers a startling share of the items. It is also the cheapest: a Shopify return label that is never used is never scanned.

**Shipped and stalled.** There are scans and then there are not. This is a carrier problem, the clock is a claim window rather than a return window, and the customer has already done their part. Chasing this one for a tracking number they already gave you is how a loyal buyer becomes a review.

**Arrived and unprocessed.** The box is on your own bench. Somebody signed for it on the nineteenth, the packing slip is not in it, and matching it to an order takes ten minutes nobody has on a Thursday. This is the most expensive of the three and the only one that is entirely your fault, and in every store I have looked at it is a larger share of the open returns than anyone expects.

Shopify cannot separate these for you. It only knows tracking if a label with a number is attached, and it will only create return labels itself when your primary location and the customer address are both in the United States. Everywhere else you are uploading a PDF and typing the carrier in, which is exactly the step that gets skipped at five to six on a Friday.

## What an open return actually costs

Four costs, and the item itself is usually the smallest of them.

**Inventory you are still counting.** Returns do not restock until you process them. Every open return is a unit your forecast believes is coming back, which means your reorder math is running on stock that does not exist. Thirty open returns on a seasonal line is a purchase order you did not raise.

**The fee on money you gave back.** Shopify Payments does not return credit card fees on a refund. If you refunded on approval and the box never came, you paid for the item, the refund and the processing on both legs.

**The exchange you already shipped.** This is the one that hurts. Inventory for exchange items is not reserved until you process the return. So the usual goodwill move, sending the replacement straight away so the customer is not waiting, means a second unit has left the building against a first unit that may never arrive. On a quiet return, an exchange is a free second product.

And one that is not money. Your return rate is wrong in both directions: inflated while these sit open, then flattered the moment a scheduled workflow cancels them in bulk. Neither number is the truth, and the truth was the only reason you were measuring.

## The playbook worth building

As a Dugong playbook, in plain language:

```
# trigger
Daily, over every open return,
plus every inbound parcel at
the receiving bench

# steps
1. Age each return from its first
   carrier scan, not from the
   approval date
2. Classify the silence: never
   shipped, stalled in transit,
   or sitting unprocessed here
3. Match every inbound box to an
   open return, including the
   ones with no paperwork
4. Chase on a ladder: day 7
   reminder, day 14 dated final
   notice, day 21 decision
5. Hold the refund until first
   scan, unless the customer and
   basket earn an exception
6. Flag exchanges shipped against
   a return that has not landed
7. Close it: cancel or zero-
   process, release the phantom
   unit, book it as shrinkage
8. Count quiet returns per
   customer and per address
```

**Step one is the whole difference.** Aging from the approval date treats a parcel crawling across a country the same as a label nobody printed. Aging from first scan splits your pile in two on day three, before anything has gone cold, and each half gets a different message from a different person.

**Step three is where the money is hiding.** Reconciling the receiving bench against open returns, every day, finds items you have already paid for twice. It is also the least glamorous thing on this list, which is precisely why it is never anybody's job.

**Step four works because of the date in it.** A reminder saying your return is still open recovers very little. A reminder saying this label stops working on 24 October and the refund closes with it recovers a lot. Same effort, same tone, one real number.

## Write down three numbers

Most stores do not have a returns problem here. They have an undated one, which is why every quiet return turns into a private argument between whoever opens the inbox and whoever counts the stock.

Three numbers, published in your returns policy and copied into the first email: how many days the customer has to post it, how many days after that you close the return, and what happens then. That is it. Those three numbers are also the entire configuration of the automation, which is the part worth noticing. Nobody is blocked on tooling here. They are blocked on a decision nobody has written down.

One more, internal: the value above which a quiet return goes to a human instead of being written off.

## Where AI earns its place

Three jobs, and none of them is subtraction.

**Classifying the silence.** Carrier scan history, inbound parcel logs, the photo somebody took of the receiving shelf, the note in the order, the customer's last reply. A model reads all of it and says which of the three silences this is. A rule that only counts days cannot, which is why a rule either chases people who already posted the box or writes off items sitting twelve feet away.

**Matching the orphan box.** An unlabeled parcel with a hoodie in it and a handwritten note. One open return in your list is for that variant, to that postcode, opened eleven days ago. That match is obvious to a person with the whole list in their head and invisible to a person with a queue of forty.

**Writing the three messages.** Each with the real deadline, the right tracking state, and a tone that fits a customer who may well have done nothing wrong. The day-fourteen notice is the one that pays for the build, and it is the one nobody ever gets around to sending.

Two things stay human. The write-off threshold, because it is a margin decision. And the first time you treat somebody as a return abuser, because being wrong about that costs far more than the item. Let the system count the pattern and gate the next approval; let a person say the sentence.

## Set it up this week

Filter your orders by return status today and count the open returns older than twenty-one days. Multiply by your average order value. That number has never been in a meeting.

Then walk to wherever returns arrive and count the boxes nobody has opened. Compare the two piles. The overlap is free money.

Then write down the three numbers and put them in the policy. The automation after that is a day of work. Without them it is a permanent argument.

> **◆ READING** Two companion pieces if this one landed: [The return that never goes back on the shelf](https://blog.dugong.live/how-to-automatically-restock-returns-on-shopify.html), on the units that arrive and never rejoin your stock, and [The return that won't approve itself](https://blog.dugong.live/how-to-automate-returns-and-exchanges-on-shopify.html), on the approval queue that eats a morning a week.

Sitting on a pile of open returns, a receiving bench full of unmatched boxes, an exchange you shipped twice, or a buyer whose returns never seem to ship? The inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### How do I close a Shopify return the customer never sent back?

Open the order, find the return in progress, and cancel it. Shopify will only let you cancel an open return if it has not been refunded, restocked, marked as returned, labeled, or had a fulfillment cancelled, which is a real problem in practice because the returns you most want to close are usually the ones you created a label for. When the return is blocked, the honest route is to process it with nothing received, close it, and record the write off against the order with a note. Two cautions. A cancelled return cannot be reopened, so if the parcel was only slow you have to create a second return and the customer sees two. And cancelling the return does nothing to the money: if you already refunded on approval, closing the record just tidies the admin while you remain out the item and the cash.

Permalink: https://blog.dugong.live/how-to-handle-shopify-returns-the-customer-never-sends-back.html#faq-1

### Can Shopify Flow close or cancel old returns automatically?

Partly, and it has been able to since 16 August 2024, when Shopify shipped six return triggers (return requested, approved, declined, closed, cancelled and reopened), a cancel return action, and three templates including one called cancel inactive returns. The changelog entry says in its own words that the action helps when buyers do not send products back. What it cannot do is notice. Every one of those triggers fires on a status change somebody makes, and a return that goes quiet makes no change at all, so nothing fires. The native workaround is the scheduled time trigger plus get order data with a return status query, which is exactly what a merchant was told in a September 2024 community thread asking how to close returns older than thirty days. That thread never produced a working query. Flow also has no refund action, so the money side has to go through send admin API request.

Permalink: https://blog.dugong.live/how-to-handle-shopify-returns-the-customer-never-sends-back.html#faq-2

### Why does return_status:open return no orders in the Shopify API?

Because the value the orders query accepts and the value the documentation suggests are not the same thing. A developer reported this on the Shopify Community in November 2024: an unfiltered query showed an order with a return status of IN_PROGRESS holding a return whose status was OPEN, the filter return_status:open returned nothing at all, and the filter return_status:in_progress returned the right order while the response carried a warning that in_progress is not an accepted value. No one replied and the thread is still open. The practical lesson is to test the filter against a store you can see rather than trusting the documentation or the warning, and to verify your result count against the orders page before you point a cancel action at it.

Permalink: https://blog.dugong.live/how-to-handle-shopify-returns-the-customer-never-sends-back.html#faq-3

### Should I refund a Shopify return before the item arrives?

Only deliberately, and only for the customers and price points where you have decided the goodwill is worth the exposure. Refunding on approval is the single decision that turns a quiet return from an annoyance into a loss, because once the money has gone the only lever left is asking nicely. Three details make it worse than it looks. Shopify Payments does not return your credit card fees on a refund, so you are out the item, the cash and the processing. Inventory is not restocked until you process the return, so your forecast keeps counting a unit that is never coming. And on an exchange, inventory for the replacement is not reserved until you process the return, which means a replacement you shipped early is a gift if the original never lands. A better default is to refund on first carrier scan rather than on approval: the customer gets a date they can trust, and you only pay once the box is genuinely moving.

Permalink: https://blog.dugong.live/how-to-handle-shopify-returns-the-customer-never-sends-back.html#faq-4

### Can AI handle Shopify returns that never come back?

This is a good fit, because the work is classification and writing rather than arithmetic. Three silences look identical in the admin: the customer never shipped, the parcel shipped and is lost, and the parcel arrived and is sitting unopened in your receiving area. A model can separate them by reading carrier scan history, the inbound parcel log and the receiving photos, and it can match an unlabeled box with no paperwork to the one open return whose items and address fit. It can then write the three messages that actually recover the item, each with the real deadline in it, and escalate only the decisions worth a human. It can also see the pattern nobody has time to look for: the same buyer, or the same address under three names, opening returns that never ship. Keep two things human. The write off threshold, because that is a margin call. And the first accusation of abuse, because being wrong about that costs more than the item.

Permalink: https://blog.dugong.live/how-to-handle-shopify-returns-the-customer-never-sends-back.html#faq-5

---

Markdown rendition of https://blog.dugong.live/how-to-handle-shopify-returns-the-customer-never-sends-back.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
