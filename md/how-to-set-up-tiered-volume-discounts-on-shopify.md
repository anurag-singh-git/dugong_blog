# How to set up tiered volume discounts (buy more, save more) on Shopify

> Shopify discounts allow one tier each, so buy more save more never works natively. The AI playbook that runs real quantity breaks across your whole catalog.

- Canonical: https://blog.dugong.live/how-to-set-up-tiered-volume-discounts-on-shopify.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-07-16
- Updated: 2026-10-25
- Section: Research
- Word count: 2215
- Dispatch: Nº 84 · Research · 10 min read
- Full headline on page: How to set up tiered *volume discounts* (buy more, save more) on Shopify
- Keywords: Shopify tiered discount, Shopify volume discount, Shopify buy more save more, Shopify quantity break discount, Shopify tiered pricing not working, Shopify multiple discount tiers, bulk discount Shopify, Shopify quantity discount native
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

Every merchant who sells anything people buy in multiples reaches for the same lever eventually. Coffee, candles, socks, supplements, wholesale anything: the way to lift the average order is to reward the bigger basket. Buy three, save a little. Buy six, save more. Buy a case, save the most. It is the oldest pricing move there is, and shoppers understand it on sight. So you go into Shopify to build it, and you discover the platform will let you build exactly one rung of the ladder.

This is one of the most-repeated frustrations in the Shopify community, and the threads say it plainly. "Tiered discounts based on variant quantity." "Tiered buy X get Y discount?" "How do I do buy more save more without an app?" The answers are always some mix of the same three: it is not natively possible for regular customers, you can fake a single tier and hope, or you install an app. Merchants are not asking for anything exotic. They want a discount that gets deeper as the cart gets bigger, and Shopify's discount engine was built for simple, not for tiered.

## The short answer

Shopify's discount engine allows one condition per discount, so buy 3 save 10 is one rule and buy 6 save 20 is a second, separate one. There is no way to say step up to 20 at six and 30 at twelve inside a single offer, which is why a real buy-more-save-more ladder is not natively possible for regular shoppers. The simple single-tier case does work cleanly, with no code and no app.

Building three automatic discounts at once is where it breaks. A cart of twelve units qualifies for all three tiers, Shopify does not pick the best one and suppress the rest, so the shopper can land on the smallest saving or the discounts simply refuse to combine. There is also a hard cap of 25 active automatic discounts on the store, so one discount per tier per product runs out of room quickly.

True quantity tiers exist in exactly one place: attach quantity pricing to a B2B price list and it behaves like a proper ladder, but it reaches only customers assigned to a company profile, not tagged retail customers, not cart-total tiers, and not your open storefront. Shopify Scripts, the old fake, stopped running on June 30, 2026. Treat the tier table as the source of truth and resolve the *single highest* break each cart has actually earned.
## What Shopify actually does, and where it stops

Give the platform its due first. Shopify's native discounts are genuinely good at the simple case. You can create an automatic discount like "buy 3, get 10 percent off," and it applies cleanly at checkout with no code and no app. You can gate a discount to a collection, to a minimum quantity, or to a minimum spend. For a store that wants one straightforward promotion running at a time, the native tools do the job and do it well.

The wall is that each discount holds a single condition. "Buy 3 save 10" is one rule. "Buy 6 save 20" is a second, separate rule. Shopify gives you no way to say "and if they reach 6, step up to 20, and if they reach 12, step up to 30" inside one offer. So merchants try to fake it by creating three automatic discounts at once, and that is where it breaks: a cart with 12 units qualifies for all three tiers, Shopify does not pick the best one and suppress the rest, and the shopper can land on the smallest saving or the discounts simply refuse to combine. There is also a hard cap of 25 active automatic discounts on the store, so the "one discount per tier per product" approach runs out of room fast.

The one place Shopify does real quantity tiers is B2B. If you run a wholesale setup, you can attach quantity pricing to a price list, and it behaves like a proper ladder. But it applies only to customers who are assigned to a company profile in your B2B configuration. It does nothing for your open storefront, nothing for tagged retail customers, and nothing for a cart-total tier that a first-time visitor should see. So the one native feature that tiers correctly is walled off from almost everyone you would actually want to show it to.

> **◆ TIMELY** The old workaround is gone. For years, Shopify Plus merchants faked tiered cart pricing with **Shopify Scripts**, which stopped executing on **June 30, 2026**. Any store that ran buy-more-save-more logic through a Script now has a broken checkout and is being pushed toward [Shopify Functions](https://shopify.dev/docs/apps/build/functions) or a discount app built on them. If your tiers quietly stopped working in the last few weeks, this is almost certainly why.

> A volume discount is not one rule. It is a ladder, and Shopify only ever hands you a single rung.

## Why doing it by hand never keeps up

The by-hand version of tiers is a maze of overlapping automatic discounts and coupon codes, and it turns fragile the moment anything else is running. Say you build your three tiers as three discounts. Now you launch a [weekend sale](https://blog.dugong.live/how-to-schedule-a-sale-on-shopify.html) on the same collection. Does the volume tier stack on top of the sale price, or replace it? Now a newsletter code goes out. Does buy 12 plus the code push the item below your cost? Shopify's combination settings are coarse, so you are left toggling "combines with other discounts" and testing carts by hand, hoping you have not opened a hole that a sharp shopper drives a bulk order through at negative margin.

Then there is the judgment that a tier table can never hold on its own. Not every product can carry the same ladder, because margins differ, so a 30 percent top tier that is fine on a high-margin candle is a loss on a thin-margin electronic. A wholesale buyer and a retail shopper should not see the same breaks. A deep tier during a promotion window is a different decision from the same tier as a permanent price. None of this is a single subtract. It is a running set of rules with exceptions and floors, and it is exactly what a person loses the thread of across a catalog and a calendar of overlapping promotions.

## What the automation actually has to do

The real job is not "make a discount." It is "read a tier table, and on every cart pick the single correct break by quantity or spend, apply just that one, keep it from stacking past a floor, apply the right ladder to the right audience, and nudge the shopper toward the next rung, with the risky calls handed to a person." That is a resolver, a guardrail, and an escalation, running on every cart change. As a Dugong playbook, in plain prose, it reads like this:

```
# trigger
On any cart change for a product or collection
   that carries a volume tier

# steps
1. Read the tier table: the breaks, whether they key
   off units or cart spend, and the audience they apply to
2. Resolve the single highest tier this cart has
   actually earned
3. Apply only that tier, to the right lines or the
   whole cart, never a smaller one by accident
4. Guard stacking: enforce whether it can combine with
   a code or a live sale, and hold every tier above its margin floor
5. Show the shopper the next rung ("add 2 more to save
   20 percent") so the ladder does its own upselling
6. Hold for review a tier that crosses a floor, a
   code clash, or a new promo that overlaps an existing ladder
```

Six lines. The compiler fills in the rest: reading the tier table as intent rather than as a pile of competing discounts, choosing the one right break instead of letting three fight, doing the math per line or per cart depending on how the offer is written, enforcing the stacking rule you chose so a coupon and a volume break never quietly double up, holding each rung above the margin floor you set, and telling the cart how close it is to the next tier so the discount pulls the order up instead of sitting there invisible. The merchant never built twenty-five overlapping discounts. They described the ladder once and let the compiler run it on every cart.

> **◆ NOTE** The trap here is building tiers as separate discounts and hoping Shopify picks the best one. It does not. Treat the tier table as the source of truth and the applied discount as a *result* the automation computes on each cart, and the ladder is correct by construction: one break, the right one, every time. Whether a tier can stack with a code, whether it clears a margin floor, and whether wholesale sees a deeper ladder than retail are the judgment calls that matter as much as the percentages themselves.

## Why this is a compiler problem, not an app problem

There are capable volume-discount apps on the Shopify App Store, and a store losing average order value every day should evaluate one. But the thing that makes tiers safe is not one more grid of quantities and percentages. It is judgment about a specific cart at a specific moment: is this the best tier the cart earned, does applying it alongside the code that is also in the cart cross the floor, should this buyer see the wholesale ladder or the retail one, and does this new promotion overlap a tier that is already live. Those answers change per product, per audience, and per promotion window, which is exactly what a fixed rulebook handles badly and a person cannot hold across a busy catalog.

A natural-language compiler fits because a volume discount was never a single action. It is a resolver that reads intent, a guardrail that protects margin and stacking, and a nudge that upsells the next rung, all running on every cart as it changes. You can describe the whole behavior in a paragraph. You could never keep twenty-five overlapping discounts honest by hand. It sits in the same family as [the free gift that never lands in the cart](https://blog.dugong.live/how-to-automatically-add-a-free-gift-with-purchase-on-shopify.html), where a threshold has to change what the cart does rather than just lower a price, and [the minimum order Shopify won't enforce](https://blog.dugong.live/how-to-set-a-minimum-order-amount-on-shopify.html), where the cart itself has to carry a rule the platform leaves to you.

Picture a case-pack seller heading into a peak. You want buy 6 save 15 and buy 12 save 25 across a collection, but only on the items whose margin can carry it, not stacking with the launch code, and showing wholesale accounts a deeper rung. On the native setup that is a dozen automatic discounts, a combination-settings guessing game, and a Script that no longer runs. With the automation, it is one tier table with a floor and an audience rule: every cart gets the single right break, the code and the tier respect the floor, wholesale sees its own ladder, and the cart tells each shopper how close they are to the next saving. Same offer, none of the overlap, and no negative-margin surprise at the end of the week.

## The workflow worth building this week

If you sell anything in multiples, or you just lost a Script-based tier on June 30, this is the automation to set up now, because the cost of not having it is invisible: the bigger baskets you never earned, and the occasional oversold discount that quietly clears your margin. It pairs naturally with the pricing work we have written about, like [the price change you make one product at a time](https://blog.dugong.live/how-to-bulk-edit-product-prices-on-shopify.html), which keeps the list prices under the tiers honest, and [the sale you start by hand](https://blog.dugong.live/how-to-schedule-a-sale-on-shopify.html), which decides how a running promotion and a volume tier are allowed to meet. It feeds the same flywheel as [the Shopify automations no one builds](https://blog.dugong.live/best-shopify-automations-to-set-up.html), where the work that compounds is the part merchants never get to.

Describe it the way you would brief a careful merchandiser: here is the ladder, here is what it keys off, here is the floor it must never cross, here is who sees the deeper version, and never stack it past that floor. On every cart, give the shopper the best rung they have earned and tell them how to reach the next one, and bring me anything that would cross a line. That is the whole brief. The compiler does the reading, the resolving, the guarding, and the nudging. Your average order climbs, your margin holds, and buy more save more finally behaves the way shoppers already expect it to.

> **◆ READING** If this resonates, two companion pieces: our dispatch on [the free gift that never lands in the cart](https://blog.dugong.live/how-to-automatically-add-a-free-gift-with-purchase-on-shopify.html), where a threshold has to add to the cart rather than just discount it, and [the minimum order Shopify won't enforce](https://blog.dugong.live/how-to-set-a-minimum-order-amount-on-shopify.html), where the cart carries a rule the platform leaves entirely to you. Also worth reading: [the sale your stockists take too](https://blog.dugong.live/how-to-stop-shopify-b2b-prices-dropping-when-you-run-a-sale.html), on what a catalog percentage does to B2B pricing the moment a retail sale starts.

If you are a Shopify merchant who has built tiered volume pricing that survives codes, sales, and the Scripts sunset, or you have a story about the bulk discount that cleared your margin, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Can Shopify do tiered volume discounts natively?

Not as a real buy-more-save-more ladder for regular shoppers. Shopify's discount engine allows one condition per discount, so you can build a single tier like buy 3 and save 10 percent, but you cannot chain buy 3, buy 6, and buy 12 into one storefront offer that steps the saving up as the cart grows. The only native quantity pricing that behaves like true tiers is the B2B feature, and it applies only to customers who are assigned to a company profile in your B2B setup, not to tagged retail customers, not to cart-total tiers, and not to your general storefront. Shopify Scripts, the old way stores faked tiered cart logic, stopped running on June 30, 2026, so that route is closed too. Real tiers for everyone else come from Shopify Functions or an app.

Permalink: https://blog.dugong.live/how-to-set-up-tiered-volume-discounts-on-shopify.html#faq-1

### Why does my Shopify tiered discount only apply one tier?

Because each Shopify discount holds one rule, so when you create separate discounts for each break they compete instead of laddering. A cart that qualifies for buy 12 also qualifies for buy 3 and buy 6, and Shopify applies one automatic discount rather than picking the best tier and ignoring the rest, so the shopper can land on the smaller saving or the discounts refuse to combine at all. There is also a cap of 25 active automatic discounts, so building a tier per product this way runs out fast. To make tiers behave you need one piece of logic that reads the quantity or spend, chooses the correct single tier, and applies just that one, which is exactly what stacking separate discounts cannot do.

Permalink: https://blog.dugong.live/how-to-set-up-tiered-volume-discounts-on-shopify.html#faq-2

### What replaced Shopify Scripts for tiered pricing in 2026?

Shopify Scripts stopped executing on June 30, 2026, so any tiered cart pricing or buy-more-save-more logic that ran through Scripts now needs to move to Shopify Functions or a discount app built on them. Functions can express real tier logic, but it is developer work: you write, deploy, and maintain the code, and you own every edge case as your catalog and promotions change. That is why most merchants reach for an app or a compiler instead. The dependable approach is to keep the tier table as something you can read and change in plain language, and let the automation translate it into the correct per-line and per-cart behavior, rather than hard-coding one promotion at a time.

Permalink: https://blog.dugong.live/how-to-set-up-tiered-volume-discounts-on-shopify.html#faq-3

### Can I use Shopify's B2B quantity pricing for regular retail customers?

No, and it is the most frustrating almost-answer on the platform. Shopify's one native feature that tiers correctly is B2B quantity pricing: attach quantity breaks to a price list and it behaves like a proper ladder, stepping the price as the count climbs. But it applies only to customers assigned to a company profile in your B2B configuration. It does nothing for the open storefront, nothing for retail customers you have merely tagged as wholesale, and nothing for a cart-total tier a first-time visitor should be able to see and earn. So the buyers a buy-more-save-more ladder is designed to convert, the anonymous shopper deciding between three candles and six, are exactly the ones it cannot reach. For everyone outside a company profile you are back to stacking automatic discounts, with the tier-fighting and the 25-discount cap that come with that approach.

Permalink: https://blog.dugong.live/how-to-set-up-tiered-volume-discounts-on-shopify.html#faq-4

### How many automatic discounts can a Shopify store have active at once?

Twenty-five. That is the hard cap on active automatic discounts across the store, and it is the number that quietly kills the fake-a-ladder approach. Build buy 3, buy 6, and buy 12 as three separate automatic discounts and one product family's ladder has already consumed three slots; run different breaks for different collections and a modest catalog hits the ceiling fast, with the cap still needing to hold every other automatic promotion the store runs. Worse, the slots do not even buy correct behavior: a cart with 12 units qualifies for all three tiers at once, and Shopify does not pick the best break and suppress the rest, so the shopper can land on the smallest saving. A tier table resolved per cart inverts this. It consumes none of the 25 while it computes the single right break every time, which is why it is correct by construction.

Permalink: https://blog.dugong.live/how-to-set-up-tiered-volume-discounts-on-shopify.html#faq-5

---

Markdown rendition of https://blog.dugong.live/how-to-set-up-tiered-volume-discounts-on-shopify.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
