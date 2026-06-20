# SEO / GEO report — 2026-06-20

**Post:** The image alt text no one writes
**URL:** https://blog.dugong.live/the-image-alt-text-no-one-writes.html
**Dispatch:** Nº 64 · Author: Priya Singh · ~2,000 words / 9 min

## Target query space

Primary intent: Shopify merchants who want to add alt text to all their product images and find no
native bulk way to do it, plus those auditing image SEO or accessibility.

- bulk alt text Shopify / add alt text to all images Shopify
- Shopify image alt text (SEO + accessibility)
- does Shopify add alt text automatically
- how to add alt text to Shopify product images
- Shopify alt text best practices / length
- image SEO Shopify / Google Images ranking
- Shopify accessibility / WCAG alt text / screen reader

The heading "The image alt text no one writes" leads with the searched noun phrase ("image alt text")
and names the pain (the field that never gets written), so it pulls both the frustrated merchant and the
solution-seeker. The slug mirrors the headline exactly.

## On-page SEO

- **Title tag:** "The image alt text no one writes — Dugong Field Notes" (front-loads the key phrase).
- **Meta description:** ~150 chars, states the native gap (no auto-fill, no bulk) and the AI fix. Inside
  the house SERP-safe range; unique vs every sibling.
- **Canonical** self-referential; robots index,follow with max-image-preview:large and max-snippet:-1.
- **Keywords meta + OG/Twitter** cards complete with image alt text on the banner image (practising what
  the post preaches).
- **Heading hierarchy:** single H1; H2s frame the funnel (two problems at once → what Shopify does and
  where it stops → why the usual fixes fail → what the automation has to do → compiler vs app → the
  workflow worth building). FAQ questions are H2 to match the FAQPage schema.
- **Internal links:** body links the meta-description and product-descriptions posts (same on-page chore
  family), the sold-out/merchandising post, and the field study; Read-next links 16 siblings. Two
  inbound backlinks added (first Read-next card in the product-descriptions and meta-description posts)
  plus two topic-cloud entries on the homepage. Net internal-link equity flows in and out.

## GEO / answer-engine optimisation

- **BlogPosting + BreadcrumbList + FAQPage + HowTo** JSON-LD, all parsing. `speakable` targets the title
  and FAQ.
- **FAQPage** answers three high-intent questions verbatim-quotable by an answer engine: can you bulk
  edit alt text in Shopify (no, CSV is the only bulk path), does Shopify add alt text automatically (no),
  and what makes good alt text (under ~125 chars, describe the picture, decorative = empty alt, no
  stuffing).
- **HowTo** encodes the seven-step playbook as structured steps, the format answer engines lift for
  "how to" queries.
- **about** entities link Shopify, Alt attribute, and Web accessibility on Wikipedia for entity grounding.
- **llms.txt** carries a long, self-contained descriptive entry so a model reading the site index gets
  the full crux (the native gap, the two failure jobs, the workaround failures, and the playbook) without
  fetching the page.
- The body states concrete, citable facts an answer engine can quote: no native bulk editor or audit,
  blank-by-default and file-name-is-not-alt-text, the CSV Image Alt Text column and its limits, the
  ~125-character screen-reader cutoff, decorative-images-get-empty-alt, and missing alt text as the most
  common accessibility failure in demand letters.

## Distinctiveness vs existing catalogue

Distinct from Nº 61 (meta description = SERP snippet) and Nº 63 (product description = body copy): this
post is the alt attribute on the images, with the unique angles of accessibility/legal exposure and AI
vision (the line has to come from looking at the photo). No keyword cannibalisation; the three posts
cross-link as a deliberate on-page-SEO cluster.

## Checks

- Meta description unique and in range; title unique; slug matches headline.
- Schema validates (BlogPosting/Breadcrumb/FAQ/HowTo); FAQ text mirrors visible FAQ.
- Added to sitemap.xml (priority 0.9), feed.xml (newest item), llms.txt (top of Articles), homepage
  JSON-LD blogPost array (newest after lead essay), and topic cloud.
