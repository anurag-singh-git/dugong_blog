# How to merge duplicate customer profiles on Shopify in bulk

> Shopify merges duplicate customers two at a time and refuses some pairs entirely. The AI playbook that finds and merges duplicate profiles in bulk, safely.

- Canonical: https://blog.dugong.live/how-to-merge-duplicate-customer-profiles-on-shopify.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-07-22
- Updated: 2026-10-25
- Section: Research
- Word count: 2254
- Dispatch: Nº 87 · Research · 10 min read
- Full headline on page: How to merge *duplicate customer profiles* on Shopify in bulk
- Keywords: Shopify merge duplicate customers in bulk, Shopify duplicate customer profiles, Shopify merge customer accounts, Shopify duplicate customer accounts, Shopify bulk merge customers, Shopify customer merge not working, Shopify POS duplicate customers, Shopify guest checkout duplicate accounts
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

Somewhere in your customer list right now is a person your store has met many times and recognized never. She created an account two years ago with her personal email. Last spring she checked out as a guest with her work address because she was buying from her desk. In December she tapped a wallet button that handed you a hide-my-email relay address. And when she found you at a weekend market, your POS filed her under a phone number and nothing else. Four profiles, four short histories, one human. To every report, segment, and flow you run, your best kind of customer looks like four unremarkable strangers.

The community threads on this are some of the longest-running in Shopify's forums, and the titles barely change from year to year. "Can merging duplicate customers in Shopify really be that complicated?" "Merging duplicate customers in bulk." "Built-in duplicate customer account detection and bulk merge tool." The thread that asks whether it can really be that complicated has been collecting replies across a decade of merchants, page after page of the same request. Nobody is asking for anything exotic. They want the store to know one person as one person, and to fix the thousands of cases where it does not, without doing it one pair at a time.

## The short answer

Shopify's merge is real and it takes exactly two profiles at a time, chosen by hand, from a profile's More actions or by selecting two customers on the Customers page. Orders, addresses, tags and notes combine properly under one record, and one profile per email address is enforced, so a logged-in customer cannot fork themselves by accident. There is no bulk select, no store-wide duplicate report and no queue of likely pairs to approve.

Detection is shallow and the merge is sometimes refused outright. The admin can point out two profiles sharing a name or a phone number; it cannot see that a plus-addressed alias is the same inbox, that a wallet relay address lands at the same street, or that a POS profile with no email shares a card and a postcode with an online account. The button disappears entirely for subscriptions, B2B companies, vaulted cards, store credit and multipass, which are the profiles most worth consolidating.

Flow has no merge customers action either, so the platform's own workflow tool can report a duplicate at best and never fix one. A real cleanup sweeps the whole list, scores each candidate pair on evidence rather than a name, picks the survivor carrying the login and the marketing consent, chains clusters of three or more down one join at a time, and leaves the genuinely uncertain pairs *in front of a person*.
## What Shopify actually does, and where it stops

Give the platform its due first, because the picture has improved. Shopify enforces one profile per email address, so a logged-in customer cannot fork themselves by accident. The admin will point out similar profiles when you are looking at a customer. And there is now a real merge: open a profile and choose Merge customer under More actions, or select two customers on the Customers page, and Shopify combines them properly, orders, addresses, tags, and notes brought together under one record. For the pair in front of you, it works.

The first wall is arithmetic. The merge takes exactly two profiles at a time, chosen by hand. There is no bulk select, no store-wide duplicate report, no queue of likely pairs to approve. A store that has traded for a few years across web, POS, and a marketplace or two carries duplicates in the thousands, and clusters rather than pairs: the same person as three, four, five records, which even by hand means merging down the chain one join at a time. The detection is shallow too. The admin can notice two profiles sharing a name or a phone number. It cannot notice that `j.smith@gmail.com` and `jsmith+shop@gmail.com` are the same inbox, that a relay address and a real one land at the same street, or that the POS profile with no email at all shares a card and a postcode with an online account.

The second wall is refusal. The merge is blocked entirely when either profile has a subscription contract, current or past, is linked to a B2B company, holds a vaulted payment card, carries a store credit account, or signs in through multipass. Those are precisely the profiles most worth consolidating, your subscribers and wholesale buyers, and for them the button simply is not there. And the automation escape hatch does not exist: [Shopify Flow](https://help.shopify.com/en/manual/shopify-flow) has no merge customers action, so the platform's own workflow tool can tell you about duplicates at best and can never fix one.

> Shopify enforces one profile per email address. Your customer has four email addresses.

Why it matters is arithmetic of a worse kind. Lifetime value splits across the fragments, so the regular who has spent eight hundred dollars reads as four people who spent two hundred, and never trips the VIP threshold in [the segments you build on spend](https://blog.dugong.live/how-to-segment-repeat-customers-on-shopify.html). The welcome flow greets her as a new customer, with a new customer's discount, every time she arrives under a new address. Two of her profiles are subscribed to your email list, so campaign sends double up or get flagged as spam by the same person they were meant to delight. Support opens the profile that matches the ticket's email and sees a quarter of the story. And your dashboards quietly inflate: new customer counts include people you have known for years, and repeat rate sags below the truth, so you spend acquisition budget re-acquiring customers you already own.

## Why doing it by hand never keeps up

The by-hand version is not hard, it is endless. Each merge is a minute of clicking once you are sure, and the being sure is the actual work. Two profiles named Maria Garcia are either one woman with two emails or two women in the same city, and the answer is not in the names. It is in the fragments: the same street address spelled two ways, the same phone with and without a country code, orders that alternate like one person shopping, a payment card that repeats. A person can weigh all of that, for about twenty pairs, and then the afternoon is gone and the list has minted new duplicates behind them, because every guest checkout and market day adds more.

Getting it wrong is worse than leaving it alone. Merge two profiles that are actually two people and you have joined their order histories, their addresses, and their store activity into one record each of them can see parts of. That is not an untidy database, that is a privacy incident, and there is no unmerge button waiting behind the mistake. The consent question has the same edge: one profile opted into marketing and the other explicitly unsubscribed, and a careless merge that keeps the wrong flag turns an unsubscribe into a subscription, which is the kind of error regulators and spam filters both remember. Caution is why most merchants do nothing, and doing nothing is how a list gets to ten thousand duplicates.

## What the automation actually has to do

The real job is not a merge button pressed faster. It is a sweep, a judgment, and a safe hand on the button, running continuously: find the likely duplicates across the whole list, decide which are truly the same person from evidence rather than string matching, merge the safe ones through Shopify's own merge so the history combines cleanly, route the blocked ones to a plan instead of a dead end, and bring the genuinely uncertain ones to you. As a Dugong playbook, in plain prose, it reads like this:

```
# trigger
On a scheduled sweep of the whole customer list, and
   on every new profile created at checkout, at the
   POS counter, or by an app

# steps
1. Find the likely duplicates: email variants and
   typos, shared phones and addresses, same name at
   the same street or postcode
2. Decide same person or coincidence from the whole
   record, never from the name alone
3. Pick the survivor: the profile with the login, the
   marketing consent, and the cleanest data
4. Merge pair by pair through the native merge,
   chaining clusters of three or more down to one
5. Queue what Shopify will not merge, with the
   subscription, B2B, and store-credit profiles
   consolidated around the survivor instead
6. Hold the ambiguous matches for a human, and log
   every merge so the cleanup is auditable
```

Six lines. The compiler fills in the rest: sweeping nightly instead of the once-a-year purge, scoring each candidate pair on the evidence a person would use, refusing to act on a name alone, keeping consent conservative so nobody unsubscribed is ever re-subscribed by a merge, carrying tags and notes onto the survivor, working the clusters down join by join in the right order, and writing a log you can audit: which profiles merged, on what evidence, and which pairs were left alone on purpose. The list gets clean once, then stays clean, because the same watcher meets every new profile on the day it is born.

> **◆ NOTE** The trap is **exact-match dedup**. A bulk tool that merges on same first and last name will eventually weld two real people together, and one bad merge costs more trust than a thousand duplicates. Matching is evidence work: an email variant plus a shared address is a strong yes, a shared name alone is a hard no, and the honest middle belongs in front of a person, not inside a default.

## Why this is a compiler problem, not an app problem

There are dedup apps, and a store drowning in duplicates should look at them. But the thing that makes a cleanup safe is not a merge executed quickly, it is the judgment about a specific pair: is the relay address her, is the POS profile him, does this pair share an inbox or merely a surname, which record deserves to survive, and is this cluster safe to collapse or is one profile in it a subscriber the merge will refuse. Those answers change per pair and per store, which is exactly what a fixed matching rule handles badly and a person cannot keep up with across fifty thousand profiles.

A natural-language compiler fits because identity was never a single setting. It is the foundation under half the automations this desk has written about. [The repeat customer your store treats like a stranger](https://blog.dugong.live/how-to-segment-repeat-customers-on-shopify.html) can only be labeled correctly if she is one record instead of four. [The second order that arrives before the first ships](https://blog.dugong.live/how-to-combine-multiple-orders-from-the-same-customer-on-shopify.html) can only be caught if both orders resolve to the same buyer. Even [the buyer who clears your whole drop](https://blog.dugong.live/how-to-limit-purchase-quantity-per-customer-on-shopify.html) is, underneath, this problem wearing a mask: a per-customer limit is only as strong as your notion of a customer.

Picture a home goods store, six years in, online plus two retail locations. Fifty thousand profiles, and a sweep finds six thousand that collapse into twenty-three hundred people. The VIP segment grows by a third without a single new order, because its members were hiding in fragments. The welcome code stops going out to regulars twice a month. Support starts seeing whole histories. And the two thousand profiles the merge refuses, the subscribers and the wholesale accounts, arrive as a tidy queue with a consolidation plan instead of a wall. Same customers, finally counted as themselves.

## The workflow worth building this week

If your store is more than a couple of years old, sells anywhere besides the website, or has ever run guest checkout, which is every store, this cleanup is already costing you money labeled as something else: acquisition spend re-acquiring your own customers, welcome discounts handed to regulars, a repeat rate that reads lower than it is. It pairs naturally with [the repeat customer your store treats like a stranger](https://blog.dugong.live/how-to-segment-repeat-customers-on-shopify.html), which depends on whole identities to label, and [the abandoned cart that gets one email](https://blog.dugong.live/how-to-set-up-an-abandoned-cart-email-sequence-on-shopify.html), which recovers more when the cart can be matched to a known customer. It feeds the same flywheel as [the Shopify automations no one builds](https://blog.dugong.live/best-shopify-automations-to-set-up.html), where the compounding work is the housekeeping nobody gets around to.

Describe it the way you would brief a careful assistant: sweep the list for people we know under more than one name, merge the ones the evidence proves, keep the profile with the login and respect every unsubscribe, chain the clusters down to one, queue the ones Shopify will not let us merge with a note on what to do instead, and show me anything you are not sure about. That is the whole brief. The compiler does the sweeping, the weighing, the merging, and the logging. Your store finally knows its customers the way your best staff do: one face, one name, one history.

> **◆ READING** If this resonates, two companion pieces: our dispatch on [the repeat customer your store treats like a stranger](https://blog.dugong.live/how-to-segment-repeat-customers-on-shopify.html), which puts the cleaned-up identities to work, and [the second order that arrives before the first ships](https://blog.dugong.live/how-to-combine-multiple-orders-from-the-same-customer-on-shopify.html), where matching the same buyer across records saves a shipping bill instead of a segment.

If you are a Shopify merchant who has cleaned a list of thousands, or you have a story about the merge that went wrong, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Can I merge duplicate customer profiles in bulk on Shopify?

No. Shopify's native merge combines exactly two profiles at a time: you select two customers on the Customers page and choose Merge customers, or open one profile and use More actions, then Merge customer. There is no bulk select, no store-wide duplicate report, and no admin screen that queues thousands of likely pairs for review, so a list that has accumulated years of guest checkouts and POS sales is a two-at-a-time job with no end. Cleaning a real list means detection and judgment first: finding likely pairs across email variants, shared phones, and matching addresses, deciding which pairs are truly the same person, then running the merges pair by pair, which is exactly the part worth automating.

Permalink: https://blog.dugong.live/how-to-merge-duplicate-customer-profiles-on-shopify.html#faq-1

### Why does Shopify keep creating duplicate customer profiles?

Because a profile is keyed to contact details, not to a human being. Shopify enforces one profile per email address, but the same person checks out as a guest with a work email, uses a hide-my-email relay address at a wallet checkout, gives your POS counter only a phone number, or simply mistypes their email once, and each new detail mints a fresh profile. POS and online are the classic split: the person your staff knows by face and the person who orders from your site at midnight are two records that never meet. Nothing native watches for the same human arriving under new details, so the list fragments quietly as the store grows.

Permalink: https://blog.dugong.live/how-to-merge-duplicate-customer-profiles-on-shopify.html#faq-2

### Why won't Shopify let me merge two customer profiles?

The merge is blocked whenever either profile is entangled in something Shopify cannot cleanly combine: a subscription contract, current or past; a link to a B2B company; a vaulted payment card; a store credit account; a multipass login; or a pending customer data request or redaction. Those pairs need a different path than the merge button: consolidate what can move, such as tags, notes, addresses, and a record of which profile is the primary one, point future activity at the survivor, and leave the entangled record intact. That is judgment work per pair, which is why a cleanup that only knows how to press merge stalls the first time it meets a subscriber.

Permalink: https://blog.dugong.live/how-to-merge-duplicate-customer-profiles-on-shopify.html#faq-3

### What happens to marketing consent when I merge two Shopify customer profiles?

The merge brings orders, addresses, tags, and notes together under the surviving record, and consent is where a careless merge does real damage. If one profile opted into marketing and the other explicitly unsubscribed, keeping the wrong flag turns an unsubscribe into a subscription, which is the kind of error regulators and spam filters both remember. The safe rule is to keep consent conservative: if any profile in the cluster said no, the survivor says no, and nobody who unsubscribed is ever re-subscribed by a cleanup. The same care picks the survivor in general, the profile with the login, the defensible consent status, and the cleanest data, with tags and notes carried over rather than dropped. And because there is no unmerge button, every merge should be logged, which profiles combined and on what evidence, so the cleanup can be audited and argued with later, entry by entry.

Permalink: https://blog.dugong.live/how-to-merge-duplicate-customer-profiles-on-shopify.html#faq-4

### How do I find duplicate customer profiles on Shopify?

The admin will point out similar profiles while you are looking at one customer, and that is the extent of the native detection: it can notice a shared name or phone number, and it stops there. What it cannot see is where the duplicates actually live. It cannot tell that j.smith@gmail.com and jsmith+shop@gmail.com are the same inbox, that a hide-my-email relay address and a real one land at the same street, or that a POS profile with no email at all shares a card and a postcode with an online account. Finding those takes evidence work across the whole record: email variants and typos, shared phones and addresses, the same name at the same street or postcode. The scoring rule that keeps it safe: an email variant plus a shared address is a strong yes, a shared name alone is a hard no, and the honest middle goes to a human.

Permalink: https://blog.dugong.live/how-to-merge-duplicate-customer-profiles-on-shopify.html#faq-5

---

Markdown rendition of https://blog.dugong.live/how-to-merge-duplicate-customer-profiles-on-shopify.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
