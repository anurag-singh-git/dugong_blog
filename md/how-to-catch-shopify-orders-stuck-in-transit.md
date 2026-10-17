# How to catch Shopify orders stuck in transit before your customer does

> The first scan comes in, then six days of silence, and the customer notices before you do. The AI playbook that catches stuck Shopify shipments in time.

- Canonical: https://blog.dugong.live/how-to-catch-shopify-orders-stuck-in-transit.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-08-12
- Updated: 2026-08-13
- Section: Research
- Word count: 2740
- Dispatch: Nº 105 · Research · 10 min read
- Full headline on page: How to catch Shopify orders *stuck in transit* before your customer does
- Keywords: shopify order stuck in transit, shopify tracking not updating, package stuck in transit, tracking added not updating, shipment stopped moving, stalled shipment alert, shopify flow tracking, usps missing mail search, lost package claim, proactive shipping updates
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

Order 2213 ships on a Wednesday morning: a $140 dinnerware set, label bought in the admin at 10:20, tracking number emailed to the customer before lunch. That evening the first scan lands, accepted at the regional facility, and everyone involved stops thinking about the box, which is the correct response to a working system. Thursday brings no scan. Friday brings no scan. The weekend passes in silence, and on Monday the tracking page still shows one line, five days old, like a heartbeat monitor that beeped once.

The customer checks the link Tuesday, twice, the way people check a phone that has stopped ringing. Wednesday, day six, she writes: is my order lost? And that email is the first time anyone at the store learns something is wrong, because nothing in the stack was ever going to mention it. The order page looks perfect. Fulfilled, green, tracking attached. Support opens the same tracking page she did, sees the same lone scan, and types the sentence every merchant has typed with slightly gritted teeth: we are looking into it with the carrier. Nobody is looking into it with the carrier. Nobody knows how.

The stuck package is the middle silence of shipping, and the genre has three. Before the label, there is the order that has not shipped yet, the [delay nobody announces](https://blog.dugong.live/how-to-notify-customers-of-shipping-delays-on-shopify.html). After the last scan, there is the box that says [delivered but never arrived](https://blog.dugong.live/how-to-handle-delivered-but-not-received-claims-on-shopify.html). Between them sits the shipment that launched, scanned once, and went dark: the only shipping problem that consists entirely of nothing happening. It is also the one Shopify is structurally unable to see.

## Every alert Shopify has needs an event

Follow the machinery and the blindness makes sense. When a carrier scan arrives, Shopify advances the shipment status on the order, Tracking added, then In transit, then Out for delivery, then Delivered, and the customer-facing [tracking](https://en.wikipedia.org/wiki/Package_tracking) timeline moves with it. The developer docs define eleven fulfillment event statuses a shipment can post, from label_printed and picked_up through attempted_delivery and failure, and the list even includes delayed, a status expressly reserved for a fulfillment running late. Emails exist at every milestone: a shipping confirmation when the label goes on, out for delivery and delivered notices as the scans come in, a shipping update template for when tracking changes. It is a complete nervous system, and every neuron in it fires on an event arriving.

A stall never sends the event. Six days of silence produce six days of no triggers, no status change, no email, no badge, nothing to filter for, because the system records what carriers say and a stuck package says nothing. The delayed status sits in the schema waiting for a carrier integration to post it, and mid-transit, for a package sitting in the wrong corner of a sort facility, effectively none do. The absence has edges worth knowing. Shipment status only advances for carriers Shopify recognizes, so a label from an unrecognized or misdetected carrier keeps the order on Tracking added for its entire, possibly flawless journey. An order shipped with no tracking number at all simply stays On its way until someone manually marks it delivered. In every case the admin renders the same calm: a chip that stopped changing, indistinguishable from a chip that never could.

> Every email Shopify can send is triggered by something happening. The stuck package is the one problem made entirely of nothing happening.

## The alert merchants keep asking for

This is not a gap merchants have failed to notice. In May 2024 a Shopify Plus merchant opened a community thread with the whole use case in two sentences: packages travel for two weeks without any tracking update and remain on Tracking added, so they wanted a Flow that would tag and alert those orders after X days, so we can take actions before customers complaining. The phrasing is imperfect and the product spec is perfect. A Flow product manager replied a month later, helpfully and damningly: the status lives at `order / fulfillment orders / fulfillments / displayStatus`, the Fulfillment event created trigger might help depending on what you used to fulfill, and knowing how long a shipment has sat in a status would be difficult without storing it yourself, or potentially using a Wait step.

Read that answer again, because it is the platform describing its own ceiling. Store the state yourself: Flow does not remember. A Wait step: park every fulfillment in a timer, wake up once, check one field, and hope the delay you picked suits every carrier, service, and destination you ship. The thread is not alone. February 2025, another merchant asks for email notifications for orders in transit longer than 7 days. December 2025, another wants not-delivered orders flagged into a spreadsheet, and the thread sits at zero replies. Meanwhile the adjacent threads report the same chip from the other side, orders stuck on Tracking added while the carrier's own site shows the package delivered, which means merchants cannot even trust the silence to mean silence.

> **◆ NOTE** The boundaries, in one place. Shipment status advances **only for carriers Shopify recognizes**; everything else stays on Tracking added. The event model has **eleven statuses including delayed**, and nothing in the admin acts on a status that never arrives. [Shopify Flow](https://help.shopify.com/en/manual/shopify-flow) has **no duration-in-state trigger**; the staff-suggested workaround is storing state yourself or Wait steps. And the carrier clocks are short: **USPS accepts a Missing Mail search 7 days after mailing**, **UPS opens claims 24 hours after the scheduled delivery date** and wants notice inside **60 days of the ship date**, with FedEx on a similar window.

## The carrier clocks run whether you watch or not

The reason a stall deserves an alarm, rather than patience, is that three clocks start the moment a package goes quiet, and none of them belong to you. The first clock is the network's. Parcels routinely go 24 to 72 hours between scans inside a domestic system and still arrive on time; economy services that ride one carrier's linehaul and hand the [last mile](https://en.wikipedia.org/wiki/Last_mile_(transportation)) to the postal service go dark longer than that by design. Silence has a normal length, and the normal length differs by carrier, service, and lane, which is precisely why one global X-days slider never fits. Distinguish the first mile while you are at it: a label with no acceptance scan after a day has usually not left your building, and the correct response is a walk to the packing bench, not an apology about carrier delays. The box is on a shelf. It is on a shelf more often than anyone likes to admit.

The second clock is the customer's. Descartes surveyed 8,000 consumers across North America and Europe and found 67 percent had hit a delivery problem in just the preceding three months, and 63 percent of those took some action against the brand for it: fewer orders, a warning to friends, or gone entirely. Note who absorbs the punishment. The carrier lost the box, and the store loses the customer, because the store is who they paid. Every day of silence after the promised date converts a shipping incident into a trust incident, and past a certain point the customer stops writing emails and starts a payment dispute, where an item-not-received claim with no delivery scan is a [chargeback you will not win](https://blog.dugong.live/how-to-win-chargeback-disputes-on-shopify.html).

The third clock is the carrier's own bureaucracy, and it is the one merchants discover last. USPS will accept a Missing Mail search request once 7 days have passed since the mailing date, and its insurance claims run on windows measured from that same date. UPS lets you open a claim as soon as 24 hours after the scheduled delivery date passes, and wants notice of a lost package inside roughly 60 days of shipment. FedEx traces run on the same order of magnitude, with claim windows around 60 days. Every one of those clocks starts at the label, not at the moment you notice. A stall that surfaces on day 12, because that is when the customer finally wrote in, has already spent a fifth of the claim window doing nothing. The trace that would have found the box in a Des Moines sort facility on day 5 gets filed on day 13 instead, and the reimbursement that would have covered the reship quietly expires unclaimed.

## What the automation actually has to do

None of this requires new information. Every input already exists: the fulfillment date, the [tracking number](https://blog.dugong.live/how-to-automatically-add-tracking-numbers-to-shopify-orders.html), the last scan and its timestamp, the promised delivery window, the customer's order history, and the carrier's own trace and claim procedures, published and stable for years. What is missing is the worker who checks the silent ones on a schedule. As a Dugong playbook, in plain prose:

```
# trigger
On every open fulfillment, from first
scan to doorstep, checked daily

# steps
1. Learn the lane: normal scan rhythm
   and delivery window per carrier,
   service, and destination
2. Watch the first mile: no acceptance
   scan in 24 hours means the warehouse,
   not the carrier
3. Flag the stall: silence past the
   lane's rhythm, about 3 days domestic,
   5 to 7 cross-border, opens a case
4. Tell the customer first: the honest
   status and the next update's date,
   before they check twice
5. Open the trace on the carrier's
   clock: USPS at day 7, UPS the day
   after due, claims inside the window
6. Decide the save: reship or refund by
   value, stock, and history, not by
   the carrier's verdict
7. Report the lanes: stall and loss
   rate per carrier and service,
   monthly, so volume moves
```

Steps one through three are the detection Shopify never shipped. The baseline matters because a useful alarm is a quiet one: flag every 48-hour gap and the alerts channel becomes wallpaper by Thursday; learn that this carrier's ground service scans daily while that consolidator goes dark for four days crossing a border, and the flag means something every time it fires. The first-mile check earns its keep fastest, because the package with a label and no acceptance scan is the one stall you can fix with your own hands, today, by finding the box before the apology instead of after.

Step four is where the economics change. The customer who hears from you on day 4, your package went quiet in transit, we are already on it with the carrier, next update Friday, writes zero emails and tells the story as good service. The customer who discovers the stall alone on day 8 writes three, and some fraction of her cohort files the dispute instead. Proactive is not a tone, it is a race: the note must exist before the second tracking-page visit, which is why it cannot depend on a human remembering to sweep a spreadsheet on the right morning. The message states what is known, what happens next, and when they will hear again, and then the next update actually arrives, because the same agent that sent the first one owns the follow-through.

Steps five and six are the carrier-side work that support teams improvise today, standardized. The Missing Mail search goes in the day the package becomes eligible, with the mail class, addresses, and contents description already filled from the order. The UPS claim opens the day after the due date passes, not three weeks later when someone finds the tab. And the save decision runs on your policy rather than the carrier's timetable: a $38 order with stock on hand reships immediately, because the goodwill is worth more than the second unit; a $600 order waits for the trace and reships with signature required; the address on its third lost package this quarter gets the evidence file treatment instead of the benefit of the doubt. The carrier's reimbursement, when it comes, lands as a bonus rather than a bottleneck.

Step seven turns incidents into leverage. One lost box is weather; a stall rate is data. When the monthly report shows the economy service saving $1.10 a label and going dark for five days on one lane in eight, the cheap label stops being obviously cheap, and the case for moving that lane, or for billing the rep with numbers attached, writes itself.

## Why this is a compiler problem, not an app problem

Tracking apps exist, and the good ones do real work: branded tracking pages, milestone emails, an exceptions dashboard with a stalled-shipments tab. What they ship is a dashboard plus a threshold slider, and what the problem actually contains is judgment that differs at every store: which lanes go quiet harmlessly, what day the note should go out and what it should promise, when a trace beats a reship and when the reverse, which customers get the instant save and which addresses get scrutiny, what loss rate finally justifies switching carriers. That is a paragraph of policy, not a settings page, and it is the argument behind [the automations no one builds](https://blog.dugong.live/best-shopify-automations-to-set-up.html): the paragraph should compile into the workflow, instead of being shaved down to whichever checkboxes the dashboard happened to ship.

Run order 2213 again with the paragraph compiled. Wednesday the label goes on, the evening scan arrives, the agent files the shipment under a lane that normally scans daily. Thursday is quiet, within rhythm. Friday, day 2 of silence, is not, and a case opens while the customer still thinks about other things. Saturday she gets the note before her first worried check: went quiet in transit, on it with the carrier, update Wednesday. Wednesday the Missing Mail search goes in the hour it becomes eligible, order details already attached. Thursday the box surfaces at a sort facility two states sideways, and Saturday it lands, ten days late and zero emails angry, the whole incident costing the store one proactive message and a trace request that filed itself. The claim window closes a month and a half later, untouched, because it was never needed. Nobody at the store did anything except read a weekly digest with one line in it.

## The workflow worth building this week

Start with the audit Shopify will not volunteer. Pull every order fulfilled more than ten days ago that has no delivered scan, and sort the silence into its three species: labels with no acceptance scan, which are probably still in your building; shipments on Tracking added whose carrier was never recognized, which are a settings fix; and true mid-transit stalls, which are cases. Check the oldest ones against the claim windows they have left. Most stores find at least one package whose window has already closed, which is the tuition for this particular lesson, paid once.

Then run the playbook in draft mode for two weeks: let it flag stalls, draft the customer notes, prepare the traces, and send nothing. You are auditing its judgment against yours. Would you have flagged that lane on day 3 or given it four? Is the note worded the way you would say it? When its calls match yours, let the clean paths run, and keep the expensive saves and the odd cases for a human, which is where they belonged all along.

Then say the brief out loud, the way you would hand shipping to a new hire. Watch every package from the first scan. Know what normal silence looks like on each lane, and flag anything longer. If the label never gets scanned, check our own shelves first. Tell the customer before they notice, with a real status and a real date. Open the trace the day the carrier allows it, file every claim inside its window, reship by our policy, and show me once a month which lanes keep going quiet. That is the whole paragraph. The compiler turns it into the workflow, and the next box that stops moving gets found by your system instead of your customer.

> **◆ READING** Two companion pieces if this one landed: [the where-is-my-order tickets that eat your afternoon](https://blog.dugong.live/how-to-reduce-where-is-my-order-wismo-tickets-on-shopify.html), on answering the question before it gets asked, and [the package that says delivered but never arrived](https://blog.dugong.live/how-to-handle-delivered-but-not-received-claims-on-shopify.html), on the silence that starts after the last scan instead of between scans.

If you are a Shopify merchant with a horror story about a box that sat in a sort facility for three weeks, a support inbox that fills with is-my-order-lost emails every December, or a claim you missed by four days, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Why is my Shopify order stuck on Tracking added?

Tracking added means Shopify has a tracking number but has not seen a carrier scan it can read, and there are three common reasons the chip never moves. First, carrier support: the shipment status on the order only advances for carriers Shopify recognizes, so a label from an unrecognized or misdetected carrier sits on Tracking added for the whole journey even while the package moves normally, and selecting the right carrier from the dropdown during fulfillment is the fix. Second, the first mile: a label that was printed but never received an acceptance scan has usually not left your building, which means the package is on a shelf or in a bin the pickup missed, and no amount of waiting on the carrier will move it. Third, a real stall: the package was scanned once and then stopped. The three cases need three different responses, a settings fix, a warehouse walk, and a trace with the carrier, which is exactly why a chip that cannot tell them apart is not enough information to act on.

Permalink: https://blog.dugong.live/how-to-catch-shopify-orders-stuck-in-transit.html#faq-1

### How long should a package go without tracking updates before you do something?

Set thresholds by lane rather than one global number. Inside a domestic network, parcels routinely go 24 to 72 hours between scans and still arrive on time, so a domestic shipment is worth flagging around day 3 of silence. Economy services that hand off between carriers and anything crossing a border go dark longer by design, so 5 to 7 days is a saner line there. The first mile is stricter: a label with no acceptance scan within 24 to 48 hours usually means the package never left, and that check points at your own warehouse rather than the carrier. What matters most is that the flag beats two other clocks: the customer, who typically notices somewhere past the promised date and blames the store, and the carrier windows, since USPS accepts a Missing Mail search once 7 days have passed since mailing, UPS lets a claim open 24 hours after the scheduled delivery date passes and wants notice within 60 days of the ship date, and FedEx runs on a similar order of 60 days. A stall you notice on day 12 has already spent a fifth of the claim window.

Permalink: https://blog.dugong.live/how-to-catch-shopify-orders-stuck-in-transit.html#faq-2

### Can Shopify Flow alert me when tracking stops updating?

Not directly, because Flow's shipping triggers fire when events arrive, and a stalled shipment is defined by events not arriving. Merchants have asked for exactly this alert on the community forums, orders with no tracking movement after a number of days, and the staff answer points at the fulfillment displayStatus field buried under order, fulfillment orders, fulfillments, and concedes that knowing how long a shipment has sat in a status would require storing the state yourself or building chains of Wait steps that re-check later. That workaround re-checks once, applies one global delay to every carrier and lane, and forgets everything between runs. It also cannot see the difference between a missing first scan and a mid-transit stall, and it cannot open a Missing Mail search or draft the customer note when it fires. An agent that watches every open fulfillment on a schedule, knows each lane's normal rhythm, and owns the next three steps, the customer message, the carrier trace, and the reship decision, is the version of the alert that actually ends the problem.

Permalink: https://blog.dugong.live/how-to-catch-shopify-orders-stuck-in-transit.html#faq-3

### Why doesn't Shopify have a delayed shipment status?

It has one and nothing posts it. The developer docs define eleven fulfillment event statuses a shipment can carry, from label_printed and picked_up through attempted_delivery and failure, and the list includes delayed, a status expressly reserved for a fulfillment running late. But every status advances only when a carrier integration posts the event, and mid transit, for a package sitting in the wrong corner of a sort facility, effectively none do. The whole notification system is built the same way: emails exist at every milestone, and every one fires on an event arriving, so six days of silence produce no status change, no email, and nothing to filter for. The edges are worth knowing too: an order shipped with no tracking number at all simply stays On its way until someone manually marks it delivered, indistinguishable from a chip that never could change.

Permalink: https://blog.dugong.live/how-to-catch-shopify-orders-stuck-in-transit.html#faq-4

### Should I tell the customer before they notice their package is stuck?

Yes, and the note has a deadline: it must exist before the second tracking-page visit. Descartes surveyed 8,000 consumers across North America and Europe and found 67 percent had hit a delivery problem in just the preceding three months, and 63 percent of those took some action against the brand, fewer orders, a warning to friends, or gone entirely. The carrier lost the box; the store loses the customer, because the store is who they paid. The customer who hears on day 4 that the package went quiet and the next update comes Friday writes zero emails and tells the story as good service. The one who discovers the stall alone on day 8 writes three, and some fraction of her cohort files the payment dispute instead, where an item not received claim with no delivery scan is a chargeback you will not win.

Permalink: https://blog.dugong.live/how-to-catch-shopify-orders-stuck-in-transit.html#faq-5

---

Markdown rendition of https://blog.dugong.live/how-to-catch-shopify-orders-stuck-in-transit.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
