# How to fix Shopify Flow emails that never send

> Your workflow ran. The step went red. Shopify will not send a marketing email to a customer who is not subscribed to marketing, and most of your buyers are not.

- Canonical: https://blog.dugong.live/how-to-fix-shopify-flow-emails-that-never-send.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-11-04
- Section: Research
- Word count: 2841
- Dispatch: Nº 139 · Research · 10 min read
- Full headline on page: How to fix Shopify Flow emails that never send *to most of your customers*
- Keywords: shopify flow email not sending, customer not subscribed to marketing, shopify transactional email flow, send marketing email action, shopify marketing consent, pending email subscribers shopify, email subscription status shopify, double opt-in pending, AI order notifications
- Entities: Shopify (https://www.wikidata.org/wiki/Q7501150); Email spam (https://www.wikidata.org/wiki/Q13512320); Customer relationship management (https://www.wikidata.org/wiki/Q485643); Business process automation (https://www.wikidata.org/wiki/Q5001911)
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

The workflow took ten minutes to build. Order fulfilled, wait two days, send the customer a short note about where their made-to-order piece is in the queue. You tested it against your own account and the email arrived in seconds.

Three weeks later a customer asks why nobody ever told her anything. You open the workflow. It has run two hundred and forty times. Most of those runs carry an error, and the error is the same one every time:

`Exception: Email not sent because Sarah Mitchell is not subscribed to marketing.`

Not failed. Not delayed. Shopify looked at the customer, decided she had not agreed to hear from you, and declined on your behalf.

## The short answer

Shopify Flow ships with exactly one email action, Send marketing email, and its recipient field is fixed to customers subscribed to email marketing. There is no option to deselect it. Every customer who is not subscribed produces an exception instead of a message.

Most of your buyers are in that group. The marketing checkbox at checkout is optional and has to stay optional, so a large share of people who buy from you never tick it. If you have double opt-in switched on, the ones who do tick it sit in pending until they click a link in a confirmation email, and pending is treated as not subscribed too.

Flow has no transactional email action at all, which is the part that catches people out. An order update feels like the most ordinary thing an automation could send, and it is the one thing this action cannot be used for.

So the fix is not a setting. It is a split. Order information goes out through Shopify's own notifications or a connected email service, where consent is not the gate. Marketing goes through the consent gate as designed. And somebody has to know, as a number, how many of your customers are actually on the far side of that gate.

## Flow has one email action and you cannot change who it goes to

This is the whole mechanism, and it has not changed in three years.

A merchant running in-person training classes described it clearly in [January 2023](https://community.shopify.com/t/sending-emails-with-shopify-automation-send-regardless-of-opt-in-status/180892). He wanted to email everyone who bought a ticket with the lodging, schedule and food details, which is about as transactional as an email gets. The action offered one recipient, customers subscribed to email marketing, and he noted that there is no option to deselect it. A Shopify partner replied the next day that the action cannot reach customers who are not subscribed, and that the only way around it is to use a third-party app's email action in Flow.

Then, nearly three years later, in [October 2025](https://community.shopify.com/t/shopify-flow-email-error-customer-not-subscribed-to-marketing-need-alternative-solution/570799), a merchant with a fulfillment window of around fifty days asked the same question and got the same answer, this time from a Shopify specialist: the action requires marketing consent, and there is currently no built-in Flow action for transactional emails. Another reply made the obvious point that the action is called Send *marketing* email, so respecting the marketing state is the correct behavior rather than a defect. Nothing in the thread is marked as a solution.

It is worth knowing why, because the reason is sound and it tells you not to wait for a fix. A Shopify staff member explained in the 2023 thread that transactional email is a product in its own right, that Flow cannot guarantee that the email would not be used for marketing purposes, and that one store abusing a free transactional channel would cost every store on the shared sending reputation. That is a defensible position. It is also a permanent one.

## The run goes red, and nobody is looking at the run

The failure mode here is not the gate. It is that the gate reports itself in the one place nobody reads.

Flow does not skip a non-subscribed customer silently in the sense of recording nothing. It records an exception on the step and moves on. The workflow keeps running, the trigger keeps firing, and the run log fills up with a line that would tell you everything if anybody opened it. On an ordinary Tuesday nobody opens it. You find out when a customer asks.

So the symptom you actually experience is a workflow that looks healthy from the outside and delivers to a fraction of the people it was built for. If that shape is familiar, it is the same shape as [workflows that fail silently](https://blog.dugong.live/how-to-catch-shopify-flow-workflows-that-fail-silently.html) in general: Flow's own reporting is built for debugging a workflow once, not for watching one for six months.

The gate is not only Flow's, either. Shopify's [marketing automations documentation](https://help.shopify.com/en/manual/promoting-marketing/create-marketing/create-marketing-automations) says that marketing automations send only to customers subscribed to marketing by default. There is exactly one exception, abandoned checkout, where the recipient field can be changed to All customers in the email editor, and the same page notes that you cannot override this setting for SMS or WhatsApp automations. A merchant in the October 2025 thread confirmed in April 2026 that Shopify's messaging automations are sent only to customers who are subscribed to marketing, which rules out the obvious workaround.

One abandoned-checkout exception, and everything else behind the gate. That is the full extent of the flexibility you have.

## Not subscribed and unsubscribed are not the same thing

Shopify's Admin API is more precise about this than the admin screen is. The [email marketing state](https://shopify.dev/docs/api/admin-graphql/latest/enums/CustomerEmailAddressMarketingState) on a customer has five values: subscribed, not subscribed, pending, unsubscribed and invalid. The documentation defines not subscribed as the customer is not subscribed to email marketing, and unsubscribed as the customer is not subscribed to email marketing but was previously subscribed. Pending means the customer is in the process of subscribing. Invalid means the state itself is broken, which in practice usually means a malformed address.

At send time Shopify treats one of those five as yes and the other four as no. That is correct, and it also flattens the only distinction that matters to you.

A not subscribed customer is a gap in your collection. Nobody asked them, or they were asked at a bad moment. An unsubscribed customer made a decision, and the correct response to a decision is to respect it. A pending customer said yes and then did not finish. Those are three different jobs with three different answers, and most merchants have one number that covers all of them.

Pull them apart before you do anything else. In almost every store the recoverable group is far larger than the group that said no, and it is sitting under a label that makes it look like a lost cause.

## Why most of your buyers were never going to be subscribed

Shopify's page on [collecting customer contact information](https://help.shopify.com/manual/promoting-marketing/customer-emails) describes a narrow mechanism. Consent is captured at checkout when the customer selects the marketing checkbox and proceeds with checkout. You can choose the regions where the box is preselected, based on local law or by hand, and if you choose no regions it is never preselected. Even where it is preselected, customers can still deselect it.

Which means your subscriber rate is mostly decided by a checkbox at the end of a checkout, at the moment the customer has already got what they came for and wants the page to go away.

Merchants regularly try to make it mandatory. One asked in [August 2023](https://community.shopify.com/t/customers-who-ordered-and-email-marketing/238586) whether checkout could require an email marketing subscription, having found that his third-party email tool was missing customers who had ordered without subscribing. The replies covered a required email field, post-purchase invitations, and privacy policy wording, and also warned that a forced checkbox is not lawful everywhere. A later reply stated the position plainly: Shopify separates customers from email subscribers, and the marketing opt-in at checkout has to stay optional.

Making the email field required, which people do try, changes nothing here. An address is not consent. You end up with a complete customer list and the same locked automation.

## The pending queue you are not allowed to clear

Double opt-in is where the gap goes from large to strange.

With it on, ticking the box does not subscribe anybody. Shopify holds the customer in pending, sends a confirmation email, and waits for a click. Customers who were already subscribed before you switched double opt-in on are not asked to confirm, so the queue only grows from the day you turn it on.

The [thread about pending customers](https://community.shopify.com/t/how-do-i-confirm-pending-customer-emails/190009) has been running since February 2023 and reads like a slow-motion survey of the same discovery. The original poster found a wall of customers showing Pending and Email awaiting confirmation, and asked whether he needed to do something. A Shopify staff member answered that merchants do not need to do anything to confirm the subscriptions at that stage, which is true and is also not what the merchant was worried about. In October 2023 someone turned double opt-in off, which fixed new customers, and asked what to do about the existing pending ones. In December 2023 a merchant with thousands of pending statuses asked whether they could be changed to subscribed in bulk, and got no reply. In December 2024 another reported more than four hundred and fifty pending, then wrote again at the end of the month to say about half of all their customers were pending, that reminding people one at a time recovers some of them, and asked how to send a second email to all pending customers. No reply to that one either.

A separate [thread from September 2023](https://community.shopify.com/t/email-subscriptions-over-200-pending-get-rid-of-the-double-opt-in/246607) puts the ratio in plain numbers. Over two hundred customers had left the checkout box ticked, and only a fair few had actually confirmed.

And the advice from Shopify in the first thread, repeated twice, is not to send reminders to pending customers, because it could be seen as spam. That is reasonable advice. It is also the bind in one sentence: the only people you are allowed to email at scale are the ones who have already said yes, so the pending queue is not a backlog you work through. It is the price of double opt-in, paid once per customer, and the only lever you have on it is the quality of the original ask.

Decide deliberately whether you want double opt-in at all. If you are not sending from a shared domain with a damaged reputation, and you are not subject to a jurisdiction that requires confirmation, the cost is usually higher than the benefit.

## The consent your email tool thinks you have

If you send through Klaviyo, Omnisend, Mailchimp or anything similar, you have two consent records, written at different times by different systems, and the lower of the two decides whether a message goes out.

A [thread opened in September 2024](https://community.klaviyo.com/marketing-30/accepts-marketing-in-shopify-but-not-subscribed-in-klaviyo-14918) works through why. Shopify's accepts marketing field is a Shopify field. It becomes a subscription in your email tool only once the sync is turned on, and the sync applies to opt-ins collected after that point, so every consent you gathered before you set it up reads as accepted in Shopify and never subscribed in the email tool. Historical contacts need a deliberate update, not patience.

The harder version of the problem is also in that thread. Merchants with the sync enabled, and accepts marketing set to true in Shopify, report profiles that still read never subscribed, one of them as recently as July 2026, asking whether the cause is a delay, a separate webhook or a double opt-in setting somewhere. Nobody in the thread resolves it.

The operational lesson is not which system is right. It is that you cannot work out your reachable audience from either one on its own. Pull the count from both, match on email address, and treat every mismatch as a defect with an owner rather than as noise.

## What this costs you on an ordinary month

Take a store doing fifteen hundred orders a month from about twelve hundred distinct customers, with a checkout opt-in rate of a quarter and double opt-in on, confirming at roughly a third.

Three hundred customers tick the box. Around a hundred confirm. So the review request, the post-delivery follow-up, the replenishment nudge and the progress update on a made-to-order item all reach about one customer in twelve, and the workflow reports two hundred and something exceptions a month that nobody reads as a number.

The money is not in the emails you failed to send. It is in the decisions you made on top of a broken assumption. You judged a review request flow that technically never ran. You concluded that post-purchase email does not work in your category. You answered the same two support questions all year because the automation that was meant to pre-empt them was delivering to eight percent of its audience.

None of that shows up as a failure anywhere. It shows up as a store where automation does not seem to do much.

## What the automation actually has to do

As a Dugong playbook, in plain prose:

```
# trigger
Scheduled daily consent sweep,
plus order fulfilled

# steps
1. Sort every customer by what
   you may send
2. Route order news off the
   marketing path
3. Watch the workflow run, not
   the inbox
4. Ask for consent at the moment
   it is earned
5. Clear the pending queue once,
   properly
6. Reconcile consent with your
   email tool
7. Report reachable customers
   every month
```

Step one is the foundation and takes an afternoon once. Four buckets: subscribed, pending, never asked, said no. Every automation you build afterwards declares which bucket it is for, and you stop building things for an audience that does not exist.

Step two is the actual fix for the problem in the error message. Order status, shipping, delays, pickup reminders and progress on a custom item are transactional. If Shopify models the event, use its notification templates, which go to every customer. If it does not, connect an email service to the workflow and use its send action, which is not gated on a marketing opt-in. Never route operational information through the marketing action, even when it is quicker.

Step three is monitoring the right surface. An exception on a send step is the evidence, and it lives in a log with a fourteen-day memory. Read the runs, count the exceptions by reason, and alert on a rate rather than on a single failure.

Step four moves the ask to where it works. A checkout is the worst moment to ask somebody for a long-term relationship. A week after a delivery that went well is a good one, and the order is already in the system. Ask once, by a channel you are allowed to use, and record the answer.

Step five is a decision rather than a campaign. Work out what pending is costing you, then either turn double opt-in off and keep the queue as a historical artefact, or keep it on and accept the confirmation rate as a known number. What you must not do is leave it on and pretend those customers are subscribers.

Step six is the reconciliation. Match Shopify's consent record against your email tool's, by address, on a schedule. Report the count that disagrees. Every one of those rows is a customer who is reachable in one system and invisible in the other.

Step seven is the number that makes the rest stick. Publish, monthly, the share of your buyers you can legally reach. It is the denominator under every piece of lifecycle marketing you do, and almost nobody tracks it.

## Do this before you close the laptop

Three things, about twenty minutes, before you automate anything.

Open your most important Flow workflow with an email step and read the run log rather than the summary. Count the exceptions. That number against the run count is your real delivery rate, and you have probably never seen it.

Then build a customer segment for email subscribers and put its size next to your total customer count. The ratio is the ceiling on every marketing automation in the store. If it is under a fifth, the automation is not your problem.

Last, check whether double opt-in is on, and if it is, count how many customers are pending. If that number is anywhere near your subscriber count, you have a second store's worth of people who said yes and were never counted.

> **◆ READING** Two companion pieces if this one landed: [the automation that quietly stopped running](https://blog.dugong.live/how-to-catch-shopify-flow-workflows-that-fail-silently.html), on why Flow's own reporting hides this class of problem, and [the order confirmation that never arrives](https://blog.dugong.live/how-to-fix-order-confirmation-emails-not-sending-on-shopify.html), on the transactional mail that fails for completely different reasons.

If you sell on Shopify and have a version of this story, the workflow that ran two hundred times and delivered twelve, the pending queue nobody could explain, the consent count that disagreed with your email tool by a thousand, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Why does Shopify Flow say the email was not sent because the customer is not subscribed to marketing?

Because the only email action Flow ships with is Send marketing email, and its recipient field is fixed to customers subscribed to email marketing. When the workflow reaches a customer who is not subscribed, it does not skip the step quietly. It records an exception that reads Email not sent because the customer is not subscribed to marketing, and carries on. A merchant hit exactly this in a thread opened in October 2025, trying to send order updates across a fulfillment window of about fifty days. A Shopify specialist confirmed the next day that the action requires marketing consent and that there is currently no built-in Flow action for transactional emails. Nothing in that thread is marked as a solution. The same answer had already been given almost three years earlier: in January 2023 a merchant pointed out that there is no option to deselect the recipient field, and was told that the only way around it is to use a third-party app's email action in Flow. So this is not a bug in your workflow and not a setting you have missed. The action does what it says, and the word marketing in its name is doing the work.

Permalink: https://blog.dugong.live/how-to-fix-shopify-flow-emails-that-never-send.html#faq-1

### Can Shopify Flow send transactional emails?

Not on its own. Flow has no transactional email action, which is the part most people do not expect, because an order update feels like the most natural thing in the world for an automation to send. The reasoning a Shopify staff member gave in January 2023 still holds: transactional email is a product in its own right, Flow cannot guarantee that the email would not be used for marketing purposes, and one store abusing it would damage deliverability for every store on the shared sending infrastructure. The practical routes are three. Order status information that Shopify already knows about belongs in the notification templates under Settings, which send to every customer because they are transactional by definition. Anything Shopify does not model, such as a made-to-order progress update, needs an email service connected to the workflow, which gives you an email action that is not gated on marketing consent. And a handful of cases are better off not being email at all: a tag on the order plus a note on the customer record is often what the person actually needed.

Permalink: https://blog.dugong.live/how-to-fix-shopify-flow-emails-that-never-send.html#faq-2

### What is the difference between not subscribed and unsubscribed on a Shopify customer?

One of them never answered the question and the other said no. The Admin API spells out five states for a customer's email marketing. Subscribed means the customer is subscribed to email marketing. Not subscribed means the customer is not subscribed to email marketing. Pending means the customer is in the process of subscribing. Unsubscribed means the customer is not subscribed but was previously subscribed. Invalid means the state itself is invalid, which usually points at a malformed address. At send time Shopify treats the first state as yes and the other four as no, which is correct and also hides the only distinction that matters commercially. A not subscribed customer is a gap in your collection: nobody asked them, or they were asked in a moment when they were not going to say yes. An unsubscribed customer is a decision, and the right response is to leave them alone. If your consent report shows one number for both, you cannot tell the recoverable group from the finished one, and the recoverable group is usually much the larger of the two.

Permalink: https://blog.dugong.live/how-to-fix-shopify-flow-emails-that-never-send.html#faq-3

### Why are so many of my Shopify email subscribers stuck on pending?

Because double opt-in asks for a second action that most people never take. With it on, ticking the box at checkout does not subscribe a customer. They are placed in pending, Shopify sends a confirmation email, and only a click on the link in it moves them to subscribed. Merchants describe the result the same way year after year. One wrote in September 2023 that over two hundred customers had left the box checked and only a fair few had actually confirmed. Another asked in December 2023 whether thousands of pending statuses could be bulk-changed to subscribed, and got no reply. A third wrote in December 2024 that roughly half their customers were pending, that reminding people one at a time recovers some, and asked how to send a second email to all pending customers. No reply there either. Shopify's own guidance in that thread is that merchants do not need to do anything to confirm the subscriptions, and separately that sending a reminder to pending customers is not recommended because it could be seen as spam. Which is the bind: the people you are allowed to email at scale are the ones who already said yes. Pending is not a queue you can work through. It is the cost of double opt-in, and the only lever you have is the moment of asking.

Permalink: https://blog.dugong.live/how-to-fix-shopify-flow-emails-that-never-send.html#faq-4

### Why does a customer who accepted marketing in Shopify show as not subscribed in Klaviyo?

Because they are two consent records, written at different times by different systems, and the lower of the two decides whether an email goes out. The Shopify field only becomes a Klaviyo subscription if the sync is turned on, and the sync applies from the day you turn it on, so every opt-in collected before that sits in Shopify as accepted and in Klaviyo as never subscribed. That was the answer accepted in a September 2024 thread, and it still leaves the historical contacts needing a deliberate update rather than a wait. The thread also shows the harder version of the problem: merchants with the sync enabled and accepts marketing true in Shopify reporting profiles that still read never subscribed, one of them as recently as July 2026, asking whether the cause is a delay, a separate webhook or a double opt-in setting. The lesson for an operator is not which tool is right. It is that you cannot infer your reachable audience from either platform alone. Pull the count from both, compare them by email address, and treat the difference as a defect with an owner rather than a rounding error.

Permalink: https://blog.dugong.live/how-to-fix-shopify-flow-emails-that-never-send.html#faq-5

### Can AI fix Shopify automated emails that never send?

Yes, and the useful work is mostly sorting and watching rather than writing. An automation like Dugong starts by sorting every customer into what you are allowed to send them, so the workflow you are about to build knows its real audience before it runs once. It routes order information off the marketing path entirely, into Shopify's own notifications or a connected email service, so an operational message is never gated on a marketing opt-in. It reads the workflow run rather than the inbox, which is where the evidence actually is: an exception on a send step is the signal, and nobody opens Flow's run log on an ordinary Tuesday. It asks for consent at the moment it is earned, after a delivery that went well rather than in the middle of a checkout. It reconciles Shopify's consent record against your email tool's record by address and reports the mismatch. And it publishes one number every month, the share of your buyers you can legally reach, so the thing gets managed instead of assumed. The honest limits: it cannot manufacture consent, it cannot confirm a pending subscriber on their behalf, and it will not make a customer who unsubscribed reachable again. What it can do is stop you believing a message went out when it did not.

Permalink: https://blog.dugong.live/how-to-fix-shopify-flow-emails-that-never-send.html#faq-6

---

## Read next

- [The automation that quietly stopped running](https://blog.dugong.live/how-to-catch-shopify-flow-workflows-that-fail-silently.html): Flow marks a run Completed when actions fail, alerts once per 30 days, and deletes run history after 14. The AI playbook that watches outcomes, not logs.
- [The order confirmation that never arrives](https://blog.dugong.live/how-to-fix-order-confirmation-emails-not-sending-on-shopify.html): Shopify order confirmations that never send: spam, typos, suppressed channels, no resend button. The AI playbook that catches every silent order in minutes.
- [The review request you never send](https://blog.dugong.live/how-to-automatically-request-product-reviews-on-shopify.html): Shopify has no native way to ask for a review, so it never goes out or it blasts everyone at the wrong time. The AI playbook that requests reviews after delivery.
