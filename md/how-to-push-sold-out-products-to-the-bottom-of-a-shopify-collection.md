# How to push sold-out products to the bottom of a Shopify collection

> Shopify can't reliably push sold-out products to the bottom of a collection, so dead tiles greet your best traffic. The AI playbook that fixes it.

- Canonical: https://blog.dugong.live/how-to-push-sold-out-products-to-the-bottom-of-a-shopify-collection.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-06-13
- Updated: 2026-08-16
- Section: Research
- Word count: 2130
- Dispatch: Nº 57 · Research · 9 min read
- Full headline on page: How to push *sold-out products* to the bottom of a Shopify collection
- Keywords: Shopify hide out of stock products, sort out of stock to bottom, out of stock collection sort, push down sold out products, Shopify merchandising automation, collection page conversion, hide sold out products, out of stock down sort
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

Spend an evening in the Shopify community forums or the merchant subreddits and one request comes up again and again, often with years of replies stacked under it. How do I stop sold-out products from sitting at the top of my collection pages? People assume there is a setting that quietly slides the empty shelves to the back. There is not, or at least not one that holds. The thread always ends the same way: a moderator suggests dragging the products by hand, someone replies that they run a hundred collections with thousands of products, and a third person recommends paying for an app. The frustration is not that the fix is hard. It is that the storefront is working against the store, and Shopify treats fixing it as a manual chore.

Here is why it is expensive. A collection page is your best salesperson. It is the first real screen a browsing customer sees after they click in from search or an ad, and the products at the top of it carry more weight than anything else on the site. When the first three tiles are grayed-out sold-out badges, you have told a ready buyer, in the most valuable real estate you own, that you are out of what they came for. Most of them will not patiently scroll to the in-stock product further down. They read the top row, decide the store is picked over, and go somewhere else.

> A sold-out product at the top of a collection is a closed sign hung over everything *in stock* behind it.

## How big the leak actually is

Out-of-stock products are not a small cosmetic problem. Stockouts account for roughly forty percent of lost sales, and when shoppers cannot find or buy what they came for, nearly seven in ten leave without buying anything at all, frequently straight to a competitor. Researchers who study conversion increasingly call product availability the single largest controllable factor in whether a visit turns into a sale, ahead of pricing, copy, or checkout friction. The empty shelf does not just lose its own sale. It poisons the visit.

And the empty shelves are not rare. Around fifty one percent of products hit at least one stockout in a year and stay unavailable for an average of about thirty five days, while the typical out-of-stock rate across a store sits near eight percent and climbs to roughly ten percent on the promotional items that draw the most traffic. So at any given moment about one tile in twelve is a dead end, and on a sale day, when traffic is highest and stock moves fastest, it is worse. The exact products you pushed hardest to drive visits are the ones most likely to be greeting those visitors sold out.

## What Shopify actually does, and where it stops

Shopify is precise about the thing next to this and silent on the thing itself. It tracks inventory to the unit and knows the instant a variant crosses to zero. What it does not do is act on that knowledge to re-merchandise the storefront. The gap shows up in three concrete ways that the forum threads circle around.

First, **there is no reliable sort by stock**. Shopify offers no true sort that pushes out-of-stock products to the end of a whole collection. Some sort options and a bit of theme code can push sold-out tiles down within a single page, but the moment pagination kicks in, each page sorts itself in isolation. Page one ends up a healthy mix while page three is a wall of sold-out, which is exactly backwards. Shopify's [Liquid](https://shopify.dev/docs/api/liquid) sort filter has no inventory quantity parameter, so a theme cannot sort cleanly across the full collection either. That leaves dragging products by hand in a manual sort, which no store with a real catalog can keep up with.

Second, **hiding is all or nothing**. You can add an inventory condition to an automated collection so sold-out products drop out of it entirely. For some stores that is acceptable, but it removes the product instead of demoting it, which throws away the page's search ranking and the back-in-stock signup that lives on it, and it leans on the rule to re-publish the moment stock returns. You have traded a visible dead tile for an invisible one, along with its SEO.

Third, **search and manual collections are left out**. The inventory condition only applies to automated collections. It does not touch site search, and it does not touch the manual, hand-curated collections where merchandising matters most, the seasonal edit, the homepage feature, the bestsellers row. The two surfaces a merchant cares about most are the two the native tools ignore.

> **◆ DATA** The arithmetic is unforgiving. Stockouts cause roughly **40% of lost sales**, about **69% of shoppers** leave without buying when they cannot find what they came for, and a sold-out product sits dark for around **35 days** on average. A dead tile at the top of a collection does not just lose its own sale, it drags down the conversion of every in-stock product sitting behind it.

## Why the usual fixes don't hold

Once a store feels the leak, merchants reach for three coping strategies. Each helps for a while and each breaks in a predictable place.

**"I'll reorder the collections by hand."** This works for a shop with five small collections and falls apart everywhere else. Stock changes by the hour, so a manual sort is stale by lunch, and a catalog with dozens of overlapping collections turns the chore into a full-time job that is never actually finished. The stores that need it most, the big fast-moving ones, are precisely the ones where hand-sorting is hopeless.

**"I'll hide them with a smart-collection rule."** Hiding buys a cleaner page at a real cost. The product's URL goes dark, so the ranking and the links you earned for it evaporate, and the customer who would have clicked notify me when this is back never gets the chance, because the page is gone. When it restocks you are trusting the rule to bring it back at the right moment, and none of it covers search or your manual collections anyway.

**An app or a snippet of theme code.** Liquid cannot sort by inventory, so theme code can only fake it page by page. A dedicated app can sort and hide more capably, but it arrives with its author's idea of how merchandising should work, wrapped in a settings page and a fee that often scales with your catalog size. What it usually cannot express is the nuance every real store has: bury the sold-out items but keep the bestseller pinned to the top even when it is low, hide from search but not from the edit I hand-picked, badge the ones coming back this week instead of burying them. Those are the decisions that matter, and they are the ones a fixed app cannot hold.

## What the automation actually has to do

The real job is not "hide sold-out products." It is "watch real inventory across every surface, and present each collection the way a careful store manager would, demote the dead tiles instead of letting them lead, keep the ones returning this week visible with an honest badge, never bury a product you rank for, treat search differently from a curated edit, and put everything back the instant stock returns." That is judgment applied continuously, not a one-time sort. As a Dugong playbook, in plain prose, it reads like this:

```
# trigger
When a product's available count crosses zero in either
direction, on any collection or search surface

# steps
1. Find every collection and search result where the
   product currently shows
2. If it just sold out → move it below the in-stock
   items, not off the page, and keep its URL and notify-me form alive
3. If it's restocking within the week → keep it visible
   with a back-soon badge instead of burying it
4. Protect the hero and high-ranking products → never
   bury a page I rank for; flag it for me instead
5. Apply per surface: demote on browse pages, drop from
   search, leave my hand-curated edits to my rules
6. When it restocks → restore its original position
   automatically
7. If a whole collection goes mostly empty →
   tell me, don't quietly serve a wall of sold-out
```

Seven lines. The compiler fills in everything beneath them: subscribing to the inventory change across collections and search, re-sorting without breaking pagination, keeping the URL and the waitlist intact instead of deleting the page, badging the items that are genuinely coming back soon, exempting the products the store ranks for, and restoring every position the moment stock lands. The merchant never reordered a collection by hand. They described how a good store presents itself and let the compiler keep the storefront honest minute to minute.

> **◆ NOTE** Hiding is not always the answer. Yanking every sold-out product off the page can cost you more than the dead tile did, because you lose the ranking and the back-in-stock capture along with it. The **judgment** is the value: what to demote, what to hide from search, what to keep up front with an honest back-soon badge, and what to protect because you earned its place on page one of Google.

## Why this is a compiler problem, not an app problem

There are capable merchandising apps in the Shopify ecosystem, and for plenty of stores they are worth installing. But an app hands you its author's opinion of how a storefront should behave, expressed as toggles and a monthly fee that frequently grows with your catalog. What most merchants actually want is to encode *their* rules: demote sold-out items on browse pages but keep the signature product pinned, drop empty shelves from search yet leave my hand-built new-arrivals edit exactly as I arranged it, badge anything restocking inside seven days, and never, under any rule, bury a product that ranks on the first page of search. Those are sentences about how a specific store sells, not switches in a panel.

A natural-language compiler is the unlock because this was never really a sort problem. It was a *merchandising and timing* problem wearing a sort problem's clothes. The sort itself is the easy part, which is exactly why every theme ships a half-working version of it. The hard part is the judgment and the freshness: knowing what is truly out, what is coming back and when, what you rank for and must protect, and keeping all of that current across every collection and the search box as stock moves through the day. You can write that brief in a paragraph. You could never maintain it as a rule tree with a branch for every collection, product, and restock.

## The workflow worth building this week

If you carry a catalog that sells out and comes back, this is the merchandising automation to build before your next sale, because it protects the conversion of everything that *is* in stock. It sits right next to two pains we have written about. It depends on the same honest counts as [the overselling problem no one automates](https://blog.dugong.live/how-to-prevent-overselling-on-shopify-across-channels.html): a storefront can only demote what it is truly out of if the inventory number is real, so the store that keeps its counts honest is the one that can trust its own merchandising. And it pairs with [the restock alert that never fires](https://blog.dugong.live/how-to-set-up-back-in-stock-notifications-on-shopify.html): demote the sold-out tile for the browsers, capture the waitlist on the page you kept alive, and notify those people in fair order when it returns. Together they turn a stockout from a leak into a loop.

Describe it the way you would brief a sharp merchandiser on day one: here is what to bury, here is what to badge, here is what to protect, here is how search is different, and here is when to restore. That is the whole brief. The compiler does the watching and the re-sorting across every surface, minute to minute. You keep your attention for the collections that need a human eye, and you stop letting empty shelves greet your best traffic.

> **◆ READING** If this resonates, two companion pieces: the dispatch on [the overselling problem no one automates](https://blog.dugong.live/how-to-prevent-overselling-on-shopify-across-channels.html), the inventory pain that decides whether your storefront can trust its own counts, and [the restock alert that never fires](https://blog.dugong.live/how-to-set-up-back-in-stock-notifications-on-shopify.html), the demand-recovery loop that lives on the page you chose not to delete. Both sit inside the broader field study on [the Shopify automations no one builds](https://blog.dugong.live/best-shopify-automations-to-set-up.html).

If you are a Shopify merchant who has wired up a storefront that re-merchandises itself as stock moves, or you have watched a hero collection greet shoppers with a wall of sold-out during your biggest sale day, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Can Shopify automatically move out-of-stock products to the bottom of a collection?

Not reliably. Shopify has no true sort-by-stock that pushes sold-out items to the end of a whole collection. Some sort options and theme code can push out-of-stock down within a single page, but once pagination kicks in each page sorts itself, so a later page can be all sold-out while the first page is mixed. Shopify's Liquid sort filter has no inventory quantity parameter, so theme code cannot sort cleanly across the collection either. The only native, reliable option is dragging products by hand in a manual sort, which does not scale past a few small collections.

Permalink: https://blog.dugong.live/how-to-push-sold-out-products-to-the-bottom-of-a-shopify-collection.html#faq-1

### Why not just hide sold-out products with a smart collection rule?

You can add an inventory stock is greater than zero condition to an automated collection so sold-out products drop out, and for some stores that is fine. But it only works on automated collections, not manual ones, and it does not apply to site search. It also removes the product entirely, which throws away the page's SEO and the back-in-stock signup that sits on it, and you have to trust the rule to re-publish the product on restock. For most stores, burying the product with an honest badge is better than hiding it outright.

Permalink: https://blog.dugong.live/how-to-push-sold-out-products-to-the-bottom-of-a-shopify-collection.html#faq-2

### How much do out-of-stock products on a collection page actually cost?

More than the missing sale itself. Stockouts account for roughly 40 percent of lost sales, and when shoppers cannot find or buy what they came for, nearly 7 in 10 leave without buying anything, often for a competitor. Around 51 percent of products hit at least one stockout a year and stay unavailable for about 35 days on average, while the typical out-of-stock rate sits near 8 percent and climbs to about 10 percent on promotional items. A dead tile at the top of a collection does not just lose its own sale, it drags down the conversion of every in-stock product behind it.

Permalink: https://blog.dugong.live/how-to-push-sold-out-products-to-the-bottom-of-a-shopify-collection.html#faq-3

### What should happen when a sold-out Shopify product comes back in stock?

Its original position should come back with it, automatically. The restock is where the two coping strategies quietly fail: a hand-sorted collection stays stale until someone remembers to drag the product back up, and a smart-collection hiding rule has to re-publish the page at exactly the right moment on its own. Demotion handles the return cleanly because the product never left. The URL stayed live, so its search ranking survived, and the notify-me form stayed on the page, so the waitlist kept growing while the shelf was empty. A product genuinely restocking within the week deserves different handling again: keep it visible with an honest back-soon badge instead of burying it, because a shopper who can see it is coming back may wait, where an empty gap sends them to a competitor. Restoring positions on restock is the half of re-merchandising the manual approaches never get to.

Permalink: https://blog.dugong.live/how-to-push-sold-out-products-to-the-bottom-of-a-shopify-collection.html#faq-4

### Should sold-out products be handled the same way in search and in collections?

No, each surface deserves its own rule. On browse pages, demote the sold-out tile below the in-stock items but keep it on the page with its URL and notify-me form alive. In site search, drop it, because a shopper who typed a query is further along than a browser and a dead result wastes the click. In hand-curated edits, the seasonal feature or the bestsellers row, leave the merchant's arrangement alone and flag rather than reorder. And some products should never be buried anywhere: a page that ranks on the first page of Google earned its position and draws traffic regardless of stock, so protect the hero products and alert a human instead of demoting them. If a whole collection goes mostly empty, the right move is not sorting at all but a warning, so you never quietly serve a wall of sold-out tiles to your best traffic.

Permalink: https://blog.dugong.live/how-to-push-sold-out-products-to-the-bottom-of-a-shopify-collection.html#faq-5

---

Markdown rendition of https://blog.dugong.live/how-to-push-sold-out-products-to-the-bottom-of-a-shopify-collection.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
