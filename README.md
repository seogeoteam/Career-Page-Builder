# Career Page Builder 🚀

> **Autonomous Website Scraper, Google for Jobs JSON-LD Schema Generator & Zero-Defect Recruitment Funnel Builder.**

Give it **only a website URL**, and Career Page Builder autonomously reverse-engineers brand assets, extracts dual-color hex palettes from the logo, verifies business entity & licensing credentials, and compiles a production-grade, 100% Google-compliant Careers Page with zero errors on the Google Rich Results Test.

---

## 🌟 Key Capabilities

1. **Single-URL Ingestion (Zero Extra Inputs):**
   * Automatically scrapes business name, headquarters address, phone numbers, contact emails, founder names, CSLB / Red Seal license numbers, Google Knowledge Graph IDs (`kgmid`), Google Maps CID, and BBB ratings.
2. **Deep Logo Color Extraction:**
   * Analyzes the website's logo image to extract exact **Primary** (dominant corporate/navy tone) and **Secondary** (vibrant construction amber/accent) hex colors.
3. **Google for Jobs Schema Guaranteed (0 Errors, 0 Warnings):**
   * Generates 100% valid JSON-LD `@type: "JobPosting"` schemas with mandatory properties (`title`, `description`, `datePosted`, `validThrough`, `employmentType`, `hiringOrganization`, `jobLocation`, `baseSalary`, and `directApply: true`).
4. **Zero Funnel Drop-off (Eliminates Broken Loops):**
   * Replaces broken, self-referencing links with an inline 60-second mobile Quick-Apply form with file upload support and direct HR fallback channels.
5. **Strict Design Mandates Built-In:**
   * **Centered Header:** Location badge, title, and subtitle are strictly centered (`text-align: center; margin: 0 auto;`).
   * **Pure White Background:** Strictly `#FFFFFF` on container cards.
   * **Fluid Responsiveness:** Universal `max-width: 100%` container bounding for seamless desktop, tablet, and mobile layouts.
6. **3-Variant Meta Title, Description & H1 Generator:**
   * Produces Geo-Targeted Local SEO, Benefit-Driven E-E-A-T, and Action-Oriented Direct Apply copy variants.

---

## 📁 Repository Structure

```text
Career-Page-Builder/
├── SKILL.md                          # AGY / IDE Skill Definition & Workflow
├── README.md                         # Documentation & Usage Guide
├── scripts/
│   ├── scrape_website.py             # Autonomous Website Scraper
│   ├── extract_logo_palette.py       # PIL-based Logo Dual-Color Extractor
│   └── generate_career_page.py       # Standalone HTML & Schema Compiler
└── examples/
    └── burnette_careers_sample.html  # Production Sample (Burnette Construction)
```

---

## ⚡ Quick Start

### 1. Scrape Any Website URL
```bash
python scripts/scrape_website.py --url "https://burnetteco.com/" --out scraped_data.json
```

### 2. Extract Exact Logo Colors
```bash
python scripts/extract_logo_palette.py --logo "https://burnetteco.com/wp-content/uploads/2026/03/logo2.png"
```
*Output:*
```json
{
  "primary": "#02349A",
  "secondary": "#F5A11C"
}
```

### 3. Generate 100% Valid Careers Page
```bash
python scripts/generate_career_page.py \
  --data scraped_data.json \
  --primary "#02349A" \
  --secondary "#F5A11C" \
  --out careers.html
```

---

## 📋 Google for Jobs Schema Compliance

Career Page Builder produces schemas fully validated against Schema.org and Google Search Central requirements:

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "JobPosting",
      "title": "Lead ADU Carpenter & Framing Specialist",
      "description": "<p>Full job responsibilities, requirements, and benefits...</p>",
      "datePosted": "2026-10-15T08:00:00-07:00",
      "validThrough": "2026-12-31T23:59:59-07:00",
      "employmentType": "FULL_TIME",
      "directApply": true,
      "hiringOrganization": {
        "@type": "Organization",
        "name": "Burnette Construction",
        "sameAs": "https://burnetteco.com/",
        "logo": "https://burnetteco.com/wp-content/uploads/2026/03/logo2.png"
      },
      "jobLocation": {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "8100 Otium Way",
          "addressLocality": "Antelope",
          "addressRegion": "CA",
          "postalCode": "95843",
          "addressCountry": "US"
        }
      },
      "baseSalary": {
        "@type": "MonetaryAmount",
        "currency": "USD",
        "value": {
          "@type": "QuantitativeValue",
          "minValue": 36.00,
          "maxValue": 52.00,
          "unitText": "HOUR"
        }
      }
    }
  ]
}
```

---

## 🛠️ WordPress & Elementor Integration
1. Open WordPress Admin and create or edit your `/careers/` page.
2. In Elementor, drop an **HTML Widget** into a Full-Width (100%) section.
3. Paste the generated HTML directly into the widget and hit **Publish**.

---

## 📄 License
MIT License. Free for commercial and agency use.
