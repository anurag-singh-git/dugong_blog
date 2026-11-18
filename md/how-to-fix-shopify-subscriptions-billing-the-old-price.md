# How to fix Shopify subscriptions billing the old price

> You raised the price in March. Your oldest subscribers are still paying the 2024 number, with a discount code you deleted, and the admin will never tell you.

- Canonical: https://blog.dugong.live/how-to-fix-shopify-subscriptions-billing-the-old-price.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-11-07
- Section: Research
- Word count: 2282
- Dispatch: Nº 140 · Research · 8 min read
- Full headline on page: How to fix Shopify subscriptions billing the old price *and dead discount codes*
- Keywords: shopify subscription price change existing subscribers, update subscription contract price shopify, shopify subscription old price, deleted discount code still billing, shopify subscription contract snapshot, delete subscription product shopify, subscription plan edit existing contracts, AI subscription audit
- Entities: Shopify (https://www.wikidata.org/wiki/Q7501150); Subscription business model (https://www.wikidata.org/wiki/Q1972241); Pricing (https://www.wikidata.org/wiki/Q2516951); Business process automation (https://www.wikidata.org/wiki/Q5001911)
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

You raised the price of the forty dollar coffee subscription to forty-six in March. Good decision, overdue, and the new signups have been paying it without a murmur ever since.

Last week you exported your subscription orders to work out why the category margin looked thin. Four hundred and twelve active contracts. Two hundred and sixty of them billing forty. Thirty-one billing thirty-four, which was a launch promotion you ran in 2024 and switched off the same year.

Nobody broke anything. Shopify did exactly what it is designed to do. The problem is that it never told you.

## The short answer

A Shopify subscription contract is a snapshot of the terms the customer agreed to, not a live link to your catalog. The price, the discount, the plan name and the variant are each copied onto the contract on the day the customer subscribes, and nothing you do in the admin afterwards goes back to change them.

So a price rise reaches new subscribers only. A discount code you deleted carries on taking money off every renewal it was ever attached to. A variant you deleted keeps getting billed on a line that resolves to nothing. All three are by design, and none of them appears anywhere in the admin as a warning.

The fix is not a setting. It is a report you do not currently have: every live contract, what it is actually billing, and how far that sits from what you would charge for the same thing today.

## A contract is a copy, not a link

Shopify's own API documentation is the clearest place this is written down, which is part of the problem, because merchants do not read API documentation.

A [subscription line](https://shopify.dev/docs/api/admin-graphql/latest/objects/SubscriptionLine) holds its own `currentPrice`, documented as the price per unit for the subscription line in the contract's currency. Not the variant's price. The line's price. It also holds its own copy of the plan it came from, and the documentation is unusually direct about what that means: the selling plan identifier may no longer match the plan's current attributes, and the selling plan name can differ from the plan's current name, because each of them can be updated independently.

Read that twice. Shopify is telling you, in the reference docs, that the thing on the contract and the thing in your admin are two separate records that are allowed to disagree.

Every subscription app has had to explain this to merchants, and they all land in the same place. Bold Commerce [writes](https://support.boldcommerce.com/boldsubscriptions/why-don-t-shopify-price-updates-automatically-affe) that price updates do not affect existing subscribers, because they stay subscribed under the terms they agreed to at checkout when the subscription contract was made. Recharge [writes](https://support.getrecharge.com/hc/en-us/articles/360008681974-Changing-the-price-of-subscription-products) that existing subscribers will still be subscribed to the old price, and that you change it by editing the customer's subscription, one at a time for a few or by CSV for many.

None of this is a bug, and I would not want it changed. You agreed a recurring price with somebody. A platform that silently repriced their standing order every time you edited a product would be a worse platform and, in several jurisdictions, an illegal one.

## The two screens that are each silent about the other

Here is why so few merchants know this. Shopify has two help pages a person would naturally read, and between them they leave the whole question unwritten.

The page on [managing subscription contracts](https://help.shopify.com/en/manual/products/purchase-options/subscriptions/shopify-subscriptions/manage-subscriptions/manage-contracts) covers a lot: editing the products, the quantity and the delivery frequency, with a note that updating the delivery frequency automatically updates the billing frequency. Adding, changing and removing billing dates. Pausing, resuming and cancelling on a customer's behalf. Skipping an upcoming order. It does not mention price.

The page on [adding and editing subscription plans](https://help.shopify.com/en/manual/products/purchase-options/subscriptions/shopify-subscriptions/manage-subscriptions/add-edit-plans) tells you to click the plan, edit the details and save, and warns that deleted plans are not recoverable. It says nothing about what editing or deleting a plan does to the contracts already running on it. It does say, in passing, that removing a plan from a product does not cancel any existing subscriptions for the product, which is the one hint that those contracts are living their own lives.

A merchant asked the direct question in a [community thread in March 2024](https://community.shopify.com/t/does-updating-price-on-shopify-subscription-plan-update-price-for-old-contracts-too/304528): if you update the price of a plan rather than a contract, in the middle of active subscriptions, does it update the price for all old and new customers or only new ones. The one reply answered a different question, about the app billing API. The merchant came back two days later to say they were not writing custom code and had no API access, and asked what the Shopify Subscriptions app does by default.

Nobody ever replied. Nothing in the thread is marked as a solution. Two and a half years on, that unanswered post is still one of the better pieces of evidence that this is a common question with no findable answer.

## The discount code you deleted is still taking money

This is the part that surprises even people who understand the price behavior, and it is recent enough that almost nothing has been written about it.

In October 2026 a developer [filed a detailed report](https://community.shopify.dev/t/discount-codes-on-subscriptions-combineswith-ignored-once-per-customer-bypassed-deleted-codes-still-billed/38200) on how discount codes behave on subscription contracts. The headline finding, in their words: billing attempts check nothing, and every code on the contract is applied to the order. That includes codes you deleted, expired or deactivated after they were attached.

Shopify's answer, after checking with the team that owns the subscriptions API, confirmed it rather than fixing it. Expired and deactivated codes continuing to bill is expected. Deletion behaves the same as expiry or deactivation. The saved snapshot stays until the app removes it.

Two more findings in the same thread are worth your attention. Discount codes added through the older contract creation and draft update flows are each evaluated on their own, so the combination rules that checkout would have enforced are not enforced there, though the newer calculation API does evaluate codes together and warns when they conflict. And a once-per-customer limit is checked against past orders and checkout reservations, never against discounts saved on contracts, so the same customer can carry the same code on several subscriptions at once. Shopify's suggestion was an app-side check, which is a courteous way of saying this one is yours.

Put all that together and the practical reading is simple. A launch code from two years ago is very probably still discounting somebody's monthly order, you will not find it by looking at the discounts page, and the only place it exists is on the contracts themselves. This is the same class of leak as [a code that double-dips a sale price](https://blog.dugong.live/how-to-stop-discount-codes-applying-to-sale-items-on-shopify.html), except that it renews.

## The variant you deleted is still being billed

Deleting a product does not stop the subscriptions that contain it. It orphans them. The line keeps the title and price it was created with and simply stops resolving to anything you sell.

The sharp edge of this was [reported in October 2024](https://community.shopify.dev/t/bug-subscriptions-with-deleted-products-get-inconsistent-insufficient-inventory-billing-failures/800), when contracts with deleted variants started failing billing with an insufficient inventory error. The reporter made the obvious point: the variant is deleted, so there is no inventory for a merchant to add. And the behavior was inconsistent. A contract with one deleted line and one live line billed successfully and produced an order containing the deleted item.

A Shopify engineer replicated it within four days, shipped a fix six days after the report, and restored what they called the original behavior: contracts with deleted variants do create orders. The original reporter confirmed it was working. Then, in August 2025, a different merchant turned up in the same thread with insufficient inventory errors and no explanation, asking whether customers should just resubscribe. No reply.

So the current state is the one that should bother you more, not less. Deleted variants bill quietly. The order goes out, the card is charged, and your warehouse gets a line for something you stopped selling. [One app's documentation](https://help.subi.co/en/articles/17565558-what-happens-to-a-subscription-when-its-product-is-deleted-or-replaced-in-shopify) states it plainly: deleting a product or variant does not change the subscriptions that include it, and the subscription keeps billing that line at its price on the subscription. Its advice is to swap the product on every affected contract while the old one still exists, and it notes that subscriptions whose discount cannot be carried over are not swapped in bulk at all, so those have to be done by hand.

Which means the order of operations matters more than almost anything else in this article. Swap first. Delete second. Never the other way round.

## What this costs on an ordinary month

Take four hundred active contracts on a product you now sell at forty-six dollars, billing monthly.

Two hundred and sixty are still on forty, from before the March rise. That is six dollars times two hundred and sixty, every month, which is fifteen hundred and sixty dollars of revenue you decided to charge and are not charging. Thirty-one are on a thirty-four dollar launch code you turned off in 2024, which is another three hundred and seventy-two. Call it just under two thousand a month, twenty-three thousand a year, on one product.

None of that appears as a problem anywhere. Your subscription revenue is growing. Your churn is fine. The only visible symptom is a margin that reads worse than your pricing says it should, and the natural explanation for that is shipping or packaging or the cost of goods, because those are the numbers you have a report for.

This is the characteristic shape of a snapshot problem. It does not fail. It drifts, and every month it drifts a little further, and the gap is widest on your oldest and most loyal customers, because they have been frozen the longest.

## What the automation actually has to do

As a Dugong playbook, in plain prose:

```
# trigger
Scheduled weekly contract sweep,
plus product price changed

# steps
1. List every contract and what
   it bills
2. Compare each line to today's
   price
3. Age the gap and price it
4. Audit the discounts riding on
   contracts
5. Check every line still has a
   variant
6. Make a price change a two-part
   job
7. Report the drift every month
```

Step one is the report nobody has. Read the live contracts, not the catalog, and write down what each line is actually billing. Most stores cannot produce this today, which is exactly why the drift survives.

Step two is the comparison. For every contract line, the price on the line against the price you would charge for that variant today. The output is a list of names and amounts, not an impression.

Step three turns that list into money. A dollar of drift on a contract that has billed monthly since 2024 is worth many times a dollar on one opened in September, so age each gap and total it. That number is what gets the work prioritized.

Step four is the discounts, and it is the one step that has no alternative. Read the codes sitting on live contracts, look each one up, and flag every code that is expired, deactivated or deleted. Nothing in the admin will do this for you, because as far as the discounts page is concerned those codes are gone.

Step five is the orphan check. Every contract line should resolve to a live variant. Any that does not is either billing for something you cannot ship or waiting to, and it got that way because somebody deleted a product in the right order for the catalog and the wrong order for the contracts.

Step six changes a habit rather than running a check. A price change is two jobs, not one: the catalog, then the contracts. Doing the first and intending to do the second next week is how every cohort in your store got frozen at a different number.

Step seven is the number that keeps it from coming back. Publish, every month, the share of your subscription revenue billing at current prices. If it is under ninety percent you have a pricing decision that is not being enforced, and now it has a name.

## Do this before you close the laptop

Three things, about fifteen minutes, no tooling required.

Open your subscription app, sort your active contracts by creation date, and look at the oldest ten. Note what each one bills. If you have raised a price at any point in the last two years, you are about to see the gap for yourself.

Then take the oldest promotional code you can remember running on a subscription product and check whether any live contract still carries it. If your app can filter contracts by discount, this takes a minute. If it cannot, that is its own finding.

Last, before you delete any subscription product this quarter, search your contracts for it first. The order of those two actions is the difference between a tidy catalog and a cohort of orders for something that does not exist.

> **◆ READING** Two companion pieces if this one landed: [the price change you make one product at a time](https://blog.dugong.live/how-to-bulk-edit-product-prices-on-shopify.html), on getting a new price into the catalog in the first place, and [the misprice that sells all night](https://blog.dugong.live/how-to-catch-pricing-errors-on-shopify-before-orders-flood-in.html), on the version of this problem that breaks in minutes rather than years.

If you sell subscriptions on Shopify and have a version of this story, the cohort still on a 2023 price, the launch code you found two years later, the deleted variant that kept shipping, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Does changing a product price in Shopify update existing subscriptions?

No. A price change in your catalog applies to new orders and new subscribers, and existing subscription contracts carry on at the price they captured when the customer signed up. Shopify's own API documentation is the clearest statement of why. A subscription line holds its own currentPrice, described as the price per unit for the subscription line in the contract's currency, and its own copy of the plan it was created from: the docs note that the selling plan identifier may no longer match the plan's current attributes, and that the selling plan name can differ from the plan's current name, since each can be updated independently. The contract is a copy, not a pointer. Every subscription app says the same thing in merchant language. Bold Commerce writes that price updates do not affect existing subscribers because they stay subscribed under the terms they agreed to at checkout when the subscription contract was made. Recharge writes that existing subscribers will still be subscribed to the old price. This is deliberate, and in most places it is also the legally safe default: you agreed a recurring price with a customer and you cannot quietly change it. The problem is not the behavior. The problem is that nothing in the admin shows you the gap, so a store two years into selling subscriptions is usually billing three or four different prices for the same product without anyone having decided to.

Permalink: https://blog.dugong.live/how-to-fix-shopify-subscriptions-billing-the-old-price.html#faq-1

### How do I update prices for existing Shopify subscribers?

One contract at a time, or in bulk through whichever app runs your subscriptions, and never by editing the product. Recharge's guidance is to change the price on the existing customer for a small number, and to use its multi-select or bulk CSV tools for a large one. Bold Commerce ships a bulk price update specifically for existing subscribers. The mechanics differ per app, so the useful work is upstream of the mechanics: know which contracts are off today's price and by how much before you open any of those tools. Two practical cautions. First, a price rise on an existing contract is a change to an agreed recurring charge, so tell the customer before it lands rather than after, and check what your own terms promised. Second, do the catalog and the contracts in the same session. The common failure is a store that raises the catalog price on a Monday, means to sweep the contracts on the Friday, and then forgets, which is how a cohort gets frozen at a price nobody remembers setting.

Permalink: https://blog.dugong.live/how-to-fix-shopify-subscriptions-billing-the-old-price.html#faq-2

### What happens to a Shopify subscription if I delete the product or variant?

The subscription keeps going, pointed at nothing. Deleting a product or variant does not change the subscriptions that include it: the line keeps its original title and price and simply stops resolving to anything in your catalog, and the contract keeps billing that line at the price stored on it. Removing a subscription plan from a product is just as quiet. Shopify's own documentation notes that doing so does not cancel any existing subscriptions for the product. The sharper version of this showed up as a developer bug report in October 2024, where contracts whose variant had been deleted started failing with an insufficient inventory error, and the reporter pointed out the obvious trap: you cannot add inventory to a variant that no longer exists. Worse, a two-line contract with one deleted variant billed successfully and produced an order containing the deleted item. Shopify replicated it within four days and restored the previous behavior, which is that contracts with deleted variants do create orders. That is the current state, and it is the state that should worry you more, because it means the failure is silent. The right move is to swap the product on every affected contract before you delete anything, and to keep a standing check that every contract line still resolves to a live variant.

Permalink: https://blog.dugong.live/how-to-fix-shopify-subscriptions-billing-the-old-price.html#faq-3

### Why is a deleted discount code still being applied to my Shopify subscription orders?

Because the code was copied onto the contract when it was added, and billing does not re-check it. A developer raised exactly this in October 2026, reporting that billing attempts check nothing and that every code on the contract is applied to the order, including codes deleted, expired or deactivated afterwards. Shopify's reply, three weeks later, confirmed the behavior rather than fixing it: expired and deactivated codes continuing to bill is expected, deletion behaves the same as expiry or deactivation, and the saved snapshot stays until the app removes it. The same thread records two related gaps. Codes attached through the older contract creation and draft update flows are evaluated independently of each other, so combination rules that checkout would have enforced are not, although the newer calculation API does evaluate them together and warns when codes conflict. And a once-per-customer limit is checked against past orders and checkout reservations, not against discounts saved on contracts, so one customer can carry the same code on several subscriptions. Shopify's own suggestion there is an app-side check, which is a polite way of saying this is yours to watch. Practically: a promotional code you ran for a launch two years ago is probably still taking money off somebody's monthly order, and the only way to know is to read the discounts sitting on live contracts rather than the discounts listed in your admin.

Permalink: https://blog.dugong.live/how-to-fix-shopify-subscriptions-billing-the-old-price.html#faq-4

### What happens to existing subscriptions if I edit or delete a subscription plan?

Shopify does not say, which is the honest answer and the reason this catches people. The help page for adding and editing subscription plans walks through editing a plan and saving it, and warns that deleted plans are not recoverable, and says nothing about what either action does to live contracts. The page for managing contracts covers products, quantity, delivery frequency, billing dates, pausing, resuming, skipping and cancelling, and does not mention price at all. So the two screens a merchant would use to reason about this are each silent on the half the other owns. The API fills the gap. A contract line stores the plan identifier it was created from and the plan name as it read at the time, and the documentation says plainly that both can diverge from the plan's current state because the plan and the line are updated independently. Read that as a rule: editing a plan changes what new subscribers get and leaves existing contracts exactly as they were. A merchant asked this directly in a March 2024 community thread, whether updating a plan price mid-subscription affects old customers or only new ones, and the thread never answered the question for the Shopify Subscriptions app. Nothing in it is marked as a solution. Two and a half years later it is still the clearest single piece of evidence that the question is common and the answer is not written down anywhere a merchant will find it.

Permalink: https://blog.dugong.live/how-to-fix-shopify-subscriptions-billing-the-old-price.html#faq-5

### Can AI fix Shopify subscriptions billing the wrong price?

It can find every one of them, price the problem, and stop it recurring, which is most of the job. An automation like Dugong reads your live contracts rather than your catalog, pulls what each line is actually billing, and compares it to today's price for the same variant, so instead of a vague sense that some subscribers are on old pricing you get a list with names, amounts and dates. It ages each gap, because a dollar of drift on a contract billing monthly since 2024 is not the same as a dollar on one opened in September. It reads the discounts sitting on contracts and flags any whose code is expired, deactivated or deleted, which is the one class of leak no screen in the admin will show you. It checks that every contract line still resolves to a live variant, so a deletion cannot quietly orphan a cohort. And it watches the catalog, so when a price changes it tells you the same day how many contracts just fell out of line, while you still remember why you changed it. The honest limits: it will not raise a customer's price for you, because that is a commercial and sometimes contractual decision rather than a data one, and the actual edit happens in whichever subscription app owns the contract. What it removes is the part that was never going to happen on its own, which is somebody noticing.

Permalink: https://blog.dugong.live/how-to-fix-shopify-subscriptions-billing-the-old-price.html#faq-6

---

## Read next

- [The price change you make one product at a time](https://blog.dugong.live/how-to-bulk-edit-product-prices-on-shopify.html): Shopify's bulk editor handles ten products, not ten thousand. The AI playbook that reprices a whole catalog without touching a spreadsheet.
- [The discount code that double-dips your sale](https://blog.dugong.live/how-to-stop-discount-codes-applying-to-sale-items-on-shopify.html): Shopify stacks a code on top of a sale price unless you stop it. The AI playbook that keeps promotions from eating each other.
- [The misprice that sells all night](https://blog.dugong.live/how-to-catch-pricing-errors-on-shopify-before-orders-flood-in.html): A missing decimal point sells out your bestseller at a tenth of cost. The AI playbook that catches a bad price in minutes, not mornings.
