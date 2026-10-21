# How to bulk edit variant metafields on Shopify

> The definition takes four minutes. Filling it in across six thousand variants is where the week goes, because the product CSV leaves these fields out and the grid that can edit them is not in the product list.

- Canonical: https://blog.dugong.live/how-to-bulk-edit-variant-metafields-on-shopify.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-10-21
- Section: Research
- Word count: 2872
- Dispatch: Nº 133 · Research · 9 min read
- Full headline on page: How to bulk edit variant metafields *on Shopify*
- Keywords: bulk edit variant metafields shopify, shopify variant metafield csv, shopify variant metafields bulk editor, update variant metafield shopify api, metafieldsSet variant, shopify flow update product variant metafield, shopify variant metafield import, AI metafield automation
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

The definition took four minutes. Settings, then Custom data, then Variants, add a definition, single line text, call it material, save. Then the merchant opened the first product, typed the fabric into three variants, saved, and opened the second product.

There were several hundred more.

On 18 July 2026 that merchant asked Shopify's community the question in its plainest form. They were setting up variant metafields for material and care instructions across the catalog, [the native bulk editor did not expose them](https://community.shopify.com/t/how-do-you-bulk-edit-variant-metafields-native-bulk-editor-doesnt-expose-them/652699), editing product by product was far too slow for hundreds of variants, and was there a tool they were missing, or does everyone do this by hand?

The thread filled with app recommendations. Nobody from Shopify answered it. Three weeks later another merchant asked whether the original poster had got anywhere, and there is no reply to that either.


## The short answer

Shopify will not bulk edit variant metafields the way it bulk edits product ones. The product CSV carries product metafields and the documentation states plainly that variant metafields are not supported for product CSV import or export.

The grid that can edit them exists but sits behind a view that lists variants rather than products, needs a definition created at the variant level, and in practice handles simple text fields only.

Shopify Flow has an Update product variant metafield action, but it is offered with four inventory triggers only and the variant ID comes from the trigger, so Flow can hold the forward edge and cannot touch the variants already in your catalog.

That leaves the Admin API, where metafieldsSet takes 25 metafields per request and productVariantsBulkUpdate works one product at a time, with bulk operations and a JSONL file for real volume.

The fix is a workflow that reads the definition first, keys every row to a variant ID, refuses any SKU that matches two variants or none, derives the value from data the store already holds, backfills once and then holds the edge.

Start with the CSV, because that is where everyone starts. Shopify's [product CSV documentation](https://help.shopify.com/en/manual/products/import-export/using-csv) is clear that metafields belong in the file: once a product metafield is defined it is included in your product CSV exports, under a header in the form name (product.metafields.namespace.key), and the bare product.metafields.namespace.key works too if you prefer it without the name.

Then comes the sentence that ends the conversation. Variant metafields are not supported for product CSV import or export. The page's own suggestion is to use the variant bulk editor and add metafield columns there instead.

Now go to the other official surface. On 3 October 2025 a developer asked the same thing in [Shopify's developer community](https://community.shopify.dev/t/how-to-bulk-edit-product-variant-metafields-in-shopify/23443): the default CSV import and export shows product metafield columns and no variant ones, and the bulk edit interface does the same. The answer, inside an hour, was that there is no view for bulk updating variant metafields directly, and that the options are the Admin API or a third party app.

One surface says use the grid. The other says the grid does not exist. Both are partly right, which is the most expensive kind of documentation there is.

## The grid is real. Finding it is the trick.

Shopify's [page on bulk editing metafields](https://help.shopify.com/en/manual/custom-data/metafields/bulk-edit-metafields) opens by saying you can bulk edit metafields for products, variants, collections and customers, and then documents exactly one of those four. The steps it gives are Products, select with the checkboxes, Edit products, Columns, then pick what you want from the Metafields section. Follow them and you get product metafields, because you are in a view that lists products.

Variants need a view that lists variants. The route merchants report is Products, then Inventory, tick the box at the top to select everything, Bulk edit, then Columns, and the variant metafield columns are in that list. Two things have to be true before they appear. The definition has to exist at the variant level, which is a separate definition under Settings, Custom data, Variants, not the product definition that looks identical in every other respect. And the type has to be one the grid can render, which in practice means a simple text field rather than a list, a reference or JSON.

The feature also has a history, which is worth knowing before you conclude you are doing it wrong. On 27 February 2025 a merchant reported that variant metafields [had vanished from bulk editing](https://community.shopify.com/t/cannot-see-variant-metafields-in-bulk-editing/397411). On 7 April another said they had built a custom app around bulk editing them and lost the capability. That evening the first merchant said it was back and that they had used it, suspecting a regression that had since been fixed. The next morning a third merchant could still see product metafields only. In July 2026, on that same thread, somebody asked whether the Inventory route works at all, and said they were still editing hundreds of variants one by one.

The one limitation Shopify does document on the bulk editing page is a browser note: Microsoft Edge can produce errors when you bulk edit metafields because of a limited URL length, with Chrome, Firefox or Safari suggested instead. Useful to know at row four hundred of a grid that has just failed to save.

## A grid is for typing. The work is deriving.

Suppose the grid behaves. It solves exactly one shape of problem, which is the same literal value typed into many cells. Almost nothing that creates this work has that shape.

Care instructions are keyed to fabric, so forty fabrics decide six thousand values. Country of origin is keyed to the supplier, which lives in a file somebody emails you. A size chart is keyed to the option value, so every small variant in a product line wants one block and every medium wants a different one. None of those are things you type. They are things you look up, and then write.

The clearest version of this came up on 17 September 2025. A store running a wholesale app saw only the wholesale price in B2B mode and wanted the retail price shown struck through beside it. The app reads that from a variant metafield, in a specific JSON shape, one per variant. The number was already in Shopify, sitting on the variant as its own price. The suggestions were to export, build the JSON with a spreadsheet formula and re-import, which is the route Shopify's CSV page says does not exist for variant metafields, or to buy a bulk editor with formula rules.

That is the pattern every time. The data exists, the field exists, and the only thing missing is something that will read one and write the other six thousand times without a person in the middle.

## Flow has the action and not the trigger

Shopify Flow has an action called [Update product variant metafield](https://help.shopify.com/en/manual/shopify-flow/reference/actions/update-product-variant-metafield), and it does what the name says: it adds a metafield to the product variant that triggered the workflow, or updates the one already there. The product ID and the product variant ID are set by default and documented as fields you cannot change, which tells you where the variant has to come from.

It comes from the trigger, and the action is offered with four of them: inventory quantity changed, product variant added, variant back in stock, and variant out of stock.

Read that list again. Every one is an inventory event. Flow will keep a metafield current on variants that sell, restock or get created from the day you switch it on, and that is genuinely useful, because it is the forward edge of the problem handled for free. What it has no trigger for is the variants you already have. The rows already sitting in your catalog are outside its reach however you arrange the conditions. Flow holds the edge. It cannot do the backfill.

## What the API will do, and what it costs you

The Admin API has three answers and they are three different shapes.

metafieldsSet creates and updates in one call and takes an ownerId, which can be a variant, so it does not care about products at all. Shopify's [metafield limits](https://shopify.dev/docs/apps/build/metafields/metafield-limits) page caps it at 25 metafields per request with a maximum payload of 10MB. Six thousand variants carrying three fields each is eighteen thousand metafields, which is 720 requests.

[productVariantsBulkUpdate](https://shopify.dev/docs/api/admin-graphql/latest/mutations/productVariantsBulkUpdate) is documented as updating multiple product variants for a single product in one operation, and the phrase for a single product is the one that sets your loop. Nine hundred products is nine hundred calls however you arrange the batches inside them.

For anything larger, Shopify's own answer is [bulk operations](https://shopify.dev/docs/apps/build/apis/graphql-admin/bulk-operations/imports): reserve an upload with stagedUploadsCreate, write a JSONL file where each line is one set of mutation variables, run bulkOperationRunMutation so the mutation executes once per line, then either subscribe to the bulk_operations/finish webhook or poll bulkOperation(id:), which replaced currentBulkOperation in API version 2026-01, and finally download the JSONL results file to find out which lines failed. One sibling limit is worth noting while you are on that page: metafieldsDelete takes 250 per request, a number that comes from the platform wide maximum input array size.

None of that is difficult. All of it is a project. Authentication, paging the variant list, mapping SKUs to GIDs, batching to 25, backing off when you get throttled, and a results file somebody actually has to open. Which is why every thread on this ends at an app, and why on 12 April 2026 a merchant with roughly six thousand variants [formally requested](https://community.shopify.com/t/feature-request-native-csv-import-support-for-variant-metafields/607347) that variant metafields be supported in the standard CSV import and export, rather than pay for an app or build against the Admin API. Ten replies, latest activity 11 September 2026, no Shopify staff in the thread.

## The failure that costs more than the typing

The best answer anyone gave on the July thread was not a tool. On 15 September 2026 a developer suggested keeping a source of truth sheet keyed by SKU or variant ID and validating that the keys match before applying anything, because the real risk is putting a valid metafield value on the wrong variant.

That is the right fear, and it is worth being precise about why. An empty metafield is visibly empty. You can count the blanks, filter for them, and ship the feature when the count reaches zero. A wrong value is not visible anywhere. The cotton care instruction on the polyester version renders on the product page, feeds the filter somebody created the definition for, goes out in the product feed, and reads as perfectly ordinary data. Nothing flags it. You find out when a customer does, or when the return arrives.

So key on the variant ID wherever you have it. Where you only have a SKU, treat the match as a question rather than a lookup: a SKU that hits two variants, or none, is not a row to write, it is a row to report. Shopify will let two variants [share a SKU](https://blog.dugong.live/how-to-fix-duplicate-skus-on-shopify.html) and will let a variant have no SKU at all, which is the quiet reason a careful import still lands on the wrong row.

## What this costs in an afternoon

Take the catalog from that thread. Six thousand variants, three fields each. In the grid, with the columns loaded and nothing breaking, four seconds a cell is a fair rate for somebody who already knows what to type. Eighteen thousand cells is twenty hours, and that is the typing alone, after the fabric lookup has told you what goes in each one.

Product by product, which is where that merchant actually was, nine hundred products at two minutes each is thirty hours. Then a new product line lands in March and a share of it happens again.

The expensive version is neither of those. It is the one where the work never happens, the fields stay blank, and the filter the definition was created for never ships. That is the usual ending, and it does not appear in any report you have.

## What the automation actually has to do

As a Dugong playbook, in plain prose:

```
# trigger
Variant created, variant
updated, source sheet changed,
plus a nightly sweep

# steps
1. Read the definition before
   writing a single value
2. Key every row to a variant ID,
   never to a product title
3. Refuse the write when a SKU
   matches two variants or none
4. Build the value from the data
   you already hold
5. Write in the batches the API
   accepts and log what landed
6. Backfill the catalog once, then
   hold the edge
7. Report what is still blank
   every morning
```

Step one is not bureaucracy. A metafield definition carries a type and its validations, and a value that does not match the type is rejected rather than quietly coerced, so the first thing worth knowing is whether the field you are filling is single line text, a list, a reference or JSON, and whether the definition sits on the variant or on the product. Half the cases reported as the bulk editor being broken are a product level definition being looked for in a variant view.

Steps two and three are the same instinct twice, and they are what make this safe enough to run unattended. A variant ID is unique. A SKU is a promise nobody enforces. If your source sheet only carries SKUs, the automation's job is not to do its best, it is to write the rows that match exactly once and hand you a short list of everything else.

Step four is the part no grid will ever do. The value usually exists somewhere in the store already, in the variant's own price, its option values, the product type, or a supplier file that arrives every Monday. Deriving it is a rule you describe once, not a value you type six thousand times.

Step five is the dull engineering that decides whether this finishes at all. Twenty five metafields per request, throttle responses that mean wait rather than fail, and a written record of which variant received which value, because the one thing worse than a blank catalog is an unverifiable one.

Step six is the ordering that keeps it cheap. A backfill is one large job you run once and check. The edge is a small job that runs forever, on new variants and on changed ones. If the four triggers Flow offers happen to cover your case, let Flow hold the edge for free and point the automation at the backfill.

The honest limits. A variant metafield is only worth filling if something reads it, so confirm your theme or your app actually does before you fill six thousand of them. The grid is still better than any automation for a quick correction to a dozen cells. And nothing here removes the hard part, which is deciding what the correct value for each variant is. Automation writes the answer. It does not know it.

## Why this is a workflow, not a feature request

Three facts have to meet, and Shopify keeps them in three places with nothing joining them. The definition knows the type and the validations. The variant knows its own identity, its price and its option values. The correct value lives in a sheet, in a supplier file, or in the store's own data one field over.

No single feature joins those. A CSV column that accepted variant metafields, which is the thing everybody is asking for and which Shopify should ship, would still leave somebody deriving eighteen thousand values in a spreadsheet and keying them by SKU. A better grid still needs a person typing into it. A new Flow trigger still needs the lookup. What closes this holds all three at once, which is a workflow, and it has the shape every quiet gap in a store has: the data exists, the field exists, and nothing stands between them.

## Do this before you close the laptop

Three checks, ten minutes, no code.

Open Settings, then Custom data, and look at whether the definition you have been fighting is listed under Variants or under Products. That single check explains a surprising share of the threads.

Export your products to CSV and read the header row. Every metafield column you find there is a product metafield. The fields you cannot find in that file are the ones this dispatch is about, and now you know why.

Then multiply variants by fields. If the number is over a few hundred, no afternoon exists that fixes it, and the question stops being whether to automate and becomes what to key on.

> **◆ READING** Two companion pieces if this one landed: [the price change you make one product at a time](https://blog.dugong.live/how-to-bulk-edit-product-prices-on-shopify.html), on the same gap in the pricing field, and [the image alt text no one writes](https://blog.dugong.live/how-to-add-alt-text-to-shopify-product-images-in-bulk.html), on the catalog field nobody ever fills.

If you sell on Shopify and have a version of this story, the fabric sheet, the six thousand size charts, the metafield an app needs in a shape nothing produces, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Can you bulk edit variant metafields on Shopify?

Yes, but not from the product list and not through the product CSV. Shopify's bulk editing metafields page says metafields can be bulk edited for products, variants, collections and customers, then documents only the product route: Products, select with the checkboxes, Edit products, Columns, and pick from the Metafields section. That route shows product metafields because it lists products. For variants you need a view that lists variants, which merchants reach through Products, then Inventory, selecting everything and clicking Bulk edit, then adding the variant metafield columns from Columns. Two conditions have to hold. The definition has to exist at the variant level under Settings, Custom data, Variants, which is a separate definition from the product one. And the type has to be simple enough for the grid, which in practice means a single line text field rather than a list, a reference or JSON. When it works it is a grid you type into, so it is good for the same value across many cells and no help at all when the value has to be derived per variant. The product CSV is not an alternative: Shopify's own documentation states that variant metafields are not supported for product CSV import or export.

Permalink: https://blog.dugong.live/how-to-bulk-edit-variant-metafields-on-shopify.html#faq-1

### Why don't variant metafields show up in the Shopify bulk editor?

Three reasons, in the order they usually turn out to be the cause. First, the definition is on the wrong owner. A product metafield and a variant metafield can carry the same name and namespace and are still separate definitions, and only one created under Settings, Custom data, Variants appears in a variant grid. Second, you are in a product view. The documented procedure starts from the Products list, which lists products, so the Columns control offers product metafields. Merchants who do get variant columns describe starting from the Inventory view instead, selecting everything and clicking Bulk edit. Third, the type: merchants report success with simple text fields and far less with lists, references and JSON. There is also precedent for the feature simply breaking. On 27 February 2025 merchants reported that variant metafields had disappeared from bulk editing, a developer said on 7 April that a custom app built around it had lost the capability, and that evening the original reporter said it was working again and suspected a regression that had been fixed, while another merchant the next day still saw product metafields only. If you have checked the owner, the view and the type, changing browser is a reasonable next step, because Shopify documents that Microsoft Edge can throw errors here due to a limited URL length.

Permalink: https://blog.dugong.live/how-to-bulk-edit-variant-metafields-on-shopify.html#faq-2

### Does the Shopify product CSV support variant metafields?

No. Product metafields are in the file: Shopify's CSV documentation says that once a product metafield is defined it is included in your product CSV exports, with a header in the form name (product.metafields.namespace.key), and that the bare product.metafields.namespace.key works as well. Variant metafields are excluded, and the documentation says so directly, that variant metafields are not supported for product CSV import or export, with a pointer to the variant bulk editor instead. This is the most commonly misunderstood fact in the area, partly because third party import apps do accept variant metafield columns, so a merchant who has used one reasonably assumes the format is native. On 12 April 2026 a merchant with roughly six thousand variants opened a formal feature request asking for variant metafields in the standard CSV import and export, explaining that they wanted per variant descriptions without paying for an app or building against the Admin API. It drew ten replies, mostly workarounds and tool recommendations, no response from Shopify staff, and its latest activity was 11 September 2026. Until that changes, a CSV route for variant metafields means a third party app implementing its own format, not Shopify's.

Permalink: https://blog.dugong.live/how-to-bulk-edit-variant-metafields-on-shopify.html#faq-3

### Can Shopify Flow update variant metafields in bulk?

Flow can keep them current and cannot backfill them. The action exists and is called Update product variant metafield. Shopify documents it as adding a metafield to the product variant that triggers the workflow, and notes that the product ID and product variant ID are set by default and cannot be changed. That is the constraint that matters, because it means the variant is whichever one the trigger handed over. The action is available only in workflows started by one of four triggers: inventory quantity changed, product variant added, variant back in stock, and variant out of stock. All four are inventory events. So Flow is excellent at the forward edge, where a new variant can get its country of origin the moment it is created and a variant that sells out can have a status field updated. It has no trigger that iterates the variants you already have, so a catalog of six thousand existing variants sits outside its reach regardless of how the conditions are arranged. The practical split is to let Flow handle everything from today onward, and to use something that can walk the whole catalog for the one time backfill.

Permalink: https://blog.dugong.live/how-to-bulk-edit-variant-metafields-on-shopify.html#faq-4

### How do you bulk update variant metafields with the Shopify API?

There are three routes and the right one depends on volume. metafieldsSet creates and updates in a single mutation and takes an ownerId, so a variant GID is all it needs; Shopify's metafield limits page caps it at 25 metafields per request with a maximum payload of 10MB. productVariantsBulkUpdate is documented as updating multiple product variants for a single product in one operation, so it batches by product, which makes a catalog of nine hundred products nine hundred calls. For large volumes Shopify's documented path is bulk operations: reserve an upload with stagedUploadsCreate, build a JSONL file where each line is one set of mutation variables, call bulkOperationRunMutation to run the mutation once per line, then either watch for the bulk_operations/finish webhook or poll bulkOperation(id:), which replaced currentBulkOperation in API version 2026-01, and download the JSONL results file when it completes. For deletions, metafieldsDelete accepts 250 per request, a figure that comes from the platform wide maximum input array size. The work that is not in the documentation is the surrounding part: resolving SKUs to variant GIDs, batching, retrying on throttle, and reading the results file to find out which rows failed.

Permalink: https://blog.dugong.live/how-to-bulk-edit-variant-metafields-on-shopify.html#faq-5

### Can AI bulk edit variant metafields on Shopify?

Yes, and it fits automation better than most catalog work, because the values are nearly always derived from data the store already holds rather than invented. An automation like Dugong reads the metafield definition first, so it knows the owner, the type and the validations before it writes anything. Then it keys every row to a variant ID rather than a product title, and refuses to write a row whose SKU matches two variants or none, handing those back as a short exceptions list instead of guessing. It builds the value from what you already have, which is the step a grid can never do: a care instruction from the fabric, a country of origin from the supplier file, a JSON retail price block from the variant's own price. It writes in the batches the API accepts, twenty five metafields a request, and logs which variant received which value. Then it backfills the catalog once and holds the edge, filling new and changed variants as they appear. The honest limits: the automation writes the answer, it does not know it, so the mapping from fabric to care instruction is still yours to state; nothing reads a variant metafield unless your theme or app is built to, so check that before you fill six thousand of them; and for a quick correction to a dozen cells the grid is still faster than describing a rule.

Permalink: https://blog.dugong.live/how-to-bulk-edit-variant-metafields-on-shopify.html#faq-6

---

## Read next

- [The meta description you write one at a time](https://blog.dugong.live/how-to-bulk-edit-meta-descriptions-on-shopify.html): Shopify bulk edits meta descriptions only by making them identical, so unique ones get written one at a time or left blank. The AI playbook that fixes it.
- [The image alt text no one writes](https://blog.dugong.live/how-to-add-alt-text-to-shopify-product-images-in-bulk.html): Shopify never writes image alt text and has no bulk way to add it, so it sits blank across your catalog. The AI playbook that reads each photo and writes it.
- [The SKU two products share](https://blog.dugong.live/how-to-fix-duplicate-skus-on-shopify.html): Shopify says SKUs must be unique, then lets two products share one and splits the stock. The AI playbook that finds every collision and fixes it.
