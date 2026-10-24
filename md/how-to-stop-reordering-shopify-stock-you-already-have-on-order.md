# How to stop reordering Shopify stock you already have on order

> Incoming reads zero while the pallet sits at the supplier, so the report tells you to buy it again. The AI playbook that tracks every open Shopify purchase order.

- Canonical: https://blog.dugong.live/how-to-stop-reordering-shopify-stock-you-already-have-on-order.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-10-15
- Section: Research
- Word count: 2462
- Dispatch: Nº 128 · Research · 8 min read
- Full headline on page: How to stop reordering Shopify stock *you already have on order*
- Keywords: shopify incoming inventory, shopify purchase order tracking, shopify purchase order api, inventoryPurchaseOrders, read_inventory_purchase_orders, shopify on order quantity, shopify late purchase order, shopify double ordering stock, stocky sunset replacement, shopify flow incoming inventory
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

The second pallet arrives on a Thursday and nobody ordered it. Except somebody did, twice, six weeks apart, because the first purchase order never showed up as anything. The stock sat at the supplier, the incoming column read zero, the low stock report put the SKU back on the buy list, and a reasonable person bought it again. Now there is four thousand dollars of inventory in the aisle, the supplier is confused, and the person who placed both orders did nothing wrong.

This is the most expensive Shopify gap I know of that almost nobody writes about, and it comes down to one word being defined more narrowly than everyone assumes.


## The short answer

Incoming inventory on Shopify counts units in transit, not units you have bought, so a purchase order the supplier has not shipped reads as zero and the low stock report tells you to buy it again. The purchase order and its linked inventory transfer operate independently by design, Shopify Flow cannot read incoming quantities or purchase order data at all, and the purchase order API that landed in the 2026-10 Admin GraphQL version carries exactly two statuses, DRAFT and ORDERED, with no received state and no expected arrival date. The playbook builds the on order number Shopify does not give you, dates every open purchase order, flags the late ones, and warns the buyer before the same pallet is ordered twice.
## Incoming does not mean on order

Shopify's Help Center says incoming inventory is inventory that is on its way to your location from inventory transfers or apps. Units that have not been received are excluded from on hand and cannot be sold. Available, the number your storefront reads, explicitly excludes incoming as well.

Read that definition again and notice what it is about. It is about movement. A merchant who tested this on a development store in September 2026 put it plainly: the number shown as incoming on a product is narrower than it looks, because incoming counts units that are in transit. Transfers still in draft add nothing. Transfers marked ready to ship but not yet dispatched add nothing. A purchase order you placed three weeks ago that the supplier has not shipped shows as zero.

So incoming is a transit number. The number you need for a buying decision is an **on order** number: what you have committed to buy and not yet received, regardless of whether it has moved. Shopify has no field for that, no column for it, and no report that shows it.

## And then the reports tell you to buy it again

On 24 July 2026 a merchant posted the consequence exactly. His custom purchasing reports depend on incoming quantities, and after the new purchase order system launched, incoming stopped reflecting open purchase orders. His line was: my reports keep telling me to procure what is already in process. He asked for the old purchase order system back and flagged the obvious risk to capital management. No staff reply.

Thirty minutes later he posted his own workaround, which is the part worth sitting with. Create a transfer from the purchase order and mark it in transit before it has shipped. In other words, tell Shopify the goods are moving when they are not, so the number comes out right. He called the extra steps frustrating. They are also now standard practice in a lot of stores.

Another member explained the mechanics the same evening. Incoming is derived from transfers and shipments, not from purchase orders, so the transfer step is mandatory. Then the warning that matters most: editing the purchase order afterwards, or receiving a short shipment, will not update the transfer, which can silently re-create overcounting. His suggestion was to store the purchase order number in a transfer metafield so reports can join the two records back together.

That is the whole trap in three sentences. Undercounting makes you double order. The fix for undercounting creates overcounting. And the join between the two records is something you have to build yourself out of a metafield.

## The purchase order and its transfer stop talking

On 16 September 2026 a merchant asked for something that sounds like it should already be true: when you add products to a purchase order, the linked inventory transfer should update too. His words were that the current workflow requires duplicate manual edits. The reply quoted Shopify's own documentation back at him. Once a purchase order and an inventory transfer are linked, they operate independently.

So you keep two records of the same delivery. One is the commercial agreement and one is the count, they are linked in name only, and every edit after the link has to be made twice. Nothing tells you when they drift.

## Two years, two systems, the same hole

This is not new and it did not arrive with the new system. In April 2024 the same merchant asked why Stocky purchase orders were not syncing to Shopify's incoming inventory. A week later another merchant replied that he had at least five active or partially received purchase orders and that Stocky was completely unaware of these incoming inventories, which made the low stock report useless. Support told him to re-enter the data manually. In July 2024 a third merchant asked whether anyone had solved it. No staff reply, no resolution.

Stocky shut down on 31 August 2026 and the native purchase order screen inherited the job. In the thread where merchants worked out what to do about the sunset, one of them wrote in May 2026 that the native purchase order system is fundamentally incomplete. Another reported that the only option support offered was to pay for an ERP. A third shared a support table listing minimum and maximum replenishment as not planned for 2026, and bulk CSV import as not currently available.

> **◆ FROM THE FORUMS** February 2026, a merchant asking what replaces Stocky for purchase orders is told by support that the path forward is to buy an ERP. Eight months later the same thread is still open, the sunset has happened, and the answer has not improved. The gap between a $39 app and an ERP is where most of the Shopify catalog lives.

## Flow cannot see any of this

On 26 January 2026 a merchant asked for a workflow that lists products with incoming inventory above zero, sorted by purchase order and vendor. He had already asked Sidekick, Shopify's own assistant, and quoted the answer: Shopify Flow cannot access incoming inventory quantities for reporting and automation. The thread was revived on 5 October 2026 and two developers confirmed nothing had changed, pointing at a custom app or a scheduled job against the Admin API instead.

Flow's inventory bench is short and entirely event-driven: inventory item created, inventory item deleted, inventory transfer completed, inventory transfer ready to ship, product variant back in stock, product variant out of stock, product variant inventory quantity changed. Every one of them needs something to happen.

A late purchase order is the absence of something happening. There is no trigger for a delivery date that passed, because Shopify does not hold a delivery date to pass. The only native shape left is the scheduled time trigger driving a sweep that you build and maintain. It is the right shape. It is not a feature.

## The API finally got purchase orders, two weeks ago

Here is the genuinely new part, and most of the advice online has not caught up with it yet. The 2026-10 Admin GraphQL version exposes `inventoryPurchaseOrders` and `inventoryPurchaseOrder`, behind a `read_inventory_purchase_orders` scope. A Shopify engineer confirmed on 2 October 2026 that the scope is available to all apps now, outside the preview.

Getting there was messy enough to explain why nobody has written about it. On 11 August a developer hit ACCESS_DENIED on the query, found the scope was absent from both the public access scopes reference and the dashboard selector, and was told by a Shopify engineer that declaring it in `shopify.app.toml` passes validation and then fails at deploy. Shopify patched it server side on 14 August so existing read_inventory access would work on preview stores. Before that, every feature request since June 2026 had gone unanswered, including one on 30 July asking for a firm yes or no on whether the API would arrive inside twelve months.

So it exists. Now read what it actually gives you. The object is defined as an agreement from a merchant to buy goods or services from a supplier, and it carries the name, the supplier as origin, the destination location, dateCreated, orderedAt, the line items, which can be searched by unit cost, variant id, supplier SKU and incoming quantity, and a transfers connection.

And the status enum has exactly two values. `DRAFT`, open and not marked as ordered yet. `ORDERED`, open and marked as ordered. That is the entire lifecycle. There is no received, no partially received, no closed and no late. There is an orderedAt timestamp and no expected arrival anywhere on the object.

Which means the two questions you actually have, how much of this is still outstanding and which of these should have landed by now, are both things you compute from the linked transfers. The same transfers that, per Shopify's own documentation, operate independently of the purchase order.

## What it costs while nobody counts

Take a store carrying four hundred SKUs across a dozen suppliers, with an average purchase order around four thousand dollars. Two duplicate orders a month is eight thousand dollars of working capital converted into stock you already owned, plus the storage, plus the markdown on whatever does not sell at full price. That is the loud half.

The quiet half is worse. Purchase orders that are simply late, with nothing watching the date. A thirty five day lead time slips by three weeks and nobody finds out until the shelf is empty and the product page says sold out. Then you are paying for air freight, or losing the sale, or both.

Both halves come from the same missing object: a list of what is on order, with a date on it, that something checks every night. Everything else here is a symptom.

## The playbook worth building

As a Dugong playbook, in plain language:

```
# trigger
Nightly, and on every purchase
order status change, over all
open purchase orders

# steps
1. Pull every PO marked ordered
   and not fully received, with
   lines, supplier, destination
2. Reconcile: sum the linked
   transfers and shipments per
   line, keep the remainder
3. Date it: expected arrival
   from supplier lead time when
   the PO carries none
4. Flag late: past expected,
   remainder still open, aged
   in days not listed by date
5. Publish on order per variant:
   ordered minus received, per
   location, beside available
6. Block the duplicate: warn at
   the moment someone drafts a
   PO for a SKU already on order
7. Chase the supplier with the
   PO number, the open lines
   and the days late
8. Score lead time actual vs
   promised, and short ship
   rate, per supplier
```

**Step five is the one everyone skips.** Everything else is housekeeping. This one changes the decision. Write a real on order quantity per variant per location somewhere your reorder logic can read it, a metafield is fine, and the low stock report stops lying the same week. Until that number exists, every buying decision in the store is made against a count that is missing the orders you already placed.

**Step six is where the money is.** A warning at the moment someone drafts the order is worth more than any dashboard, because the duplicate order is not a reporting failure, it is a decision made with the wrong number in front of a person who is in a hurry.

## Three numbers to write down

The build is a day. The decisions are what stall people, and all three are small. How many days past expected arrival makes a purchase order late, which is usually seven for domestic and fourteen for ocean freight. What short ship percentage you let through without chasing, which for most stores is about two percent. And the purchase order value above which a human reviews it before it goes to the supplier. Pick those three and the rest is configuration.

## Where AI earns its place

Three jobs here, and none of them is running a query.

**Matching the delivery to the order.** Pulling open purchase orders is mechanical. Working out what arrived is not. The supplier's packing slip uses their part numbers, their case packs and their own wording for each line, and real deliveries come short, split across two shipments, or substituted. The purchase order line does carry a supplier SKU field, which helps on the clean ones and not at all on the rest. A model reads the supplier's document against your lines and proposes the match, which is what makes the remainder number trustworthy.

**Finding the real date.** Expected arrival almost never lives in Shopify. It lives in an email saying shipping Friday, a second one moving it to the week of the tenth, and a PDF with a carrier reference buried in it. A model reads that thread and keeps one honest date per purchase order, which is the input every other step depends on.

**Writing the chase.** The purchase order number, the lines still outstanding, the days past the date the supplier themselves gave you, in a tone that keeps the relationship. Most late deliveries move when somebody asks on day three instead of day thirty.

Keep three things human. Sending a purchase order above whatever value you set. Accepting a substitution. And any change to agreed cost.

## Do this before you close the laptop

Open Products, then Purchase orders, filter to ordered, and sort oldest first. Count how many were created more than one supplier lead time ago and are still sitting there. Then take three of them, pick one variant from each, and look at its incoming count. In most stores at least one of the three reads zero, which means your reorder report has been treating that stock as if it does not exist since the day you bought it.

> **◆ READING** Two companion pieces if this one landed: [The reorder you always make too late](https://blog.dugong.live/how-to-set-inventory-reorder-points-on-shopify.html), on deciding what to buy and when, and [The stock Shopify won't let you sell](https://blog.dugong.live/how-to-fix-shopify-committed-inventory-that-never-clears.html), on the same arithmetic going wrong at the other end. And when the pallet does land, [The stock in your building your store will not sell](https://blog.dugong.live/how-to-catch-shopify-inventory-transfers-that-never-get-received.html), on the transfer nobody receives and the stock that stays unsellable because of it.

Sitting on purchase orders nobody has looked at since they were sent, a supplier who is three weeks late and does not know you noticed, or a low stock report you have stopped trusting? The inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Why does Shopify show zero incoming inventory when I have a purchase order open?

Because incoming counts units that are moving, not units you have bought. Shopify's Help Center defines incoming inventory as inventory that is on its way to your location from inventory transfers or apps, and says units that have not been received are excluded and cannot be sold. In practice the number is narrower still. A merchant who tested this on a development store in September 2026 reported that incoming counts units in transit, that transfers sitting in draft or marked ready to ship but not yet dispatched add nothing to the number, and that an order placed weeks earlier which the supplier has not shipped shows as zero. So a confirmed purchase order with a signed price, a quantity and a delivery date contributes nothing to incoming until somebody creates a transfer against it and marks it in transit. Incoming is a transit number. On order is the number you actually need for buying decisions, and Shopify does not have a field for it.

Permalink: https://blog.dugong.live/how-to-stop-reordering-shopify-stock-you-already-have-on-order.html#faq-1

### Does Shopify count purchase orders in incoming inventory?

The documentation says yes and merchants report otherwise. The Help Center names purchase orders in its incoming section and says that clicking a variant's incoming quantity shows which transfers, purchase orders or apps make up the number. On 24 July 2026 a merchant posted that incoming quantities stopped reflecting open purchase orders after the new purchase order system launched, and that his reports keep telling him to procure what is already in process. He asked for the old system back. There was no staff reply. Within the hour he posted his own workaround, which is to create a transfer from the purchase order and mark it in transit before the goods have shipped. Another member explained the mechanics: incoming is derived from transfers and shipments rather than from purchase orders, so the transfer step is mandatory, and he warned that editing the purchase order afterwards, or receiving a short shipment, will not update the transfer, which silently re-creates an overcount. The practical answer is that a purchase order on its own does not move incoming.

Permalink: https://blog.dugong.live/how-to-stop-reordering-shopify-stock-you-already-have-on-order.html#faq-2

### How do I see how much of a product is already on order in Shopify?

There is no on order column in the admin, so you have to build the number. As of the 2026-10 Admin GraphQL API you can query inventoryPurchaseOrders and inventoryPurchaseOrder with the read_inventory_purchase_orders scope, which Shopify staff confirmed on 2 October 2026 is available to all apps outside the preview. The purchase order object gives you the name, the supplier as origin, the destination location, dateCreated, orderedAt, the line items, which can be searched by unit cost, variant id, supplier SKU and incoming quantity, and a transfers connection. On order per variant is then ordered quantity minus what the linked transfers and shipments show as received, summed per line and per location. Nothing in Shopify calculates that for you and no report exposes it, so it is a nightly job you run and write back somewhere your buying decisions can read it, usually a metafield or an outside planning tool.

Permalink: https://blog.dugong.live/how-to-stop-reordering-shopify-stock-you-already-have-on-order.html#faq-3

### Is there a Shopify purchase order API?

Yes, as of the 2026-10 Admin GraphQL version, and it is new enough that most of the advice online still says there is not. Developers asked for it repeatedly through 2026. A feature request on 16 June 2026 asked for read, create and receive, noting that the inventory transfer and shipment types do not cover supplier or purchase order level tracking, and got no staff reply. A separate thread on 30 July 2026 asked for a firm answer on whether the API would arrive within twelve months. Access was awkward at first: on 11 August 2026 a developer hit ACCESS_DENIED on inventoryPurchaseOrders, found that read_inventory_purchase_orders was not in the public access scopes reference or the dashboard selector, and a Shopify engineer confirmed that declaring it in shopify.app.toml passes validation but fails at deploy. Shopify patched it server side on 14 August so that read_inventory would work on preview stores, and the dedicated scope went generally available in 2026-10. Read the status enum before you plan around it, though. It has exactly two values, DRAFT and ORDERED. There is no received, no partially received and no closed, so lifecycle state is something you derive from the linked transfers.

Permalink: https://blog.dugong.live/how-to-stop-reordering-shopify-stock-you-already-have-on-order.html#faq-4

### Can Shopify Flow alert me when a purchase order is late?

No, on two counts. Flow cannot read incoming quantities or purchase order data at all. A merchant asked on 26 January 2026 for a workflow listing products with incoming above zero sorted by purchase order and vendor, and quoted Sidekick saying that Shopify Flow cannot access incoming inventory quantities for reporting and automation. The thread was revived on 5 October 2026 and two developers confirmed nothing had changed, suggesting a custom app or a scheduled job against the Admin API instead. The second problem is structural. Flow's inventory bench is inventory item created, inventory item deleted, inventory transfer completed, inventory transfer ready to ship, product variant back in stock, product variant out of stock and product variant inventory quantity changed. Every one of them needs an event. A late purchase order is the absence of an event, so there is nothing for Flow to listen to. The only native shape is the scheduled time trigger driving a sweep you build and maintain yourself.

Permalink: https://blog.dugong.live/how-to-stop-reordering-shopify-stock-you-already-have-on-order.html#faq-5

### Can AI handle purchase order tracking for a Shopify store?

It fits this problem well, because the hard parts are reading and matching rather than counting. Pulling open purchase orders is a query once you have API access. Reconciling what arrived against what you ordered is not, because the supplier's packing slip uses their part numbers, their case packs and their own description of each line, while your purchase order uses yours. The purchase order line item does carry a supplier SKU field, but real deliveries arrive short, split across two shipments, or substituted, and a model can read the supplier's document against your lines and propose the match. The second job is dates. Expected arrival almost never lives in Shopify. It lives in an email saying shipping Friday, a later one moving it to the week of the tenth, and a PDF with a carrier reference, and a model can read that thread and keep one honest date per purchase order. The third is writing the chase: the purchase order number, the lines still outstanding, the days past the date the supplier gave you. Keep three things human. Sending a purchase order above whatever value you set, accepting a substitution, and any change to agreed cost.

Permalink: https://blog.dugong.live/how-to-stop-reordering-shopify-stock-you-already-have-on-order.html#faq-6

---

Markdown rendition of https://blog.dugong.live/how-to-stop-reordering-shopify-stock-you-already-have-on-order.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
