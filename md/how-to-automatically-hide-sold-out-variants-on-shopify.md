# How to automatically hide sold-out variants on Shopify

> Shopify keeps sold-out variants in the dropdown with no native way to hide them. The AI playbook that hides them and brings each back the moment stock returns.

- Canonical: https://blog.dugong.live/how-to-automatically-hide-sold-out-variants-on-shopify.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-07-03
- Updated: 2026-10-27
- Section: Research
- Word count: 2401
- Dispatch: Nº 75 · Research · 9 min read
- Full headline on page: How to automatically *hide sold-out variants* on Shopify
- Keywords: Shopify hide sold out variants, hide out of stock variants Shopify, Shopify hide unavailable variants, hide sold out options Shopify, Shopify variant dropdown sold out, remove sold out sizes Shopify, hide out of stock variant automatically Shopify
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

Watch someone shop a product with sizes. They do not read the whole grid. They look for their size, tap it, and wait for the price and the Add to Cart button to confirm they can buy it. When the button instead says Sold Out, the message they take is not "this one size is out." It is "this product is not available," and they leave. The cruel part is that the two sizes on either side of theirs were in stock and ready to ship. Shopify just showed the shopper the one thing they could not have and let them draw the wrong conclusion.

This is one of the most-repeated requests in every Shopify merchant community, and the threads all read the same. "Hide specific variants when sold out." "Hide out of stock product variants." "How do I stop showing a size once it hits zero." Merchants are not asking for anything exotic. They want the obvious thing: when a variant is gone, take it off the page, and when it comes back, put it back. Shopify does not have a button for that, and the answers underneath the threads are always some mix of edit your theme code or install an app.

> The shopper looked for their size, found it, and it was gone. *The two sizes that were in stock never got a look, because Sold Out reads as the whole product being over.*

## The short answer

Shopify has no setting that hides a variant once it sells out. It holds the variant list as part of the product's structure rather than a live view of what is buyable now, so every size and color you created keeps rendering, marked Sold Out or Unavailable and often greyed out or struck through.

The two settings that look like they should help do not. Turning off continue selling when out of stock prevents the purchase and still leaves the variant on the page. The newer unlisted status hides a whole product rather than one variant, which is the wrong instrument the moment everything else on the product is still selling.

That leaves theme code or an app. A Liquid edit is tidy on a single option and genuinely fiddly once size and color combine, because a color is only truly gone when every size inside it is out, and the customization goes with the next theme update. Deleting the variant is worse, since the SKU history, the barcode and any *back-in-stock signup* pointing at it go too.

## Why Shopify keeps showing a variant you can't buy

Shopify treats the list of variants as part of the product's structure, not as a live view of what is buyable right now. Every size and color you created lives on the product as an option value, and the theme faithfully renders all of them whether they have stock or not. Selling out changes one thing only: whether that variant can be added to cart. It does not change whether the variant appears. So the grid you built when everything was in stock is the grid the shopper sees when half of it is gone, with the empty ones marked Sold Out or Unavailable and often grayed out or struck through.

There is a setting that looks like it should help and does not. Turning off **continue selling when out of stock** stops a shopper from buying a variant past zero, which is the right call for most stores, but it only disables the variant. It still shows. And Shopify's newer **unlisted** product status hides a whole product from the storefront, not a single variant, so it is the wrong tool the moment the rest of the product is still selling. There simply is no admin toggle that says hide this variant while it is out and restore it when it returns. The platform stores the variant as a fixed fact and leaves the display of it to the theme.

## What the "official" fix actually costs you

Go looking for how to hide sold-out variants and you land on two roads, both with a toll. The first is **editing the theme's [Liquid](https://shopify.dev/docs/api/liquid)**. You open the product template, find where the option values render, and wrap them in logic that skips a value when its inventory is zero. On a simple product with one option it is a tidy afternoon. The trouble starts with two options. Once size and color combine, "hide the sold-out ones" stops being a single check, because a color is only truly gone when every size in it is out, and hiding a value without breaking the selector for the combinations that remain is genuinely fiddly Liquid. And whatever you write is tied to this theme. Switch themes, or take a theme update, and the customization is gone or broken, and you are back in the code.

The second road is **a third-party app** that scans your catalog and hides or restyles sold-out variants for you. Good ones exist, and a store that lives with this pattern should look at one, which is itself proof the native gap is real. But an app is one more subscription, one more thing touching your theme, and it hides on a fixed rule: everything at zero, off. That rule cannot tell the difference between a size that is out until Friday and a color you are discontinuing, and it does not decide when hiding a variant would be a mistake. It just applies the switch.

> **◆ DATA** The reason this is worth fixing is that it hits the exact moment of intent. A shopper who selects a variant has already chosen, mentally, to buy. That is the highest-converting second on the whole page, and a Sold Out on their pick is the worst possible thing to show them, because it does not just lose that variant, it casts doubt on the product. They rarely go back and try another size. They read the page as unavailable and bounce. Every in-stock variant sitting behind a sold-out one is carrying a tax it did nothing to earn, and it is the size that sells best that goes out first.

## Why the usual fixes don't hold

Faced with the sold-out size on the page, merchants reach for a handful of moves. Each one gives something back that you did not want to lose.

**"I will just leave it showing as Sold Out."** The default, and the one quietly costing you the most. It looks harmless because nothing is broken, but every shopper who picks that size gets a dead end at the moment of intent, and a share of them decide the product is gone. You never see the lost sale. It shows up only as a conversion rate that is a little lower than it should be, on the products that sell best.

**"I will edit the theme to hide them."** The correct instinct, and the one that does not stay fixed. It works until size and color combine, until you change themes, until a theme update lands, or until a variant comes back in stock and nobody remembers to make sure the code lets it reappear. A hide that does not reliably un-hide is its own trap: now you have an in-stock size that no one can see and no one can buy.

**"I will unpublish the product until it is fully back."** This throws out the baby with the bathwater. One size out of stock takes the whole product off the storefront, so the four sizes that are in stock stop selling too. You have traded a small display problem for a real revenue one, and lost the page's search ranking while it is dark, the same [dead-URL problem](https://blog.dugong.live/how-to-fix-404-errors-from-deleted-products-on-shopify.html) that follows any product you pull without a plan.

**"I will delete the sold-out variant and re-add it later."** Now you are destroying data to change a display. Delete the variant and you lose its SKU history, its barcode, its cost, and any waitlist attached to it, and re-adding it later is manual and error-prone. It also silently breaks [the restock alert that never fires](https://blog.dugong.live/how-to-set-up-back-in-stock-notifications-on-shopify.html), because there is nothing left for a back-in-stock signup to point at.

## What the automation actually has to do

The real job is not "hide everything at zero." It is "watch each variant, decide whether a sold-out one should disappear or stay with a signup, hide it cleanly without touching the rest of the product, capture the demand you are hiding, and put it back the second stock returns, while pulling in a human for the calls that are actually merchandising decisions." That is detection, judgment, and a reversible action that has to run both ways. As a Dugong playbook, in plain prose, it reads like this:

```
# trigger
On a variant's available quantity crossing zero
   (or back above it), per size, color, and location

# steps
1. Read the variant: is it briefly out and restocking,
   or discontinued and gone for good
2. Hide the sold-out value from the storefront so it
   drops out of the dropdown or swatch, product still live
3. Collapse the whole option only if every value in it
   is gone, never leave an empty selector
4. Keep the demand: attach a back-in-stock signup to
   the hidden or unavailable variant
5. Restore the variant the moment inventory returns
   and notify the waitlist
6. Hold for review a discontinued line, a core size
   that keeps flickering, or a page left with nothing to buy
```

Six lines. The compiler fills in the rest: reading inventory per variant and per location rather than per product, telling a temporary stockout apart from a discontinuation so it hides the right ones, keeping the selector clean when only some values in an option are gone, holding the demand on a hidden variant instead of throwing it away, and reversing the whole thing automatically the instant a restock lands so an in-stock size is never left invisible. The merchant never opened the theme editor. They described how a sharp merchandiser would keep a product page honest, and let the compiler run it at the speed inventory actually moves.

> **◆ NOTE** The trap here is hiding on too blunt a rule. Not every sold-out variant should vanish. A popular size that is out until the weekend is usually better left visible with a back-in-stock capture, so you keep the waitlist instead of pretending the size never existed; a color that is discontinued is better hidden so it stops drawing dead-end clicks; and a product where hiding would leave nothing buyable should never be stripped to an empty page. Blind hiding loses demand and can black out a whole product; blind showing buries your best sellers behind dead options. Knowing which sold-out variant to hide, which to keep with a signup, and which to escalate is as much the point as the hiding itself.

## Why this is a compiler problem, not an app problem

There are decent variant-hiding apps on the Shopify App Store, and a store that sees this constantly should evaluate one. But the thing that makes hiding safe is not one more toggle. It is judgment about a specific variant at a specific moment: is this out for a week or gone for the season, does hiding it leave a clean selector or an empty one, is there demand worth capturing before it disappears, and would hiding this one leave the shopper with nothing to buy. Those answers change per variant, per product, and per day, which is exactly what a fixed rule handles badly and a person handles too slowly to keep up with a moving catalog.

A natural-language compiler fits because hiding a sold-out variant was never a single action. It is detection, a judgment call, a reversible change to the storefront, and a demand-capture step, and it has to run in both directions as stock moves in and out. You can describe the whole behavior in a paragraph. You could never keep up with it by hand across a catalog that changes hourly. It sits in the same family as [the sold-out products that sink your collection](https://blog.dugong.live/how-to-push-sold-out-products-to-the-bottom-of-a-shopify-collection.html), where the fix is to re-merchandise as stock moves rather than freeze the page, and [the overselling problem no one automates](https://blog.dugong.live/how-to-prevent-overselling-on-shopify-across-channels.html), where the same live inventory signal has to drive what the store does next.

## The workflow worth building this week

If your best-selling size is the first to go out, and it sits on the page as Sold Out for days while the sizes around it quietly under-convert, this is the automation to set up now, because the cost is invisible and continuous and lands on the products you can least afford to lose. It pairs naturally with the inventory and merchandising work we have written about, like [the restock alert that never fires](https://blog.dugong.live/how-to-set-up-back-in-stock-notifications-on-shopify.html), which captures the demand on a hidden variant, and [the reorder you always make too late](https://blog.dugong.live/how-to-set-inventory-reorder-points-on-shopify.html), which keeps the size from going out in the first place, and it feeds the same flywheel as [the Shopify automations no one builds](https://blog.dugong.live/best-shopify-automations-to-set-up.html), where the work that compounds is the part merchants never get to.

Describe it the way you would brief a sharp merchandiser: when a variant sells out, decide whether to hide it or keep it with a back-in-stock signup, take it off the page cleanly without touching the sizes still in stock, hold onto the demand, and put it straight back the moment it returns, and bring me anything that is really a merchandising call. That is the whole brief. The compiler does the watching, the judgment, the hide, the capture, and the restore. Your in-stock sizes stop carrying a dead one, and the shopper who came for a size that is gone still sees a page full of ones they can buy.

> **◆ READING** If this resonates, two companion pieces: our dispatch on [the restock alert that never fires](https://blog.dugong.live/how-to-set-up-back-in-stock-notifications-on-shopify.html), where a hidden variant's demand becomes recovered revenue, and [the sold-out products that sink your collection](https://blog.dugong.live/how-to-push-sold-out-products-to-the-bottom-of-a-shopify-collection.html), where the same stock signal has to re-merchandise the page as inventory moves.

If you are a Shopify merchant who has built something that hides sold-out variants and reliably brings them back, or you have a story about the best-selling size that sat on the page as Sold Out and dragged the whole product down, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Can Shopify hide out-of-stock variants automatically?

Not with a built-in setting. Shopify has no native switch that hides a variant when it sells out. Turning off continue selling when out of stock stops the shopper from buying the variant, but the variant still appears on the product page, usually shown as Sold Out or Unavailable and often grayed out or crossed off. To actually hide it you either edit your theme's Liquid code so the option value stops rendering when its inventory is zero, or you install a third-party app that hides and restores variants for you. There is no toggle in admin that does it.

Permalink: https://blog.dugong.live/how-to-automatically-hide-sold-out-variants-on-shopify.html#faq-1

### Why does Shopify still show a variant I marked as sold out?

Because Shopify treats the variant list as part of the product's structure, not as a live view of what is buyable right now. Every size and color you created stays on the product as an option value regardless of its stock level, and the theme renders all of them. Marking a variant sold out only changes whether it can be added to cart, not whether it appears. So a shopper sees the full grid of sizes, selects the one they want, and only then learns it is gone, which reads as the product being unavailable rather than one size being out.

Permalink: https://blog.dugong.live/how-to-automatically-hide-sold-out-variants-on-shopify.html#faq-2

### Should you hide sold-out variants or just show them as unavailable?

It depends on the case, which is exactly why a fixed rule struggles. A size that is briefly out and restocking next week is often better shown as unavailable with a back-in-stock signup, so you capture the demand instead of pretending the size never existed. A size that is discontinued, or a color that is gone for the season, is usually better hidden so it stops drawing clicks that dead-end. Hiding everything blindly loses waitlist demand, and showing everything blindly buries your in-stock options behind dead ones. The right move is per variant and changes over time, so the useful thing is judgment about which sold-out variants to hide, which to keep with a signup, and which to bring straight back when stock returns.

Permalink: https://blog.dugong.live/how-to-automatically-hide-sold-out-variants-on-shopify.html#faq-3

### Should I delete a sold-out variant to hide it on Shopify?

No. Deleting destroys data to change a display. The variant's SKU history, barcode, cost, and any waitlist attached to it all go with it, and re-adding the variant when stock returns is manual and error-prone. Deletion also breaks back-in-stock alerts, because there is nothing left for a signup to point at, so the demand you most wanted to keep is the demand you threw away. Unpublishing the whole product is the other tempting shortcut and costs even more: one missing size takes every in-stock size off the storefront with it, and the page's search ranking goes dark while it is down. The right move is a display-level hide that leaves the variant and its data intact, keeps the product live, collapses an option only when every value in it is gone, and reverses itself the moment inventory returns.

Permalink: https://blog.dugong.live/how-to-automatically-hide-sold-out-variants-on-shopify.html#faq-4

### Will a hidden sold-out variant come back on its own when restocked?

Not with the usual fixes, and that is where they quietly cost the most. A Liquid edit that skips zero-stock values only reverses if the code still works when stock returns: switch themes or take a theme update and the customization is gone or broken, and nobody remembers to confirm that a restocked size actually reappeared. A hide that does not reliably un-hide is its own trap, an in-stock variant no shopper can see or buy, which is worse than the Sold Out label ever was. A real automation runs in both directions off the same signal: it watches available quantity per variant and per location, hides on the cross to zero, then restores the variant the moment inventory returns and notifies the waitlist that accumulated while it was gone. The restore is not a nice-to-have. It is half the job.

Permalink: https://blog.dugong.live/how-to-automatically-hide-sold-out-variants-on-shopify.html#faq-5

---

Markdown rendition of https://blog.dugong.live/how-to-automatically-hide-sold-out-variants-on-shopify.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
