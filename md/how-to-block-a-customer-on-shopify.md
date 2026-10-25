# How to block a customer on Shopify from placing orders

> Shopify has no ban button: deleting an account leaves guest checkout open, and Flow cancels after the order exists. The AI playbook that makes a block stick.

- Canonical: https://blog.dugong.live/how-to-block-a-customer-on-shopify.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-07-23
- Updated: 2026-10-25
- Section: Research
- Word count: 2509
- Dispatch: Nº 89 · Research · 10 min read
- Full headline on page: How to *block a customer* on Shopify from placing orders
- Keywords: Shopify block customer, ban customer Shopify, Shopify blacklist customer, block customer from ordering Shopify, Shopify serial returner, Shopify block email address checkout, Shopify IP block customer, stop customer from buying Shopify
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

Every store meets this customer eventually. The one who has ordered eleven times and returned nine, always worn once, always just inside the window. The one who files an item-not-received claim on every third package. The one who was abusive to your support person twice and is somehow back with a full cart. The competitor who places orders and cancels them to poke at your stock. The details vary, and the merchant's next move never does: they open the customer's profile, look for the button that says never again, and discover that in a platform which can schedule a sale to the second, there is no way to refuse a sale at all.

The community threads on this run back years and read like one long support queue. "How can I block or blacklist certain customers from placing orders?" "How can I block or blacklist a problematic customer in Shopify?" "IP ban customer from buying from or even seeing my store?" And, still arriving in 2025, "How to block customer account." Different stores, different bad actors, the same discovery underneath: the platform holds a complete record of what this person did to you and offers no way to act on it. Nobody in those threads is asking for something exotic. Every marketplace has a block button. Every email client has one. The storefront where this person costs you actual money does not.

## The short answer

Shopify has no block or ban button anywhere in the admin. Deleting or disabling a customer's account touches only the login, and guest checkout stays open to anyone who can type an email address, so the person you just deleted can order again thirty seconds later. Fraud analysis will not stand in for it, because a serial returner paying with their own valid card from their own address is genuinely low risk as a payment.

The Flow workaround reacts instead of refusing. Tag the customer, cancel on Order created, restock: the order was already placed and the payment already captured, so every catch still costs you processing fees that refunds generally do not return, and the cancellation notice teaches the blocked person the exact shape of the wall. Checkout validation functions can truly decline a checkout, but they live inside a custom app someone has to build and maintain.

Matching is the deeper crack, because Flow compares strings. One alias walks past an email blocklist on the first attempt, while the literal match is the version most likely to catch an innocent relative who shares a surname. A block has to be held as an identity: email variants, phone, ship-to address, payment fingerprint and the history that earned it, screened at order creation, *before* the pick.
## What Shopify actually does, and where it stops

The obvious moves all miss, and it is worth being precise about why. Deleting or disabling the customer's account touches only the login: guest checkout remains open to anyone who can type an email address, which is to say the person you just deleted, thirty seconds later, with the same email or a new one. Shopify's fraud analysis will not catch them either, because it is answering a different question. It exists to spot stolen payment methods, the mismatched cards and impossible geographies behind [the high-risk flag that makes you guess](https://blog.dugong.live/how-to-handle-high-risk-orders-on-shopify.html). Your serial returner is not stealing anything at checkout. They pay with their own valid card from their own address, the transaction is perfectly legitimate, and the analysis waves it through as low risk, because as a payment it is. The damage comes later, and no field in the fraud panel looks later.

The workaround the forums converge on is [Shopify Flow](https://help.shopify.com/en/manual/shopify-flow), and it gets closer while still missing the point. Tag the customer as blocked, then build a workflow on the Order created trigger: if the customer carries the tag, or the email matches a list, cancel the order, restock the items, maybe send the cancellation notice. This genuinely works, and for some stores it is enough. But look at what it is actually doing. The order was placed. The payment was captured. Cancelling now means refunding, and payment processing fees are generally not returned on refunds, so every order your blocklist catches still costs you the fees on money you never wanted. The customer gets a cancellation email and learns the exact shape of the wall, and nothing stops them from checking out again in two minutes, because Flow reacts to orders and cannot refuse one. A block that charges you per use and tells the blocked person how it matched is not a block. It is a toll booth you pay for.

The matching is the deeper crack. Flow compares strings. The email `jane@gmail.com` is on your list, so `jane+1@gmail.com` is not, and `jane.doe@icloud.com` is certainly not, and the fresh address created in one minute is invisible. The person is identical, the ship-to flat is identical, the behavior about to happen is identical, and the workflow sees a brand-new customer, which is the same blindness that lets [one loyal customer split into four strangers](https://blog.dugong.live/how-to-merge-duplicate-customer-profiles-on-shopify.html) in the other direction. There are sharper tools further down: checkout validation functions can truly decline a checkout before it completes, but they live inside a custom app that someone has to build and maintain, and they match on the same literal fields. And the IP blocking apps dissolve on contact with reality, because the determined returner switches to a VPN in seconds while a shared office or campus address locks out innocent shoppers wholesale.

> Shopify can tell you an order looks stolen. It has no way to remember that this exact customer has burned you three times.

What the missing button costs depends on which bad actor you drew. The serial returner runs up outbound shipping, return shipping, and restocking on merchandise that comes back unsellable, a loop that [an automated returns desk](https://blog.dugong.live/how-to-automate-returns-and-exchanges-on-shopify.html) processes faster but cannot refuse. The item-not-received filer converts your goodwill into [chargebacks you lose by default](https://blog.dugong.live/how-to-win-chargeback-disputes-on-shopify.html), each one carrying its own fee on top of the product. The launch-day buyer who [clears your whole drop](https://blog.dugong.live/how-to-limit-purchase-quantity-per-customer-on-shopify.html) comes back under a new name the moment his first cart gets cancelled. And the abusive customer costs you something no ledger holds, which is the support person who has to be polite to them again. None of these people are anonymous. You know exactly who they are. That is the insult in it: the block fails not for lack of information but for lack of anywhere to put it.

## Why doing it by hand never keeps up

The manual version is a memory game scored in real money. Someone keeps the list, in their head or in a spreadsheet: the names, the emails, that one address on Elm Street. Every morning someone scans the new orders against it, which works until the day the orders are many and the scan is quick, and the match that mattered wore a middle initial. Catch it after fulfillment and you are no longer blocking, you are chasing: intercepting a label that already printed or eating one more round trip of shipping. Miss it entirely and you find out in three weeks, at the returns desk, from the person processing refund number ten.

And the memory game has a second failure mode that costs more than the misses: false positives. A spreadsheet matched on surname will eventually cancel a wedding gift from the blocked customer's cousin, or a genuine order from a flatmate at the same address, and that person tells the story forever. A block list enforced by tired pattern-matching at 8 a.m. swings between too loose, letting the tenth order through, and too tight, executing an innocent, and it cannot tell you which mode it is in today.

## What the automation actually has to do

A block that sticks is not one rule. It is a memory, a screen, a judgment, and a follow-through: remember every signal about who burned you, check every new order against that memory before fulfillment starts, decide match or coincidence from the whole record rather than one string, act while the order is still cheap to act on, and keep watching, because blocked customers come back sideways. As a Dugong playbook, in plain prose, it reads like this:

```
# trigger
On every new order, and whenever a return closes
   badly, a chargeback lands, or support flags an
   abusive exchange

# steps
1. Keep the blocklist as identities, not strings:
   email variants, phone, ship-to address, payment
   fingerprint, and the history that earned the block
2. Screen each order at creation against the list,
   before the label, before the pick
3. Decide match or coincidence from the whole
   record: a shared surname is nothing, a fresh email
   shipping to the same flat is not
4. Cancel the confirmed match unfulfilled, restock,
   and file the reason on the order
5. Watch the comeback: new aliases, new accounts,
   small address edits that point at the same person
6. Escalate the borderline case to a human with
   the history attached
```

Six lines. The compiler fills in the rest: reading plus-addressing and dot tricks for what they are; treating the shipping address and phone number as the durable identity they actually represent; scoring a borderline order instead of guessing, this email is new but the flat and the phone both match, say it plainly and wait; cancelling inside the window where cancellation is clean, before the warehouse moves, the same race that [order edits lose by hand](https://blog.dugong.live/how-to-edit-a-shopify-order-after-its-been-placed.html); [tagging the order and the customer](https://blog.dugong.live/how-to-automatically-tag-orders-on-shopify.html) so support sees the history before they answer the angry email; and remembering why each block exists, so the list can be argued with later, entry by entry, when someone asks whether the person who made two returns in 2024 really belongs next to the one who made nine.

> **◆ NOTE** The trap is **blocking by exact email**. One string in a Flow condition feels like a wall and works like a turnstile: the plus-sign alias walks past it on the first try, and meanwhile the literal match is the version most likely to hit an innocent, the relative with the shared surname, the flatmate at the same address. A block is a judgment about a person, and it has to be enforced on the person, not on the last email address they happened to use.

## Why this is a compiler problem, not an app problem

There are blocking apps, and a store under active siege should look at them. But the hard part of a block is not refusing a checkout, it is everything around the refusal: is this order actually the blocked person, or their neighbor; is this customer's record bad enough to block at all, or is two returns in a year just a person with opinions about fit; should the block cancel silently, or ask a human first, because the match is only probable; and when the blocked customer inevitably comes back under a new name, is the new name recognized as a comeback or greeted as a first-time buyer with a welcome discount. Those are judgments about identity and proportion, they change with every order, and a fixed rule holds none of them. The cost of getting the judgment wrong is asymmetric, too: a bad order slipping through costs you a return cycle, while a good customer cancelled as a suspect costs you the customer, their friends, and a public review that says your store cancels orders for no reason.

It also sits in a web this desk keeps mapping. Nearest neighbor is [the high-risk flag that makes you guess](https://blog.dugong.live/how-to-handle-high-risk-orders-on-shopify.html), which judges the payment while this playbook judges the person, and a store wants both watching every order. The identity work underneath is the same skill as [merging the customer Shopify counts three times](https://blog.dugong.live/how-to-merge-duplicate-customer-profiles-on-shopify.html), pointed at the opposite end of the customer list. The volume attacks belong to [the card-testing flood](https://blog.dugong.live/how-to-stop-card-testing-attacks-on-shopify.html) and [the buyer who clears your whole drop](https://blog.dugong.live/how-to-limit-purchase-quantity-per-customer-on-shopify.html), while the damage a missed block does downstream lands on [the returns desk](https://blog.dugong.live/how-to-automate-returns-and-exchanges-on-shopify.html) and [the chargeback desk](https://blog.dugong.live/how-to-win-chargeback-disputes-on-shopify.html) in equal measure.

Picture a mid-sized apparel store with one professional returner. Eleven orders, nine returns, every item back worn with the tags retucked. The merchant tags her blocked, and the Flow cancellation catches order twelve. Order thirteen arrives four days later under a new Gmail with one dot moved, same flat, same phone, and sails through. With the playbook running, order thirteen scores as a comeback at creation: the address and phone match an identity on the list, the order cancels unfulfilled with the stock returned to the shelf, the reason is filed on the order, and the merchant reads about it in a morning summary instead of a returns report. Order fourteen never comes. The whole affair cost two cancellations and zero shipped boxes, against the alternative, which was four more round trips of worn merchandise and a support inbox learning to dread one name.

## The workflow worth building this week

If you sell anything with a return window, run limited drops, or have ever had a customer your team recognizes by name with a sinking feeling, the missing ban button is already costing you money labeled as something else: shipping on round trips that were never sales, chargeback fees on claims that were never honest, support hours spent being polite to someone who is not a customer but a recurring event. It pairs naturally with [the high-risk order playbook](https://blog.dugong.live/how-to-handle-high-risk-orders-on-shopify.html), which catches the strangers with stolen cards, while this one remembers the regulars who cost you on purpose. It feeds the same flywheel as [the Shopify automations no one builds](https://blog.dugong.live/best-shopify-automations-to-set-up.html), where the compounding work is the institutional memory nobody has time to keep.

Describe it the way you would brief a careful assistant: here is the list of people we no longer sell to and why, watch every new order against it, treat the address and the phone as the person rather than the email, cancel the confirmed ones before the warehouse touches them and put the stock back, ask me about the borderline ones instead of guessing, and tell me when one of them tries to come back as somebody new. That is the whole brief. The compiler does the remembering, the screening, the scoring, and the paper trail. Your store finally gets the thing every other platform gave its users years ago, which is the right to say no thank you, and mean it tomorrow too.

> **◆ READING** If this resonates, two companion pieces: our dispatch on [the high-risk flag that makes you guess](https://blog.dugong.live/how-to-handle-high-risk-orders-on-shopify.html), which handles the fraud Shopify does try to catch, and [the customer Shopify counts three times](https://blog.dugong.live/how-to-merge-duplicate-customer-profiles-on-shopify.html), where the same identity problem wrecks your best customers instead of shielding you from your worst.

If you are a Shopify merchant who has fought a professional returner across five aliases, or you have a blocklist story with a better ending, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Can I block a customer from placing orders on Shopify?

Not natively. Shopify has no block or ban feature anywhere in the admin. Deleting or disabling a customer's account only affects their ability to log in, and guest checkout remains open to anyone with an email address, so the same person can order again immediately. Shopify's fraud analysis does not help either, because it is built to flag stolen payment methods, and a serial returner paying with their own valid card registers as low risk. Merchants make a block stick by automating the whole loop: keep a blocklist built on identity rather than one email string, check every incoming order against it, and cancel and restock before fulfillment when a match is confirmed.

Permalink: https://blog.dugong.live/how-to-block-a-customer-on-shopify.html#faq-1

### Can Shopify Flow block a customer from ordering?

Flow cannot prevent an order, only react to one. The standard workaround is to tag the customer as blocked and build a workflow on the Order created trigger that checks the tag or email and cancels the order, restocks the items, and optionally notifies the customer. It works, but the order still gets placed and paid: the payment is captured and then refunded, and payment processing fees are generally not returned on refunds, so every blocked order costs money. The match is also literal, so a plus-addressed alias or a brand-new email walks straight past the condition, and the customer just tries again since nothing stops the next checkout.

Permalink: https://blog.dugong.live/how-to-block-a-customer-on-shopify.html#faq-2

### Can I block someone's IP address on Shopify?

There is no native IP blocking in Shopify. Third-party apps can block IP addresses or countries at the storefront level, but as a way to ban a specific person it is weak on both sides: the determined returner switches to a VPN or their phone's network in seconds, while a shared address like an office, a campus, or a mobile carrier's network can lock out innocent shoppers along with the one you meant. IP is one useful signal among several for recognizing a returning bad actor, but it cannot carry a block on its own, which is why identity-based matching across email variants, phone, and shipping address works better.

Permalink: https://blog.dugong.live/how-to-block-a-customer-on-shopify.html#faq-3

### Can I stop a blocked customer at checkout on Shopify, before they pay?

Only with checkout validation functions, and they come with a maintenance bill. Validation functions are the one tool that can truly decline a checkout before it completes, which fixes the worst property of the Flow workaround, where the order is placed, the payment is captured, and the processing fees are lost to the refund. But they live inside a custom app that someone has to build and maintain, which puts them out of reach of most stores without a developer, and they match on the same literal fields as everything else, so a fresh email address walks past them exactly as it walks past a Flow condition. The honest summary: cancel-after-order costs fees per catch and teaches the blocked customer the shape of the wall, decline-at-checkout costs an app build, and neither solves the matching problem, which is recognizing the person rather than the string they typed.

Permalink: https://blog.dugong.live/how-to-block-a-customer-on-shopify.html#faq-4

### How do I avoid blocking the wrong person on Shopify?

Match on the whole record, never on one string, because a false positive costs more than a miss. A blocklist matched on surname will eventually cancel a wedding gift from the blocked customer's cousin, or a genuine order from a flatmate at the same address, and that person tells the story forever. The judgment runs on evidence. A shared surname is nothing. A fresh email shipping to the same flat with the same phone number is close to certain. The durable identity is the shipping address, the phone, and the payment fingerprint, not the last email address the person happened to use. The borderline case should not be settled by tired pattern-matching at eight in the morning; it belongs in front of a human with the history attached. And every confirmed block should carry the reason it exists, so the list can be argued with later, entry by entry.

Permalink: https://blog.dugong.live/how-to-block-a-customer-on-shopify.html#faq-5

---

Markdown rendition of https://blog.dugong.live/how-to-block-a-customer-on-shopify.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
