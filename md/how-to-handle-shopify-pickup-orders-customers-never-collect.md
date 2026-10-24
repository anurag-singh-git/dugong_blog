# How to handle Shopify pickup orders customers never collect

> Shopify sends one ready for pickup email and goes silent: no reminders, no resend button, no auto-cancel window. The AI playbook that clears the pickup shelf.

- Canonical: https://blog.dugong.live/how-to-handle-shopify-pickup-orders-customers-never-collect.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-08-24
- Updated: 2026-10-24
- Section: Research
- Word count: 2800
- Dispatch: Nº 114 · Research · 10 min read
- Full headline on page: How to handle Shopify pickup orders customers *never collect*
- Keywords: pickup reminder email, resend ready for pickup notification, local pickup order not collected, uncollected pickup orders, ready for pickup resend button grayed out, cancel pickup order not collected, automatic pickup reminders, local pickup automation, AI order monitoring
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

The shelf behind the register tells the story better than any report. Eleven paper bags, each with a sticky note: a name, an order number, a date. The newest is from Saturday. The oldest is from March. Every one of them is a completed sale, paid in full, picked and packed by someone on your payroll, and every one of them is also a small standing question: does she know it's here? Did the email land? Do we call? At what point does a sold candle become a stored candle become a problem?

Shopify's answer to that question is one email. When you mark a pickup order ready, the customer gets a [Ready for pickup notification](https://help.shopify.com/en/manual/fulfillment/setup/delivery-methods/pickup-in-store), once. If it goes to spam, that was the notification. If she reads it on a busy Tuesday and forgets, that was the notification. There is no reminder after three days, no resend button when she calls to say she never got it, no expiry date on the shelf, and no policy engine deciding what happens next. The flow assumes every customer collects promptly, and the shelf is where that assumption goes to age.

## The short answer

Give the shelf a policy and a clock: start counting the day the order is marked ready, remind the customer on a fixed schedule, and decide in advance what happens when the window closes. Shopify does none of this. It sends one Ready for pickup email at the moment you mark an order ready, and then it goes quiet.

There is no resend for that notification anywhere in the admin or the POS app, and the control that does appear in the order timeline sits grayed out and unclickable. There is no reminder schedule and no pickup window either, so a bag marked ready in March looks exactly like yesterday's in the fulfillment queue.

Reminders therefore have to go out through whatever still works: a manual email, an SMS, the contact customer template, or the order status page link. The piece worth building is the column the admin lacks, a shelf age on every bag, with a friendly nudge at day two, a named deadline at day five, a ship-it-or-refund-it choice at day seven, and a cancel, refund and restock when the window closes. Most high street chains return goods to stock after about a week. Pick your own number and make the dates fire without anyone remembering them.

## The shelf is money standing still

Count what one uncollected bag actually costs. The inventory inside it is sold but not gone: it cannot be resold, and it sits outside the counts that drive reordering, a cousin of [the dead stock your dashboard never mentions](https://blog.dugong.live/how-to-automatically-clear-dead-stock-on-shopify.html). The order sits unfulfilled in the admin, cluttering the queue your team works from every morning. The customer's money is captured, which starts a quiet clock of its own: a shopper who paid months ago and never received anything is a refund request at best and a chargeback at worst, and a cardholder who can say the goods were never received is a hard dispute to win. And the shelf itself is real estate. A florist loses the cooler space, a bakery throws the order away, a schoolwear shop watches the uniform sizes it could have resold in August sit in bags until October.

Multiply by peak season and the number stops being funny. The merchant who documented this best runs a schoolwear shop, essential purchases for parents, and still ended one summer with hundreds of uncollected orders. The team sifted through every last one to send reminders by hand. Many orders, she wrote, didn't get collected until months after purchase.

## The community record

The reference thread was opened in October 2021 by a tea merchant in Hawaii with a problem he described mildly: I have customers who sometimes forget about their order for a month or more, and I have to send personal emails to remind them. A resend button in the order timeline would be much easier. Shopify staff answered the same week, and the answer has not changed since: re-sending the Ready for pickup notification is a feature that isn't available in the Shopify admin yet, the feedback would be passed to the developers, and the merchant should keep an eye on the changelog. The thread ran to 27 replies and well over a thousand views, and was still collecting posts in April 2025. The changelog never delivered.

Read in order, the replies map every corner of the failure. June 2022: there is no point resending the order confirmation, which is allowed, when the pickup notification is the one that matters, especially if the pickup details change and every affected customer must be emailed by hand. July 2022: it should be a simple button in the POS app. October 2022, a genuine puzzle: the resend control appears in the order timeline but sits grayed out, unclickable, and in August 2023 another merchant posted a screenshot of the same dead button, wondering if the functionality exists but isn't working. December 2023: would be hugely valuable to remind customers to come get their stuff after 3 days, 7 days, any solutions here, after 2+ years on the initial request? March 2024 lost patience entirely: it's completely asinine that this is not an existing feature. August 2024 asked for the fuller fix, a pickup reminder email that can be set to send automatically, and staff replied that the feedback had been shared with the developers, again. September 2024 needed one line: it's been YEARS, lol. Any update?

A second thread opened in May 2024 to ask for the same button, called it a very, very basic function, and aged the same way: a me-too in December 2024, a May 2025 reply pointing out that the other thread requesting this feature goes back five years, and a June 2025 closing note that stands for the whole genre: how is this not an option yet?! Meanwhile the apps thread from March 2021, the schoolwear shop's thread, recorded the market's answer. One developer offered to build the app. One vendor pitched a payment reminder app bent into pickup duty at ten dollars a month, and got the reply every app store pitch dreads: no thanks, it's a one in a hundred problem, not worth a monthly charge. The thread's real finding was the norm it named in passing: most high street chains return goods to stock after 7 days or so and cancel the order. The big retailers have a shelf policy. Shopify merchants have a shelf.

> **◆ NOTE** The record, in the merchants' own words: customers forget their orders for a month or more, October 2021, with Shopify staff confirming no resend exists. Hundreds of uncollected orders in one peak season, sifted by hand, March 2021. The resend button visible but grayed out, October 2022, still dead in an August 2023 screenshot. Remind customers after 3 days, 7 days, any solutions, December 2023. Completely asinine, March 2024. A pickup reminder that sends automatically, requested August 2024, passed to developers, again. It's been YEARS, lol, September 2024. How is this not an option yet, June 2025.

## One email, then silence

Look at where the pickup flow actually leaks, because there are four holes and they need different patches. The ready email never lands: it bounces, files into spam, or goes to the typo the customer made at checkout, the same silent failure as [the order confirmation that never arrives](https://blog.dugong.live/how-to-fix-order-confirmation-emails-not-sending-on-shopify.html), and nothing in the admin tells you. The email lands and evaporates: read once, forgotten by Friday, and Shopify's flow has no second touch, the same one-shot design as [the gift card that never arrives](https://blog.dugong.live/how-to-automate-gift-card-delivery-and-reminders-on-shopify.html). The details change after the send: a moved counter, new hours, a different location, and there is no way to re-notify anyone except by hand. And the shelf date passes with no consequence, because Shopify has no pickup window: the order will sit unfulfilled for a year without anything asking whether it should.

The admin adds two aggravations of its own. Pickup orders cannot be edited the way shipped orders can, so when a customer finally writes back asking you to just mail it, you are into [the pickup order that should have shipped](https://blog.dugong.live/how-to-change-a-shopify-order-from-local-pickup-to-shipping.html), a workaround genre of its own. And the fulfillment queue has no concept of shelf age: an order marked ready yesterday and an order marked ready in March look identical in the list, so the backlog hides in plain sight until someone physically counts the bags.

## The sticky note is the right idea in the wrong tool

Watch what merchants actually do, because as always the workarounds contain the spec. The Hawaii merchant writes personal reminder emails, one at a time. The schoolwear shop sifts hundreds of orders after peak. One thread documents the template swap: temporarily paste the Ready for Local Pickup template code into the Contact customer email template, so a manual send carries the real pickup details instead of a retyped approximation. The sticky notes on the bags are a shelf-age database maintained in handwriting. Every one of these is a person performing a schedule: notice the order aging, remember the interval, compose the nudge, escalate politely, and eventually decide when a sale becomes a restock. The instinct is exactly right. The flaw is that every step depends on someone noticing, during exactly the seasons when nobody has time to notice, which is how a shop that sells school uniforms in August ends up doing collections in October.

## What the automation actually has to do

As a Dugong playbook, in plain prose:

```
# trigger
On order marked ready for
pickup, and on a daily sweep
of the shelf

# steps
1. Write the shelf policy:
   pickup window, reminder
   days, deadline outcome
2. Start the clock at ready:
   every bag gets a shelf age,
   visible in one list
3. Remind on a schedule: day
   two nudge, day five with
   the deadline named
4. Catch the silent ready
   email: bounces, typos, the
   notification that died
5. Offer another door at the
   window's edge: ship it for
   a fee, or refund
6. Close and restock at the
   deadline: cancel, refund,
   note the timeline
7. Report weekly: shelf age,
   collection rate, recovered
   sales, repeat offenders
```

Step two is the missing column in the admin: shelf age. The moment an order is marked ready, it joins a list sorted by days waiting, and the list is the whole dashboard, because most orders leave it in a day or two on their own. Step three is the feature the threads have requested since 2021, running on your templates and your intervals. The day two note is friendly and complete: address, hours, what to bring. The day five note names the deadline, which is not rudeness, it is the courtesy the big chains extend by policy. Both go by email, and by SMS if you have the number, because the phone is where the original ready email went to die.

Step four is the reading work. A reminder schedule is wasted on an address that bounces, so the watcher checks whether the ready email landed at all, flags the gmial.com typos for [a correction](https://blog.dugong.live/how-to-edit-a-shopify-order-after-its-been-placed.html) instead of a third send into the void, and switches to SMS when email has failed twice. Step five is where sales get recovered instead of refunded: at day seven the customer gets a choice, we can hold it three more days, ship it to you for a small fee, or refund you, and the reply routes to a human when it needs one. Step six is the high street policy, executed with a paper trail: cancel, refund, restock, a timeline note saying which reminders went out and when, so the customer who surfaces in November gets a polite history instead of an argument. The same discipline that runs [the unpaid order that never cancels itself](https://blog.dugong.live/how-to-automatically-cancel-unpaid-orders-on-shopify.html) applies here: the deadline is only real if something happens when it passes.

The honest limits, stated plainly. No automation walks the customer to your door, and a fraction of bags will always hit the deadline. Shopify still has no native resend for the ready notification, so reminders travel through the doors that open: your email platform, SMS, the contact template, the order status link. Switching a pickup order to shipping still runs through Shopify's own constraints on editing pickup orders. And the policy is yours to write: seven days or fourteen, fee or free, restock or hold, those are judgment calls about your customers, not settings a tool should guess. What changes is that the policy executes itself, on every order, in every season, including the one where you have no time to execute anything.

## Why this is a compiler problem, not an app problem

There are apps in this neighborhood: payment reminder apps bent sideways into pickup duty, carrier-specific tools for lockers and parcel shops, POS add-ons. The thread record shows why they never quite stick. The ten dollar app solved one interval for one email and cost more than the problem seemed worth. The carrier app only worked for that carrier. And none of them hold the part that varies, which is the policy. A bakery's shelf window is two days and the deadline outcome is the bin. A schoolwear shop's window is long and forgiving in August and ruthless in October. A gallery holds a sold painting for a month but wants a personal phone call at day ten, not an automated email. Those are sentences about your shop. They should compile into the watcher as written, the same principle that runs [every automation worth building](https://blog.dugong.live/best-shopify-automations-to-set-up.html): the schedule is cheap, knowing what your store means by too long is the job.

Run the March bag again with the sentences compiled. The order is marked ready on a Tuesday; it joins the shelf list at age zero. Thursday, a reminder with the address and hours. Sunday, a second note: we'll hold your order through Friday. Wednesday, the choice: ship it for six dollars, collect by Friday, or we refund you. She picks shipping, pays the fee from her phone, and the order routes into the shipping queue. Total staff time spent: none. The sticky note never gets written, and the shelf holds three bags, all under five days old, which is what a shelf is for.

## The workflow worth building this week

Start by counting the shelf you already have. Filter orders to unfulfilled pickup orders, sort by date, and put an age on each one; most merchants have never seen the number, and the oldest sticky note is usually a surprise. While you are in there, check the ready emails on the stragglers: how many bounced, how many went to addresses with obvious typos, how many customers plausibly never knew their bag was waiting. That split, forgot versus never told, decides how much of your problem is reminders and how much is deliverability.

Then write the shelf policy in plain language: how long the window is, which days the reminders go, what the day seven offer says, what happens at the deadline, and which orders are exceptions, the wedding cake, the commissioned piece, the wholesale pallet. Publish the window on your pickup page and inside the ready email, because a deadline the customer has seen twice is customer service, and a cancellation from nowhere is a one star review.

Then say the brief the way you would hand it to a new hire. Watch every order we mark ready for pickup. If it's still waiting after two days, remind the customer with the address and hours; after five, remind them again and name the deadline. If the ready email bounced or the address looks wrong, tell me instead of sending again. At seven days, offer shipping for our flat fee or a refund, and route any reply to me. At fourteen, cancel, refund, restock, and note everything on the order. Every Monday, tell me how many bags are on the shelf, the oldest age, and how many sales we recovered by shipping. That is the whole paragraph. The compiler turns it into the workflow, and the shelf behind the register goes back to being furniture.

> **◆ READING** Two companion pieces if this one landed: [the pickup order that should have shipped](https://blog.dugong.live/how-to-change-a-shopify-order-from-local-pickup-to-shipping.html), on the workaround maze when a customer asks you to mail it, and [the gift card that never arrives](https://blog.dugong.live/how-to-automate-gift-card-delivery-and-reminders-on-shopify.html), on Shopify's other one-shot email with no reminder behind it.

If you are a Shopify merchant with a shelf story, the bag that sat for a season, the customer who swore they were never told, the peak-season backlog you cleared by hand, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### How do I resend a ready for pickup notification on Shopify?

You cannot, natively. Shopify sends the Ready for pickup email exactly once, when you mark the order ready, and there is no resend button for it anywhere in the admin or the POS app. Shopify staff confirmed this in an October 2021 community thread, and the thread was still collecting requests for the button in April 2025. The workarounds merchants use: send the customer a manual email with the pickup details retyped, send the order status page link from the More actions menu on the order, or the template swap trick, where you temporarily paste the Ready for Local Pickup template code into the Contact customer email template so the reminder carries the real pickup details. Shopify Flow can send scheduled follow-ups on some plans, and the Admin API can trigger notifications programmatically. The durable fix is not any single resend but a schedule: a watcher that starts a clock when the order is marked ready and sends reminders at day two and day five without anyone remembering to.

Permalink: https://blog.dugong.live/how-to-handle-shopify-pickup-orders-customers-never-collect.html#faq-1

### Why is the resend button grayed out on my ready for pickup order?

Because the button you can see was never wired up for pickup notifications. Merchants first reported the grayed out resend control in the order timeline in October 2022, and a screenshot posted in August 2023 showed it still inert, which reads like the functionality exists but is not working. The resend that does work on a Shopify order is the order confirmation email, which is the wrong email for this job: it tells the customer what they bought, not that their bag is packed and waiting at the counter with an address and opening hours. A June 2022 reply in the same thread made the point plainly: there is no point resending the order confirmation when the pickup notice is the one that matters, especially when pickup details change and every affected customer must be emailed by hand. Until Shopify ships the button, treat the grayed out control as decoration and route reminders through a door that opens: a manual email, the order status link, the template swap, or an automation that sends on a schedule.

Permalink: https://blog.dugong.live/how-to-handle-shopify-pickup-orders-customers-never-collect.html#faq-2

### Can Shopify send automatic pickup reminder emails?

Not out of the box. Shopify's native pickup flow sends one Ready for pickup email at the moment you mark the order ready, and nothing afterward: no day three nudge, no final notice, no expiry warning. Merchants asked for exactly this, a reminder that can be set to send automatically after a few days, in threads dating to March 2021 and as recently as August 2024, and staff responses have been to pass the feedback along. The options today: Shopify Flow on eligible plans can wait a set number of days after fulfillment events and send or tag, third party apps built for payment reminders have been bent into pickup reminder duty, POS-adjacent apps handle it for specific carriers and lockers, and an AI automation layer like Dugong can watch for orders marked ready, wait your chosen interval, and send reminders on your template through email or SMS, escalating to a final notice and a ship-or-refund offer as the shelf date approaches. Whichever route you pick, the reminder schedule matters more than the tool: day two and day five catch most stragglers before the shelf does.

Permalink: https://blog.dugong.live/how-to-handle-shopify-pickup-orders-customers-never-collect.html#faq-3

### How long should you hold uncollected pickup orders before cancelling?

The retail convention is about seven days: a March 2021 community post noted that most high street chains return goods to stock and cancel the order after a week. Small merchants hold far longer, partly from kindness and partly because nothing in Shopify forces the decision, and the same thread records the cost of that: hundreds of uncollected orders after one peak season, some collected months after purchase, every one sifted by hand. A workable policy has three dates. Remind at day two. Remind again at day five, with a deadline named. At day seven, offer the customer a choice: we can ship this for a small fee, or refund it. At day ten to fourteen, cancel, refund, restock, and note the timeline. Publish the window on your pickup page and in the ready email so the cancellation is never a surprise. The policy only works if the dates fire themselves; a shelf policy that depends on someone remembering to check order ages during peak season is how the shelf got full in the first place.

Permalink: https://blog.dugong.live/how-to-handle-shopify-pickup-orders-customers-never-collect.html#faq-4

### Can AI automate pickup reminders and uncollected order handling on Shopify?

Yes, because the whole failure is a timer problem, and timers are what automation is for. An automation like Dugong watches for the moment an order is marked ready for pickup and starts a clock. Day two, a reminder goes out on your template with the address, hours, and what to bring. Day five, a firmer note with the shelf deadline. Day seven, a choice: switch to shipping for a fee, or take a refund. Day fourteen, the order is cancelled, refunded, restocked, and annotated, per the policy you wrote. Along the way it catches the cases a schedule alone misses: the ready email that bounced, the address that looks like a typo, the customer who replied asking to ship it, the order whose pickup location changed after the ready email went out. The honest limits: no automation walks the customer to your door, Shopify still lacks a native resend button so reminders travel through the invoice, contact, or app door instead, and a store policy still needs a human to write it. What changes is that the shelf stops being a memory test. Every bag has a clock, every clock has a next step, and the weekly report tells you the collection rate instead of the shelf telling you the backlog.

Permalink: https://blog.dugong.live/how-to-handle-shopify-pickup-orders-customers-never-collect.html#faq-5

---

Markdown rendition of https://blog.dugong.live/how-to-handle-shopify-pickup-orders-customers-never-collect.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
