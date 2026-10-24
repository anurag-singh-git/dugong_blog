# How to add alt text to Shopify product images in bulk

> Shopify never writes image alt text and has no bulk way to add it, so it sits blank across your catalog. The AI playbook that reads each photo and writes it.

- Canonical: https://blog.dugong.live/how-to-add-alt-text-to-shopify-product-images-in-bulk.html
- Author: Priya Singh (https://blog.dugong.live/priya-singh.html)
- Published: 2026-06-20
- Updated: 2026-08-12
- Section: Research
- Word count: 2390
- Dispatch: Nº 64 · Research · 9 min read
- Full headline on page: How to add *alt text* to Shopify product images in bulk
- Keywords: Shopify image alt text, bulk alt text Shopify, add alt text to all images, product image SEO, image alt attribute, Shopify accessibility, WCAG alt text, AI alt text
- Publisher: Dugong Field Notes, https://blog.dugong.live/ (Dugong, https://dugong.live)

---

There is a question that turns up in the Shopify community forums in nearly the same words every few weeks. Someone has a few hundred products, several photos each, and they want to know if there is a way to add alt text to all of them without opening every image one at a time. The reply they get is the uncomfortable kind. There is no bulk field for alt text in the admin, there is no screen that shows you which images are missing it, and Shopify will not write one for you. One thread asks it plainly: is there a way to bulk upload alt text to images on a Shopify site. The honest answer is that the admin does not give you one.

It sounds like a footnote until you do the arithmetic. A store with five hundred products at an average of four images each is two thousand alt fields, and every one of them starts empty and stays empty until a human opens the product, clicks into the media, and types a line. Nobody schedules a two-thousand-line typing job, so it gets done for the first few products and the homepage banner and then abandoned. The field that decides whether a blind shopper can use your store, and whether your product photos show up in image search, becomes a task nobody finishes, and most stores quietly leave it blank across the whole catalog.

> Shopify will store an alt text for every image. It just will not *write* one, and it will not show you the ones that are missing.

## Why a blank alt field is two problems, not one

Alt text is the short written description attached to an image. It does two jobs at once, and the empty field fails both. The first is accessibility. A shopper using a screen reader does not see your photo, they hear whatever is in the alt text. When it is blank, the reader either says nothing or reads the file name out loud, so a customer hears "image four eight two one j p g" where a sighted shopper sees a navy wool coat. That is the difference between a store someone can buy from and one they leave. It is also increasingly a legal exposure: missing alt text is the single most common accessibility failure cited in the demand letters that now land on ecommerce stores, and enforcement under the standards that govern them has only picked up.

The second job is search. Search engines cannot see the contents of a photo the way a person can, so they lean on the alt text to understand what the image shows. That is what gets your product photos into Google Images, which for a lot of product categories is a real and underused source of traffic, and it is one more signal about what the page itself is about. A blank alt field gives the search engine nothing, so the image is effectively invisible to it. And the newer answer engines, the AI layers that increasingly sit between a shopper and your store, read the same descriptive text to decide what a page is and whether to surface it. The alt attribute has quietly gone from an accessibility nicety to a line that screen readers, image search, and AI all read, and it is still sitting empty on most of the catalog.

## What Shopify actually does, and where it stops

Shopify is fluent in storing the field and silent on the part that takes the work, which is writing an accurate description for each image. The gap shows up in three places merchants hit fast.

First, **there is no [bulk editor](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/bulk-editing) and no audit**. You set alt text one image at a time, inside each product's media, by typing the line. There is no view anywhere in the admin that lists which images have alt text and which do not, so on a catalog of any size you cannot even see the size of the gap, let alone close it in one move. The work is invisible until a screen reader or an SEO audit surfaces it months later.

Second, **nothing is filled in by default, and the file name is not alt text**. Upload a photo and the alt field is empty. Shopify does not generate a description from the image, and a photo that came off a phone as `IMG_4821.jpg` carries nothing a screen reader can use. Because the field is blank rather than visibly broken, most merchants never notice it is empty, which is exactly why thousands of images ship live with no alt text at all.

Third, **the one bulk path is the CSV, and it is brittle**. The product export does include an Image Alt Text column, so you can fill it in a spreadsheet and re-import, which is the answer every forum thread lands on eventually. But the spreadsheet does not write the descriptions for you, it just gives you two thousand empty cells instead of two thousand empty fields. It only covers product images, not the collection banners, theme slides, and content images that also need alt text. And a careless re-import can overwrite the columns next to it, so the bulk move meant to save an afternoon turns into a cleanup.

> **◆ DATA** Keep alt text **short, roughly under 125 characters**, since many screen readers cut off around there. **Describe what is in the picture** in plain language rather than stuffing in keywords, which reads badly aloud and can look like spam to a search engine. And genuinely decorative images, a divider or a background flourish, should get an **empty alt attribute** so a screen reader skips them instead of reading noise. None of these are rules Shopify can apply for you, because each one depends on looking at the specific image.

## Why the usual fixes don't hold

Once a merchant feels this, they reach for one of a few workarounds. Each buys a little ground and each breaks in a familiar spot.

**"I will just write them all by hand."** The right instinct, and fine for a small catalog. It collapses at scale. Two thousand images at even thirty seconds each of looking and typing is the better part of a work week of nothing else, so it gets done for the newest products and the bestsellers and abandoned for the long tail, which is exactly the part of the catalog that needed the image-search traffic. The work is never wrong, it is just never finished.

**"I will export a CSV and fill the column."** A real step up for moving the data, and the right tool once the lines are written. But the spreadsheet does not look at the photos for you, so you are still describing every image, now in a cramped grid of cells instead of next to the picture where you can at least see what you are describing. It misses every non-product image, and one wrong re-import can stamp stale data over live fields.

**"I will install an alt text app that bulk-fills them."** The app store is full of these, which by itself tells you the native gap is real. The cheap ones work from a template, usually the product title plus the variant, so every image on a product gets the same line, the front and the back and the detail shot all reading "Navy Wool Coat." That is technically filled and functionally useless: it does not describe the actual photo, it often repeats across a dozen near-identical images, and when it pads the line with extra keywords it tips into the stuffing that search engines discount. The better ones use image recognition and genuinely help, which is the right idea, and the point of this piece is that the recognition is the whole job, not a feature to bolt on.

## What the automation actually has to do

The real job is not "fill the field." It is "for every image that has no alt text, or a duplicated one, or just the file name, look at the picture, write a line that describes what it actually shows, keep it short and on brand, leave the decorative ones empty, and never let two near-identical shots read the same." That is looking, judgment, and bookkeeping at catalog scale. As a Dugong playbook, in plain prose, it reads like this:

```
# trigger
On a catalog audit, and again whenever an image is uploaded or replaced

# steps
1. Find every product, variant, collection, and content image
   whose alt text is missing, duplicated, or just the file name
2. Look at the image itself, plus the product context: title,
   type, the variant it belongs to, color and material
3. Write a concise, accurate line that describes what the
   photo shows, in the store's voice, under ~125 characters
4. Keep near-identical variant and angle shots distinct, so
   a front and a back, or two colorways, never read the same
5. Leave genuinely decorative images with an empty alt so a
   screen reader skips them instead of reading noise
6. Write the alt text back through the Admin API in batches,
   touching nothing else on the product
7. Log every line for a quick human spot-check, and flag the
   images too generic or low-quality to describe well
```

Seven lines. The compiler fills in everything beneath: pulling the list of images with no alt text or a duplicated one across products, variants, collections, and content, looking at each photo to write a line that fits it and only it, holding the length and the brand voice, telling a meaningful product shot from a decorative divider, comparing the set so the front and the back of the same item do not come out identical, writing back to the right image without disturbing price or inventory, and re-checking new uploads as they land so the field never silently drifts back to blank. The merchant never sat in the admin typing the two-thousandth description. They described how a careful editor would caption the catalog, and let the compiler do the volume.

> **◆ NOTE** The blank field is the quiet one. A missing alt text is not a neutral gap, it is a **customer who hears "image four eight two one" instead of your product**, and a photo your search engine cannot read. The goal is not "every field is filled," it is a line that actually describes the picture, which is precisely the judgment a template built from the product name can never make. The picture is the whole point, and the template never looks at it.

## Why this is a compiler problem, not an app problem

There are capable alt text apps, and the ones that read the image are a fine start for plenty of stores. But good alt text is not a slot to fill, it is a sentence about this specific photo: what it shows, from what angle, in which color, on whom. That is different for the front of a coat than for the lining detail, different again for a lifestyle shot than for a flat product shot of the same item, and different for a decorative banner that should carry no alt at all. Those are judgments about the picture in front of you, not tokens in someone else's template.

A natural-language compiler fits because writing alt text was never really a data problem. It is a *looking and judgment* problem wearing a data problem's clothes. Storing the field is the easy part, which is why Shopify does it. The hard part is everything around it: open each image, see what is actually in it, write a line that fits only it, keep them all distinct, hold the length, sound like the brand, know which images deserve no alt at all, and keep doing it as the catalog grows. You can write that brief in a paragraph. You could never hold it as two thousand careful captions in the admin, repeated every time you add a product. It sits in the same family as the other on-page work Shopify stores but will not write for you, like [the meta description you write one at a time](https://blog.dugong.live/how-to-bulk-edit-meta-descriptions-on-shopify.html) and [the product descriptions you'll never finish writing](https://blog.dugong.live/how-to-generate-shopify-product-descriptions-with-ai.html).

## The workflow worth building this week

If image search is any part of how customers find you, or if you would rather not be the store named in an accessibility complaint, this is the automation to set up before your next product drop, because the alt text you never wrote is quietly losing you both a slice of traffic and the shoppers who cannot use a page without it. It sits right next to the on-page SEO chores we have written about already, the line under your link in [the meta description you write one at a time](https://blog.dugong.live/how-to-bulk-edit-meta-descriptions-on-shopify.html), and the body copy in [the product descriptions you'll never finish writing](https://blog.dugong.live/how-to-generate-shopify-product-descriptions-with-ai.html). The deeper pattern, that the work worth automating is rarely the work that is easy to automate, is the whole argument of [the Shopify automations no one builds](https://blog.dugong.live/best-shopify-automations-to-set-up.html).

Describe it the way you would brief a careful editor: here is the catalog, look at every image that has no alt text or a duplicated one, write me an accurate, on-brand line that describes what each photo actually shows, keep them short, leave the decorative ones empty, never two the same, and keep it current as I add products. That is the whole brief. The compiler does the looking, the writing, the uniqueness check, and the write-back. You keep your attention for the products themselves, and you stop discovering that the entire catalog ships photos a screen reader and a search engine both read as nothing.

> **◆ READING** If this resonates, two companion pieces: our dispatch on [the sold-out products that sink your collection](https://blog.dugong.live/how-to-push-sold-out-products-to-the-bottom-of-a-shopify-collection.html), where the storefront has to stay sharp as stock moves, and the field study on [the Shopify automations no one builds](https://blog.dugong.live/best-shopify-automations-to-set-up.html), where the work that scales with the catalog is a sliver of what merchants actually wire up. Also worth reading: [the variant field the product CSV leaves out](https://blog.dugong.live/how-to-bulk-edit-variant-metafields-on-shopify.html), on the same bulk-fill problem one level down, at the variant. And [the product that went live with no photo](https://blog.dugong.live/how-to-find-shopify-products-missing-images-or-weights.html), on finding the products where there is no image to describe in the first place.

If you are a Shopify merchant who has wired up an alt text workflow that actually reads each image and keeps it current, or you have a story about the catalog that ranked but shipped two thousand blank alt fields, the inbox is open: `field-notes@dugong.live`. We are collecting case studies for the next issue.

---

## Common questions

### Can you bulk edit image alt text in Shopify?

Not in the admin. Shopify lets you set an alt text on an image, but only one image at a time, by opening each product, clicking into the media, and typing the line. There is no bulk editor for alt text and no view that shows you which images are missing it, so on a catalog of any size you cannot even see the gap, let alone fix it in one move. The one bulk path is the product CSV, which has an Image Alt Text column you can fill in a spreadsheet and re-import. That moves the data but does not write the descriptions for you, it only covers product images and not theme or content images, and a careless re-import can overwrite other fields. So past the first handful of products the alt text simply never gets written.

Permalink: https://blog.dugong.live/how-to-add-alt-text-to-shopify-product-images-in-bulk.html#faq-1

### Does Shopify add alt text to images automatically?

No. When you upload an image to a Shopify product the alt text starts empty and stays empty until someone types it. Shopify does not generate a description from the image, and the file name is not alt text, so a photo uploaded as IMG_4821.jpg has nothing a screen reader can read and nothing a search engine can use. Because the field is blank rather than visibly broken, most merchants never notice it is empty, which is exactly why thousands of product images ship to the live store with no alt text at all.

Permalink: https://blog.dugong.live/how-to-add-alt-text-to-shopify-product-images-in-bulk.html#faq-2

### What makes good alt text for a Shopify product image?

Describe what is actually in the picture, in plain language, as if you were telling someone who cannot see it what the photo shows. Keep it short, roughly under 125 characters, because many screen readers cut off around there. Lead with the thing itself and the detail that matters for that product, the color, material, angle, or who is wearing it, rather than stuffing in keywords, which reads badly aloud and can look like spam to search engines. Genuinely decorative images, a divider line or a background flourish, should get an empty alt attribute so screen readers skip them instead of reading noise. The hard part is not the rule, it is that a good line has to come from looking at the specific image, which is why a template built from the product name never quite describes the photo.

Permalink: https://blog.dugong.live/how-to-add-alt-text-to-shopify-product-images-in-bulk.html#faq-3

### Is missing alt text an accessibility or legal risk for a Shopify store?

Yes, and it is the risk merchants see last. A shopper using a screen reader hears the alt text instead of seeing the photo, so when the field is blank the reader either says nothing or reads the file name aloud, and a customer hears image four eight two one j p g where a sighted shopper sees a navy wool coat. That is the difference between a store someone can buy from and one they leave. It is also a growing legal exposure: missing alt text is the single most common accessibility failure cited in the demand letters that now land on ecommerce stores, and enforcement of the standards behind them has only picked up. Because Shopify never shows you which images are blank, a store can carry thousands of these gaps without anyone noticing until an audit or a demand letter arrives.

Permalink: https://blog.dugong.live/how-to-add-alt-text-to-shopify-product-images-in-bulk.html#faq-4

### Does alt text help Shopify product images rank in Google Images?

Yes. Search engines cannot see what a photo shows the way a person can, so they lean on the alt text to understand the image, and that line is what gets product photos into Google Images, which for a lot of product categories is a real and underused source of traffic. The same text is one more signal about what the page itself is about, and the newer AI answer engines that sit between a shopper and your store read the same descriptive text when they decide what a page is and whether to surface it. A blank alt field gives all of them nothing, so the image is effectively invisible to image search no matter how good the photo is. On most Shopify catalogs that is the default state, because the field starts empty on every upload and nothing in the admin ever flags it.

Permalink: https://blog.dugong.live/how-to-add-alt-text-to-shopify-product-images-in-bulk.html#faq-5

---

Markdown rendition of https://blog.dugong.live/how-to-add-alt-text-to-shopify-product-images-in-bulk.html. Written by Priya Singh for Dugong Field Notes, the working journal of Dugong (https://dugong.live), AI-native workflow automation. Cite the canonical URL above.
