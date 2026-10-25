# How to stop Shopify B2B prices dropping every time you run a sale

> You ran 25 percent off for the weekend and your trade accounts took it too, on top of their wholesale discount. The AI playbook that holds the B2B price floor.

- Canonical: https://blog.dugong.live/how-to-stop-shopify-b2b-prices-dropping-when-you-run-a-sale.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-10-17
- Section: Research
- Word count: 3000
- Dispatch: Nº 130 · Research · 10 min read
- Full headline on page: How to stop Shopify B2B prices dropping *every time you run a sale*
- Keywords: shopify b2b discount stacking, shopify wholesale price sale, shopify b2b catalog discount, shopify price list fixed prices, shopify b2b pricing automation, b2b catalog percentage adjustment shopify, shopify b2b markets discount eligibility, AI wholesale pricing automation
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

You find out on the invoice after the sale, not during it. Six cases of the mug that lists at forty dollars, bought by a stockist on your trade catalog, and the line price reads twenty four. Twenty five percent off because the storefront ran a weekend sale, twenty percent off because she is a stockist, and the two found each other at checkout while nobody was looking.

Nobody set that price. You set a sale. The sale walked into your wholesale catalog, because in Shopify a catalog is not a discount, and the number your trade accounts pay is pinned to the number your retail customers pay.


## The short answer

A B2B catalog is part of Shopify's pricing system, not its discount system, so a catalog percentage is calculated from the product's standard store price at the moment the buyer loads the page, which means every retail markdown moves your wholesale floor down with it.

If the sale is an automatic discount or a code instead, Shopify documents that those apply as additional discounts on top of any price adjustments made through catalogs, and that in a blended store existing discounts apply to both B2B and D2C customers unless you assign a B2B market in the discount's eligibility settings. There is no setting that anchors a trade price to list price.

Fixed prices are the only native lock, because after a fixed price is assigned any overall adjustments on the catalog no longer apply, and they go stale the next time you raise list prices, with no stale price report, a 250 price per request cap on priceListFixedPricesAdd and priceListFixedPricesUpdate, and a catalog CSV export that includes only fixed-price products.

Flow has no price changed trigger and no price list action, so the fix is an external loop that sets the trade floor from list price and cost, writes a fixed price to hold it through every markdown, releases it afterwards, and scopes every promotion away from your B2B markets.
## Catalogs are pricing, discounts are discounts

The clearest statement of this is not in Shopify's documentation, it is in a community reply from January 2026: catalogs are part of the pricing system, not the discount system. Everything that goes wrong here follows from that one sentence.

A B2B catalog does two things to a price. It can apply an overall percentage increase or decrease across every product in it, and it can set fixed prices on specific products or variants. The [Help Center](https://help.shopify.com/manual/b2b/catalogs/creating-catalogs)'s own example is ten dollar candles at 20 percent off, which become eight dollars for companies with catalog access. Notice what the eight dollars is made of. It is not a wholesale price. It is a calculation performed on the retail price, at the moment the buyer loads the page.

The API does not hide this. The [price list object](https://shopify.dev/docs/api/admin-graphql/latest/objects/PriceList) calls its adjustment the `parent`, documented as relative adjustments to other prices, and `priceListCreate` takes parent adjustment settings that determine how the system calculates prices relative to base prices. Relative is doing all the work in that sentence. Mark the candle down to seven fifty for a four day sale and the trade price becomes six without anybody touching the catalog. Nothing is misconfigured. It is working exactly as written.

## And then the discount stacks on top

That is only the first of two leaks, and most stores have both. If your sale is a price edit, the catalog percentage follows it down. If your sale is an automatic discount or a code, something different and equally expensive happens: [Shopify documents](https://help.shopify.com/en/manual/b2b/catalogs/discounts) that automatic discounts and discount codes apply as additional discounts on top of any price adjustments made through catalogs. The trade price is computed first, then the promotion comes off that.

The default is the part that catches people. Discounts are enabled for B2B out of the box, and in a blended store the Help Center states plainly that existing discounts apply to both B2B and D2C customers unless you scope them. The scoping exists: you assign a B2B market in the discount's eligibility settings. But it is opt out, not opt in, so a promotion written for a retail audience is live for your stockists the second you publish it, landing on a price that is already a fifth under list, and nothing in the admin ever mentions that the combination is possible.

> **◆ NOTE** If you only fix one thing after reading this, fix the eligibility default. Scoping promotions to exclude B2B markets closes the louder of the two leaks in an afternoon, and it does not require a single line of code.

## The merchants who found out in public

[August 2024](https://community.shopify.com/t/price-catalog-b2b/348867), a merchant asks how to base her B2B catalog discount on compare at price rather than price, because, as she puts it, price is dynamic in B2C and compare at is the fixed list price. She is asking for the normal thing every wholesale business does: a trade price anchored to list, not to whatever retail is doing this week. Two years later there is still no setting for it.

[December 2025](https://community.shopify.com/t/b2b-trade-catalog-discount-stacking-from-b2c-site/579283) is where it gets specific. A merchant with a 20 percent trade catalog and B2C promotions running describes the symptom in one line: the discount gets stacked on top of the 20 percent trade discount on our B2B site. He has over 300,000 SKUs, so the export and reimport fixed prices suggestion dies on arrival. The next day he comes back and says he has no development team, and asks for setup instructions for the API script everyone keeps mentioning. That is the last anyone hears from him.

The thread kept running for eight more months without him, through a confirmation that there is no native fix, the pricing versus discounts distinction, a sketch of a Shopify Function that skips products already on sale, and somebody in August asking whether he ever solved it. The last reply is the clearest one: catalog percentage adjustments use the current price, and the `PriceListCompareAtMode` setting does not change that, so automate fixed catalog prices through the Admin GraphQL API or build a custom Function. Six replies recommend an app and four of those are the replier's own. No Shopify staff posted. Nothing is marked as the solution.

One workaround in the neighboring thread deserves naming, because it is what this looks like when a human does it. A merchant keeps a collection called Sale Items, updates it weekly by hand, and scopes an automatic discount to that collection only. It works. It is also a person joining the promotion calendar to the price list every Monday morning, forever, and forgetting once costs a quarter of margin.

## Fixed prices, and the trap inside them

Shopify does give you a lock. The Help Center says fixed prices override any overall adjustments that you set, and that after a fixed price is assigned, any overall adjustments on the catalog no longer apply. The nine dollar candle stays nine dollars while everything around it drops to eight. Put fixed prices on everything and no sale can reach wholesale again.

That is true, and here is the bill.

A fixed price is a number, not a rule. Nothing in Shopify re-derives it when your list price or your landed cost moves. Raise prices 6 percent in March and every fixed price in every catalog still reads February, with no warning, no stale price report and no alert anywhere in the admin. The catalog you made immune to your sales is now immune to your price increases, which is the same bug wearing a different coat. This is the trade every store makes without noticing: [a price change you make one product at a time](https://blog.dugong.live/how-to-bulk-edit-product-prices-on-shopify.html) becomes a price change you have to make twice, once on the product and once in every catalog.

Rewriting them is bounded. The [`priceListFixedPricesAdd`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/priceListFixedPricesAdd) mutation creates or updates fixed prices and replaces any existing fixed prices for those variants, and Shopify staff [confirmed in August 2025](https://community.shopify.dev/t/pricelistfixedpricesadd-limit/21835) that it and `priceListFixedPricesUpdate` both cap at 250 prices per request. A 300,000 SKU catalog is 1,200 calls, multiplied by however many catalogs you run, and a company location can hold up to 25.

Auditing is worse than writing. Shopify documents that exported catalog CSV files include only fixed-price products, not percentage-adjusted prices, so the one report you would reach for omits, by design, exactly the prices that move on their own. And the import can undo you: leaving both Fixed Price and Compare At blank for a product removes that product's fixed price, and removed fixed prices revert all variant prices to the price list's adjustment rules. One blank column silently hands the variant back to the percentage rule you were escaping.

None of that is theoretical. In June 2025, after Markets became Catalogs, merchants reported CSV market price columns behaving inconsistently, some products pricing correctly and others ignoring the columns entirely. One said they had been selling at wrong prices. Another, running 23 markets and over 1.5 million lines, reported a single download taking more than two hours and producing 23 files totalling 223MB, and started building his own export tool. Support said they had not seen the issue before. No staff reply ever landed.

## Compare at mode is not the lever people reach for

There is a settings field that looks like the answer and is not. [`PriceListCompareAtMode`](https://shopify.dev/docs/api/admin-graphql/unstable/enums/PriceListCompareAtMode) has exactly two values. `ADJUSTED` means the compare at price is adjusted based on the percentage specified in the price list. `NULLIFY` means compare at prices are set to null unless explicitly defined by a fixed price value. One styles the strikethrough, the other removes it. Neither changes a cent of what the buyer is charged, and there is no third value that says take 20 percent off compare at. The merchant who asked for that in August 2024 was asking for a value that does not exist.

## Flow has no idea your price changed

The usual next move is to automate around it, and this is where Flow runs out of bench. The native product triggers are product created, product deleted, product status updated, product variant added, product variant deleted, product variant inventory quantity changed, product variant out of stock and product variant back in stock. There is no price changed trigger, and not even a general product updated trigger.

On the B2B side Flow has the company location created trigger and an [add catalog to company location](https://help.shopify.com/en/manual/shopify-flow/reference/actions/add-catalog-to-company-location) action, which maps to `catalogContextUpdate` and is genuinely useful for [onboarding a new trade account](https://blog.dugong.live/how-to-automatically-approve-wholesale-customers-on-shopify.html). Nothing on the bench reads a price list, writes a fixed price, compares a catalog price against cost, or notices that [a scheduled markdown](https://blog.dugong.live/how-to-schedule-a-sale-on-shopify.html) is about to take the trade price with it.

So the event you need to react to is invisible to Flow, and the object you need to write to is untouchable by it. That combination has a familiar shape: [the automation that never ran](https://blog.dugong.live/how-to-catch-shopify-flow-workflows-that-fail-silently.html) looks identical to a quiet week. Here it is worse, because the automation was never buildable in the first place, and the leak is silent by construction.

## What the silence costs

Put numbers on it. A mug lists at forty, lands at twenty two, and your trade catalog takes 20 percent off, so the stockist pays thirty two and you keep ten. Run 25 percent off retail for a long weekend and the catalog follows the markdown down: she now pays twenty four and you keep two. If the sale was an automatic discount instead, the 25 percent comes off the thirty two, she pays twenty four, and in plenty of stores the same arithmetic lands under cost once you add freight on a pallet.

Then the volume works against you, which is what makes this different from a retail markdown. Retail customers buy one. Trade accounts buy by the case, so the leak is multiplied by exactly the number that made wholesale worth doing. And where a location holds several catalogs with the same product at different prices, Shopify shows the lowest, so one leaking catalog sets that buyer's price however carefully the others are kept.

The slowest cost is behavioral. Buyers notice patterns faster than merchants audit them, and a stockist who works out that your trade price dips during every storefront promotion will simply time her reorders. That never shows up as a discount problem. It shows up as flat trade revenue with a thin margin in Q4, and it gets blamed on freight.

## What the automation actually has to do

As a Dugong playbook, in plain prose:

```
# trigger
Hourly on list price and
cost, plus every discount
before it goes live

# steps
1. Resolve what every buyer
   actually pays: variant,
   catalog, price, cost
2. Set the floor from policy,
   off list price, never off
   the sale price
3. Hold it: write a fixed
   price when a markdown
   would break the floor
4. Release the fixed price
   when the markdown ends,
   250 variants per call
5. Refuse any promotion
   still eligible for your
   B2B markets
6. Alarm on stale: fixed
   prices older than the last
   list change, any under cost
7. Report realized margin by
   company location and by
   promotion
```

Step one is the whole trick, and it is the thing Shopify will not hand you. The API will tell you a price list's `fixedPricesCount` and let you page its prices filtered by origin type, fixed or relative. It will not give you one table saying: for this variant, this buyer pays this, it came from a percentage rule, cost is this, margin is this. That table is the artifact everything else compares against.

Steps two and three are where the policy lives, and the policy is one sentence: the trade price is a function of list price and cost, never of the retail selling price. Write that down and the behavior falls out. When a markdown is scheduled or a price edited, the system computes what each catalog would charge afterwards, and anywhere that number lands below the floor it writes a fixed price at the floor instead. The sale runs on the storefront. The trade price does not move. This is the honest version of what the community arrived at after nine months, except that it also knows when to take the fixed prices off again, which is the step every manual version forgets.

Step five is cheap and catches the majority of real money. Every new discount gets checked before it is published: if the eligibility still includes a B2B market and nobody said that on purpose, it does not ship. The same guard that stops [a code double dipping on a sale item](https://blog.dugong.live/how-to-stop-discount-codes-applying-to-sale-items-on-shopify.html) works here, one layer up.

Step six pays for itself in the quarter after a price increase. Any fixed price older than the last change to its product's list price is stale by definition and gets flagged with both numbers side by side. Any catalog price under landed cost is an incident, not a report line. And any variant whose [quantity breaks](https://blog.dugong.live/how-to-set-up-tiered-volume-discounts-on-shopify.html) stop descending as quantity rises is a configuration bug worth catching before a buyer finds it.

The honest limits. Your floor is a commercial decision and nothing can write it for you. Only a Shopify Function can change what checkout computes in the moment, so this playbook holds the line by writing prices rather than intercepting them, which leaves a window between a price edit and the next reconciliation. The way to shrink it is to catch the edit rather than the aftermath, the same discipline as [catching a mispriced product before the orders arrive](https://blog.dugong.live/how-to-catch-pricing-errors-on-shopify-before-orders-flood-in.html).

## Why this is a compiler problem, not an app problem

There is no shortage of B2B pricing apps, and several turned up in both threads, usually posted by the people who built them. They are not frauds. Each does one piece well: a better price list editor, a discount engine with eligibility rules, a Function that skips products already on sale.

The leak lives in none of those pieces. It lives in the join between four of them: list price, the catalog's rule, the promotion calendar, and landed cost. Shopify keeps those in four places with no relationship declared between them, so the only thing that can see the problem is something holding all four at once and checking them against a policy you wrote in one sentence. That is a workflow, not a feature, which is why the answer in the threads keeps coming out as write code and the merchants asking keep replying that they have no developer.

## Do this before you close the laptop

Three checks, twenty minutes, no code.

Open your next scheduled promotion and look at its eligibility. If it applies to all customers and you run a blended store, your wholesale accounts are in it, and that is Shopify's documented default rather than a mistake you made.

Take your five biggest trade SKUs and work out what a stockist actually paid during your last storefront sale. Not the catalog percentage, the number on the order. Put landed cost next to it. If any of the five is thinner than you expected, the other thousand are too.

Then export the catalog and count the rows against your variant count. The gap is the share of your wholesale pricing computed on the fly from retail prices, which is the share that moves every time you run a sale, and which the export cannot show you precisely because it moves.

> **◆ READING** Two companion pieces if this one landed: [the discount code that double dips your sale](https://blog.dugong.live/how-to-stop-discount-codes-applying-to-sale-items-on-shopify.html), on the same stacking problem one layer down, and [the certificate nobody checks](https://blog.dugong.live/how-to-make-shopify-wholesale-customers-tax-exempt.html), on the other wholesale detail that quietly costs money.

If you run wholesale on Shopify and have a version of this story, the sale that reached your trade catalog, the fixed prices nobody updated after a price rise, the buyer who learned your promo calendar, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Why do my Shopify B2B prices drop when I run a sale?

Because a B2B catalog is part of Shopify's pricing system, not its discount system, and a catalog percentage is calculated from whatever the product's price is at that moment. Shopify's Help Center describes the catalog adjustment as an overall percentage increase or decrease applied to the product's standard store price: ten dollar candles at 20 percent off become eight dollars for companies with catalog access. Mark the candle down to seven fifty for a weekend sale and the trade price silently becomes six. Nothing is misconfigured. The Admin API is honest about it, describing the price list parent as relative adjustments to other prices and the parent adjustment settings as the thing that determines how the system calculates prices relative to base prices. Relative is doing the work in that sentence: the trade price is pinned to the retail price, so every markdown you run moves the wholesale floor down with it. A merchant asked about this in August 2024, wanting the catalog discount calculated from compare at price instead, since price is dynamic in B2C and compare at is the fixed list price, and the answer two years later is still that there is no native setting for it.

Permalink: https://blog.dugong.live/how-to-stop-shopify-b2b-prices-dropping-when-you-run-a-sale.html#faq-1

### Do automatic discounts and discount codes apply to B2B customers on Shopify?

Yes, by default, and they stack. Shopify documents that automatic discounts and discount codes apply as additional discounts on top of any price adjustments made through catalogs, and that discounts are enabled for B2B by default. In a blended store that sells to both audiences, the Help Center is explicit that existing discounts apply to both B2B and D2C customers unless you scope them, and the way to scope one is to assign a B2B market in the discount's eligibility settings. That default is where most of the leak comes from. A promotion built for a retail audience goes live for your stockists too, lands on a price that is already 20 or 30 percent under list, and nothing in the admin flags that the combination exists. One merchant described the result in December 2025 in plain terms: the discount gets stacked on top of the 20 percent trade discount on our B2B site. The fix is not clever discount configuration, it is a rule that no promotion ships without its eligibility checked first.

Permalink: https://blog.dugong.live/how-to-stop-shopify-b2b-prices-dropping-when-you-run-a-sale.html#faq-2

### How do I stop a B2B catalog discount stacking on top of a sale price?

There are three honest paths and none of them is a setting. First, scope every retail promotion so B2B markets are not eligible, which closes the discount half of the leak but does nothing about markdowns made by editing the price. Second, stop marking prices down at all and run retail sales as automatic discounts only, so the catalog percentage always computes from an untouched list price. That works and it costs you strikethrough pricing on the storefront unless you manage compare at yourself. Third, put fixed prices on the catalog, because Shopify documents that after a fixed price is assigned, any overall adjustments on the catalog no longer apply, which also means no sale can reach it. Fixed prices are the real answer for most stores and they come with their own maintenance problem, described below. The path the community converged on, after a thread that ran from December 2025 to August 2026 with no Shopify staff reply and no accepted solution, was to automate fixed catalog prices through the Admin GraphQL API or to write a custom Shopify Function. Both are software projects, which is why the thread's original poster, running over 300,000 SKUs with no development team, asked for setup instructions and was never answered.

Permalink: https://blog.dugong.live/how-to-stop-shopify-b2b-prices-dropping-when-you-run-a-sale.html#faq-3

### Do Shopify B2B fixed prices update when I change a product's price?

No. A fixed price is a number, not a rule, and nothing in Shopify re-derives it when list price or cost moves. That is exactly why it defeats your sales, and exactly why it will eventually sell at last year's price. Raise list 6 percent in March and every fixed price in every catalog still says February until somebody rewrites it, with no warning, no stale price report and no alert. Rewriting is bounded too: priceListFixedPricesAdd creates or updates fixed prices and replaces any existing fixed prices for those variants, and Shopify staff confirmed in August 2025 that it and priceListFixedPricesUpdate both cap at 250 prices per request, so a 300,000 SKU catalog is 1,200 calls, multiplied by however many catalogs you run. Auditing is worse than the writing: Shopify documents that exported catalog CSV files include only fixed-price products and not percentage-adjusted prices, so the prices most likely to be wrong are the ones the export leaves out. And the import can undo you, because leaving both Fixed Price and Compare At blank for a product removes that product's fixed price, which hands the variant back to the percentage rule you were escaping.

Permalink: https://blog.dugong.live/how-to-stop-shopify-b2b-prices-dropping-when-you-run-a-sale.html#faq-4

### Can Shopify Flow react to a price change or update a B2B price list?

No to both, which is the structural reason this stays manual. Flow's native product bench is product created, product deleted, product status updated, product variant added, product variant deleted, product variant inventory quantity changed, product variant out of stock and product variant back in stock. There is no price changed trigger and no general product updated trigger, so the one event that moves your wholesale floor is the one event Flow cannot see. On the B2B side Flow has the company location created trigger and the add catalog to company location action, which maps to the catalogContextUpdate mutation and is genuinely useful for onboarding a new account. Nothing on the bench reads a price list, writes a fixed price, compares a catalog price against cost, or notices that a scheduled markdown is about to take the trade price with it. So the detection has to live outside Flow, on your own schedule, reading list price and cost and resolving what each catalog actually charges, and then writing prices back as the only lever Shopify exposes.

Permalink: https://blog.dugong.live/how-to-stop-shopify-b2b-prices-dropping-when-you-run-a-sale.html#faq-5

### Can AI keep my Shopify wholesale prices right?

Yes, because almost all of this is reading and reconciliation rather than judgment. An automation like Dugong builds the table Shopify will not give you, every variant against every catalog, with the resolved trade price whether it came from a percentage or a fixed price, the cost, and the margin that falls out. Then it watches: list price and cost hourly, the promotion calendar before anything goes live, and every catalog price against the floor your policy sets. When a markdown would push a catalog under that floor it writes a fixed price to hold the line, 250 variants per call, and releases it when the markdown ends. When you raise list prices it rewrites the fixed prices that have gone stale, which is the failure mode fixed prices create. It refuses a D2C promotion that still has B2B markets eligible, and it reports realized margin by company location so you can see which accounts have learned your promo calendar. The honest limits: your floor is a policy decision and nobody can write it for you; only a Shopify Function can change what checkout computes in the moment, so this approach holds the floor by writing prices rather than intercepting them; and if your catalogs are percentage-only across a very large SKU count, the first reconciliation run is long. What it removes is the quarter where trade margin quietly fell and freight took the blame.

Permalink: https://blog.dugong.live/how-to-stop-shopify-b2b-prices-dropping-when-you-run-a-sale.html#faq-6

---

Markdown rendition of https://blog.dugong.live/how-to-stop-shopify-b2b-prices-dropping-when-you-run-a-sale.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
