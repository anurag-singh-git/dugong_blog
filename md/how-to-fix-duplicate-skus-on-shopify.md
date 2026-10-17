# How to find and fix duplicate SKUs on Shopify before they break your inventory

> Shopify says SKUs must be unique, then lets two products share one and splits the stock. The AI playbook that finds every collision and fixes it.

- Canonical: https://blog.dugong.live/how-to-fix-duplicate-skus-on-shopify.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-09-17
- Section: Research
- Word count: 2500
- Dispatch: Nº 117 · Research · 10 min read
- Full headline on page: How to find and fix duplicate SKUs on Shopify *before they break your inventory*
- Keywords: shopify duplicate sku, duplicate skus shopify, shopify same sku two products, shopify inventory not syncing same sku, find duplicate skus shopify, shopify sku best practices, shopify sku conflict, AI catalog automation
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

The email arrives on a Tuesday at 4:12 pm, and the customer is being very polite about it. She ordered the midnight blue mug from your gift bundle page nine days ago. It has not shipped.

You open the order, open the product, and the variant reads 0 available. Then you search the admin for the mug and find it a second time, on its own product page, 14 in stock, selling quietly all week.

Same mug. Same shelf. Same characters typed into the SKU field. Two products, two inventory numbers, and nothing anywhere in Shopify that ever thought to mention they were the same thing.

## Shopify treats the SKU as a label, not a key

Here is the part that surprises people who assume the code means something to the platform. Inventory in Shopify does not live on the SKU. It lives on an inventory item, one per variant, and the SKU is a text field sitting next to it. Type the same string into two variants and you have not linked anything. You have created two separate stock counts wearing the same name tag.

Shopify's own documentation is clear about what you should do. SKUs within your Shopify admin must be unique, it says, and no two product variants should include the same SKU. It is equally clear about the consequence: duplicate SKUs can cause issues with third- party integrations and inventory tracking. And it tells you the platform is watching: if a duplicate SKU is detected, then a warning message displays.

That is the entire enforcement. A line of gray text near a field. It does not block the save. It does not block a CSV import. It does not block an app writing through the API. And it never goes back to look at the duplicates you made last March, because nothing in the admin ever does.

The warning also has a blind spot the documentation names itself. SKUs are case-sensitive, so ABC123 and abc123 are recognized as different SKUs. The same is true of a trailing space typed by someone in a hurry at 6 pm. Those pass every uniqueness check the platform runs, and then fail every match your warehouse, your feed, and your accountant try to make.

There is exactly one place Shopify draws a hard line: Shopify Fulfillment Network requires unique SKUs for each product variant. Everywhere else, duplicates are legal, invisible, and yours to find.

## The community record

The thread that defines this problem opened on August 7, 2019 and was still collecting replies in November 2022, twenty-odd posts across two pages. The title is the whole complaint: multiple products with the same SKU, not updating inventory in sync.

The answer never changed, and it never came from Shopify. It came from other merchants, in the flat tone of people who already went through it. Unfortunately Shopify doesn't keep in sync inventory for products that have the same SKU. One reply asked the question everybody in the thread was actually asking: I dont understand why they would even allow duplicate a product if you cant sync the inventory.

What filled the space where a staff answer would have been was the app store. Trunk at twenty-nine dollars a month. Bundles at fourteen. A five dollar app whose entire name is Duplicate SKU Sync. Sync Master GoGo on a pay-as-you-grow plan. One merchant read the thread, did the arithmetic on a small catalog, and went back to tracking it by hand.

Then, on May 24, 2024, a harder version of the same thread, and this one is worth reading twice, because it shows the problem is structural rather than merely missing. A merchant running a fulfillment service integration laid out the arithmetic. Shopify asks a fulfillment service for one available number per SKU. But Shopify subtracts a different committed quantity from each duplicate variant. So if two variants share a code and one of them has three units committed to open orders, there is no single number you can return that is correct for both variants at the same time. Not hard. Impossible.

His proposed fix was one sentence long: when duplicate SKUs point at the same location, deduct the committed amounts for all of them together, and treat committed units as reserved across the group. A follow-up post arrived on May 5, 2025. No staff reply in that thread either.

And the front door is still swinging. On September 15, 2026, two days before this dispatch, a developer filed a bug on the Shopify developer forum with a title that needs no elaboration: duplicating a variant duplicates the SKU, even when not selected. Even if you tell it to NOT duplicate the SKU, it does so. A related regression in the same report copies barcodes onto new variants added to an existing product. No staff reply yet on that one either.

> **◆ NOTE** The record, compressed: SKUs must be unique, says the documentation, and nothing enforces it. Products with the same SKU do not sync, asked August 2019, answered by other merchants and by app links, never by staff. One number per SKU against a different committed quantity per variant, asked May 2024, asked again May 2025, unanswered. Duplicating a variant copies the SKU when you told it not to, filed September 15, 2026, open. Every thread ends in the same place: a spreadsheet, or a subscription.

## Nobody types a duplicate SKU on purpose

Which is exactly why they accumulate. Every duplicate in a working catalog got there through a door the merchant was not watching.

The Duplicate button is the biggest one. You copy a product to make the holiday version, the bundle listing, the wholesale page, and the copy brings its codes along for the ride. The open bug means it can bring them even when you ask it not to.

CSV imports are the second. Shopify matches an import by handle, not by SKU, so a re-import under a different handle does not update the old product, it creates a second one carrying the same codes. Feed and merge files that already contain duplicates pass them straight through, and a custom [metafield](https://help.shopify.com/en/manual/custom-data/metafields) named SKU will collide with the real field during an import and manufacture duplicates on the way in.

Apps are the third, and this one catches good merchants doing sensible things. Membership and wholesale pricing apps routinely clone a product to offer tier pricing, and the clone carries the original SKU by design.

Then there are the two categories that are not mistakes at all. Bundles, multipacks, and kits, where the six- pack deliberately borrows the single unit's code because it draws from the same physical shelf. And blank SKUs, which are usually the largest duplicate group in any catalog over a thousand variants, because every system downstream that keys on SKU treats all of them as one enormous bucket.

This is why the common advice, find the duplicates and delete them, is wrong in a way that costs money. Some collisions are decisions. The work is not deletion. The work is telling them apart.

## What the split count costs

The first cost is the one that brought you here: overselling and phantom stock. The count splits at the moment the second listing is created, and from then on it drifts. One page sells out while the other keeps taking orders. A restock lands on one and not the other. A physical stock take reconciles to a number that is correct for the shelf and wrong for both product pages, which is the most demoralizing result a stock take can produce.

The second cost lives past your admin, in the systems that actually move boxes. Your 3PL, your shipping app, a barcode scanner, a warehouse system: none of them see your product pages. They see a code on a line. Two products, one code, and the pick becomes a guess.

Mature integrations know this and say so out loud. Cin7 Core used to refuse the import entirely: duplicate SKUs in Shopify would not be imported until the user changed the Shopify SKUs to unique values. It now accepts them behind a setting you have to switch on deliberately, and hands you the rules that come with it. Only make stock adjustments on the main product, because adjusting the kit product can cause incorrect stock numbers. Map Shopify locations one to one. That is what a serious system does with duplicate codes: it lets you have them, and it makes you declare what you meant.

The third cost is quieter and shows up in decisions. Sales by SKU adds two different products together and reports a number nobody questions. Channel feeds either collapse the rows or reject them, and the rejection email names an error, not a cause. Reorder points fire against half a shelf.

And the bill compounds, because a SKU accumulates history. A duplicate found in the week it was created is a two-minute rename. A duplicate found in year two has order lines, returns, purchase orders, supplier records, and a 3PL's own database attached to it, and every one of those is an argument against renaming anything. The cheapest moment to fix a collision is always the day it was made, which is the one day nobody is looking.

Which brings up the last cost, the one no merchant tracks: finding them. There is no duplicate SKU report in the Shopify admin. The standard method, still, is to export the product CSV, sort it by the SKU column in a spreadsheet, and read. The [bulk editor](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/bulk-editing) apps that do this for you run the same errand with a better interface: filter, export to a sheet, edit, upload the sheet back. It works on the day you run it. Nothing is watching on the days you do not.

> Shopify treats the SKU as a label you wrote on a box. Every system downstream treats it as the *name* of the box.

## What the automation actually has to do

As a Dugong playbook, in plain prose:

```
# trigger
Every morning, plus every
product or variant saved
during the day

# steps
1. Scan every variant in the
   catalog and group them
   by SKU
2. Normalize first: fold
   case, strip whitespace,
   then compare
3. Separate intent from
   accident: bundle groups
   stay, clones do not
4. Sync the deliberate ones:
   one shelf, one number,
   many listings
5. Rename the accidents on
   our code format, history
   shown, human approves
6. Guard the front door: new
   collisions flagged within
   the hour
7. Report weekly: opened,
   closed, prevented, and
   what each one cost
```

Step two is the one most spreadsheet passes skip, and it is where a surprising share of real collisions hide. Fold case, strip leading and trailing whitespace, and compare the cleaned codes. A pair like MUG-MDNT-01 and mug-mdnt-01 will never sort next to each other in a raw export, and it will break every downstream match exactly as hard as an exact duplicate does.

Step three is the judgment call, and it is the reason this cannot be a button. A bundle sharing its component's code and a wholesale clone carrying a copied code look identical in a spreadsheet. The difference exists only in what you meant, so the automation has to hold your rules: collisions inside a bundle group are expected and stay in sync, everything else is a defect and gets renamed on our format, the customer-facing listing is canonical when two products disagree.

Step five is where the honest limit sits. Renaming a SKU that already carries order history is not a small edit, and an automation that quietly rewrites codes on products with two years of purchase orders behind them has replaced one mess with a more confident mess. The right behavior is to propose, show the attached history, and wait for a human to nod. New collisions, caught within minutes of the save, need no such ceremony, which is the whole argument for step six.

## Why this is a compiler problem, not an app problem

The app store covers exactly half of this, twice. Sync apps keep duplicate SKUs moving in step, which is genuinely useful, and they will never tell you which of those duplicates should not exist in the first place. Bulk editors find collisions and hand you a spreadsheet, which is also useful, and they will never decide anything. Between them sits the actual work, which is a judgment about your own catalog that neither tool is built to hold.

[Shopify Flow](https://help.shopify.com/en/manual/shopify-flow) cannot bridge it either, and the reason is worth naming precisely, because it is the same shape as the other walls in this series. Flow reacts to one product at a time. It has no way to ask the question that matters here, which is what else in this catalog carries this code. A trigger that fires on a product update can tell you a product changed. It cannot compare that product to the other eleven thousand.

What the job actually needs is a scan the platform will not run, a comparison Flow cannot express, and a set of rules that only exist in the merchant's head. That is a description, not a diagram. You write it in a paragraph and a compiler turns it into the loop that runs every morning.

## The workflow worth building this week

Every morning, read every variant in the catalog and group them by SKU with case and spacing ignored. If two or more variants share a code, check my bundle list first: if they are all in one bundle group, keep their stock in step and say nothing. If they are not, open a collision, show me both products with their order history, and propose a new code for the one that is not the customer-facing listing, following our format. List every variant with a blank SKU as its own problem. Then watch the catalog all day, and if a new or edited variant lands on a code that already exists, tell me within the hour, while it is still a rename. Once a week, show me what opened, what closed, and what the open ones are holding up.

That is the whole paragraph. It names a scan Shopify does not offer, a comparison Flow cannot make, and three judgments that belong to the merchant. The compiler turns it into a workflow, and the store stops discovering its duplicates through a polite email about a mug.

> **◆ READING** Two companion pieces if this one landed: [the bundle sale that never touches your component stock](https://blog.dugong.live/how-to-sync-bundle-inventory-with-component-stock-on-shopify.html), on the collisions you make on purpose, and [the overselling problem no one automates](https://blog.dugong.live/how-to-prevent-overselling-on-shopify-across-channels.html), on what a split count does once it reaches a second [sales channel](https://help.shopify.com/en/manual/online-sales-channels).

If you are a Shopify merchant with a duplicate SKU story, the bundle page that sold air for a month, the 3PL that picked the wrong box, the rename you could not do because of the order history, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Does Shopify allow duplicate SKUs?

Yes, and that is the root of the problem. Shopify's own documentation says that SKUs within your Shopify admin must be unique and that no two product variants should include the same SKU, but nothing in the platform enforces it. Inventory does not live on the SKU: it lives on an inventory item, one per variant, and the SKU is a text field sitting next to it. Type the same code into two variants and you have not linked them, you have created two separate stock counts wearing the same name tag. The admin displays a warning message when it detects a duplicate, and that warning does not stop the save, does not stop a CSV import, does not stop an app writing through the API, and never goes back to look at the duplicates already sitting in your catalog. The one place Shopify draws a hard line is Shopify Fulfillment Network, which requires unique SKUs for each product variant. Everywhere else, duplicates are legal, invisible, and yours to find.

Permalink: https://blog.dugong.live/how-to-fix-duplicate-skus-on-shopify.html#faq-1

### Why is my Shopify inventory not syncing between two products with the same SKU?

Because Shopify never promised it would. Merchants have been asking since a community thread opened on August 7, 2019 that was still collecting replies in November 2022, and the answer in it never changed: Shopify does not keep inventory in sync for products that have the same SKU. One merchant put the frustration plainly, asking why the platform would even allow duplicating a product if you cannot sync the inventory. No Shopify staff answered, and the thread filled with app pitches instead, at five, fourteen, and twenty-nine dollars a month. A second thread from May 24, 2024 showed the problem is structural rather than simply missing: Shopify asks a fulfillment service for one available number per SKU, but it subtracts a different committed quantity from each duplicate variant, so no single number can be correct for both variants at the same time. The merchant's suggested fix, deducting the committed amounts for all duplicate SKUs together when they point at the same location, was raised again in May 2025 and has not been answered.

Permalink: https://blog.dugong.live/how-to-fix-duplicate-skus-on-shopify.html#faq-2

### How do I find duplicate SKUs in my Shopify store?

There is no duplicate SKU report anywhere in the Shopify admin, so the standard method is manual: export your products to CSV, sort by the SKU column in a spreadsheet, and read down the list looking for repeats. Bulk editor apps package the same errand with a filter and a re-upload step. Both work on the day you run them, and neither is watching the next day. Two things the spreadsheet pass usually misses: SKUs are case-sensitive in Shopify, so ABC123 and abc123 are treated as different codes and will not sort next to each other unless you normalize the column first, and the same is true of a trailing space. Blank SKUs are the other blind spot, because every system downstream treats them as a single bucket. A scan worth trusting folds case, strips whitespace, groups by the cleaned code, reports blanks as their own collision group, and runs on a schedule rather than on the morning you remember.

Permalink: https://blog.dugong.live/how-to-fix-duplicate-skus-on-shopify.html#faq-3

### Should bundles and multipacks share the same SKU as the single product?

Sometimes, which is exactly why blanket advice to find and delete duplicate SKUs is wrong in a way that costs money. A six-pack that draws down the same physical shelf as the single unit is a deliberate collision, and merchants use it so stock stays allocated from one place. What is not deliberate is the seasonal copy of a product, the wholesale clone an app created for tier pricing, or the second listing made by a re-import under a new handle. Those two cases look identical in a spreadsheet, because the difference lives only in what you intended. Mature integrations handle it by making you declare that intent: Cin7 Core used to refuse to import duplicate SKUs at all until merchants made them unique, and now imports them behind a setting, with the rule that stock adjustments should be made only on the main product because adjusting the kit product can cause incorrect stock numbers. The right workflow does the same thing inside your own store: label the intentional collisions, keep them in sync, and treat everything else as a defect.

Permalink: https://blog.dugong.live/how-to-fix-duplicate-skus-on-shopify.html#faq-4

### Can AI find and fix duplicate SKUs on my Shopify store?

Yes, and it fits because the job is two parts detection and one part judgment. Detection is mechanical: read the whole catalog, fold case and whitespace, group by code, surface every collision including the blank ones. Shopify Flow cannot do this, because Flow reacts to one product at a time and has no way to ask what else in the catalog carries the same code. Judgment is where your rules live, in plain language: bundle groups that share a component code are expected and stay in sync, wholesale clones are defects and get renamed on our format, the customer-facing listing wins when two products disagree. An automation like Dugong runs the scan on a schedule, checks every new or edited variant within minutes of the save so a collision is caught while it is still a rename, applies your code format to the accidents, keeps the intentional groups in step, and reports weekly. The honest limits: it will not decide for you which of two listings is the real product, and renaming a code that already carries order lines, purchase orders, and 3PL records is a decision that needs your sign-off, so the workflow proposes and you approve.

Permalink: https://blog.dugong.live/how-to-fix-duplicate-skus-on-shopify.html#faq-5

---

Markdown rendition of https://blog.dugong.live/how-to-fix-duplicate-skus-on-shopify.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
