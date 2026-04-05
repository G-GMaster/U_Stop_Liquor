# U Stop Liquor - Website

A modern, responsive e-commerce website for U Stop Liquor featuring a searchable, filterable product inventory.

## Features

✅ **Responsive Design** - Works on mobile, tablet, and desktop  
✅ **Search & Filter** - Find products by name, type, size, price, or category  
✅ **Sort Options** - Sort by name (A-Z, Z-A) or price (low-to-high, high-to-low)  
✅ **Product Cards** - Display product details with images, prices, and SKUs  
✅ **Featured Categories** - Homepage displays all beverage categories  
✅ **Modern UI** - Clean design with black, white, deep red, and gold color scheme  
✅ **GitHub Pages Ready** - Deploy for free with no server needed  

## Project Structure

```
U_Stop_L/
├── index.html                  # Homepage
├── inventory.html              # Products page
├── css/
│   └── styles.css             # All styling
├── js/
│   └── script.js              # Functionality (search, filter, sort)
├── assets/
│   ├── images/                # Product and category images
│   └── data/
│       └── inventory.json     # Product inventory data
├── .gitignore                 # Git ignore rules
├── DEPLOYMENT_GUIDE.md        # Full deployment instructions
└── README.md                  # This file
```

## Quick Start

### Run Locally

1. **Using Direct Browser:**
   - Simply open `index.html` in your web browser

2. **Using Local Web Server (Recommended):**

   **Windows (PowerShell):**
   ```powershell
   cd d:\VS_Code2\U_Stop_L\U_Stop_L
   python -m http.server 8000
   # Visit: http://localhost:8000
   ```

   **Mac/Linux:**
   ```bash
   cd ~/path/to/U_Stop_L
   python3 -m http.server 8000
   # Visit: http://localhost:8000
   ```

   **Alternative (Python 2):**
   ```powershell
   python -m SimpleHTTPServer 8000
   ```

3. **Update inventory:**
   - Edit `assets/data/inventory.json` directly
   - Or regenerate from CSV: `python convert_csv_to_json.py`

4. **Add product images:**
   - Place images in `assets/images/`
   - Update filenames in `inventory.json`

---

## Deploy to Internet (Free with GitHub Pages)

### Quick Deploy (One-Time Setup)

#### **Step 1: Create GitHub Repository**
1. Go to [GitHub.com](https://github.com) and sign in
2. Click **"+"** → **"New repository"**
3. Name it: `u-stop-liquor`
4. Select **Public**
5. Click **"Create repository"**

#### **Step 2: Upload Files (Choose One Method)**

**Method A: Using Git Command (Recommended)**
```powershell
cd d:\VS_Code2\U_Stop_L\U_Stop_L
git init
git add .
git commit -m "Initial commit - U Stop Liquor website"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/u-stop-liquor.git
git push -u origin main
```

**Method B: Drag & Drop on GitHub**
1. On your repository, click **"uploading an existing file"**
2. Drag all files from your `U_Stop_L` folder
3. Commit changes

#### **Step 3: Enable GitHub Pages**
1. Go to repository → **Settings**
2. Scroll to **"Pages"**
3. Set **Source** = `"Deploy from a branch"`
4. Set **Branch** = `main / root`
5. Click **Save**
6. Site URL: `https://YOUR_USERNAME.github.io/u-stop-liquor/`

#### **Step 4 (Optional): Connect Custom Domain**
- See `DEPLOYMENT_GUIDE.md` for GoDaddy domain setup instructions

---

### Update Site After Launch

**Update Products:**
```powershell
# 1. Edit your Inventory.csv in Excel or your POS system
# 2. Export as CSV
# 3. Regenerate JSON:
python convert_csv_to_json.py

# 4. Push changes to GitHub:
git add assets/data/inventory.json
git commit -m "Update inventory"
git push origin main
```

**Changes go live in 1-2 minutes!**

## Updating Inventory

### From Excel/CSV File (Recommended for POS Systems)

1. **Export your POS inventory as CSV** with these columns:
   ```
   Upc, Department, qty, cents, Name, proper Name, size, ebt, byweight, 
   Fee_Multiplier, cost_qty, cost_cents, variable_price, addstock, setstock,
   pack_name, pack_qty, pack_upc, unit_upc, unit_count, is_oneclick,
   oc_color, oc_border_color, oc_text_color, oc_fixedpos, oc_page, oc_key, oc_relpos
   ```

2. **Save as** `Inventory.csv` in the project root

3. **Run conversion:**
   ```powershell
   python convert_csv_to_json.py
   ```
   This creates `assets/data/inventory.json` automatically

4. **Verify output:**
   - Check console for "Successfully converted X products"
   - Products appear in website automatically

### Edit JSON Directly (For Quick Changes)

Edit `assets/data/inventory.json` manually:

```json
{
  "id": 15,
  "name": "Product Name",
  "category": "Beer",
  "type": "IPA",
  "size": "12 oz",
  "quantity": "6-Pack",
  "price": 9.99,
  "sku": "CODE-12OZ-6PK",
  "image": "product.jpg",
  "description": "Product description"
}
```

**Available Categories:**
- Beer
- Spirits
- Mixers
- Liqueurs

## Features Explained

### Search
- Search by product name, type, or SKU
- Real-time search results

### Filters
- **Category** - Filter by beverage type
- **Size** - Filter by bottle/package size
- **Price Range** - Set min and max price

### Sort
- Name A→Z or Z→A
- Price Low→High or High→Low

### Add to Cart
- Click "Add to Cart" on any product
- Placeholder alert (can be extended with full cart system)

## Customization

### Change Colors
Edit `css/styles.css`:
```css
:root {
  --primary-black: #1a1a1a;
  --primary-red: #8b0000;
  --gold: #d4af37;
  --white: #ffffff;
}
```

### Change Store Name
- `index.html` - Update logo and titles
- `inventory.html` - Update page titles
- `inventory.json` - Update store name in "store" object

### Add New Categories
- Add to `inventory.json` → "categories" array
- Add products with the new category
- Filter dropdowns auto-populate

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## Performance

- **Lightweight:** No external dependencies
- **Fast Loading:** Optimized CSS and JavaScript
- **Mobile-Optimized:** Responsive grid layouts
- **GitHub Pages:** Free, fast CDN delivery

## Deployment

See `DEPLOYMENT_GUIDE.md` for complete instructions on:
1. Uploading to GitHub
2. Enabling GitHub Pages
3. Connecting your GoDaddy domain

## CSV to JSON Conversion Script

The `convert_csv_to_json.py` script automatically converts your POS inventory CSV to the website JSON format.

### What It Does:
- **Reads:** `Inventory.csv` (any POS export format)
- **Filters:** Beer, Liquor, and Soda/Drinks departments only
- **Converts:** Prices from cents to dollars
- **Generates:** `assets/data/inventory.json` with all POS fields preserved
- **Outputs:** Summary report (products per category)

### Supported CSV Headers (all optional):
```
Upc, Department, qty, cents, incltaxes, inclfees, Name, proper Name, 
size, ebt, byweight, Fee_Multiplier, cost_qty, cost_cents, variable_price,
addstock, setstock, pack_name, pack_qty, pack_upc, unit_upc, unit_count,
is_oneclick, oc_color, oc_border_color, oc_text_color, oc_fixedpos, 
oc_page, oc_key, oc_relpos
```

### Run the Script:
```powershell
cd d:\VS_Code2\U_Stop_L\U_Stop_L
python convert_csv_to_json.py
```

Output:
```
✅ Successfully converted 3357 products to JSON!
📁 Saved to: d:\VS_Code2\U_Stop_L\U_Stop_L\assets\data\inventory.json

Products by category:
  - Beer: 1781 products
  - Mixers: 1576 products
```

---

## Manage Inventory

### Update from POS System:
1. Export new CSV from your POS
2. Replace `Inventory.csv`
3. Run: `python convert_csv_to_json.py`
4. Commit & push (if deployed)

### Update Single Product on Website:
1. Open `assets/data/inventory.json`
2. Find the product by ID or name
3. Edit price, description, image, etc.
4. Save file
5. Commit & push (if deployed)

### Check Product Count:
```powershell
python -c "import json; data = json.load(open('assets/data/inventory.json', encoding='utf-8')); print(f'Total Products: {len(data[\"products\"])}')"
```

## Troubleshooting

### Local Server Won't Start
**Problem:** "Python is not recognized"
**Solution:** 
```powershell
# Install Python from https://www.python.org
# Or use full path:
C:\Users\Master\AppData\Local\Programs\Python\Python310\python.exe -m http.server 8000
```

### CSV Conversion Fails
**Problem:** "Error: [Errno 2] No such file or directory"
**Solution:** Make sure `Inventory.csv` is in the same folder as `convert_csv_to_json.py`

### Products Not Showing on Website
**Problem:** Blank page or no products
**Solution:**
1. Check browser console (F12) for JavaScript errors
2. Verify `assets/data/inventory.json` exists
3. Verify JSON is valid: `python -m json.tool assets/data/inventory.json`

### GitHub Pages Not Updating
**Problem:** Changes don't appear after push
**Solution:**
1. Hard refresh browser: `Ctrl+Shift+R`
2. Wait 2-3 minutes for GitHub to rebuild
3. Check "Actions" tab on GitHub for build errors

### Images Not Loading
**Problem:** Broken image icons on products
**Solution:**
1. Verify image files exist in `assets/images/`
2. Check filenames match exactly (case-sensitive)
3. Use supported formats: `.jpg`, `.png`, `.webp`

---

## Future Enhancements

- 🛒 Shopping cart system
- 👤 User accounts & login
- 📦 Order history
- ⭐ Product reviews & ratings
- ❤️ Wishlist/favorites
- 📧 Email notifications
- 🔧 Admin dashboard for inventory management
- 📱 Mobile app

---

## Support & Help

### Getting Help:
1. **For local setup issues:** Check the Troubleshooting section above
2. **For deployment issues:** See `DEPLOYMENT_GUIDE.md` (detailed GitHub Pages setup)
3. **For CSV conversion:** Run `python convert_csv_to_json.py` and check the output
4. **For code questions:** See comments in:
   - `js/script.js` - Search, filter, sort functions
   - `css/styles.css` - Styling variables (colors, fonts, breakpoints)

### Quick Reference:
| Task | Command |
|------|---------|
| Run locally | `python -m http.server 8000` |
| Update inventory | `python convert_csv_to_json.py` |
| Check product count | `python -c "import json; data = json.load(open('assets/data/inventory.json', encoding='utf-8')); print(len(data['products']))"` |
| Validate JSON | `python -m json.tool assets/data/inventory.json` |

---

**Website Version:** 2.0  
**Last Updated:** April 5, 2026  
**Built with:** HTML5, CSS3, Vanilla JavaScript  
**CSV Conversion:** Python 3.x  
**Deployment:** GitHub Pages (free)

## License

© 2026 U Stop Liquor. All rights reserved.
