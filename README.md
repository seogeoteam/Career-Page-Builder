# Career Page Builder 🚀

> **Autonomous Website Scraper, Google for Jobs JSON-LD Schema Generator & Zero-Defect Recruitment Funnel Builder.**

Give it **only a website URL**, and Career Page Builder autonomously reverse-engineers brand assets, extracts dual-color hex palettes from the logo, verifies business entity & licensing credentials, and compiles a production-grade, 100% Google-compliant Careers Page with zero errors on the Google Rich Results Test.

---

## 🌟 Key Capabilities

1. **Single-URL Ingestion (Zero Extra Inputs):**
   * Automatically scrapes business name, headquarters address, phone numbers, contact emails, founder names, CSLB / Red Seal license numbers, Google Knowledge Graph IDs (`kgmid`), Google Maps CID, and BBB ratings.
2. **WordPress Embed & Zero Header Conflict Mandate (Strict Mandate):**
   * Built specifically for clean integration into client WordPress/CMS themes (Astra, Elementor, Divi).
   * **Zero Mock Nav Clutter:** Does NOT inject fake multi-item navigation bars or top utility strips that create duplicate headers over the WordPress theme's existing navigation.
   * **No Duplicate Logo Rows:** The careers layout begins directly with the centered hero title section.
3. **Strict Logo Sizing & Anti-Overflow Controls:**
   * Prevents unconstrained high-res logos (1024px+) from blowing up and squashing contact buttons. Enforces strict dimension caps (`height: 48px; max-width: 220px; object-fit: contain;`).
4. **Deep Logo Color Extraction & Dual-Color Harmony:**
   * Analyzes the website's logo image to extract exact **Primary** (dominant corporate/navy/gold tone) and **Secondary** (vibrant amber/accent) hex colors.
5. **Strict Centered Alignment Built-In:**
   * **Centered Header:** Location badge, H1 title, subtitle, and trust badges are strictly centered (`text-align: center; margin: 0 auto;`).
   * **Pure White Background:** Strictly `#FFFFFF` on container cards and forms. Never dark, grey, or tinted cards.
   * **Fluid Responsiveness:** Universal `max-width: 100%` container bounding for seamless desktop, tablet, and mobile layouts.
6. **Google for Jobs Schema Guaranteed (0 Errors, 0 Warnings):**
   * Generates 100% valid JSON-LD `@graph` containing `WebPage`, `BreadcrumbList`, and multi-role `@type: "JobPosting"` schemas with mandatory properties (`title`, `description`, `datePosted`, `validThrough`, `employmentType`, `hiringOrganization`, `jobLocation`, `baseSalary` hourly ranges, and `directApply: true`).
7. **Zero Funnel Drop-off (Eliminates Broken Loops):**
   * Replaces broken, self-referencing links with an inline 60-second mobile Quick-Apply form with interactive role selection, file upload dropzone, and direct HR fallback channels.
8. **3-Variant Meta Title, Description & H1 Generator:**
   * Produces Geo-Targeted Local SEO, Benefit-Driven E-E-A-T, and Action-Oriented Direct Apply copy variants.

---

## 📁 Repository Structure

```text
Career-Page-Builder/
├── SKILL.md                                 # AGY / IDE Skill Definition & Workflow
├── README.md                                # Documentation & Usage Guide
├── scripts/
│   ├── scrape_website.py                    # Autonomous Website Scraper
│   ├── extract_logo_palette.py              # PIL-based Logo Dual-Color Extractor
│   └── generate_career_page.py              # Standalone HTML & Schema Compiler
└── examples/
    ├── burnette_careers_sample.html         # ADU General Contractor (Burnette Construction)
    └── royal_custom_surfaces_sample.html    # Stone & Countertop Fabricator (Royal Custom Surfaces)
```

---

## ⚡ Quick Start

### 1. Scrape Any Website URL
```bash
python scripts/scrape_website.py --url "https://royalcustomsurfaces.com/" --out scraped_data.json
```

### 2. Extract Exact Logo Colors
```bash
python scripts/extract_logo_palette.py --logo "https://royalcustomsurfaces.com/wp-content/uploads/2025/12/Transparent-Background-RCS-Logo-1024x344.png"
```
*Output:*
```json
{
  "primary": "#BA862F",
  "secondary": "#C89B36"
}
```

### 3. Generate 100% Valid Careers Page

**Embed Mode (Default for WordPress / Elementor / Astra):**
```bash
python scripts/generate_career_page.py \
  --data scraped_data.json \
  --primary "#BA862F" \
  --secondary "#C89B36" \
  --mode embed \
  --out careers.html
```

**Standalone Mode (With Minimal Isolated Brand Top Bar):**
```bash
python scripts/generate_career_page.py \
  --data scraped_data.json \
  --primary "#BA862F" \
  --secondary "#C89B36" \
  --mode standalone \
  --out careers_standalone.html
```

---

## 📋 Google for Jobs Schema Compliance

Career Page Builder produces schemas fully validated against Schema.org and Google Search Central requirements:

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://royalcustomsurfaces.com/careers/#webpage",
      "url": "https://royalcustomsurfaces.com/careers/",
      "name": "Careers at Royal Custom Surfaces | Countertop & Stone Jobs Sacramento & Modesto, CA"
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://royalcustomsurfaces.com/careers/#breadcrumb",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://royalcustomsurfaces.com/" },
        { "@type": "ListItem", "position": 2, "name": "Careers" }
      ]
    },
    {
      "@type": "JobPosting",
      "@id": "https://royalcustomsurfaces.com/careers/#job-lead-fabricator",
      "title": "Lead Stone & Countertop Fabricator & Shop Foreman",
      "description": "<p>Full trade responsibilities, qualifications, and benefits...</p>",
      "datePosted": "2026-10-15T08:00:00-07:00",
      "validThrough": "2026-12-31T23:59:59-07:00",
      "employmentType": "FULL_TIME",
      "directApply": true,
      "hiringOrganization": {
        "@type": "Organization",
        "name": "Royal Custom Surfaces",
        "sameAs": "https://royalcustomsurfaces.com/",
        "logo": "https://royalcustomsurfaces.com/wp-content/uploads/2025/12/Transparent-Background-RCS-Logo-1024x344.png"
      },
      "jobLocation": {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "3830 Omec Cir #4",
          "addressLocality": "Rancho Cordova",
          "addressRegion": "CA",
          "postalCode": "95742",
          "addressCountry": "US"
        }
      },
      "baseSalary": {
        "@type": "MonetaryAmount",
        "currency": "USD",
        "value": {
          "@type": "QuantitativeValue",
          "minValue": 32.00,
          "maxValue": 48.00,
          "unitText": "HOUR"
        }
      }
    }
  ]
}
```

---

## 🛠️ WordPress / Elementor / Astra Integration

To embed onto a client WordPress page:
1. Create a new page in WordPress at `/careers/`.
2. Add an **HTML Element** (in Elementor, Gutenberg, or Beaver Builder).
3. Paste the generated HTML into the block.
4. Because the embed code adheres to the **Zero Header Conflict Mandate**, it will render seamlessly below your WordPress header and above your footer with zero duplicate menus, zero styling collisions, and full responsive fluid bounds.

---

## 📄 License
MIT License. Built for SEO and CRO high-converting recruitment workflows.
