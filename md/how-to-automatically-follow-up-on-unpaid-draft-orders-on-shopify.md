# How to automatically follow up on unpaid draft orders on Shopify

> Shopify sends one draft order invoice and never a reminder, so quotes die in silence. The AI playbook that follows up, answers, and retires stale quotes.

- Canonical: https://blog.dugong.live/how-to-automatically-follow-up-on-unpaid-draft-orders-on-shopify.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-08-03
- Updated: 2026-08-15
- Section: Research
- Word count: 2410
- Dispatch: Nº 101 · Research · 9 min read
- Full headline on page: How to automatically follow up on *unpaid draft orders* on Shopify
- Keywords: Shopify draft order follow up, unpaid draft order invoice Shopify, Shopify draft order payment reminder, Shopify quote follow up automation, draft order invoice link expires, auto cancel draft orders Shopify, Shopify Flow draft order trigger, B2B quote follow up Shopify
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

An interior designer in Savannah emails a lighting studio about twelve brass pendants for a restaurant opening in October. The owner does what Shopify tells him to do with a sale that starts in an inbox: he builds a draft order, applies her trade discount, adds a shipping line, writes a warm note, and clicks Send invoice. The status flips to Invoice sent. It feels like closing. It is actually the last thing Shopify will ever do for this sale.

Because that is the entire feature. One email, one checkout link, and the platform's part is over. If the designer opens the invoice on her phone between site visits, means to pay on Friday, and forgets, nothing happens. Not to her: no reminder, no nudge, no second email, ever. And not to you: no alert, no aging view, no overdue state. The draft wears the same badge on day forty that it wore in the first hour.

The forums have been asking about this for years. The thread titled *How to automate unpaid invoice reminders?* gets pointed at apps. The one titled *auto cancel [draft orders](https://help.shopify.com/en/manual/fulfillment/managing-orders/create-orders)* gets pointed at scripts. And the merchants inside them describe the same Drafts page: dozens or hundreds of open quotes, some alive, some long dead, and no way inside Shopify to tell which is which, let alone to do anything about either.

## One email, then the machinery goes quiet

Draft orders are Shopify's quote workflow, whether or not anyone calls them that. The phone order, the Instagram DM, the wholesale inquiry, the custom piece, the pro forma [invoice a business buyer needs](https://blog.dugong.live/how-to-automatically-send-invoices-on-shopify.html) before their accounts team will pay anything: all of it runs through a draft. A draft has exactly three states, Open, Invoice sent, and Completed, and only a customer can reach the third one, by paying. There is no due date on a draft, no overdue status, and no second invoice email unless a human opens the draft and sends one by hand.

Here is the detail that stings once you notice it. Shopify knows how to send payment reminders. Orders with payment terms attached, net 30 and its cousins, can send up to five scheduled reminder emails, on the due date and after it. The machinery exists, one screen away in the same admin, and draft orders are excluded from it: a draft has no due date, so there is nothing to count down from, so nothing ever fires. The product knows how to nag. For quotes, it declines to.

Some merchants borrow the machinery anyway: complete the draft as a pending payment order, attach Net 7 terms, and reminders suddenly exist. So does an order, though. Every undecided quote becomes a live order sitting in your reports and committing stock it may never sell, right next to [the unpaid orders that never cancel themselves](https://blog.dugong.live/how-to-automatically-cancel-unpaid-orders-on-shopify.html), and every quote that dies now needs a cancellation to bury it. You have traded a follow-up problem for an accounting one.

## The quote that cannot die

Stale drafts have the opposite problem, and it is stranger. A draft order has no cancelled status. The community feature request asking for one is polite, specific, and open. Your choices for a dead quote are two: leave it, or delete it. Leave it and the Drafts page slowly becomes an archaeology site, this month's live pipeline interleaved with February's ghosts, which is why so many merchants end up keeping the real list in a spreadsheet next to Shopify. The spreadsheet is its own admission.

Leaving a dead draft does something worse than clutter. The checkout link in that invoice stays live for as long as the draft exists, and product prices inside a draft are locked by default. That is correct behavior for a quote this week and a liability by summer: a customer can dig a January email out of search and pay January prices in July, and the first you hear of it is an order you have to honor or awkwardly refund. The only expiry Shopify applies is blunt: drafts created on or after April 1, 2025 delete themselves after a full year of inactivity. A year is not a quote lifecycle. It is a statute of limitations.

And a third failure mode catches the quotes that were about to succeed. Inventory is not held for a draft unless you deliberately reserve it, and nobody reserves stock for a maybe. So the customer who finally clicks the link in week three can meet a checkout that refuses her, because one line item sold out on Tuesday. The sale survived your silence and died at the finish line, and nobody tells you about that either.

> **◆ NOTE** The trap is **treating follow-up as memory**. Every unpaid quote is a small task with no owner, and the default owner becomes whoever feels guilty on a Friday. At thirty quotes a month that is not a memory problem. It is a sales pipeline with no one running it, and pipelines nobody runs leak money quietly.

## Why the manual version fails quietly

The manual version is a spreadsheet, or worse, a feeling. Export the drafts, add a column for chased once and chased twice, resolve to keep it current. What actually happens is batches: follow-ups go out on the afternoon someone remembers, which is precisely the afternoon the oldest quotes are three weeks cold and the note has decayed to just checking in. Timing is most of a follow-up's value, and batch-when-guilty is the worst possible timing, too early for nobody and too late for exactly the quotes that mattered.

Uniform chasing is the second failure. The eighty dollar phone order and the thirty-eight hundred dollar trade order sit in the same list and get the same template, which in practice means the big one gets undertreated. It deserved a stock check and a phone call. It got bumping this to the top of your inbox, eleven days late.

And [Flow](https://help.shopify.com/en/manual/shopify-flow), the tool that should fix this, is the wrong shape for it. Flow does have a Draft order created trigger. It fires once, at the moment of creation, for drafts that contain products, and the useful actions available against a draft essentially end at tags. There is no trigger for an invoice that has sat unpaid for five days, and nothing in Flow writes to your customer about a draft at all. The accepted workaround on the forums is a Scheduled time trigger that emails your own staff a list of open drafts. Sit with that for a second: the automation platform's answer to forgotten follow-ups is a scheduled email reminding you to do them. It automates the guilt.

> Shopify keeps every quote you have ever written, and reminds no one about any of them.

## What the automation actually has to do

The fix is not a louder invoice. It is the follow-up a good salesperson runs on every open quote without being asked, which means reading before writing. As a Dugong playbook, in plain prose:

```
# trigger
On invoice sent, on customer reply, and on
a daily sweep of open drafts

# steps
1. Read the draft: value, customer, history,
   stock, and how long it has been sitting
2. Remind on the cadence the quote deserves:
   day two, day seven, day fourteen, warmer
   and personal above the big-ticket line
3. Answer every reply: small questions the
   same hour, negotiations handed to a human
4. Check stock before every nudge: never
   chase payment for a quote you can no
   longer fill; re-quote or reserve instead
5. Retire quotes at your cutoff: tag the
   loss, delete the draft, let the stale
   link and its locked prices die with it
6. Escalate the quotes worth a phone call,
   with the context already attached
7. Report the pipeline weekly: sent, paid,
   expired, and how long paying took
```

Step one is the part that looks decorative and is not. A rule can find drafts older than seven days; that is a filter, and a filter chases everything equally. Reading means noticing that the thirty-eight hundred dollar draft belongs to a trade account that always pays after one nudge, that the sixty dollar one is a phone customer who probably changed her mind, and that the draft with a reply sitting in your inbox is not stalled at all, it is waiting on you to answer a question about finishes. That is the same species of judgment as [deciding what a risk flag actually means](https://blog.dugong.live/how-to-handle-high-risk-orders-on-shopify.html) or [tagging an order from its contents](https://blog.dugong.live/how-to-automatically-tag-orders-on-shopify.html): context weighed against context, not a field against a threshold.

Steps two and three are where the money is. A note on day two converts because the decision is still warm; the customer meant to pay, and the bump is a courtesy. A note in week three is an apology for the silence in both directions. Replies matter even more than reminders. Most are one question long, how soon can these ship, can you do ten instead of twelve, does the discount survive the change, and every unanswered hour lowers the odds the quote survives. An agent that answers the small ones inside the hour and hands the real negotiations to you with the history attached is doing sales work, not clerical work.

Steps four and five are the two ends of the staleness problem. A nudge that says pay now for a quote whose contents sold out is worse than no nudge, so the sweep checks stock first and either re-quotes honestly or asks you whether to reserve. And retirement is protection, not tidying: deleting the dead draft is the only way Shopify gives you to kill a live checkout link and the locked prices inside it, so quotes past your cutoff get tagged, logged, and removed on schedule, not whenever someone gets around to it.

## Why this is a compiler problem, not an app problem

There are reminder apps for this, and the good ones do what they say: resend an email on the schedule you configured. A schedule is what an app can hold. What it cannot hold is the paragraph your follow-up policy actually is: nudge at two days and a week, then stop. [Trade accounts](https://blog.dugong.live/how-to-automatically-approve-wholesale-customers-on-shopify.html) get more patience than retail, and anyone on [volume pricing](https://blog.dugong.live/how-to-set-up-tiered-volume-discounts-on-shopify.html) gets a call, not a template. Anything over fifteen hundred dollars comes to me. Never chase what we can no longer fill. Kill everything at thirty days so nobody pays spring prices in August, and tell me what died, because that is pricing feedback. That paragraph changes with your margins, your lead times, and your patience. An app settings page cannot hold it. A compiler that turns the paragraph into the running workflow can, which is the argument behind [the automations no one builds](https://blog.dugong.live/best-shopify-automations-to-set-up.html): the valuable workflow is shaped like your store, not like a feature list.

Picture a furniture workshop in Asheville: forty quotes a month, mostly trade. Twenty-two pay on their own within a few days, and the other eighteen used to age out in silence unless the owner happened to remember one on a slow Friday. With the playbook running, eight pay after the day-two note and three more after day seven. Two reply with questions, get answers within the hour, and pay the same week. One turns into a quantity negotiation the owner takes over by phone, and the remaining four go quiet for good and are retired at day thirty, links dead, stock released, reasons logged. That is thirteen recovered quotes out of eighteen that used to be coin flips, and at the workshop's average quote of six hundred forty dollars, it is eight thousand three hundred twenty dollars a month that stopped depending on the owner's memory. Her involvement is one weekly summary and the occasional phone call she would have wanted to make anyway.

## The workflow worth building this week

Start with the number you do not have. Open Drafts, filter to Invoice sent, and count three things: how many there are, how old the oldest is, and what they add up to. Then look at last quarter and count how many of those drafts ever received a single follow-up. Most stores that quote at all discover a five-figure pipeline being run entirely on remorse.

Then automate the reading before the sending. For the first two weeks, let the workflow watch the drafts, write every reminder, and queue them for your click. You are checking its judgment: does it know a live negotiation from a stalled quote, does it catch the sold-out line item before nudging, does it sound like you. Once it has been right fifty times in a row, let the routine cadence run end to end and keep the escalations, the negotiations and the big-ticket calls, for yourself.

Describe it the way you would brief a new hire on their first morning. When we send a quote, stay on it. Nudge politely at two days, again at a week, once more at two, then let it go: tag it lost, note why, and delete it so the link dies. Answer the small questions yourself, the same hour. Bring me anything that turns into a negotiation and anything over fifteen hundred dollars. Never chase a quote we can no longer fill. And on Fridays, tell me how many we sent, how many paid, and how long they took, because that number is how I fix my prices. That is the brief. The compiler handles the sweeps, the drafts, and the timers, and the designer in Savannah pays for her pendants on Thursday because a two-line note landed Wednesday morning, while it was still just a bump between friends.

> **◆ READING** Two companion pieces if this one landed: [the wholesale application that sits all weekend](https://blog.dugong.live/how-to-automatically-approve-wholesale-customers-on-shopify.html), on the other queue where B2B revenue waits for a human click, and [the unpaid order that never cancels itself](https://blog.dugong.live/how-to-automatically-cancel-unpaid-orders-on-shopify.html), on the same silence after checkout instead of before it. Also worth reading: [the order that ships before the money lands](https://blog.dugong.live/how-to-stop-shipping-shopify-orders-with-payment-pending.html), on the unpaid order that reaches your fulfillment queue looking exactly like a paid one.

If you are a Shopify merchant with a Drafts page holding a hundred open quotes, a follow-up spreadsheet that was last current in March, or a customer who just paid last winter's price from a link you forgot existed, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Does Shopify automatically send reminders for unpaid draft order invoices?

No. Sending an invoice from a draft order sends exactly one email with a checkout link, and nothing follows it, ever. Shopify does have automatic payment reminders, up to five scheduled emails, but only for orders that have payment terms assigned, such as net 30, and a draft order has no due date for a reminder to count down from, so drafts are excluded entirely. Some merchants work around this by completing the draft as a pending payment order with short terms just to borrow the reminder machinery, but that turns every undecided quote into a real order that lands in reports, commits inventory, and needs a cancellation to undo when the customer never pays. The practical alternatives are a reminder app that resends on a fixed schedule, or an AI workflow that reads each draft and follows up the way a salesperson would, matching the cadence to the quote's value and stopping when the customer says no.

Permalink: https://blog.dugong.live/how-to-automatically-follow-up-on-unpaid-draft-orders-on-shopify.html#faq-1

### Do Shopify draft order invoice links expire?

Not on any schedule you control. The checkout link in a draft order invoice keeps working for as long as the draft exists, and because product prices in a draft are locked by default, a customer can open a months-old email and pay a price you have since raised. There is no cancelled status for draft orders, a gap merchants have a standing feature request open for, so the only way to kill a live link is to delete the draft itself. The single expiry Shopify applies is automatic deletion of drafts created on or after April 1, 2025 once they have sat inactive for a full year, and any edit resets that clock. A year is not a quote lifecycle. If your prices move, retiring old drafts deliberately, on a cutoff you choose, is the only real protection against last winter's quote being paid at last winter's price.

Permalink: https://blog.dugong.live/how-to-automatically-follow-up-on-unpaid-draft-orders-on-shopify.html#faq-2

### Can Shopify Flow follow up on unpaid draft orders?

Not with the customer. Flow has a Draft order created trigger, and it fires once, at the moment of creation, for drafts that contain products. There is no trigger for an invoice that has sat unpaid for a number of days, and the actions available against a draft are organizational, tagging mainly, with nothing that emails a customer about a draft at all. The accepted community workaround is a Scheduled time trigger that sends your own staff a list of open drafts on a schedule, which automates the reminder to you rather than the follow-up itself. A real follow-up means reading the draft's value, age, stock, and any reply that has already arrived before writing to a human being, then choosing between a nudge, an answer, an escalation, and retirement. That is judgment rather than a condition, and it is the part an AI workflow adds on top of what Flow can see.

Permalink: https://blog.dugong.live/how-to-automatically-follow-up-on-unpaid-draft-orders-on-shopify.html#faq-3

### How do I see which Shopify draft orders are still unpaid?

Open the Drafts page and filter to Invoice sent, because that is all the visibility Shopify gives you. A draft has exactly three states, Open, Invoice sent, and Completed, and only a customer can reach the third one, by paying. There is no aging view, no overdue state, and no due date, so a draft wears the same badge on day forty that it wore in the first hour, and this month's live quotes sit interleaved with long-dead ones. The useful exercise is to count three things on that filtered list: how many drafts there are, how old the oldest is, and what they add up to, then check how many ever received a single follow-up. Most stores that quote at all discover a five-figure pipeline being run entirely on remorse, which is why so many merchants end up keeping the real list in a spreadsheet next to Shopify.

Permalink: https://blog.dugong.live/how-to-automatically-follow-up-on-unpaid-draft-orders-on-shopify.html#faq-4

### What happens if a customer pays a draft order invoice after the stock has sold out?

The checkout refuses her, and the sale dies at the finish line. Shopify does not hold inventory for a draft order unless you deliberately reserve it, and nobody reserves stock for a maybe, so the customer who finally clicks the invoice link in week three can meet a checkout that declines the purchase because one line item sold out on Tuesday. Nobody alerts you when that happens either, so a quote that survived your silence is lost silently too. The protection is to check stock before every reminder: never chase payment for a quote you can no longer fill, and when a line has sold out, either re-quote honestly at current availability or decide whether to reserve the remaining units. A nudge that says pay now for items you cannot ship is worse than no nudge, because it converts your own follow-up into a refund and an apology.

Permalink: https://blog.dugong.live/how-to-automatically-follow-up-on-unpaid-draft-orders-on-shopify.html#faq-5

---

Markdown rendition of https://blog.dugong.live/how-to-automatically-follow-up-on-unpaid-draft-orders-on-shopify.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
