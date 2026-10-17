# How to fix Shopify committed inventory that never clears

> Committed is read-only and Shopify will not tell you which orders hold it. The AI playbook that finds the stuck orders and gets your shelf selling again.

- Canonical: https://blog.dugong.live/how-to-fix-shopify-committed-inventory-that-never-clears.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-10-12
- Section: Research
- Word count: 2166
- Dispatch: Nº 125 · Research · 8 min read
- Full headline on page: How to fix Shopify committed inventory that *never clears*
- Keywords: shopify committed inventory, committed inventory not clearing, shopify shows sold out but in stock, clear committed inventory shopify, which orders hold committed inventory, shopify committed inventory negative, shopify available vs on hand, draft order reserve inventory
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

You count the shelf because a customer emailed to ask whether you really were out of the navy one. Fourteen units, boxed, labeled, right where they should be. The admin agrees: on hand, fourteen. The product page says sold out, and it is not lying either. Available is zero.

The fourteen are in *committed*. Click the number and Shopify shows you a list of orders. Two of them shipped in August.

Now try to fix it. There is no edit field on committed. There is no release button. There is no app that clears it, no Flow action that touches it, and no API call that moves it. You have found the one number in Shopify inventory that you are not allowed to change, holding stock you can physically pick up.

## What committed actually is

Worth being precise, because almost every wrong fix starts with a wrong mental model. Shopify splits the stock at each location into states. On hand is everything physically there. Available is what the storefront may sell. Between them sit committed, reserved, damaged, safety stock and quality control, and Shopify's developer docs state the arithmetic outright: on hand is the sum of all six.

Your store sells *available*. Your warehouse counts *on hand*. Nobody reconciles the difference, which is where this whole problem lives.

Three things move units into committed, per Shopify's help documentation, which describes committed as the number of units that are set aside and cannot be sold: line items on orders placed but not yet fulfilled, items reserved against a draft order, and transfers marked ready to ship.

All three are correct on the day they happen. An order placed at 9am should hold its units until it ships. The failure is that nothing ages them. Shopify has no concept of a stale commitment, no report listing them by age, and no alert when one outlives the order that made it.

## Committed is read-only, and Shopify says so

This is the sentence that saves you a week. From Shopify's developer documentation on inventory states: you cannot use the GraphQL Admin API to adjust or move inventory quantities in the committed state.

Everything else is writable. Available moves with `inventorySetQuantities`, `inventoryAdjustQuantities` and `inventoryMoveQuantities`. Reserved, damaged, safety stock and quality control move with the adjust and move mutations. Committed moves only when Shopify decides, through order creation and fulfillment, draft reservations and transfer readiness.

Flow sits on the same API, so Flow cannot do it either. It cannot even read committed natively. A merchant asked in August 2025 how to compare incoming stock against committed inside Flow, and the working answer was to pull `quantities(names: ["incoming", "committed"])` through a send admin API request or a third-party GraphQL action and compare the numbers in a run code step. Read only, in both senses.

> Committed is not a setting you got wrong. It is an effect. The only way to move it is to finish or undo the thing that caused it.

## The breakdown you can see and cannot query

Here is the gap that turns a five-minute fix into a project.

In the admin, clicking committed shows which orders hold the units. Through the API that list does not exist. A developer building a private 3PL integration went looking in May 2025, found that the admin uses a non-public field called `activeLedgerDocuments`, and asked whether there is any way to accomplish the same thing with public Shopify GraphQL.

Shopify's answer was to approximate it: query orders with a filter such as `fulfillment_status:unfulfilled AND status:open AND sku:...`. A second developer hit the identical wall for safety stock in September 2025, finding the admin's `ledgerDocumentQuantities` and `externalQuantityByApp` absent from the public schema, and was told that currently you can only narrow this down to the name. The thread is still open.

So Shopify knows exactly which orders hold your stock, shows you in the interface, and gives no programmatic way to get it. Any automation here rebuilds that breakdown from the orders side and checks its own work.

## The six reasons it never clears

Every stuck unit has one of six causes, and each needs a different release. Mixing them up is why the usual fix, editing on hand upward until the site sells again, quietly creates an oversell three weeks later.

**One. The order nobody will ever fulfill.** Cancelled, refunded, test, or simply abandoned by the customer who stopped answering. It is closed as far as everyone is concerned and still unfulfilled as far as inventory is concerned, so it keeps its units. A merchant hit this in August 2020 with a cancelled test order that blocked them from de-stocking the item, Shopify answering that it cannot unstock from this location because it has unfulfilled orders. Same report in December 2020 and January 2021. The only workaround, posted in April 2024, is to unarchive the order, fulfill the line or move its location, then archive it again. Five years, no native fix.

**Two. The fulfillment nobody released.** An order on hold is an unfulfilled order. A fraud check from a Friday night, a payment question, a pre-order waiting on a drop. The stock stays committed for as long as the hold lasts, and nothing counts the days.

**Three. The quote that went quiet.** Reserve items on a draft order and Shopify's help page is explicit about what happens: those inventory units are put in the committed inventory state and cannot be purchased by other customers. You pick the expiry date yourself. Which means somebody chose 31 December, the buyer went quiet in July, and your best seller has been short six units since then.

**Four. The line item at the wrong location.** As a merchant put it on that de-stocking thread, committed inventory just means it is assigned to that location in an order. If the order routed to a location that no longer picks, or a 3PL that never got the order, the commitment sits at a shelf nobody is looking at. You have to either reassign the location or fulfill the item to clear it.

**Five. The transfer marked ready and never moved.** Marking a transfer ready to ship commits the stock at the origin. If the pallet never left, or left and was never received, the units are committed at one end and not incoming at the other.

**Six. Shopify is just wrong.** This one is real and the public record is uncomfortable. In January 2024 a merchant reported an order fulfilled and still counted in committed. Three more arrived underneath: a sixteen-item order showing eighteen committed, the same across many products, and one merchant concluding that we have to wait, I guess. No staff reply, no accepted answer, last post still asking for an update. In February 2023 the inverse appeared, committed going *negative*, a staff member confirming your committed quantity should not be showing negative values and calling it a known issue while the merchant reported inventory showing hundreds more items than are actually available. A later reply traced it to adjustments labeled data correction that reset committed to zero, after which fulfilling older orders pushed it below.

Causes one to five you can fix. Cause six you can only detect, evidence and escalate, which is itself worth automating, because a wrong committed number is indistinguishable from a stuck order until somebody counts.

## What it costs while you do not know

**The sale you never see.** A sold-out product page produces no order, no abandoned checkout and no ticket. No report has a row for revenue you did not take on stock you own, and the only way to find it is to compare on hand against available yourself.

**The reorder you raise too early.** Reorder logic runs on available. Fourteen units frozen in committed look exactly like zero units, so the system asks for more of something sitting in your own stockroom, and ties up cash on a line that was never short.

**The checkout that fails in one country and not another.** This one bites multi-location stores hard. A merchant reported in December 2025 that with fulfillable inventory switched on, products whose warehouse stock was fully committed but unshipped still showed as available, and customers reached checkout only to be told the store does not ship to their country. The thread closed unresolved. Underneath it sits a related trap: in October 2025 a developer found the Storefront API's `quantityAvailable` returning one global total for every country, so a location at minus one hundred masked sixty-nine real units in Australia. Shopify reproduced it, fixed it in January 2026, and noted that contextual values need show only fulfillable inventory switched on.

**The stock take that never ties.** You count fourteen, the system says zero, somebody edits on hand upward to make the site sell. Two weeks later the stuck orders resolve, the committed units release, and you oversell by exactly the amount somebody added in good faith.

## The playbook worth building

As a Dugong playbook, in plain language:

```
# trigger
Nightly, over every variant at
every location with committed
above zero

# steps
1. Rebuild the breakdown: open
   unfulfilled line items, draft
   reserves, ready transfers
2. Reconcile that total against
   committed, flag every unit
   you cannot account for
3. Age each commitment from the
   day it was created, since
   Shopify ages nothing
4. Classify the stuck ones:
   unfulfillable, held, stale
   reserve, wrong location,
   dormant transfer, miscount
5. Release with the one action
   that fits: fulfill, cancel and
   restock, reassign, unhold,
   expire, receive
6. Chase stale draft reserves
   before the date, not after
7. Alert on any variant with on
   hand above zero and available
   at or below zero
8. Escalate the unexplained with
   variant, location, your count
   and the gap attached
```

**Step two is the one that matters.** The moment you can say committed is nine and I can account for six, a vague inventory complaint becomes a specific question. That is the difference between a support ticket that gets fixed and one that gets closed.

**Step seven is the cheapest alarm in ecommerce.** One query, run nightly: on hand above zero, available at or below zero. Every row is a product you own and cannot sell. Most stores running this for the first time find between three and twenty rows, and are surprised by how old some of them are.

## Three numbers to write down

The automation is a day of work. The decisions are what block people, and they are all small. How many days an unfulfilled order may sit before its commitment gets reviewed. How long a draft reserve lasts before it is chased and expired. And the variance, in units or in value, above which a release goes to a human instead of happening quietly. Pick the three and the rest is configuration.

## Where AI earns its place

Three jobs, and none of them is subtraction.

**Attribution.** Shopify will not tell you which orders hold the units, so something has to rebuild it from the orders side, match quantities per variant per location, and be honest about the leftovers. That is reconciliation with ambiguity in it, which is where a rules engine gives up.

**Choosing the release.** Six causes, six actions, and the wrong one is worse than nothing. Fulfilling a line item on an order the customer actually cancelled creates a phantom shipment. Cancelling with restock on an order waiting on a supplier loses a sale you had already won. That judgement needs the order timeline, the hold reason and the customer's last message read together, then stated in a sentence a human can approve in four seconds.

**Writing the escalation.** When no order explains committed, what gets it fixed is a ticket carrying the variant, the location, the committed figure, your own figure, the adjustment history and the date it diverged. The merchants in those threads who got movement were the ones who could show the number.

Two things stay human. Cancelling a customer's order to free up stock, because that is a customer decision wearing an inventory costume. And any release above your variance threshold, because the opposite of a phantom unit is an oversell, and oversells cost more.

## Do this before you close the laptop

Export your inventory, filter to available at zero with on hand above zero, count the rows and multiply by price. Then open the oldest one, click committed, and read the date of the order holding it. That date is how long your store has been telling customers you were out of something you could have picked off a shelf.

> **◆ READING** Two companion pieces if this one landed: [The stock count that changes overnight](https://blog.dugong.live/how-to-stop-your-shopify-inventory-changing-by-itself.html), on adjustments nobody can trace, and [The overselling problem no one automates](https://blog.dugong.live/how-to-prevent-overselling-on-shopify-across-channels.html), on the gap that opens when two channels sell the same unit.

Sitting on stock your store insists you do not have, a committed figure that no order explains, or a draft reserve from last quarter nobody closed? The inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Why does my Shopify product show sold out when I have stock on the shelf?

Because your store sells the available number, not the on hand number, and the two are different by whatever is sitting in committed. Shopify splits every location's stock into on hand, which is everything physically there, and available, which is what is left after committed, reserved, damaged, safety stock and quality control are taken out. On hand equals the sum of all of them. So a variant with fourteen on hand and fourteen committed reads as sold out on the product page while fourteen units sit on the shelf. Three things put units into committed: line items on orders that are placed but not yet fulfilled, items reserved on a draft order, and transfers marked ready to ship. The number is almost always correct on the day it appears. It becomes a problem when the order that created it never finishes, because nothing in Shopify ages committed inventory or tells you it has gone stale.

Permalink: https://blog.dugong.live/how-to-fix-shopify-committed-inventory-that-never-clears.html#faq-1

### How do I clear committed inventory on Shopify?

Not directly, and this catches almost everybody. There is no edit field on committed in the admin and no button that releases it, because committed is an effect rather than a setting. The only way to move it is to finish or undo the thing that created it. Fulfill the line item and the units leave committed. Cancel the order with restock ticked and they go back to available. Reassign the line item to a different location and the commitment moves with it. Complete or delete the draft order and the reserve ends. Receive or cancel the transfer and the ready-to-ship hold goes. The community workaround for a line item you cannot fulfill, posted on the five-year-old thread about being unable to de-stock a location with unfulfilled orders, is exactly this: unarchive the order if you have to, then fulfill the line or change its location, then archive it again. Tedious on one order, impossible by hand on two hundred, which is the whole reason this is an automation problem rather than an admin problem.

Permalink: https://blog.dugong.live/how-to-fix-shopify-committed-inventory-that-never-clears.html#faq-2

### Can I adjust committed inventory through the Shopify API or Shopify Flow?

No, and Shopify says so in plain words in its own developer documentation: you cannot use the GraphQL Admin API to adjust or move inventory quantities in the committed state. Available, reserved, damaged, safety stock and quality control are all writable through inventoryAdjustQuantities, inventoryMoveQuantities or inventorySetQuantities. Committed is not. Shopify manages it itself through order creation and fulfillment, draft order reservations and transfer readiness. Flow inherits the same ceiling, since its inventory actions go through the same API, and Flow cannot even read committed natively: a merchant asking in August 2025 how to compare incoming against committed was told to use a send admin API request step or a third-party GraphQL action to pull quantities with names committed and incoming, then compare the values in a run code step. So any fix you build acts on orders, not on the inventory number.

Permalink: https://blog.dugong.live/how-to-fix-shopify-committed-inventory-that-never-clears.html#faq-3

### How do I find out which orders are holding my committed inventory?

In the admin you click the committed number and a popover lists the orders. Through the API you cannot, and that gap is documented. A developer building a 3PL integration asked for the same breakdown in May 2025 and pointed out that the admin gets it from a non-public field called activeLedgerDocuments, then asked whether there is any way to accomplish the same thing with public Shopify GraphQL. Shopify's answer was to approximate it with an orders search, filtering on fulfillment_status unfulfilled, status open and the SKU. A second developer hit the same wall for safety stock in September 2025 and was told that currently you can only narrow this down to the name, not a specific app or reference URI. The thread is still open. In practice that means you rebuild the breakdown yourself: list every open, unfulfilled line item for that variant at that location, sum the quantities, and compare the total against committed. When the two agree you know which orders to chase. When they do not, you have found a different bug.

Permalink: https://blog.dugong.live/how-to-fix-shopify-committed-inventory-that-never-clears.html#faq-4

### Why does committed inventory still show orders I have already fulfilled?

Because committed can simply be wrong, and the public record of it goes back years with no fix attached. A merchant reported in January 2024 that an order was fulfilled and committed inventory still counted it. Three more merchants arrived underneath with the same symptom, one of them noting that a sixteen item order was showing eighteen in the committed list, another reporting it across many orders and products, another concluding that we have to wait, I guess. No Shopify staff reply, no accepted solution, last post still asking for an update. In February 2023 the inverse appeared, committed going negative, with a staff member confirming your committed quantity should not be showing negative values and a merchant reporting that our inventory now shows hundreds more items than are actually available. The lesson is operational rather than technical. Treat committed as a claim to be checked, not a fact. Reconcile it nightly against the open unfulfilled line items you can count yourself, and alert on the difference, because the difference is either an order nobody is working or a number that needs support.

Permalink: https://blog.dugong.live/how-to-fix-shopify-committed-inventory-that-never-clears.html#faq-5

### Can AI fix Shopify committed inventory that never clears?

It fits well, because the work is attribution and judgement rather than arithmetic. The hard part is not seeing that committed is nine. It is reconstructing which nine units those are, from open unfulfilled line items, draft reserves and transfers marked ready, then deciding what each stuck one deserves. A cancelled order that never got its restock, an order sitting on a fulfillment hold nobody released, a draft reserve from a quote that went quiet in July, a line item pointing at a location that stopped picking, and a genuine Shopify miscount all look identical in the admin as one number, and each one needs a different release: fulfill, cancel and restock, reassign, release the hold, end the reserve, or open a support ticket with the evidence attached. A model can read the order timeline and tell them apart, and it can do it across every variant at every location every night, which is the part nobody has time for. Keep two things human. Cancelling a customer's order to free stock, because that is a customer decision and not an inventory one. And any release above your variance threshold, because the alternative to a phantom unit is an oversell.

Permalink: https://blog.dugong.live/how-to-fix-shopify-committed-inventory-that-never-clears.html#faq-6

---

Markdown rendition of https://blog.dugong.live/how-to-fix-shopify-committed-inventory-that-never-clears.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
