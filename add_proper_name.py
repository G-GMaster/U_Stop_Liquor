import csv
import re

csv_file = 'd:\\VS_Code2\\U_Stop_L\\inventory.csv'

def create_proper_name(name, upc):
    """
    Creates a proper product name for liquor inventory
    """
    if not name or name.strip() == '':
        return ''
    
    name = name.strip()
    
    # Remove extra quotes and special characters
    name = name.replace('="', '').replace('"', '')
    
    # Known brand mappings to proper case
    brand_mappings = {
        'budlight': 'Bud Light',
        'budweiser': 'Budweiser',
        'heineken': 'Heineken',
        'stella': 'Stella Artois',
        'corona': 'Corona Extra',
        'cass': 'Cass',
        'villon': 'Villon',
        'cognac': 'Cognac',
        'plantery': 'Plantery',
        'diplomatico': 'Diplomatico',
        'old monk': 'Old Monk',
        'martini': 'Martini & Rossi',
        'fanta': 'Fanta',
        'sprite': 'Sprite',
        'coca cola': 'Coca-Cola',
        'pepsi': 'Pepsi',
        'mountain dew': 'Mountain Dew',
        'aquafina': 'Aquafina',
        'fafda': 'Fafda',
        'pelon': 'Pelon',
        'labubu': 'Labubu',
        'halls': 'Halls',
        'halls uva': 'Halls Uva',
        'vaseline': 'Vaseline',
        'glow stick': 'Glow Stick',
        'rhino': 'Rhino',
        'kittykat': 'Kitty Kat',
        'reeds': 'Reed\'s',
        'zig zag': 'Zig Zag',
        'jolly rancher': 'Jolly Rancher',
        'payday': 'PayDay',
        'tic tac': 'Tic Tac',
        'kinder': 'Kinder',
        'nutella': 'Nutella',
        'ferrero': 'Ferrero Rocher',
        'baileys': 'Baileys',
        'cointreau': 'Cointreau',
        'tanqueray': 'Tanqueray',
        'johnnie walker': 'Johnnie Walker',
        'bacardi': 'Bacardi',
        'rum': 'Rum',
        'vodka': 'Vodka',
        'whiskey': 'Whiskey',
        'gin': 'Gin',
        'cabernet': 'Cabernet Sauvignon',
        'pinot grigio': 'Pinot Grigio',
        'moscato': 'Moscato',
        'champagne': 'Champagne',
        'vermouth': 'Vermouth',
    }
    
    # Convert to lowercase for processing
    name_lower = name.lower()
    
    # Apply brand mappings
    for key, proper in brand_mappings.items():
        if key in name_lower:
            name = name_lower.replace(key, proper.lower())
            break
    
    # Standardize common abbreviations and terms
    replacements = {
        r'\bvsop\b': 'VSOP',
        r'\bxo\b': 'XO',
        r'\bml\b': 'ml',
        r'\boz\b': 'Oz',
        r'\box\b': 'Oz',
        r'\bfl oz\b': 'fl oz',
        r'\bfloz\b': 'fl oz',
        r'\bpk\b': 'Pack',
        r'\bpacks?\b': 'Pack',
        r'\b6pk\b': '6-Pack',
        r'\b12pk\b': '12-Pack',
        r'\b4pk\b': '4-Pack',
        r'\bcans?\b': 'Cans',
        r'\bcans?\b': 'Cans',
        r'\bbottle\b': 'Bottle',
        r'\bbottles?\b': 'Bottle',
        r'\bcan\b': 'Can',
        r'\b2l\b': '2L',
        r'\b750\b': '750ml',
        r'\b375\b': '375ml',
        r'\b50ml\b': '50ml',
        r'\b500ml\b': '500ml',
        r'\b1l\b': '1L',
        r'\b1\.5l\b': '1.5L',
        r'\bking\b': 'King',
        r'\b100s\b': '100s',
        r'\bblue\b': 'Blue',
        r'\bred\b': 'Red',
        r'\bgreen\b': 'Green',
        r'\bmenthol\b': 'Menthol',
        r'\bgold\b': 'Gold',
        r'\bsilver\b': 'Silver',
        r'\borange\b': 'Orange',
        r'\bblack\b': 'Black',
        r'\bwhite\b': 'White',
        r'\boriginal\b': 'Original',
        r'\bfresh\b': 'Fresh',
        r'\bpremium\b': 'Premium',
    }
    
    # Apply replacements
    for pattern, replacement in replacements.items():
        name = re.sub(pattern, replacement, name, flags=re.IGNORECASE)
    
    # Title case with special handling
    words = name.split()
    proper_words = []
    
    for word in words:
        word = word.strip()
        if not word:
            continue
        
        # Keep all caps for abbreviations
        if len(word) <= 2 and word.isupper():
            proper_words.append(word)
        # Check if it's already proper (like VSOP, XO, MLML, etc.)
        elif word.isupper() and len(word) <= 4:
            proper_words.append(word)
        # Otherwise title case
        else:
            proper_words.append(word.capitalize())
    
    proper_name = ' '.join(proper_words)
    
    # Fix common spacing issues
    proper_name = proper_name.replace(' - ', '-')
    proper_name = re.sub(r'\s+', ' ', proper_name)  # Remove multiple spaces
    
    return proper_name.strip()


# Read CSV and add proper name column
rows = []
headers = []

try:
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        
        # Find the position of 'Name' column
        name_index = headers.index('Name')
        
        for row in reader:
            name = row.get('Name', '')
            upc = row.get('Upc', '')
            
            # Create proper name
            proper_name = create_proper_name(name, upc)
            
            rows.append((row, proper_name))
    
    # Insert 'proper Name' column right after 'Name'
    new_headers = list(headers)
    new_headers.insert(name_index + 1, 'proper Name')
    
    # Write back to CSV with new column
    with open(csv_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=new_headers)
        writer.writeheader()
        
        for row, proper_name in rows:
            new_row = dict(row)
            new_row['proper Name'] = proper_name
            
            # Reorder to match new headers
            reordered = {k: new_row.get(k, '') for k in new_headers}
            writer.writerow(reordered)
    
    print(f'✅ Successfully added "proper Name" column!')
    print(f'📁 Updated: {csv_file}')
    print(f'\n📊 Sample conversions:')
    
    # Show some examples
    count = 0
    for row, proper_name in rows:
        if row.get('Name', '').strip() and count < 10:
            original = row.get('Name', '').replace('="', '').replace('"', '')
            print(f'  "{original}" → "{proper_name}"')
            count += 1

except Exception as e:
    print(f'❌ Error: {str(e)}')
