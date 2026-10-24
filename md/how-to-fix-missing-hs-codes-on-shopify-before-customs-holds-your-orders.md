# How to fix missing HS codes on Shopify before customs holds your orders

> De minimis is gone and every parcel needs the HS codes your catalog never carried. The AI playbook that classifies products before customs bills your customer.

- Canonical: https://blog.dugong.live/how-to-fix-missing-hs-codes-on-shopify-before-customs-holds-your-orders.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-08-13
- Updated: 2026-10-24
- Section: Research
- Word count: 3000
- Dispatch: Nº 107 · Research · 10 min read
- Full headline on page: How to fix *missing HS codes* on Shopify before customs holds your orders
- Keywords: shopify hs codes, add hs codes shopify, missing hs code, bulk edit hs codes, country of origin shopify, customs information, duties wrong at checkout, de minimis, customs hold, AI hs code classification
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

The email lands Thursday at 7:52 am, from a customer in Denver. There is a card from the carrier, she writes, asking for $61.84 in import charges before they will hand over her order, and she wants to know if it is a scam. It is not. It is a $78 box of taper candles from your studio in Manchester, and it cleared US customs the way every underdocumented parcel clears customs now: by billing the person least able to fix it.

Two years ago that parcel was invisible. Anything valued under $800 entered the United States duty free under the de minimis rule, which meant the two customs fields on a Shopify product, the HS code and the country of origin, could stay blank for an entire business lifetime without costing a cent. Executive Order 14324, signed July 30, 2025, ended that on August 29, 2025, for every country and every value at once. The response told you how unprepared the world's parcel infrastructure was: in the last week of that August, more than 20 national postal operators, Japan Post announcing on the 25th, Australia Post and Royal Mail stopping on the 26th, much of Europe in the same few days, paused US-bound parcels in whole or in part rather than guess at paperwork they had never been asked for. A temporary flat fee of $80 to $200 per postal package softened the landing for six months; that window closed at the end of February 2026. Then on July 1, 2026, the European Union removed its own 150 euro exemption and replaced it with a flat 3 euro duty counted per product category, and the category is the six digit tariff subheading: a parcel spanning three headings pays three times. Read that twice, because it quietly redefines the field in your admin. The HS code is no longer paperwork that travels with the parcel. It is the unit the bill is counted in.

Your catalog was not built for that. Most catalogs were not. The fields were optional when every product in them was created, no import requires them, no theme displays them, and nothing in the admin has ever chased you about the blanks. The border chases your customer instead.

## The short answer

Fill the HS code and the country of origin on every variant, because both fields live on the variant rather than the product and nothing in Shopify enforces them. A product created tonight publishes, sells and ships without either. Shopify added a store level default for country of origin in May 2025, and there is still no equivalent for HS codes: no default, no product level value, no inheritance.

Leave them blank and duties at checkout fall back to the description and the product category, which the help center itself calls likely to be inaccurate, and warns might put additional duties on your customer at delivery. That is the carrier texting a payment link to someone who already paid. A wrong code fails in the other direction: one merchant measured duties computed at 95 to 100 percent of the price where the correct rate was 3.5 to 5 percent, and nobody checks out through that.

Three native routes exist: one variant at a time on the product page, the bulk editor, and the duties CSV under Settings, then Taxes and duties, which exports the products with information missing and is the closest thing to a coverage report. None survives 400 products at three variants, which is 1,200 fields. What does is proposing six digit codes from title, description and materials with confidence attached, sending confident batches to the bulk editor and the tail to a human, and flagging any product that goes live without codes the same *hour*.

## Two fields nobody filled in

Both fields live on the variant, not the product. The HS code is typically six digits, the part harmonized across countries by the World Customs Organization, and individual countries hang extra digits off the end for their own tariff lines: Shopify's documentation uses 3210.00 as the global code with 3210.00.123 as a UK-specific refinement, and checkout uses the more specific code when one exists. The country of origin is where the product was made or assembled into the thing you sell, not where you ship it from, and the distinction matters because the duty rate is keyed to both fields together.

There are exactly three ways to fill them in. One product at a time on the product page, where typing a description searches for candidate codes. In bulk through the bulk editor, adding the HS code field by hand. Or through a dedicated duties CSV that lives under Settings, then Taxes and duties, which will export your products with missing information, a detail worth knowing because it is the closest thing the platform has to a coverage report, and it only runs when you go get it. Shopify added a store level default for country of origin in May 2025, one value that backfills any variant without its own. For HS codes there is no equivalent: no default, no product level value, no inheritance.

Merchants have started saying this out loud. A June 2026 feature request describes the arithmetic on one product: a hand poured candle in 17 colors is 17 variants, identical in material and origin, and the same code has to be entered 17 times. A reply in July widens the lens: three variants across 400 products is 1,200 fields, most of them the same code, and the reply also explains why a blind product level default would be wrong, because the same bag lands on a different heading in leather than in canvas. Per variant is correct and per variant by hand is unworkable, which is roughly the situation [alt text was in](https://blog.dugong.live/how-to-add-alt-text-to-shopify-product-images-in-bulk.html) before someone let software read the images.

And nothing enforces any of it. A product created tonight publishes without codes, sells without codes, and ships without codes. The one screen that reviews the gap, a step in the duties at checkout setup that flags products with missing information, runs once, during setup, on the catalog you had that day. The products you add next month answer to nobody.

## What a blank costs at the border

Shopify does its best with what it has, and what it has degrades in a documented cascade: if a product is missing its HS code, duties at checkout are estimated from the description and the product category instead, and if those are missing too, the calculation still runs and the help center says the result is likely to be inaccurate. The same page carries the sentence that should be printed above every import button: inaccurate product information, such as a missing country of origin or an incorrect HS code, might result in additional duties being charged to the customer upon delivery.

Charged to the customer upon delivery is the polite version of the Denver email. The carrier fronts the duty, adds a brokerage fee, and texts your customer a payment link. Some pay it and quietly resent you. Some refuse the parcel, and it rides back across the ocean at your expense to a returns pile that [nobody restocks](https://blog.dugong.live/how-to-automatically-restock-returns-on-shopify.html). Either way the tracking page shows a week of customs limbo first, which is why a customs hold is so often mistaken for [a shipment stuck in transit](https://blog.dugong.live/how-to-catch-shopify-orders-stuck-in-transit.html): the package is not lost, it is impounded, and the six digits that would have released it were never in your catalog to print.

Get the code wrong instead of blank and the failure changes direction. A community thread titled Shopify charging 100 percent duties on certain products to the US had collected 20 replies and over 1,200 views by August 2026 and was still active this month: one UK merchant measured duties computed at 95 to 100 percent of the product's price where the correct rate was 3.5 to 5 percent. Nobody checks out through a doubled total, so the error costs you the sale instead of the refund, and no report anywhere will tell you it is happening.

The stories underneath these threads are not edge cases. The merchant who opened the tariff calculation thread two days after de minimis ended ships 70 percent of their business to the US and was running dry run orders to see what checkout would charge. The answer was the wrong method entirely: their postal carrier applies the flat postal tariff, Shopify's calculator assumed a commercial carrier and stacked HS code duties on top, and support's written reply conceded the mismatch, said the team was working to align the calculator with the new postal rules, offered no timeline, and confirmed you are not the only merchant experiencing this. A year later the successor threads, UK sellers on the new tariffs, constant issues with the duty calculator, were still collecting replies. And the fee makes it personal: calculating duties at checkout costs 0.85 percent per order on [Shopify Payments](https://help.shopify.com/en/manual/payments/shopify-payments), 1.5 percent on other gateways, temporarily lowered to 0.5 percent since February 2025, and it is charged on every order the calculation runs on, including the ones where it ran on blanks.

> **◆ NOTE** The dates that did this: July 30, 2025, Executive Order 14324 signs. August 29, 2025, US de minimis ends for all countries, and 20 plus postal operators pause US-bound mail the same week. End of February 2026, the $80 to $200 postal flat fee window closes. July 1, 2026, the EU's 150 euro exemption ends, replaced by 3 euros per six digit subheading until July 2028. November 1, 2026, EU line items need three product identifiers, and Shopify has native fields for two of them.

## Six digits of judgment

So the fix is to fill in the fields, and here the problem changes shape, because classification is not data entry. The Harmonized System is a nomenclature of more than five thousand six digit subheadings, revised on a five year cycle, with general rules of interpretation about sets, mixtures, and essential character that customs brokers train on. The difference between two plausible codes is routinely the difference between a single digit duty rate and a double digit one. Guessing low on purpose stopped being a quiet trick, too: replies on the same community threads now warn that customs agencies are penalizing mismatched paperwork, and point to a DOJ and DHS trade fraud task force with whistleblower incentives that reward logistics workers for reporting intentional misclassification. The code has to be right, defensibly, per variant.

Shopify's own tooling concedes the judgment is the hard part. The product page search takes a typed description and suggests codes, one product at a time. Managed Markets assigns codes automatically when you activate it, and the documentation is careful to say the assigned code is not guaranteed to match the one you entered, which is a sentence worth reading as a to-do: somebody should review the differences, and no screen makes that a job.

Here is what makes this tractable in 2026: classifying a product from its title, description, and materials is a reading task, and reading tasks are what language models do. A model that has seen the nomenclature can propose 3406.00 for the taper candle, flag that the ceramic candle holder bundled in the gift set belongs to a different chapter, attach a confidence score and its reasoning to both, and do it four hundred times before lunch. That is the same trick that [writes the product descriptions nobody had time for](https://blog.dugong.live/how-to-generate-shopify-product-descriptions-with-ai.html), pointed at a field where the blank has a customs officer at the end of it. What it must not do is publish silently: high confidence proposals batch into the [bulk editor](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/bulk-editing) with an audit trail, low confidence ones queue for a human, and the genuinely ambiguous handful go to a broker once and come back as a written rule.

## What the automation actually has to do

Filling today's blanks is a project. Staying filled is a process, because the catalog keeps moving: new products, new variants, new suppliers, a materials change that quietly invalidates last year's code. The worker this needs watches the catalog and the border rules at the same time. As a Dugong playbook, in plain prose:

```
# trigger
On every product published or edited,
and every international order

# steps
1. Audit the catalog: HS code, country
   of origin, and weight per variant,
   coverage counted and kept current
2. Classify with AI: propose six digit
   codes from title, description, and
   materials, confidence attached
3. Review the tail: high confidence
   batches to the bulk editor, low
   confidence to a human or a broker
4. Guard the door: a product that goes
   live without codes gets flagged the
   same hour, not at the border
5. Check the order: international
   orders carrying a codeless line item
   get held before the label prints
6. Watch the estimates: checkout duty
   against carrier invoice, anomalies
   flagged as misclassification signals
7. Report monthly: coverage, codes
   changed and by whom, duty disputes
   and doorstep complaints
```

Steps one through three are the backfill, and the audit is broader than the codes: Switzerland needs a weight before checkout can price duties at all, so the sweep counts weights and origins too, and reads plausibility while it is there, because a catalog where every product shares one code is usually a catalog where somebody pasted their way out of a warning. Step four is the difference between a project and a process. The platform checks your catalog once, during duties setup; the playbook checks every product the hour it publishes, which is the only moment the fix costs nothing, because no order is carrying it yet.

Step five is the seatbelt, and it is the same reflex as [holding the bad address before the label prints](https://blog.dugong.live/how-to-validate-shipping-addresses-on-shopify.html): an international order containing a line item with no code is a doorstep bill in progress, and it is cheaper to hold it for an hour than to argue about $61.84 across an ocean. Step six closes the loop nobody closes: checkout collected a duty estimate, the carrier invoiced a real one, and the gap between them is your misclassification report, the place a 100 percent anomaly or a silently absurd rate surfaces before a thread does. When a hold does happen, the customer hears it from you first, with the [delay named honestly](https://blog.dugong.live/how-to-notify-customers-of-shipping-delays-on-shopify.html), not from a carrier's payment link.

## Why this is a compiler problem, not an app problem

There are bulk editor apps for HS codes now, and they are fine at what they do, which is move values into fields faster. The judgment is the part that does not fit in their checkboxes: which chapter your gift sets belong to when the candle and the holder disagree, whether your origin is where the wax is poured or where the components came from, which SKUs earn a broker's hour and which can ride a model's 97 percent, what happens to the order that arrives while a code is missing, and who gets told when the EU adds a third identifier in November. Those are sentences about your store, and the argument of [the automations no one builds](https://blog.dugong.live/best-shopify-automations-to-set-up.html) applies verbatim: the sentences should compile into the workflow, instead of being shaved down to whatever a settings page exposes.

Run the Denver order again with the sentences compiled. The gift set publishes Tuesday; within the hour the agent flags it, proposes 3406.00 for the tapers at high confidence, routes the ceramic holder to you with two candidate headings and a recommendation, and you approve both from your phone. Wednesday's order to Denver ships with codes on the customs form, checkout collected $9.12 of duty with the parcel, and the carrier releases it without a text. The email that arrives Thursday at 7:52 am is the customer saying the candles smell like the shop in Manchester she visited in March. Nothing interesting happened at the border, which is the entire point.

## The workflow worth building this week

Start with the export the platform already gives you. Go to Settings, then Taxes and duties, then Manage, and export the duties CSV of products with missing information. That file is your blank map. Sort it against last quarter's international orders and the gap stops being abstract: these forty products carried revenue across a border with no code attached.

Fix the top of that list first, by hand or with the classifier proposing and you approving, and set the country of origin default while you are in the settings, because it backfills every blank origin in one save. Then run the watcher in propose-only mode for two weeks: let it classify new products and flag gaps, and check its homework. You are calibrating where its confidence deserves yours, exactly the drill from the [pricing guardrail](https://blog.dugong.live/how-to-catch-pricing-errors-on-shopify-before-orders-flood-in.html), applied to a slower moving field.

Then say the brief out loud, the way you would hand customs to a new hire. Every variant carries an HS code, an origin, and a weight, and you tell me our coverage number when I ask. Propose codes for anything new the hour it publishes; publish the confident ones with a record of what changed, bring me the doubtful ones, send the truly odd ones to the broker and remember the answer. Hold any international order carrying a blank. Compare what checkout charged with what the carrier billed, and treat a big gap as a wrong code until proven otherwise. Once a month, show me coverage, changes, and every duty complaint. That is the whole paragraph. The compiler turns it into the workflow, and the next card the carrier leaves is for a parcel that is not yours.

> **◆ READING** Two companion pieces if this one landed: [the image alt text no one writes](https://blog.dugong.live/how-to-add-alt-text-to-shopify-product-images-in-bulk.html), on the other catalog field everyone skips until it costs them, and [the bad address that ships anyway](https://blog.dugong.live/how-to-validate-shipping-addresses-on-shopify.html), on catching order data problems before the label prints. Also worth reading: [the order from a state you can't ship to](https://blog.dugong.live/how-to-restrict-shopify-products-from-shipping-to-certain-states.html), on the other compliance field Shopify will happily let you sell without.

If you are a Shopify merchant with a customs story, the parcel that came back with a bill, the duty calculated at double the price, the classification you still argue about, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Do I need HS codes on every Shopify product?

Shopify's help center is unambiguous: HS codes are required for all international orders, and some destinations, Switzerland is the named example, also need a product weight before duties can be calculated at checkout. What the platform does not do is enforce any of it. A product publishes and sells with both customs fields blank, and the gap only surfaces at the border. If you sell domestically today, blanks cost nothing until the first international order, and that order is rarely announced in advance. Since August 29, 2025 every shipment into the US owes duty regardless of value under Executive Order 14324, and since July 1, 2026 the EU charges a flat 3 euro duty per six digit tariff subheading on parcels under 150 euros, so the code is no longer paperwork that travels with the parcel, it is the unit the bill is counted in. The practical rule: every variant that could ever cross a border needs its six digit code and its country of origin, and the fields live on the variant, reachable through the product page, the bulk editor, or the duties CSV under Settings, then Taxes and duties.

Permalink: https://blog.dugong.live/how-to-fix-missing-hs-codes-on-shopify-before-customs-holds-your-orders.html#faq-1

### What happens if a Shopify product has the wrong HS code?

The wrong rate gets charged in one direction or the other, and both directions cost you. Undercharge at checkout and the shortfall surfaces on the doorstep: Shopify's own documentation cautions that a missing country of origin or an incorrect HS code might result in additional duties being charged to the customer upon delivery, which reads as a scam text to the customer and becomes your refund. Overcharge and carts abandon: a community thread titled Shopify charging 100 percent duties on certain products to the US had collected 20 replies and over 1,200 views and was still active in August 2026, with one UK merchant measuring duties computed at 95 to 100 percent of price where the correct rate was 3.5 to 5 percent. At the border itself, a code that contradicts the product description gets the parcel flagged for manual review, reassessed, held, or returned to sender. And choosing a lower duty code on purpose stopped being a quiet trick: forum replies in mid 2026 point to a DOJ and DHS trade fraud task force and whistleblower incentives that reward reporting intentional misclassification. One more trap: Managed Markets assigns its own codes when activated and does not guarantee they match the ones you entered, so review what it assigned rather than assuming.

Permalink: https://blog.dugong.live/how-to-fix-missing-hs-codes-on-shopify-before-customs-holds-your-orders.html#faq-2

### Can AI classify HS codes for my Shopify products?

Yes, with a human on the low confidence tail. Classification is a reading task: the Harmonized System is a nomenclature of more than five thousand six digit subheadings maintained by the World Customs Organization, and picking the right one means reading a title, a description, and a materials list, which is exactly what a language model does in seconds and a person does slowly four hundred times. Shopify's product page already does a small version of this, type a description and it searches for codes, but only one product at a time. The working pattern: the model proposes a six digit code per variant with a confidence score and its reasoning, high confidence batches flow into the bulk editor or the duties CSV with an audit trail of what changed, low confidence items and the SKUs carrying real international revenue go to a human, and the genuinely ambiguous cases, the bag that lands on a different heading in leather than in canvas, go to a customs broker once and become a written rule afterward. What should never happen is silent auto publishing of low confidence codes, because a wrong code ships real bills to real doorsteps.

Permalink: https://blog.dugong.live/how-to-fix-missing-hs-codes-on-shopify-before-customs-holds-your-orders.html#faq-3

### How do I find which Shopify products are missing HS codes?

Export the duties CSV. Under Settings, then Taxes and duties, Shopify offers a dedicated CSV that will export your products with missing customs information, and that export is the closest thing the platform has to a coverage report: it only runs when you go and fetch it, so the check has to become a habit. The other audit runs once and quietly expires. During the duties at checkout setup there is a step that flags products with missing information, but it reviews the catalog you had that day, and the products you add next month answer to nobody. Nothing else enforces the fields: a product created tonight publishes, sells, and ships with both customs fields blank, and no theme displays them. A practical routine is to pull the CSV monthly, treat blanks as defects, and hold new products incomplete until their variants carry a code and an origin.

Permalink: https://blog.dugong.live/how-to-fix-missing-hs-codes-on-shopify-before-customs-holds-your-orders.html#faq-4

### Does Shopify charge a fee for calculating duties at checkout?

Yes. Collecting duties and import taxes at checkout costs 0.85 percent per order on Shopify Payments and 1.5 percent on other gateways, temporarily lowered to 0.5 percent since February 2025, and the fee lands on every order the calculation runs on, including the ones where it ran on blanks. That last clause is the trap. When a product is missing its HS code, Shopify estimates duties from the description and the product category instead, and when those are missing too the calculation still runs and the help center calls the result likely to be inaccurate, yet the fee is still charged. So a catalog full of blank customs fields pays full price for estimates the documentation itself hedges on, and the customer absorbs the difference on the doorstep. The fee is reasonable rent for accurate math. Filling in the codes, per variant, is what makes the math accurate.

Permalink: https://blog.dugong.live/how-to-fix-missing-hs-codes-on-shopify-before-customs-holds-your-orders.html#faq-5

---

Markdown rendition of https://blog.dugong.live/how-to-fix-missing-hs-codes-on-shopify-before-customs-holds-your-orders.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
