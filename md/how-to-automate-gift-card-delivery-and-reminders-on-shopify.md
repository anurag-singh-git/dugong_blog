# How to automate gift card delivery and reminders on Shopify

> The buyer paid, the admin says sent, and the birthday came and went. The AI playbook that lands every Shopify gift card and wakes every sleeping balance.

- Canonical: https://blog.dugong.live/how-to-automate-gift-card-delivery-and-reminders-on-shopify.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-08-10
- Updated: 2026-10-24
- Section: Research
- Word count: 2800
- Dispatch: Nº 104 · Research · 10 min read
- Full headline on page: How to automate gift card delivery and reminders *on Shopify*
- Keywords: shopify gift card email not received, shopify gift card not sent, resend gift card shopify, shopify gift card recipient form, schedule gift card delivery shopify, shopify gift card expiry, gift card balance reminder, gift card breakage, shopify flow gift card
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

The order lands on a Tuesday at 9:41 pm: one digital gift card, seventy five dollars, and a message in the recipient form that says Happy 30th, Maya. Love, Dan. Dan has done everything right. He typed his sister's email, wrote the message, and picked September 12, her birthday, from the little calendar. Then he paid the way he pays for everything, with the express checkout button his phone offered, and that one tap quietly undid the rest. Shopify's gift card recipient form does not support accelerated checkout buttons. The card mailed itself to Dan, immediately. The schedule never existed.

Dan does not notice, because the email looks like a receipt and receipts are for ignoring. September 12 comes and goes. On the 14th, no thank-you text having arrived, he checks, finds the code sitting in his own inbox under two weeks of promotions, and writes the store a message with the word unacceptable in it. The merchant opens the admin and finds nothing wrong: order paid, card issued, notification sent, every light green. The birthday was still missed, and of the three people involved, the store was the only one who could have known in time.

The [gift card](https://en.wikipedia.org/wiki/Gift_card) is the strangest product in your catalog. It costs nothing to ship, carries no inventory, and is paid in full before it exists. It is also the only product that is entirely a promise: the customer hands you money, and what they get is your obligation to hand it back later, as merchandise, to someone you have usually never met. Bankrate has measured how that promise ages. As of its 2024 survey, 43 percent of American adults were sitting on at least one unused gift card or store credit, an average of $244 per person, roughly $27 billion nationwide. A fifth of them have let a card expire outright. Walmart and Starbucks each carry more than a billion dollars of unspent card value on their books. None of that money is missing. All of it is asleep.

## The short answer

Shopify will mint the card and mail it, and that is the whole of what it guarantees. The only delivery state it records is sent: there is no delivered, no bounce, no open, and a typo in the recipient address reports success. Flow has no gift card trigger of any kind, so nothing in the platform can watch what happens next.

Four boundaries decide whether the card reaches the right person on the right day. Cards fulfill automatically on payment except in medium and high risk orders, which hold them silently. The recipient form is a theme feature, present from v9.0.0 of the free themes and off until someone ticks it, and its validation works only through Add to Cart, so an express checkout button drops the recipient details. The `Send on` date reaches 90 days at most, and scheduled cards go out between about 4:00 am and 10:00 am in the buyer's timezone rather than the recipient's.

So treat each card as an obligation with a clock on it rather than a line on a paid order. Confirm the fulfillment inside the hour, clear risk holds the same day, catch bounces and chase a missing recipient with one question, queue scheduled cards to the recipient's own morning, and tell the giver when it lands. Then keep going after delivery, because the money nobody spends is the larger number: 43 percent of American adults were holding an unused card in 2024, at an average of $244 *each*.

## An email with money inside

On Shopify, a sold gift card is a unique code inside a notification email, and everything that goes wrong starts with when and where that email travels. The when is gated by fulfillment. By default, gift cards fulfill automatically the moment the order is paid, and the email follows. But switch your store to manual fulfillment and the card waits for a human to click. And there is a quieter exception that catches stores with all the right settings: when an order is flagged medium or high risk, Shopify does not auto-fulfill the gift cards in it. The help documentation says it plainly: gift cards in that order aren't automatically fulfilled. The caution is not wrong, because instant digital delivery makes gift cards a favorite target for [stolen-card fraud](https://blog.dugong.live/how-to-stop-card-testing-attacks-on-shopify.html). But the hold is silent. Your [fraud filter](https://blog.dugong.live/how-to-handle-high-risk-orders-on-shopify.html) can strand a birthday, and nothing anywhere will say so.

The where has more trapdoors. The email reaches the recipient only if the buyer filled in the recipient form, and the recipient form is less a Shopify feature than a theme feature. It arrived in v9.0.0 of Shopify's free Online Store 2.0 themes, lives in Dawn and the Horizon family, does not exist on vintage themes, and even where it exists it is off until someone finds the checkbox that activates it, Show recipient information form for gift card products, inside the Buy buttons block of the theme editor. No form, and every gift card email goes to the buyer, who may or may not realize that forwarding it is now their job.

Fill the form and two footnotes still apply. The first is Dan's: the form's validation works only with the Add to Cart flow, not with accelerated checkout buttons, so the buyer most eager to pay is the one whose recipient details fall off. The second is timing: the `Send on` date can sit at most 90 days in the future, and scheduled cards go out approximately between 4:00 am and 10:00 am in the purchasing customer's timezone. The birthday email keys off the buyer's clock, not the birthday. And underneath all of it run two separate notification templates, New gift card for the recipient and Gift card receipt for the buyer; customize them, or carry customizations from before the recipient feature existed, and the recipient fields can simply be absent, along with the Add to Apple Wallet button that was supposed to put the card somewhere it could not be lost.

> Shopify can mint money it cannot deliver, and remember money it will never mention again.

> **◆ NOTE** Three boundaries worth knowing before the next gift card sells. Gift cards fulfill automatically on payment **except in medium and high risk orders**, which hold them silently. The recipient form is **theme-dependent** (v9.0.0 of the free themes and later), validates only through **Add to Cart**, schedules at most **90 days** ahead, and sends between **4:00 am and 10:00 am in the buyer's timezone**. And after creation the admin shows only the **last four characters** of any code, while **[Shopify Flow](https://help.shopify.com/en/manual/shopify-flow) has no gift card trigger** of any kind.

## Sent is not delivered

Search the community forums for gift card email not received and settle in; the genre runs back years and always has the same shape. A customer bought a card, the recipient has nothing, and the admin says sent. Sent is the only state Shopify has. There is no delivered, no bounced, no opened, no landed in spam under a casino newsletter. A typo in the recipient's email does not error; it mails seventy five dollars to a stranger-shaped void and reports success.

The security model then removes the obvious repair. Once a gift card is created, its full code is shown exactly once. After that the admin displays only the last four characters, and the API behaves the same way, returning the last characters and nothing more, because a gift card code is currency and Shopify treats reading it back as a hole. So you cannot look the code up and paste it into an apologetic email. What you can do is open Products, then Gift cards, find the card, and click Resend gift card, which works, one card at a time, provided you already know which card failed. Nothing in the system will tell you which cards failed. The store learns about a failed delivery from an angry human, weeks later, on the exact day the failure was engineered to hurt the most.

## The $27 billion that never gets spent

The cards that do land enter a second silence. Shopify keeps a perfect ledger of every card, its balance, its dates, its remaining value, and volunteers none of it to anyone. There are no balance reminders, no you-still-have-$43.50 note at the six month mark, no warning as an expiry date approaches. Expiry itself is a settings choice: under Settings, then Payments, gift cards default to never expiring, because expiring them is illegal in some countries, and if you set a term the default is five years. That number is not arbitrary: the US [CARD Act of 2009](https://en.wikipedia.org/wiki/Credit_CARD_Act_of_2009) made five years the federal floor, several states go further and ban expiration outright, and in many states a balance that sits unredeemed long enough becomes unclaimed property owed to the government, not kept by the store. [Breakage](https://en.wikipedia.org/wiki/Breakage), the industry's word for money that will never be spent, shows up in giant retailers' earnings as income. At your size it is mostly a liability line with paperwork attached.

Which is why reminding is not charity. A gift card recipient is usually a stranger to your store: someone else chose you for them, and the redemption visit is the [first visit](https://blog.dugong.live/how-to-segment-repeat-customers-on-shopify.html), the one where they decide what your brand is. A card spent is a customer acquired at zero ad cost. A card expired is a person who now remembers your brand as the small theft at the bottom of a drawer. The $244 sitting with the average American is not refusing to be spent. Nobody is asking for it.

The automation gap has a precise shape. Shopify Flow, the platform's own automation tool, has no gift card trigger: nothing fires when a card is created, sent, redeemed, or approaches its expiry date. What Flow does have, since the Get data actions arrived, is Get gift card data, which can query up to 100 cards at a time on a schedule and loop over the results. The raw material for a reminder program sits one query away. The program itself, the cadence, the copy, the thresholds, the legal footnote per jurisdiction, exists nowhere, because it was never going to ship as a checkbox.

## What the automation actually has to do

None of this needs invention. It needs the job description of a good concierge, executed every time: make sure the gift arrives, on the day it was meant for, tell the giver it landed, and never let the money be forgotten. As a Dugong playbook, in plain prose:

```
# trigger
On every gift card, from the minute
it is minted to the day it hits zero

# steps
1. Watch the send: fulfillment confirmed
   within the hour, risk holds cleared
   by a human the same day
2. Verify the landing: bounces caught,
   missing recipients chased with one
   question, resends in minutes
3. Honor the date: scheduled cards
   queued to the recipient's morning,
   buyer told when it lands
4. Wake the balance: nudge at 30 and
   90 days unspent, balance and code
   re-attached
5. Warn before the cliff: 60 and 14
   days out, where expiry is set
   and legal
6. Rescue the lost card: never-got-it
   answered with a resend, same hour
7. Report monthly: liability, redemption
   rate, aging cards, breakage named
```

Steps one and two are the chaperone Shopify never assigned. A gift card order still unfulfilled an hour after payment is either a settings problem or a risk hold, and a risk hold on a gift card deserves a same-day human decision, because a buyer is watching an inbox somewhere assuming the present is on its way. The landing check is the part merchants assume already exists: watch the notification actually leave, catch the bounce or the dead address the day it happens, and when a gift card order arrives through an express button with no recipient attached and a message that plainly names one, hold the send and ask the buyer a single question: was this meant for someone else? Dan answers that question in one minute on Tuesday night, or he writes the unacceptable email two weeks later.

Steps three through five are the memory. If a date was promised, queue the send yourself and aim it at the recipient's own morning instead of trusting a window pinned to the buyer's timezone, then tell the buyer the moment it lands, because the giver's anxiety is the quiet churn risk in the whole transaction. After that, remind: a nudge at 30 and 90 days of stillness with the balance stated and the code re-attached so nobody digs through old email, and where an expiry term is set and lawful, plain warnings at 60 and 14 days. Every reminder is your brand doing the recipient a favor with someone else's money, which is the cheapest goodwill in commerce.

Steps six and seven close the loop. She-never-got-it becomes a resend and a warm reply inside the hour, instead of a ticket that waits for Monday. And the monthly report carries the numbers this pipeline exists to move: total outstanding balance, redemption rate, cards aging toward expiry, and breakage named per month, routed to whoever does your books, because an auditor asking about unclaimed property is the expensive way to learn the word escheatment.

## Why this is a compiler problem, not an app problem

Gift card apps are real products, and the good ones run the storefront half well: designs, denominations, bulk issuance, greeting videos, their own scheduling stacks. But follow the card past the purchase and the failure tail runs through systems no app owns end to end: your risk tolerance on held orders, your email domain's deliverability, your theme's checkout quirks, your states' unclaimed property rules, your accountant's calendar. That is not a settings page. It is a paragraph of judgment, and it is different at every store, which is the argument behind [the automations no one builds](https://blog.dugong.live/best-shopify-automations-to-set-up.html): the paragraph should compile into the workflow, instead of being shaved down until it fits the checkboxes an app happened to ship.

Run Dan's Tuesday again with the paragraph compiled. The order lands at 9:41 with a gift card, no recipient attached, and a message that names a Maya. The playbook holds the send and asks Dan one question by reply. Recipient repaired by 9:52, card queued for the morning of September 12 on Maya's clock, Dan notified the moment it lands. Maya redeems on the 13th, a $75 card against a $112 basket, her first order at a store she had never heard of two days earlier. Nobody opened the admin. Nothing happened on the 14th, because there was nothing to find out.

## The workflow worth building this week

Start with an hour of honesty. Open Products, then Gift cards, and export everything. Three numbers matter: the total outstanding balance, which is the size of the interest-free loan your customers have made you and the liability your books should already carry; the count of cards with balance and no movement in six months; and the count inside 90 days of any expiry you set years ago and forgot. Then place two test orders for your own card: one through Add to Cart with the recipient form filled in, one through the express button. Watch which inbox each email reaches. Most stores learn something from the second test that they are glad to have learned on purpose.

Then run the playbook in draft mode for two weeks: let it flag the unfulfilled cards, catch the bounces, draft every nudge and resend, and send nothing. You are auditing its judgment against yours. Does it hold the send you would hold, ask the question you would ask, word the reminder the way you would say it. When its calls match yours, let the clean paths run and keep the risk holds and the odd ones for a human, which is where they belonged all along.

Then say the brief out loud, the way you would hand gift cards to a new hire. Watch every card from the minute it is minted. Make sure it lands where it was aimed, on the day it was meant for, and tell the giver. Nudge sleeping balances at 30 and 90 days, warn before anything expires, resend within minutes when someone asks, and show me the liability once a month. That is the whole paragraph. The compiler turns it into the workflow, and the drawer where $27 billion currently sleeps stays, for your store at least, empty.

> **◆ READING** Two companion pieces if this one landed: [the high-risk flag that makes you guess](https://blog.dugong.live/how-to-handle-high-risk-orders-on-shopify.html), on the risk analysis that quietly holds gift cards, and [the card-testing attack that floods your store](https://blog.dugong.live/how-to-stop-card-testing-attacks-on-shopify.html), on why fraud tools watch gift cards so closely in the first place.

If you are a Shopify merchant with a gift card horror story, a support inbox that fills every January with where-is-my-card emails, or a balance ledger you have never once looked at, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Why didn't my customer receive their Shopify gift card email?

Work through four suspects in order. First, fulfillment: the gift card email goes out when the card is fulfilled, and while gift cards fulfill automatically on payment by default, a store switched to manual fulfillment leaves the card waiting for a click, and medium and high risk orders skip automatic gift card fulfillment entirely, so a fraud flag can hold the send in silence. Second, the recipient form: unless your theme supports the form, it is activated in the theme editor, and the buyer filled it in through the standard Add to Cart flow, the card goes to the purchaser rather than the recipient, and accelerated checkout buttons bypass the form's validation altogether. Third, the address itself: a typo in the recipient email neither errors nor bounces anywhere you can see, because the admin has no delivered or bounced state, only sent. Fourth, spam. The repair is the Resend gift card button on the card's page under Products, then Gift cards, and since the admin shows only the last four characters of any code after creation, resending is the only repair there is.

Permalink: https://blog.dugong.live/how-to-automate-gift-card-delivery-and-reminders-on-shopify.html#faq-1

### Can customers schedule a Shopify gift card to send on a specific date?

Yes, within boundaries worth knowing before you promise anyone a birthday. The recipient form's optional Send on date schedules a card at most 90 days in the future, and scheduled cards go out approximately between 4:00 am and 10:00 am in the purchasing customer's timezone, so the delivery morning keys off the buyer's clock unless the theme passes the recipient's timezone offset along. The form itself is a theme feature: it arrived in v9.0.0 of Shopify's free Online Store 2.0 themes, lives in Dawn and the Horizon family, does not exist on vintage themes, and stays off until the Show recipient information form for gift card products checkbox is enabled in the Buy buttons block. And the form's validation supports only the Add to Cart flow, so a buyer who pays with an accelerated checkout button can lose the recipient details, in which case the card sends immediately to the buyer and no schedule exists. If a specific date genuinely matters, an automation that queues the send itself and confirms to the buyer when the card lands is the only version of the promise you fully control.

Permalink: https://blog.dugong.live/how-to-automate-gift-card-delivery-and-reminders-on-shopify.html#faq-2

### Do Shopify gift cards expire, and should you set an expiry?

By default Shopify gift cards never expire, and the setting lives under Settings, then Payments, in the Default expiration section. If you switch expiry on, the default term is five years, which matches the floor the US CARD Act of 2009 sets for how quickly gift card funds can expire; several states are stricter, some ban gift card expiration outright, and in many states balances that sit unredeemed long enough become unclaimed property owed to the state rather than kept by the store, so check the rules everywhere you sell before touching the setting. The better question is what happens before any expiry: Shopify sends no balance reminders and no expiry warnings, and Bankrate's survey work counts about $27 billion of unused gift card value held by 43 percent of American adults, an average of $244 per person. A reminded card gets spent, and a spent card is usually a new customer's first visit to your store; an expired card is a small grudge with your brand's name on it. Remind first, and treat expiry as a legal detail rather than a revenue plan.

Permalink: https://blog.dugong.live/how-to-automate-gift-card-delivery-and-reminders-on-shopify.html#faq-3

### Can Shopify Flow send gift card reminders?

Not from a trigger, because Flow has no gift card trigger of any kind: nothing fires when a card is created, sent, redeemed, or approaches its expiry date. What Flow does have, since the Get data actions arrived, is Get gift card data, which can query up to 100 cards at a time on a schedule and loop over the results, so the raw material for a reminder program sits one query away. The program itself is the part that exists nowhere as a checkbox: a nudge at 30 and 90 days of stillness with the balance stated and the code re-attached so nobody digs through old email, plain warnings at 60 and 14 days where an expiry term is set and lawful, and a monthly report of outstanding balance, redemption rate, aging cards, and breakage, routed to whoever does your books.

Permalink: https://blog.dugong.live/how-to-automate-gift-card-delivery-and-reminders-on-shopify.html#faq-4

### Why is my customized gift card email missing the recipient details?

Because two separate notification templates carry gift cards, and customizations age badly. New gift card goes to the recipient and Gift card receipt goes to the buyer; customize either, or carry customizations from before the recipient feature existed, and the recipient fields can simply be absent from the email, along with the Add to Apple Wallet button that was supposed to put the card somewhere it could not be lost. The reliable diagnostic is two test orders for your own card: one through Add to Cart with the recipient form filled in, one through the express checkout button, then watch which inbox each email reaches, since the form validates only on the Add to Cart flow and an express button sends the card to the buyer. Most stores learn something from the second test that they are glad to have learned on purpose.

Permalink: https://blog.dugong.live/how-to-automate-gift-card-delivery-and-reminders-on-shopify.html#faq-5

---

Markdown rendition of https://blog.dugong.live/how-to-automate-gift-card-delivery-and-reminders-on-shopify.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
