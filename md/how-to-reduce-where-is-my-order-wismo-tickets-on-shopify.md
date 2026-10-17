# How to reduce 'where is my order?' (WISMO) tickets on Shopify

> WISMO ('where is my order?') is the most common ecommerce support ticket, ~18% of inbox volume. The AI playbook that answers tracking questions automatically.

- Canonical: https://blog.dugong.live/how-to-reduce-where-is-my-order-wismo-tickets-on-shopify.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-06-04
- Updated: 2026-08-10
- Section: Research
- Word count: 1320
- Dispatch: Nº 49 · Research · 6 min read
- Full headline on page: How to reduce *'where is my order?'* (WISMO) tickets on Shopify
- Keywords: WISMO, where is my order, order tracking automation, ecommerce support, Shopify customer support
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

There is a thread that resurfaces on r/shopify every few weeks, almost word for word. A solo founder ran a good ad. Orders tripled. And then the inbox did too, not with new sales, but with four words, over and over: *where is my order?* One merchant described spending more time answering tracking emails than packing the things people were asking about. The replies are all the same: hire a VA, set up a canned response, add a tracking app. None of them make the question go away.

The acronym for this is WISMO, "where is my order?", and it is the single most common message in ecommerce. Gorgias, which sees support volume across tens of thousands of stores, puts it at roughly **18% of all incoming tickets on an average week**. ShippyPro and Salesforce both report it climbing past **50% during peak periods** like Black Friday. It is the most predictable flood in the entire business, and most Shopify merchants still bail the water out by hand.

> WISMO is the only support category where the customer, the merchant, and the carrier all already know the answer. It's sitting in the tracking API. Nobody's asking it.

## What a single "where is my order?" actually costs

The reason WISMO hurts isn't any one ticket. It's the volume, and the fact that each one looks trivial right up until you multiply it. Industry estimates put the fully-loaded cost of handling one support interaction at **$5 to $25**, depending on channel and labor. A store doing 3,000 of these a month is spending somewhere between fifteen and sixty thousand dollars answering a question the carrier could answer for free.

For a solo merchant the cost isn't dollars, it's attention. Every WISMO email is a context switch away from the work that grows the store, sourcing, marketing, product. The Reddit complaint is never "this is hard." It's "this is endless, and it's drowning everything else."

> **◆ DATA** ShippyPro estimates **70-90% of shipping inquiries are pure WISMO**, questions that a proactive notification would have prevented entirely. The ticket isn't a support problem. It's an information-timing problem wearing a support problem's clothes.

## Why the canned auto-reply never fixed it

Every merchant eventually rigs up some version of a fix. A [Shopify Flow](https://help.shopify.com/en/manual/shopify-flow) rule. A help-desk macro. A tracking app that adds a "track your order" page. They help a little. They never close the loop. Here's why.

A real WISMO message is rarely just "where is my order?" It's *"hi, I ordered the navy one last Tuesday for my dad's birthday on Saturday, the tracking hasn't moved in three days, is it going to make it?"* A canned reply with a tracking link answers none of what was actually asked. It doesn't know the package is stuck in a carrier scan gap. It doesn't know Saturday is a hard deadline. It doesn't know whether to apologize, reassure, or proactively offer a reship. So the customer replies again, and now you're in the thread anyway, except annoyed, because the robot wasted a round trip.

In a node-based builder this is unwinnable. You'd need a branch for "tracking stalled," a branch for "delivered but says missing," a branch for "still in pre-transit," a branch for "international customs hold," each with its own tone and its own decision about whether to escalate. Nobody draws that graph. So they don't, and the inbox wins.

## What the automation actually has to do

The job isn't "auto-reply with a link." The job is: read the message, figure out what the customer is really worried about, pull the live carrier status, compare it against the promised delivery window, and decide, case by case, whether to reassure, escalate to a human, or get ahead of the problem with a reship before the customer even asks for one.

That is a conversation, not a rule. Written as a Dugong playbook, in plain prose, it looks like this:

```
# trigger
When a support email mentions an order or tracking

# steps
1. Find the order in Shopify from their email or order number
2. Pull live tracking from the carrier
3. Compare status against the promised delivery date
4. If on track → reply warmly with the real ETA, no link dump
5. If stalled > 48h or past due → apologize, offer a
   reship or refund, and flag it to me in Slack
6. If marked delivered but they say missing →
   route to a human with the delivery scan attached
7. Match the brand voice; sign off as the team, not a bot
```

Seven lines. The compiler fills in everything underneath: the Shopify lookup, the carrier API call, the date math, the retry logic when the tracking endpoint times out, the brand-voice pass on the reply. The merchant named none of those services. They described what they wanted to happen, and the compiler decided what it needed to *be*.

## The real win: answering before they ask

The reframing that matters most is in that ShippyPro number, 70 to 90% of these are preventable. The same playbook that answers a WISMO email can run the other direction: watch every in-flight order, and the moment one stalls or slips past its window, reach out *first*.

```
# trigger
Every few hours, check all orders shipped but not delivered

# steps
1. Flag any order stalled in transit or past its ETA
2. Email the customer proactively: here's where it is,
   here's what we're doing, no action needed from you
3. If it's a gift or time-sensitive order → offer a reship now
4. Log the at-risk orders to a sheet so I can see patterns
```

A customer who gets "hey, your order's running a day late, we're on it" before they think to ask never opens a ticket. The flood doesn't get handled faster, it never forms. That is the difference between a tracking app and an automation that understands the order: one answers the question, the other removes it.

> **◆ NOTE** The economics are blunt. If WISMO is 18% of your tickets at, say, $7 each, and a proactive playbook prevents 70% of them, a store fielding 1,000 support contacts a month saves roughly **$880 a month**, before counting the replies you no longer write at 11pm, or the refunds you avoid because you caught the late package first.

## Why this is a compiler problem, not an app problem

There are dozens of WISMO apps in the Shopify App Store, and they all do roughly the same thing: a branded tracking page and a templated notification. They're fine. They also can't read an angry email, weigh a birthday deadline, or decide that *this* customer should get a reship and *that* one should get an apology. That decision is a judgment call, and judgment calls don't fit in a settings panel.

A natural-language compiler is the unlock precisely because the hard part of WISMO was never the tracking lookup, it was the hundred small decisions about tone, timing, and escalation that sit on top of it. You can describe those decisions in a paragraph. You could never draw them in a node graph. That gap, between what merchants can describe and what the old tools could compile, is exactly where the unbuilt automations live.

## The workflow worth building this week

If you run a Shopify store and you've ever typed the same tracking-status reply twice in one afternoon, this is the automation to build before any tag rule, any cart email, any analytics dashboard. It's the one that's been quietly eating your time the whole while you were building the easy ones.

Describe it the way you'd explain it to a new hire: when someone asks where their order is, find it, check the carrier, and answer like a human who actually looked. Then let it watch your in-flight orders and get ahead of the ones going wrong. That's the whole brief. The compiler handles the rest.

> **◆ READING** If this resonates, two companion pieces: our field study on [the Shopify automations no one builds](https://blog.dugong.live/best-shopify-automations-to-set-up.html), and the essay on [the death of the drag-and-drop builder](https://blog.dugong.live/the-death-of-the-drag-and-drop-builder.html).

If you're a Shopify merchant drowning in "where is my order?", or you've built a WISMO playbook that actually works, the inbox is open: `field-notes@dugong.live`. We're collecting case studies for issue 50.

---

## Common questions

### What is WISMO?

WISMO stands for "where is my order?", the single most common message in ecommerce support. It accounts for roughly 18% of all incoming tickets on an average week and can climb past 50% during peak periods like Black Friday.

Permalink: https://blog.dugong.live/how-to-reduce-where-is-my-order-wismo-tickets-on-shopify.html#faq-1

### How much does answering a "where is my order?" ticket cost?

Industry estimates put the fully-loaded cost of handling one support interaction at $5 to $25 depending on channel and labor. A store fielding 3,000 WISMO tickets a month spends roughly $15,000 to $60,000 answering a question the carrier's tracking data could answer for free.

Permalink: https://blog.dugong.live/how-to-reduce-where-is-my-order-wismo-tickets-on-shopify.html#faq-2

### Why doesn't a canned auto-reply fix WISMO?

A static auto-reply still makes the customer do the work, find the tracking link, click through, interpret the carrier status. It deflects nothing and often increases follow-ups. The fix is a playbook that reads the order and tracking data and answers the specific question automatically, ideally before the customer asks.

Permalink: https://blog.dugong.live/how-to-reduce-where-is-my-order-wismo-tickets-on-shopify.html#faq-3

### How do I prevent WISMO tickets before customers ask?

Run the playbook in the other direction. Instead of waiting for the email, watch every shipped order every few hours and flag any that has stalled in transit or slipped past its promised window. The moment one does, email the customer first: here is where the package is, here is what we are doing, no action needed. If the order is a gift or time-sensitive, offer a reship immediately rather than waiting for the complaint. ShippyPro estimates 70 to 90% of shipping inquiries are pure WISMO, questions a proactive notification would have prevented, so the flood never forms. The economics follow: if WISMO is 18% of tickets at $7 each and the proactive playbook prevents 70% of them, a store fielding 1,000 support contacts a month saves roughly $880 a month, before counting the 11pm replies no longer written and the refunds avoided by catching late packages early.

Permalink: https://blog.dugong.live/how-to-reduce-where-is-my-order-wismo-tickets-on-shopify.html#faq-4

### Can Shopify Flow reduce WISMO tickets?

Only at the edges. A Flow rule or help-desk macro can send a templated reply with a tracking link, and a tracking app can add a branded tracking page. They help a little and never close the loop, because a real WISMO message is specific: the tracking has not moved in three days, the package is a birthday gift with a Saturday deadline, the carrier says delivered but nothing arrived. Answering it means reading the message, pulling live carrier status, comparing it against the promised delivery window, and deciding case by case whether to reassure, escalate to a human, or offer a reship before it is requested. In a node builder that is a branch for stalled tracking, one for pre-transit, one for delivered-but-missing, one for customs holds, each with its own tone and escalation call. Nobody draws that graph, which is why the inbox keeps winning.

Permalink: https://blog.dugong.live/how-to-reduce-where-is-my-order-wismo-tickets-on-shopify.html#faq-5

---

Markdown rendition of https://blog.dugong.live/how-to-reduce-where-is-my-order-wismo-tickets-on-shopify.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
