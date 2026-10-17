# How to set inventory reorder points on Shopify

> Shopify's purchase orders are too basic to reorder for you, so bestsellers sell out while cash sits in slow movers. The AI playbook that reorders on time.

- Canonical: https://blog.dugong.live/how-to-set-inventory-reorder-points-on-shopify.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-06-15
- Updated: 2026-08-10
- Section: Research
- Word count: 2130
- Dispatch: Nº 59 · Research · 9 min read
- Full headline on page: How to set *inventory reorder points* on Shopify
- Keywords: Shopify purchase order automation, reorder point, inventory replenishment, demand forecasting, stockout prevention, low stock alert, supplier purchase orders, reorder automation
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

Read enough Shopify community threads and the same frustration surfaces in a different costume every week. Merchants want the store to reorder for them. They have watched a bestseller sell out three times this quarter, they know roughly how fast it moves, they know which supplier makes it, and they cannot understand why the platform that tracks every unit will not just tell them to buy more before it runs out. The answer they get is always some version of the same thing. Shopify counts your stock. It does not plan your stock. There is a purchase order screen, and merchants who find it usually come away calling it, in the exact words of one well-read forum thread, too basic.

That gap is easy to shrug off because it has no dramatic moment. A stockout on a hot product feels like an event. A reorder placed two weeks late feels like nothing at all, just a quiet stretch where the page said sold out and the customers went elsewhere. Nobody opens a support ticket about a purchase order that should have gone out on Tuesday. So the single most expensive operations decision in the store, how much of what to buy and when, gets made in the cracks of a busy week, on a spreadsheet that is always a little out of date.

> Shopify will count every unit you own. It will never tell you which one to *buy back*.

## How big the leak actually is

Running out of stock is not a rare accident, it is a constant background cost. Stockouts cost retailers on the order of one and a quarter trillion dollars a year in lost sales worldwide. At any given moment roughly eight percent of all SKUs are out of stock, about half of all products hit at least one stockout in a year, and the average stockout lasts around thirty five days from the first empty shelf to the day stock is back. That is more than a month per incident of a product page that converts a ready buyer into a shrug.

And the buyer does not wait. When a shopper finds an item unavailable, about forty three percent go straight to a competitor, and many of them do not come back. So a late reorder is not a delayed sale, it is usually a lost one, plus a small chip off the trust that brings people back. The reorder decision is where most of this is won or lost, because every one of those thirty five day gaps traces back to a purchase order that went out too late, or for too few units, or never went out at all.

## What Shopify actually does, and where it stops

Shopify is good at the half of this it owns and silent on the half that matters most. It tracks inventory per location, it knows the running count of every variant, and it gives you a purchase order screen where you can record what you are buying from a supplier and receive it against stock. What it does not do is decide. There is no native engine that reads your sales and your stock, works out what is about to run out, and drafts the order. The gap shows up in three concrete ways merchants run into fast.

First, **there is no reorder point that thinks per SKU**. Shopify has no native field that says reorder this variant when it drops to this level, let alone one that sets that level from how fast the item sells and how long its supplier takes. The closest thing is eyeballing a low-stock report. So the trigger to buy lives in a human's memory, and it fires whenever someone happens to scroll past the right row.

Second, **the purchase order itself is bare**. Merchants in the forums hit the same walls again and again: the PO does not auto-populate the product cost you already entered, so you retype prices you have on file; there is no native field to store the supplier's own SKU, so you cross-reference part numbers by hand; and there is no real reporting on what is on the way, what arrived partially, and what is still pending. The screen records a decision. It does not help you make one.

Third, **nothing connects the count to the calendar**. The number that matters for reordering is not how many you have, it is how many days you have left at the current pace, minus how many days the supplier needs to deliver. Shopify shows you the first number and knows nothing about the second. So even a diligent merchant is forced to do lead-time math in their head, per product, for a catalog that may run to hundreds of SKUs across more than one supplier.

> **◆ DATA** The leak is steady and large. Stockouts cost retailers roughly **$1.2 trillion** a year in lost sales worldwide, about **8% of SKUs** are out of stock at any moment, around **half of all products** hit at least one stockout a year, and the average stockout runs about **35 days**. When the shelf is empty, roughly **43% of shoppers** buy from a competitor instead. Almost all of it traces to a reorder made too late or too small.

## Why the usual fixes don't hold

Once a merchant feels the leak, they reach for one of three coping strategies. Each buys a little control and each breaks in a predictable spot.

**"I track reorders in a spreadsheet."** This is the honest default, and it works until the catalog grows or the week gets busy. The sheet is a snapshot the moment you build it and stale by the afternoon, it does not watch sales as they happen, and it cannot tell you that a slow mover just started trending until you go looking. The products that need the sharpest attention, the fast and the seasonal, are exactly the ones a static sheet gets wrong, because their pace is the thing that changed.

**"I set one reorder point for everything."** Pick a tidy rule like reorder anything that drops below ten units and you have bought too late for the bestseller with a six week lead time and far too early for the slow mover sitting on three months of cover. A flat threshold treats a product that sells forty a week and one that sells two the same way. The whole problem is that every SKU moves at its own speed and every supplier delivers on its own clock, which is the one thing a single number cannot capture.

**A [Shopify Flow](https://help.shopify.com/en/manual/shopify-flow) low-stock alert.** Flow can watch inventory and ping you when a variant crosses a level, which feels like progress. But an alert is not a plan. It still lands on a human who has to decide whether the dip is real demand or a blip, how many to buy given the lead time and the trend, whether to wait and bundle it with other items from the same supplier to clear a minimum, and then actually build and send the PO. The notification moves the work to your inbox. It does not do the work.

## What the automation actually has to do

The real job is not "alert me when stock is low." It is "watch how each product is actually selling, know how long each supplier takes, and put a right-sized purchase order in front of me before anything runs out, grouped so it is worth sending." That means forecasting, lead-time math, and a little judgment about cash and minimums. As a Dugong playbook, in plain prose, it reads like this:

```
# trigger
Every morning, and whenever a product's sales pace
shifts sharply

# steps
1. Project days of cover left for each SKU from its
   recent sales pace, trend, and any seasonality
2. Subtract that supplier's real lead time to find
   the date each item must be reordered by
3. Size the order to cover demand through the next
   cycle, not a flat number, and not so much that cash sits idle
4. Group the items by supplier so each PO clears the
   order minimum instead of shipping in dribs
5. Draft the purchase order with the right cost,
   supplier SKU, and quantities filled in
6. Flag anything unusual: a sudden spike, a stockout
   already imminent, a price that moved
7. Hand me the drafted POs to approve, and only send
   on my okay
```

Seven lines. The compiler fills in everything underneath: pulling the sales history per variant, fitting a demand curve that respects trend and season, storing each supplier's lead time and minimum, doing the days-of-cover-minus-lead-time math for every SKU, batching the buys by vendor, and pre-filling the order with the cost and part number Shopify makes you retype. The merchant never built a rule per product. They described how a careful inventory planner works, and let the compiler do the watching and the arithmetic.

> **◆ NOTE** Reordering late is only half the cost. **Reordering too much** is the same mistake pointed the other way: buy a year of a slow mover and the cash that should have restocked your bestseller is frozen on a shelf, racking up storage and inviting a markdown. The goal is not "never run out," it is the right quantity at the right time, which is exactly the balance a flat rule and a stale spreadsheet cannot strike.

## Why this is a compiler problem, not an app problem

There are capable inventory-planning apps in the Shopify ecosystem, and for many stores they earn their fee. But an app ships with its author's idea of how to forecast and reorder, wrapped in a settings page and a monthly bill that often climbs with your SKU count. What most merchants actually want is to encode *their* rules: this supplier needs six weeks so reorder early, never go below two weeks of cover on the hero product, hold small buys until the vendor minimum is met, treat the pre-order SKUs differently, ignore the one-off bundle that spiked last week, and always let me approve a purchase order over a certain value. Those are sentences about your business, not toggles in someone else's UI.

A natural-language compiler is the unlock because replenishment was never really a button problem. It is a *forecasting and timing* problem wearing a data-entry problem's clothes. Recording a purchase order is the easy part, which is why Shopify can do it. The hard part is everything before: read the demand, respect each supplier's clock, size the buy against both stockouts and idle cash, group it to clear a minimum, and know which orders are routine and which need your eyes. You can write that brief in a paragraph. You could never maintain it as a rule tree with a branch for every SKU, season, and supplier.

## The workflow worth building this week

If you sell physical products that you restock from suppliers, this is the automation to build before the next sale or new launch, because it protects revenue you have already proven you can earn. It sits right next to two pains we have written about already. Reorder timing is the upstream cause of [the restock alert that never fires](https://blog.dugong.live/how-to-set-up-back-in-stock-notifications-on-shopify.html): get the purchase order out on time and far fewer customers ever land on a sold-out page in the first place. And it depends on the same honest counts as [the overselling problem no one automates](https://blog.dugong.live/how-to-prevent-overselling-on-shopify-across-channels.html), because a forecast built on a number that is wrong will reorder the wrong amount with confidence.

Describe it the way you would brief a sharp inventory planner on day one: here is how fast each thing sells, here is how long each supplier takes, here is how much cushion I want, here is how to group the buys, and here is the line above which I want to approve before anything sends. That is the whole brief. The compiler does the forecasting, the lead-time math, and the drafting. You keep your attention for the calls that need a human, and you stop discovering your bestseller is gone the same way your customers do.

> **◆ READING** If this resonates, two companion pieces: our field study on [the Shopify automations no one builds](https://blog.dugong.live/best-shopify-automations-to-set-up.html) (where the planning work that scales with the business is a sliver of what merchants automate, despite paying back the most), and the dispatch on [the overselling problem no one automates](https://blog.dugong.live/how-to-prevent-overselling-on-shopify-across-channels.html), the inventory accuracy that decides whether your reorder math can be trusted at all.

If you are a Shopify merchant who has built a replenishment flow that actually keeps the shelves full, or you have a bestseller that went dark for a month because the reorder slipped and it still stings, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Can Shopify reorder stock from suppliers automatically?

No. Shopify tracks inventory and will let you create a purchase order by hand, but it has no native automation that reads your sales and stock, decides what to reorder and how much, and generates the PO for you. The native purchase order is also basic: there is no per-SKU reorder point, it does not auto-populate the product cost you already entered, there is no native field for the supplier's own SKU, and there is no reporting that shows what is on the way or partially received. Merchants who want real replenishment either reorder from a spreadsheet by hand or bolt on a third-party inventory app.

Permalink: https://blog.dugong.live/how-to-set-inventory-reorder-points-on-shopify.html#faq-1

### Why is one reorder point for the whole catalog a bad idea?

Because every product moves at a different speed and every supplier takes a different amount of time to deliver. A flat rule like reorder when stock hits ten units buys far too late for a bestseller with a six week lead time, and far too early for a slow mover that will take three months to sell what you already have. The right reorder point is per SKU and is a function of how fast that item sells, how that pace is trending, and how long that specific supplier takes to ship, which is exactly the calculation a flat threshold cannot do.

Permalink: https://blog.dugong.live/how-to-set-inventory-reorder-points-on-shopify.html#faq-2

### How much do stockouts and overordering actually cost?

Stockouts cost retailers on the order of 1.2 trillion dollars a year in lost sales worldwide. About 8 percent of SKUs are out of stock at any given moment, roughly half of all products hit at least one stockout a year, and the average stockout lasts around 35 days from the first empty shelf to full replenishment. When a customer finds an item unavailable, about 43 percent go straight to a competitor. The mirror cost is overordering: buy too much and the cash is frozen in stock that sells slowly, plus storage and the risk of markdowns. Reordering too late and reordering too much are the same planning failure pointed in opposite directions.

Permalink: https://blog.dugong.live/how-to-set-inventory-reorder-points-on-shopify.html#faq-3

### How do I calculate a reorder point for a Shopify product?

Work in days, not units. The number that matters is days of cover: how many days of stock remain at the product's current sales pace, adjusted for trend and seasonality, minus the supplier's real lead time. When cover minus lead time reaches zero, the reorder date has arrived, whatever the unit count says. A flat threshold like reorder below ten units gets both directions wrong, too late for a bestseller with a six week lead time and too early for a slow mover holding three months of cover. Size the order to carry demand through the next cycle rather than to a round number, and hold small buys until the supplier's order minimum is met by grouping SKUs from the same vendor into one purchase order. Shopify shows the count per location and knows nothing about the calendar, so the pace and lead-time math is the part you have to add.

Permalink: https://blog.dugong.live/how-to-set-inventory-reorder-points-on-shopify.html#faq-4

### Is a Shopify Flow low-stock alert enough to manage reordering?

An alert is not a plan. Flow can watch a variant and ping you when the count crosses a level, and then the entire decision still lands on a human: is the dip real demand or a blip, how many units to buy given the lead time and the trend, whether to hold the buy until other items from the same supplier clear the order minimum, and then building the purchase order itself. The PO screen makes that last step slower than it sounds, because it does not auto-populate the product cost you already entered, has no field for the supplier's own SKU, and offers no real view of what is on the way or partially received. The notification moves the work to your inbox without doing any of it, which is the difference between an alert and a drafted, right-sized purchase order waiting for approval.

Permalink: https://blog.dugong.live/how-to-set-inventory-reorder-points-on-shopify.html#faq-5

---

Markdown rendition of https://blog.dugong.live/how-to-set-inventory-reorder-points-on-shopify.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
