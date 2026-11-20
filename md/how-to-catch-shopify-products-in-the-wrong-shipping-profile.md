# How to catch the Shopify products in the wrong shipping profile

> You built a custom shipping profile once. Every product you have added since went somewhere else, and the first person to notice is a customer who cannot check out.

- Canonical: https://blog.dugong.live/how-to-catch-shopify-products-in-the-wrong-shipping-profile.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-11-19
- Section: Research
- Word count: 2855
- Dispatch: Nº 144 · Research · 10 min read
- Full headline on page: How to catch the Shopify products in the *wrong shipping profile*
- Keywords: shopify new product not in shipping profile, shopify no shipping rates available, shopify shipping profile not working, shopify products missing from general profile, shopify shipping not available to this address, assign products to shopify shipping profile, shopify deliveryProfileUpdate variantsToAssociate, shopify shipping options by market
- Entities: Shopify (https://www.wikidata.org/wiki/Q7501150); Freight rate (https://www.wikidata.org/wiki/Q927345); Order fulfillment (https://www.wikidata.org/wiki/Q1473552); E-commerce (https://www.wikidata.org/wiki/Q484847)
- Section anchors: The short answer (https://blog.dugong.live/how-to-catch-shopify-products-in-the-wrong-shipping-profile.html#h-the-short-answer); Every new product goes to general, and nothing moves it (https://blog.dugong.live/how-to-catch-shopify-products-in-the-wrong-shipping-profile.html#h-every-new-product-goes-to-general-and-nothing-moves-it); One product, one profile, and what that does to a cart (https://blog.dugong.live/how-to-catch-shopify-products-in-the-wrong-shipping-profile.html#h-one-product-one-profile-and-what-that-does-to-a-cart); The two ways it costs you, and only one of them is visible (https://blog.dugong.live/how-to-catch-shopify-products-in-the-wrong-shipping-profile.html#h-the-two-ways-it-costs-you-and-only-one-of-them-is-visible); The threads all end the same way (https://blog.dugong.live/how-to-catch-shopify-products-in-the-wrong-shipping-profile.html#h-the-threads-all-end-the-same-way); What the API knows that the admin will not show you (https://blog.dugong.live/how-to-catch-shopify-products-in-the-wrong-shipping-profile.html#h-what-the-api-knows-that-the-admin-will-not-show-you); Shipping is moving to Markets, and the gap moves with it (https://blog.dugong.live/how-to-catch-shopify-products-in-the-wrong-shipping-profile.html#h-shipping-is-moving-to-markets-and-the-gap-moves-with-it); What the automation actually has to do (https://blog.dugong.live/how-to-catch-shopify-products-in-the-wrong-shipping-profile.html#h-what-the-automation-actually-has-to-do); Do this before you close the laptop (https://blog.dugong.live/how-to-catch-shopify-products-in-the-wrong-shipping-profile.html#h-do-this-before-you-close-the-laptop); Common questions (https://blog.dugong.live/how-to-catch-shopify-products-in-the-wrong-shipping-profile.html#faq-heading); Read next (https://blog.dugong.live/how-to-catch-shopify-products-in-the-wrong-shipping-profile.html#related-heading)
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

The new product went live on Tuesday. On Friday a customer in Manchester got as far as the shipping step and was told you do not deliver to her address.

You ship to Manchester five days a week. The rate is sitting in Settings, in the profile you built in March for everything that travels on a pallet.

The product was never in that profile. Shopify put it in the general one, the way it puts every new product in the general one, and told nobody.

## The short answer

Shopify adds every new product to the general shipping profile. Custom profiles are opt in, one product at a time, and nothing ever moves a new product into one for you. So the moment you build a second profile your catalog has two halves, and only one of them grows by itself.

A product cannot sit in two profiles at once, so the two halves never overlap and never warn each other. The failure lands at checkout in one of two directions: no rate at all for a destination the product's profile does not cover, or the cheap general rate on an item you meant to charge freight for. You lose the first one in silence. You pay for the second one.

Nothing in the admin lists the products a profile should hold and does not. The check has to run on the catalog rather than on the order: every profile, everything in it, every destination with no active rate, read daily, so a gap is one day old instead of one quarter old.

## Every new product goes to general, and nothing moves it

Shopify documents this accurately and in a tone that makes it sound like good news. The [shipping profiles page](https://help.shopify.com/en/manual/fulfillment/setup/shipping-profiles) says that all your existing and new products are added to the general profile, that you can create up to ninety nine custom profiles when some products need different rates, and that a product or variant which is not in a custom profile uses the general shipping rates.

Read those three sentences as a store that already has a custom profile and they stop being reassuring. New products go to general. Custom profiles are the exception you maintain by hand. There is no setting that makes your fragile profile, or your pallet profile, or your refrigerated profile the default for anything.

The predictable result shows up in the community every few weeks. In July 2022 a merchant posted that they had [just added several products and none of them appeared](https://community.shopify.com/c/payments-shipping-and/why-are-new-products-missing-from-my-general-shipping-profile/m-p/1675492) in their General profile. They had checked the obvious things first: requires shipping was ticked on every product, the stocking location was right, and General was their only profile so nothing else could be holding the items. The replies asked for screenshots and raised active versus draft status. The thread has no resolution. It is still one of the first results anyone finds when they go looking.

## One product, one profile, and what that does to a cart

The mechanism is in a 2021 thread, in an answer from Shopify's own support team, and it is the most useful paragraph written about this anywhere. Products not explicitly added to a custom profile default to the General profile, and [a product cannot be in two shipping profiles at the same time](https://community.shopify.com/c/payments-shipping-and/no-products-under-the-general-shipping-profile/m-p/1310423), so assigning a product to a custom profile removes it from General.

That makes a custom profile a replacement rather than an addition. It is worth saying out loud with numbers. Your general profile has zones for the United States, Canada and the United Kingdom. You build a custom profile for oversize goods and give it a single United States zone, because that is the problem you were solving on the day. Every product you move into it just lost Canada and the United Kingdom, and the admin showed you nothing, because from inside that profile the configuration is complete and correct.

The merchant in that thread was watching precisely this happen. Their customers in England were being told their location is not available for shipping. The support agent ran a test checkout, saw rates, and asked which rates were missing. Nobody joined the two halves of the store, and the thread closed with the question still open.

Mixed carts make it worse, in a way that is easy to misread as a bug. A cart holding one product from each profile has to be satisfied on both sides at once. If either profile has no rate for that address, the customer gets nothing, even though the other product in the cart is perfectly shippable and even though both products sell fine on their own. You cannot reproduce it by testing products one at a time, which is exactly how most people test.

## The two ways it costs you, and only one of them is visible

Direction one is the dead end. The customer reaches the shipping step, is told you do not deliver to their address, and leaves. They do not email you, because as far as they can tell your store is simply not for them. Shopify files the checkout as abandoned, where it sits looking identical to the hundreds of abandoned checkouts that were ordinary browsing. There is no error, no flag and no counter. The only number that moves is your conversion rate, by an amount too small to notice in a week and large enough to matter in a quarter.

Direction two is the invoice. The new oversize item is in the general profile, so it quotes the flat rate you wrote for everything else, and you ship a thing that costs four times that to move. Nobody at your end sees a problem, because the order looks healthy and the customer is happy. The cost arrives three weeks later folded into a carrier bill, spread across hundreds of shipments, in a line item nobody reconciles back to a product.

The two directions share a cause and nothing else, which is why most stores only ever find one of them. If you discovered this through a checkout complaint, go and look at your margins. If you discovered it through a carrier invoice, go and look at your abandoned checkouts.

## The threads all end the same way

In June 2025 a merchant added their first product that was not print on demand, diecast models they stocked themselves, and built a new profile with two zones: discounted United States rates and international DHL rates. Their test checkout answered [shipping not available to this address](https://community.shopify.com/t/shipping-problems-for-a-new-product/420805). Postal codes from other countries did not help either. Three people replied with the standard checklist, the merchant confirmed they had done all of it, and then wrote the sentence that belongs in every thread like this: they did not really know what to do at that point.

The one genuinely diagnostic thing they reported came next. A flat rate worked. So the problem was in the calculated rates, which is a different investigation entirely. A week later someone suggested removing the product from the General profile and adding named carrier services to the custom one. There is no reply confirming whether that fixed it.

Three years earlier an Irish store added [flat rates for the United Kingdom and Northern Ireland](https://community.shopify.com/c/shopify-discussions/newly-added-shipping-rates-not-showing-at-checkout/td-p/1648336) to a store that had only ever shipped domestically. Every British customer was told the store does not deliver to their destination. It took two weeks of screenshots to reach a diagnosis, and the diagnosis was that the products were not added, or the conditions were mismatched. The recommendation was to collapse everything back into one general profile holding all products, with both zones on it.

That recommendation is honest and it works. It also throws away the reason the second profile existed. Which is the real state of this problem: the native fix for a membership gap is to stop having more than one profile.

## What the API knows that the admin will not show you

Open Settings and Shipping and delivery and you get a list of profiles, each with a count of products in it. The count is true and almost useless, because the number you need is the one that does not exist: the products that should be in this profile and are not. Shopify cannot compute that, reasonably enough, because only you know what should ship like what.

The API is a different story. The [DeliveryProfile object](https://shopify.dev/docs/api/admin-graphql/latest/objects/DeliveryProfile) carries `profileItems` for the products and variants associated with the profile, `productVariantsCount` for how many variants are in it, `activeMethodDefinitionsCount` for the number of active shipping rates, `locationsWithoutRatesCount` for the number of locations with no rates defined, and `zoneCountryCount` for the number of countries with active rates to deliver to. The `deliveryProfiles` query takes `merchantOwnedOnly`, which returns only the profiles you created, so you can audit your own setup without tripping over the ones your shipping apps manage.

Those last three fields are the interesting ones. Read across every profile and you have a matrix of what ships from where to where, and the gaps in that matrix are the checkouts that will fail. A profile with a non zero `locationsWithoutRatesCount` is a profile where some of your stock is unsellable, today, and the admin reports it as a number on a settings page rather than as a problem.

Writing is the part that catches people out. A developer in October 2025 tried `productUpdate` with a [deliveryProfileId and was told ProductInput does not accept that argument](https://community.shopify.com/t/adding-products-or-variants-to-a-shipping-profile-with-api/572600), then tried the same thing from the product side again and got nowhere. The answer, from another developer rather than from the documentation, is `deliveryProfileUpdate` with `variantsToAssociate`. Note what that implies: association is per variant, not per product. A product with twelve variants is twelve associations, and the thirteenth variant somebody adds in February is a thirteenth gap.

## Shipping is moving to Markets, and the gap moves with it

This is worth knowing now rather than on upgrade day. Shopify's own page on the change says that [shipping is moving from shipping profiles to Markets](https://help.shopify.com/en/manual/fulfillment/setup/shipping-options/whats-changing-with-shipping), that shipping zones and location groups are replaced, and that each rate uses product conditions to set which products it applies to. Your rates are migrated for you; you do not recreate them.

Here is the part that matters for this article. Product based profiles become collections, unpublished so customers never see them, prefixed in square brackets with the word Shipping, so a Fragile profile becomes a Shipping Fragile collection. Those collections are then assigned automatically to the right product conditions on the migrated rates.

Nothing about the membership question has gone away. It has moved into a collection. If that collection is manual, your next product falls out of it exactly as it fell out of the profile. If it is automated on a tag or a product type, the gap moves one step upstream, to whether anyone tagged the product, which in most stores is a worse place for it to live rather than a better one. Either way something still has to check.

Three other changes are worth reading before your store is upgraded. Rates that share a shipping option name are consolidated into a single option. Within one option only the highest matching rate is charged, instead of the rates being added together, so a mixed cart's shipping total can move on upgrade day without anybody touching a setting. And split shipping is activated for every upgraded store, including stores that had deliberately turned it off. The rollout is gradual rather than dated, there is an opt out window once your store is upgraded, and when that window closes you cannot switch back.

## What the automation actually has to do

As a Dugong playbook, in plain prose:

```
# trigger
Daily pass over profiles and the
catalog, plus every new product

# steps
1. Pull every profile and
   everything in it
2. Flag the products no profile
   you built claims
3. Check each profile for a
   destination with no rate
4. Compare the new product with
   its siblings
5. Assign it, or hand it to a
   person
6. Test the checkout before
   calling it fixed
7. Report the gap the day it
   opens
```

Step one is the whole shipping configuration, not a sample of it. Every profile you own, its variants, its location groups and its zones, with app managed profiles kept separate so you are auditing your own decisions rather than an app's. This is the part that is tedious by hand and trivial for a machine, and it has to happen every day, because profiles change for reasons nobody logs.

Step two is the catalog comparison. Any product in the general profile that resembles the contents of a custom profile is a candidate. Resembles is doing real work in that sentence: same product type, same vendor, similar weight, a tag that matches, a title that matches the pattern. This is a judgment rather than a rule, which is why it has never been written as a Flow condition and never will be.

Step three is the other half, and the one that catches the problems nobody created today. Walk each profile and ask which countries it has active rates for and which of your locations have no rates defined at all. A profile that covers three countries when your general profile covers nine is not broken, but every product in it has lost six countries, and somebody should have decided that on purpose.

Step four is how the decision gets made without a human reading it. Take the new product and find the five products most like it, then look at which profile those five are in. If all five agree, you have an answer and a reason you can print. If they disagree, you do not have an answer, and pretending otherwise is how automation loses trust in week three.

Step five is the action, and it is per variant because the API is per variant. Confident cases get assigned and logged with the siblings that justified it. Ambiguous cases go to a person as one line with the evidence attached, which is a ten second decision rather than a research task. Anything that would remove a product from a profile should always be a person, because that is the direction that breaks a working checkout.

Step six is the test nobody runs. After an assignment, quote the rate for the destinations that were failing, from the location the stock actually sits in. A rate that exists in a profile and a rate that appears at checkout are not the same claim, as every merchant who has had the standard checklist read back to them already knows.

Step seven is the cadence, and it is the reason this is worth automating at all. A product that fell out of a profile on Tuesday and is found on Wednesday is a non event. The same product found in March, after the oversize items shipped at the flat rate all quarter and the Manchester customers quietly stopped trying, is a number on a spreadsheet you will argue about.

## Do this before you close the laptop

Three things, about twenty minutes, no tooling required.

Open Settings, then Shipping and delivery, and write down each custom profile with its product count. Then sort your products by date created and take the twenty newest. For each one, open it and check which profile holds it. If you have ever built a custom profile, expect to find at least one product in the wrong half. Most stores find several, and the oldest one is usually the most expensive.

Then take each custom profile and list the countries it has rates for next to the countries your general profile has rates for. Any country in the second list and not the first is a checkout that is failing right now for every product in that profile. Do the same for your locations if you ship from more than one, because a location with no rates in a profile makes that stock unsellable without saying so.

Last, run a test checkout with a mixed cart: one item from a custom profile and one from general, to an address in your furthest zone. It is the case that single product testing cannot see, and it is the case your customers create by accident every day.

> **◆ READING** Two companion pieces if this one landed: [the shipping rate that ignores your box](https://blog.dugong.live/how-to-fix-shopify-shipping-rates-that-ignore-product-dimensions.html), on the rate that is right in the settings and wrong for the parcel, and [the order from a state you cannot ship to](https://blog.dugong.live/how-to-restrict-shopify-products-from-shipping-to-certain-states.html), on the other place where Shopify's unit of shipping and your unit of shipping do not match.

If you run a store with a version of this story, the new product that quoted the wrong rate for a month, the customer who could not check out from a country you ship to weekly, the profile somebody built in 2023 that nobody has added a product to since, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Why are my new Shopify products missing from my shipping profile?

Because Shopify only ever adds them to one profile, and it is not the one you built. The help page says that all your existing and new products are added to the general profile, and that a product or variant that is not in a custom profile uses the general shipping rates. Nothing in that sentence moves a new product into a custom profile, and no setting anywhere turns it into a default. So the day you create your first custom profile your catalog splits in two: the general half, which grows by itself every time you add a product, and the custom half, which only grows when somebody remembers. A merchant in July 2022 posted the version of this that most people hit first. They had just added several products, none of them showed up in the General profile, the products were imported through a Printful integration, every one had the requires shipping box checked, and the stocking location was set correctly. The replies asked for screenshots and raised active versus draft status. The thread has no resolution and is still one of the first results for the question.

Permalink: https://blog.dugong.live/how-to-catch-shopify-products-in-the-wrong-shipping-profile.html#faq-1

### Why does Shopify checkout say there are no shipping rates for my customer's address?

Nine times out of ten the product in that cart is in a profile whose zones do not include the address, and almost always because the product moved profiles rather than because a rate was deleted. The order matters here. First check which profile holds the product, not whether the rate exists, because the rate almost certainly does exist in a profile that no longer applies. Then check that the profile holding the product has an active rate for both the destination country and the location the stock ships from. Then check whether the cart is mixed, because a cart with items from two profiles has to be satisfied on both sides. A merchant in July 2022 added flat rates for the United Kingdom and Northern Ireland to a store that had only ever shipped to Ireland, and every British customer was told the store does not deliver to their destination. The diagnosis, two weeks later, was that the products were not added or the conditions were mismatched. The recommendation was to collapse back to one general profile holding all products. That fix works. It also throws away the reason you made the second profile.

Permalink: https://blog.dugong.live/how-to-catch-shopify-products-in-the-wrong-shipping-profile.html#faq-2

### Can a Shopify product be in two shipping profiles at once?

No, and this is the single fact that explains most of the confusion. A Shopify support agent put it plainly in a September 2021 thread: products not explicitly added to a custom profile default to the General profile, and a product cannot be in two shipping profiles at the same time, so assigning a product to a custom profile removes it from the General profile. That means a custom profile is not an addition to your general rates. It is a replacement for the products in it. If your general profile covers the United States, Canada and the United Kingdom, and your new custom profile covers only the United States, then every product you move into it has just lost Canada and the United Kingdom. The merchant in that thread was watching exactly that happen to English customers and could not see why. Nobody in the thread connected the two halves, and it closed unresolved.

Permalink: https://blog.dugong.live/how-to-catch-shopify-products-in-the-wrong-shipping-profile.html#faq-3

### How do I assign products to a Shopify shipping profile with the API?

With the deliveryProfileUpdate mutation, passing variantsToAssociate inside the profile argument as a list of ProductVariant IDs. This catches out almost everyone who tries it from the product side first. A developer in October 2025 attempted productUpdate with a deliveryProfileId and got back that ProductInput does not accept that argument, then tried variantsToAssociate on the product input and got nothing. The working answer came from another developer in the thread, and the original poster confirmed it. Two details are worth carrying. The association is per variant, not per product, so a product with twelve variants is twelve associations and a thirteenth variant added later is a thirteenth gap. And on the read side, the deliveryProfiles query takes merchantOwnedOnly, which returns only the profiles created by the merchant, so you can audit your own profiles without tripping over the ones your shipping apps manage.

Permalink: https://blog.dugong.live/how-to-catch-shopify-products-in-the-wrong-shipping-profile.html#faq-4

### Can Shopify Flow catch a product that is missing from a shipping profile?

Not the thing you actually need it to catch. Flow can fire when a product is created and can tag it, add it to a collection or send a message, which is genuinely useful as a reminder step, and a tag plus an automated collection is the closest thing to a native guardrail that exists today. What Flow cannot do is answer the question that matters, which is whether this product is now in a profile that has an active rate for every destination it is meant to reach. That answer lives across delivery profiles, location groups and zones, and Flow does not read it. So Flow is good at the moment of creation and blind afterwards, which is the wrong shape for this defect, because the gap usually opens later: a new variant, a new location, a zone edited for one profile and not the other. This needs something that reads the whole shipping configuration on a schedule and compares it with the catalog.

Permalink: https://blog.dugong.live/how-to-catch-shopify-products-in-the-wrong-shipping-profile.html#faq-5

### What happens to my shipping profiles when my store moves to shipping options by market?

The profiles stop being the unit and the membership problem moves into collections. Shopify's own page on the change says shipping is moving from shipping profiles to Markets, that shipping zones and location groups are replaced, and that each rate uses product conditions to decide which products it applies to. Product based profiles become unpublished collections prefixed with Shipping, such as Shipping Fragile, and those collections are assigned to the product conditions on the migrated rates. Read that as an operator rather than a reader. Nothing about the question has gone away. If the new collection is manual, your next product falls out of it exactly as it fell out of the profile. If it is automated on a tag or product type, the gap moves upstream to whether anyone tagged the product. Three other changes are worth knowing before upgrade day: rates sharing a shipping option name are consolidated into one option, within an option only the highest matching rate is charged instead of rates being added together, and split shipping is turned on for every upgraded store including the ones that had turned it off. The rollout is gradual, there is an opt out window after your store is upgraded, and once that window closes you cannot switch back.

Permalink: https://blog.dugong.live/how-to-catch-shopify-products-in-the-wrong-shipping-profile.html#faq-6

---

## Read next

- [The shipping rate that ignores your box](https://blog.dugong.live/how-to-fix-shopify-shipping-rates-that-ignore-product-dimensions.html): Shopify has no product dimensions field and quotes every order from one default box. The AI playbook that prices dimensional weight before checkout, not after.
- [The order from a state you cannot ship to](https://blog.dugong.live/how-to-restrict-shopify-products-from-shipping-to-certain-states.html): Shopify restricts shipping by zone, not by product, and a mixed cart breaks the workaround. The AI playbook that blocks only the items a state bans.
- [The bad address that ships anyway](https://blog.dugong.live/how-to-validate-shipping-addresses-on-shopify.html): Shopify warns about a bad address, you ship anyway, and the package bounces back. The AI playbook that catches undeliverable addresses before the label prints.
