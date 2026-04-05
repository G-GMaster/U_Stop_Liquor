"""
U Stop Liquor - Automated Image Downloader
Downloads product images from Bing Image Search
"""

import json
import os
import urllib.request
import time
from pathlib import Path

# Configuration
json_file = 'd:\\VS_Code2\\U_Stop_Liquor\\U_Stop_Liquor\\assets\\data\\inventory.json'
images_dir = 'd:\\VS_Code2\\U_Stop_Liquor\\U_Stop_Liquor\\assets\\images'
download_limit = 50  # Download first 50 unique products

# Create images directory
Path(images_dir).mkdir(parents=True, exist_ok=True)

def sanitize_filename(name):
    """Convert product name to safe filename"""
    name = name.lower()
    name = name.replace(' ', '-')
    name = name.replace("'", "").replace('"', '')
    for char in ['/', '\\', ':', '*', '?', '<', '>', '|']:
        name = name.replace(char, '-')
    while '--' in name:
        name = name.replace('--', '-')
    return name.strip('-') + '.jpg'

try:
    from bing_image_downloader import downloader
    
    # Load inventory
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    products = data['products']
    
    print(f"📦 U STOP LIQUOR - DOWNLOADING IMAGES")
    print(f"{'='*60}")
    
    # Get unique products
    unique_products = {}
    for p in products:
        if p['name'] not in unique_products:
            unique_products[p['name']] = p
    
    total = min(download_limit, len(unique_products))
    downloaded = 0
    skipped = 0
    
    print(f"Found {len(unique_products)} unique products")
    print(f"Downloading {total} products...\n")
    
    for idx, (product_name, product) in enumerate(list(unique_products.items())[:total]):
        filename = sanitize_filename(product_name)
        filepath = os.path.join(images_dir, filename)
        
        # Skip if exists
        if os.path.exists(filepath):
            skipped += 1
            continue
        
        try:
            # Clean temp folder
            import shutil
            temp_dir = "temp_images"
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir)
            
            # Download
            downloader.download(
                query=product_name + " bottle",
                limit=1,
                output_dir=temp_dir,
                adult_filter_off=True,
                force_replace=True,
                timeout=10,
                verbose=False
            )
            
            # Find and move downloaded file
            for root, dirs, files in os.walk(temp_dir):
                for file in files:
                    if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                        src = os.path.join(root, file)
                        dest = filepath
                        os.makedirs(os.path.dirname(dest), exist_ok=True)
                        os.rename(src, dest)
                        downloaded += 1
                        break
            
            # Clean up
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir)
            
            # Progress
            if (idx + 1) % 10 == 0:
                print(f"  Progress: {idx + 1}/{total} ({downloaded} downloaded)")
            
            time.sleep(0.5)  # Be nice to the server
        
        except Exception as e:
            pass  # Silently skip failed downloads
    
    print(f"\n{'='*60}")
    print(f"✅ Downloaded: {downloaded} images")
    print(f"⏭️  Already existed: {skipped}")
    print(f"📁 Location: {images_dir}")
    print(f"\n🌐 Refresh website to see new images!")

except ImportError:
    print("❌ bing-image-downloader not found")
    print("Install with: pip install bing-image-downloader")
except Exception as e:
    print(f"❌ Error: {str(e)}")
