# How to restrict Shopify products from shipping to certain states

> Shopify restricts shipping by zone, not by product, and a mixed cart breaks the workaround. The AI playbook that blocks only the items a state bans.

- Canonical: https://blog.dugong.live/how-to-restrict-shopify-products-from-shipping-to-certain-states.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-09-19
- Updated: 2026-10-24
- Section: Research
- Word count: 2500
- Dispatch: Nº 119 · Research · 9 min read
- Full headline on page: How to restrict Shopify products from shipping to *certain states*
- Keywords: shopify restrict shipping to certain states, shopify block states, restrict product by state shopify, shopify shipping profiles state restriction, shopify restrict shipping by zip code, shopify checkout validation, shopify state compliance, AI compliance automation
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

The order lands at 11:40 on a Saturday night. Four tins of hemp gummies, paid in full, shipping to an address in Boise.

Idaho is one of the states you cannot send that to. Your store took the money anyway, printed a label option, and sent a cheerful confirmation email. Nothing in Shopify knows which of your products are legal where, so nothing in Shopify had an opinion.

You will spend Monday refunding it and writing an apology that has to sound like a policy rather than a mistake. Then it happens again, because the setting you are about to go looking for does not exist.

## The short answer

Shopify restricts shipping by zone, and a zone belongs to the whole store, so unchecking Idaho stops every product reaching Idaho. No field on a product says where that product may not go. The only product-level lever is the shipping profile, and you get up to 99 custom ones, so you move the restricted items into a profile of their own and leave the banned states with no rate at all.

The restriction is then an absence rather than a rule, and it breaks in two places. Shopify adds rates together across profiles, so a cart holding one restricted item and one ordinary one pays shipping twice, which the documentation describes as intended. And when the restricted profile has no rate for the buyer's state, checkout fails the whole delivery step, so the legal items in the basket go down with the banned one.

Zones also stop at the state line, so a dry county or a township cannot be expressed at all, and nothing in the settings records when a rule last changed. Enforcement has to run before the charge. A cart and checkout validation function can block checkout progress when business rules are not met, and Shopify names restricted shipping locations as an example use, but it is an empty box until something classifies your catalog and keeps the rules current. Flow runs after the order exists, so it can only tag, hold or cancel a sale you have already taken.

## Shopify restricts by zone, not by product

Shipping in Shopify is organized around zones. A zone is a list of countries and, inside a country, a list of states or provinces that you are willing to quote rates for. Uncheck Idaho and you have stopped shipping to Idaho. All of it. The gummies, the t-shirts, the sticker packs, the thing your best customer in Boise orders every month.

That is the answer merchants get first, and it is why the follow-up question always arrives about a week later. On November 13, 2023 someone asked the plain version, how to sell in the USA but not in all states, and was told to build a US zone and deselect the states they did not want. Correct, and store-wide, which is the opposite of what a restricted-product merchant needs.

The only product-level lever Shopify gives you is the [shipping profile](https://help.shopify.com/en/manual/fulfillment/setup/shipping-profiles), which the documentation describes as a set of shipping rules for specific products and locations. You get up to 99 custom profiles on top of the general one. Move the restricted items into a profile of their own, then build that profile's zones without the states you cannot serve.

Notice what you have actually built. There is no rule anywhere saying this product may not go to Idaho. There is only an absence: no rate exists, so checkout has nothing to offer. The restriction is a hole in a table, and holes are hard to audit, hard to explain to a new hire, and completely silent when someone widens a zone six months from now.

## The workaround, and the two ways it breaks

This approach has been the standing recommendation for years. On June 18, 2021 a merchant asked how to stop CBD shipments reaching four states, and a Shopify moderator answered the same day: make a custom profile for those products and make sure no shipping rates exist for those states. Clear, official, and it holds right up to the moment a customer puts two different kinds of thing in one basket.

The first break is the bill. Shopify's own documentation on [combining rates across profiles](https://help.shopify.com/en/manual/fulfillment/setup/shipping-profiles/combined-shipping-rates) says the separate shipping rates for each product are combined and a single shipping rate is displayed to your customer at checkout, and that rates with the same name are added together, even those in different shipping profiles. Added together. Not the higher of the two. A cart with one restricted item and one ordinary one pays shipping twice.

A merchant named it on May 8, 2023, in the flat tone of someone who had already argued about it: charging twice as it's the default shopify behavior, it cannot be changed. Another came back to the same thread on June 17, 2024 to report that customers get double-charged shipping, and added the line that ends most of these threads. After talking to Shopify Support they have no solution.

The second break costs more and gets discussed less. When the restricted profile has no rate to the buyer's state, checkout does not quietly drop that one item. It fails the whole delivery step. The customer is told you do not ship to their address, and the legal half of the basket goes down with the illegal half. You have not blocked a sale you were not allowed to make. You have blocked a customer.

And the setup itself is fragile. On June 18, 2021 another merchant asked how to restrict a set of products to Virginia only, got the profile instructions, and came back on July 6, 2021 with three words that will be familiar to anyone who has tried this: this still isn't working. All fifty states were still showing at checkout. No staff member returned to the thread. Three years later, in June 2024, the answer posted there was the name of a paid app.

## The community record

Laid end to end, the threads read like one conversation held five times with different people.

June 18, 2021, CBD into four states: use shipping profiles, answered by a moderator. June 18, 2021, products restricted to Virginia: use shipping profiles, still broken three weeks later. May 1, 2023, what is the best way to restrict certain states from purchasing certain products: profiles, and then the double-charge problem. June 13, 2023, a staff member arrives, asks about plan and carrier setup, and recommends an app. June 18, 2024, another app. October 22, 2025, a merchant needs to exclude specific areas within states and is told, correctly, that it cannot be done natively at all.

The most recent entry is the most telling. On August 7, 2026 a merchant returned to the 2023 thread to point out that checkout extensibility now gives apps a validation hook that avoids the double-charge trap, and framed it exactly right: there is still no native fix. Five years, and the platform answer is the same absence of a rate it was in 2021.

> **◆ NOTE** The record, compressed: zones are store-wide, profiles are the only product-level lever, and a profile restricts by having no rate. Mixed carts either pay twice, default behavior, cannot be changed, or fail entirely and take the legal items with them. Asked June 2021, answered with profiles. Asked May 2023, answered with profiles and an app. Asked October 2025 below the state line, answered not possible. Noted August 2026: still no native fix.

## The map moves faster than the setting

Even a perfectly built profile is a photograph of the law on the day you built it.

Take hemp. Federal restrictions on hemp-derived THC products were due to take effect on November 12, 2026, then moved to December 11, 2026 by a continuing appropriations bill the House passed 370 to 48 on September 1, 2026. That is one date change, thirty days of notice, decided in a week. Underneath it sits a state patchwork that rewrites itself every legislative session. Nobody is going to remember to open the shipping settings.

Alcohol is worse, because the line is not the state line. Six states restrict direct-to-consumer shipment into dry territory, and in two of them the geography is real: Alaska has roughly 75 dry communities, Arkansas has 29 dry counties plus 24 that are partly wet and partly dry. Those boundaries are drawn by townships, precincts and local votes, not by postcodes or city limits, and a single local election redraws one.

Shopify cannot express any of it. A merchant asked on October 22, 2025 how to exclude specific areas within states and got the accurate answer the next morning: Shopify's native shipping zones only let you include or exclude entire states or countries, so there isn't a way to blacklist specific postcodes without using a workaround. A second reply said the same thing in fewer words. Shopify only lets you block shipping at the state level.

> A shipping zone answers where will you quote a rate. Compliance asks what is this thing, and where is it allowed to arrive. Those are not the same question, and only one of them has a settings page.

## What a real check has to know

Strip away the workarounds and the job has four inputs, none of which live in your shipping settings.

What the product is. Not a tag someone remembered to add, but the actual attribute the rule cares about: the cannabinoid, the alcohol by volume, the blade length, the aerosol classification, the nicotine. Your catalog knows it in titles, descriptions, ingredient lists and supplier sheets. Your shipping settings have never read any of that.

Where the order is really going, resolved below the state field when the rule is drawn below it. Then the rule itself, with a date on it, because a rule without a date cannot tell you whether it is stale. And finally a decision point early enough to matter, which means before the charge, not after it.

That last one rules out the tool most merchants reach for. [Shopify Flow](https://help.shopify.com/en/manual/shopify-flow) runs on orders that already exist, so the best it can do is tag, hold or cancel a sale you have already taken. For compliance that is a record of the problem, not a fix. The surface that can actually stop a checkout is a [cart and checkout validation function](https://shopify.dev/docs/apps/build/checkout/cart-checkout-validation), which runs on Shopify's servers and can block checkout progress when business rules are not met. Shopify's own documentation lists preventing shipping to restricted locations as an example. It is the right enforcement point. It is also an empty box until something tells it what the rules are.

## What the automation actually has to do

As a Dugong playbook, in plain prose:

```
# trigger
Every cart that reaches
checkout, plus a nightly
catalog and rules pass

# steps
1. Classify each product
   once: what it is, which
   rules touch it
2. Resolve the address
   below the state line:
   county, township, ZIP
3. Check the cart line by
   line, not as a single
   basket
4. Block only the restricted
   lines, let the rest of
   the order check out
5. Say why, in plain words,
   at the point where it
   fails
6. Re-read the rule set
   nightly and surface every
   dated change
7. Log every block with the
   rule and date that
   caused it
```

Step one is the unglamorous half of the work and the half that decides whether the rest is worth anything. A rule set is useless against a catalog that has not been classified, and classification is exactly the sort of reading job that used to require a person with a spreadsheet and now does not.

Step four is where the money is. The profile workaround treats a cart as one decision, so a restricted item poisons the whole order. Checking line by line turns a lost order into a smaller one. The customer buys the three things you are allowed to send them, sees a clear note about the fourth, and does not go looking for a competitor who will ship all four.

Step five sounds cosmetic and is not. A generic no shipping available at this address message produces a support ticket and, often enough, a second attempt with a friend's address. Naming the item and the reason ends the conversation and leaves you with a record that you told them.

Step six is the one that ages well. When the hemp date moves by thirty days, or a state adds a product category in April, the workflow should notice, show you the change, and wait for you to accept it. An automation that silently starts refusing orders because it read a news item is worse than no automation. Propose, then enforce.

## Why this is a compiler problem, not an app problem

Every app in these threads solves one slice. Some hide shipping methods by state code. Some validate postcodes. Some block countries. All of them need you to maintain the list, and none of them know what your products are.

The reason this stays unsolved is that the rule is not really about shipping. It is a sentence about your business, and it sounds like this: we do not send anything containing THC to the states that ban it, we do not send spirits into dry counties, we never send aerosols by air, and if a cart has one of those in it we block the line and sell the rest. That sentence is already complete. What has been missing is anything that can turn it into a check that runs at checkout.

That is the whole argument for describing workflows in language and compiling them. The merchant holds the judgment, which is theirs by law and by license. The compiler holds the plumbing: the classification pass, the address resolution, the line-level decision, the validation function, the log. Nobody has to translate a compliance policy into an absence of shipping rates and then remember, a year later, why Idaho is missing from a table.

## The workflow worth building this week

Start narrow. Take the one product category that actually carries risk, write the rule as a sentence with the states in it, and put the check in front of checkout rather than behind the order. Then add the nightly pass that re-reads the rules, because the date is the part that will catch you out.

Everything else is refinement. But the store stops taking money it cannot keep, and you stop finding out about it at 11:40 on a Saturday night.

> **◆ READING** Two companion pieces if this one landed: [the bad address that ships anyway](https://blog.dugong.live/how-to-validate-shipping-addresses-on-shopify.html), on the other half of the checkout that nobody validates, and [the parcel customs sends back](https://blog.dugong.live/how-to-fix-missing-hs-codes-on-shopify-before-customs-holds-your-orders.html), on what happens when the rule you missed is enforced at a border instead of a state line.

If you are a Shopify merchant with a restricted shipping story, the refund you wrote on a Monday, the cart that charged twice, the customer who could not buy a t-shirt because of a tin of gummies, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Can I stop one Shopify product from shipping to certain states?

Not directly, and that is the whole problem. Shopify restricts shipping with zones, and a zone belongs to the store, so unchecking Idaho stops every product going there, not just the one that is restricted. The only product-level lever is a shipping profile, which is a set of shipping rules for specific products and locations. You move the restricted items into their own profile and simply give that profile no rate for the states in question, which makes the restriction an absence rather than a rule. That is the answer a Shopify moderator gave on June 18, 2021 to a merchant who needed to keep CBD out of four states, and the same answer merchants were still passing around in 2026. It works only while the restricted item is alone in the cart. There is no field on a product that says where it may not go, no report of which products are blocked where, and nothing that tells you when a rule changed.

Permalink: https://blog.dugong.live/how-to-restrict-shopify-products-from-shipping-to-certain-states.html#faq-1

### Why does Shopify charge shipping twice when I use two shipping profiles?

Because that is what Shopify does by design when one cart draws from more than one profile. The documentation is explicit: the separate shipping rates for each product are combined and a single shipping rate is displayed to your customer at checkout, and rates with the same name are added together, even those in different shipping profiles. Add together is the operative phrase. A cart with one item from your general profile and one from your restricted profile gets the sum of two rates, not the higher of them. A merchant put it flatly on May 8, 2023: charging twice as it's the default shopify behavior, it cannot be changed. Another merchant reported in June 2024 that customers get double-charged shipping and added, after talking to Shopify Support they have no solution. The usual workaround is to name the rates identically and hope the arithmetic lands somewhere defensible, or to apply a discount equal to the smaller rate, which is a coupon covering a bug.

Permalink: https://blog.dugong.live/how-to-restrict-shopify-products-from-shipping-to-certain-states.html#faq-2

### Can Shopify block shipping to a specific ZIP code or county?

Not natively. Shopify zones are built from countries and their states or provinces, and they stop there. A merchant asked on October 22, 2025 how to exclude specific areas within states, and the reply the next day was direct: Shopify's native shipping zones only let you include or exclude entire states or countries, so there isn't a way to blacklist specific postcodes without using a workaround. A second reply put it the same way, that Shopify only lets you block shipping at the state level. This matters more than it sounds, because several real restrictions are drawn below the state line. Six states restrict direct shipment of alcohol into dry territory, and those boundaries follow townships, precincts and county votes rather than ZIP codes or city limits, so a postcode list is an approximation that a single local election can invalidate. Getting below the state line means resolving the address against the boundary that actually governs it, which is work no shipping zone was designed to do.

Permalink: https://blog.dugong.live/how-to-restrict-shopify-products-from-shipping-to-certain-states.html#faq-3

### Can Shopify Flow stop an order to a restricted state before it is placed?

No. Flow is an order-level automation that runs after the order exists, so the earliest it can act is to tag, hold or cancel an order you have already accepted and, in most setups, already charged. For a compliance restriction that is the wrong side of the line: you did not prevent the sale, you made a record of it and then wrote to the customer. The surface that can actually stop a checkout is a cart and checkout validation function, which runs on Shopify's servers and can block checkout progress when business rules are not met, with preventing shipping to restricted locations named as an example use. It is app territory rather than a setting, it needs the logic written and maintained, and it needs something to tell it which products are restricted where. The validation function is the enforcement point. It is not the answer to what the rule should be today.

Permalink: https://blog.dugong.live/how-to-restrict-shopify-products-from-shipping-to-certain-states.html#faq-4

### Can AI handle state shipping restrictions on a Shopify store?

Yes, because the hard parts of this job are reading and matching, not enforcement. There are three of them. Classifying the catalog: deciding that this tin is a hemp product, that bottle is a spirit and that folding knife is blade-length restricted, read from titles, descriptions, ingredients and supplier sheets rather than from a tag somebody remembered to add. Resolving the destination below the state line when the rule is drawn by county or township. Keeping the rule set current, which is the part that quietly rots, since state law changes on its own schedule and the federal hemp THC restrictions alone moved from November 12, 2026 to December 11, 2026 on a bill passed on September 1, 2026. An automation like Dugong holds those rules in plain language, classifies every new product as it is saved, checks each cart line by line so only the restricted line is blocked and the rest of the basket still checks out, writes the explanation the customer sees, and logs every block against the rule and the date that caused it. The honest limits: it will not tell you whether you hold the license a state requires, and a rule change needs a human to accept it before it starts refusing orders.

Permalink: https://blog.dugong.live/how-to-restrict-shopify-products-from-shipping-to-certain-states.html#faq-5

---

Markdown rendition of https://blog.dugong.live/how-to-restrict-shopify-products-from-shipping-to-certain-states.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
