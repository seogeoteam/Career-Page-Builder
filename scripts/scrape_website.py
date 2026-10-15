#!/usr/bin/env python3
"""
Career Page Builder - Autonomous Website Scraper
Ingests a single URL and extracts all brand, NAP, schema, and trade information.
"""

import argparse
import json
import re
import sys
import urllib.request
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

def scrape_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }
    
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Error fetching URL {url}: {e}", file=sys.stderr)
        return None

    soup = BeautifulSoup(html, 'html.parser')
    domain = urlparse(url).netloc
    base_url = f"{urlparse(url).scheme}://{domain}"

    data = {
        "url": url,
        "domain": domain,
        "title": soup.title.string.strip() if soup.title else "",
        "meta_description": "",
        "company_name": "",
        "logo_url": "",
        "phone": "",
        "email": "",
        "street_address": "",
        "locality": "",
        "region": "",
        "postal_code": "",
        "country": "US",
        "license_number": "",
        "founder": "",
        "founding_date": "",
        "rating_value": "",
        "rating_count": "",
        "google_kgmid": "",
        "google_cid": "",
        "bbb_url": "",
        "service_lines": [],
        "service_areas": [],
        "extracted_hex_colors": []
    }

    # Meta Tags
    for m in soup.find_all('meta'):
        name = (m.get('name') or m.get('property') or '').lower()
        content = m.get('content', '')
        if name in ['description', 'og:description']:
            if not data['meta_description']:
                data['meta_description'] = content
        elif name in ['og:site_name']:
            data['company_name'] = content

    # Check JSON-LD Schemas
    for s in soup.find_all('script', type='application/ld+json'):
        try:
            schema_json = json.loads(s.string)
            items = schema_json.get('@graph', [schema_json]) if isinstance(schema_json, dict) else schema_json
            if not isinstance(items, list):
                items = [items]
            
            for item in items:
                if not isinstance(item, dict):
                    continue
                t = str(item.get('@type', ''))
                
                # Organization / LocalBusiness / Contractor details
                if any(x in t for x in ['Organization', 'LocalBusiness', 'GeneralContractor', 'HomeAndConstructionBusiness', 'ProfessionalService']):
                    if item.get('name') and not data['company_name']:
                        data['company_name'] = item['name']
                    if item.get('telephone') and not data['phone']:
                        data['phone'] = item['telephone']
                    if item.get('email') and not data['email']:
                        data['email'] = item['email']
                    
                    addr = item.get('address')
                    if isinstance(addr, dict):
                        data['street_address'] = addr.get('streetAddress', data['street_address'])
                        data['locality'] = addr.get('addressLocality', data['locality'])
                        data['region'] = addr.get('addressRegion', data['region'])
                        data['postal_code'] = addr.get('postalCode', data['postal_code'])
                        data['country'] = addr.get('addressCountry', data['country'])
                    
                    logo = item.get('logo')
                    if isinstance(logo, dict):
                        data['logo_url'] = logo.get('url', data['logo_url'])
                    elif isinstance(logo, str) and not data['logo_url']:
                        data['logo_url'] = logo
                    
                    if item.get('foundingDate'):
                        data['founding_date'] = str(item['foundingDate'])
                    
                    founder = item.get('founder')
                    if isinstance(founder, dict):
                        data['founder'] = founder.get('name', data['founder'])
                    elif isinstance(founder, str):
                        data['founder'] = founder

                    same_as = item.get('sameAs', [])
                    if isinstance(same_as, list):
                        for link in same_as:
                            if 'kgmid=' in link:
                                data['google_kgmid'] = link.split('kgmid=')[-1]
                            if 'cid=' in link:
                                data['google_cid'] = link.split('cid=')[-1]
                            if 'bbb.org' in link:
                                data['bbb_url'] = link

        except Exception:
            continue

    # Regex search for phone, email, and licenses
    full_text = soup.get_text()
    if not data['phone']:
        phones = re.findall(r'\(?\b[0-9]{3}\)?[-.\s]?[0-9]{3}[-.\s]?[0-9]{4}\b', full_text)
        if phones:
            data['phone'] = phones[0]

    if not data['email']:
        emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', full_text)
        valid_emails = [e for e in emails if not any(x in e.lower() for x in ['png', 'jpg', 'wix', 'example', 'sentry'])]
        if valid_emails:
            data['email'] = valid_emails[0]

    license_match = re.search(r'(CSLB|Lic|License|Red Seal)[\s#:]{1,5}([A-Z0-9-]{5,12})', full_text, re.IGNORECASE)
    if license_match:
        data['license_number'] = f"{license_match.group(1).upper()} #{license_match.group(2)}"

    # Logo Fallback
    if not data['logo_url']:
        for img in soup.find_all('img'):
            src = img.get('src') or img.get('data-src') or img.get('data-lazy-src') or ''
            alt = img.get('alt', '')
            cls = str(img.get('class', ''))
            if any(k in (src + alt + cls).lower() for k in ['logo', 'brand']):
                data['logo_url'] = urljoin(base_url, src)
                break

    # Discover Service Lines from Nav / Links
    for a in soup.find_all('a'):
        href = a.get('href', '')
        txt = a.get_text(strip=True)
        if 4 < len(txt) < 35 and any(w in href.lower() for w in ['service', 'remodel', 'construction', 'repair', 'installation', 'build']):
            if txt not in data['service_lines'] and not any(x in txt.lower() for x in ['home', 'contact', 'about', 'blog', 'privacy']):
                data['service_lines'].append(txt)

    # Detect Dominant Hex Colors in CSS/Inline
    hex_colors = set(re.findall(r'#(?:[0-9a-fA-F]{3}){1,2}\b', html))
    data['extracted_hex_colors'] = sorted(list(hex_colors))[:20]

    return data

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Scrape website data for Career Page Builder')
    parser.add_argument('--url', required=True, help='Website URL to scrape')
    parser.add_argument('--out', default='', help='Optional output JSON file')
    args = parser.parse_args()

    scraped = scrape_url(args.url)
    if scraped:
        output_str = json.dumps(scraped, indent=2)
        if args.out:
            with open(args.out, 'w', encoding='utf-8') as f:
                f.write(output_str)
            print(f"Scraped data written to {args.out}")
        else:
            print(output_str)
