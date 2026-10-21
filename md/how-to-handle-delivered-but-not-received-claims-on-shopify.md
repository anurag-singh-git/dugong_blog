# How to handle delivered but not received claims on Shopify

> Tracking says delivered, the customer says nothing came. The AI playbook that pulls carrier proof, runs the 48 hour play, and decides with evidence.

- Canonical: https://blog.dugong.live/how-to-handle-delivered-but-not-received-claims-on-shopify.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-08-07
- Updated: 2026-08-12
- Section: Research
- Word count: 2540
- Dispatch: Nº 102 · Research · 10 min read
- Full headline on page: How to handle delivered but not received claims *on Shopify*
- Keywords: delivered but not received shopify, shopify package says delivered but customer never received, customer claims package not delivered, item not received chargeback shopify, proof of delivery, porch piracy, missing package refund or reship, delivery claim automation
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

The email arrives Tuesday at 8:04 a.m., subject line all lowercase: package never came. The order is a $167 housewarming set, a candle, a throw, a note she wrote in the gift message field for her sister in Columbus. The tracking page says Delivered, Saturday, 2:41 p.m., front door/porch. Her email says her sister was home all weekend, that there is no package anywhere, and that she needs this fixed today.

You open the tracking page like it will settle something, and it says what she said it says. Delivered. That one word is your entire file, and it supports four different stories. The driver marked it delivered from the truck and it shows up tomorrow. It landed on the wrong porch, unit B instead of unit A, the gray house one street over. It landed on the right porch and someone [walked off with it](https://en.wikipedia.org/wiki/Package_theft). Or it is in the garage behind the paint cans, or nowhere at all, because a small share of these claims are not claims, they are refunds being farmed. Four stories, four different right answers, and the scan cannot tell you which one you are in.

Merchants ask about this every week, under titles like Package marked delivered but never received and Customer claims non-delivery, tracking shows delivered, and the replies always split into the same two camps. Refund it, the goodwill is worth more than the box. Never refund without proof, you will train every porch in the zip code. Both camps are right about the failure mode of the other one, which is how you know that neither camp has a policy. They have a mood.

## Delivered is a scan, not a doorstep

Start with the part almost nobody in the thread says out loud: the delivered scan is an event in a handheld, not a fact about a doorstep. Carriers run GPS-enabled scanners that let a driver mark a package delivered from the curb, and on a heavy route drivers batch-scan a street's packages before walking them, so the scan can run a stop, an hour, or a day ahead of the actual porch. This is common enough that the standard carrier guidance for a package marked delivered that is not there is simply to wait: most of them surface within 24 to 48 hours, walked back by the same driver who scanned them early.

The rest of the misses are geography and crime. Wrong-door drops cluster around duplexes, rear units, and buildings where the [address on the label](https://blog.dugong.live/how-to-validate-shipping-addresses-on-shopify.html) was two characters short of unambiguous. And package theft is common enough that the carriers themselves changed how they prove delivery: a signature line became a photograph of your doormat.

Which is the part almost nobody uses. FedEx runs Picture Proof of Delivery on residential deliveries released without a signature in the US and Canada: the driver photographs the package where it sits, and the photo appears on the tracking page, free, no account or login required. UPS attaches delivery photos to many residential stops the same way. USPS does not photograph doorsteps, but the delivery scan carries GPS coordinates, your local Post Office can read them back if you ask at the counter (the 800 number cannot), and at 7 business days you can file a Missing Mail search at missingmail.usps.com. [Proof of delivery](https://en.wikipedia.org/wiki/Proof_of_delivery) has quietly become better than it has ever been. It is also scattered across three carrier sites, gated behind the right question asked at the right counter, and pulled by nobody at 8:04 on a Tuesday with a queue building.

## What Shopify hands you when the claim lands

Inside the admin, the order timeline marches from label created to in transit to out for delivery to delivered, and stops. Delivered is the last word Shopify has on the subject. There is no claim object anywhere in the platform: no place to record what the customer said, what the photo showed, what you decided, or why. An order that is delivered and disputed looks exactly like an order that is delivered and fine, which means your store's most contested orders are indistinguishable from its most finished ones.

If you run [Shop Pay](https://help.shopify.com/en/manual/payments/shop-pay) you may believe you are covered, and this is the boundary worth reading twice. Shopify Protect protects eligible orders against fraudulent and unrecognized chargebacks: the cardholder who says I did not make this purchase. A customer who says the package never arrived files under item not received, a different reason code, and it is not on the list. The protected badge on the order does not change that. Merchants meet this edge at the exact moment they need it not to exist, dispute email in hand.

[Shopify Flow](https://help.shopify.com/en/manual/shopify-flow) gets you closer than nothing and stops short of useful. The one delivery-aware trigger, Fulfillment event created, fires on updates from third-party fulfillment services, picked up, in transit, delivered, and the documentation adds a line that decides the matter for half the stores reading this: manual fulfillment events do not start workflows. Fulfill by hand and even the delivered scan may pass Flow by. Either way, no trigger exists for the event that actually starts this problem, a customer typing nothing came, because that is an email, not a [webhook](https://shopify.dev/docs/apps/build/webhooks). Flow can [tag delivered orders](https://blog.dugong.live/how-to-automatically-tag-orders-on-shopify.html). It cannot hear a claim.

And nothing remembers. Helpdesks remember tickets, but orders do not remember claims, so the third nothing-came from the same address this year opens exactly like the first, assigned to whoever is on the queue, decided by whatever feels fair that afternoon. The serial claimer is not outsmarting your store. The store is simply not keeping score.

> **◆ NOTE** Three boundaries worth knowing before the next claim lands. Shopify Protect covers **fraudulent and unrecognized** chargebacks on eligible Shop Pay orders; item not received is neither. The USPS GPS readback comes from your **local Post Office counter**, not the 800 number, and the Missing Mail search opens at **7 business days**. And a delivered scan makes a carrier lost-package claim nearly unwinnable, so the useful ask is a **delivery investigation**, not a claim form.

## The decision you are actually making

Strip the fog away and a delivered-but-missing claim is a choice between four doors: wait, reship, refund, or deny. That is the entire decision space. What should pick the door is the evidence and the account, and what usually picks it is the clock, because the ticket is aging, the queue is long, and a refund is the only button that closes it in one click.

Refund-by-default has a compounding cost that never appears on the ticket. Word travels, the same building files again, and the claims concentrate exactly where they are easiest to make. Deny-by-default costs more per incident: the honest customer goes to her bank, the dispute comes back as item not received, and your only evidence is the same scan she already told you was wrong. Without a photo, a signature, or coordinates, [you lose most of those](https://blog.dugong.live/how-to-win-chargeback-disputes-on-shopify.html), plus the chargeback fee, plus a review that names your store and the word stolen in the same sentence.

In between the two defaults sits the process nobody staffs: ask the customer to check with neighbors, wait two days, pull the photo, ask the counter for coordinates, file the trace on day 7. Every step is real, every step works sometimes, and every step is hand-typed by a support person who also has [forty where-is-my-order tickets](https://blog.dugong.live/how-to-reduce-where-is-my-order-wismo-tickets-on-shopify.html) from customers whose packages are merely slow. The evidence decays while the queue catches up: the photo is easiest to pull this week, the counter remembers this month, and the trace filed late is a trace filed for the record.

## What the automation actually has to do

The fix is what a careful operations person would do with unlimited attention: treat every claim as a case, gather the proof while it is fresh, give the honest 48 hours room to work, and make the decision by a policy the store wrote down in advance. As a Dugong playbook, in plain prose:

```
# trigger
On every message that says a delivered
package never arrived, on any channel

# steps
1. Hear the claim: match sender to order,
   open a case file on the order itself
2. Pull the proof while it is fresh: scan
   time, carrier photo, GPS readback,
   address match, AVS, signature status
3. Run the 48 hour play: same-hour reply
   with photo and checklist, day-2 follow
   up, trace and Missing Mail on schedule
4. Score the claim: value against cost,
   first time or pattern, what the
   photo actually shows
5. Decide by policy: reship with signature,
   refund, hold for the trace, or deny
   with the file attached
6. Execute end to end: duplicate order,
   tagged refund, evidence-backed denial,
   chargeback response drafted early
7. Report weekly: claims by carrier, zip,
   and SKU, cost per decision, and the
   addresses that keep coming back
```

The same-hour reply in step three is doing three jobs at once. It buys the 24 to 48 hour window honestly, with a message that reads as action instead of stalling: here is the driver's photo, here is where the scan placed it, could you check the side door and the building office while we open a trace. It resolves a real share of cases on sight, because the photo either shows her doormat or it shows a porch she has never seen, and both answers end the mystery. And it timestamps your diligence, which the bank will weigh months later if this becomes a dispute. The day-2 follow-up catches the packages that surfaced. The day-7 filings catch the ones that did not.

Steps four and five are where your judgment gets encoded instead of improvised. A policy paragraph most stores would recognize: under $75, first claim, clean history, reship at once with a warm note and eat it at cost. Between $75 and $250, run the full 48 hours, then reship or refund by stock and margin. Above $250, nothing moves until the GPS readback and the trace come home, and the replacement ships signature required. Deny only on pattern plus evidence, politely, file attached. The thresholds are yours and the point is that they exist before the ticket does, so the queue stops making portfolio decisions one mood at a time.

Step six is the part that turns a decision into an afternoon saved. The reship is a duplicated order with signature required added and the original tagged. The refund carries a reason your reports can read. The denial goes out with the photo, the coordinates, and the timeline attached, which is the version of no that fewest people escalate. And the chargeback response is drafted the day the claim closes, delivery confirmation to the AVS-matched address, photo, correspondence, all of it, so if the bank letter comes anyway you are attaching a file, not reconstructing a month-old argument. The weekly report closes the loop upstream: claims by carrier, by zip, by SKU, the signature threshold doing its job, and the two addresses that have now claimed three times, which your [block list](https://blog.dugong.live/how-to-block-a-customer-on-shopify.html) should hear about.

## Why this is a compiler problem, not an app problem

The apps in this category are insurance, and it is worth being precise about what that means. Shipping protection widgets add a dollar or two at checkout, and when a package goes missing they settle: a reorder or a refund, funded by the pool. That is a real product and for some stores the right one. But it answers a different question than the one the Tuesday email asks. It prices the loss; it does not investigate it, does not pull the photo, does not remember the address, does not tune your signature threshold, and your customers pay the premium whether their block has ever lost a box. Your actual policy, the one with thresholds and exceptions and a memory, is a paragraph with judgment folded into every clause, and no settings page has a field for it. This is the argument behind [the automations no one builds](https://blog.dugong.live/best-shopify-automations-to-set-up.html): describe the paragraph in plain language and let a compiler turn it into the running workflow, instead of shaving your policy down until it fits an insurance product.

Run the Tuesday email again with the paragraph running. The claim lands at 8:04 and the case file exists by 8:05: FedEx photo pulled, brick steps and a terracotta planter, AVS matched, first claim on the account. The reply goes at 8:09 with the photo attached. At 9:40 the sister writes back: that is the house behind ours, and by evening the box is on the right porch, case closed, wrong-door note filed with the carrier. Or the photo shows her own doormat, 48 hours pass, nothing surfaces, and the $167 replacement ships Thursday, signature required, because the policy says a first claim under $250 with a clean history gets believed. Or it is February, the third claim from that address this year, and the reply is the file, not a refund. Three endings, one system, zero improvisation.

## The workflow worth building this week

Start with the autopsy. Export the last two quarters of refunds and search the reasons for never arrived, lost, and stolen. Total it, and then open five of them and ask one question: what evidence existed that nobody pulled? Most stores find full retail refunds sitting next to delivery photos that were free on the tracking page the whole time, and a number that funds this project by lunch.

Then run the playbook in draft mode for two weeks: let it open the case files, propose each reply, and stage each decision without sending anything. You are auditing its judgment, not its typing. Does it wait where you would wait, believe the first-timer you would believe, hold the $400 order your gut would hold, recognize the address you already distrust. When fifty proposals in a row match your calls, let the clean cases run and keep the denials and the big ones for a human, which is where they belonged all along.

Then say the paragraph out loud, the way you would brief a new hire. Answer every nothing-came inside the hour, with the photo. Give honest packages 48 hours to surface. Reship small, verify big, deny patterns with the file attached, and put a signature on everything over the line we set. Never let the same address surprise us twice. And tell me on Fridays what it cost, what it saved, and which carrier keeps scanning early. That is the brief. The compiler turns it into the workflow, and the delivered scan goes back to being good news, which is the only thing it was ever supposed to be.

> **◆ READING** Two companion pieces if this one landed: [the chargeback you lose by default](https://blog.dugong.live/how-to-win-chargeback-disputes-on-shopify.html), for when the claim skips you entirely and goes to the bank, and [the WISMO tickets that eat your afternoon](https://blog.dugong.live/how-to-reduce-where-is-my-order-wismo-tickets-on-shopify.html), on the gentler cousin where the package is merely late. Also worth reading: [the refund you gave for nothing](https://blog.dugong.live/how-to-handle-shopify-returns-the-customer-never-sends-back.html), on the same missing parcel pointed the other way down the pipe.

If you are a Shopify merchant with a refund log full of the word stolen, a delivery photo you found three weeks too late, or an address you have quietly stopped shipping to, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Who is responsible when a package is marked delivered but the customer says it never arrived?

Practically, the merchant is. The carrier's contract ends at the delivery scan, and a package with a delivered status is nearly impossible to claim as lost: UPS and FedEx will open a delivery investigation, and USPS accepts a Missing Mail search after 7 business days, but a scan with GPS coordinates at the right address usually closes the case in the carrier's favor. The card networks point the same direction: if the customer disputes the charge as item not received, the burden of proof is on the merchant, and the winning evidence is delivery confirmation to the address on the order, an AVS match from checkout, a delivery photo, and a signature for high-value shipments. A shipping policy page that says not responsible for stolen packages does not bind the customer's bank. So the practical question is not who is responsible but what evidence you can produce and how fast: the photo, the GPS readback, and the correspondence, gathered while the claim is hours old, decide most cases either way.

Permalink: https://blog.dugong.live/how-to-handle-delivered-but-not-received-claims-on-shopify.html#faq-1

### Does Shopify Protect cover delivered but not received chargebacks?

No. Shopify Protect protects eligible Shop Pay orders against fraudulent and unrecognized chargebacks, the disputes where a cardholder says the purchase was not authorized or not recognized. A customer who says the package never arrived files under item not received, which is a different reason code and is not covered, even on an order wearing the protected badge. That distinction surprises merchants at the worst moment: the order says protected, the dispute arrives, and the response is still yours to build. For item not received disputes you respond with delivery evidence: tracking showing delivered to the address on the order, the delivery photo if the carrier took one, GPS coordinates from the carrier if you requested them, the AVS result from checkout, and your correspondence with the customer. Signature confirmation is the strongest single item and worth requiring automatically above a value threshold you choose.

Permalink: https://blog.dugong.live/how-to-handle-delivered-but-not-received-claims-on-shopify.html#faq-2

### Should I refund, reship, or deny when tracking shows the package was delivered?

Wait first, then decide by evidence and history, not by mood. Carriers mark packages delivered early often enough that the standard guidance is to give it 24 to 48 hours: reply in the first hour with the delivery photo and a short checklist covering household members, neighbors, side doors, and the building office, and a real share of claims close themselves when the package surfaces or the photo shows someone else's porch. If nothing surfaces, split by stakes. A first claim from a customer with clean history on a low-value order is a reship or refund: the goodwill costs you the product at cost, and fighting it costs more. A high-value order waits for the GPS readback and the carrier trace before anything moves, and ships again only with signature required. A repeat pattern, whether the same customer, the same address, or the same building cluster, gets a polite denial with the evidence file attached, because paying it once more buys the next claim. Put thresholds on those doors in advance so the queue stops improvising.

Permalink: https://blog.dugong.live/how-to-handle-delivered-but-not-received-claims-on-shopify.html#faq-3

### Do carriers provide photo proof of delivery for disputed packages?

Yes, and it is better evidence than most merchants realize they have. FedEx runs Picture Proof of Delivery on residential deliveries released without a signature in the US and Canada: the driver photographs the package where it sits, and the photo appears on the tracking page, free, with no account or login required. UPS attaches delivery photos to many residential stops the same way. USPS does not photograph doorsteps, but its delivered scan carries GPS coordinates, and your local Post Office counter can read them back if you ask there rather than calling the 800 number; at 7 business days you can also file a Missing Mail search. The catch is that none of it arrives on its own. The evidence sits scattered across three carrier sites, gated behind the right question, so at 8:04 on a Tuesday with a queue building, nobody pulls it.

Permalink: https://blog.dugong.live/how-to-handle-delivered-but-not-received-claims-on-shopify.html#faq-4

### Can Shopify Flow detect a delivered but not received claim?

No. The claim is a customer typing nothing came, and that is an email, not a webhook, so no Flow trigger exists for it. The closest trigger, Fulfillment event created, fires on updates from third-party fulfillment services as a package moves through picked up, in transit, and delivered, and the documentation adds the line that decides the matter for half the stores reading it: manual fulfillment events do not start workflows. Fulfill by hand and even the delivered scan may pass Flow by. So Flow can tag delivered orders, but it cannot hear a claim, and nothing native records one either. Shopify has no claim object, so an order that is delivered and disputed looks identical to one that is delivered and fine, and the third nothing-came from the same address this year opens exactly like the first.

Permalink: https://blog.dugong.live/how-to-handle-delivered-but-not-received-claims-on-shopify.html#faq-5

---

Markdown rendition of https://blog.dugong.live/how-to-handle-delivered-but-not-received-claims-on-shopify.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
