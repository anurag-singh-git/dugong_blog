# How to automatically add tracking numbers to Shopify orders

> Shopify makes you paste each order's tracking number by hand, and Flow cannot help. The AI playbook that fulfills every order with the right number and carrier.

- Canonical: https://blog.dugong.live/how-to-automatically-add-tracking-numbers-to-shopify-orders.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-06-27
- Updated: 2026-10-27
- Section: Research
- Word count: 2491
- Dispatch: Nº 69 · Research · 9 min read
- Full headline on page: How to *automatically add tracking numbers* to Shopify orders
- Keywords: Shopify mark as fulfilled, add tracking number Shopify, auto fulfill Shopify orders, bulk fulfill orders Shopify, import tracking numbers CSV Shopify, dropshipping fulfillment tracking, supplier tracking numbers Shopify, Shopify Flow fulfill order, third party fulfillment tracking sync, fulfillment automation Shopify
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

Picture the part of the day no one puts on a roadmap. A supplier emails a list of tracking numbers. A warehouse drops a spreadsheet. A dropship partner sends a confirmation per item. And then a person, often the owner, sits down and turns that pile into fulfilled orders one at a time: find the order, press mark as fulfilled, choose the line items, paste the tracking number, pick the carrier from the dropdown, save, send the confirmation, next. It is not hard. That is exactly why it is so corrosive. It is easy, repetitive, and endless, and it scales linearly with how well the store is doing. The more you sell, the more of your evening you spend copying numbers from an email into a text box.

This is one of the most common operational complaints in the merchant forums, and it almost always sounds the same. Someone is fulfilling through one or several suppliers, the tracking comes back by email or CSV, and they want to know how to stop pasting it in by hand. The replies point at a bulk fulfill button that still needs the numbers, a CSV importer that still needs the file built, or a paid app that does one supplier's format. The merchant is not asking for anything exotic. They want the obvious thing a store that ships through suppliers needs: when a tracking number comes in, put it on the right order, mark it shipped, and tell the customer. The platform that runs the whole store leaves that last mile to a human with a mouse.

> Shopify will take the order all day long. It just *will not finish it* for you when the tracking comes back.

## The short answer

Shopify auto-fulfills narrow cases only: an order that is entirely digital, or one whose items a connected fulfillment service owns and pushes its own tracking back into. For a self-shipped order, or one you forward to a supplier whose tracking lands in your inbox, you open the order and enter the number yourself.

Bulk fulfill and the CSV route both leave the matching with you. Bulk fulfill marks many orders shipped and still wants each tracking number attached to its own order. The CSV has to be assembled by hand, pairing every order reference with the number and carrier that belong to it, so the matching has only moved into a spreadsheet.

Flow has no action that fulfills an order with a given tracking number and carrier, so the step that actually ships it is the step it cannot take. And where the items sit at a third-party fulfillment location, Shopify withholds the mark as fulfilled button altogether, so a silent service leaves you *moving items between locations* to ship them yourself.

## Why pasting tracking by hand is a tax on every order

Entering a tracking number takes maybe thirty seconds. The damage is not in any single one, it is in the multiplication and in what those seconds crowd out. At fifty orders a day that is a chunk of someone's afternoon spent on pure transcription, every day, forever, and it is the kind of work that gets squeezed into the gaps and then done in a hurry. Hurry is where the real cost lives. The tracking number gets pasted onto the wrong order. A digit gets dropped. The carrier dropdown gets left on the default, so the customer gets a tracking link that goes nowhere. An order with two suppliers gets marked fully shipped when only half of it has actually left.

Every one of those small slips lands downstream as something bigger. A wrong or dead tracking link is a customer who cannot see their package moving, which turns straight into a support ticket, the exact [where is my order message](https://blog.dugong.live/how-to-reduce-where-is-my-order-wismo-tickets-on-shopify.html) the store is trying to avoid. An order marked shipped too early starts the delivery clock in the customer's head before the box exists. And because the shipping confirmation fires off whatever you entered, a mistake in the tracking field is a mistake mailed directly to the customer with your logo on it. The manual step is not just slow. It is the single most error-prone touch in the whole post-purchase flow, sitting right at the moment the customer is paying closest attention.

## What Shopify actually does, and where it stops

Shopify is glad to automate the parts around fulfillment. It will email the order confirmation, hold the order, let you tag it. What it does not do for most stores is the act in the middle: take a real tracking number from a supplier and turn it into a fulfilled order with a working tracking link. The gap shows up in three places merchants hit quickly.

First, **auto-fulfillment only covers narrow cases**. Shopify can mark an order fulfilled automatically when the order is entirely digital, or when a connected fulfillment service or app owns the items and pushes its own tracking back into the order. For the self-shipped order, the order you forward to a supplier, the dropshipped order whose tracking arrives in your inbox, none of that applies. The default for a physical, manually shipped order is that you fulfill it yourself and you enter the tracking yourself.

Second, **bulk fulfill and CSV import still leave the work to you**. Shopify lets you select many orders and mark them fulfilled at once, and there is a CSV route for adding tracking in bulk. Both sound like the answer until you try them. Bulk fulfill marks orders shipped, but you still attach each tracking number to its order. The CSV still has to be assembled by you, with the right order numbers matched to the right tracking numbers and carriers, which is the exact matching job you were trying to avoid, just moved into a spreadsheet. You are still the one reading the supplier's email and deciding which number belongs to which order.

Third, **Flow cannot add a tracking number**. [Shopify Flow](https://help.shopify.com/en/manual/shopify-flow), free on every plan, can react when an order is created or fulfilled, can tag it, and can notify you. But Flow has no action that marks an order fulfilled with a specific tracking number and carrier pulled from a supplier email or a feed. You can automate a reminder that an order is waiting to ship. You cannot automate the step that ships it. And if the order's items sit at a third-party fulfillment service location, Shopify will not even show you the mark as fulfilled button, because that service is meant to control the status, so when the service is slow or silent you are stuck moving items between locations just to do it yourself.

> **◆ DATA** The tell that this is a real gap is the size of the cottage industry built to fill it. There is a whole shelf of apps whose entire job is to import tracking numbers from a spreadsheet or an FTP drop and mark orders fulfilled in bulk, scheduled hourly or daily, per supplier feed. They exist, and merchants pay for them, precisely because the native flow ends at a text box and a save button. When an app category exists only to automate one field, the platform has told you where its automation stops.

## Why the usual fixes don't hold

Once the pasting starts to hurt, merchants reach for one of a few workarounds. Each one helps and each one breaks in a predictable spot.

**"I will just bulk fulfill in the admin."** Good for the day every order ships the same way with no tracking to attach. The moment tracking is involved, bulk fulfill only handles the marked-as-shipped half; you are back to entering numbers per order. And bulk fulfill is blind to the split order, the one where one supplier has shipped and the other has not, so it either marks the whole thing done too early or you pull it out of the batch and handle it by hand anyway.

**"I will build a tracking CSV every morning."** This is the workaround that quietly turns a merchant into a data-entry clerk. You open each supplier email, copy order references and tracking numbers into a template, reconcile the ones that do not line up, and upload. It works until the formats diverge, and they always do: one supplier sends a clean sheet, another sends numbers in the body of an email, a third uses your reference and a fourth uses their own. The CSV only imports what you have already matched, so all the actual thinking still happens in your head over a spreadsheet before the import ever runs.

**"I will install a tracking importer."** There are solid ones, and for a store with one tidy supplier feed they are a fair answer, which again proves the native gap is real. But most need a clean, mapped file or a consistent feed to work from. They do not read a free-form supplier email, they do not reconcile a tracking number that arrived for an item that is not on that order, and they do not know that a number repeated from yesterday should not re-fulfill anything. The import is only as good as the file you hand it, and assembling that file from messy, mismatched supplier messages is the part that was hard in the first place.

## What the automation actually has to do

The real job is not "mark orders fulfilled." It is "when a supplier or warehouse sends tracking, in whatever shape it arrives, match each number to the right order and the right line items, set the correct carrier so the link works, fulfill, and send the customer one accurate confirmation, while stopping on anything that does not cleanly match." That is reading, matching, and judgment, run per shipment across every supplier you use. As a Dugong playbook, in plain prose, it reads like this:

```
# trigger
On a supplier or warehouse sending tracking
   (email, spreadsheet, CSV, or feed)

# steps
1. Catch the tracking wherever it lands, instead of
   waiting for someone to open it
2. Match each tracking number to the right order and
   the right line items, even on split shipments
3. Detect the carrier from the number so the customer
   gets a link that works
4. Fulfill the matched line items at the correct
   location with the tracking attached
5. Send the shipping confirmation once per shipment,
   and a partial when only part has gone
6. Hold anything that does not match, repeats, or is
   blank for a human to look at
7. Log which number went to which order, and why
```

Seven lines. The compiler fills in everything underneath: watching the inbox and the feeds, reading a message whether it is a neat sheet or a sentence in an email, pairing each tracking number with the order and the specific items it covers, recognizing the carrier from the format of the number, fulfilling exactly those line items at the right location, and sending a single clean confirmation at the moment the package really moves. The merchant never sat with twenty browser tabs open pasting numbers after dinner. They described how a careful shipping clerk would handle a day's tracking, and let the compiler do the volume and catch the exceptions.

> **◆ NOTE** The fulfillment that does damage is the confident wrong one. A tracking number pasted onto **the wrong order** sends a real customer a stranger's package link and marks their order shipped when it is not. A blank or repeated number marks an order done with nothing behind it. The job is not "clear the queue," it is "put this specific number on the order it actually belongs to, ship exactly what shipped, and when anything is ambiguous, stop and ask rather than guess." Automation that cannot tell a clean match from a messy one should not be touching the confirmation email.

## Why this is a compiler problem, not an app problem

There are capable tracking importers, and for a single clean feed they are a reasonable answer. But the thing that makes fulfillment safe to automate is not pushing a number into a field, it is the matching and the judgment around it: reading a supplier message that was never formatted for a machine, knowing which line items a shipment covers when an order is split across two suppliers, telling a fresh tracking number from one that already went out, and noticing when a number arrived for something that is not even on the order. Those are decisions about a particular shipment, weighed together, and the right answer changes with every supplier and every order, which means a fixed import mapping was never going to hold.

A natural-language compiler fits because entering tracking was never really a data-entry problem. It is a *reading and matching* problem wearing a text box's clothes. Pasting one clean number is the easy part, which is why the shortcuts do it. The hard part is everything around it: read what the supplier actually sent, find the order it belongs to, ship only what shipped, set the carrier so the link is live, send one honest confirmation, and pull a human in on anything that does not line up. You can write that brief in a paragraph. You could never hold it across every supplier email that landed today. It sits in the same family as [the order tag you set by hand](https://blog.dugong.live/how-to-automatically-tag-orders-on-shopify.html), where the routing depends on reading the whole order rather than one condition, and [the order change that races your warehouse](https://blog.dugong.live/how-to-edit-a-shopify-order-after-its-been-placed.html), where the window between paid and shipped is exactly where the manual steps pile up.

## The workflow worth building this week

If you ship through suppliers, a warehouse, or a dropship partner, and your tracking comes back as email or spreadsheets you then retype into Shopify, this is the automation to set up before the next busy stretch, because every order you fulfill by hand is thirty seconds you will never get back and one more chance to mail a customer the wrong link at the worst possible moment. It pairs naturally with the post-purchase work we have written about, like the [where is my order tickets that eat your afternoon](https://blog.dugong.live/how-to-reduce-where-is-my-order-wismo-tickets-on-shopify.html), which mostly come from tracking that was wrong or missing, and it feeds the same flywheel as [the Shopify automations no one builds](https://blog.dugong.live/best-shopify-automations-to-set-up.html), where the work that compounds is the part merchants never get to.

Describe it the way you would brief a careful shipping clerk: when a supplier sends tracking, put each number on the order it belongs to, ship only what actually went, set the carrier so the link works, tell the customer once, and bring me anything that does not match before you touch it. That is the whole brief. The compiler does the reading, the matching, the fulfilling, and the confirmation. You keep your evening, and you stop being the slowest, most error-prone step between a paid order and a shipped one.

> **◆ READING** If this resonates, two companion pieces: our dispatch on [the order tag you set by hand](https://blog.dugong.live/how-to-automatically-tag-orders-on-shopify.html), where the work is reading the whole order instead of one rule, and the field study on [the Shopify automations no one builds](https://blog.dugong.live/best-shopify-automations-to-set-up.html), where the work that actually compounds is a sliver of what merchants wire up.

If you are a Shopify merchant who has wired up tracking that matches itself to the right order instead of being pasted in by hand, or you have a story about the night you fulfilled a hundred orders off a supplier spreadsheet, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Does Shopify automatically fulfill orders and add tracking numbers?

Only in narrow cases. Shopify can mark an order fulfilled automatically when the whole order is digital, or when a connected fulfillment service or app controls the items and pushes its own tracking back. For everything else, the self-shipped order, the dropshipped order, the order whose tracking your supplier emails you, you open the order yourself, press mark as fulfilled, and type or paste the tracking number into the tracking field one order at a time. There is a bulk fulfill option and a CSV import, but you still have to know each tracking number and match it to the right order before either one helps.

Permalink: https://blog.dugong.live/how-to-automatically-add-tracking-numbers-to-shopify-orders.html#faq-1

### Can Shopify Flow add a tracking number or fulfill an order?

No. Shopify Flow can react to an order, tag it, and send you a notification, but it has no action that marks an order fulfilled with a specific tracking number and carrier read from a supplier email or spreadsheet. The one step that actually clears the order, attaching the right tracking and sending the shipping confirmation, is the step Flow cannot take, which is why merchants who ship through suppliers end up doing it by hand or buying a separate import tool.

Permalink: https://blog.dugong.live/how-to-automatically-add-tracking-numbers-to-shopify-orders.html#faq-2

### Why can't I mark a third-party fulfillment order as fulfilled?

When an order's items sit at a location owned by a third-party fulfillment service, the mark as fulfilled button is not available to you, because that service is supposed to control the fulfillment status and push tracking back. If the service is slow to sync, or if it never sends tracking, you are stuck: to fulfill it yourself you have to move the items to a location you manage first, then fulfill and add tracking manually. That extra dance is exactly the kind of judgment and data entry an automation should handle instead of you.

Permalink: https://blog.dugong.live/how-to-automatically-add-tracking-numbers-to-shopify-orders.html#faq-3

### How do I add tracking numbers to Shopify orders in bulk?

Two native routes exist and both leave the matching to you. Bulk fulfill marks many orders shipped in one screen, but each tracking number still gets attached per order, and the batch is blind to the split order where one supplier has shipped and the other has not, so it either marks the whole thing done too early or you handle it by hand anyway. The CSV import takes tracking in bulk, but you assemble the file, matching order numbers to tracking numbers and carriers, which is the same matching job moved into a spreadsheet, and supplier formats always diverge: one sends a clean sheet, another puts numbers in the body of an email, a third uses your reference and a fourth uses their own. Importer apps handle one clean, mapped feed; none of them read a free-form supplier email or notice that a repeated number should not re-fulfill anything.

Permalink: https://blog.dugong.live/how-to-automatically-add-tracking-numbers-to-shopify-orders.html#faq-4

### What happens if the wrong tracking number goes on a Shopify order?

The mistake mails itself: the shipping confirmation fires off whatever you entered, so a wrong number goes straight to the customer with your logo on it. From there the damage lands downstream. A wrong or dead link is a customer who cannot see their package moving, which turns directly into a where is my order ticket. A carrier dropdown left on the default sends a tracking link that goes nowhere. An order marked shipped too early starts the delivery clock in the customer's head before the box exists. Each entry takes maybe thirty seconds, but it is done in a hurry in the gaps, at the exact moment the customer is paying closest attention, which makes hand-entered tracking the single most error-prone touch in the whole post-purchase flow. The rule that survives volume: hold anything blank, repeated, or ambiguous, and ask rather than guess.

Permalink: https://blog.dugong.live/how-to-automatically-add-tracking-numbers-to-shopify-orders.html#faq-5

---

Markdown rendition of https://blog.dugong.live/how-to-automatically-add-tracking-numbers-to-shopify-orders.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
