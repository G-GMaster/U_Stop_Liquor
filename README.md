# U Stop Liquor - Website


https://github.com/G-GMaster/U_Stop_Liquor/settings/pages
I'll help you deploy the U Stop Liquor website to GitHub Pages and get you a live link. To do this, I need a bit of information:

Do you have a GitHub account? (If not, you'll need to create a free one at github.com)
Do you have Git installed? (You can check by running git --version in PowerShell)
What GitHub username would you like to use? (This will be in your deployment URL)
Once you confirm these, I'll walk you through the deployment process using Git commands. Here's what we'll do:

The deployment will give you a link like:

And optionally, you can connect your GoDaddy domain to make it something like yourdomain.com

Please let me know:

 GitHub username (or confirm you need to create an account)
 Whether Git is installed on your system
 If you want to use this as your primary domain or if you'll connect a different domain later
I'm ready to guide you through the full deployment! 
A modern, responsive e-commerce website for U Stop Liquor featuring a searchable, filterable product inventory.

Perfect! I've added comprehensive deployment information to the README including:

✅ Live website link: https://G-GMaster.github.io/U_Stop_Liquor/
✅ GitHub repository link: https://github.com/G-GMaster/U_Stop_Liquor
✅ All deployment steps we completed
✅ How to update and re-deploy in the future
✅ Quick command reference
✅ Troubleshooting tips

Now let me push this updated README to GitHub:

Done! ✅ I've updated your README.md with:

What was added:
📍 Live Website Links

Website: https://G-GMaster.github.io/U_Stop_Liquor/
Repository: https://github.com/G-GMaster/U_Stop_Liquor
📋 Deployment Steps Documented

Git initialization
GitHub connection details
GitHub Pages setup
Live status
🔄 Update & Deploy Commands

How to push future changes
Quick command reference
Troubleshooting guide
The README now has a complete record of your deployment process for future reference! Anyone can see exactly how to update the site in the future. 🍷

Perfect! Your code is pushed to GitHub! 🎉

Now I need you to enable GitHub Pages to make it live:

Go to: https://github.com/G-GMaster/U_Stop_Liquor
Click Settings (gear icon)
Scroll down to "Pages"
Under "Build and deployment":
Source: Select Deploy from a branch
Branch: Select main and / (root)
Click Save
Wait 2-3 minutes for GitHub to deploy
🔗 YOUR LIVE WEBSITE LINK:
After you enable GitHub Pages above, visit that link and your site will be live!

Once Pages is enabled, GitHub will show you a green checkmark confirming deployment is successful. The site should be live within 2-3 minutes.

Let me know once you enable GitHub Pages and I can verify the deployment is working! 🍷



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

### 🔗 LIVE WEBSITE
**Your U Stop Liquor website is now live!**

- **Live URL:** https://G-GMaster.github.io/U_Stop_Liquor/
- **GitHub Repository:** https://github.com/G-GMaster/U_Stop_Liquor

### Deployment Completed ✅

The website was successfully deployed to GitHub Pages using the following steps:

1. **Initialized Git Repository**
   - Ran: `git init`
   - Committed all files to the repository

2. **Connected to GitHub**
   - Repository: `G-GMaster/U_Stop_Liquor`
   - Branch: `main`
   - Pushed to: `https://github.com/G-GMaster/U_Stop_Liquor.git`

3. **Enabled GitHub Pages**
   - Settings → Pages
   - Source: Deploy from a branch
   - Branch: main / root
   - Status: Active ✅

4. **Website is now accessible at:**
   ```
   https://G-GMaster.github.io/U_Stop_Liquor/
   ```

### Update Your Inventory & Deploy Changes

After deployment, here's how to update your website:

```powershell
# 1. Navigate to project directory
cd d:\VS_Code2\U_Stop_Liquor\U_Stop_Liquor

# 2. Make changes to inventory.json, images, etc.

# 3. Stage changes
git add .

# 4. Commit with message
git commit -m "Update inventory - [your message]"

# 5. Push to GitHub (changes go live in 1-2 minutes)
git push origin main
```

### Quick Commands for Future Updates

| Task | Command |
|------|---------|
| Check Git status | `git status` |
| View commit history | `git log --oneline` |
| Update and deploy | `git add . && git commit -m "message" && git push origin main` |
| Check remote URL | `git remote -v` |

### Connect Custom Domain (Optional)

To connect a custom domain (like from GoDaddy):
- See `DEPLOYMENT_GUIDE.md` for detailed GoDaddy setup instructions
- Add domain in GitHub Settings → Pages → Custom domain
- Update DNS settings with GitHub Pages IP addresses

### Troubleshooting Deployment

- **Changes not appearing?** Hard refresh browser (Ctrl+Shift+R) and wait 2-3 minutes
- **GitHub shows error?** Check "Actions" tab on your repository for build logs
- **Need to rollback?** Previous commits are safe in Git history; use `git revert`

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
