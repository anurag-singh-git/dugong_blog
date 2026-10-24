# How to fix Shopify shipping rates that ignore product dimensions

> Shopify has no product dimensions field and quotes every order from one default box. The AI playbook that prices dimensional weight before checkout, not after.

- Canonical: https://blog.dugong.live/how-to-fix-shopify-shipping-rates-that-ignore-product-dimensions.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-09-18
- Updated: 2026-10-24
- Section: Research
- Word count: 2650
- Dispatch: Nº 118 · Research · 10 min read
- Full headline on page: How to fix Shopify shipping rates that *ignore product dimensions*
- Keywords: shopify product dimensions, shopify dimensional weight, shopify undercharging shipping, shopify shipping rates wrong at checkout, shopify default package size, shopify carrier calculated shipping, dimensional weight divisor 139, AI shipping automation
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

The order landed at 9:40 on a Friday night. One floor lamp, nine pounds on the scale, $11.40 of shipping collected at checkout.

Monday morning you box it. The box is 44 by 12 by 12, because a floor lamp is 44 inches long and nothing about that is negotiable. You buy the label. It costs $38.

Nothing malfunctioned. Shopify quoted the rate your carrier returned, and your carrier priced the only fact your store knows how to send, which is the weight. The box never entered the conversation, because there is nowhere in Shopify to put one.

## The short answer

Shopify has nowhere to store a box. A variant carries a weight and no length, width or height, not on the product, not on the variant, not in the shipping section of the admin. What the platform offers instead is one default package saved in Shipping settings, and every carrier-calculated quote your store sends out describes that same box whether the cart holds a phone case or a rug.

Carriers do not price parcels that way. UPS and FedEx bill the greater of actual weight and dimensional weight, which is length times width times height divided by 139, with every fractional inch rounded up since August 18, 2025. Surcharges stack on top once the cubic volume crosses the thresholds both carriers set in January 2026. The real cost then reaches you twice, in the label price and again in a price adjustment the carrier posts weeks later, and never at checkout.

The fix lives outside the platform. Store a length, width and height per variant yourself, keep a library of the boxes you really own, pack each cart into those boxes and return the greater of dimensional and actual weight through the Carrier Service API, which is the only route that computes a rate. Flow never sees that moment, because a rate request is not one of the events it can trigger on, and Delivery Customization functions only hide, rename and reorder options. Then reconcile every quote against its label and its adjustment, so the SKUs quoting under name themselves.

## Shopify stores a weight. It does not store a box.

Open any variant in the admin and you will find a weight field. Look for length, width or height, on the product, on the variant, anywhere in the shipping section, and there is nothing. The data model has a number for how heavy a thing is and no number for how big it is.

What it has instead is one default package. You save a box in Shipping settings, mark it default, and every carrier-calculated quote your store makes goes out describing that box, whether the cart holds a phone case or a rug. A September 2023 thread put it in one line that has not needed updating since: when it comes to Shopify shipping, there is a limitation, you can only designate a single default shipping box.

This is not a setting somebody forgot to ship. It was answered by a Shopify moderator on February 5, 2021, in the thread that first asked for product dimensions, in a single sentence: Shopify doesn't have support for that, we use an app called boxify. Five years on, that is still the answer, and Boxify is still the app in it.

## The community record

The February 2021 thread ran for two years and twenty-odd replies, and the tone in it is people discovering the same wall one at a time. How is that even possible, one merchant wrote, every vendor has multiple products and multiple box sizes. Another made the comparison that keeps coming up: if I list on Etsy, eBay, Bonanza or anywhere else, I don't have to worry about this issue. A third asked the question that actually names the defect. Why am I entering the dimensions to ship my items after the customer has already paid?

On November 11, 2021 a developer asked the technical version on the API forum: how do you pass a product's length, height and width into a CarrierService rate request? Nobody answered. Someone came back in April 2024 to ask whether it was possible yet. Nobody answered that either.

March 22, 2023, a merchant posts the receipt. Shopify is not charging enough for shipping, they wrote. I ship through Shopify and they calculated $9.69 when the shipping was nearly $13. Staff replied that the rates are provided via the carrier, not Shopify, and that discrepancies happen when order dimensions are slightly larger than listed. Which is true, and which quietly concedes the point, because the store was never given a place to list them.

January 21, 2024 is the thread everybody remembers, because the merchant stopped being polite in the title. When I ship with USPS or UPS I don't just give them the weight, they charge based on size as well, he wrote, and then: I am just in awe at the stupidity, a college student could code it into the system. Two staff replies arrived on March 9. The first pointed at custom package dimensions in Shipping settings, which is the default box again. The second named the third-party app and offered to share the feedback with the development team.

February 22, 2024, a merchant selling long, light products lays out the mechanism exactly. The calculation is completely wrong and under charging my customers due to lack of product dimensions. Some of my products are quite long and light so when shipping is calculated by weight only it under charges the customer. I really don't understand why the biggest ecommerce platform in the world doesn't have product dimensions as a standard for shipping. Support sent them to their carrier app vendor. Their reply to the app suggestions in the thread is the sentence the whole archive keeps arriving at: this should be a problem addressed by Shopify, not third party apps.

March 12, 2024 opens a thread that would collect more than a hundred replies. It is ridiculous that you need an app to do this, one of them reads, naming the $20 discrepancy on shipping for large and bulky items which was calculated with the default small box at checkout.

January 31, 2025, the same question with five more years of patience gone. How on earth does it make sense for Shopify to only calculate shipping based on one default package. I can't charge accurate shipping prices. The replies through February and May 2025 are app names and monthly prices, one of them rebranded mid-thread.

## The arithmetic the carrier runs and your checkout does not

Carriers stopped billing on weight alone a long time ago. UPS and FedEx bill the greater of actual weight and dimensional weight, and dimensional weight is length times width times height divided by 139.

Run the lamp through it. 44 by 12 by 12 is 6,336 cubic inches. Divided by 139 that is 45.6, which bills as 46 pounds. You collected shipping on nine. The carrier billed you on 46. The entire $27 gap is that one division, and no person in your store made a mistake to produce it.

Two recent changes widened it. On August 18, 2025 both carriers began rounding every fractional inch up before the division, so 9.1 inches becomes 10 and 5.01 becomes 6. A box measuring 11.1 by 8.5 by 6.2 used to come out at 5 pounds of dimensional weight and now comes out at 6, and it is the same box.

Then the January 2026 notices moved the volume thresholds. FedEx on January 12 and UPS on January 26 both set additional handling at 10,368 cubic inches and oversize at 17,280 cubic inches or 110 pounds. Those are surcharges. They stack on top of the dimensional weight, and they are triggered by exactly the number your checkout has never been told.

## The bill arrives twice, and only one of them is quoted

There is a second charge most merchants meet before they understand it. Shopify documents it plainly. A shipping label price adjustment occurs when you purchase a shipping label and the shipping carrier determines that you've provided inaccurate information that results in an incorrect shipping label price. One of the listed reasons is that the package dimensions specified on the label don't match the actual dimensions of shipment. After you ship, the carrier verifies the price, and if you paid an incorrect amount, then your carrier credits or debits you the difference, which shows up on your next bill.

So the true cost of an oversized order reaches you in two pieces, neither of them at checkout. The label price on the day, and an adjustment weeks later, arriving in a bill that is hard to attribute back to any single order. The customer paid once, in advance, on a number your store guessed with no dimensions in hand, and that transaction is closed. There is no version of this where you go back and ask for the other $27.

The quiet third cost is the overcorrection. Merchants who get burned twice usually give up on calculated rates and set a flat rate high enough to survive the worst box in the catalog. That works, and it prices the small orders out of the store, which is how a shipping data problem turns into a conversion problem nobody labels as one.

## Why Flow and the customization API do not reach this

The instinct is to automate around it, so it is worth being precise about which doors are locked.

[Shopify Flow](https://help.shopify.com/en/manual/shopify-flow) reacts to events that have already happened: an order created, a product updated, an inventory level crossed. A rate request is not one of them. There is no trigger that fires while the customer is standing at checkout waiting for a number, so Flow cannot be in that moment at all.

[Delivery Customization](https://shopify.dev/docs/api/functions/latest/delivery-customization) Functions look closer and are not. They do three things: hide an option, rename an option, reorder the list. None of them calculate anything. They cannot create an option and they cannot change a price. You can use one to suppress a rate you know is wrong. You cannot use one to produce the right one.

The [Carrier Service API](https://shopify.dev/docs/api/admin-graphql/latest/objects/DeliveryCarrierService) is the only route that computes, and that brings you back to the November 2021 question that never got an answer: the rate request that arrives at your endpoint carries the cart's weights, not a set of per-product dimensions, because the platform has none to send. Which means the dimensions have to live somewhere you own, and something has to do the packing arithmetic before the quote goes back, in the few hundred milliseconds the checkout will wait.

## What the automation actually has to do

Four jobs, and the apps do roughly one and a half of them. As a Dugong playbook, in plain prose:

```
# trigger
Every rate request, plus a
nightly pass over shipped
orders and carrier bills

# steps
1. Audit every sellable
   variant for a length,
   width, height and weight
2. Fill the gaps from
   supplier sheets, with a
   confidence on each guess
3. Queue the low-confidence
   ones for a person with a
   tape measure
4. Pack the cart into the
   boxes we really own, not
   one default package
5. Price dim weight at L x W
   x H over 139, inches
   rounded up, plus
   surcharges
6. Quote the greater of dim
   and actual through the
   carrier service endpoint
7. Reconcile quoted against
   label and adjustment,
   name the SKUs quoting
   under
8. Guard new variants saved
   with no dimensions before
   they can sell
```

**Fill the catalog.** Every sellable variant needs a length, a width, a height and a weight that matches a scale. Almost no store has this, because nobody has ever been asked for it by the platform. This is the part AI is unreasonably good at: read the supplier spec sheets, the packing lists, the PDFs in the shared drive, the manufacturer's own product page, and propose dimensions per variant with a confidence on each. Low confidence goes in a queue for someone to measure. High confidence goes in and gets checked by the loop below.

**Keep a real box library.** Not one default package: the boxes you actually own, with inner dimensions, wall thickness and the mailer sizes for the small stuff.

**Pack the cart before quoting it.** Given the items and the box library, choose the smallest set of boxes that fits, compute dimensional weight per box on the current divisor, take the greater of that and actual, add whatever surcharges the cubic thresholds trigger, and hand that back through the carrier service endpoint as the quote. This is the part the packing apps do.

**Close the loop.** This is the part nothing does, and it is the one that compounds. Every shipped order has three numbers: what you quoted, what the label cost, and what the adjustment corrected weeks later. Line them up. Where a SKU's quotes keep landing under its labels, the stored dimension is wrong, and the system should say which SKU and by how much rather than waiting for you to notice a margin dip in March. Adjust, re-measure the outliers, and the catalog gets more accurate every week instead of drifting.

Then guard the front door. A new variant saved with no dimensions, or a dimension that does not fit any box you own, should be flagged before it can take an order, because the cheapest moment to fix this is the one before something sells.

## Why this is a compiler problem, not an app problem

Box-packing apps solve the packing. What they do not solve is that your rules are not their rules. Never quote below cost on the 48-inch rods. Absorb up to three dollars on orders over $150 because the margin carries it. Ship the two-jar orders in the mailer, never the box. Anything over 10,000 cubic inches goes to the freight quote, not the parcel rate. Those are sentences, not settings, and they change the week your carrier publishes its January notice.

They also assume the data is already correct, which is the actual problem. An app that packs perfectly from dimensions nobody has verified produces confident wrong answers, which is worse than the default box, because at least the default box was obviously wrong.

## The workflow worth building this week

Read every sellable variant and find the ones with no dimensions. For those, pull what you can from the supplier sheets and the manufacturer pages, propose a length, width and height with a confidence score, and queue anything under the bar for someone to measure with a tape. Keep my box list current. When a rate is requested, pack the cart into my real boxes, compute dimensional weight on the current divisor with fractional inches rounded up, bill the greater of that and actual, add the surcharge if the cubic volume crosses the threshold, and quote that. Then every night, compare what I quoted against what the label cost and against any adjustment that landed since, and tell me which SKUs are consistently quoting under, with the dollars attached. Flag any new variant saved without dimensions before it can sell.

That is one paragraph, and it names three things the platform does not offer, one thing Flow cannot be present for, and a reconciliation loop that no app in the archive above was selling. The compiler turns it into a running workflow, and the store stops finding out what its boxes cost from a bill that arrives three weeks after the customer paid.

> **◆ READING** Two companion pieces if this one landed: [the bad address that ships anyway](https://blog.dugong.live/how-to-validate-shipping-addresses-on-shopify.html), on the other checkout field nobody validates until the carrier does, and [the parcel customs sends back](https://blog.dugong.live/how-to-fix-missing-hs-codes-on-shopify-before-customs-holds-your-orders.html), on the product data gap that costs you the whole shipment rather than part of it.

If you are a Shopify merchant with a dimensional weight story, the lamp that shipped for a third of its label, the flat rate you set too high and watched conversion fall, the adjustment line you could not trace to an order, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Does Shopify have a product dimensions field?

No. A Shopify variant has a weight field and no length, width or height field anywhere on the product, the variant, or the shipping section of the admin. The platform stores how heavy a thing is and not how big it is. What it offers instead is one default package saved in Shipping settings, and every carrier-calculated quote your store makes describes that same box whether the cart holds a phone case or a rug. A September 2023 community thread summarized it exactly: when it comes to Shopify shipping, there is a limitation, you can only designate a single default shipping box. This is long-standing and acknowledged. A Shopify moderator answered the first dimensions request on February 5, 2021 with one sentence, that Shopify does not have support for that and they use an app called Boxify, and the same app was still being recommended by staff in a March 2024 reply. Merchants who sell long, light or bulky items are the ones who feel it, because those are exactly the products whose price depends on volume rather than weight.

Permalink: https://blog.dugong.live/how-to-fix-shopify-shipping-rates-that-ignore-product-dimensions.html#faq-1

### Why is Shopify undercharging for shipping?

Because the rate request your store sends the carrier describes a weight and a default box, and the carrier prices the real box you actually ship. UPS and FedEx bill the greater of actual weight and dimensional weight, where dimensional weight is length times width times height divided by 139. A 44 by 12 by 12 box is 6,336 cubic inches, which is 45.6 and bills as 46 pounds, so a nine pound floor lamp quoted on weight alone misses by 37 pounds of billable weight before any surcharge. Shopify staff have confirmed the mechanism in the community: the rates are provided via the carrier, not Shopify, and discrepancies occur when order dimensions are slightly larger than listed. Merchants have posted the receipts for years, including $9.69 collected against a label that cost nearly $13 in March 2023, and a $20 discrepancy on large and bulky items calculated with the default small box at checkout in March 2024. Two carrier changes have widened the gap since: from August 18, 2025 both carriers round every fractional inch up before dividing, and in January 2026 both set additional handling at 10,368 cubic inches and oversize at 17,280 cubic inches or 110 pounds.

Permalink: https://blog.dugong.live/how-to-fix-shopify-shipping-rates-that-ignore-product-dimensions.html#faq-2

### Can I assign different package sizes to different products on Shopify?

Not natively. You can save several packages in Shipping settings, but only one is the default, and the default is what carrier-calculated rates are quoted against for the whole cart. There is no per-product or per-variant package assignment, which is why the request has stayed open in the community since 2021 and why the staff answer has been an app recommendation rather than a setting. Merchants regularly point out that Etsy and eBay listings do not have this problem, and one thread on the subject collected more than a hundred replies before it stopped. The workaround most stores end up with is either a box-packing app sitting on the Carrier Service API, or a flat rate set high enough to survive the largest item in the catalog, which protects the margin on bulky orders and quietly overcharges every small one.

Permalink: https://blog.dugong.live/how-to-fix-shopify-shipping-rates-that-ignore-product-dimensions.html#faq-3

### What is dimensional weight and what changed for 2025 and 2026?

Dimensional weight prices a parcel by the space it occupies rather than what it weighs. For UPS and FedEx the formula is length times width times height divided by 139, and you are billed on whichever is greater, the dimensional weight or the actual weight. Two changes matter for anyone quoting rates. From August 18, 2025 both carriers round every fractional inch up before the division, so 9.1 inches is measured as 10 and 5.01 as 6, which turned a box of 11.1 by 8.5 by 6.2 from 5 billable pounds into 6. Then in January 2026 both moved cubic volume thresholds onto the same footing, FedEx effective January 12 and UPS effective January 26, with additional handling applying over 10,368 cubic inches and oversize or large package charges over 17,280 cubic inches or 110 pounds. Those surcharges stack on top of the dimensional weight, and every one of them is triggered by a measurement Shopify never asked you for.

Permalink: https://blog.dugong.live/how-to-fix-shopify-shipping-rates-that-ignore-product-dimensions.html#faq-4

### Can AI fix Shopify shipping rates that ignore box size?

Yes, and the fit is specific. The job is four parts, and off-the-shelf packing apps cover about one and a half. First, fill the catalog: read supplier spec sheets, packing lists and manufacturer pages to propose a length, width and height per variant with a confidence score, and queue the low-confidence ones for someone to measure. Second, keep a library of the boxes you actually own with inner dimensions, not one default package. Third, pack each cart into those boxes before quoting, compute dimensional weight on the current divisor with fractional inches rounded up, bill the greater of that and actual, and add a surcharge when the cubic volume crosses the threshold. Fourth, and this is the part nothing on the app store does, reconcile every order's quoted rate against its label cost and against the adjustment the carrier posts weeks later, then name the SKUs that keep quoting under and by how many dollars. An automation like Dugong can also enforce your own rules in plain language, such as never quoting below cost on a given product line or routing anything over a cubic threshold to a freight quote. The honest limits: it cannot invent a measurement for a product nobody has ever measured, so the first pass on a messy catalog needs a tape and a person, and a rate returned through the Carrier Service API has to answer inside the checkout's timeout, so the packing logic has to be fast, not merely clever.

Permalink: https://blog.dugong.live/how-to-fix-shopify-shipping-rates-that-ignore-product-dimensions.html#faq-5

---

Markdown rendition of https://blog.dugong.live/how-to-fix-shopify-shipping-rates-that-ignore-product-dimensions.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
