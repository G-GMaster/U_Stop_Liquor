# Excel to JSON Conversion Guide

## Quick Method (Recommended)

### Step 1: Export Excel as CSV

1. Open your Excel inventory file
2. Click **File** → **Save As**
3. Choose format: **CSV (Comma delimited) (.csv)**
4. Save it (e.g., `inventory.csv`)

### Step 2: Convert CSV to JSON Online

1. Go to: **https://www.convertcsv.com/csv-to-json.htm**
2. Click "Choose File" and upload your `inventory.csv`
3. Click "Convert"
4. Copy the JSON output
5. Replace contents of `assets/data/inventory.json` with the output

### Step 3: Update & Deploy

1. Edit the JSON if needed (see format below)
2. Commit changes: `git add . && git commit -m "Updated inventory" && git push`
3. Done! Your website updates automatically in a few seconds

---

## JSON Format Required

The JSON must follow this structure:

```json
{
  "store": {
    "name": "U Stop Liquor",
    "description": "Your store description"
  },
  "categories": ["Beer", "Wine", "Spirits", "Mixers", "Liqueurs"],
  "products": [
    {
      "id": 1,
      "name": "Product Name",
      "category": "Beer",
      "type": "Product Type (e.g., Lager, IPA)",
      "size": "12 oz",
      "quantity": "6-Pack",
      "price": 8.99,
      "sku": "CODE-12OZ-6PK",
      "image": "filename.jpg",
      "description": "Optional product description"
    }
  ]
}
```

### Required Fields:
- `id` - Unique product identifier (number)
- `name` - Product name (string)
- `category` - Must match one in categories array (string)
- `type` - Specific type/style (string)
- `size` - Bottle/can/package size (string)
- `quantity` - Package quantity (string)
- `price` - Price in dollars (number, e.g., 8.99)
- `sku` - Stock keeping unit code (string)
- `image` - Filename in assets/images/ (string)
- `description` - Optional product description (string)

---

## Excel Column Headers

Your Excel file should have these columns (in any order):

| id | name | category | type | size | quantity | price | sku | image | description |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Corona Extra | Beer | Lager | 12 oz | 12-Pack | 15.99 | COR-12OZ-12PK | corona.jpg | Crisp lager |
| 2 | Heineken | Beer | Pilsner | 12 oz | 6-Pack | 8.99 | HEI-12OZ-6PK | heineken.jpg | Premium pilsner |

---

## Manual Editing

If you need to manually edit the JSON:

1. Open `assets/data/inventory.json` in VS Code
2. You can:
   - Add new products (copy a product object and modify)
   - Edit existing products (change values)
   - Add new categories (update categories array, then use in products)
   - Delete products (remove the entire product object)

3. **Important:** Keep JSON syntax valid
   - Use commas between list items
   - No trailing commas (last item in array/object shouldn't have comma)
   - Wrap strings in double quotes

4. Save and commit:
   ```powershell
   git add assets/data/inventory.json
   git commit -m "Updated product information"
   git push
   ```

---

## Validating JSON

Before deploying, validate your JSON:

1. Go to: **https://jsonlint.com**
2. Paste your JSON
3. Click **"Validate JSON"**
4. If it shows "Valid JSON", you're good!
5. If there are errors, fix them using the error hints

---

## Example CSV Format

Save this as `inventory.csv` and convert:

```
id,name,category,type,size,quantity,price,sku,image,description
1,Corona Extra,Beer,Lager,12 oz,12-Pack,15.99,COR-12OZ-12PK,corona.jpg,Crisp refreshing lager
2,Heineken,Beer,Pilsner,12 oz,6-Pack,8.99,HEI-12OZ-6PK,heineken.jpg,Premium Dutch pilsner
3,Cabernet Sauvignon,Wine,Red Wine,750 ml,Single Bottle,24.99,CAB-750ML-RED,cabernet.jpg,Full-bodied red wine
```

---

## Troubleshooting

### "Invalid JSON" error?
- Use https://jsonlint.com to find the exact error
- Check for:
  - Missing commas between items
  - Trailing commas (last item shouldn't have comma)
  - Unclosed brackets or quotes
  - Special characters not escaped

### Products not showing on website?
- Verify `inventory.json` is in `assets/data/` folder
- Check JSON is valid with jsonlint.com
- Verify `category` values match the categories array exactly
- Check browser console (F12) for errors

### Images not displaying?
- Image files must be in `assets/images/` folder
- Filename in JSON must match file exactly (case-sensitive)
- Use relative path: `filename.jpg` (not full path)

---

## Automated Conversion Tools (Advanced)

If you have programming experience, you can automate this:

### Python Script
```python
import csv
import json

csv_file = 'inventory.csv'
json_file = 'inventory.json'

data = {
    "store": {
        "name": "U Stop Liquor",
        "description": "Your one-stop destination for premium beverages"
    },
    "categories": ["Beer", "Wine", "Spirits", "Mixers", "Liqueurs"],
    "products": []
}

with open(csv_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        row['id'] = int(row['id'])
        row['price'] = float(row['price'])
        data['products'].append(row)

with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Converted {len(data['products'])} products to JSON!")
```

### Node.js Script
```javascript
const fs = require('fs');
const csv = require('csv-parser');

const products = [];

fs.createReadStream('inventory.csv')
  .pipe(csv())
  .on('data', (row) => {
    row.id = parseInt(row.id);
    row.price = parseFloat(row.price);
    products.push(row);
  })
  .on('end', () => {
    const data = {
      store: {
        name: "U Stop Liquor",
        description: "Your one-stop destination for premium beverages"
      },
      categories: ["Beer", "Wine", "Spirits", "Mixers", "Liqueurs"],
      products: products
    };
    
    fs.writeFileSync('assets/data/inventory.json', JSON.stringify(data, null, 2));
    console.log(`Converted ${products.length} products!`);
  });
```

---

## Need Help?

- **Validator:** https://jsonlint.com
- **CSV to JSON:** https://www.convertcsv.com/csv-to-json.htm
- **Excel Help:** Microsoft Excel documentation
- **JSON Format:** https://www.json.org

Good luck! 🎉
