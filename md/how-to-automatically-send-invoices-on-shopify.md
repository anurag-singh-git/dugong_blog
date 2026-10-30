# How to automatically send invoices to Shopify customers

> Shopify sends a receipt, not a real invoice, and has no VAT field. The AI playbook that invoices every order and issues a credit note on refunds.

- Canonical: https://blog.dugong.live/how-to-automatically-send-invoices-on-shopify.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-07-06
- Updated: 2026-10-27
- Section: Research
- Word count: 2620
- Dispatch: Nº 78 · Research · 9 min read
- Full headline on page: How to automatically *send invoices* to Shopify customers
- Keywords: Shopify send invoice automatically, Shopify automatic invoice, Shopify PDF invoice, Shopify VAT invoice, send invoice to customer Shopify, Shopify B2B invoice tax number, Shopify order invoice email, Shopify tax invoice, Shopify credit note refund
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

There is a small, recurring tax on selling to anyone who buys for a business, and it lands after the sale is done. The order came in clean, the money is in, the box is on its way, and then the follow-up arrives: could you send us an invoice with our company name and VAT number for our records. What Shopify sent the customer at checkout was an order confirmation, which lists what they bought and what they paid, and reads like a receipt because that is what it is. It is not an invoice, it does not carry their tax registration number, and in most countries it is not the document their accountant will accept. So you open a template or a spreadsheet, retype their details, generate a PDF, and email it back by hand, and you do this again for the next business order, and the one after that.

This is one of those gaps that stays invisible until you have your first handful of business buyers, and then it never goes away. The Shopify community threads about it read like a slow accumulation of the same discovery. How do I send a proper invoice automatically. Where is the field for a customer's VAT number. Why does the order confirmation not count as a tax invoice. The answers underneath are always some mix of Shopify does not do that natively, rename the confirmation email, install an app, or regenerate it in your accounting software. Merchants are not asking for anything exotic. They want the obvious thing every offline business has always had: an order goes through, and a correct invoice goes out with it.

> The confirmation email did exactly what it was built to do. *It told the customer what they bought, and left out the one thing their finance team actually needed, so the real invoice still had to be made by hand.*

## The short answer

What Shopify emails after a paid order is a receipt rather than an invoice. It sets out what was bought and what was paid, shows neither party's tax registration number, and in most countries is not the document a buyer's finance team can file. Shopify Tax does produce a genuine VAT invoice for orders shipped inside the EU and the UK, and that one is worth turning on.

Its edges are where the work comes back. That VAT invoice is never emailed and only sits on the order status page, so customers assume nothing was sent and ask anyway. It is locked to EU and UK orders, and it cannot be reissued once an order has been edited. The checkout has no field for a buyer's tax number either, only a company name inside the billing address.

That missing number is why invoicing stays manual even with a PDF app installed, since Shopify cannot attach a file to its own emails and an app stamps one layout on every order. The working shape is classification first, a receipt or a full tax invoice, then a sequentially numbered document and a matching *credit note* whenever money goes back.

## What Shopify does and does not do about invoices

Give Shopify credit for the part it does. Every paid order fires an order confirmation email automatically, and for a straightforward consumer sale that confirmation is often all anyone needs. There is also a genuine tax-invoice feature inside [Shopify Tax](https://help.shopify.com/en/manual/taxes/shopify-tax): for orders shipped within the European Union and the United Kingdom, Shopify can generate a VAT invoice and display it on the order status page for the customer to view, save, or print. If your whole business is consumer sales inside those regions, that covers a real slice of the need, and it is worth turning on. The trouble is everything around the edges of that, and each limit is invisible until a specific customer or a specific market hits it.

It is **a receipt, not an invoice**, by default. The confirmation email is not structured as a formal invoice and carries no tax registration numbers, so a business buyer cannot hand it to their accountant. The VAT invoice that Shopify Tax does produce is **never emailed**; it sits on the order status page, so unless the customer goes and finds it, they assume nothing was sent and they ask. It is **region-locked** to EU and UK orders, so a store selling into other markets that also require formal invoices is back to doing it by hand. It **cannot be regenerated** after an order is edited, so a changed order means downloading the old invoice and annotating it manually. And most fundamental of all, Shopify's checkout has **no field for the customer's tax number**: it collects a company name in the billing address and nothing more, so the single detail a business-to-business invoice legally needs is the one thing the platform never captures.

## The tax number Shopify never collects

In much of the world, an invoice to a company is not valid unless it shows that company's VAT or tax registration number alongside your own. It is not a nicety, it is what makes the document a deductible business expense on their side and a compliant record on yours. And it is exactly the field Shopify's standard checkout does not have. The buyer can type their company name into the billing address, but there is nowhere to put the tax number, so it arrives, if it arrives at all, jammed into the order notes, or in a follow-up email, or not until you ask for it. The detail that the invoice cannot be finished without is the detail the checkout was never built to gather.

That missing field is why invoicing on Shopify almost always ends in manual work, even for stores that have installed something to make the PDF. The document can be templated, but the number that makes it valid has to be chased, matched to the right order, checked that it is a real registration and not a typo, and dropped into the invoice. It is the same shape of problem as [the order tag you set by hand](https://blog.dugong.live/how-to-automatically-tag-orders-on-shopify.html): the platform captured most of the order but not the one attribute your downstream process actually turns on, so a human fills the gap every time.

> **◆ DATA** The reason this is worth fixing is that invoicing scales with exactly the customers you most want. Every business buyer, wholesale account, and repeat company is another invoice to issue, another tax number to capture, and another credit note to cut when they return something. The work grows precisely as the high-value side of your book grows, and because each invoice looks like a small five-minute job, it never gets prioritized into an automation, it just quietly eats an afternoon a week and occasionally ships wrong.

## Why the usual workarounds don't hold

Faced with a platform that emails a receipt and leaves the invoice to you, merchants reach for a handful of moves. Each one gives back something you did not want to lose.

**"I will just rename the order confirmation to invoice."** The fastest fix, and the one that is not really an invoice. Editing the notification template to say Invoice at the top does not add the customer's tax number, does not give you a sequential invoice series, and does not produce a credit note when you refund. It looks like the document until an accountant or a tax authority looks closely, and then it is a receipt in a costume.

**"I will use the Shopify Tax VAT invoice."** The right instinct inside the EU and UK, and a partial one everywhere else. It is a genuine compliant invoice for those orders, but it never emails itself, so customers keep asking; it does not cover your other markets; and it cannot be reissued after you edit an order. You have automated one region's happy path and left the rest of the world, and every changed order, on the manual pile.

**"I will install a PDF invoice app."** Reasonable, and a fixed template bolted to your store. A good app generates a branded PDF and adds a download link to the confirmation email, which is real progress and proof the native gap exists. But Shopify does not let its emails carry attachments, so it is a link rather than the attached document many finance teams want, and the app applies one layout to every order: it does not decide that this order needs a full tax invoice and that one just needs a receipt, does not validate the VAT number, and does not know your reverse-charge rules. It prints the document. It does not make the judgment.

**"I will regenerate it in Xero or QuickBooks."** Accurate books, and double the handling. Rebuilding each Shopify sale as an invoice in your accounting software gives you a clean compliant document, but it means the sale now lives in two systems that have to be kept in step, and it is the same re-entry burden that makes [reconciling your payouts](https://blog.dugong.live/how-to-reconcile-shopify-payouts-with-your-sales.html) such a chore. You have moved the manual work, not removed it.

## What the automation actually has to do

The real job is not "make a PDF for this order." It is "take each order, decide whether it needs a plain receipt or a full tax invoice, fill in the buyer's company and tax details, generate a compliant numbered document, send it without being asked, and cut a matching credit note when the order is refunded, pulling in a human only for the calls that are genuinely tax decisions." That is a classification, a data-capture step, a document build, and a reversible counterpart on refunds. As a Dugong playbook, in plain prose, it reads like this:

```
# trigger
On an order being paid, and again on any refund

# steps
1. Read the order: line items, tax, discounts,
   shipping, customer, and consumer vs business
2. Decide the document: a receipt for a consumer,
   a full tax invoice when there is a company or VAT number
3. Fill the tax number from notes, a past order, or
   the customer record, and ask once if it is truly missing
4. Generate a compliant, sequentially numbered PDF
   with your and the buyer's details and the tax breakdown
5. Send it automatically in the order email and to
   the buyer's accounts address, no request needed
6. Issue a matching credit note against the invoice
   when the order is refunded in part or full
7. Hold a failed VAT check, a reverse-charge order,
   or an edited order whose invoice must be reissued
```

Seven lines. The compiler fills in the rest: reading the whole order rather than a single field, telling a consumer sale from a business one, capturing the tax number wherever it actually landed, keeping the invoice numbers sequential and gapless so the series survives an audit, sending the document at the moment of payment instead of when the customer chases it, and generating the credit note that keeps the books balanced on a refund. The merchant never opened a template and never retyped a company address. They described how a careful bookkeeper would invoice each order, and let the compiler do it on every order, in the background.

> **◆ NOTE** The trap here is treating every order the same. An invoice is not one document; it is a receipt for a consumer, a full tax invoice for a company, a reverse-charge note for a cross-border business sale, and a credit note when money goes back. A template that stamps the same layout on all of them ships invoices that are wrong for half your orders, and a VAT number pasted in without a validity check is worse than a blank one because it looks compliant. Knowing which document each order needs, and which one to escalate, is as much the point as producing the PDF.

## Why this is a compiler problem, not an app problem

There are capable PDF invoice apps on the Shopify App Store, and a store that invoices often should look at one. But the thing that makes automatic invoicing safe is not one more template. It is judgment about each specific order: does this one need a full tax invoice or just a receipt, is the buyer's VAT number present and valid, does this cross-border sale fall under reverse charge, and does an edited order need its invoice reissued against the same number. Those answers change per order, per customer, and per market, which is exactly what a fixed template handles badly and a person handles too slowly to keep up with a growing book of business buyers. It is the same reason [segmenting your repeat customers](https://blog.dugong.live/how-to-segment-repeat-customers-on-shopify.html) resists a single rule: the useful distinctions live in the pattern, not in one threshold.

A natural-language compiler fits because invoicing was never a single action. It is a classification, a data capture, a compliant document build, an automatic send, and a reversible credit note, and it has to run again every time an order changes or is refunded. You can describe the whole behavior in a paragraph. You could never keep up with it by hand across every business order, every market, and every return. It sits in the same family as [the second order that arrives before the first ships](https://blog.dugong.live/how-to-combine-multiple-orders-from-the-same-customer-on-shopify.html), where the right move depends on reading the specific orders rather than firing one rule, and [the order change that races your warehouse](https://blog.dugong.live/how-to-edit-a-shopify-order-after-its-been-placed.html), where an edit has to ripple cleanly through everything downstream, the invoice included.

## The workflow worth building this week

If you sell to businesses at all, or into any market where a formal invoice is expected, and you have ever retyped a customer's company details into a template after the sale was already done, this is the automation to set up now, because the work scales with your best customers and every one of them expects the document as a matter of course. It pairs naturally with the finance and order work we have written about, like [the payout that never matches your sales](https://blog.dugong.live/how-to-reconcile-shopify-payouts-with-your-sales.html), the other half of keeping your books straight, and [the unpaid order that never cancels itself](https://blog.dugong.live/how-to-automatically-cancel-unpaid-orders-on-shopify.html), where a draft invoice sent to chase payment is part of the same flow, and it feeds the same flywheel as [the Shopify automations no one builds](https://blog.dugong.live/best-shopify-automations-to-set-up.html), where the work that compounds is the part merchants never get to.

Describe it the way you would brief a careful bookkeeper: for every order, work out whether it needs a receipt or a full tax invoice, put the company and tax details on it, number it in sequence, and send it the moment the order is paid, and cut a credit note whenever we refund, and bring me anything where the tax number does not check out or the order is a reverse-charge or export. That is the whole brief. The compiler does the classification, the capture, the document, the send, and the credit note, on every order. Your business buyers get the invoice they were going to ask for before they ask, and your books stay clean without anyone retyping an address.

> **◆ READING** If this resonates, two companion pieces: our dispatch on [the payout that never matches your sales](https://blog.dugong.live/how-to-reconcile-shopify-payouts-with-your-sales.html), the reconciliation side of keeping Shopify finances clean, and [the order tag you set by hand](https://blog.dugong.live/how-to-automatically-tag-orders-on-shopify.html), where reading the whole order and acting on it beats a single blunt rule. Also new: [the overdue invoices nobody adds up](https://blog.dugong.live/how-to-chase-overdue-shopify-b2b-invoices.html), on chasing the same business buyer once the order exists and the terms are running.

If you are a Shopify merchant who has built something that invoices every order correctly and cuts credit notes on refunds without anyone touching a template, or you have a story about a business buyer whose invoice you have retyped one too many times, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Does Shopify automatically send an invoice after an order?

No. Shopify automatically sends an order confirmation email, which is a receipt of what was bought, not a formal invoice. For most stores there is no native downloadable PDF invoice and no way to auto-send a proper tax invoice. Shopify Tax can generate a VAT invoice for orders shipped within the EU and UK and show it on the order status page, but even that is not emailed to the customer automatically, so any business buyer who needs an invoice with company and tax details still has to ask, and someone produces it by hand.

Permalink: https://blog.dugong.live/how-to-automatically-send-invoices-on-shopify.html#faq-1

### Can Shopify collect a customer's VAT or tax number at checkout?

Not with a dedicated field. Shopify's checkout collects a company name in the billing address, but there is no standard field for a customer's VAT or tax registration number, which a business-to-business invoice legally needs in many countries. Merchants work around it by asking the buyer to type the number into the order notes, adding it as a customer note in the admin after the fact, or collecting it through a checkout customization or app. Because the number is not captured cleanly at the source, the invoice that needs it is almost always finished by hand.

Permalink: https://blog.dugong.live/how-to-automatically-send-invoices-on-shopify.html#faq-2

### How do most Shopify stores send invoices today?

Usually one of three ways, and all of them cost time. Some rename the order confirmation email to look like an invoice and paste in the company and tax details each time. Some install a PDF invoice app, which adds a download link to the confirmation email, though Shopify cannot attach files to its emails, so it is a link rather than an attachment, and the app applies one fixed template to every order. Some regenerate the invoice in Xero or QuickBooks, which means re-entering the sale in a second system. The better approach is to describe the invoice rules once, per market and per customer type, and let it produce and send the right document for every order.

Permalink: https://blog.dugong.live/how-to-automatically-send-invoices-on-shopify.html#faq-3

### What happens to the invoice when a Shopify order is edited or refunded?

Both events invalidate the document you already sent, and Shopify handles neither. The VAT invoice that Shopify Tax generates cannot be regenerated after an order is edited, so a changed order means downloading the old invoice and annotating it by hand. A refund, partial or full, needs a matching credit note issued against the original invoice to keep the books balanced on both sides, and nothing native produces one. Numbering is what makes both jobs delicate: an invoice series should stay sequential and gapless so it survives an audit, which rules out quietly deleting a bad invoice, and means an edited order needs its invoice reissued rather than replaced with a new number. A working automation treats the refund and the edit as triggers of their own, cutting the credit note or the corrected invoice automatically and holding only the genuine tax judgment calls for a person.

Permalink: https://blog.dugong.live/how-to-automatically-send-invoices-on-shopify.html#faq-4

### Do business orders need a different invoice than consumer orders?

Yes, and treating every order the same is the trap. An invoice is not one document: a consumer sale needs a receipt, a company purchase needs a full tax invoice carrying both parties' details and the buyer's VAT or tax registration number, a cross-border business sale may fall under reverse charge, and a refund needs a credit note. A template that stamps one layout on all of them ships documents that are wrong for half your orders. The judgment step matters more than the PDF build: a VAT number pasted in without a validity check is worse than a blank one, because it looks compliant while being useless to both sides. So the automation's first move on every order is classification, receipt or tax invoice, and its escalation list is the genuinely hard calls: a failed VAT check, a reverse-charge order, an edited order needing reissue.

Permalink: https://blog.dugong.live/how-to-automatically-send-invoices-on-shopify.html#faq-5

---

Markdown rendition of https://blog.dugong.live/how-to-automatically-send-invoices-on-shopify.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
