# How to automatically clear dead stock on Shopify

> Shopify has no last-sold date, no aging alert, and no automatic markdowns, so dead stock sits until stocktake. The AI playbook that finds and clears it on time.

- Canonical: https://blog.dugong.live/how-to-automatically-clear-dead-stock-on-shopify.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-08-01
- Updated: 2026-08-13
- Section: Research
- Word count: 2173
- Dispatch: Nº 97 · Research · 9 min read
- Full headline on page: How to automatically clear dead stock *on Shopify*
- Keywords: clear dead stock Shopify, slow moving inventory Shopify, automatically discount slow moving inventory Shopify, Shopify products not selling, inventory aging report Shopify, markdown automation Shopify, clearance collection Shopify, Shopify smart collection last sold date
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

The linen shorts arrived in April: 240 units across five sizes, because the rep offered a price break at 240 and June was going to be big. June was fine. The last pair sold on June 9. It is now August, and 212 pairs sit folded on four shelves of your Nashville stockroom, $9,300 at cost, and nothing anywhere in Shopify will ever tell you so. The product page looks healthy. The inventory count is comfortably green. To your admin, a product that has not sold in eight weeks looks exactly like a product that launched this morning.

You will find out in October, and not from a report. You will find out the way most merchants find dead stock: doing the fall stocktake, or unpacking the new season's delivery with nowhere to put it, or opening the 3PL invoice and noticing you have paid storage on the same 212 pairs for the fourth straight month. By then the season the shorts belonged to is over, and every option left is a bad one: bury them at 60 percent off in a January sale, bundle them away below cost, or write them off entirely.

The overbuy itself is ordinary. Every store that carries inventory makes it, every season, and a store that never overbuys is a store that constantly sells out. What turns an ordinary buying mistake into a write-off is the silence afterward: no aging alert, no last sold date, no report that acts. A product crosses 60 days without a sale, then 90, then 120, and each threshold passes without a single pixel changing anywhere in the admin.

## Why dead stock hides in a dashboard you check daily

Start where you would expect the answer to live: the products list. It has no last sold column, and it cannot be sorted by sales recency. To learn when a product last sold, you open the product, note the SKU, walk over to orders, and search. That is one product. A 340 SKU catalog is an afternoon, which is why nobody does it and the question goes unanswered until stocktake forces it.

The reports get closer, and stop short. **ABC analysis by product** grades your catalog by revenue share, and grade C, the bottom five percent of revenue, is where dead stock lives, alongside every new product too young to have earned its rank. **Days of inventory remaining** divides stock on hand by recent velocity, which is genuinely useful right up until velocity hits zero and the math gives up. Both reports describe. Neither one emails you, neither one changes anything, and neither one knows that the shorts were seasonal, that the candles sell only in Q4, or that the leather bags are slow every summer and always recover. The report is a mirror, not a tripwire.

Then you reach for the tools that automate everything else and find both of them blind. Smart collections match on title, type, vendor, price, tag, weight, and stock level, and not one condition can see sales data, so *products that have not sold in 90 days* is a collection Shopify cannot express. Neither can *new this month*, which is why new arrivals run on hand-applied tags that someone eventually forgets to remove, the same gap facing both directions. And [Shopify Flow](https://help.shopify.com/en/manual/shopify-flow), the automation layer, is built entirely on events: order created, inventory changed, product added.

> A product that stops selling emits no event. The automation platform is built on events, so the most expensive thing in your stockroom is the one thing it cannot see.

There is no trigger for silence, no product field holding time since last sale, nothing to hang a condition on. The absence of a sale, the exact signal that costs you the most money, is the one signal the platform has no way to represent.

## The clearance you eventually run by hand

So dead stock gets handled the way it has always been handled: in arrears, in a panic, usually the weekend before a new season lands. You export the orders CSV, pivot by SKU, and hand-build the list of what stopped moving. You [reprice it through the bulk editor](https://blog.dugong.live/how-to-bulk-edit-product-prices-on-shopify.html), fifty products at a time, setting compare-at prices by hand and hoping you fat-finger nothing. You drag products into a Sale collection one at a time. Somewhere in hour three you remember that [the welcome code stacks on top of markdowns](https://blog.dugong.live/how-to-stop-discount-codes-applying-to-sale-items-on-shopify.html) unless you guard for it, and now the 40 percent clearance is a 50 percent clearance for every subscriber.

Meanwhile the rest of the stack never got the memo. The [ad account is still spending](https://blog.dugong.live/how-to-automatically-pause-ads-for-out-of-stock-products-on-shopify.html) on products that died in June, paying full acquisition cost to send shoppers to a full-price page for a product you are about to mark down. The dead SKUs still sit mid-collection at full price, pushing live sellers [further down the page](https://blog.dugong.live/how-to-push-sold-out-products-to-the-bottom-of-a-shopify-collection.html). And the cruelest one: [the next purchase order](https://blog.dugong.live/how-to-set-inventory-reorder-points-on-shopify.html) quietly includes a reorder of something that was already dying, because the buying spreadsheet tracks what sold, not what stopped.

> **◆ NOTE** Holding inventory is not free storage of future revenue. The standard estimate puts carrying cost at **25 to 30 percent of the inventory's value per year** once storage, insurance, shrink, and the cost of the tied-up cash are counted. The $9,300 of shorts is not sitting still; it is quietly invoicing you a couple of hundred dollars a month for the privilege of keeping the mistake.

## What the automation actually has to do

The fix is not a better report. It is the Monday morning read a good merchandiser would do, and the actions that follow from it, running every week without being asked. As a Dugong playbook, in plain prose:

```
# trigger
On a weekly schedule, and when a season end nears

# steps
1. Read sell-through per product: last sale
   date, weekly velocity, stock on hand, days
   of cover, season
2. Flag what crossed your thresholds: 60 days
   slowing, 90 stalled, 120 dead, with the
   cash value attached to each
3. Choose the move per product: markdown,
   bundle, gift with purchase, outlet
   collection, or write-off
4. Draft the markdown against a margin floor,
   compare-at handled, end date attached
5. Re-merchandise: tag into clearance, demote
   in full-price collections, keep codes off
   the markdowns, stop the ads
6. Watch the move work: no lift in two weeks
   means deeper cut or different move, and a
   product that wakes up gets its price back
7. Report weekly: cash freed, what moved, what
   did not, and what buying should stop
   reordering
```

Step one is the part that looks trivial and is not. Computing last sale date per product is arithmetic, but reading it is judgment. A winter coat that has not sold since March is not dead in July, it is early. A product with 30 days of silence and four units left is not a markdown candidate, it is nearly sold through. A size run broken down to XS and XXL will never move at any discount, and wants a bundle or an outlet, not a price cut that insults the margin without shifting a unit. A threshold can count days. It takes something that understands what the product is to know which silences matter.

Steps four and five are where hand-run clearances leak. The markdown needs a floor, because clearing stock at any price is how you teach yourself to lose money twice on the same buy. The compare-at price needs to be set honestly and put back when the markdown ends, which is [its own unautomated chore on Shopify](https://blog.dugong.live/how-to-schedule-a-sale-on-shopify.html). The clearance tag needs to drive everything downstream in one motion: the outlet collection gains the product, the full-price collections demote it, the ads stop spending on it, and the discount codes are fenced off from double-dipping. Done by hand, those are five separate sessions in five separate screens, which is exactly why at least one of them is always forgotten.

And step three is where the interesting money is, because a markdown is not the only move, just the only one anyone remembers at 11 p.m. on inventory weekend. Slow candles can ride along as [a gift with purchase](https://blog.dugong.live/how-to-automatically-add-a-free-gift-with-purchase-on-shopify.html) that lifts the average order instead of cutting a price. Broken size runs bundle with their bestselling siblings. A product that died on your store but sells steadily wholesale wants a line on the next trade order, not a discount. The move should fit the product, and the automation should propose it, not just the percentage.

## Why this is a compiler problem, not an app problem

There are markdown apps, and for a store with one rule they are fine. What they hold is a threshold. What you have is a policy, and your policy is a paragraph: anything past 90 days goes to 20 percent off, except the leather goods, which never go on sale because the brand does not discount leather; candles bundle instead of marking down; broken size runs go to the outlet collection; nothing drops below 15 points of margin without a human saying so; and if a product starts selling again, put the price back and take it out of clearance. That paragraph changes with the season and the cash position. No settings page holds it. A compiler that turns the paragraph into the running workflow can, which is the argument behind [the automations no one builds](https://blog.dugong.live/best-shopify-automations-to-set-up.html): the valuable workflow is shaped like your store, not like a feature list.

Run the tape forward for the Nashville boutique. The first weekly read flags 41 of 340 SKUs past 90 days, $28,400 at cost, which is the number that finally makes the problem real. The owner approves the first wave: 19 markdowns at 20 percent with the floor respected, six bundles, five gift-with-purchase candidates, the shorts to the new outlet collection at 30 percent off while August can still sell them. Two weeks later the automation deepens four markdowns that did not lift and quietly restores one product that woke up. Five weeks in, 60 percent of the flagged cash has moved at planned margins instead of January panic prices. And the April-style overbuy that happens again next spring gets flagged at 60 days, marked down 20 percent while the season is alive, instead of 60 percent after it is dead.

## The workflow worth building this week

Start with the number you do not have. Export your orders, pivot to a last sale date per SKU, and count what has crossed 90 days, with the cost value next to it. Most merchants who run this for the first time find more cash on the aging list than in their bank account, and the number is worst in exactly the categories they were proudest of buying deep.

Then automate the reading before the acting. For the first two weeks, let the workflow compute the aging list, flag the crossings, and draft the moves, and approve each one yourself. You are checking its judgment against yours: does it know the coats are seasonal, does it respect the no-discount brands, does it propose bundles where a markdown would be waste. Once it has been right fifty times, let the clear cases run end to end and keep the approvals for anything touching your margin floor.

Describe it the way you would brief a merchandiser on their first Monday. Every week, tell me what stopped selling and what it is costing us to keep. Propose the move for each one, and mark things down with the margin protected, the sale price honest, and an end date attached. When something goes to clearance, make the whole store agree: collection, ads, codes, everything. If a move does not work in two weeks, escalate it. And tell buying what to stop reordering. That is the brief. The compiler handles the schedules, the tags, and the price edits, and the shorts get cleared in August at 30 percent off instead of surviving to haunt the January sale.

> **◆ READING** Two companion pieces if this one landed: [the reorder you always make too late](https://blog.dugong.live/how-to-set-inventory-reorder-points-on-shopify.html), on the same loop from the buying side, and [the sale you have to start by hand](https://blog.dugong.live/how-to-schedule-a-sale-on-shopify.html), on the mechanics of moving prices on time. Also worth reading: [the expiry date your store can't see](https://blog.dugong.live/how-to-track-product-expiry-dates-on-shopify.html), on the stock that does not just sit, it spoils.

If you are a Shopify merchant with a stockroom shelf you avoid looking at, a January sale that is really a confession, or a spreadsheet named clearance_final_v3, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### How do I find products that are not selling on Shopify?

Shopify will not surface them for you. The products list has no last sold column and cannot be sorted by sales recency, so the honest answers live in reports and exports. Start with the ABC analysis by product report, where grade C collects the bottom five percent of your revenue, and Days of inventory remaining, which divides stock on hand by recent velocity. Neither shows a plain last sold date, so for that you export orders, pivot by SKU, and take the most recent order date per product. Most merchants grade against thresholds by category, commonly 60 days for slowing, 90 for stalled, and 120 for dead, with seasonal exceptions applied by judgment. The catch is that all of this describes the problem on the day you run it. Nothing in Shopify alerts you when a product crosses 90 days without a sale, which is why dead stock is usually discovered at stocktake, months after it stopped moving.

Permalink: https://blog.dugong.live/how-to-automatically-clear-dead-stock-on-shopify.html#faq-1

### Can Shopify automatically discount slow moving inventory?

Not natively. The bulk editor changes prices by hand, discounts target products and collections rather than sales velocity, and Shopify Flow has no trigger and no product field for time since last sale, so there is nothing to build the rule on. Automatic markdown apps exist and hold a threshold like 90 days then 20 percent off, which works until the exception list grows: brands that must never be discounted, margin floors that differ by category, products that are seasonal rather than dead, and markdowns that need compare-at prices handled cleanly and an end date attached. Whatever runs your markdowns also needs to keep stacking in check, because discount codes still apply on top of lowered prices unless you guard against it, and it should put prices back when a product starts selling again. That full loop, detect, decide, mark down, watch, and revert, is an automation job rather than a setting.

Permalink: https://blog.dugong.live/how-to-automatically-clear-dead-stock-on-shopify.html#faq-2

### Can I create a Shopify collection of products that have not sold in 90 days?

Not with smart collection conditions. They match on things like title, type, vendor, price, tag, weight, and stock level, and none of them can see sales data, so a collection defined as has not sold in 90 days is impossible to express natively. It is the same gap that keeps new arrivals collections running on hand-applied tags. The working pattern is to let an automation compute last sold per product on a schedule, apply a tag such as aging-90 when a product crosses the line, and remove the tag if the product sells again. A smart collection keyed on that tag then stays current on its own, and it can drive both an outlet page on the storefront and internal saved views. The tag becomes the hook for everything downstream: markdowns, demotion in full-price collections, paused ads, and the weekly count of cash sitting in aged stock.

Permalink: https://blog.dugong.live/how-to-automatically-clear-dead-stock-on-shopify.html#faq-3

### How much does it cost to keep dead stock?

The standard estimate puts carrying cost at 25 to 30 percent of the inventory's value per year once storage, insurance, shrink, and the cost of the tied-up cash are counted, so the $9,300 of unsold shorts is not sitting still; it is quietly invoicing a couple of hundred dollars a month for the privilege of keeping the mistake, plus the 3PL storage line that arrives for the same units a fourth straight month. The bigger cost is the decay of options. Flagged at 60 days, an overbuy marks down 20 percent while the season is alive. Found at the fall stocktake, the choices left are 60 percent off in a January sale, bundling below cost, or a write-off. Meanwhile the ad account keeps paying full acquisition cost for products that died in June, and the next purchase order quietly reorders one of them.

Permalink: https://blog.dugong.live/how-to-automatically-clear-dead-stock-on-shopify.html#faq-4

### What should I do with dead stock besides discounting it?

Fit the move to the product, because a markdown is only the move everyone remembers at 11 p.m. on inventory weekend. Slow candles ride along as a gift with purchase that lifts the average order instead of cutting a price. A size run broken down to XS and XXL will never move at any discount and wants a bundle with its bestselling siblings or a spot in the outlet collection, not a price cut that insults the margin without shifting a unit. A product that died on your store but sells steadily wholesale wants a line on the next trade order. Guardrails hold it honest: nothing drops below 15 points of margin without a human saying so, a move that shows no lift in two weeks escalates to a deeper cut or a different move, and a product that wakes up gets its price back.

Permalink: https://blog.dugong.live/how-to-automatically-clear-dead-stock-on-shopify.html#faq-5

---

Markdown rendition of https://blog.dugong.live/how-to-automatically-clear-dead-stock-on-shopify.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
