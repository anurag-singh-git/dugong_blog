# How to sync supplier stock feeds to Shopify without zeroing your catalog

> One renamed column and your sync app sets 400 products to zero. The AI playbook that checks a supplier feed before it trusts it and holds back bad updates.

- Canonical: https://blog.dugong.live/how-to-sync-supplier-inventory-feeds-to-shopify.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-07-26
- Updated: 2026-10-25
- Section: Research
- Word count: 2710
- Dispatch: Nº 92 · Research · 10 min read
- Full headline on page: How to sync *supplier stock feeds* to Shopify without zeroing your catalog
- Keywords: Shopify supplier inventory sync, sync supplier stock feed Shopify, Shopify SKU case sensitive inventory, supplier feed set products to zero Shopify, Shopify FTP inventory sync, dropship inventory sync Shopify, vendor stock report Shopify, Shopify inventory feed mapping
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

There are two ways a supplier feed ruins your week, and the loud one is easier to describe. At 6am your distributor uploads their daily stock file to the same FTP folder they have used for two years. At 6:05 your sync app collects it. At 6:06 four hundred products in your store are sitting at zero. Nothing sold overnight. Over the weekend somebody at the supplier changed a column header from QTY to Qty Available, the SKU column moved one position to the right, and the matcher came back with nothing. Your app then did precisely what you told it to do when you set it up: treat an unmatched item as out of stock. By the time you notice, you have lost a morning of traffic, your paid campaigns have been running to sold-out pages, and a queue of back-in-stock alerts is building for products that never left the shelf.

The quiet one costs more over a year. The feed parses perfectly. It just arrives once a day, and your bestseller sold out at the supplier's warehouse at eleven in the morning. For the next nineteen hours your store takes orders against stock that does not exist, and you find out when the fulfillment file bounces or a customer emails to ask where their thing is. Both failures come from the same place. A stock feed is a claim about the world that was true at the moment it was written, and nothing in your stack is asking whether it is still true, or whether it was ever well formed to begin with.

## The short answer

Shopify has no concept of a supplier anywhere in the platform. There is no scheduled import, no FTP or SFTP client, no column mapping screen, and no reconciliation report telling you what last night's update changed. Locations, quantities and committed stock all work properly; the feed itself is somebody else's file, arriving on somebody else's schedule, and nothing native reads it.

Matching is where it bites. Inventory updates key on SKU as an exact string, case included, so TurkeySandwich and Turkeysandwich are two different products. Trailing whitespace, leading zeros stripped the moment someone opens the CSV, and long numeric codes rendered in scientific notation break the match just as often, and the product CSV import keys on Handle, so the two-column file of SKU and quantity will not import without a workaround.

The sync apps do the plumbing well, then make you pre-answer the one question that only ever has an answer in context: what happens to a SKU missing from today's file. Zero takes the catalog offline the morning a column header changes; leave alone keeps selling a line discontinued in March. Inspect the file before trusting any of it, match on meaning rather than string equality, and buffer by velocity rather than *one global number*.
## What Shopify actually does, and where it stops

Shopify's inventory model itself is not the problem. Locations, quantities, committed stock, and the ability to stop selling at zero all work. What Shopify has no concept of anywhere in the platform is a supplier. There is no scheduled import, no FTP or SFTP client, no column mapping screen, no place to store a vendor's price and stock file, and no reconciliation report that tells you what last night's update changed. The platform assumes inventory moves because something sold or because a person typed a number.

Where it gets sharp is the matching. Shopify updates inventory by SKU and the comparison is an exact string match, case included, so TurkeySandwich and Turkeysandwich are two different products as far as the platform is concerned. Merchants have been raising this on the community boards for years and the behavior has not changed. Three neighbors of that problem show up constantly and are much harder to spot: trailing whitespace in the supplier's export, leading zeros stripped the moment somebody opens the CSV in Excel to take a look, and long numeric SKUs rendered in scientific notation. Then there is Shopify's own product CSV import, which is keyed on Handle. A supplier file with two columns, SKU and quantity, which is the most common shape of supplier file in the world, will not import without a workaround, and the community threads asking how to do it are years old and still open.

The reverse failure is quieter. Shopify will let two variants carry the same SKU without complaint. When that happens, the sync updates one of them and the other keeps selling stock that is already committed, which is the same overselling hole described in [the overselling problem no one automates](https://blog.dugong.live/how-to-prevent-overselling-on-shopify-across-channels.html), except the second channel is your own store.

> A sync app asks you what to do with an unmatched SKU once, at setup. The right answer changes with every file.

The instinct is to reach for [Shopify Flow](https://help.shopify.com/en/manual/shopify-flow), and Flow genuinely helps downstream. It can start a workflow when an inventory quantity changes, and it can tag the product, unpublish it, or ping a channel. What it cannot do is any part of the job that happens before that: it cannot fetch a file, parse a CSV or an XML feed, map a vendor's column names onto your fields, or compare thousands of rows against your catalog. It also cannot hold an opinion about the run as a whole, because every condition it evaluates reads one product in isolation, and the question that would have saved you this morning is a question about the file. Does this look like the feed we got yesterday. Flow has no way to ask that, which is the same structural wall behind [bundle inventory that never touches component stock](https://blog.dugong.live/how-to-sync-bundle-inventory-with-component-stock-on-shopify.html).

## Why the sync apps get you most of the way and then stop

This is not a knock on the tools. The dedicated inventory sync apps do the plumbing well, and if you are doing this by hand today one of them is a real upgrade. They schedule the fetch, speak FTP and HTTP and sometimes an API, parse CSV and XML and the occasional spreadsheet, let you map columns, and apply a safety buffer so you advertise fewer units than the supplier claims. All of that is solved.

What none of them can do is decide. Every one of these tools makes you pre-answer, in a settings dropdown, the single question that only ever has a right answer in context: what should happen to a SKU in your store that is not in today's file. There are two options. Set it to zero, and one malformed export takes your catalog offline. Leave it alone, and a line the supplier genuinely discontinued in March continues to sell into July. Merchants pick zero, because overselling feels like the worse sin, and then they live with the risk that a column header can cost them a Monday. There is no third option in the dropdown for figure out which of those two things actually happened, because that is not a setting. It is a judgment, and the tool has no way to hold one.

The buffer has the same shape. A single global number, say hold back three units, is too tight on the item that sells fifty a day between feed drops and absurdly wasteful on the one that sells two a week. The correct buffer is a function of velocity and feed frequency, and it changes as products move through their season, which means it is a number that should be recalculated continuously and instead gets typed once and forgotten, exactly like the thresholds behind [reorder points nobody revisits](https://blog.dugong.live/how-to-set-inventory-reorder-points-on-shopify.html).

## Why doing it by hand never keeps up

The manual version is a morning ritual and it is more common than the software industry likes to admit. Download three files. Open them in Excel. Run a lookup against your product export. Eyeball the mismatches. Fix the codes that changed. Paste the result into the bulk editor. Forty-five minutes on a good day, before the store has really woken up, and the whole thing has to be redone tomorrow because a stock file is worthless the moment it is a day old.

What actually breaks it is that the mapping never stays mapped. Suppliers rename SKUs. They add a prefix when they migrate warehouse systems, so ACM-4471 becomes UK-ACM-4471 overnight and every one of their four thousand lines fails to match. A pack of six becomes a pack of twelve under the same code, and now the number in the quantity column means something different than it did last week. A discontinued line comes back next season under a new code with the same product inside it. Each of those is a five-second call for a person who knows the catalog and an impossible one for a string comparison, and there are dozens of them a month across three suppliers.

And the ritual only runs when a person runs it. The feed that does not arrive at all is the failure nobody catches, because silence looks identical to everything being fine. Stock simply stops moving, the numbers on your storefront quietly go stale, and the first signal is a customer buying something that went out of stock four days ago.

## What the automation actually has to do

The working version is not a better importer. It is something that reads the file the way an experienced ops person reads it, which is skeptically, before touching a single product. As a Dugong playbook, in plain prose, it looks like this:

```
# trigger
On every supplier feed arrival, and on schedule
when one does not arrive

# steps
1. Inspect the file first: shape, row count, and how
   far it moves from yesterday, before applying
   anything
2. Match on meaning, not on string equality: case,
   whitespace, stripped zeros, new prefixes,
   renames, changed pack sizes
3. Judge every zero: really out of stock, quietly
   discontinued, renamed, or dropped by a broken
   export
4. Buffer by velocity, not by one global number
5. Apply what looks normal, hold what does not, and
   ask about the difference
6. Notice the feed that is late, thin, or quietly a
   different file than it used to be
```

Step one is the one that saves the Monday, and it is almost never built. Before any update is applied, the run compares the file against what a normal file from this supplier looks like: roughly this many rows, roughly this delimiter and encoding, these column names, this distribution of quantities, this much daily churn. A file that suddenly matches nothing is not an inventory event, it is a broken export, and the right response is to apply nothing and tell a human. A file where eleven percent of the catalog went to zero on a Tuesday in July is worth a question. A file where eleven percent went to zero the morning after a flash sale is just Tuesday.

Step three carries the rest of the weight. A missing row means four different things and the difference matters commercially. Genuinely out of stock means stop selling and [queue the restock alerts](https://blog.dugong.live/how-to-set-up-back-in-stock-notifications-on-shopify.html). Discontinued means stop selling, retire the page, and [redirect it before it 404s](https://blog.dugong.live/how-to-fix-404-errors-from-deleted-products-on-shopify.html). Renamed means match it to the new code and carry on. Dropped by a bad export means do nothing at all. A rule collapses all four into one behavior. A judgment that can look at the rest of the file, the supplier's history, and whether a suspiciously similar code appeared in the same run gets it right most of the time, and asks when it is not sure.

> **◆ NOTE** The trap is **the global rule for unmatched SKUs**. Whichever way you set it, you have chosen a failure mode in advance and agreed to accept it forever. Zero means one malformed file can take your catalog offline before breakfast. Leave alone means dead product sells for months. The honest answer is that the setting is the wrong shape for the problem, because the same missing row means different things on different mornings, and only something that can read the whole file can tell them apart.

## Why this is a compiler problem, not an app problem

Everything in this workflow is a small decision that depends on context nobody can encode in advance. Is this file trustworthy. Is this SKU the same product under a new name. Does this zero mean stop selling or ignore. How much stock should we hold back on this item today. Do we hide the product, keep taking orders with a longer lead time, or leave it up and eat the risk. Those answers depend on your supplier's reliability, your margin, your season, and how badly you want the sale, and they move week to week. A settings screen holds them badly in both directions.

It also sits in the middle of a neighborhood this desk keeps mapping. Downstream of a good sync is [hiding the sold-out variant](https://blog.dugong.live/how-to-automatically-hide-sold-out-variants-on-shopify.html) instead of showing a dead swatch, [pushing sold-out products to the bottom of the collection](https://blog.dugong.live/how-to-push-sold-out-products-to-the-bottom-of-a-shopify-collection.html), and [pausing the ads pointed at them](https://blog.dugong.live/how-to-automatically-pause-ads-for-out-of-stock-products-on-shopify.html) before the budget goes to a page nobody can buy from. Upstream of it is [routing each order to the right supplier](https://blog.dugong.live/how-to-automatically-split-and-route-shopify-orders-to-multiple-suppliers.html), which only works if you know who actually has the stock. And the same feed usually carries cost prices, which is the input to [the price change you make one product at a time](https://blog.dugong.live/how-to-bulk-edit-product-prices-on-shopify.html). Get the sync wrong and every one of those runs on bad numbers.

Picture a homeware store with three suppliers and 4,200 SKUs. On a Tuesday the largest supplier ships a file where the SKU column has picked up a UK- prefix after a warehouse migration nobody mentioned. Without the playbook, the matcher scores zero, the unmatched rule fires, 2,800 products go to zero at 6:06am, and the merchant spends the morning restoring quantities from a two-day-old export while ads burn. With it running, the file is flagged before anything is applied, the prefix is recognized as a systematic shift rather than 2,800 separate discontinuations, the mapping is proposed with a handful of genuinely ambiguous codes held back for a person, the safe updates go through on time, and the merchant reads a three-line summary over coffee instead of firefighting.

## The workflow worth building this week

If any part of your catalog depends on somebody else's stock file, you already have this problem, and the useful question is not whether the sync breaks but how long it takes you to find out. Start with the cheap half. Even a watcher that does nothing except tell you a feed is late, thin, oddly shaped, or moving more stock than usual, and refuses to apply it until you say so, removes the single worst outcome. That is the same compounding logic behind [the Shopify automations no one builds](https://blog.dugong.live/best-shopify-automations-to-set-up.html): the boring guardrail earns more than the clever feature.

Describe it the way you would brief a good ops hire on their first day: pick up each supplier's stock file when it lands, and before you touch anything, check it looks like their normal file; match their codes to our products even when they have changed the case, added a prefix, or renamed a line; when something is missing, work out whether it is out of stock, discontinued, renamed, or just fell out of a bad export, and only stop selling when it is one of the first two; hold back a little more stock on the fast movers than the slow ones; push through everything that looks normal and bring me the rest with your read on it; and tell me if a supplier goes quiet. That is the brief. The compiler handles the fetching, the parsing, the matching, and the timing, and your storefront stops advertising a version of reality that expired yesterday.

> **◆ READING** If this resonates, two companion pieces: our dispatch on [the overselling problem no one automates](https://blog.dugong.live/how-to-prevent-overselling-on-shopify-across-channels.html), which is what happens after a stale number reaches a checkout, and [the reorder you always make too late](https://blog.dugong.live/how-to-set-inventory-reorder-points-on-shopify.html), which fails for the same reason: a threshold typed once cannot keep up with a catalog that moves. Also worth reading: [the reorder you already placed](https://blog.dugong.live/how-to-stop-reordering-shopify-stock-you-already-have-on-order.html), on buying a second pallet because the incoming count reads zero.

If you are a Shopify merchant with a supplier feed story, a morning your catalog went to zero, or a mapping spreadsheet you have been maintaining by hand for three years, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Why did my supplier feed set all my Shopify products to zero?

Almost always because the matching failed and the sync was configured to treat an unmatched SKU as out of stock. Every inventory sync tool asks you this question once, at setup: if a SKU in your store is not found in today's file, should we leave it alone or set it to zero. Merchants pick zero because it is the safe answer against overselling. Then the supplier renames a column, adds a header row, exports with a different delimiter, or truncates the file, the matcher finds nothing, and the safe answer wipes the catalog in one pass. Nothing about the run looks like an error to the tool, because from its point of view it matched zero rows and applied the rule you gave it. The fix is not a different setting. It is a check on the file itself before any of it is trusted: is this file the shape yesterday's file was, does the row count make sense, and is a change this large plausible.

Permalink: https://blog.dugong.live/how-to-sync-supplier-inventory-feeds-to-shopify.html#faq-1

### Why does Shopify inventory sync fail when the SKU looks correct?

Because Shopify matches SKUs as exact strings and the match is case sensitive, so TurkeySandwich and Turkeysandwich are two different products as far as the platform is concerned. Merchants have raised this on the Shopify community boards for years. Three other things break the match just as often and are harder to see: trailing whitespace in the supplier's export, leading zeros stripped by Excel when someone opens the CSV to look at it, and a long numeric SKU read as scientific notation. There is also the reverse failure, where two variants share the same SKU. Shopify allows that, so the sync updates one of them and the other keeps selling stock that is already gone.

Permalink: https://blog.dugong.live/how-to-sync-supplier-inventory-feeds-to-shopify.html#faq-2

### Can Shopify Flow import a supplier stock file?

No. Flow reacts to things that happen inside Shopify. It can start a workflow when an inventory quantity changes and it can tag, unpublish, or alert on that product, which is useful downstream. It cannot fetch a file from an FTP server, parse a CSV or an XML feed, map a supplier's column names to your fields, or reconcile thousands of rows against your catalog. It also cannot form an opinion about the file as a whole, because every condition it evaluates reads a single product in isolation, and the question that actually protects you here is a question about the whole run: does this feed look like the feed we got yesterday.

Permalink: https://blog.dugong.live/how-to-sync-supplier-inventory-feeds-to-shopify.html#faq-3

### How do I stop a broken supplier feed from zeroing my Shopify catalog?

Inspect the file before applying it, which is the step almost nobody builds. Before any update runs, compare the feed against what a normal file from this supplier looks like: roughly this many rows, this delimiter and encoding, these column names, this much daily churn. A file that suddenly matches nothing is not an inventory event, it is a broken export, and the right response is to apply nothing and tell a human. Context decides the borderline cases: eleven percent of the catalog going to zero on a random Tuesday deserves a question, while the same movement the morning after a flash sale is just Tuesday. The inspection also catches systematic renames, like a SKU column that picks up a UK- prefix after a warehouse migration, which is one mapping shift rather than 2,800 separate discontinuations. Even a watcher that only flags a late, thin, or oddly shaped file and refuses to apply it removes the worst outcome.

Permalink: https://blog.dugong.live/how-to-sync-supplier-inventory-feeds-to-shopify.html#faq-4

### What inventory buffer should I set on a supplier feed sync?

Not one global number, which is the shape the sync apps offer and the wrong one. A hold back three units setting is too tight on the item that sells fifty a day between feed drops and absurdly wasteful on the one that sells two a week. The correct buffer is a function of velocity and feed frequency: how much a SKU can sell in the hours between updates, given that a once-daily feed leaves you exposed for up to nineteen hours after the supplier's warehouse actually runs out. That number changes as products move through their season, so it should be recalculated continuously rather than typed once at setup and forgotten. And pair the buffer with a silence alarm, because the feed that does not arrive at all is the failure nobody catches: stock simply stops moving, and the first signal is a customer buying something that sold out four days ago.

Permalink: https://blog.dugong.live/how-to-sync-supplier-inventory-feeds-to-shopify.html#faq-5

---

Markdown rendition of https://blog.dugong.live/how-to-sync-supplier-inventory-feeds-to-shopify.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
