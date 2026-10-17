# How to add a gift message and gift wrap option at checkout on Shopify

> Shopify has no real gift message or gift wrap field, so notes get lost and prices print on the box. The AI playbook that runs gifting end to end.

- Canonical: https://blog.dugong.live/how-to-add-a-gift-message-and-gift-wrap-at-checkout-on-shopify.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-07-18
- Updated: 2026-08-15
- Section: Research
- Word count: 2090
- Dispatch: Nº 85 · Research · 10 min read
- Full headline on page: How to add a *gift message* and gift wrap option at checkout on Shopify
- Keywords: Shopify gift message, Shopify gift wrap at checkout, Shopify gift note packing slip, Shopify gift receipt hide prices, add gift message option Shopify, Shopify gift option not working, Shopify order notes gift, Shopify gifting checkout
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

A large share of what any store sells is bought for someone else. Birthdays, holidays, a thank-you, a new baby: the shopper is not the recipient, and they want two small things that every gift shop has offered forever. Wrap it nicely, and let me write a note. On Shopify, both of those simple wishes fall into a gap, and the customer usually does not find out until the gift has already landed wrong.

This is one of the steadiest complaints in the Shopify community, and the threads are blunt about it. "How can I add a gift note to my packing slip?" "Add a gift message option at checkout." "How do I hide prices on the slip for a gift?" The answers are always the same short menu: repurpose the order-note box, edit your theme's [Liquid](https://shopify.dev/docs/api/liquid), or install an app. Shoppers are not asking for anything unusual. They want a labeled message field and a wrap option, and they want the note to reach the person packing the box instead of dying in a field no one reads.

## What Shopify actually does, and where it stops

Give the platform its due first. Shopify does have one native place for a customer to leave text: the cart order-note field. You can switch it on in the theme, you can rename its label to something like "Add a gift message here," and whatever the shopper types is saved to the order and visible in the admin. For a store that only ever needs a single line of free text on an order, that field technically exists and technically works.

The wall is that the order note was built for delivery instructions, not for gifting, and it shows. It is one field for the whole order, so a gift message shares the same box as "leave it with the neighbor" and anything else the buyer wants to say. It does not attach to a specific item, so a cart with one gift and one thing for yourself has nowhere to say which is which. It is off by default in many themes, it has no length limit or validation, and it is a plain textarea, so there is no toggle that says "this is a gift" for the rest of your systems to act on. It captures text. It does not capture intent.

Gift wrap is thinner still. There is no native "add gift wrap" option at checkout for a standard store. The one native path is Checkout Extensibility, which lets Shopify Plus merchants add fields and options to the checkout, and even there the out-of-the-box result is a bare toggle, not a wrap that arrives as a fee on the order, a line item your accounting can see, and a clear instruction at the packing bench. Everyone below Plus is left faking wrap as a hidden product, a variant, or an app, and then hoping the warehouse notices.

> **◆ THE REAL STING** The worst failure is the **price on the box**. Shopify's packing slip is one template for every order, and it prints prices. There is no native switch that says "this order is a gift, hide the totals," so unless you edit the Liquid and branch it by hand, the recipient opens their present and sees exactly what the sender paid. A gift is the one order where the price must never show, and it is the order Shopify treats like every other.

> A gift is not a normal order with a note bolted on. It is an order that has to hide its own price and carry a message to a stranger, and Shopify ships neither by default.

## Why doing it by hand never holds

The by-hand version of gifting is a chain of small manual steps, and it breaks at the first busy week. The shopper leaves a note in the order box, and someone in the admin has to notice it, read it, decide it is a gift, and remember to do something about it. To get the message onto the paper, you edit the packing-slip template to pull the order note in, which then prints on every order that has a note, gift or not, right next to the full prices. To keep prices off a gift, you would need a second, price-free slip that you only use for gift orders, which Shopify does not branch to on its own. So the whole thing rests on a person spotting a note and picking the right template, at exactly the moment the fourth-quarter rush makes that impossible.

Then there is the judgment a text field can never hold. Some messages should not print: the empty submission, the paste of a tracking URL into the wrong box, the occasional abusive note aimed at the recipient. A gift that ships to a different address than the buyer needs its own handling. A cart that is half gift and half self-purchase should not wrap the wrong item or hide the price on the part the buyer keeps. And a [split shipment](https://blog.dugong.live/how-to-combine-multiple-orders-from-the-same-customer-on-shopify.html) means the message and the wrap have to travel with the right box. None of that is a single field. It is a set of decisions, and a person loses the thread of them the moment the volume climbs.

## What the automation actually has to do

The real job is not "add a note field." It is "capture the gift and the message, make sure the message is safe to print, attach the wrap as something real, mark the order as a gift, and then produce a slip that carries the note and hides the price, routed to the bench, with the odd cases handed to a person." That is a capture, a guardrail, a document, and an escalation, all triggered when an order comes in marked as a gift. As a Dugong playbook, in plain prose, it reads like this:

```
# trigger
On a new order flagged as a gift
   (toggle, wrap choice, or a message present)

# steps
1. Capture the gift toggle, wrap choice, and message
   as order attributes, not one buried note
2. Validate the message: length, empties, anything
   offensive, and tidy the formatting
3. Attach the wrap as a real line item or fee, or as a
   packing instruction where it is free
4. Tag the order as a gift so every later step can
   branch on it instead of guessing
5. Build a gift packing slip: message in, every price
   and total out, and route it to the bench
6. Hold for review an offensive or oversized message,
   a multi-address gift, or a split shipment
```

Six lines. The compiler fills in the rest: reading the gift toggle, the wrap choice, and the message as structured intent instead of one free-text field, checking the note before it ever prints, turning wrap into a charge and a clear bench instruction rather than a hidden SKU nobody sees, tagging the order so the slip, the routing, and any notification all know it is a gift, and generating the one document that a normal order never needs, a slip with the message on it and the prices gone. The merchant never edited a Liquid template or trained the packing team to hunt for notes. They described how a gift should be handled once, and let the compiler handle every gift the same way.

> **◆ NOTE** The trap here is treating the order note as the gift feature. It is a single unlabeled field with no validation and no signal, and it prints next to the price. Treat the gift as its own kind of order, with a tag, a clean message, a real wrap charge, and a price-free slip, and the whole thing becomes reliable by construction. Whether a message is safe to print, whether the wrap reached the bench, and whether the price ever shows on the box are the judgment calls that matter as much as the note itself.

## Why this is a compiler problem, not an app problem

There are capable gifting apps on the Shopify App Store, and a store that sells a lot of gifts should evaluate one. But the thing that makes gifting safe is not one more field on the product page. It is judgment about a specific order at a specific moment: is this message fit to print, does this gift ship to the buyer or to someone else, should the price be hidden on this box and shown on the next, and did the wrap instruction actually reach the person folding the paper. Those answers change per order, which is exactly what a fixed form handles badly and a busy packing team cannot hold in their heads through a peak.

A natural-language compiler fits because gifting was never a single action. It is a capture that reads intent, a guardrail that keeps a bad note off the paper, a document that hides a price a normal slip would show, and a hand-off to the bench, all running the moment a gift order lands. You can describe the whole behavior in a paragraph. You could never keep a theme edit, a manual template switch, and a "watch for the note" habit honest across a holiday week. It sits in the same family as [the free gift that never lands in the cart](https://blog.dugong.live/how-to-automatically-add-a-free-gift-with-purchase-on-shopify.html), where an order has to do more than lower a price, and [the order tag you set by hand](https://blog.dugong.live/how-to-automatically-tag-orders-on-shopify.html), where the label that drives everything downstream is the part nobody keeps up with.

Picture a candle brand heading into December. Half the carts are gifts, each with a note, some with wrap, a few shipping straight to the recipient. On the native setup that is a renamed note box, an edited packing slip that prints prices anyway, and a packing team told to eyeball every order for a message. With the automation, it is one rule: capture the gift, clean the message, charge the wrap, tag the order, and print a slip that carries the words and hides the totals. Every gift is handled the same way, no full-price invoice ever rides along in a present, and the one message that should not print gets held for a human before it ever reaches the paper.

## The workflow worth building this week

If any real fraction of your orders are gifts, and for most stores the fourth quarter makes that most of them, this is the automation to set up now, because the cost of not having it is a bad first impression on a brand-new customer: the recipient. A ruined gift is the worst kind of unboxing, and it happens to the exact person you most want to win over. It pairs naturally with the fulfillment work we have written about, like [the WISMO tickets that eat your afternoon](https://blog.dugong.live/how-to-reduce-where-is-my-order-wismo-tickets-on-shopify.html), which is the same instinct of getting the right information to the right place before someone has to ask, and [the invoice you send by hand](https://blog.dugong.live/how-to-automatically-send-invoices-on-shopify.html), which is the other document your store has to get right without a person driving it. It feeds the same flywheel as [the Shopify automations no one builds](https://blog.dugong.live/best-shopify-automations-to-set-up.html), where the work that compounds is the part merchants never get to.

Describe it the way you would brief a careful packer: when an order is a gift, capture the note and the wrap, make sure the note is clean before it prints, charge the wrap and flag it for the bench, and give me a slip with the message on it and no prices anywhere. Ship it to the right address, keep the price off the box, and bring me anything that looks off before it goes out. That is the whole brief. The compiler does the capturing, the checking, the tagging, and the printing. Your gifts arrive wrapped, with the words that were meant for them and none of the numbers that were not.

> **◆ READING** If this resonates, two companion pieces: our dispatch on [the free gift that never lands in the cart](https://blog.dugong.live/how-to-automatically-add-a-free-gift-with-purchase-on-shopify.html), where an order has to add something rather than just discount it, and [the order tag you set by hand](https://blog.dugong.live/how-to-automatically-tag-orders-on-shopify.html), where the label that steers every later step is the one nobody keeps current.

If you are a Shopify merchant who has built gifting that actually reaches the box, message clean and price hidden, or you have a story about the full-price invoice that arrived inside a present, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Does Shopify have a gift message option at checkout?

Not as a real, dedicated field on a standard store. The only native place for a shopper to leave a note is the cart order-note box, which is a single freeform field for the whole order, unlabeled unless you rename it, and off by default in many themes. It was built for delivery instructions, not gifting, so a gift message shares one field with everything else, does not attach to a specific item, and has no validation. Gift wrap at checkout is native only for Shopify Plus stores using Checkout Extensibility, and even there it is a bare option rather than a fee, a line item, and a packing instruction. Everyone else stitches gifting together with the order note, theme edits, and apps.

Permalink: https://blog.dugong.live/how-to-add-a-gift-message-and-gift-wrap-at-checkout-on-shopify.html#faq-1

### Why doesn't my Shopify gift note show on the packing slip?

Because the packing slip is one template for every order, and the order note does not print on it unless you edit the Liquid template to pull the note in. Even after you do, the note prints on every order that has one, gift or not, and it prints alongside the full prices, because there is no native switch to hide prices for a gift. So the recipient can open a box that shows what the sender paid, which is the opposite of a gift. Getting the message onto the slip and the prices off it, for gift orders only, is theme code plus a manual habit, and it breaks the first time an order is edited or a warehouse app takes over fulfillment.

Permalink: https://blog.dugong.live/how-to-add-a-gift-message-and-gift-wrap-at-checkout-on-shopify.html#faq-2

### How do I hide prices on a Shopify gift receipt?

There is no native per-order toggle that says this order is a gift, hide the prices. The packing slip template is shared across the whole store, so hiding prices there hides them for every order, and leaving them shows them on gifts too. The dependable way is to mark an order as a gift the moment it is placed, then generate a separate gift packing slip for those orders that carries the message and omits every price and total, while normal orders keep their standard slip. That means detecting the gift, tagging the order, and branching the document, which is exactly the judgment a shared template cannot make on its own.

Permalink: https://blog.dugong.live/how-to-add-a-gift-message-and-gift-wrap-at-checkout-on-shopify.html#faq-3

### Why should gift messages be validated before printing?

Because a text field will print whatever it holds, and some of what it holds should never reach the box. The order note has no length limit and no validation, so the messages that arrive include empty submissions, a tracking URL or address pasted into the wrong box, and occasionally an abusive note aimed at the recipient, which a busy packing bench will fold into a present unread. Validation is a small step that runs the moment a gift order lands: check the message for length and empties, tidy the formatting, and hold anything offensive or oversized for a human before it prints. The judgment calls sit right next to it: a gift shipping to a different address than the buyer needs its own handling, and on a split shipment the message and the wrap have to travel with the right box. A person loses that thread during a rush; the workflow does not.

Permalink: https://blog.dugong.live/how-to-add-a-gift-message-and-gift-wrap-at-checkout-on-shopify.html#faq-4

### What happens when a Shopify cart is half gift and half regular order?

By default, nothing good, because the order note is one field for the whole order. A cart holding one gift and one thing for the buyer has nowhere to say which item the message belongs to, so a note meant for a birthday recipient rides along with the buyer's own purchase, the wrap can end up on the wrong item, and hiding prices on the packing slip hides them for the part the buyer keeps too. The fix is to capture gifting as structured intent instead of one buried note, per item where it matters: which line is the gift, which gets wrapped, where the message goes, and whether it ships to the buyer or straight to the recipient. Once that is captured, the wrap charge lands on the right line, the slip hides prices for the gift only, and the odd cases, a multi-address gift or a cart nobody can parse, go to a person.

Permalink: https://blog.dugong.live/how-to-add-a-gift-message-and-gift-wrap-at-checkout-on-shopify.html#faq-5

---

Markdown rendition of https://blog.dugong.live/how-to-add-a-gift-message-and-gift-wrap-at-checkout-on-shopify.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
