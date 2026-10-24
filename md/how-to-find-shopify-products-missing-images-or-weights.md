# How to find Shopify products missing images or weights

> Nothing in the Shopify admin will tell you which products went live without a photo. There is no filter for it, no column that sorts it, and the storefront is where you find out.

- Canonical: https://blog.dugong.live/how-to-find-shopify-products-missing-images-or-weights.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-10-24
- Section: Research
- Word count: 3258
- Dispatch: Nº 134 · Research · 12 min read
- Full headline on page: How to find Shopify products missing *images or weights*
- Keywords: shopify products missing images, find products without images shopify, shopify product missing weight, shopify flow check product has image, shopify product data quality, shopify no image filter, shopify missing barcode, AI catalog audit shopify
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

A merchant in menswear went looking for a filter. He had the products list open, the filter menu pulled down, and he wanted one thing out of it: show me the products with no photo. He wrote down what Shopify offered instead. Vendor. Tag. Status. Sales channel. Market. Product type. Collection. Publishing error. Gift card. Nothing about an image.

He asked the community on 26 April 2023 whether [a no-image filter could be added](https://community.shopify.com/t/how-can-i-add-a-no-image-filter-to-my-products/211441). Nobody from Shopify replied, and he never posted on the thread again.

Two years and nine months later a second merchant found it and added to it. He had solved the forward half, with a flow that tags any new product `missing_image` when it arrives without one. What he could not do was look backwards. Everything created before that flow existed was still out there, and he had gone hunting on GitHub for a script to export the whole catalog so he could find it in a spreadsheet.

That is the state of the art for a question that sounds like it should be a dropdown.

## The short answer

The Shopify admin cannot filter on a field being absent. There are sixteen filters on the products list and none of them concerns an image, a weight or a barcode, and Shopify's documentation says the search bar and the filters do not support searching for products that are missing an attribute.

The product CSV will find a missing image and a missing barcode. It cannot find a missing weight, because a blank weight imports as zero and exports as zero, so nobody-weighed-this and this-weighs-nothing come out of the file looking identical.

Shopify Flow can guard the front door. It has a Product created trigger and a Product status updated trigger, and no Product updated trigger, so nothing fires when somebody opens a live product and deletes its last image.

The condition most people write first reports clean on exactly the products they built it to catch. A test written against each item in a list never runs when the list is empty, so the check needs the None operator rather than a question about a blank URL.

And an image that exists is not an image that will display. Shopify processes media asynchronously, so a product can hold media whose status is FAILED while any count-based check calls it fine.

What works is a gate plus a sweep: write down what finished means, hold anything short of it in draft, walk the back catalog once because no trigger covers it, re-check after the processing delay, and mail one short list every morning.

## There is no filter for this, and Shopify says so

Shopify's page on [searching for products and filtering your product list](https://help.shopify.com/en/manual/products/searching-filtering) names sixteen filters: Vendors, Tag, Statuses, Categories, Sales channel, Region catalog, B2B catalog, Company location catalog, Retail catalog, Unassigned catalog, Types, Collection, Publishing error, Gift card, Combined listings and Metafields.

Read that list for its shape rather than its contents. Every filter on it selects products by a value they have. Not one selects products by a value they lack. The nearest miss is Publishing error, which tells you a sales channel has already rejected the product, which is the symptom arriving after the fact rather than the cause you could have caught at the keyboard.

The documentation is straight with you, which is more than most documentation manages. The same page says the search bar and filters do not support searching for products that are missing a specific attribute, and for the one case it addresses, products with no tags, its advice is to export the product list and read the column. Keep that sentence: it is the end of the first three hours most people spend here. There is no clever query syntax waiting to be found, and the export is not a workaround for a missing feature. It is the documented answer.

## The CSV answers three questions and loses the fourth

So export. The CSV is a decent instrument right up to the point where it is not, and it helps to know in advance which point that is.

Images come out clean. A product with no image has an empty product image URL cell, and finding those is a sort. Barcodes come out clean too: [Shopify's CSV reference](https://help.shopify.com/en/manual/products/import-export/using-csv) describes that column as all of the barcodes for a product or variant, up to a maximum of twenty, and a blank cell is a blank cell. Worth knowing for when you refill them, a barcode supplied with no type is imported as a Custom barcode.

Weight does not come out clean, and this is the part nobody writes down. The same reference describes the weight column as the weight of the product or variant expressed in grams, and then states that the default value is zero if no value is entered. The file has no way to say unset. A pair of boots nobody weighed exports as zero. So does a gift card, and so does a digital download. They are the same row.

Which is why weight problems get found by customers rather than by audits. A zero is a legal value. It passes every import without a warning and quietly produces a shipping rate of whatever your cheapest band happens to be. Merchants meet it from the far end: a sticker and a winter coat costing the same to post, a free shipping threshold firing on orders it should not. The threads are always titled after the rates. The cause is a column that cannot tell absent from zero.

The Admin API can tell them apart, which is the useful half. An inventory item always carries a [measurement object](https://shopify.dev/docs/api/admin-graphql/latest/objects/InventoryItemMeasurement) and the weight inside it is nullable, so null means nobody has said and zero means somebody has. The spreadsheet cannot carry that distinction. If weight matters in your store the CSV is the wrong tool, and you will keep reaching for it because the CSV is the tool the documentation pointed you at. It is the same gap that leaves [variant metafields out of the file](https://blog.dugong.live/how-to-bulk-edit-variant-metafields-on-shopify.html) altogether. The format was built to move a catalog, not to audit one.

## Flow will guard the door it has a trigger for

Shopify Flow is the right instinct and a partial answer. The product [triggers](https://help.shopify.com/en/manual/shopify-flow/reference/triggers) are Product created, Product deleted, Product status updated, Product variant added, Product variant deleted, Product variant back in stock, Product variant out of stock, and Product variant inventory quantity changed.

Read that list the way you read the filter list. There is no Product updated.

So a product arrives with no photo and Flow catches it. A product is switched from draft to active with no photo and Flow catches that too. Somebody opens a live product, deletes the one image on it, saves, and nothing happens at all. The catalog is now wrong and no trigger fired.

[Product created](https://help.shopify.com/en/manual/shopify-flow/reference/triggers/product-added-to-store) is narrower than it sounds, too. Shopify documents it as starting when a user in your organization or a third-party app adds a new product, in the admin or through the API, whether or not it goes to the Online Store sales channel, and then says it applies only to new products and does not start when a new variant is added to an existing product. So the new colorway on last season's jacket, added as a variant with no variant image, sits outside it. None of which makes Flow the wrong tool. It makes Flow the gate rather than the audit.

## Why your first attempt misses the products you were looking for

This is the most useful paragraph here and it comes from no documentation at all. It comes from two merchants, three months apart, finding the same trapdoor.

In January 2024 a merchant with over two thousand items, many never photographed and some duplicated by staff without images, set out to build the check. The logic was simple in his head: if the product has no image, unpublish it. He wrote the condition the obvious way, as a test on the image URL, and [asked which field to use](https://community.shopify.com/t/i-want-to-write-a-flow-that-checks-to-see-if-a-product-has-an-image-associated-with-it/285582), because the Product object offers featuredImage, featuredMedia, images and media and the builder gives no hint. He was told to use Product, then Images, then URL, and to leave Media alone. It worked. Three months later another merchant built the same flow and it did not run. His test product had no image at all, which was the entire point of the test, and the workflow stayed silent.

The reason will cost you an afternoon if you meet it alone. A condition written against a list runs once for each item in the list. If the list is empty the per-item test never runs, so a check for the image URL being empty finds nothing on a product with no images, because there is no image whose URL could be empty. What does run on an empty list is the Any, All or None operator. The working version uses None, phrased as none of the product's images existing, with the two action paths swapped so the empty case is the one that acts.

So the naive check does not merely under-report. It reports clean on precisely the products you built it to find, which is the worst failure a monitoring workflow can have, because it looks like good news. If you have one of these running today, test it against a product with zero images rather than a product with one bad image. Those are different tests and only one of them is the one you care about.

One more thing from that thread, because advice ages. The guidance that worked points at the images field and says to avoid media. On the current [Admin API Product object](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product), images and featuredImage are both marked deprecated and media is the live field, documented as the media associated with the product, where valid media are images, 3D models and videos. The Flow condition still works. It is not what you would write from the schema today, and anything you build against the API should go through media.

## An image that exists is not an image that displays

Now the failure that survives a correct presence check, which is the one that catches careful people.

Shopify does not finish processing an image at the moment you attach it. Every media object carries a status and [the enum has four values](https://shopify.dev/docs/api/admin-graphql/latest/enums/MediaStatus): UPLOADED, meaning the media has been uploaded but not yet processed; PROCESSING, meaning it is being processed; READY, meaning it is ready to be displayed; and FAILED, meaning media processing has failed. Media errors and media warnings sit alongside it.

Put that beside a check that counts images and the hole is obvious. A product whose single image has the status FAILED has an image. It has a row in the media connection, an id, a line in the CSV export. It shows a customer nothing. A count passes it and the storefront is where you find out.

Not a hypothetical. In August 2026 an agency-side thread went looking for [how to verify product imagery after a bulk catalog change](https://community.shopify.com/t/how-do-shopify-agencies-verify-product-images-after-bulk-catalog-changes/664741), on the stated grounds that image problems are harder to detect than text problems. The replies converge on one answer. Compare the intended state against the live state rather than before against after, recording ids, image references, positions, alt text and variant assignments and then querying them again. Treat a successful write as evidence the operation finished and nothing more. And, from the last reply, wait before verifying, because image processing is asynchronous: run the comparison at write time and again after a delay, and trust only the delayed result.

That is the discipline, written down by people who got it wrong first, and it is not new. In September 2021 a developer pushing tens of thousands of products into Shopify nightly asked [for an API way to list the ones with no images](https://community.shopify.com/t/admin-api-rest-or-graphql-list-products-variants-with-no-images/68735) so they could be fixed before customers noticed. He answered himself the same afternoon: check the response after creating each product, and if an expected image is missing, set the product to draft and send an email. The accepted reply a week later added that you should check whether the media had actually been processed. Five years on that is still the shape of the answer, and still something each merchant assembles alone.

## What this costs on an ordinary Tuesday

Take a store with four thousand products and three people who add things. Finding the gaps by hand means exporting the catalog and sorting four columns. Call it forty minutes. You will do it once, feel good about it, and not do it again next month, which is how every catalog audit in recorded history has gone.

The cost of not doing it never arrives as a task. A product with no image converts at a rate you will never measure, because nobody emails to say they did not buy the thing they could not see. A product with no weight ships at the wrong postage until somebody in the warehouse notices the margin. A product with no barcode fails a channel feed, which turns up days later as a disapproval in an ads dashboard and gets handled by whoever runs ads rather than whoever created the product.

That is the real shape of this one. The damage is spread across people who did not cause it and arrives too late to connect back to the row that did. Which is exactly the kind of problem worth automating, and exactly the kind nobody puts on a sprint board.

## What the automation actually has to do

As a Dugong playbook, in plain prose:

```
# trigger
Product created, variant added,
status changed, supplier feed
landed, plus a nightly sweep

# steps
1. Write down what finished
   means in your store
2. Check media status, not
   whether media exists
3. Treat a zero weight as
   unknown, not as zero
4. Hold the publish instead of
   reporting the damage
5. Sweep the back catalog once,
   because no trigger covers it
6. Re-check after the delay,
   because processing is asynchronous
7. Send one list every morning,
   worst first
```

Step one is the one people skip and the one that decides whether the rest is useful. Finished is not a universal standard. A print shop needs an image, a weight and a description. A download shop would be wrong to require a weight. A store feeding a shopping channel needs a barcode on branded items and does not care on the ones it makes itself. Write the rule for your store, in a sentence, before anybody writes a query.

Steps two and three are the two checks everyone gets slightly wrong. Ask the media for its status rather than asking the product for a count, because one image with the status FAILED is a product with no image that happens to own a file. And treat a zero weight as a question rather than an answer: keep a short list of the product types that are genuinely weightless, usually one or two, and treat a zero anywhere else as unknown until a human says otherwise. That single rule turns the unanswerable CSV column into something you can act on.

Step four is where automation earns the difference from reporting. A report tells you about the damage, a gate prevents it, and holding anything unfinished in draft with a note about why is what that 2021 developer arrived at by himself. It beats a daily email because the broken product never reaches a customer.

Steps five and six are the two things Shopify will not do for you. There is no trigger for your existing catalog, so the back catalog is one large job that runs once, reports what it found and never needs to run again if the gate holds. And the sweep needs two passes, with the second one sending the mail, because the first pass is full of images that were merely still being processed.

Step seven decides whether anybody acts. A list of eight hundred incomplete products gets archived. A list of the nine added yesterday that are missing something gets fixed before lunch. Sort by what is costing money, which usually means active products with traffic, and send the short one.

The honest limits. The automation cannot weigh your boots or photograph your sofa, only refuse to let an unweighed, unphotographed product sell. For a catalog of forty products the spreadsheet is faster than describing a rule, and you should use the spreadsheet. And a gate will annoy somebody in week one, because sooner or later a product is wanted live now and finished later, so decide in advance who may override it.

## Why this is a workflow and not a checklist

A checklist is a good answer when the work is rare. This work is not rare. Every product added, every variant added, every supplier feed that lands overnight, every bulk edit somebody runs at four in the afternoon is another chance for the catalog to drift away from finished. A rule enforced by a person who remembers is a rule that holds until the week gets busy.

And it has been asked long enough to stop waiting. The filter request is from April 2023 with no Shopify answer on it. The API question is from September 2021 and was answered by the person who asked it. The agency thread from August 2026 ends on good practice rather than a fix. Three forums, five years, the same hole.

With Dugong you describe this one in a sentence. A product is finished when it has at least one image whose processing succeeded, a weight somebody has actually entered, a barcode if the channel needs one, and a description; hold anything unfinished in draft and tell me what is holding it; sweep the whole catalog on the first of the month. That is the specification. Everything after it is plumbing, and plumbing is what automation is for.

## Do this before you close the laptop

Three checks, ten minutes, no code.

Export your products to CSV and sort by the product image URL column. The number at the top of that sort is the number you did not know, and the surprise is the useful part.

Sort the same file by weight and count the zeros. Everything in that count is either a deliberately weightless product or a product nobody has weighed, and the file cannot tell you which. If the number is bigger than your list of genuinely weightless products, you have found your shipping rate problem.

Then, if you already have a flow checking for images, open it and point it at a product with no images at all. If it stays quiet, it has been sending you good news about a catalog it never looked at.

> **◆ READING** Two companion pieces if this one landed: [the image alt text no one writes](https://blog.dugong.live/how-to-add-alt-text-to-shopify-product-images-in-bulk.html), on the catalog field Shopify stores and never fills, and [the product descriptions you'll never finish writing](https://blog.dugong.live/how-to-generate-shopify-product-descriptions-with-ai.html), on the other half of a product page nobody gets to the end of.

If you sell on Shopify and have a version of this story, the product that sold for a month with no photo, the sticker that shipped at coat postage, the feed that rejected four hundred rows on a Friday, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### How do you find Shopify products with no image?

You export the catalog, because the admin cannot do it. Shopify's page on searching for products and filtering the product list offers sixteen filters, which are Vendors, Tag, Statuses, Categories, Sales channel, Region catalog, B2B catalog, Company location catalog, Retail catalog, Unassigned catalog, Types, Collection, Publishing error, Gift card, Combined listings and Metafields, and not one of them concerns an image. The same page states that the search bar and the filters do not support searching for products that are missing a specific attribute, and for products with no tags it recommends exporting the product list and reading the column in a spreadsheet. The same method works for images. Export the products, sort by the product image URL column, and everything with a blank cell is a product with no image. That finds the gap and does nothing to stop it happening again, which is why most merchants end up with both: an export they run occasionally, and a Shopify Flow workflow that tags or unpublishes new products arriving without a photo. The export answers today. The flow answers tomorrow. Neither on its own covers both.

Permalink: https://blog.dugong.live/how-to-find-shopify-products-missing-images-or-weights.html#faq-1

### Can Shopify Flow check whether a product has an image?

Yes, and the field to use is not the obvious one. In the flow builder the condition people land on is Product, then Images, then URL, tested for existing or for being non-empty, which merchants on the Shopify community confirmed working in January 2024 and again in April 2024. The Product object also exposes featuredImage, featuredMedia and media, and the advice on that thread was to leave Media alone for this purpose. Two cautions. First, that advice is now at odds with the API: on the current Admin API Product object both images and featuredImage are marked deprecated, and media is the live field, described as the media associated with the product, where valid media are images, 3D models and videos. The Flow condition still works; anything you build against the API should use media. Second, the obvious phrasing of the condition fails on exactly the products you want. A test on each item in a list does not run when the list is empty, so you need the None operator rather than a check for a blank URL. That is the single most common reason one of these workflows reports a clean catalog.

Permalink: https://blog.dugong.live/how-to-find-shopify-products-missing-images-or-weights.html#faq-2

### Why does my Shopify Flow miss products that have no image at all?

Because your condition is written against each image, and those products have no images for it to run against. This is the trapdoor in the whole area. A Flow condition on a list evaluates once per item in the list, so a test like the image URL is empty produces no result on a product with zero images, since there is no image whose URL could be checked. The workflow then takes the path for a passing product and tells you nothing is wrong. What does evaluate on an empty list is the Any, All or None operator. The fix, which a merchant reported working in April 2024 after exactly this symptom, is to phrase the condition as None, meaning none of the product's images exist, and to swap the action branches so the empty case is the one that acts. There is a practical lesson underneath the mechanics. Test any catalog-completeness workflow against a product with nothing in the field rather than a product with something wrong in the field. A monitoring workflow that is silent for the wrong reason is worse than no workflow, because you stop looking.

Permalink: https://blog.dugong.live/how-to-find-shopify-products-missing-images-or-weights.html#faq-3

### How do you find Shopify products missing a weight?

Not from the CSV, which is the problem. Shopify's CSV reference describes the weight column as the weight of the product or variant expressed in grams, and then says the default value is zero if no value is entered. So the export has no way to express unset. A product nobody weighed exports as zero, and so does a gift card, a digital download or anything else that genuinely weighs nothing. They are the same row and no sort separates them. The Admin API can separate them, because an inventory item always carries a measurement object and the weight inside that object is nullable, so a null weight means nobody has entered one and a zero weight means somebody has. That distinction is the whole answer. In practice the workable approach is to hold a short list of the product types in your store that are legitimately weightless, then treat a zero weight anywhere else as unknown rather than as a value. It is also the check worth running first, because a missing weight does not look broken anywhere in the admin. It surfaces as a shipping rate that is wrong in a way nobody can explain.

Permalink: https://blog.dugong.live/how-to-find-shopify-products-missing-images-or-weights.html#faq-4

### Can you stop a Shopify product from going live if it is incomplete?

Yes, and this is the version worth building. Shopify Flow has a Product created trigger, which Shopify documents as starting when a user in your organization or a third-party app adds a new product, in the admin or through the API, whether or not it is added to the Online Store sales channel. It also has Product status updated. Between them you can catch a product as it arrives and as it is switched to active, check the fields you care about, and set it back to draft with a note about what is missing. A developer running tens of thousands of products into Shopify nightly described doing precisely this in 2021: check the response, and if an expected image is missing, set the product to draft and send an email. Two gaps to plan for. There is no Product updated trigger, so nothing fires when somebody edits a live product and removes its last image, which means you still need a periodic sweep. And Product created does not fire when a new variant is added to an existing product, so a new colorway with no variant image gets past the gate even on a store where the gate works.

Permalink: https://blog.dugong.live/how-to-find-shopify-products-missing-images-or-weights.html#faq-5

### Can AI audit Shopify product data for missing images and fields?

Yes, and it suits automation better than most catalog work, because every judgment involved is a rule rather than an opinion. An automation like Dugong starts from a definition of finished that you write once in a sentence, since finished differs by store: a print shop needs an image, a weight and a description, a download shop would be wrong to require a weight, and a store feeding a shopping channel needs a barcode on branded items only. It then checks media status rather than counting media, so an image whose processing failed is treated as a missing image instead of a present one. It treats a zero weight as unknown unless the product type is on your weightless list. It holds anything unfinished in draft and says what is holding it, rather than mailing you a report about a product a customer can already see. It sweeps the existing catalog once, because no Shopify trigger covers products that already exist. It re-checks after a delay, because image processing is asynchronous and a verification pass run immediately is measuring the wrong moment. And it mails one short list each morning, worst first, because a list of nine products gets fixed and a list of eight hundred gets archived. The limits are honest ones: it cannot weigh your boots or photograph your sofa, a forty-product catalog is faster to fix in a spreadsheet, and somebody has to decide who may override the gate.

Permalink: https://blog.dugong.live/how-to-find-shopify-products-missing-images-or-weights.html#faq-6

---

## Read next

- [The image alt text no one writes](https://blog.dugong.live/how-to-add-alt-text-to-shopify-product-images-in-bulk.html): Shopify stores an alt text on every image but never writes one and has no bulk way to add it, so it sits blank across the catalog. The AI playbook that reads each photo and writes it.
- [The product descriptions you'll never finish writing](https://blog.dugong.live/how-to-generate-shopify-product-descriptions-with-ai.html): Shopify Magic writes one product at a time from keywords you type, so the catalog never gets done. The AI playbook that writes it whole, in one voice.
- [The deleted product that 404s your customers](https://blog.dugong.live/how-to-fix-404-errors-from-deleted-products-on-shopify.html): Delete a product on Shopify and its old URL just 404s, with no redirect. The AI playbook that catches every dead link and sends it to the right live page.
