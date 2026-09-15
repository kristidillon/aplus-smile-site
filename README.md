# A+ Smile / BNY Dental P.C. — Website

Static, no-build website for A+ Smile / BNY Dental P.C., Fort Lauderdale, FL.
Served by GitHub Pages at **https://www.aplusdentalfl.com**.

**Doctors:** Dr. Natalia Bartkova, DDS · Dr. Yuriy Kaziyev, DDS
**Address:** 6231 N Federal Hwy, Fort Lauderdale, FL 33308
**Office:** (754) 802-1588 · **Urgent:** (347) 284-8463
**Email:** hello@aplusdentalfl.com

---

## ⚠️ Read this first

`robots.txt` previously contained `Disallow: /`, which told every search engine
to ignore the entire site. It now allows crawling and points at the sitemap.
**Nothing on this site could rank until that shipped.**

---

## Structure

```
aplus-smile-site/
├── index.html                     # Home — "dentist Fort Lauderdale"
├── services/
│   ├── index.html                 # Services hub
│   ├── family-dentistry/
│   ├── preventive-dentistry/
│   ├── restorative-dentistry/
│   ├── cosmetic-dentistry/
│   ├── teeth-whitening/
│   ├── dental-implants/
│   ├── dentures/
│   ├── invisalign/
│   ├── periodontal-care/
│   └── emergency-dentistry/
├── doctors/
│   ├── index.html
│   ├── dr-natalia-bartkova/
│   └── dr-yuriy-kaziyev/
├── 404.html
├── assets/
│   ├── site.css                   # All styles, shared by every page
│   ├── favicon.svg
│   ├── dr-bartkova.jpg            # 400×520
│   ├── dr-kaziyev.jpg             # 400×520
│   └── before-after.jpg           # 760×754
├── tools/
│   ├── content.py                 # ← all page copy lives here
│   └── build.py                   # generates the HTML + sitemap.xml
├── robots.txt
├── sitemap.xml
├── CNAME
└── .nojekyll
```

## Editing the site

All page copy lives in **`tools/content.py`**. Edit it, then regenerate:

```bash
python3 tools/build.py
```

That rewrites every `.html` page and `sitemap.xml` from the same templates, so
the nav, footer, structured data and metadata can never drift apart across
15 pages. **Do not hand-edit the generated `.html` files** — the next build
overwrites them. Design changes go in `assets/site.css`; layout changes go in
`tools/build.py`.

GitHub Pages still serves the committed HTML directly. There is no build step
at deploy time.

### Content rules for `tools/content.py`

* Every claim must be verifiable by the practice. No awards, no outcome
  guarantees, no invented credentials, no insurance-participation claims.
* FAQs in `content.py` are rendered as **visible** questions on the page. That
  is what makes the `FAQPage` structured data legitimate — never add an FAQ
  that a human reader cannot see.
* Keep the location references natural. Once in the H1 and once or twice in the
  body is enough; the current pages sit at 0.8–1.4% density.

## Run locally

```bash
python3 -m http.server 8000     # then open http://localhost:8000
```

Opening `index.html` directly with `file://` will not work — links and the
stylesheet use root-relative paths.

---

## Local SEO implementation

| Item | Where |
|---|---|
| Unique title + meta description | `head_html()` in `tools/build.py`, values in `content.py` |
| Canonical URLs | Self-referencing on every page |
| Open Graph + Twitter cards | Every page, with per-page image |
| `Dentist` / `LocalBusiness` schema | Full node on home (`#practice`), reference node on every other page |
| `Person` schema | Both doctor pages, linked to `#practice` via `employee` / `worksFor` |
| `Service` schema | All 10 service pages, `provider` → `#practice` |
| `FAQPage` schema | Only on pages with a visible "Questions patients ask" section |
| `BreadcrumbList` | Every interior page, matching the visible breadcrumb trail |
| `WebSite` / `WebPage` | Home / all pages |
| XML sitemap | `sitemap.xml`; `lastmod` per URL comes from the file's last commit, so it reflects real changes |
| `robots.txt` | Allows all crawlers, references the sitemap |

### Target term → page

| Term | Page |
|---|---|
| dentist Fort Lauderdale / Fort Lauderdale dentist | `/` |
| family dentist Fort Lauderdale | `/services/family-dentistry/` |
| preventive dentistry Fort Lauderdale | `/services/preventive-dentistry/` |
| restorative dentist Fort Lauderdale | `/services/restorative-dentistry/` |
| cosmetic dentist Fort Lauderdale | `/services/cosmetic-dentistry/` |
| teeth whitening Fort Lauderdale | `/services/teeth-whitening/` |
| dental implants Fort Lauderdale | `/services/dental-implants/` |
| dentures Fort Lauderdale | `/services/dentures/` |
| Invisalign Fort Lauderdale | `/services/invisalign/` |
| periodontal care Fort Lauderdale | `/services/periodontal-care/` |
| emergency dentist Fort Lauderdale | `/services/emergency-dentistry/` |

One page owns each term, in both the `<title>` and the `<h1>`. No page competes
with another for the same query.

### Brand continuity (BNY Dental P.C.)

The prior practice name is preserved so existing citations, directory listings
and links keep pointing at the same entity: it appears in `legalName` and
`alternateName` in the schema, in the home page `<title>`, in the site-wide
footer, and in the copyright line.

### Performance

* One shared, preloaded stylesheet (~17 KB) cached across all 15 pages.
* No JavaScript, no web fonts, no third-party requests.
* Every `<img>` carries intrinsic `width`/`height` (no layout shift), the LCP
  image on each page carries `fetchpriority="high"`, and below-the-fold images
  are `loading="lazy" decoding="async"`.
* No horizontal overflow at 390 px — verified on every page template.

---

## Before launch — verification checklist

Claims the practice must confirm (these were already on the site; making the
site indexable means they will now be read by patients and by Google):

- [ ] **"Most insurance accepted"** (home page trust row) — confirm, or replace
      with the specific plans accepted. Do not publish an insurance claim that
      cannot be substantiated.
- [ ] **"Same-week appointments"** and **"Clear, upfront pricing"** (home page).
- [ ] **Free implant & cosmetic consults** — referenced on the home page and on
      `/services/dental-implants/` and `/services/cosmetic-dentistry/`.
- [ ] **Doctor bios.** The generated doctor pages deliberately omit years-in-
      practice figures. The home page bios still describe career history; confirm
      the wording with both doctors.
- [ ] **Invisalign.** `/services/invisalign/` describes clear aligner treatment
      generally and makes no provider-tier or certification claim. If the
      practice holds a specific Invisalign provider status, add it; if it uses a
      different aligner system, rename the page.
- [ ] **Before/after photo** — confirm it is this practice's own case, with
      documented patient consent.
- [ ] **WebMD review quote** on the home page — swap for a Google review once
      the Business Profile has one.

Still to do:

- [ ] **Office hours.** Intentionally omitted rather than guessed. Once
      confirmed, add them to the Visit section *and* to `openingHoursSpecification`
      in `practice_node()` — Google weights this for local ranking.
- [ ] **Geo coordinates.** `geo` is deliberately absent from the schema rather
      than approximated. Take the exact lat/long from the Google Business
      Profile pin and add it to `practice_node()`.
- [ ] **Google Business Profile.** Create/claim it. Name, address and phone must
      match the site *character for character* — the site uses
      `A+ Smile / BNY Dental P.C.`, `6231 N Federal Hwy`, `(754) 802-1588`.
      Then add the profile URL to `sameAs` in `practice_node()` and link the
      review page from the footer.
- [ ] **Google Search Console.** Verify the domain, submit
      `https://www.aplusdentalfl.com/sitemap.xml`, and request indexing for the
      home page and the services hub.
- [ ] **Social accounts.** Recommended handle `@APlusSmileFTL`. Once live, add
      them to `sameAs` in `practice_node()`.
- [ ] **Open Graph image.** Pages currently share the before/after photo. A
      dedicated 1200×630 branded image would present better when the site is
      shared.
- [ ] **WebP versions** of the three photos, served via `<picture>`. Current
      JPEGs are 27–71 KB, so this is an optimisation, not a blocker.
- [ ] **Practice logo** in the nav (currently the text wordmark "A+ Smile").

## Design system

Tokens live in `:root` at the top of `assets/site.css`.

| Token | Value | Use |
|---|---|---|
| `--ink` | `#1C2422` | Headlines, body |
| `--gray` | `#5F6B68` | Secondary text |
| `--teal` | `#157A72` | CTAs, links (from the tooth logo) |
| `--teal-deep` | `#0F5F59` | Hover state |
| `--aqua` | `#ECF5F3` | Tinted section backgrounds |
| `--sand` | `#F7F4EE` | Cards |
| `--gold` | `#C9A05C` | Accents (logo's gold swoosh) |

Type: system stack (`-apple-system`, SF Pro on Apple devices, Segoe/Roboto
elsewhere). Light mode only.
