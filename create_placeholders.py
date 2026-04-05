"""
U Stop Liquor - Generate Professional Placeholder Images
Creates SVG-based product images for quick visual setup
"""

import json
import os
from pathlib import Path

json_file = 'd:\\VS_Code2\\U_Stop_Liquor\\U_Stop_Liquor\\assets\\data\\inventory.json'
images_dir = 'd:\\VS_Code2\\U_Stop_Liquor\\U_Stop_Liquor\\assets\\images'

# Category colors
category_colors = {
    'Beer': '#D4A574',
    'Spirits': '#8B4513',
    'Mixers': '#FFD700',
    'Liqueurs': '#8B0000'
}

def sanitize_filename(name):
    name = name.lower().replace(' ', '-').replace("'", "").replace('"', '')
    for char in ['/', '\\', ':', '*', '?', '<', '>', '|']:
        name = name.replace(char, '-')
    while '--' in name:
        name = name.replace('--', '-')
    return name.strip('-')

def create_placeholder(product_name, category):
    """Create SVG placeholder image"""
    color = category_colors.get(category, '#D4AF37')
    
    # Escape product name for XML
    safe_name = product_name.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="200" height="300" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <rect width="200" height="300" fill="#f5f5f5"/>
  
  <!-- Bottle shape -->
  <ellipse cx="100" cy="80" rx="25" ry="30" fill="{color}"/>
  <rect x="80" y="110" width="40" height="100" fill="{color}"/>
  <ellipse cx="100" cy="210" rx="35" ry="20" fill="{color}"/>
  
  <!-- Bottle shine -->
  <ellipse cx="90" cy="100" rx="8" ry="40" fill="white" opacity="0.3"/>
  
  <!-- Label -->
  <rect x="75" y="140" width="50" height="40" fill="white" stroke="#999" stroke-width="1"/>
  <text x="100" y="168" font-size="8" text-anchor="middle" fill="#333" font-weight="bold">
    {safe_name[:15]}
  </text>
  
  <!-- Category -->
  <rect x="75" y="190" width="50" height="15" fill="{color}" opacity="0.5"/>
  <text x="100" y="200" font-size="8" text-anchor="middle" fill="white">
    {category}
  </text>
</svg>'''
    return svg

try:
    # Load inventory
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    products = data['products']
    
    print("🎨 CREATING PLACEHOLDER IMAGES")
    print("="*60)
    
    # Get unique products
    unique_products = {}
    for p in products:
        if p['name'] not in unique_products:
            unique_products[p['name']] = p
    
    Path(images_dir).mkdir(parents=True, exist_ok=True)
    
    created = 0
    skipped = 0
    
    for product_name, product in sorted(unique_products.items()):
        filename = sanitize_filename(product_name) + '.svg'
        filepath = os.path.join(images_dir, filename)
        
        if os.path.exists(filepath):
            skipped += 1
            continue
        
        svg_content = create_placeholder(product_name, product['category'])
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        
        created += 1
        
        if created % 500 == 0:
            print(f"  Created: {created} images...")
    
    print(f"\n{'='*60}")
    print(f"✅ Created: {created} placeholder images")
    print(f"⏭️  Already existed: {skipped}")
    print(f"\n📁 Location: {images_dir}")
    print(f"🎨 All products now have visual placeholders!")
    print(f"\n💡 Next step: Replace placeholders with real product images")
    print(f"   as you source them from:")
    print(f"   • Google Images (search: 'product name bottle')")
    print(f"   • Brand websites (official product images)")
    print(f"   • Stock photo sites (Unsplash, Pexels, etc.)")

except Exception as e:
    print(f"❌ Error: {str(e)}")
