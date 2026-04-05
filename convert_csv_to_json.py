import csv
import json

# Read CSV file
csv_file = 'd:\\VS_Code2\\U_Stop_Liquor\\U_Stop_Liquor\\Inventory.csv'
json_file = 'd:\\VS_Code2\\U_Stop_Liquor\\U_Stop_Liquor\\assets\\data\\inventory.json'

products = []
product_id = 1

# List of liquor/beverage departments to include
liquor_departments = ['Beer', 'Liquor ', 'Soda & Drink\'s']

try:
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            # Skip empty rows and non-liquor items
            # Use "proper Name" if available, otherwise fall back to "Name"
            name = row.get('proper Name', row.get('Name', '')).strip()
            department = row.get('Department', '').strip()
            price_cents = row.get('cents', '0').strip()
            size = row.get('size', '').strip()
            
            # Skip if no name or not in liquor departments
            if not name or department not in liquor_departments:
                continue
            
            # Skip items with missing critical data
            if not price_cents or price_cents == '0':
                continue
            
            try:
                price = float(price_cents) / 100  # Convert cents to dollars
            except:
                continue
            
            # Determine category based on department
            if department == 'Beer':
                category = 'Beer'
                type_val = 'Beer'
            elif department == 'Liquor ':
                category = 'Spirits'
                type_val = 'Spirit'
            elif department == 'Soda & Drink\'s':
                category = 'Mixers'
                type_val = 'Beverage'
            else:
                continue
            
            # Create product object with ALL CSV fields
            product = {
                # Display/Website Fields
                'id': product_id,
                'name': name,
                'category': category,
                'type': type_val,
                'size': size if size else 'Standard',
                'quantity': 'Single Unit',
                'price': round(price, 2),
                'sku': row.get('Upc', f'SKU-{product_id}').replace('="', '').replace('"', ''),
                'image': f'{name.lower().replace(" ", "-")}.jpg',
                'description': f'{name} - {category}',
                
                # POS System Fields (from CSV)
                'upc': row.get('Upc', '').replace('="', '').replace('"', ''),
                'department': row.get('Department', '').strip(),
                'qty': int(row.get('qty', 0)) if row.get('qty', '0').isdigit() else 0,
                'cents': int(row.get('cents', 0)) if row.get('cents', '0').isdigit() else 0,
                'incltaxes': row.get('incltaxes', 'n').strip(),
                'inclfees': row.get('inclfees', 'n').strip(),
                'proper_name': row.get('proper Name', '').strip(),
                'ebt': row.get('ebt', 'n').strip(),
                'byweight': row.get('byweight', 'n').strip(),
                'fee_multiplier': float(row.get('Fee Multiplier', 1)) if row.get('Fee Multiplier', '1').replace('.','',1).isdigit() else 1,
                'cost_qty': int(row.get('cost_qty', 1)) if row.get('cost_qty', '1').isdigit() else 1,
                'cost_cents': int(row.get('cost_cents', 0)) if row.get('cost_cents', '0').isdigit() else 0,
                'variable_price': row.get('variable_price', 'n').strip(),
                'addstock': int(row.get('addstock', 0)) if row.get('addstock', '0').isdigit() else 0,
                'setstock': int(row.get('setstock', 0)) if row.get('setstock', '0').isdigit() else 0,
                'pack_name': row.get('pack_name', '').strip(),
                'pack_qty': int(row.get('pack_qty', 0)) if row.get('pack_qty', '0').isdigit() else 0,
                'pack_upc': row.get('pack_upc', '').strip(),
                'unit_upc': row.get('unit_upc', '').strip(),
                'unit_count': int(row.get('unit_count', 0)) if row.get('unit_count', '0').isdigit() else 0,
                'is_oneclick': row.get('is_oneclick', 'n').strip(),
                'oc_color': row.get('oc_color', '').strip(),
                'oc_border_color': row.get('oc_border_color', '').strip(),
                'oc_text_color': row.get('oc_text_color', '').strip(),
                'oc_fixedpos': row.get('oc_fixedpos', '').strip(),
                'oc_page': row.get('oc_page', '').strip(),
                'oc_key': row.get('oc_key', '').strip(),
                'oc_relpos': row.get('oc_relpos', '').strip()
            }
            
            products.append(product)
            product_id += 1

    # Create JSON structure
    data = {
        'store': {
            'name': 'U Stop Liquor',
            'description': 'Your one-stop destination for premium beverages and spirits'
        },
        'categories': ['Beer', 'Spirits', 'Mixers', 'Liqueurs'],
        'products': products
    }
    
    # Write JSON file
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f'✅ Successfully converted {len(products)} products to JSON!')
    print(f'📁 Saved to: {json_file}')
    print(f'\nProducts by category:')
    
    # Count by category
    categories_count = {}
    for product in products:
        cat = product['category']
        categories_count[cat] = categories_count.get(cat, 0) + 1
    
    for cat, count in sorted(categories_count.items()):
        print(f'  - {cat}: {count} products')

except Exception as e:
    print(f'❌ Error: {str(e)}')
