# How to automatically capture payments on Shopify

> Authorized is not paid: Shopify gives you 7 days to capture before the hold expires. The AI playbook that captures every order before the clock runs out.

- Canonical: https://blog.dugong.live/how-to-automatically-capture-payments-on-shopify.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-08-03
- Updated: 2026-08-07
- Section: Research
- Word count: 2412
- Dispatch: Nº 99 · Research · 10 min read
- Full headline on page: How to automatically capture payments *on Shopify*
- Keywords: capture payment Shopify, Shopify capture payment automatically, Shopify payment authorization expired, authorized but not paid Shopify, manual payment capture Shopify, Shopify 7 day authorization period, capture payment when order fulfilled, expired authorization Shopify
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

The order lands on a Sunday at 11:47 p.m.: two pairs of boots, $412, a new customer, a billing address one state away from shipping. You are on manual capture for exactly this moment, because a rough month of [card testing](https://blog.dugong.live/how-to-stop-card-testing-attacks-on-shopify.html) taught you to look before you charge. Monday morning you look. The [risk signals](https://blog.dugong.live/how-to-handle-high-risk-orders-on-shopify.html) come back reasonable, the customer answers a quick verification email by lunch, and at 4 p.m. the boots are packed, labeled, and gone. The tracking updates Tuesday. The customer is delighted.

Nobody clicks Capture payment. Not out of carelessness, exactly. Fulfillment feels like the end of an order, the admin shows a tidy Fulfilled badge, and the one thing still open is a payment status quietly reading Authorized in a column nobody sorts by. The authorization [Shopify Payments](https://help.shopify.com/en/manual/payments/shopify-payments) created on Sunday night is good for 7 days. On Thursday at 11:47 p.m. it expires, the hold releases, and $412 goes back to the customer's available balance while her boots sit by her door.

You find out three weeks later, doing the month's [payout reconciliation](https://blog.dugong.live/how-to-reconcile-shopify-payouts-with-your-sales.html): an order that shipped, a payout that never included it, and a payment status you have to squint at to believe. The product is gone, the shipping is spent, and your only path to the $412 is an email asking a stranger to pay for boots she has worn twice. Merchants post this exact autopsy in the community every month, under titles like Payment Authorized but not Paid and Fulfilled orders are not paid. The answers are always the same, and always a week too late.

## Authorized is not paid

Card payments on Shopify happen in two steps. Authorization checks the card and places a hold for the amount. Capture is the part where money actually moves. On the default setting, Automatically at checkout, the two happen together and you never think about it. The moment you switch to anything else, a clock starts on every order: Shopify Payments gives you a 7 day authorization period, and the help center is blunt about the stakes. You need to capture payment before the authorization period ends to receive any money for the order.

Stores leave the default for good reasons. Fraud review before charging, so a suspicious order can be [cancelled](https://blog.dugong.live/how-to-let-customers-cancel-their-own-orders-on-shopify.html) without a refund ever appearing on a statement. Made-to-order and [preorder catalogs](https://blog.dugong.live/how-to-set-up-pre-orders-on-shopify-without-holding-in-stock-items.html) that charge at shipment, either by policy or by local regulation. Accounting standards that recognize revenue at fulfillment. B2B flows where the terms are not card-shaped. All of them are sensible. All of them turn getting paid into a deadline.

Shopify offers four capture settings under Settings, then Payments: automatically at checkout, automatically when the entire order is fulfilled, automatically per fulfillment on Shopify Plus, and manually. The names read like a solved problem. The fine print under each one is where the boots money goes.

## The four settings, and the traps inside them

Manual capture is honest about what it is: a human clicking a button on every order before day 7. Its one safety net is a checkbox that emails you a warning 1 day before an authorization expires. One email, per order, into the same inbox as everything else, with roughly 24 hours left on the clock. If your fraud reviewer is out Friday, the warning for Sunday's orders lands while nobody is watching, which is the exact hour the race is usually lost.

Capture at fulfillment sounds like the fix, and for simple orders it is. Then a size 11 goes on backorder and the order splits. Shopify's documentation says it plainly: the entire order must be fulfilled, and partially fulfilled orders won't be captured. Ship one box of two and no capture fires, no warning distinguishes this order from any other, and the authorization runs out its clock behind a Partially fulfilled badge that looks like progress. Stores that split shipments, fulfill from multiple locations, or mix instant digital items with physical ones live in this gap permanently.

> **◆ NOTE** Three more documented edges, all quiet. The fulfillment setting **only applies to orders placed after you activate it**, so the existing queue stays manual. Fulfillment apps that require a paid status before they start **deadlock** against a capture that waits for fulfillment: the app waits for paid, the capture waits for shipped, and the order waits for day 7. And a foreign currency payment converts at the rate on **capture day, not authorization day**, so a slow capture can shrink on the way in.

Shopify Plus stores get extended authorization periods with Shopify Payments: up to 30 days on Visa, Mastercard, and American Express, up to 10 on Discover and JCB, 7 on Diners Club and China UnionPay, depending on the issuing bank. Longer rope, new knot: capture after the standard 7 days and Shopify adds a 1.75% charge on top of your regular processing fees. A store that leans on the 30 day window as a buffer is paying a quiet tax on every order that needed it, and the expiry date still arrives, card by card, on a schedule no one memorizes.

And when the clock does run out, there is no recovering the original authorization. Shopify's guidance is to cancel the order and create a new one, or contact the customer and arrange payment again. Which is to say: the platform's plan for an expired authorization is that you start over, with a customer who already has the product and no longer has a reason to type a card number.

## What stores do about it today

The folk remedies are all real and all partial. The warning email gets turned on and then filtered, batched, or buried; it also fires per order, so a busy weekend produces a Monday wall of them. Calendar reminders and a pinned spreadsheet work until the person who owns them takes a vacation. Some teams run [tagging conventions](https://blog.dugong.live/how-to-automatically-tag-orders-on-shopify.html), capture-by-Wednesday columns, or a standing 9 a.m. sweep of the Authorized filter, which is a fine system for eleven orders a week and a liability at a hundred.

[Shopify Flow](https://help.shopify.com/en/manual/shopify-flow) deserves an honest word, because Flow can do the famous version of this: the template that captures payment when an order is not high fraud risk exists, it works, and if your entire policy is capture everything Shopify does not flag, you should turn it on today and stop reading. But watch what it cannot hold. It cannot wait for your actual fraud process, the one with a verification email and a human yes. It cannot capture when the first box ships instead of the last. It cannot notice a day-six authorization and chase the decision that is blocking it. It cannot choose between capturing and voiding when the order is being cancelled. It runs one rule at one moment, and your capture policy is not one rule. It is a paragraph.

## What the automation actually has to do

The fix is what a careful finance person would do if they watched every authorization all day: know each order's real deadline, charge it the moment your policy says it is safe, and raise exactly the right alarm when something blocks the charge. As a Dugong playbook, in plain prose:

```
# trigger
On every new authorization, and every day
after, until captured, voided, or expired

# steps
1. Watch each authorization with its real
   deadline: provider, card type, expiry
   hour, and the fee cliff at day 7
2. Capture on the trigger your policy names:
   fraud check passed, order fulfilled,
   first shipment out, preorder released
3. Handle the split shipment: capture the
   whole order at first box, or per
   fulfillment where the plan allows it
4. Escalate day-5 authorizations with
   evidence: what blocks it, who owes the
   decision, hours left on the clock
5. Void instead of abandoning: a cancelled
   or failed order releases its hold
   deliberately, tagged with the reason
6. Recover the expired in the same hour:
   cancel, duplicate, payment link, and a
   message that reads like competence
7. Report weekly: captured, voided,
   expired, fees avoided, dollars saved
```

Step two is where the paragraph replaces the rule. Capture when the fraud check passes is not one trigger: it is Shopify's risk signal, plus the verification email a human sent, plus the reply that came back, read together. Capture at first shipment is not a Shopify setting at all: it is a judgment call that your store would rather charge for the whole order when the first box leaves than gamble the balance on a backorder date. A workflow that can hold your actual policy, with its exceptions for preorders and its carve-out for B2B terms, is the difference between automating the easy half and automating the job.

Step four is the one that saves the orders the rules cannot. Some authorizations should not be captured yet: the review is waiting on a customer reply, the [order is mid-edit](https://blog.dugong.live/how-to-edit-a-shopify-order-after-its-been-placed.html), the preorder window slipped. Fine. Then someone has to own that clock, and an escalation that says this $412 authorization dies in 41 hours, it is waiting on your verification decision, here is the whole file, turns a silent expiry into a two-minute decision. The difference between a warning email and an escalation is that an escalation names a person and arrives with the evidence.

Step five is the courtesy nobody budgets for. An abandoned authorization does expire on its own, eventually, but the hold can sit on the customer's statement for days doing nothing but generating a where is my refund ticket. Voiding on cancel is free, instant on your side, and it is the difference between a customer who saw the hold vanish and one who called their bank about you. The same discipline pays at capture time: charging a card that passed review beats [refunding a charge you should never have made](https://blog.dugong.live/how-to-win-chargeback-disputes-on-shopify.html), because a refund still costs you the processing fees and sometimes the argument.

## Why this is a compiler problem, not an app problem

Write your actual capture policy down and look at its shape. Capture everything clean within an hour of the fraud check. Hold anything flagged until a human clears it, and never let a hold die silently: escalate at day 5, decide by day 6. Capture preorders when the shipment is booked, not when the last unit arrives. Capture split orders in full at first shipment unless the balance ships more than a week out, then ask. Void within minutes on every cancel. Any authorization that expires anyway gets a payment link and an apology inside the hour, and a line in Friday's report with a reason attached. That is a paragraph with your store's judgment folded into every clause, and no settings page has a field for it. This is the argument behind [the automations no one builds](https://blog.dugong.live/best-shopify-automations-to-set-up.html): describe the paragraph in plain language, and let a compiler turn it into the running workflow, instead of shaving the policy down until it fits a template.

Run the boots order again with the paragraph running. The authorization lands Sunday 11:47 p.m. and enters the watch list with a deadline: Sunday next, 11:47 p.m., standard window. The risk check passes Monday morning, the verification reply lands at 12:31, and the capture fires at 12:31 and 4 seconds, three and a half hours before the boots are even packed. Payment status: Paid. The Friday digest has one line for it, and the line is boring. The interesting line is the other one: two authorizations escalated this week, one captured after a day-5 nudge, one voided on a cancel, zero expired, $963 that did not walk. Boring digests are what winning this particular race looks like.

## The workflow worth building this week

Start with the autopsy you hope comes back empty. Filter orders by payment status Expired for the last six months, then cross it against fulfillment status. Every expired-and-shipped order is money you handed over; every expired-and-unshipped one is a sale you paid to acquire and then released. Add the late-capture fees if you are on Plus and using the long windows. Most stores on manual capture find a number that funds this project in the first afternoon.

Then run the playbook in draft mode for two weeks: let it watch every authorization, propose each capture with its reason, and draft the escalations without sending. You are auditing its judgment, not its clicks. Does it hold the flagged order your gut would hold, does it catch the split shipment your setting would miss, does it void the cancel your intern would forget. When its proposals match your decisions for fifty orders in a row, let the clean captures run on their own and keep the escalations for humans, which is where they belonged all along.

Then say the paragraph out loud, the way you would brief a new finance hire. Charge every order the moment our policy says it is safe. Never let an authorization die without a named person having seen it with time to act. Release holds on purpose, never by neglect. If the clock ever beats us anyway, we ask for the payment again the same hour, like professionals. And tell me on Fridays what almost slipped. That is the brief. The compiler turns it into the workflow, and the payment status column goes back to being the most boring column in the admin, which is the only thing it was ever supposed to be.

> **◆ READING** Two companion pieces if this one landed: [the unpaid order that never cancels itself](https://blog.dugong.live/how-to-automatically-cancel-unpaid-orders-on-shopify.html), on the cousin problem where the customer never pays at all, and [the payout that never matches your sales](https://blog.dugong.live/how-to-reconcile-shopify-payouts-with-your-sales.html), on the reconciliation ritual where expired authorizations usually surface. Also worth reading: [the order that ships before the money lands](https://blog.dugong.live/how-to-stop-shipping-shopify-orders-with-payment-pending.html), on the orders that read Payment pending and get picked anyway.

If you are a Shopify merchant with an Authorized column you have learned not to look at, a warning email folder you stopped opening, or a story about the order you shipped and never charged, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### How long do I have to capture an authorized payment on Shopify?

Seven days on Shopify Payments: the card is authorized at checkout, and you must capture within the authorization period to collect any money for the order. The period varies by payment provider, and on the Shopify Plus plan with Shopify Payments some cards support extended authorization periods: up to 30 days for Visa, Mastercard, and American Express, up to 10 days for Discover and JCB, and 7 days for Diners Club and China UnionPay, depending on the issuing bank. Two details catch merchants. Capturing after the standard 7 days on an extended authorization adds a 1.75% charge on top of standard processing fees. And if the payment was made in a foreign currency, the amount converts at the rate on capture day, not authorization day, so a slow capture can also be a smaller one. Shopify can email you a warning 1 day before an authorization expires: one email, worth turning on, and not a system for a store doing real volume.

Permalink: https://blog.dugong.live/how-to-automatically-capture-payments-on-shopify.html#faq-1

### What happens if a Shopify payment authorization expires before I capture it?

The hold releases and the money returns to the customer's available balance. An expired authorization cannot be captured, so the order sits in your admin looking normal, sometimes already shipped, with payment that will never arrive. Shopify's guidance is to cancel the order and create a new one, or contact the customer to arrange payment again, usually with a payment link. Recovery depends almost entirely on speed and tone: a same-day message saying the payment hold expired before we charged you, here is a secure link, reads as competence, while a two-week-old request to please pay again for boots the customer already owns reads as a bill from nowhere and converts accordingly. If the order has not shipped, hold it until the new payment lands. If it already shipped, you are collecting a debt now, politely, and every day of delay costs recovery rate.

Permalink: https://blog.dugong.live/how-to-automatically-capture-payments-on-shopify.html#faq-2

### Why didn't Shopify capture payment when I fulfilled the order?

The most common reason is a partial fulfillment. The capture-at-fulfillment setting only captures when the entire order is fulfilled, and Shopify's documentation is explicit that partially fulfilled orders won't be captured. Split a shipment, backorder one line, or fulfill items from two locations on different days and the authorization keeps running out its clock while the order looks handled. Other documented causes: the setting only applies to orders placed after it was activated, so everything already in the queue stays manual; B2B orders and orders from B2B checkout often must be captured manually; some fulfillment apps require a paid status before they start, which deadlocks against a capture that waits for fulfillment; and running a third-party auto-capture app alongside a Shopify automatic capture setting can conflict. Capture per fulfillment, which charges for items as each fulfillment happens, exists but only on Shopify Plus and only with providers that support multiple captures.

Permalink: https://blog.dugong.live/how-to-automatically-capture-payments-on-shopify.html#faq-3

### Should I use automatic or manual payment capture on Shopify?

Automatic capture at checkout is right when nothing ever stands between an order and its money: no fraud verification step, no preorders, no B2B terms. The moment any order can need review, the choice gets sharper. Manual capture is honest but fragile: a human clicking a button on every order inside the 7 day authorization window, with one warning email that arrives with roughly 24 hours left. Capture at fulfillment sounds like the compromise, but it only fires when the entire order is fulfilled, so a split shipment or one backordered line quietly runs the clock out. The setting matters less than owning the deadline. Whatever mode you pick, some order will eventually wait on a decision, and the store needs an escalation that says which authorizations die soon, what blocks each one, and who owes the decision, with hours on the clock attached.

Permalink: https://blog.dugong.live/how-to-automatically-capture-payments-on-shopify.html#faq-4

### Can Shopify Flow capture payments automatically?

Yes, within one policy's worth of logic. The well-known Flow template that captures payment when an order is not high fraud risk exists and works, and if your entire capture policy fits in that sentence, Flow closes the gap. Real stores rarely stay that simple. The policies that show up in practice name different triggers for different orders: capture when the fraud check passes, capture at first shipment for split orders, hold preorders until release day, carve out B2B orders on terms entirely. Add the deadline problem, watching each authorization's true expiry by provider and card type, escalating day 5 holds with what blocks them, and voiding deliberately instead of letting holds die silently, and the job outgrows a single trigger and condition. Flow is the right tool for the simple capture rule; the full clock-watching policy is a playbook an agent has to run.

Permalink: https://blog.dugong.live/how-to-automatically-capture-payments-on-shopify.html#faq-5

---

Markdown rendition of https://blog.dugong.live/how-to-automatically-capture-payments-on-shopify.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
