# How to set up back-in-stock notifications on Shopify

> Shopify has no real back-in-stock automation, so the customer who asked never hears and a competitor sells it instead. The AI playbook that fixes it.

- Canonical: https://blog.dugong.live/how-to-set-up-back-in-stock-notifications-on-shopify.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-06-13
- Updated: 2026-08-10
- Section: Research
- Word count: 2010
- Dispatch: Nº 56 · Research · 9 min read
- Full headline on page: How to set up *back-in-stock notifications* on Shopify
- Keywords: Shopify back in stock automation, restock notifications, back in stock alerts, notify me when available, stockout recovery, waitlist automation, inventory alerts Shopify, back-in-stock email
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

Spend an evening in the Shopify community forums or the merchant subreddits and you will find the same quiet question asked a hundred different ways. How do I let customers know when something is back in stock? People expect the answer to be a setting. It is not. The thread that follows is always the same shape: someone explains that the built-in notify me form only collects an email, that it does not actually send anything, that you have to export the list and message people yourself, and that by the time you do, the restock is already gone. The disappointment is not that the feature is hard. It is that everyone assumed it existed.

Here is the part that makes it expensive. A customer who clicks notify me when this is available has done the single most valuable thing a shopper can do. They have told you exactly what they want and handed you a way to reach them. They are not a cold lead. They are a warm, self-identified buyer waiting with their wallet out. And in most Shopify stores, that request lands in a void. The item comes back, the page goes live, and the people who raised their hands hear nothing.

> A back-in-stock request is the only lead that asks you to sell to it, and most stores answer it with *silence*.

## How big the leak actually is

Stockouts are not a small tax on a store. They account for roughly forty percent of lost sales, and the lost sales ratio, the share of revenue a store misses because items were not available to buy, runs around twenty to thirty percent in ecommerce. That is not a rounding error. That is a fifth of the top line walking out the door because the shelf was empty at the moment of intent.

And shoppers do not wait politely. When a product is out of stock, about sixty nine percent of online shoppers will go buy it from a competitor rather than come back later. A stocked-out product stays unavailable for an average of around thirty five days, which is more than a month of a page that converts visitors into a shrug. The back-in-stock list is the one tool that fights all of this directly, because it captures the intent at the exact moment it is highest and gives you a way to act on it the instant supply returns. Leaving that list unworked is leaving the most recoverable revenue a store has on the table.

## What Shopify actually does, and where it stops

Shopify is excellent at the things adjacent to this and silent on the thing itself. It tracks inventory, it knows the moment a variant crosses from zero back to one, and many themes will even show a notify me form on a sold-out product. What it does not do is close the loop. There is no native feature that emails or texts the people who asked when the item returns. The gap is real, and it shows up in three ways.

First, **the request goes nowhere**. The theme-level notify me form, where it exists at all, collects an email into a list. It does not watch inventory and it does not send. The standard advice in the forums is to export the addresses and email them yourself, which means the restock alert only fires when a human remembers to fire it, and only as fast as that human can work a spreadsheet.

Second, **the blast sells out to the wrong people**. Say two hundred people are waiting and forty units land. The moment you do send, one undifferentiated email pushes all two hundred to the page at once, the forty units go to whoever clicks fastest, and the other one hundred and sixty arrive to find it sold out again. The customers who waited longest are no more likely to get one than a bot refreshing the page. You have turned a goodwill gesture into a second disappointment.

Third, **the alert can fire into thin air**. If the notification triggers off a number that is not truly synced, a return that gets restocked and then cancelled, a supplier feed that flickers, a warehouse count that has not settled, you send people to buy something that is not really there, and you oversell. The alert that was supposed to recover a sale now creates a refund and a support ticket instead.

> **◆ DATA** The math is brutal in the store's favor and against it at the same time. Stockouts cause roughly **40% of lost sales**, about **69% of shoppers** defect to a competitor when an item is unavailable, and a sold-out product sits dark for around **35 days** on average. A worked back-in-stock list is the cheapest revenue a store can recover, because the buyer already told you what they want.

## Why the usual fixes don't hold

Once a store feels the leak, merchants reach for three coping strategies. Each helps a little and each breaks in a predictable place.

**"I'll email the list myself when it's back."** This works until it is the fourth restock of a busy week. The notify happens whenever someone has a free minute, not when the stock lands, so the fastest-moving products, the exact ones with the longest waitlists, are the ones that sell out before the email ever goes out. The manual path scales inversely to how much you need it.

**"I'll just send one big announcement."** The mass blast ignores who asked first and how many units exist, so it manufactures a stampede and three more disappointed customers for every one it satisfies. Worse, people learn that your restock email is a lie they can't act on fast enough, and they stop opening it. The tool that should build loyalty quietly burns it.

**A [Shopify Flow](https://help.shopify.com/en/manual/shopify-flow) rule or a basic app.** Flow can react to an inventory event and an app can hold a waitlist, but the thing that actually matters is the judgment in the middle: how many units really landed, who has been waiting longest, which variant they wanted, whether to reach them by email or text, how to stagger the sends so the units last, and when to stop because supply is gone. A simple trigger fires all at once or not at all. The decision about who to tell, in what order, throttled to real stock, is the part neither one can hold.

## What the automation actually has to do

The real job is not "collect emails on the product page." It is "when an item is genuinely back, reach the people who asked, in a fair order, only as many as there are units for, on the channel they will actually see, and stop before you oversell." That means watching real inventory, ranking the waitlist, and sending with restraint. As a Dugong playbook, in plain prose, it reads like this:

```
# trigger
When a product or variant goes from out of stock to
available, and the count is actually synced

# steps
1. Pull the waitlist for that exact variant and how
   long each person has been waiting
2. Check how many units truly landed, not the raw
   number on a flickering feed
3. Notify in priority order, first-requested first,
   only as many people as there are units, with a little headroom
4. Send on the channel they chose, SMS for the
   fast movers, email otherwise, with a link straight to the variant
5. Throttle the next wave only if more stock lands,
   so you never point more buyers at fewer units
6. Stop and close the list when it sells through,
   and tell the people who missed it they're still in line
7. If it's a hyped drop or a tiny restock →
   assemble the plan and hand it to me before anything sends
```

Seven lines. The compiler fills in everything underneath: subscribing to the inventory change, confirming the count is real before it trusts it, sorting the waitlist by wait time and variant, metering the sends to the units available, picking SMS or email per subscriber, deep-linking to the right variant, and holding the rest of the list in reserve instead of dumping it. The merchant never built a rule for every product. They described how a careful store would work a waitlist, and let the compiler handle the watching and the sending.

> **◆ NOTE** Speed is not the only goal. **Fairness** is half the value, because a restock alert that rewards the fastest refresher instead of the longest waiter teaches your best customers that the list is pointless. Notify in the order people asked, meter to the units you actually have, and the same restock that used to create three disappointments now creates a sale and a little loyalty.

## Why this is a compiler problem, not an app problem

There are good back-in-stock apps in the Shopify ecosystem, and for many stores they are worth installing. But an app hands you its author's idea of how to work a waitlist, wrapped in a settings page and a monthly fee that often scales with the number of alerts you send. What most merchants actually want is to encode *their* rules: text the people waiting on sneakers but email everyone else, never alert more buyers than units in stock, give VIP customers a thirty minute head start, hold the list if a restock is under ten units and ping me instead, suppress anyone who already bought it elsewhere in the meantime. Those are sentences, not toggles, and they are specific to how your store actually sells.

A natural-language compiler is the unlock because back-in-stock was never really a form problem. It was an *inventory and timing* problem wearing a form problem's clothes. Collecting the email is the easy part, which is exactly why every theme can do it. The hard part is everything after: know when stock is genuinely there, decide who to tell and in what order, meter it to real units, choose the channel, and stop before you oversell. You can write that brief in a paragraph. You could never maintain it as a rule tree with a branch for every product, variant, and restock size.

## The workflow worth building this week

If you have products that sell out and come back, this is the automation to build before the next discount or win-back flow, because it recovers revenue you have already earned the right to. It sits right next to a pain we have written about already. The mirror image of the alert that never fires is [the overselling problem no one automates](https://blog.dugong.live/how-to-prevent-overselling-on-shopify-across-channels.html): the same shaky inventory count that lets you sell stock you no longer have is what makes a restock alert fire into thin air, so the store that keeps its counts honest is the one that can trust its waitlist to sell.

Describe it the way you would brief a sharp ecommerce hire on day one: here is how to tell when stock is really back, here is the order to notify people in, here is how many to tell, here is the channel for each, and here is when to stop and check with me first. That is the whole brief. The compiler does the watching, the ranking, and the sending. You keep your attention for the drops that need a human plan, and you stop letting the warmest leads in your store cool off in silence.

> **◆ READING** If this resonates, two companion pieces: our field study on [the Shopify automations no one builds](https://blog.dugong.live/best-shopify-automations-to-set-up.html) (where revenue-recovery work like this is a sliver of what merchants automate, despite paying back the most), and the dispatch on [the overselling problem no one automates](https://blog.dugong.live/how-to-prevent-overselling-on-shopify-across-channels.html), the inventory pain that decides whether your restock alert can be trusted at all.

If you are a Shopify merchant who has built a back-in-stock flow that actually recovers sales, or you have a restock that sold out before your own email went out and still stings, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Does Shopify send back-in-stock notifications automatically?

No, not in any real sense. Shopify has no built-in feature that emails or texts customers when an out-of-stock product is restocked. Some themes offer a basic notify me form, but it is too limited for most stores: it collects interest without reliably sending alerts, and it has no segmentation, no SMS, no priority order, and no throttle to stop the restock from selling out to the wrong people. The standard workaround is to export the requests and notify customers by hand, or to bolt on a third-party app. The native gap is why so many waitlists are quietly never answered.

Permalink: https://blog.dugong.live/how-to-set-up-back-in-stock-notifications-on-shopify.html#faq-1

### How much revenue do stockouts actually cost a store?

More than most merchants track. Stockouts account for roughly 40 percent of lost sales, and the lost sales ratio, the share of potential revenue missed because items were unavailable, averages around 20 to 30 percent in ecommerce. When a product is out of stock, about 69 percent of online shoppers will go buy from a competitor rather than wait, and a stocked-out product stays unavailable for an average of around 35 days. Every one of those is a customer who would have bought from you if the alert had reached them in time.

Permalink: https://blog.dugong.live/how-to-set-up-back-in-stock-notifications-on-shopify.html#faq-2

### Why does blasting the whole waitlist at once cause problems?

Because a single restock rarely covers everyone who asked. If two hundred people are waiting and forty units land, one mass email sends all two hundred to the page at the same moment, the forty units sell to whoever clicks fastest, and the other hundred and sixty arrive to find it gone again. You can also oversell if the alert fires before inventory is truly synced. A good restock automation notifies in priority order, usually first-requested first, throttled to the units actually available, per variant, across email and SMS, so the people who waited longest get the real chance to buy.

Permalink: https://blog.dugong.live/how-to-set-up-back-in-stock-notifications-on-shopify.html#faq-3

### In what order should back-in-stock notifications be sent?

First requested, first told, metered to real stock. Pull the waitlist for the exact variant, rank it by how long each person has waited, and notify only as many people as there are units, with a little headroom, on the channel each subscriber chose, SMS for the fast movers and email otherwise. Release the next wave only if more stock lands, close the list when it sells through, and tell the people who missed that they are still in line. Fairness is half the value: a blast that rewards whoever refreshes fastest teaches your longest-waiting customers that the list is pointless, and with 200 people waiting on 40 units, one undifferentiated email manufactures 160 disappointments by design. Metered, ordered sends turn the same restock into 40 sales and a queue that still trusts you, and the store can add its own rules, like a thirty minute head start for VIP customers.

Permalink: https://blog.dugong.live/how-to-set-up-back-in-stock-notifications-on-shopify.html#faq-4

### Can Shopify Flow send back-in-stock notifications?

Flow can react to the inventory event, and a basic app can hold the waitlist, but neither holds the judgment in the middle, which is the actual job. What matters at send time: whether the count that just went positive is real or a flicker from a return or a supplier feed, how many units truly landed, who has waited longest for exactly that variant, which channel each person chose, how many to tell now versus hold for the next wave, and when to stop because supply is gone. A simple trigger fires all at once or not at all, so it either blasts the whole list at forty units or sends nothing. Worse, a trigger wired to an unsynced count fires into thin air, points buyers at stock that is not really there, and converts the recovered sale into an oversell, a refund, and a support ticket.

Permalink: https://blog.dugong.live/how-to-set-up-back-in-stock-notifications-on-shopify.html#faq-5

---

Markdown rendition of https://blog.dugong.live/how-to-set-up-back-in-stock-notifications-on-shopify.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
