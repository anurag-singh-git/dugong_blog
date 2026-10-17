# How to make Shopify wholesale customers tax exempt without checking certificates by hand

> Shopify gives you a tax exempt switch and no certificate record: no number, no expiry, no document. The AI playbook that reads, validates and renews every one.

- Canonical: https://blog.dugong.live/how-to-make-shopify-wholesale-customers-tax-exempt.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-10-10
- Section: Research
- Word count: 1950
- Dispatch: Nº 122 · Research · 8 min read
- Full headline on page: How to make Shopify wholesale customers *tax exempt* without checking certificates by hand
- Keywords: shopify tax exempt customer, shopify wholesale tax exempt, shopify resale certificate, shopify b2b tax exemption, taxExemptions, resale certificate expiry, exemption certificate automation, verify resale certificate
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

A new wholesale account in Florida places a $2,400 order on a Tuesday and emails forty minutes later: we are tax exempt, certificate attached. You open the attachment. It is a photograph of a form lying on a desk, one corner outside the frame, the signature line empty.

Somebody on your team now spends eleven minutes on this. They squint at the form, decide it looks official enough, open the customer in Shopify, flip the tax setting, refund the tax on the order, and move on. The certificate goes into a Drive folder, or stays in the thread, or goes nowhere at all. Nobody writes down the number. Nobody writes down the expiry. And in Florida, that certificate dies on December 31st.

Do that forty times across twelve states and you have built something that looks like a wholesale program and functions like an unlabeled box of paper. Merchants ask about this in the open: a recent Shopify community thread, titled roughly *how are you verifying tax exempt certificates or professional licenses for B2B customers*, describes exactly this process, reading the PDF, checking a state website, approving the customer by hand, and asks the obvious question of what happens when the account count grows.

## Shopify gives you a switch, not a record

The native mechanism is real and it works. Open a customer, open the menu in the Customer section, choose Manage tax settings, and pick one of two things: *Don't collect tax*, which zeroes tax for that buyer everywhere, or *Collect tax unless exemptions apply*, where you select specific exemptions. Under the hood those are a boolean, `taxExempt`, and a list, `taxExemptions`, whose values are per-jurisdiction codes: `US_CA_RESELLER_EXEMPTION`, `US_FL_RESELLER_EXEMPTION`, one for every state, plus Canadian and EU equivalents.

Read that list of fields again and notice what is not in it. There is no certificate number. No issuing form. No signature date. No expiry date. No document. No record of who approved it or what they checked. Shopify stores the *conclusion* of your verification and discards the verification. The flag you set on a Tuesday in October looks identical to a flag set three years ago against a certificate that lapsed before last Christmas.

Three more mechanics worth knowing before you build anything on top:

**The exemption follows the customer, not the cart.** It applies to the whole customer rather than specific products, and it overrides your product and shipping tax overrides. The buyer who is exempt on a pallet of resale stock is also exempt on the sample kit they keep.

**It only fires under the right email.** Shopify applies the exemption when the customer checks out with the email address on their account. A guest checkout, a second work address, an express wallet carrying a hide-my-email relay, or an order rung up at your counter under a phone number: all taxed in full, and all arriving in your inbox as a complaint.

**B2B company locations are a separate system.** On plans that support Shopify B2B you can set tax settings per company location, which is the right shape when one business buys through five contacts. It is also plan-gated, so most merchants reading this are working at the customer level.

## Three ways this costs you money

The first is the one you hear about. You charge tax to a buyer who should not pay it, they email, you refund, you apologize. Annoying, survivable, and visible.

The second is the one you do not hear about. You do not charge tax to someone who should have paid it, because the flag is on and the paper behind it is not good. When a state comes asking, it asks you, not your customer. An expired certificate offers no protection, which is the quiet sentence that makes this whole workflow worth automating.

The third is the slow one: the exemption that outlives its certificate. This is where state rules stop being trivia and start being an operations problem, because they are wildly inconsistent.

Florida's annual resale certificate expires at the end of each calendar year. Alabama runs a year. Louisiana resale certificates were cut to a year. Connecticut and Iowa run three, Rhode Island and Washington four, Maryland and Nevada five. Illinois resale certificates run three. Michigan runs four unless there is a recurring business relationship. Kansas ties validity to activity: the relationship has to keep going, with no more than twelve months between purchases. Meanwhile California, New York, Texas, New Jersey and most other states set no fixed term at all, but their certificates go invalid the moment the buyer's name, address, permit status or qualifying activity changes. Record retention is its own clock, commonly three to four years after the sale.

None of that lives in Shopify. All of it is your responsibility. And to be plain about what this piece is: these are operations notes, not tax advice, and every rule above deserves a check against the relevant state's department of revenue before you encode it.

## Why Shopify Flow does not reach this

Flow is the obvious first thought, and it gets about a third of the way. Its customer actions are adding and removing customer tags, updating a customer metafield, updating the customer note, getting customer data and looking a customer up in a segment. There is no action for tax exemption. You can reach the mutation through the *Send Admin API request* action, which runs most mutations that are not yet exposed as actions, so the write is a solved problem.

The write was never the hard part. The hard part is the eleven minutes: opening a crooked photo, deciding whether it is the right form for the state in question, whether it is complete, signed and dated, whether the business name on it is the business in your customer list, whether the number matches that state's format, and whether the resale claim is even plausible for the order attached to it. Those are judgements. A condition builder cannot make them, and merchants in that community thread say the same about plain character recognition: it speeds up data entry and will not tell you whether a document is valid.

## The playbook worth building

As a Dugong playbook, in plain language:

```
# trigger
Every certificate upload and new
wholesale application, plus a
daily expiry sweep

# steps
1. Collect through one door: state,
   form, number, signer and the
   document itself
2. Read the file: form type, state,
   number, business name, address,
   signature, dates
3. Validate: right form for that
   state, fully completed, signed,
   name matches the account,
   number in the right format
4. Check the state register where
   one exists, flag plainly where
   it does not
5. Set the per-state exemption,
   not the blanket switch, plus
   tag and metafields for number
   and expiry
6. Keep checkout taxed until a
   human approves
7. Sweep expiries by state rule:
   chase at 60, 30 and 7 days,
   revoke on lapse
8. File the evidence: document,
   every check, every decision,
   dated
```

**Step five is where most stores go wrong.** Don't collect tax is the tempting option because it is one click and it always works. It also removes tax in every state, including the ones where this buyer holds no certificate at all. Set the specific exemption for the specific state and you keep a defensible position instead of a blunt one.

**Step six is the one that saves you.** Exemption is the result of an approved certificate, never a checkbox a buyer ticks for themselves at signup. Until the document clears, the account checks out taxed like anyone else. If the review takes a day, that is one tax refund, which is a far cheaper mistake than an exemption granted on a photograph nobody read.

**Step seven revokes, and that is the uncomfortable part.** Chasing a renewal three times and then turning the exemption off feels rude to a good customer. Leaving it on feels polite right up until an auditor asks for the certificate behind two years of untaxed invoices. Chase early, chase specifically, name the date in the message, and turn it off on the day it lapses.

## The two reports nobody runs

Once the records exist, two monthly queries pay for the whole build. The first lists orders where tax was charged to an account you have marked exempt, which catches the email mismatches, the guest checkouts and the counter sales. The second lists untaxed orders shipping into a state where you hold no valid certificate for that buyer, which catches the flags that drifted out of scope.

Both are cheap to fix in the month they happen. The first is a refund and a note. The second is a conversation with a customer who will almost certainly send the paperwork. Six quarters later, neither one is cheap.

## Where AI earns its place

The genuinely hard inputs here are documents, and documents are what models are good at now. A certificate arrives as a crooked phone photo, a scan with the staple shadow across the number, or a PDF someone filled in with a touchpad. The model pulls the state, the form, the number, the business name, the address and the dates, then reasons about them: this is the Florida annual form and not a Georgia one; the buyer signed it but never dated it; *Acme LLC dba Acme Supply* is the same business as the *Acme Supply Co* in your customer list; this number is four digits short.

It also holds the state rulebook without complaint, which is the part no small team keeps in its head. Forty-six jurisdictions, each with its own form, its own validity period and its own idea of what invalidates a certificate. A model can carry that and compute the expiry date the moment it reads the signature date.

The honest limits matter as much. Where a state publishes no lookup for its certificates, and New Jersey is the standard example, no amount of reading turns a document into a verified fact, so the right output is a clear flag rather than a confident verdict. Professional license checks are worse: every board has its own portal and there is no shared interface to query. And a final tax position should sit with a person who owns it. The automation's job is to make that person's queue small, their evidence complete, and their certificates never silently expired.

## Set it up this week

Export your customer list filtered to tax exempt. For each one, answer two questions: can you find the certificate in under a minute, and can you state its expiry date. The accounts that fail both are your actual exposure, and in most stores that run a wholesale channel the number is higher than anyone expects.

Then write down the states you are registered in, the validity rule for each, and the single place certificates will live from now on. That list is the whole configuration. Everything after it is reading documents and sending reminders, which is exactly the work worth handing to an agent.

> **◆ READING** Two companion pieces if this one landed: [The wholesale application that sits all weekend](https://blog.dugong.live/how-to-automatically-approve-wholesale-customers-on-shopify.html), on vetting and answering B2B signups in minutes instead of days, and [The quote that goes quiet](https://blog.dugong.live/how-to-automatically-follow-up-on-unpaid-draft-orders-on-shopify.html), on chasing the wholesale invoices Shopify never follows up on.

Running a wholesale channel with a certificate story, the audit letter, the buyer who has been exempt since 2023 on a document nobody can find, the Florida account that expired in January? The inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### How do I make a customer tax exempt on Shopify?

Open Customers, click the customer, open the menu in the Customer section and choose Manage tax settings. Then pick either Don't collect tax, which zeroes tax for that buyer everywhere, or Collect tax unless exemptions apply, which lets you select specific exemptions such as a reseller exemption in one state. Save, and it applies when that customer checks out with the email address on their account. Two things catch merchants out: the exemption covers the whole customer rather than specific products, and it overrides your product and shipping tax overrides. On plans that support Shopify B2B you can set tax settings per company location instead, which fits better when one business buys through several contacts.

Permalink: https://blog.dugong.live/how-to-make-shopify-wholesale-customers-tax-exempt.html#faq-1

### Does Shopify track resale certificate expiry dates?

No. Shopify stores a flag on the customer, taxExempt, plus an optional list of per-state exemptions such as US_CA_RESELLER_EXEMPTION. There is no field for the certificate number, the form, the signature date, the expiry or the document, and nothing warns you when one lapses. That matters because the rules differ sharply: Florida's annual resale certificate expires at the end of each calendar year, Alabama and Louisiana resale certificates run a year, Connecticut and Iowa three, Rhode Island and Washington four, Maryland and Nevada five, while California, New York, Texas and most others set no fixed term but go invalid when the buyer's name, address or permit status changes. Store the number and a computed expiry in customer metafields and sweep them, because the switch will happily stay on for years. Confirm each rule with the relevant state before you encode it.

Permalink: https://blog.dugong.live/how-to-make-shopify-wholesale-customers-tax-exempt.html#faq-2

### Can Shopify Flow set a customer as tax exempt?

Not with a built-in action. Flow's customer actions are adding and removing customer tags, updating a customer metafield, updating the customer note, getting customer data and looking a customer up in a segment. None touch tax exemption. You can reach the mutation through the Send Admin API request action, which runs most mutations not yet available as actions, so the write is solvable. What Flow cannot do is the part that takes the time: opening a phone photo of a certificate and deciding whether it is the right form for that state, complete, signed, in the right number format, and in the name of the business in your customer list.

Permalink: https://blog.dugong.live/how-to-make-shopify-wholesale-customers-tax-exempt.html#faq-3

### Why is Shopify charging tax to my tax exempt wholesale customer?

Usually because the order did not travel under the account you flagged. Shopify applies the exemption when the buyer checks out with the email on their customer account, so a guest checkout, a second work email, an express wallet carrying a relay address or a counter sale under a phone number can all be taxed in full. The other common cause is scope: an exemption selected for one state does nothing for an order shipping to another, which is correct rather than a bug. One more trap if your prices are tax inclusive: an exempt customer pays the same listed price, so the exemption shows up in your tax reporting rather than as a visible discount. The fix is a monthly reconciliation of exempt accounts charged tax and untaxed orders with no certificate on file.

Permalink: https://blog.dugong.live/how-to-make-shopify-wholesale-customers-tax-exempt.html#faq-4

### Can AI verify resale certificates for Shopify wholesale customers?

It can do most of the work and should not do all of it. A model reads a crooked photo or a scanned PDF, extracts the state, form, number, business name, address, signature and dates, checks the form against the state it was written for, matches a trading name to the account, flags a blank signature or missing date, computes the expiry from that state's rule, and queries a state lookup where one is published. What it cannot honestly do is certify a position in a state that publishes no lookup, and New Jersey is the standard example, or query professional licensing boards that share no common interface. So the automation's job is to shrink the human queue to the genuinely ambiguous cases, set exemptions only after approval, and make sure no certificate expires in silence.

Permalink: https://blog.dugong.live/how-to-make-shopify-wholesale-customers-tax-exempt.html#faq-5

---

Markdown rendition of https://blog.dugong.live/how-to-make-shopify-wholesale-customers-tax-exempt.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
