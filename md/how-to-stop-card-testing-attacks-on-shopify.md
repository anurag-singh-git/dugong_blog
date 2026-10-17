# How to stop card testing attacks on Shopify

> Bots run stolen cards through your Shopify checkout in tiny overnight orders and you eat the fees. The AI playbook that spots the attack and shuts it down.

- Canonical: https://blog.dugong.live/how-to-stop-card-testing-attacks-on-shopify.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-07-01
- Updated: 2026-08-07
- Section: Research
- Word count: 2390
- Dispatch: Nº 73 · Research · 9 min read
- Full headline on page: How to stop *card testing attacks* on Shopify
- Keywords: Shopify card testing, card testing attack Shopify, Shopify fake orders, Shopify bot orders, Shopify carding, Shopify fraud orders, block bot orders Shopify, Shopify card testing prevention, cancel fraud orders Shopify, Shopify abandoned checkout bot
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

Most Shopify pains are slow. Card testing is not. It arrives all at once, usually in the middle of the night, and by the time you see it your orders page is a wall of tiny sales you never made. Twenty dollars here, three dollars there, one product over and over, each with a name you do not know and a card that fails. Somewhere in the pile a few went through. Those are the ones that will hurt. Your store did not have a great night. Your store became a machine for checking whether stolen cards are still alive.

This is one of the loudest complaints in every Shopify merchant community, and it always reads the same way: hundreds of small fraudulent orders overnight, different IPs, different billing addresses, all on one or two cheap products, and no clear button to make it stop. Merchants raise the price of the item hoping the bot loses interest, and the bot buys it at the higher price anyway. They email support, they email their fraud app, they even file with the authorities, and the flood keeps coming. The frustration is not only the fraud. It is that the platform that took every one of those attempts, and charged a fee for each, leaves the cleanup entirely to them.

> Card testing does not want your product. It wants your checkout as a *free place to run* a stolen-card list, and Shopify hands it one.

## Why a Shopify checkout is such an easy target

A card-testing bot needs one thing: a live checkout that will attempt a real charge for a small amount. Your store is perfect. It is public, it takes cards, and a low-value order is exactly what a fraudster wants, because a small charge is less likely to be noticed by the person whose card was stolen. The bot does not care what it is buying. It cares that the payment either approves or declines, because that single bit of information, this card works or this card is dead, is the product it is actually harvesting to sell or spend somewhere else.

So it scripts your checkout and runs a list. Each attempt uses a fresh name, email, and billing address, and often a fresh IP, so no single order looks obviously wrong on its own. The pattern only appears when you step back and look at the whole burst: dozens or hundreds of orders in minutes, almost all the same low value, almost all on the same one or two products, a huge share declined, the rest approved on cards that are not really the buyer's. It is not a spike in demand wearing a disguise. It is an attack, and the disguise is that every individual order looks almost plausible.

## What Shopify actually gives you, and where it stops

Shopify is not blind to this, but its defense is thinner than merchants expect, and it stops well short of cleaning up. The gap shows up in three places.

First, **the CAPTCHA fires on Shopify's read, not yours**. For stores on [Shopify Payments](https://help.shopify.com/en/manual/payments/shopify-payments), Shopify runs machine-learning models at checkout and can show a CAPTCHA when a session looks automated, which does block a share of the crude bots. But it triggers on the platform's judgment of risk, in the moment, and a bot that rotates IPs and spaces out its attempts can slip under that bar. Merchants still wake up to waves of card-testing orders and fake [abandoned checkouts](https://help.shopify.com/en/manual/promoting-marketing/create-marketing/abandoned-checkouts), which is the plain evidence that the native screen catches some of the flood and not all of it.

Second, **the cleanup is entirely manual**. Every test order that did get through is now sitting in your admin as a real order on a stolen card. You have to find each one, cancel it, refund it before anything ships, and restock the unit, and you have to do it fast, because the small slice that approved will turn into chargebacks. Shopify gives you the cancel and refund buttons. It does not group the attack, tell you which orders are part of it, or act on them together. On a two-hundred-order night that is two hundred trips through the same three clicks, against a clock.

Third, **the rule engine is behind a paywall and cannot read the pattern**. The tooling to auto-cancel or auto-flag orders by rule lives in [Shopify Flow](https://help.shopify.com/en/manual/shopify-flow), which is only on the Advanced and Plus plans, so the smaller stores that get hit hardest often cannot use it at all. And even where you have Flow, it reacts one order at a time. A rule can flag or cancel an order under a dollar amount, which is a blunt swing that also catches your cheapest real products, but it cannot see that forty orders in four minutes share a fingerprint, decide the store is under attack, and respond to the burst as a burst. This is the same wall we hit in [the high-risk flag that makes you guess](https://blog.dugong.live/how-to-handle-high-risk-orders-on-shopify.html): Shopify can raise a hand on a single order, but it cannot investigate, correlate, and act.

> **◆ DATA** The reason a declined order is not free is that your processor charges for the attempt, not the sale. A flood of authorizations racks up fees even when nearly all of them fail, and the few that approve become chargebacks weeks later, each with its own dispute fee. A spike in your dispute rate is the real danger: cross a threshold and your payment account goes under review or into a penalty program, so a night of fake three-dollar orders can put your ability to take money at all at risk. That is why card testing is not just annoying, it is expensive in three directions at once.

## Why the usual fixes don't hold

When the flood hits, merchants reach for a handful of moves. Each one helps a little and breaks somewhere obvious.

**"I will raise the price so it is not worth it."** This misreads the attacker. They are not price-shopping, they are testing cards on someone else's money, so a higher price is no deterrent at all, and merchants who try it watch the bot buy the more expensive item just the same. All you have done is make each fraudulent order, and each eventual chargeback, cost more.

**"I will turn on every fraud filter."** Cranking the strictness up does block more bots, and it also starts declining real customers whose details are slightly off, whose bank flagged a normal purchase, or who are traveling. Now you are losing genuine sales to stop fake ones, and you still have to clean up whatever slips through. Turned up high enough, the filter becomes its own revenue leak, the false-decline version of the guessing game.

**"I will cancel them by hand as they come in."** This is the honest answer and the one that does not scale. On a slow trickle you can keep up. In a real attack the orders arrive faster than you can cancel, refund, and restock them, and it is the middle of the night, and each one you miss is a chargeback in three weeks. It is the same race against your own warehouse we wrote about in [the order change that races your warehouse](https://blog.dugong.live/how-to-edit-a-shopify-order-after-its-been-placed.html), except the clock is a fraud window and the queue refills while you work.

**"I will just wait for it to stop."** It might, in an hour or a day. But the orders it left behind are still real charges that will dispute, the fake checkouts have already poisoned your conversion and fraud numbers, the fees are already booked, and if any test order shipped before you caught it you have lost the goods too. Waiting is not free either. It only moves the cost from tonight to next month, with interest.

## What the automation actually has to do

The real job is not "block bots." It is "notice that a burst of orders is an attack, not demand, then cancel and refund the junk, keep it out of your numbers, slow the source, and tell a human once, with the mess already handled." That is detection, correlation, cleanup, and defense, running at the speed of the attack instead of the speed of your mouse. As a Dugong playbook, in plain prose, it reads like this:

```
# trigger
On a burst of orders or checkouts that spikes
   above normal rate for the store

# steps
1. Read the burst as a whole: order values, card
   and email spread, IPs, products, decline rate, window
2. Decide attack vs. real spike from the pattern,
   not from any single order
3. Cancel and refund the test orders before they
   ship, and restock the units
4. Tag every test order and checkout so it drops
   out of revenue, conversion, and fraud metrics
5. Throttle or block the offending IPs and
   sessions, tighten checkout while the attack runs
6. Alert a human once, with the window, the count,
   and the fee exposure, cleanup already done
7. Stand down when it stops, and surface any real
   customer caught in the net for review
```

Seven lines. The compiler fills in everything underneath: measuring the normal order rate so a spike is defined against your store and not a guess, reading a whole burst instead of one order, weighing the signals that separate carding from a genuine rush, cancelling and refunding in bulk before the fulfillment clock runs out, tagging the noise so your analytics stay honest, leaning on the source with friction that stays off the paths real buyers use, and writing one alert a human can act on instead of a hundred order emails. The merchant never sat up at 3 a.m. cancelling test orders one at a time. They described how a sharp fraud lead would recognize and shut down an attack, and let the compiler do it at machine speed.

> **◆ NOTE** The trap in fraud automation is treating every order alone. One three-dollar order to a new name is nothing. Forty of them in four minutes, on the same product, across forty cards, half declined, is an attack, and the difference is only visible in the aggregate. A rule that judges each order on its own either misses the pattern or swings so wide it declines your real customers. The job is not "score this order," it is "read this burst, decide what it is, and respond to the whole thing," then hand a person the one case that genuinely needs a human eye. Automation that can only look at orders one at a time is not defending you from an attack that is coordinated by design.

## Why this is a compiler problem, not an app problem

There are capable fraud and bot-blocking apps, and a store that gets hit often should run one, which again proves the native screen leaves a gap. But the thing that makes an attack safe to handle automatically is not one more filter with a stricter setting. It is judgment about a specific burst on a specific night: is this demand or an attack, which of these orders are real, how hard do I clamp the checkout without punishing genuine buyers, and when do I pull a human in because a real customer got caught or an approved charge already shipped. Those answers change with every attack and every store, which is exactly the kind of shifting call a fixed rule was never going to make well.

A natural-language compiler fits because card testing was never really a single-order problem. It is a *coordinated burst* that only makes sense read all at once, and the response has to be just as coordinated: cancel this set, refund it, keep it out of the numbers, slow the source, and leave the real orders untouched. You can write that brief in a paragraph. You could never execute it by hand at the speed and volume an attack arrives in. It sits in the same family as [the chargeback you lose by default](https://blog.dugong.live/how-to-win-chargeback-disputes-on-shopify.html), where the loss is decided weeks later by evidence no one gathered, and [the unpaid order that never cancels itself](https://blog.dugong.live/how-to-automatically-cancel-unpaid-orders-on-shopify.html), where a junk order sits in your admin holding stock until someone deals with it.

## The workflow worth building this week

If you have ever woken up to a wall of tiny orders you did not make, spent a morning cancelling and refunding fraud one at a time, or watched your conversion and dispute numbers go strange after a bad night, this is the automation to set up before the next attack, because card testing does not warn you and the cost lands whether you are awake or not. It pairs naturally with the risk and payments work we have written about, like [the high-risk flag that makes you guess](https://blog.dugong.live/how-to-handle-high-risk-orders-on-shopify.html) and [the chargeback you lose by default](https://blog.dugong.live/how-to-win-chargeback-disputes-on-shopify.html), and it feeds the same flywheel as [the Shopify automations no one builds](https://blog.dugong.live/best-shopify-automations-to-set-up.html), where the work that compounds is the part merchants never get to.

Describe it the way you would brief a sharp fraud lead: when a burst of tiny orders spikes past our normal rate, tell me if it is an attack, cancel and refund the junk before it ships, keep it out of my numbers, slow the source without blocking real buyers, and bring me the one order that needs a human. That is the whole brief. The compiler does the reading, the correlating, the cancelling, and the defending. You keep your night, and you stop being the slowest thing standing between a stolen-card list and your payment account.

> **◆ READING** If this resonates, two companion pieces: our dispatch on [the high-risk flag that makes you guess](https://blog.dugong.live/how-to-handle-high-risk-orders-on-shopify.html), where Shopify raises a hand on one order but cannot investigate it, and [the chargeback you lose by default](https://blog.dugong.live/how-to-win-chargeback-disputes-on-shopify.html), where the bill for tonight's approved test orders arrives weeks from now and nobody built the case. Also worth reading: [the customer list the bots built](https://blog.dugong.live/how-to-stop-fake-customer-accounts-and-spam-signups-on-shopify.html), on what the same traffic leaves behind in your customer records when it is not chasing a card.

If you are a Shopify merchant who has weathered a card-testing attack and built something that catches the burst and cleans up behind it, or you have a story about the night the orders would not stop, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### What is a card-testing attack on Shopify?

Card testing, also called carding, is when someone uses an automated script to run a batch of stolen card numbers through your checkout to find out which ones still work. Your store is not the target, it is the test rig. The bot places many small orders in a short window, each with a different name, email, billing address, and card, because a low-value charge is less likely to be noticed by the real cardholder. A card that approves gets sold or used elsewhere for a real purchase, and a card that declines gets thrown away. What you see is a sudden flood of tiny orders and abandoned checkouts overnight, most declined and a few approved, none of them real customers. It looks like a spike in demand and is actually an attack running through your payment page.

Permalink: https://blog.dugong.live/how-to-stop-card-testing-attacks-on-shopify.html#faq-1

### Does Shopify stop card testing on its own?

Partly, and not enough on its own. For stores on Shopify Payments, Shopify runs machine-learning models at checkout that can trigger a CAPTCHA when a session looks like a bot, and that stops some automated attempts. But it fires on Shopify's read of the risk, not yours, and merchants still report waves of card-testing orders and fake abandoned checkouts getting through, especially when the bot rotates IPs and details so each attempt looks fresh. The cleanup after the fact, cancelling and refunding the junk orders, is still left to you, and the tooling to auto-cancel or auto-flag by rule lives in Shopify Flow, which is only on the Advanced and Plus plans. The native defense reduces the flood. It does not read your specific attack, clean up behind it, or shut the source down.

Permalink: https://blog.dugong.live/how-to-stop-card-testing-attacks-on-shopify.html#faq-2

### Why do card-testing orders cost me money even when they get declined?

Because your processor charges for the attempt, not just the sale. Every authorization the bot runs can carry a fee, and a flood of them adds up fast even when almost all of them fail. The small number that approve are worse: those are real charges on stolen cards, so they turn into chargebacks weeks later, each with its own dispute fee, and a spike in your dispute rate can put your payment account under review or into a penalty tier. On top of the direct cost, the flood buries your genuine orders, poisons your conversion rate and fraud analytics, and can trip fraud filters that then decline your real customers. A declined test order is not free. It is a small charge now and a risk to your account later.

Permalink: https://blog.dugong.live/how-to-stop-card-testing-attacks-on-shopify.html#faq-3

### How do I recognize a card testing attack on my Shopify store?

The signature is a burst: order or checkout volume spiking far above your normal rate in a tight window, concentrated on one cheap item, with unusual spread underneath it. Two hundred orders overnight for the least expensive product in the catalog, dozens of different card numbers, emails that look generated, IPs that rotate or cluster oddly, and a decline rate far beyond anything your real traffic produces. Any single order from the burst can look almost normal on its own; the attack is only visible as a pattern, which is why per-order review misses it. Watch rate first, then composition: order values, card and email spread, IPs, products, and the decline curve across the window. A store that alarms on the burst catches the attack in its first minutes instead of at breakfast, after the processor fees have already been counted.

Permalink: https://blog.dugong.live/how-to-stop-card-testing-attacks-on-shopify.html#faq-4

### What should I do first after a card testing attack hits?

Work the burst as a unit, not order by order. Cancel and refund the test orders before anything ships, and restock the units so real customers can buy them. Tag every test order and checkout from the window so the junk drops out of revenue, conversion, and fraud metrics; an untagged attack quietly poisons every dashboard it touched. Throttle or block the offending IPs and sessions, and tighten the checkout while the attack is still running. Then alert one human, once, with the window, the count, and the fee exposure, cleanup already done. One note for smaller stores: the native tooling to auto-cancel or auto-flag orders by rule lives in Shopify Flow, which requires the Advanced or Plus plan, so the stores that get hit hardest often cannot use it and need this response wired up another way.

Permalink: https://blog.dugong.live/how-to-stop-card-testing-attacks-on-shopify.html#faq-5

---

Markdown rendition of https://blog.dugong.live/how-to-stop-card-testing-attacks-on-shopify.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
