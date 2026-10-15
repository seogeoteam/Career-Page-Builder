#!/usr/bin/env python3
"""
Career Page Builder - Logo Dual-Color Palette Extractor
Inspects a logo image URL or local path and extracts exact Primary and Secondary hex colors.
"""

import argparse
import io
import json
import sys
import urllib.request
from PIL import Image

def extract_colors(image_path_or_url):
    try:
        if image_path_or_url.startswith(('http://', 'https://')):
            req = urllib.request.Request(
                image_path_or_url,
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            with urllib.request.urlopen(req, timeout=15) as resp:
                raw_data = resp.read()
            im = Image.open(io.BytesIO(raw_data)).convert('RGBA')
        else:
            im = Image.open(image_path_or_url).convert('RGBA')
    except Exception as e:
        print(f"Error opening image: {e}", file=sys.stderr)
        return {"primary": "#02349A", "secondary": "#F5A11C"}

    # Resize to speed up calculation
    im.thumbnail((150, 150))
    colors = im.getcolors(maxcolors=100000) or []
    sorted_colors = sorted(colors, key=lambda x: x[0], reverse=True)

    candidates = []
    for count, (r, g, b, a) in sorted_colors:
        # Ignore fully transparent pixels
        if a < 60:
            continue
        # Ignore near-white and near-black
        if (r > 240 and g > 240 and b > 240) or (r < 25 and g < 25 and b < 25):
            continue
        
        hex_c = f"#{r:02X}{g:02X}{b:02X}"
        if hex_c not in candidates:
            candidates.append(hex_c)

    if not candidates:
        return {"primary": "#02349A", "secondary": "#F5A11C"}

    # Assign primary and secondary
    primary = candidates[0]
    secondary = candidates[1] if len(candidates) > 1 else "#F5A11C"

    return {
        "primary": primary,
        "secondary": secondary,
        "all_extracted": candidates[:6]
    }

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract primary & secondary colors from logo')
    parser.add_argument('--logo', required=True, help='Logo URL or local image path')
    args = parser.parse_args()

    palette = extract_colors(args.logo)
    print(json.dumps(palette, indent=2))
