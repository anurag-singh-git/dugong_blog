# How to sync inventory between two Shopify stores

> Two Shopify stores cannot share a shelf: no native sync, drifting counts, the same last unit sold twice. The AI playbook that ends the double-sell for good.

- Canonical: https://blog.dugong.live/how-to-sync-inventory-between-two-shopify-stores.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-08-03
- Updated: 2026-10-24
- Section: Research
- Word count: 2500
- Dispatch: Nº 100 · Research · 9 min read
- Full headline on page: How to sync inventory between *two Shopify stores*
- Keywords: sync inventory between two Shopify stores, multiple Shopify stores same inventory, share inventory between Shopify stores, multi store inventory sync Shopify, two Shopify stores one warehouse, Shopify multi store sync, wholesale and retail Shopify stores shared inventory, Shopify oversell two stores
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

At 9:41 on a Saturday night, your retail store sells the last Meridian hoodie in medium. Forty seconds later, your wholesale store sells it again. Neither store did anything wrong. Each one checked its own inventory, found one unit, and took the money. There is one hoodie on the shelf and two customers who own it, and you will not find out until you pack Monday's orders.

This is the tax on running two Shopify stores out of one stockroom. Two stores are two separate accounts: separate products, separate counts, separate admins. The number in one store does not know the number in the other exists. Sell a unit in either place and Shopify decrements exactly one of the two ledgers, and the other keeps advertising stock you no longer have.

Merchants have been asking about this for as long as the forums go back. The community threads read like one long support ticket: *Can multiple Shopify websites share one inventory?*, *Sync inventory between multiple Shopify stores*, *Can I sync products across two different stores?* The answer never changes. Not natively. Here is a list of apps.

## The short answer

There is no native way to do it. Two Shopify stores are two separate accounts with separate products, separate counts and separate admins, so a sale in either one decrements that ledger alone while the other keeps advertising stock you no longer have. Multi-location inventory does solve this inside a single store, but locations live inside one account and a second store cannot read them, subscribe to them, or see that they exist.

Flow stops at the same wall, automating one store at a time with no trigger that reaches across accounts. The nearest native bridge is Shopify Collective, which syncs a supplier's inventory and prices into a retailer's catalog and pays the wholesale cut automatically. It is built for two businesses trading with each other, so using it on two stores of your own means onboarding yourself as your own supplier and routing a payout between your own bank accounts to move a number between two admins.

So the sync is yours to run, and the hard part is arbitration rather than writing. Match variants across stores by SKU and report the blanks and duplicates instead of guessing at them, name one store the source of truth for each SKU, the one attached to the physical shelf, mirror every change with its reason attached, sold, restocked, returned or corrected, and hold a buffer on the last units so two checkouts never race for one *hoodie*.

## Why one business ends up with two stores

Nobody runs two stores for fun. The second store is always the fix for a real constraint. The most common one is wholesale: you want to [sell to stockists at trade prices](https://blog.dugong.live/how-to-automatically-approve-wholesale-customers-on-shopify.html) without paying for Plus, so the B2B catalog gets its own password-protected store. Or the constraint is geography: a UK store in pounds with UK shipping rates, because one checkout could not say two things at once when you set it up. Or it is brand: the candle line and the homeware line deserve different websites, but they pour from the same workshop and stack on the same shelves.

All three merchants made a sensible call, and all three inherited the same leftover problem: one pile of stock, two systems counting it, and no wire between them. The stockroom is shared. The arithmetic is not.

## The silo Shopify will not bridge

Inside a single store, Shopify is actually good at this. One store can track stock across multiple locations, route orders between warehouses, and show a combined count. But locations live inside one account. A second store cannot read them, cannot subscribe to them, cannot even see that they exist. [Shopify Flow](https://help.shopify.com/en/manual/shopify-flow) stops at the same wall: it automates one store at a time, with no trigger that reaches across accounts.

The closest thing to a native bridge is Shopify Collective, and it is worth being precise about what it is for. Collective connects two stores so a retailer can list a supplier's products, with inventory and prices synced and the wholesale cut paid out automatically. It is built for two businesses trading with each other: US stores, US dollars, [Shopify Payments](https://help.shopify.com/en/manual/payments/shopify-payments), and a sales history bar to clear. If both stores are yours, you would be onboarding yourself as your own supplier and routing a payout between your own bank accounts to move a number between two admins. It can be made to work. It is not what anyone means by keeping two stores in sync.

So the real options are the ones merchants actually live with: update both stores by hand, install a sync app, or build the automation yourself.

## The manual version and the midnight spreadsheet

The manual version starts honorably. Two browser tabs, two admins, and a rule that whoever touches the shelf updates both counts. It survives about a month. Then a restock lands during a busy week, someone updates the retail store and gets interrupted, and the wholesale store spends nine days selling from a count that was true the previous Tuesday. The upgraded version is the CSV ritual: export inventory from the main store, reshape the columns, import into the second store, once a week, at midnight, by you.

> A CSV is a photograph of your inventory. Both stores keep selling after the shutter clicks.

The drift starts the moment the import finishes, and it grows with every sale the export did not see. In a slow month you get away with it. Then the busy weekend arrives, the one the whole quarter was pointed at, and the gap between the two ledgers is suddenly full of orders. That is when the hoodie sells twice, and you get to choose which customer to refund: the retail buyer who paid full price, or the stockist whose reorder was the whole point of the second store. Every path out of that choice costs money and an apology.

## The sync apps and their sharp edges

The app store's answer is a shelf of sync tools, and the good ones are good plumbing. But the mechanics have edges, and the reviews document each one. Sync apps match variants across stores by SKU, so every blank SKU is a variant that silently never syncs, and every duplicated SKU is a coin flip about which variant gets the count. One review describes an app that rewrote SKUs and zeroed inventory across the catalog, and the recovery was a full physical recount. Another describes a two-way sync that kept firing after the app was uninstalled, pushing stale counts back and forth between both stores while collections quietly dropped out of view.

Even when the plumbing works, it works on a delay. A sale on one store reaches the other by webhook in seconds on a quiet Tuesday. On the drop weekend, with both stores moving at once, the last-unit race happens inside that window, and no sync however fast can sell one hoodie to two people successfully. The app did its job. The judgment about last units was never its job.

> **◆ NOTE** The trap is **treating sync as plumbing** when half of it is judgment. Which store gets the benefit of the doubt on the final unit. Which order to keep when both stores sell it anyway. When to stop mirroring because a supplier import is mid-flight. A pipe cannot hold opinions. Your stockroom runs on them.

## What the automation actually has to do

The fix is the routine a good operations person would run if watching both admins were their whole job: mirror every change, protect the last units, and escalate the genuinely ambiguous cases. As a Dugong playbook, in plain prose:

```
# trigger
On inventory change in either store: order,
refund, cancellation, restock, manual edit

# steps
1. Match variants across stores by SKU, and
   report the blanks and duplicates instead
   of guessing
2. Designate one source of truth per SKU,
   the store attached to the physical shelf
3. Mirror every change to the other store
   with the reason attached: sold, restocked,
   returned, corrected
4. Hold a buffer on the mirrored store so
   the last units sell in one place only
5. Catch the race: both stores sell the same
   last unit, keep the order that matters
   more, tell the other customer this hour
6. Pause mirroring while bulk imports and
   supplier feeds run, reconcile on resume
7. Reconcile nightly, report the drift, and
   name the SKUs that keep drifting
```

Step one is the unglamorous win, and it comes before any syncing at all. Matching by SKU only works on a catalog where SKUs are filled in and unique, and most two-store catalogs grew up without that discipline. An automation that starts by reporting the seventeen blank SKUs and the three duplicates, rather than guessing around them, saves you from the class of failure where a sync is confidently wrong for months.

Step four is where the oversell actually dies. The double-sold hoodie was never a speed problem, it was a policy problem: the final units of anything should only be sellable in one place. A buffer of two units on the mirrored store means the wholesale site shows sold out while the retail store sells the last two at full margin, or the reverse if stockists are your priority. Which store wins the endgame is a decision about your business, which is exactly why no app ships it as a default. It is the same species of judgment as [deciding which channel to starve first when stock runs low](https://blog.dugong.live/how-to-prevent-overselling-on-shopify-across-channels.html), applied to a channel that happens to be your own second store.

Step five accepts that no window is ever zero. When the race happens anyway, the difference between a rule and a reader shows. A rule refunds whichever order arrived second, which on a bad night means refunding the stockist who reorders every quarter in favor of a first-time buyer who found you an hour ago. A reader weighs both orders, keeps the one the relationship says to keep, and sends the other customer an apology with a restock date and a [back in stock notification](https://blog.dugong.live/how-to-set-up-back-in-stock-notifications-on-shopify.html) already armed, inside the hour, while the disappointment is still small.

Step six exists because the mirror itself can become the weapon. A supplier CSV that zeroes a column, imported into the source store with the mirror running, becomes [two zeroed catalogs](https://blog.dugong.live/how-to-sync-supplier-inventory-feeds-to-shopify.html) at machine speed. Pausing the mirror during bulk operations, then reconciling before it resumes, is the difference between a bad import and a bad week. And step seven is the habit that keeps the whole thing honest: a nightly count comparison, a short morning note, and a running list of the SKUs that keep disagreeing, because a SKU that drifts weekly has a physical cause standing in your stockroom.

## Why this is a compiler problem, not an app problem

Your actual sync policy is a paragraph, and it is nothing like anyone else's. Wholesale wins ties on core styles because stockists reorder all year. Retail wins on broken sizes because stockists will not buy them anyway. Keep two units back from wholesale on anything that moved this week. Never mirror while the Tuesday supplier file loads. If both stores sell the same last unit, keep whichever order the relationship says, and make the apology generous. That paragraph moves with your margins, your stockists, and your season. A settings page cannot hold it. A compiler that turns the paragraph into the running workflow can, which is the same argument behind [the Shopify automations no one builds](https://blog.dugong.live/best-shopify-automations-to-set-up.html): the automation worth having is shaped like your store, not like a feature grid.

Picture an apparel brand in Portland: a retail site, a wholesale store for about ninety stockists, one stockroom, 1,400 SKUs between them. The first nightly reconcile finds 63 SKUs where the stores disagree, 41 counted high on wholesale and 22 high on retail, drift nobody could see because nobody was comparing. The previous month had six oversells: five were wholesale selling units retail had already shipped, one the reverse. With the playbook running, the SKU report gets fixed in an afternoon, the buffer keeps final units off the wholesale store, and the one genuine race in the next eight weeks ends with the stockist keeping the unit and the retail customer holding an apology, a code, and a restock date before she thought to complain. The owner's involvement was reading a morning summary and answering one question: **wholesale or retail on the last of the corduroy?**

## The workflow worth building this week

Start with the number you do not have. Tonight, export the inventory CSV from both stores and diff them by SKU. Two-store merchants who run this for the first time almost always find drift, and the size of it is the size of your oversell risk on the next busy weekend. While you are in there, count the blank and duplicate SKUs, because that list is the first thing any sync, bought or built, will trip over.

Then run the mirror in dry-run mode for two weeks. Let it watch both stores and report what it would have changed, and check its arithmetic against the shelf. You are walking the same trust curve as [letting an automation draft your reorders](https://blog.dugong.live/how-to-set-inventory-reorder-points-on-shopify.html): verify until it has been right fifty times in a row, then let the clear cases run end to end and keep the odd ones, the negative counts and the unmatched SKUs, for a human look.

Describe it the way you would brief a new hire on their first morning. Both stores sell from the one stockroom, so when anything changes in either store, make the other one match, and write down why. Keep the last couple of units of anything selling in one store only, and ask me which store when it is not obvious. If a supplier file is loading, stop mirroring until it is done and the counts check out. If both stores ever sell the same last unit, keep the order that matters more and apologize to the other customer within the hour. And every morning, tell me which counts disagreed and which SKUs keep doing it. That is the brief. The compiler handles the [webhooks](https://shopify.dev/docs/apps/build/webhooks), the sequencing, and the timing, and the Meridian hoodie stops being owned by two people at once.

> **◆ READING** Two companion pieces if this one landed: [the overselling problem no one automates](https://blog.dugong.live/how-to-prevent-overselling-on-shopify-across-channels.html), on the same race run against marketplaces instead of your own second store, and [the supplier feed that zeroed your catalog](https://blog.dugong.live/how-to-sync-supplier-inventory-feeds-to-shopify.html), on what bulk imports do to a live count.

If you are a Shopify merchant with two admins open in two tabs, a hoodie two customers own, or a midnight CSV ritual you have stopped mentioning out loud, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Can two Shopify stores share the same inventory without an app?

Not natively. Each Shopify store is a separate account with its own products and its own counts, and nothing built into Shopify pushes an inventory change from one store to another. Locations do not help: a single store can track stock across multiple warehouses, but locations live inside one store, and a second store cannot read them. Shopify Flow runs inside a single store too, so there is no cross-store trigger to build on. When merchants ask on the community forums, in threads titled Can multiple Shopify websites share one inventory and Sync inventory between multiple Shopify stores, the staff answer is a list of third-party sync apps. The one partial exception is Shopify Collective, which does sync inventory between connected stores, but it is built for a retailer selling a separate supplier's products, is limited to US stores on Shopify Payments, and routes payouts between two businesses. For two storefronts you own sharing one stockroom, the real options are manual CSV transfers, a sync app, or an automation you control.

Permalink: https://blog.dugong.live/how-to-sync-inventory-between-two-shopify-stores.html#faq-1

### Why do two Shopify stores oversell the same last unit even with a sync app?

Because every sync has a window. An order on store A reaches store B by webhook, and in a quiet week the delay is seconds and invisible. The oversell lives in the exception: a drop, a sale weekend, a product that catches, exactly when both stores are moving fastest. If both stores each show one unit and both sell it inside the window, no app can conjure a second unit; the sync just delivers the bad news. The fix is not faster plumbing, it is judgment about last units: keep a small buffer on the mirrored store so the final units only sell in one place, and when the race happens anyway, read both orders and decide which one to keep rather than refunding whoever was unlucky by seconds. A first-time customer buying one unit and a stockist with three years of reorders are not the same order, and a timestamp cannot tell the difference.

Permalink: https://blog.dugong.live/how-to-sync-inventory-between-two-shopify-stores.html#faq-2

### What is the safest way to set up inventory sync between two Shopify stores?

Audit SKUs first, mirror one way, and reconcile nightly. Sync tools match variants by SKU, so a blank or duplicated SKU becomes a silent miss or a wrong match; fix the catalog before wiring anything. Pick one store per SKU as the source of truth, usually the store attached to the physical shelf, and mirror changes outward instead of running two-way sync, which is how feedback loops corrupt both stores. Run the first two weeks in dry-run mode, where the automation reports what it would have changed and you check its arithmetic, then let the clear cases run and keep the odd ones for a human. Pause mirroring during bulk imports and supplier feed updates, and reconcile the full count nightly with a report naming the SKUs that keep drifting, because a sync that is quietly wrong is worse than no sync at all.

Permalink: https://blog.dugong.live/how-to-sync-inventory-between-two-shopify-stores.html#faq-3

### How do I stop two Shopify stores from selling the same last unit?

With a buffer, because the double-sell is a policy problem before it is a speed problem: the final units of anything should be sellable in one place only. Holding two units back on the mirrored store means the wholesale site shows sold out while retail sells the last two at full margin, or the reverse if stockists are the priority, and which store wins the endgame is a decision about your business, which is exactly why no app ships it as a default. When the race happens inside the sync window anyway, a rule refunds whichever order arrived second, which on a bad night means refunding a stockist who reorders every quarter in favor of a first-time buyer an hour old. The better version weighs both orders, keeps the one the relationship says to keep, and sends the other customer an apology with a restock date inside the hour.

Permalink: https://blog.dugong.live/how-to-sync-inventory-between-two-shopify-stores.html#faq-4

### Should inventory sync keep running during a bulk import?

No. Pause the mirror while bulk imports and supplier feeds run, and reconcile before it resumes, because the mirror itself can become the weapon: a supplier CSV that zeroes a column, imported into the source store with the mirror live, becomes two zeroed catalogs at machine speed. The app reviews document the neighboring failures, one sync that rewrote SKUs and zeroed inventory across the catalog, where the recovery was a full physical recount, and a two-way sync that kept firing after the app was uninstalled, pushing stale counts back and forth while collections quietly dropped out of view. The habit that keeps any mirror honest is the nightly count comparison with the drift reported each morning and the repeat offenders named, because a SKU that drifts weekly has a physical cause standing in your stockroom, not a software one.

Permalink: https://blog.dugong.live/how-to-sync-inventory-between-two-shopify-stores.html#faq-5

---

Markdown rendition of https://blog.dugong.live/how-to-sync-inventory-between-two-shopify-stores.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
