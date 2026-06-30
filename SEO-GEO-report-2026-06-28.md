# SEO / GEO report — 2026-06-28 (audit pass)

**Scope:** blog.dugong.live — index + 22 posts + feed / sitemap / llms / robots / CNAME
**Mode:** automated scheduled run (autonomous, no user present)

## Result: fixed one over-length meta description on the newest post; everything else green

The working tree was clean at start (HEAD `d0f8973 "Hola"`). Since the 06-27 audit, that commit
shipped Dispatch Nº 69 ("The tracking number you paste by hand") and propagated it fully — a
back-link card into every sibling's `.related-grid`, plus entries in index.html, sitemap.xml,
feed.xml, llms.txt, and JSON-LD. Post count on disk is now 22 (21 June dispatches + the 2026-05-28
pillar essay). The earlier recurring "new post under-linked" defect did not surface today because
that propagation was already done in the publish commit.

The one defect found was a content-meta issue on the new post: its `<meta name="description">`
(and the matching `twitter:description`) ran to 227 characters, well outside the 146–162 house
band that all other 21 posts hold. An over-length meta description gets truncated in both search
snippets and answer-engine citations, so I trimmed it to band.

## Defect: Nº 69 meta description was 227 chars (band is 146–162)

**File:** `the-tracking-number-you-paste-by-hand.html`

The post shipped with a 227-char description, duplicated into `twitter:description` per house
convention (meta == twitter; og:description is intentionally longer). Every other post sits inside
146–162. The new post was the lone outlier.

**Fix:** rewrote both the `description` and `twitter:description` to a single 160-char line:

> Shopify makes you paste each order's tracking number by hand, and Flow cannot help. The AI
> playbook that fulfills every order with the right number and carrier.

It keeps both halves of the original — the pain (pasting tracking by hand, Flow can't help) and
the payoff (fulfills with the right number and carrier) — at citation-safe length, with no em or
en dashes (house style). The longer `og:description` and the JSON-LD `description` fields were left
untouched: og has no truncation penalty and the house pattern keeps it long.

**Net change:** 2 lines in 1 file (`git diff --numstat` → `2 2`), a pure value swap. No structural
or schema lines touched.

## Verification (post-fix re-sweep)

- **Meta descriptions:** all 22 present, all 22 unique, all now inside 146–162 (0 out of band).
- **JSON-LD:** all blocks on the edited post still parse; no schema field was changed.
- **No dash regressions:** the new description contains zero em/en dashes.

## Site-wide audit (everything else clean)

**Content and meta**
- Post count: 22 on disk (21 June dispatches + the 2026-05-28 pillar essay).
- Titles: all 22 unique. H1: exactly one per post (22/22).
- Canonical: present on every post (22/22). Twitter card + og:title: present on every post (22/22).
- Image alt text: no `<img>` missing an alt attribute across posts or index.

**Internal link graph**
- In-degree is uniform at 21 for all 22 posts (every post is linked from all 21 siblings via the
  `.related-grid`). No orphans, no asymmetry. Nº 69's back-links were already complete from the
  publish commit.
- Zero broken internal `.html` links across the whole site.

**Structured data (the GEO backbone)**
- Every post carries the full rich-result stack: `BlogPosting`, `FAQPage`, `BreadcrumbList`,
  `SpeakableSpecification`, `Person`, `Organization`, `ImageObject`, plus `HowTo` on 21 of 22
  (the pillar essay intentionally omits HowTo).
- All JSON-LD parses on all 22 posts and on index.html.

**Discovery and freshness assets**
- Coverage cross-check — disk vs sitemap vs feed vs llms.txt vs index.html: all five sets
  identical at 22 posts, zero drift.
- sitemap.xml: valid XML; every post's `<lastmod>` matches that post's `dateModified` exactly
  (0 mismatches across 22 posts).
- feed.xml: valid XML.
- llms.txt: references all 22 posts.
- robots.txt: `Allow: /` for `*` plus explicit allow for every major answer-engine crawler; Sitemap
  line present.
- og-image.png, favicon.png, favicon.svg, apple-touch-icon.png all present. CNAME = blog.dugong.live.

**Homepage counters (consistency)**
- Ticker "21 NEW DISPATCHES THIS MONTH" x2 matches the 21 posts with a June 2026 datePublished.
- Hero "ISSUE Nº 69" and archive "browse all 69 dispatches" agree with the newest dispatch
  (tracking-number, datePublished 2026-06-27).

## Reviewed and intentionally not changed

- **dateModified / sitemap lastmod / feed lastBuildDate:** left as set by the 06-27 publish. The
  only edit today was a meta-description value swap, not an article-body content change, so bumping
  any freshness timestamp would send a false "updated today" signal to crawlers and answer engines.
- **og:description / JSON-LD description on Nº 69:** left long on purpose. og has no snippet-
  truncation penalty and the house pattern keeps it expansive; only the search/answer-facing meta
  and twitter descriptions need the band.

## Recommendations (for a future run with a human in the loop)

1. **Lint meta-description length at publish time.** This run's only defect was a new post shipping
   with a 227-char description. A one-line check in the publish pipeline (reject/flag any
   `meta description` outside 146–162) would catch this at source and retire it as a recurring
   audit finding, the same way back-link propagation should be automated at publish.
2. **Organization / author `sameAs`.** Standing item: the `#organization` and `Person` (Priya
   Singh) nodes still have no `sameAs` array. Verified profile URLs would strengthen entity
   grounding for answer engines. Needs real URLs supplied — not safe to invent in an autonomous run.

## Note

The single change is staged in the working tree only; no git commit or deploy was performed,
consistent with prior runs.
