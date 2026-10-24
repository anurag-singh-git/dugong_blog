# How to automatically approve wholesale customers on Shopify

> Shopify makes wholesale approval a manual chore: the B2B login has no signup, and Forms builds a queue nobody vets. The AI playbook that answers in minutes.

- Canonical: https://blog.dugong.live/how-to-automatically-approve-wholesale-customers-on-shopify.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-07-30
- Updated: 2026-10-24
- Section: Research
- Word count: 2500
- Dispatch: Nº 95 · Research · 9 min read
- Full headline on page: How to automatically approve wholesale customers *on Shopify*
- Keywords: Shopify wholesale customer approval, Shopify B2B account approval, approve wholesale applications Shopify, Shopify company account requests, Shopify Forms wholesale lead capture, restrict access to B2B customers only, Shopify B2B login no registration form, auto approve B2B customers Shopify
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

A boutique owner in Columbus finds your line at a trade show on a Friday afternoon. That evening she fills out the wholesale application on your site: store name, website, resale certificate number, the volume she has in mind. It takes her four minutes. Then nothing happens, because the form posted into a queue that nobody looks at until Monday.

She did not spend the weekend waiting. She applied to three brands that afternoon, the way wholesale buyers always do, and one of them wrote back the same evening with a login and a price list. Her opening budget landed there on Saturday morning. When your approval email finally goes out on Tuesday, it reads less like a welcome and more like an apology.

Nothing in that story involves a difficult decision. Her shop is real, her certificate checks out, her website matches her email domain. Any person who looked at the application for ninety seconds would have said yes. The problem is that on Shopify, a person looking at it for ninety seconds is the entire system.

## The short answer

Shopify will collect the application and queue it; it will not read it. On Plus, company account requests let a prospect apply through a Shopify Forms form, and the submission creates the company, its location and a customer record automatically, with the raw entry kept as a metaobject and an approve or decline button on the queue. If you are still routing applications into a shared inbox, switch today.

Nothing on the way to that button verifies anything. The tax ID is a text field and so is the website. Shopify does not check that the email domain matches the site, that the site exists, that the certificate number has the right shape for its state, or that the applicant is one of your own retail customers after a trade discount. Every application waits for the same human read, from the obvious yes to the obvious scam.

That read is what to automate, because the cost of the queue is counted in hours rather than mistakes: a buyer applies to three brands on a Friday and spends her opening budget wherever the login arrives first. Verify what can be verified the moment the form posts, domain against site, site live and retailing, tax ID shaped correctly for its state, check it against your own records for past applications and territory overlap, and sort into approve, decline and human review with the evidence *attached*.

## What Shopify actually gives you

Credit first, because the intake half of this got meaningfully better. On Shopify Plus, the B2B feature set is real: companies with locations, catalogs with their own price lists, payment terms, and buyers who log in and order against all of it. And since Shopify added company account requests, a prospect can apply through a Shopify Forms form on your storefront, and the submission automatically creates the company, a company location, and a customer record in your admin. The requests line up in a review queue, the raw submissions are kept as [metaobject](https://help.shopify.com/en/manual/custom-data/metaobjects) entries, and you approve or decline each one with a click. If you are on Plus and still routing applications through a contact form into a shared inbox, switch today. That part costs nothing.

Now look closely at what the click does not do. Nothing on the way to the approve button verifies anything. The tax ID is a text field. The website is a text field. Shopify does not check that the email domain matches the site, that the site exists, that the certificate number has the right shape for its state, or that the applicant is not one of your own retail customers fishing for forty percent off. Every application, from the obvious yes to the obvious scam, waits for the same human read. Shopify built the queue and left the judgment out.

> Shopify will collect the wholesale application for you. It will not read it.

## The login page with no door

It gets stranger on stores that are wholesale only. Shopify offers a setting called **Restrict access to B2B customers only**, and switching it on replaces your storefront with a Shopify hosted login screen containing exactly one field: an email box for customers who already exist. No registration form. No application link. No way for a new buyer to ask to become a customer. A merchant opened a community thread about it titled, in full, *Massive Oversight - Account registration/approval form feature missing on B2B login screen*, and another titled *New B2B Site - No Way To Approve Wholesale Applications*. The replies are merchants comparing workarounds, because there is no setting to compare.

The obvious move, switching the restriction off, opens a different hole. With the restriction off, the login box happily creates a customer record for any email address that asks for a six digit code. Anyone who finds the URL can make an account. Merchants testing exactly this setup reported retail shoppers wandering into a wholesale-only store and placing orders at whatever prices were exposed. So the toggle offers a choice between a door with no handle and no door at all.

You cannot patch it yourself, either. The new [customer accounts](https://help.shopify.com/en/manual/customers/customer-accounts) that B2B requires are hosted by Shopify and accept no [Liquid](https://shopify.dev/docs/api/liquid) customization and no app embeds on the login screen, so there is no hook where an approval step could be built. And on non-Plus plans the situation is simpler and worse: there are no companies, no catalogs, and no native concept of wholesale at all, so approval means a form app, a `wholesale` tag applied by hand, and a gating app that hides prices from everyone without the tag. Three apps, stitched together, to represent one sentence: this buyer is allowed to see trade prices.

## What approving actually involves

The click is called approval, but the work around it is vetting, and vetting is specific. Is the business real: does the certificate match the business name, does the email domain match the website, does the website actually sell to consumers or is it a parked domain registered on Tuesday. Does the buyer fit: is the volume plausible, is their city already covered by a stockist you promised a territory to, is the applicant a competitor whose team wants your price list. Have you met them before: an existing retail profile with three returns and a chargeback, or [the same person under a second email](https://blog.dugong.live/how-to-merge-duplicate-customer-profiles-on-shopify.html) after you declined them in March. None of this is deep detective work. All of it is twenty tabs per application, which is why it happens in batches, late.

And a yes is not the end of the job. The moment you approve, the account needs its catalog and price list, its payment terms, its tax exemption if the certificate supports one, and a welcome email that says the door is open. Miss the catalog assignment and your new buyer logs in to retail prices and emails you, politely confused. Miss the tax setup and her first invoice is wrong, which on net terms you may not notice until [the invoice conversation](https://blog.dugong.live/how-to-automatically-send-invoices-on-shopify.html) happens a month later. Approval is not a decision with a click attached. It is a decision with provisioning attached, and Shopify only automates the part between them, which is the part that was already easy.

> **◆ NOTE** The trap is **treating approval as a yes/no click** rather than the middle of a workflow. The click takes one second. The vetting before it and the provisioning after it are the actual work, and because neither is automated, the click gets batched into Monday, and the weekend applicant becomes another brand's account.

## Why the manual version fails quietly

At two applications a week, reading them by hand is correct, and you should not automate it. The failure arrives with volume and with timing. Wholesale interest is spiky: a trade show, a press mention, a TikTok from a store that stocks you, and the queue goes from two a week to nine on a Friday. The nine arrive exactly when nobody has time to open twenty tabs each, so they wait. Shopify keeps no clock on any of this. There is no report for time from application to answer, which is the only number that predicts whether the account ever places its first order.

The decline side rots even more quietly. Most stores never send declines at all, because writing a rejection to a stranger is the easiest task in the world to skip. So the fake applications sit in the queue next to the real ones, the retail discount hunters are never told no, and six months later the queue is a mix of ghosts and [people you have already decided against](https://blog.dugong.live/how-to-block-a-customer-on-shopify.html) who keep reapplying because nobody ever answered.

## What the automation actually has to do

The working version is not a faster click. It is the read a good sales ops person does with each application, done the moment the form is submitted. As a Dugong playbook, in plain prose:

```
# trigger
On wholesale application submitted, from any form

# steps
1. Read the application: business name, tax ID,
   website, channel, requested volume
2. Verify what can be verified: email domain
   matches the site, the site is live and retails,
   the tax ID has the right shape
3. Check your own records: past applications,
   retail history, territory overlap, competitors
4. Sort into three bins: approve, decline,
   human review with the evidence attached
5. Provision on approval: catalog, price list,
   payment terms, tax status, in the same pass
6. Answer the same day, yes or no, while the
   applicant still remembers your brand
7. Nudge approved accounts with no first order
   after two weeks
```

Steps two and three are where a rules engine gives out. A rule can require that the tax ID field is not empty. It cannot notice that the ID belongs to a nail salon while the application claims a gift shop, or that the website is a template with placeholder text, or that the applicant's domain belongs to the brand two booths down from you at the last show. That is reading, not filtering, and it is the same species of judgment as [deciding what a high risk flag actually means](https://blog.dugong.live/how-to-handle-high-risk-orders-on-shopify.html): context against context, not field against threshold.

Step four matters because the honest answer for some applications is a human look, and the automation's job there is to shrink the work, not to pretend confidence. A review item should arrive as one message: the application, what checked out, what did not, and what looks odd, so the human decision takes the ninety seconds it always deserved instead of twenty tabs.

Step five is the half that saves your reputation with the buyers you say yes to. Catalog, terms, and tax status assigned at the moment of approval means the welcome email and the working login arrive together. The buyer's first experience of your brand as a partner is the same hour she was approved, which is exactly the experience the brand that beat you to her order was selling.

## Why this is a compiler problem, not an app problem

There are approval apps, and on non-Plus stores one of them is probably in your stack already. They all share a shape: they gate, but they do not judge. The app can hold every account until you click, which moves the queue from your inbox into its dashboard and changes nothing about the work. The policy you actually run is not a gate. It is a paragraph: boutiques in regions we do not cover get approved at trade terms if the certificate and site check out, known stockist territories get flagged for the rep who owns them, pure marketplaces get declined politely, competitors get declined impolitely, and anything strange gets a human. That paragraph changes with your seasons and your stockist map. An app cannot hold it. A compiler that turns the paragraph into the running workflow can, which is the same argument behind [the automations no one builds](https://blog.dugong.live/best-shopify-automations-to-set-up.html): the valuable workflow is the one shaped like your business, not like a settings page.

Picture a ceramics brand doing thirty applications a month after a good press cycle. Nineteen are boutiques that check out end to end: approved within the hour, catalog and net 30 assigned, welcome sent, no human involved. Four are marketplaces and dropshippers the brand never sells to: declined the same day, kindly. Two are existing retail customers asking for wholesale pricing on personal volume: declined with a link to [the volume discount tier](https://blog.dugong.live/how-to-set-up-tiered-volume-discounts-on-shopify.html) that actually fits them. One is an application whose email domain matches a competitor: declined, and noted. And four genuinely need eyes: a boutique two towns from an existing stockist, an overseas buyer with an unfamiliar tax format. Those four arrive in the founder's inbox as four short briefs, and the whole month of wholesale admissions took her twenty minutes.

## The workflow worth building this week

Start with the number you do not have: time to answer. Pull your last twenty applications, wherever they live, and write down the gap between submitted and answered, counting never as infinity. Most stores find a median measured in days and a tail measured in silence. That is the number the automation exists to move, and it is worth knowing before and after.

Then automate the reading before you automate the deciding. A workflow that meets every application with the checks already run, domain, site, tax ID shape, history, territory, and posts the result where you already work captures most of the value with none of the risk, because the click is still yours. Once you notice that you have agreed with the workup fifty times in a row, let it carry the clear cases end to end and keep the ambiguous ones. That is the same trust curve you would run with [a floor on your checkout](https://blog.dugong.live/how-to-set-a-minimum-order-amount-on-shopify.html) or any other guardrail: watch it, then let it work.

Describe it the way you would brief a new sales ops hire on their first morning. When a wholesale application comes in, check the certificate, the site, and the domain, see if we know them, and make sure they do not step on an existing stockist. Approve the clear yeses with the right catalog and terms and welcome them the same day. Decline the marketplaces and the discount hunters, politely, the same day. Bring me anything strange with your notes attached. And if someone we approved has not ordered in two weeks, check in. That is the brief. The compiler handles the fields, the lookups, the provisioning, and the timing, and the boutique who applies on Friday evening gets her price list while her budget is still yours to win.

> **◆ READING** Two companion pieces if this one landed: [the repeat customer your store treats like a stranger](https://blog.dugong.live/how-to-segment-repeat-customers-on-shopify.html), on why customer records need judgment and not just tags, and [the invoice you send by hand](https://blog.dugong.live/how-to-automatically-send-invoices-on-shopify.html), which is where every approved wholesale account sends you next.

If you are a Shopify merchant with a wholesale queue that gets answered in batches, a B2B login page your prospects bounce off, or a stack of three apps pretending to be an approval flow, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Can Shopify automatically approve wholesale account requests?

No. On Shopify Plus, a company account request submitted through Shopify Forms automatically creates the company, a company location, and a customer record, which is real work saved. The approval itself is a manual click in the admin, and nothing on the way to that click verifies anything: the tax ID is not checked, the website is not read, and a competitor or a retail shopper applying for a discount looks identical to a legitimate boutique. Shopify Flow can notify you that a request arrived and can apply tags, but it cannot read a website or judge an application. Third party registration apps add approval gates and custom fields on non-Plus stores, and they still leave the reading, the vetting, and the post-approval setup of catalogs, payment terms, and tax exemptions to a person.

Permalink: https://blog.dugong.live/how-to-automatically-approve-wholesale-customers-on-shopify.html#faq-1

### How do new wholesale customers apply if my store is restricted to B2B customers only?

From the login page, they cannot. When Restrict access to B2B customers only is switched on, visitors are redirected to a Shopify hosted login screen that contains a single email field and no registration form, no application link, and no way to request access. Merchants have been asking for a signup path on that screen in community threads with titles like Massive Oversight and No Way To Approve Wholesale Applications. Switching the restriction off has its own cost: the login box will create a customer record for any email address that requests a six digit code, and merchants testing this reported unwanted retail customers placing orders on a wholesale-only store. The workable pattern is a public application page that collects the details you need, with approval and access granted behind it, which is exactly the step worth automating.

Permalink: https://blog.dugong.live/how-to-automatically-approve-wholesale-customers-on-shopify.html#faq-2

### What should I check before approving a wholesale application?

Five things cover most of it. Whether the business is real: a resale certificate or tax ID that matches the business name, and an email domain that matches the website on the form. Whether the applicant actually retails: a live site or storefront that sells to end customers, not a parked domain or a free email address with no trace. Whether they fit your channel: order volume they are asking for, territory overlap with existing stockists, and whether the applicant is a competitor looking at your price list. Whether they already exist in your store: a retail profile with discount-hunting history, or a previously declined application under another email. And what happens after yes: the catalog and price list they should see, payment terms, and tax exemption status all need to be assigned at approval, because an approved buyer who logs in to retail prices emails you within the hour.

Permalink: https://blog.dugong.live/how-to-automatically-approve-wholesale-customers-on-shopify.html#faq-3

### How quickly should wholesale applications be answered?

The same day, because approval is a race you cannot see. A buyer who finds you at a trade show applies to three brands the same afternoon, and the one that writes back that evening with a login and a price list takes her opening order on Saturday; the approval that goes out Tuesday reads less like a welcome and more like an apology. Shopify keeps no clock on any of this: there is no report for time from application to answer, which is the only number that predicts whether an account ever places its first order. Measure it yourself: pull the last twenty applications, write down the gap between submitted and answered, and count never as infinity. Most stores find a median measured in days and a tail measured in silence, and wholesale interest is spiky, two a week becoming nine on the Friday of a show.

Permalink: https://blog.dugong.live/how-to-automatically-approve-wholesale-customers-on-shopify.html#faq-4

### Should I send decline emails to wholesale applicants?

Yes, the same day, kindly, because silence is the expensive option. The decline side of a wholesale queue rots quietly: writing a rejection to a stranger is the easiest task in the world to skip, so the fake applications sit next to the real ones, the retail discount hunters are never told no, and six months later the queue is a mix of ghosts and people you already decided against who keep reapplying because nobody ever answered. The sort that works in practice: marketplaces and dropshippers you never sell to get a polite decline the day they apply, existing retail customers asking for trade prices on personal volume get pointed at the volume discount tier that actually fits them, and the application whose email domain matches a competitor gets declined and noted. Every answered application closes a loop that silence leaves open.

Permalink: https://blog.dugong.live/how-to-automatically-approve-wholesale-customers-on-shopify.html#faq-5

---

Markdown rendition of https://blog.dugong.live/how-to-automatically-approve-wholesale-customers-on-shopify.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
