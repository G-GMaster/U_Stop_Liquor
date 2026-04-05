import json

# Load inventory
json_file = 'd:\\VS_Code2\\U_Stop_Liquor\\U_Stop_Liquor\\assets\\data\\inventory.json'

try:
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    products = data['products']
    
    print(f"=== U STOP LIQUOR - IMAGE FILES NEEDED ===\n")
    print(f"Total products: {len(products)}")
    print(f"Total unique images needed: {len(set(p['image'] for p in products))}\n")
    
    print("Save images to: assets/images/\n")
    print("Image filenames needed:\n")
    
    # Get unique images and sort
    image_files = sorted(set(p['image'] for p in products))
    
    # Group by category
    categories = {}
    for product in products:
        cat = product['category']
        if cat not in categories:
            categories[cat] = []
        if product['image'] not in categories[cat]:
            categories[cat].append(product['image'])
    
    # Print by category
    for cat in sorted(categories.keys()):
        print(f"\n--- {cat.upper()} ({len(categories[cat])} images) ---")
        for img in sorted(categories[cat]):
            print(f"  ✓ {img}")
    
    # Generate a download list
    print("\n\n=== QUICK REFERENCE LIST ===")
    print("Copy-paste these filenames for your image folder:\n")
    for img in image_files[:20]:  # Show first 20
        print(img)
    
    if len(image_files) > 20:
        print(f"... and {len(image_files) - 20} more")
    
    # Save to file
    with open('d:\\VS_Code2\\U_Stop_Liquor\\U_Stop_Liquor\\IMAGE_FILES_NEEDED.txt', 'w') as f:
        for img in image_files:
            f.write(img + '\n')
    
    print(f"\n✅ Full list saved to: IMAGE_FILES_NEEDED.txt")

except Exception as e:
    print(f"❌ Error: {str(e)}")
