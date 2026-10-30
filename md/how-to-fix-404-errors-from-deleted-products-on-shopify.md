# How to fix 404 errors from deleted products on Shopify

> Delete a product on Shopify and its old URL just 404s, with no redirect. The AI playbook that catches every dead link and sends it to the right live page.

- Canonical: https://blog.dugong.live/how-to-fix-404-errors-from-deleted-products-on-shopify.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-06-25
- Updated: 2026-10-27
- Section: Research
- Word count: 2391
- Dispatch: Nº 68 · Research · 9 min read
- Full headline on page: How to fix *404 errors* from deleted products on Shopify
- Keywords: Shopify deleted product 404, redirect deleted product Shopify, Shopify 404 errors SEO, Shopify broken links, automatically redirect deleted product, bulk URL redirect Shopify, 301 redirect Shopify, product URL handle changed 404, soft 404
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

Every catalog sheds products. A line gets discontinued, a seasonal item ends, a supplier drops out, a duplicate listing gets cleaned up. So you open the product, hit delete, and move on. What you do not see is that the URL that product lived at does not disappear with it. It stays in Google's index for weeks. It stays in the backlinks other sites built to it. It stays in your own internal links, in old newsletters, in the Google Shopping feed, in a paid ad still running. And now every one of those points at a page that returns a 404. Shopify deleted the product and left the address pointing at nothing.

This is one of the most repeated SEO complaints in the merchant communities, and it always arrives the same way: someone notices a wall of 404s in their analytics or Search Console, traces them back to products they deleted or handles they changed, and asks how to make Shopify redirect them automatically. The early answers are a version of "it does not, you have to build the redirects yourself, or get an app." The merchant is not asking for anything fancy. They want the obvious thing a store that constantly adds and removes products needs: when a URL stops working, send the visitor to the closest page that does. The platform running their entire storefront has no built-in way to do it.

> The product is gone. The link to it is not, and Shopify *will not point it anywhere* on its own.

## The short answer

Deleting a Shopify product creates no redirect. Its URL simply begins returning a 404, with no prompt at delete time asking where the traffic should go and no default forward behind it. The same quiet break follows a handle change, which rewrites the URL and orphans the old one, and an unpublish rather than a delete.

The native repair is manual and one URL at a time, under Online Store, then Navigation, then URL Redirects. A CSV bulk import exists, and you still have to know every broken URL and settle on every destination before that file can be built. Flow can react to a product being deleted and has no action that creates a redirect.

Pointing every dead URL at the homepage is the tempting shortcut and a trap, because a search engine reads it as a soft 404 once the destination has nothing to do with what was requested. The equity the old page earned drains away regardless and the customer starts over, so the target has to be *genuinely relevant* and has to stay live.

## Why a 404 from a deleted product costs you a real sale

A 404 is not a neutral event. The page you deleted had spent months earning things you cannot see at a glance: a position in search, a set of backlinks, a place in your internal linking, a row in your product feed. That accumulated value, the link equity, only passes forward if the old URL points at a live page. When it 404s instead, the value drains. Search engines eventually drop the dead URL, the backlinks now lead to an error, and the ranking you built is simply gone rather than handed to a replacement.

The more immediate cost is the customer standing on the dead page right now. They clicked a real link, from a search result, an old email, a friend's recommendation, a paid ad you are still paying for, and they landed on "page not found." They do not patiently go hunting through your menu for the new thing. They hit back and they are gone, and if the click came from an ad, you paid for the privilege of bouncing them. On a store that churns through products, this is not one stray error. It is a steady trickle of paid and earned traffic poured onto pages that no longer exist.

## What Shopify actually does, and where it stops

Shopify is happy to let you delete a product, change a handle, or unpublish a page. What it does not do is manage the wreckage those actions leave in the URL space. The gap is the whole cleanup: noticing a URL just broke, deciding where it should now go, and writing the redirect. It shows up in three places merchants hit fast.

First, **deleting a product creates no redirect**. The old URL just starts returning a 404. There is no prompt at delete time asking where to send the traffic, no default forward, nothing. The same silent break happens when you change a product's handle, which rewrites its URL and orphans the old one, and when you unpublish rather than delete. In every case the previous address dies quietly and you only find out later, if you go looking in Search Console.

Second, **the native fix is manual, one URL at a time**. Shopify does let you create a URL redirect, under Online Store, then Navigation, then URL Redirects. You type the old path, you type the new one, you save, and you repeat for the next dead URL. There is a CSV bulk import for doing many at once, but you still have to know every broken URL and decide every destination before you can build the file. Either way the thinking and the typing are entirely on you.

Third, **Flow cannot create a redirect**. [Shopify Flow](https://help.shopify.com/en/manual/shopify-flow), free on every plan, can react to a product being deleted and can send you an internal note about it. But Flow has no action that creates a URL redirect, so the one step that actually fixes the 404 is the step it cannot take. You can automate the alert that a product was deleted. You cannot automate the redirect that keeps its URL alive.

> **◆ DATA** The tempting shortcut is to point every dead URL at the homepage in one blanket rule. Search engines treat that as a **soft 404**, because the destination has nothing to do with the page that was requested, so you lose the link equity anyway and you dump the customer somewhere they then have to start their search over. A redirect only does its job when the target is genuinely relevant: the replacement product, the same collection, the nearest alternative. The homepage is the fallback of last resort, not the plan.

## Why the usual fixes don't hold

Once the 404s start showing up, merchants reach for one of a few workarounds. Each gets you partway and each breaks in a familiar spot.

**"I will redirect everything to the homepage."** Fast, and it does technically stop the 404. But it is the soft-404 trap: the value of the old page evaporates because the homepage is not a real answer to what was requested, and the customer who wanted a specific product now faces your whole catalog with no idea where the thing went. You have swapped a dead end for a shrug.

**"I will set up the redirect by hand whenever I delete something."** A fine intention that survives until the first busy week. The discipline slips, the bulk catalog cleanup happens in one sitting with no redirects attached, and worse, the silent breaks, the handle you tidied, the product you unpublished, never even feel like deletions, so they never trigger the habit. The 404s accumulate in the background while you believe you are keeping up.

**"I will install a redirect app."** There are good ones, and for many stores they are a fair answer, which by itself proves the native gap is real. But most work by logging the 404 after a visitor has already hit it, then surfacing it for you to fix, or by offering a blanket rule that forwards by pattern. The detection is genuinely useful. The judgment it still leaves to you: which live page each specific broken URL should actually point at, so the redirect is relevant rather than just present.

## What the automation actually has to do

The real job is not "redirect deleted products to the homepage." It is "for each URL that a delete, an unpublish, or a handle change just broke, find the closest live page based on what that product actually was, write a permanent redirect to it, and keep that redirect honest as the catalog keeps moving, while holding the high-value URLs for a human to confirm." That is watching, reading, and matching, run per URL across everything that changes. As a Dugong playbook, in plain prose, it reads like this:

```
# trigger
On a product deleted, unpublished, or its handle changed

# steps
1. Catch the URL that is about to stop working before it
   goes cold
2. Read what the page was: product type, collections,
   tags, and title
3. Find the closest live page: a replacement product,
   the same collection, or the nearest alternative
4. Write a 301 redirect from the broken URL to that page
5. Recheck later that the target is still live and in
   stock, and repoint it if it is not
6. Hold URLs with real traffic, rankings, or backlinks
   for a human to confirm the destination
7. Log every broken URL, the chosen target, and why
```

Seven lines. The compiler fills in everything beneath: watching for the delete, the unpublish, and the quiet handle change alike, reading the product so the match is based on what the page was about, choosing a destination that a customer would actually accept as the next best thing, writing the permanent redirect, then circling back so the redirect never chains into a fresh dead end when the target itself sells out or gets removed. The merchant never sat in Search Console exporting a list of 404s on a Friday. They described how a careful shop owner would handle a discontinued product, and let the compiler do the volume and keep the map current.

> **◆ NOTE** The redirect that does damage is the lazy one. Forwarding a deleted product **to a page that does not match it** looks tidy in your redirect list and still loses you the ranking and the customer, because relevance is the entire point of a redirect. And a redirect that points at another product you later delete just moves the dead end down the road. The job is not "make the 404 go away," it is "send this specific visitor and this specific link equity to the live page that best answers what they came for, and keep it that way."

## Why this is a compiler problem, not an app problem

There are capable redirect apps, and for many stores they are a fine answer. But the thing that makes a redirect worth anything is not catching the 404, it is the choice of where to send it: reading what the deleted product was, knowing whether a real replacement exists or only a loose cousin, deciding when the collection is the better target than any single product, and noticing when the destination you picked last month has since gone out of stock. Those are judgments about a particular URL, weighed together, and the right answer changes with every product, which means the work is never set-and-forget. It is decided fresh each time.

A natural-language compiler fits because broken-URL cleanup was never really a redirect-button problem. It is a *matching and judgment* problem wearing a redirect button's clothes. Firing a blanket forward to the homepage is the easy part, which is why the shortcuts do it. The hard part is everything around it: read the page that died, find the closest living one, write the 301, keep it pointed at something real, and pull a human in on the URLs that carry real weight. You can write that brief in a paragraph. You could never hold it in your head across every product you removed this quarter. It sits in the same family as [the meta description you write one at a time](https://blog.dugong.live/how-to-bulk-edit-meta-descriptions-on-shopify.html), where the SEO field Shopify stores but will not fill has to be written page by page, and [the image alt text no one writes](https://blog.dugong.live/how-to-add-alt-text-to-shopify-product-images-in-bulk.html), where the same blank-field-times-the-whole-catalog problem quietly costs you search visibility.

## The workflow worth building this week

If your catalog turns over at all, if you discontinue lines, run seasonal products, clean up duplicates, or rename handles, this is the automation to set up before your next round of deletions, because every product you remove without a redirect is a link you used to own pointing at a dead page, and the only thing between you and a clean URL space is a cleanup you keep not getting to. It pairs naturally with the merchandising work we have written about, like [the sold-out products that sink your collection](https://blog.dugong.live/how-to-push-sold-out-products-to-the-bottom-of-a-shopify-collection.html), where what happens to a product as its status changes decides how the storefront performs, and it feeds the same flywheel as [the Shopify automations no one builds](https://blog.dugong.live/best-shopify-automations-to-set-up.html), where the work that compounds is the part merchants never get to.

Describe it the way you would brief a careful shop owner: whenever a product gets deleted, unpublished, or renamed, do not leave its old link pointing at nothing, send it to the closest thing we still sell, keep that redirect aimed at something live, and bring me the few pages that actually matter before you touch them. That is the whole brief. The compiler does the watching, the matching, the writing, and the upkeep. You keep your attention for the products that matter, and you stop quietly bouncing paying customers and hard-won rankings off pages that no longer exist.

> **◆ READING** If this resonates, two companion pieces: our dispatch on [the meta description you write one at a time](https://blog.dugong.live/how-to-bulk-edit-meta-descriptions-on-shopify.html), where the SEO field Shopify stores but will not write has to be filled page by page, and the field study on [the Shopify automations no one builds](https://blog.dugong.live/best-shopify-automations-to-set-up.html), where the work that actually compounds is a sliver of what merchants wire up.

If you are a Shopify merchant who has wired up an auto-redirect that picks a relevant target instead of dumping everything on the homepage, or you have a story about the day you found a thousand 404s from a catalog cleanup six months earlier, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Does Shopify automatically redirect a deleted product?

No. When you delete a product, Shopify does not create a redirect for its URL. The old address simply returns a 404 page not found. The same thing happens quietly when you change a product handle or unpublish a product: the previous URL breaks and nothing forwards it. To stop the 404 you have to create a URL redirect yourself, in Online Store then Navigation then URL Redirects, one entry at a time, or assemble a CSV and bulk import it. Shopify Flow, the free automation tool, has no action that creates a redirect, so it cannot do this for you either.

Permalink: https://blog.dugong.live/how-to-fix-404-errors-from-deleted-products-on-shopify.html#faq-1

### Do 404 errors from deleted products hurt your SEO?

They cost you the value the page had already earned. A product that ranked, collected backlinks, and sat in your internal links carries link equity, and when its URL 404s that equity drains away instead of passing to a live page. Search engines eventually drop the dead URL from the index, every backlink pointing at it now points at nothing, and any paid or social traffic still aimed at the old link lands on an error and bounces. A handful of 404s will not sink a store, but a catalog that churns products and changes handles without redirects leaks ranking and traffic continuously, and the leak is invisible until you go looking for it.

Permalink: https://blog.dugong.live/how-to-fix-404-errors-from-deleted-products-on-shopify.html#faq-2

### Should you redirect deleted Shopify products to the homepage?

Only as a last resort. Redirecting a deleted product to the most relevant live page, a replacement product, the same collection, or the closest alternative, keeps both the customer and the link value on a page that matches what they wanted. Sending every dead URL to the homepage instead is treated by search engines as a soft 404, because the destination has nothing to do with the original page, so you lose the link equity anyway and you drop the customer somewhere they then have to search from scratch. The right move is a relevant 301 per URL, with the homepage used only when genuinely nothing else fits.

Permalink: https://blog.dugong.live/how-to-fix-404-errors-from-deleted-products-on-shopify.html#faq-3

### Can Shopify Flow create a redirect when a product is deleted?

No. Flow, which is free on every plan, can react to a product being deleted and can send you an internal notification about it, but it has no action that creates a URL redirect, so the one step that actually fixes the 404 is the step it cannot take. That gap defines the workarounds. Notification-only setups still depend on a human remembering to add the redirect in the admin. Most redirect apps log a 404 after a visitor has already hit it, or apply blanket pattern rules. And sending everything to the homepage trades a 404 for a soft 404, which throws away the link equity anyway. The working shape is an automation that catches the deletion, unpublish, or handle change in the moment, reads what the page was, chooses the closest live target, writes the 301 itself, and holds only the URLs with real traffic or backlinks for a human to confirm.

Permalink: https://blog.dugong.live/how-to-fix-404-errors-from-deleted-products-on-shopify.html#faq-4

### How do I find the 404 errors already piling up on my Shopify store?

Search Console is the honest mirror: its not found report lists the URLs Google is still trying to reach, and the deleted products and renamed handles are usually recognizable straight from the paths. Your analytics show the same dead ends arriving as landing pages that bounce immediately, and redirect apps keep hit logs of 404s as visitors trip them. Two habits make the list useful instead of depressing. First, triage by weight: a URL with rankings, backlinks, or steady traffic deserves a hand-picked destination, while long-tail strays can take a rule-based target. Second, treat the backlog as a symptom. Every URL on that list went dark at a specific moment, a deletion, an unpublish, a handle edit, so pair the cleanup with an automation that catches those moments and writes the 301 before the next wall of 404s accumulates.

Permalink: https://blog.dugong.live/how-to-fix-404-errors-from-deleted-products-on-shopify.html#faq-5

---

Markdown rendition of https://blog.dugong.live/how-to-fix-404-errors-from-deleted-products-on-shopify.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
