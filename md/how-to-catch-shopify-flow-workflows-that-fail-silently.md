# How to catch Shopify Flow workflows that fail silently

> Flow marks a run Completed when actions fail, alerts once per 30 days, and deletes run history after 14. The AI playbook that watches outcomes, not logs.

- Canonical: https://blog.dugong.live/how-to-catch-shopify-flow-workflows-that-fail-silently.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-09-20
- Updated: 2026-10-24
- Section: Research
- Word count: 2900
- Dispatch: Nº 120 · Research · 11 min read
- Full headline on page: How to catch Shopify Flow workflows that *fail silently*
- Keywords: shopify flow not working, shopify flow workflow failed, shopify flow completed but not working, shopify flow error notification, shopify flow run history, shopify flow rate limited, shopify automation monitoring, AI automation monitoring
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

The VIP tag stopped happening on a Tuesday. Nobody noticed until the following Thursday, when a customer who has spent eleven thousand dollars with you over two years emailed to ask why she was being offered the welcome discount again.

You open Shopify Flow. The workflow is there. It is switched on. The run list is full of runs, and every single one of them says *Completed*.

Nothing is broken, according to the only screen that would tell you.

## The short answer

Watch the outcome a workflow is supposed to produce, not its run list. Completed in Shopify Flow means only that a run *stopped*, not that it worked, so an action can fail inside a run the log reports as Completed. Shopify staff have confirmed the mechanism. A failure stops the branch it happens on, and a workflow with parallel actions or a loop has several branches, so one dead branch never marks the run.

The native alarm does not close the gap. The Workflow error occurred trigger fires once per workflow version in any thirty day period, however many times the workflow fails, and the counter resets only when you edit the workflow or when thirty days pass. Run history is deleted 14 days after a run completes, and the run search reaches no further back than that. A workflow that stops firing altogether leaves no run at all, and an empty list looks exactly like a quiet week.

So the check belongs in your store data. Write one sentence for each automation describing what should be true when it works, such as an order over two hundred dollars always ending with that customer tagged, then count that against the store on a schedule. Alarm on zero runs as loudly as on errors, archive the run list daily so day fifteen still has a memory, and re-verify after every edit, app update and platform release.

## Completed does not mean it worked

This is the first thing to understand about Flow, and almost nobody does until it costs them something. Shopify's own documentation lists five run statuses. In progress means currently executing or retrying. Waiting means a wait step has delayed a workflow. Rate limited means the workflow was using too many resources, so Flow limited the execution. Canceled means the workflow was stopped before it could complete.

And Completed means, in full, one word: done.

Done is not succeeded. A run reaches Completed when it stops, whatever it did or failed to do on the way. A developer worked this out in public on January 2, 2026, after watching an HTTP request fail inside a loop while the run reported success. I am not sure why the Run status shows as Completed when one action had an error, he wrote. He answered his own question a few posts later: a workflow shows Completed whenever it is not running, cancelled or rate limited, regardless of what the individual actions did.

A Shopify staff member confirmed it and added the mechanism. The fail will stop execution for that path, which is usually the same as the workflow. However, here you have many paths because you have actions running in parallel and a loop. In other words, one dead branch of a workflow with several branches does not mark the run. The run finishes. The log says Completed. The tag never got applied.

> **◆ NOTE** If you are monitoring Flow by scanning the run list for the word failed, you are monitoring the one thing Flow is least likely to show you. Filter on Errors instead, which is a separate facet from status, and assume the two disagree.

## The alert fires once and then goes quiet

Flow does have an alarm. It is a trigger called Workflow error occurred, and the documentation describes it plainly: it starts a workflow when workflows fail during execution. You point it at an email action or a Slack message and you have built yourself a monitor.

Then you read the limit. The trigger runs once per workflow version within a thirty day period, however many times that workflow fails. It resets only if you edit the workflow, which creates a new version, or if thirty days pass since the last notification.

Shopify says why, and the reasoning is defensible: error notifications are designed to limit noise, so you will only get one notification per workflow version.

Consider what that means on a store doing four hundred orders a day. A workflow breaks on the first of the month. You get an email. The workflow then fails on every order for twenty nine days, in silence, and the inbox stays clean because the alarm has already been used up. If you were away that first day, or the mail went to a shared address nobody watches, or you read it and meant to look later, the next signal you get is a customer.

An alarm that rings once a month is a smoke detector with one battery and no replacement.

## The evidence deletes itself in fourteen days

Here is the second structural problem, and it is the one that turns a bad week into an unresolvable one.

Shopify's documentation on monitoring workflow runs is unambiguous. Workflow runs are stored for 14 days after a run has completed. After 14 days, the run is removed from the system. The search that lets you find a run by order number or customer ID carries the same ceiling: the search is limited to the last 14 days of workflow runs.

Fourteen days is shorter than most of the loops that actually catch these failures. A monthly reconciliation catches it on day thirty. A quarterly audit catches it on day ninety. A customer complaint arrives whenever the customer happens to notice. By the time anyone asks how long has this been wrong, the runs that would answer the question have been deleted, and the only remaining evidence is the shape of the damage in your order data.

Nobody plans for this. You discover it at the moment you most need the log, which is also the moment it is gone.

## The failure with no run at all

Everything so far assumes a run happened and went wrong. The worst case is quieter than that.

A workflow can simply stop firing. The trigger stops matching because a tag was renamed. Someone deactivated it during a busy week and forgot. An app that supplied the trigger or the action was uninstalled or changed its scopes. A condition that used to be true for half your orders is now true for none of them.

When that happens there is no failed run to find, because there is no run. The run list is not wrong, it is empty, and an empty list looks exactly like a quiet week. Every monitoring approach built on watching runs shares the same blind spot: you cannot detect a missing run by looking at runs.

This is the failure mode that costs the most and gets caught the latest, and it is the reason the rest of this piece is about outcomes rather than logs.

## Sometimes it is not your workflow

The community record is worth reading, because it kills the instinct that a broken Flow is always something you did.

On April 1, 2025 a merchant reported that a signup automation had stopped sending entirely. It worked for several month correctly, another merchant added in the same thread. Since Monday it does not work anymore. A third: it is really weird, as a few weeks ago I had one set up and it was all working perfectly. Staff first pointed at third party forms and marketing consent, the usual suspects, and then on April 3 came back with the real answer. Turns out there was an issue with a recent release that was causing issues with double opt in. The issue should be fixed now.

On May 29, 2025 a Plus merchant found a workflow that updates a company metafield had begun erroring against a field it had written to for months. Today we went to test it again, had used it before and worked perfect, and it was erroring. The log showed Flow submitting a list where the metafield expected a single integer. The fix was to point the action at a different metafield, save the whole workflow, then point it back. In the end it is identical to what it was, the merchant wrote, but something on the Shopify side had started trying to update with the wrong type and resetting it fixed it.

On September 26, 2024 a merchant watching workflows hang in progress and fail halfway concluded, reasonably, that it is some update on the backend of Shopify or Flow that is causing this error. Two other merchants in the same thread had the same symptom. No staff answer appears in it.

And on February 3, 2026 a merchant posted the purest version of the problem: the admin was showing a banner that said recent runs contain errors, and the runs themselves showed nothing. Staff replied the same day, then again on February 6 and February 9, suggesting a search filter. The thread ends without a cause.

> **◆ NOTE** Four separate years, one pattern: the workflow did not change, the ground underneath it did. Platform releases, type coercion, app updates and scope changes all break automations that you will swear you have not touched. Version pinning does not exist here. The only defense is checking that the outcome still arrives.

## The other silent one: rate limited

There is a fifth status that deserves its own mention, because merchants consistently read it as a delay when it is closer to a decision.

Rate limited means the workflow was using too many resources, so Flow limited the execution. It is not an error. It will not trip the error trigger. It arrives during exactly the periods you care about most, which are the flash sale, the drop, the Black Friday hour when six hundred orders land in ninety minutes and every one of them fans out into four workflows.

Shopify's optimization guidance is honest about the arithmetic behind it. Your shop is limited in how many requests it can handle at once by the API limits, and workflows using a Get data action are designed to return a maximum of 100 objects per workflow. The store-wide limits are real, they are shared across every workflow and every app you run, and a workflow that loops over line items will hit them faster than you expect.

Worth knowing alongside it: Flow caps a store at 1,000 workflows, a workflow at 40 wait steps and 90 days of total waiting, a config field at 50 kB, and every workflow section at a combined 36 hours of execution. Those ceilings do not announce themselves either.

## What monitoring actually has to watch

Put the five failure modes side by side and one conclusion falls out.

An action fails but the run says Completed. The alarm fires once per version per month. The evidence expires on day fourteen. The workflow stops firing and produces no run to inspect. The platform changes under a workflow you never edited.

Not one of those is reliably visible in the run list, which means the run list is the wrong thing to watch. The right thing to watch is the outcome the workflow exists to produce.

A workflow that tags VIP customers is not really a workflow. It is a promise that every order over two hundred dollars leaves a tagged customer behind it. That promise is checkable against your own store data, right now, without touching Flow at all, and it stays checkable long after the runs have been deleted. Ask the store how many orders in the last twenty four hours crossed two hundred dollars, ask how many of those customers carry the tag, and the difference between the two numbers is the only monitor that catches all five failures at once.

Shopify has moved a little way toward this. A March 24, 2026 changelog added a Get workflow run data action, which retrieves information about a workflow run, including the workflow it belongs to, the event that triggered it, retry attempts, and timing details, so that you can build workflows that monitor or report on other workflow activity. It is genuinely useful. It is also a workflow watching workflows inside the system that is failing, on data that disappears in fourteen days, and it still cannot see a run that never started.

## What the automation actually has to do

As a Dugong playbook, in plain prose:

```
# trigger
Every hour, plus a daily
digest and a check after
every workflow edit

# steps
1. List every automation and
   the outcome it is
   supposed to produce
2. Baseline each one: how
   often it should fire and
   how fast
3. Check the outcome in the
   store data, not the run
   log
4. Alarm on silence too, not
   just on errors: zero runs
   is a result
5. Copy run evidence out
   before day fourteen
   deletes it
6. Re-verify after every
   edit, app update and
   platform release
7. Open one incident per
   automation and keep it
   open until it clears
```

Step one is the part most teams have never done. Nobody has a list of what the store automates. There is Flow, there are the marketing automations, there are three apps with rules inside them, and there is the thing a contractor built in 2024. The inventory is the foundation, and the sentence next to each entry matters more than the workflow diagram: what should be true in the world if this is working.

Step two is what makes silence legible. A workflow that normally runs two hundred times a day and ran zero times today is a louder signal than any error message, but only if something remembers what two hundred looks like.

Step four is the one that catches the expensive failure. Errors are easy and absence is hard, so most monitoring never does it. Absence is where the VIP tag went.

Step five is cheap insurance. Pull the run list every day, keep it somewhere of your own, and you own a history rather than renting a two week window. The first time somebody asks how long has this been broken, that archive answers in seconds instead of never.

Step seven is the correction to the once per thirty days design. The right behavior is not more email. It is one open incident per broken automation, which stays open, updates itself with a count, and closes when the outcome starts arriving again. You want to be told once and reminded until it is fixed, which is the opposite of being told once and never again.

## Why this is a compiler problem, not an app problem

You could build most of this by hand. A scheduled job, a few Admin API queries, a table of expected rates and an alerting rule. Teams with an engineer do exactly that and it works.

What breaks it is that the expectations change every week. You launch a product and the tagging rule needs a new threshold. You add a market and the fulfillment routing splits in two. A promotion doubles the run rate for four days and every baseline alarms at once. Each of those is a ten minute edit to a hand built monitor and nobody has the ten minutes, so the monitor drifts out of date and starts crying wolf, and within a quarter people are filtering its email.

The version that survives is one where the expectation is written the way you would say it to a colleague. Every order over two hundred dollars should leave the customer tagged VIP within five minutes. Every return marked received should put stock back within the hour. Every unpaid draft older than seven days should have had a reminder sent. Those sentences are the monitor. Changing the rule means changing the sentence, which is a thing you will actually do, and an automation like Dugong can hold them, check them against the store on a schedule, and tell you which promise stopped being kept and when it stopped.

The honest limits. This does not stop a workflow breaking, it shortens the distance between breaking and knowing, from weeks to about an hour. It cannot audit what you never wrote down, so an automation missing from the inventory is still invisible. And a store in the middle of a genuine anomaly, a sale or an outage, will generate noise unless somebody tells it that this week is not normal.

## The workflow worth building this week

Pick the three automations whose failure would cost you the most. For most stores that is the fulfillment handoff, the inventory sync and whatever touches money. Write one sentence each describing what should be true when they work. Check those three sentences against the store every hour, alarm on zero as loudly as on error, and archive the run list daily so day fifteen still has a memory.

That is an afternoon of work and it converts your automation stack from something you hope is running into something you can see. The rest is refinement. But you stop learning about broken workflows from customers, and the run list goes back to being a debugging tool instead of a fire alarm that mostly does not ring.

> **◆ READING** Two companion pieces if this one landed: [the supplier feed that zeroed your catalog](https://blog.dugong.live/how-to-sync-supplier-inventory-feeds-to-shopify.html), on an automation that worked exactly as written and was still a disaster, and [the stock count that changes overnight](https://blog.dugong.live/how-to-stop-your-shopify-inventory-changing-by-itself.html), on finding out which of your integrations moved a number nobody asked it to move.

If you are a Shopify merchant with a silent automation story, the workflow that had not fired since March, the run list that said Completed while nothing happened, the customer who told you before your tooling did, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Why does Shopify Flow say Completed when my workflow did not work?

Because Completed is not a success signal. Shopify's documentation defines the run statuses as In progress, meaning currently executing or retrying, Waiting, meaning a wait step has delayed a workflow, Rate limited, meaning the workflow was using too many resources so Flow limited the execution, Canceled, and Completed, which is defined as done. A run reaches Completed when it stops, whatever the individual actions did on the way. A developer established this in public on January 2, 2026 after an HTTP request failed inside a loop while the run reported success: I am not sure why the Run status shows as Completed when one action had an error. Shopify staff confirmed it and explained the mechanism, that a fail stops execution for that path, which is usually the same as the workflow, but a workflow with parallel actions and loops has many paths, so one dead branch does not mark the run. Practical consequence: filter the run list on Errors, which is a separate facet from status, and never treat Completed as evidence that anything happened.

Permalink: https://blog.dugong.live/how-to-catch-shopify-flow-workflows-that-fail-silently.html#faq-1

### How do I get notified when a Shopify Flow workflow fails?

There is a built-in trigger called Workflow error occurred, described as starting a workflow when workflows fail during execution. You pair it with an email or Slack action and you have a monitor. The limit is the problem. It fires once per workflow version within a thirty day period, however many times the workflow fails, and the counter resets only when you edit the workflow, which creates a new version, or when thirty days pass. Shopify states the intent plainly: error notifications are designed to limit noise, so you will only get one notification per workflow version. On a store doing four hundred orders a day, a workflow that breaks on the first of the month sends one email and then fails silently for twenty nine days. It is also blind to the two failures that are not errors, a run that completes with a dead branch inside it and a workflow that stops firing altogether.

Permalink: https://blog.dugong.live/how-to-catch-shopify-flow-workflows-that-fail-silently.html#faq-2

### How long does Shopify Flow keep workflow run history?

Fourteen days. Shopify's monitoring documentation states that workflow runs are stored for 14 days after a run has completed, and that after 14 days, the run is removed from the system. The run search carries the same ceiling: the search is limited to the last 14 days of workflow runs. This matters because fourteen days is shorter than most of the loops that actually surface these failures. A monthly reconciliation finds the problem on day thirty, a quarterly audit on day ninety, and a customer whenever the customer happens to notice. By the time anyone asks how long this has been wrong, the runs that would answer have been deleted. The cheap fix is to export the run list on a schedule and keep a copy of your own, so day fifteen still has a memory.

Permalink: https://blog.dugong.live/how-to-catch-shopify-flow-workflows-that-fail-silently.html#faq-3

### How do I tell if a Shopify Flow workflow has stopped running entirely?

Not from the run list, which is the whole difficulty. When a workflow stops firing, because a trigger tag was renamed, an app supplying the trigger was uninstalled or changed scopes, a condition stopped matching, or somebody deactivated it during a busy week, there is no failed run to find. There is no run. An empty list looks identical to a quiet week, so you cannot detect a missing run by watching runs. The only reliable detection is to watch the outcome instead: baseline how often each automation should fire and what it should leave behind in your store data, then alarm when that number goes to zero. A workflow that normally runs two hundred times a day and ran zero times today is a louder signal than any error message, but only if something remembers what two hundred looks like.

Permalink: https://blog.dugong.live/how-to-catch-shopify-flow-workflows-that-fail-silently.html#faq-4

### Can AI monitor Shopify automations for silent failures?

Yes, and the reason it fits is that the hard part is expressing and re-checking expectations rather than reading logs. Every automation is really a promise about the world: every order over two hundred dollars leaves the customer tagged VIP within five minutes, every return marked received puts stock back within the hour, every unpaid draft older than seven days has had a reminder sent. Those sentences are checkable against store data directly, which catches all five failure modes at once, the completed run with a dead branch, the suppressed alert, the expired evidence, the workflow that never fired, and the platform change under a workflow you never edited. An automation like Dugong holds those sentences in plain language, checks them against the store hourly, archives run evidence before the fourteen day window closes, re-verifies after every edit and app update, and keeps one open incident per broken automation instead of one email per month. The honest limits: it does not stop a workflow breaking, it shortens the gap between breaking and knowing; it cannot audit an automation nobody wrote down; and during a genuine anomaly such as a flash sale it will need to be told that this week is not normal.

Permalink: https://blog.dugong.live/how-to-catch-shopify-flow-workflows-that-fail-silently.html#faq-5

---

Markdown rendition of https://blog.dugong.live/how-to-catch-shopify-flow-workflows-that-fail-silently.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
