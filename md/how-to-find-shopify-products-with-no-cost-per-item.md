# How to find Shopify products with no cost per item

> Your profit report is not wrong, it is incomplete. Orders for variants with no cost recorded are left out of it entirely, and Shopify gives you no way to search for them.

- Canonical: https://blog.dugong.live/how-to-find-shopify-products-with-no-cost-per-item.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-11-02
- Section: Research
- Word count: 2786
- Dispatch: Nº 138 · Research · 10 min read
- Full headline on page: How to find Shopify products with no cost per item *before your profit report lies*
- Keywords: shopify cost per item missing, shopify cogs, shopify profit report wrong, find products without cost shopify, bulk update cost per item shopify, shopify unit cost, shopify inventory value, gross profit by product shopify, AI catalog audit
- Entities: Shopify (https://www.wikidata.org/wiki/Q7501150); Gross margin (https://www.wikidata.org/wiki/Q11157999); Inventory (https://www.wikidata.org/wiki/Q815410); Business process automation (https://www.wikidata.org/wiki/Q5001911)
- Section anchors: The short answer (https://blog.dugong.live/how-to-find-shopify-products-with-no-cost-per-item.html#h-the-short-answer); A blank cost does not zero your margin, it removes the sale (https://blog.dugong.live/how-to-find-shopify-products-with-no-cost-per-item.html#h-a-blank-cost-does-not-zero-your-margin-it-removes-the-sale); Why the field is empty in the first place (https://blog.dugong.live/how-to-find-shopify-products-with-no-cost-per-item.html#h-why-the-field-is-empty-in-the-first-place); There is still no way to search for the blanks (https://blog.dugong.live/how-to-find-shopify-products-with-no-cost-per-item.html#h-there-is-still-no-way-to-search-for-the-blanks); The wrong number is worse than no number (https://blog.dugong.live/how-to-find-shopify-products-with-no-cost-per-item.html#h-the-wrong-number-is-worse-than-no-number); What your stock is worth depends on what your tool does with the gaps (https://blog.dugong.live/how-to-find-shopify-products-with-no-cost-per-item.html#h-what-your-stock-is-worth-depends-on-what-your-tool-does-with-the-gaps); One value per variant, and no history behind it (https://blog.dugong.live/how-to-find-shopify-products-with-no-cost-per-item.html#h-one-value-per-variant-and-no-history-behind-it); Flow has the pieces and not the headroom (https://blog.dugong.live/how-to-find-shopify-products-with-no-cost-per-item.html#h-flow-has-the-pieces-and-not-the-headroom); What this costs you on an ordinary month (https://blog.dugong.live/how-to-find-shopify-products-with-no-cost-per-item.html#h-what-this-costs-you-on-an-ordinary-month); What the automation actually has to do (https://blog.dugong.live/how-to-find-shopify-products-with-no-cost-per-item.html#h-what-the-automation-actually-has-to-do); Do this before you close the laptop (https://blog.dugong.live/how-to-find-shopify-products-with-no-cost-per-item.html#h-do-this-before-you-close-the-laptop); Common questions (https://blog.dugong.live/how-to-find-shopify-products-with-no-cost-per-item.html#faq-heading); Read next (https://blog.dugong.live/how-to-find-shopify-products-with-no-cost-per-item.html#related-heading)
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

You open Gross profit by product at the end of the month. The margins look plausible. Nothing is flagged, nothing is blank, nothing looks broken.

Then somebody notices that the sales total in the profit report is smaller than the sales total in the sales report, and the afternoon goes on finding out why. Eleven variants in your catalog have never had a cost on them. Every order containing one of those eleven was left out of the profit report completely.

Not counted at zero margin. Not shown as a loss. Left out.

That is the part that catches people. A missing cost does not produce the error you would notice. It produces a clean report of a smaller store.

## The short answer

Shopify's profit reports only include items that had a cost recorded at the moment they sold. The help page is explicit: profit is reported only for products and variants that had a cost recorded at the time they were sold, and if orders are missing from the report then it is likely those variants have no cost information. So a blank cost field does not make a product look unprofitable. It makes the sale invisible.

The field is also static. The cost is captured onto the order as it happens, so filling in a cost today does nothing for last month's orders. Whatever margin you have already lost sight of, you have lost for good.

Finding the blanks has no native path. Cost per item lives on the variant, there is no filter for it, and a merchant who asked for one in 2022 was told there is no way to filter or sort products based on product cost. Four years on, the answer is still a CSV export sorted on that column by hand.

Wrong costs are at least as common as missing ones and much harder to see. A merchant auditing his own store in October 2026 found 16 of his 29 active products had the wrong cost per item, some set equal to the selling price, a few left as 999 placeholders, and Shopify's profit report was telling him he lost money on products that actually make money.

So the job is not a report you run. It is a standing check: sweep every variant for blanks and for nonsense, catch a new product on the day it is created rather than the month it is reconciled, and keep your own dated record of what each delivery actually cost.

## A blank cost does not zero your margin, it removes the sale

This is the single fact worth taking away, because every other symptom follows from it. Shopify's [profit reports documentation](https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/profit-reports) says the report only takes into consideration the variants that have product cost information at the time of sale, and that if orders are missing from this report, then it is likely that these variants do not have cost information.

Five reports inherit that rule: average profit margin by market, gross profit by product, gross profit by product variant, gross profit by POS location, and profit margin by order. All five are counting a smaller set of orders than your sales reports are, and none of them says so on the screen.

Which gives you a diagnostic you can run in two minutes, and the quickest honest answer to the question of whether you have this problem at all. Pull net sales for last month from the sales reports. Pull the sales figure from a profit report for the same period. If the two disagree, the difference is revenue you cannot see a margin on.

The timing is the cruel part. The cost is written onto the order when the order is placed, and the help page describes Cost per item as containing static data. Backfilling the field fixes the future and nothing else. A product that has been selling quietly without a cost since March has six months of orders that will never carry margin, no matter what you type in now.

## Why the field is empty in the first place

Nobody decides to leave a cost blank. The admin arranges for it.

Cost per item lives on the variant, not on the product. A shirt in five sizes needs five costs, and the number you typed while setting up the first one covers exactly that one. Worse, the field is not available per variant while a product with options is being created. A merchant raised this in [April 2024](https://community.shopify.com/t/cost-per-item-no-longer-available-for-variant-when-creating-product/311192), writing that you were able to edit the Cost Per Item for each variant SKU before saving or creating the product, and noting that some products have a different cost depending on size or other reason like exclusivity. Shopify thanked her for letting them know she would like to see this flow reinstated and passed it to the development team. Nothing was marked as solved.

So the supported path is: create the product, save it, then go back into the variant list and fill in the costs. Which is a second trip, after the satisfying part is finished, on a product that is already live. It is the most skippable step in the whole catalog workflow.

Then there is everything that creates products without a human present. A CSV import that omits the column leaves it empty. A supplier feed carries retail prices and rarely carries costs. A product duplicated from last season's version inherits whatever that one had, which is often also nothing. None of these fail loudly, because an empty cost is a perfectly valid product.

## There is still no way to search for the blanks

In [March 2022](https://community.shopify.com/t/how-to-find-products-without-a-cost-per-item-for-inventory-reporting/110859) a merchant asked whether there was a way to find all products that do not have a cost per item in a search, because month-end inventory reporting depended on it. The reply was blunt: as far as I know, there is no way to filter or sort products based on product cost. Export to CSV and filter the file. There was no staff answer and nothing marked as a solution, and a week later the merchant reported back that he had used the export.

That is still the method. Products, export all, open the file, sort on the [Cost per item](https://help.shopify.com/en/manual/products/import-export/using-csv) column, which Shopify documents as how much it costs you to make or acquire the product or variant. Export at variant level, not product level, or you will miss every parent whose first variant happens to be costed.

The bulk editor will then let you fix them, fifty rows at a time, once you know which rows to fix. It is a decent repair tool and no help at all as a detector, and the distinction matters: the reason catalogs drift is not that the fixing is hard, it is that nobody is told there is anything to fix.

## The wrong number is worse than no number

A blank at least behaves consistently. A plausible wrong cost does real damage, because it passes every check and then feeds decisions.

In [October 2026](https://community.shopify.com/t/we-found-16-of-our-29-products-had-the-wrong-cost-in-shopify-free-profit-check-for-5-stores-running-meta-ads/699113) a merchant wrote up an audit of his own store: 16 of 29 active products had the wrong cost per item, some set equal to the price, a few left as 999 placeholders. His conclusion is the line to remember. Shopify's own profit report was telling him he lost money on products that actually make money.

Both of those failure shapes come from the same human moment. The field is required-looking and the real number is not to hand, so somebody types the price, or types a big round number to get past it, intending to come back. Cost equal to price reports zero margin forever. A 999 placeholder reports a catastrophic loss on a product that is fine. And both sail through any check that only asks whether the field is populated.

So the test has to be a sanity check, not a completeness check. Cost equal to or above price. Cost at suspiciously round numbers. Cost at a margin far outside the band the rest of that product type sits in. Cost untouched for two years while the supplier has raised prices twice.

## What your stock is worth depends on what your tool does with the gaps

The same hole sits under inventory valuation, and a merchant put it well in [October 2026](https://community.shopify.com/t/what-is-your-stock-worth-the-answer-turns-on-what-your-tool-does-with-the-units-that-have-no-cost-on-them/697051): Shopify holds the quantities and it holds a cost per item field, but it never multiplies the two for you.

Which means some report, app or spreadsheet does the multiplying, and that thing has to decide what to do with the units that have no cost on them. It can count them as costing nothing. It can leave them out. It can show them to you separately. As he put it, the first two give you a number that is wrong in a direction you cannot see.

His test takes a minute and is worth running on whatever tool you currently trust. Find a stocked variant with no cost, note the valuation total, put a cost on it, and look again. If the total rises by more than that one variant's value, your tool had been dropping rows rather than zeroing them, and every figure you have sent an accountant was built on a quietly shorter list.

## One value per variant, and no history behind it

Cost per item holds a single number. There is nothing behind it.

A merchant described the ordinary version of this in a [September 2026](https://community.shopify.com/t/shopify-keeps-one-cost-per-variant-where-do-you-keep-the-rest/679035) thread: a hundred units bought at one price, sixty more arriving at a higher one, one field to record both. The reply he got is the whole situation in two sentences. Cost per item is one number per variant, Shopify will overwrite it, and there is no delivery history behind that field.

Another merchant in the same thread named the consequence people trip over: type a new number in and every unit you are holding revalues, including the ones you bought at the old price. Correcting a cost silently restates the value of stock you already own.

Merchants settle into one of three habits. Overwrite with the latest cost. Keep the original. Maintain a weighted average and push that in. Any of the three is defensible. Choosing case by case is not, because then nobody can say what the number in the field means, which is how two people in the same company produce two different margins for the same product and both are reading correctly.

If you need the trail, keep it yourself: a cost per delivery in a variant metafield or your own table, and Shopify's field treated as the current cost rather than the record. The API does not make this friendlier than it sounds. Reading the value means asking an inventory item for its [unitCost](https://community.shopify.dev/t/assymetry-of-cost-and-unitcost-on-inventoryitem/13399), while writing it goes through the variant bulk update, an asymmetry a developer wrote up in April 2025 after looking for a cost field that is not there.

## Flow has the pieces and not the headroom

This looks like a job for a scheduled workflow, and Shopify Flow looks like it should do it. Its [Scheduled time trigger](https://help.shopify.com/en/manual/shopify-flow/advanced-workflows) starts a workflow at a specific time and date that you specify, recurs hourly, daily, weekly or monthly, and can run as frequently as every ten minutes. Get product data retrieves a list of products matching a query, and the documented example is products that have no inventory.

The ceiling is on the same page. Get data actions can only run on lists up to 100 items long.

A catalog audit is the one job that has to look at everything, so a hundred-item window is the wrong shape for it, and there is no cost field in the query to narrow the list to the blanks before you hit that limit. Flow is still useful at the edge of this problem, for example tagging a newly created product so that somebody has to look at it before it goes anywhere. The sweep itself needs something that can page through every variant and keep score between runs.

## What this costs you on an ordinary month

Three places, all of them quiet.

Advertising decisions get made on margins that exclude your worst offenders, because a product with no cost contributes no margin data at all and simply is not in the comparison. Discount floors get set from a margin that is wrong on the specific products somebody typed the price into. And at year end the inventory value that goes to your accountant is built on a list quietly shorter than your actual shelf.

None of this announces itself. That is the whole character of the problem: the reports do not break, they narrow.

## What the automation actually has to do

As a Dugong playbook, in plain prose:

```
# trigger
Scheduled daily catalog sweep,
plus product created

# steps
1. Sweep every variant, not
   every product
2. Flag the blanks the day the
   product is created
3. Catch the costs that are
   obviously wrong
4. Keep a dated cost for every
   delivery
5. Reconcile profit sales
   against total sales
6. Value the stock with the
   gaps shown
7. Hold the launch until a cost
   is on it
```

Step one is the design decision. Walk variants, because that is where the field lives and where the gaps hide behind a parent product that looks complete. A catalog of four hundred products can easily be two thousand variants, and the count that matters is the second one.

Step two is the one that pays for the whole thing. The cost of a new product is easiest to find on the day it is created, when the supplier invoice is still open on somebody's screen. Wait a month and it becomes research. Wait until reconciliation and the first sales are already outside the report for good.

Step three is the sanity check rather than the completeness check: cost equal to or above price, round placeholder numbers, a margin far outside the band for that product type, a cost nobody has touched in two years. These are the ones that quietly produce confident wrong answers.

Step four keeps the trail Shopify does not. One row per delivery with a date, a quantity and a unit cost, and one rule for what gets pushed into the single field, applied the same way every time.

Step five turns the invisible into a number. Compare the sales total in the profit report against the real sales total every month, and report the gap as a figure with a name. A number on a dashboard gets fixed. An absence does not.

Step six is about honesty in valuation. Show the stock value, and next to it show the units with no cost behind them, as units and as a percentage. A valuation with a stated gap is usable. A valuation that silently drops the gap is not, and it is the one most tools hand you.

Step seven is the lever that stops the problem coming back. Costless products do not go live. Hold the publish, tell whoever is launching it, and release it the moment a cost appears. It sounds strict and takes about a week to feel normal, because the alternative is finding out in March that January never had margin.

## Do this before you close the laptop

Three things, in about twenty minutes, before you automate anything.

Export your products to CSV at variant level and count the blanks in the Cost per item column. That number is the size of your problem and you have probably never seen it.

Sort that column both ways. The top end shows you the placeholders and the costs that match the price. The bottom end shows the suspiciously tidy numbers. These are the rows a completeness check would have passed.

Then put last month's net sales from the sales reports next to the sales figure in a profit report. If they differ, you now know what fraction of your revenue your margin reporting has never been able to see, and you know what the automation has to replace.

> **◆ READING** Two companion pieces if this one landed: [the price change you make one product at a time](https://blog.dugong.live/how-to-bulk-edit-product-prices-on-shopify.html), on the other half of the margin equation, and [the dead stock your dashboard never mentions](https://blog.dugong.live/how-to-automatically-clear-dead-stock-on-shopify.html), on the stock whose value you are being quietest about.

If you sell on Shopify and have a version of this story, the profit report that was short by a third, the 999 placeholder nobody went back for, the year-end valuation that moved when somebody filled in one field, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### How do I find Shopify products with no cost per item?

There is no filter for it in the admin, so the working method is a CSV export. Go to Products, export all products as a CSV, open the file and sort on the Cost per item column, which Shopify documents as how much it costs you to make or acquire the product or variant. Every blank row in that column is a variant your profit reports cannot see. Sort it the other way too, because the obviously wrong costs sit at the top: a cost equal to the price, or a round placeholder somebody typed once to get past the field. A merchant asked for a proper search in March 2022, asking whether there was a way to find all products that do not have a cost per item in a search, and was told plainly that there is no way to filter or sort products based on product cost. The thread has no staff reply and nothing marked as a solution, and four years later the export is still the answer. Export at the variant level rather than the product level, because the cost is stored per variant and a product whose first variant has a cost can easily have five more that do not.

Permalink: https://blog.dugong.live/how-to-find-shopify-products-with-no-cost-per-item.html#faq-1

### Why is my Shopify profit report missing orders?

Because a missing cost removes the sale from the report rather than showing it at zero margin. Shopify's profit reports page says profit is reported only for products and variants that had a cost recorded at the time they were sold, and adds that if orders are missing from this report, then it's likely that these variants don't have cost information. That is also why net sales in your sales reports and net sales in your profit reports can disagree: they are counting different sets of orders. The timing matters as much as the field. The cost is captured onto the order at the moment of sale, and the page describes the Cost per item field as containing static data, so filling in a cost today does not retrofit margin onto last month's orders. The gap in your historical profit numbers is permanent. All you can fix is everything from here.

Permalink: https://blog.dugong.live/how-to-find-shopify-products-with-no-cost-per-item.html#faq-2

### Why is cost per item blank on so many Shopify products?

Mostly because of where the field lives and when the admin offers it to you. Cost per item sits on the variant, not the product, so a shirt in five sizes needs five costs, and the one you typed on the first variant covers none of the others. It is also not available while you are creating a product with options. A merchant raised this in April 2024, writing that you were able to edit the Cost Per Item for each variant SKU before saving or creating the product, and noting that some products have a different cost depending on size or other reason like exclusivity. Shopify replied thanking her for letting them know she would like to see this flow reinstated and passed it to the development team. Nothing was marked as solved. So the normal path through the admin is to save the product first and come back for the costs, which is exactly the kind of step that gets skipped on a busy afternoon. Imports and apps add the rest: a CSV that omits the column, a supplier feed that carries prices but not costs, and a product duplicated from an older one that never had a cost either.

Permalink: https://blog.dugong.live/how-to-find-shopify-products-with-no-cost-per-item.html#faq-3

### Does Shopify keep a history of cost per item changes?

No. Cost per item is one value per variant with nothing behind it. A merchant described the problem precisely in a September 2026 community thread: a hundred units bought at one price, sixty more arriving at a higher one, and one field to record both. Another merchant answered that cost per item is one number per variant, that Shopify will overwrite it, and that there is no delivery history behind that field. A third pointed out the consequence that catches people out, which is that typing a new number in revalues every unit you are holding, including the ones you bought at the old price. In practice merchants pick one of three habits: overwrite with the newest cost, keep the original, or maintain a weighted average and push that number into the field. Any of them works as long as it is the same one every time. What does not work is deciding case by case, because then nobody can say what the number in the field means. If you need the trail, keep the per-delivery costs somewhere you own, a variant metafield or your own table, and treat Shopify's field as the current cost rather than the record.

Permalink: https://blog.dugong.live/how-to-find-shopify-products-with-no-cost-per-item.html#faq-4

### Can Shopify Flow find products with a missing cost?

Not across a catalog of any size. Flow does have the pieces that look right. The Scheduled time trigger starts a workflow at a specific time and date that you specify, recurs hourly, daily, weekly or monthly, and can run as frequently as every ten minutes, and the Get product data action retrieves a list of products matching a query, the documented example being products that have no inventory. The ceiling is in the same help page: get data actions can only run on lists up to 100 items long. A catalog audit is the one job that needs to look at everything, so a hundred-item window is the wrong shape for it, and there is no cost field to filter the query down to the blanks in the first place. Flow is still useful at the edges, for example tagging a newly created product so somebody has to look at it. The sweep itself needs something that can page through every variant and keep score.

Permalink: https://blog.dugong.live/how-to-find-shopify-products-with-no-cost-per-item.html#faq-5

### Can AI keep Shopify cost per item complete?

Yes, and it suits automation well, because every part of the job is a comparison rather than a judgment. An automation like Dugong reads every variant rather than every product, since the blanks hide behind parents that look fine. It checks a new product the day it is created, which is the moment the cost is cheapest to get and the only moment before the first sale is lost to the report forever. It flags the costs that are obviously wrong as well as the ones that are missing, because a cost equal to the price and a 999 placeholder both pass a completeness check and both lie: a merchant auditing his own store in October 2026 found 16 of his 29 active products had the wrong cost per item, some set equal to the price and a few left as 999 placeholders, and said Shopify's own profit report was telling us we lost money on products that actually make money. It reconciles the sales total in the profit report against the sales total in the sales report each month, so the gap becomes a number somebody sees. And it keeps a dated cost per delivery alongside the single field, so the question of what the stock is worth has an answer that does not depend on who last typed in the box. The honest limits: it cannot invent a cost nobody recorded, it cannot repair the margin on orders that already shipped without one, and it can only flag a cost that looks wrong, not one that is quietly ten percent stale.

Permalink: https://blog.dugong.live/how-to-find-shopify-products-with-no-cost-per-item.html#faq-6

---

## Read next

- [The price change you make one product at a time](https://blog.dugong.live/how-to-bulk-edit-product-prices-on-shopify.html): Shopify's bulk editor caps at fifty products, has no math, and Flow cannot reprice at all, so you retype every price by hand. The AI playbook that reprices the catalog by rule.
- [The dead stock your dashboard never mentions](https://blog.dugong.live/how-to-automatically-clear-dead-stock-on-shopify.html): Shopify has no last-sold date, no aging alert, and no automatic markdowns, so dead stock sits until stocktake. The AI playbook that finds and clears it on time.
- [The SKU two products share](https://blog.dugong.live/how-to-fix-duplicate-skus-on-shopify.html): Shopify's docs say SKUs must be unique, then let two products save the same one and split the stock between them. The AI playbook that finds every collision.
