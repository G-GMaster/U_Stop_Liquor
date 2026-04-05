# 🍷 U STOP LIQUOR - QUICK START GUIDE

## ✅ YOUR WEBSITE IS READY!

Your complete, fully functional U Stop Liquor website has been created in:
```
d:\VS_Code2\U_Stop_L
```

---

## 🚀 NEXT STEPS (In Order)

### 1️⃣ TEST IT LOCALLY (2 minutes)

Open PowerShell in your `U_Stop_L` folder and run:
```powershell
python -m http.server 8000
```

Then open your browser and visit: **http://localhost:8000**

**You should see:**
- ✅ Homepage with hero banner and featured categories
- ✅ Inventory page with searchable/filterable products
- ✅ Sample liquor store data (sample products)

### 2️⃣ CUSTOMIZE YOUR INVENTORY (5-10 minutes)

**Option A: Quick Update**
- Edit `assets/data/inventory.json` directly in VS Code
- Follow the JSON format shown in the file
- Save and refresh browser

**Option B: Convert from Excel**
- Export your Excel file as CSV
- Use: https://www.convertcsv.com/csv-to-json.htm
- Replace contents of `assets/data/inventory.json`
- See `EXCEL_TO_JSON_GUIDE.md` for detailed instructions

### 3️⃣ ADD YOUR IMAGES (Variable Time)

1. Place your product/category images in: `assets/images/`
2. Update filenames in `assets/data/inventory.json`
3. Update hero banner references in `index.html` if needed

**Example image filename:** `corona-extra.jpg`

### 4️⃣ DEPLOY TO GITHUB PAGES (10 minutes)

Follow the complete guide in `DEPLOYMENT_GUIDE.md`:
1. Create GitHub account (free)
2. Upload project to GitHub
3. Enable GitHub Pages
4. Connect your GoDaddy domain

---

## 📁 WHAT YOU HAVE

```
U_Stop_L/
├── index.html                    ← Homepage
├── inventory.html                ← Products page
├── css/styles.css               ← All styling
├── js/script.js                 ← Search, filter, sort
├── assets/
│   ├── images/                  ← Your product images
│   └── data/inventory.json      ← ⭐ YOUR INVENTORY DATA
├── DEPLOYMENT_GUIDE.md          ← How to deploy
├── EXCEL_TO_JSON_GUIDE.md       ← How to convert Excel
├── README.md                    ← Full documentation
└── .gitignore                   ← Git ignore rules
```

---

## 🎨 FEATURES INCLUDED

✅ **Homepage**
- Hero banner with call-to-action
- Featured categories grid
- Benefits section

✅ **Inventory Page**
- Search by product name/type/SKU
- Filter by category, size, price
- Sort by name or price
- Product cards with images, prices, SKUs
- Add to cart button

✅ **Responsive Design**
- Works on mobile, tablet, desktop
- Modern black/red/gold theme
- Professional liquor store aesthetic

✅ **Ready for GitHub Pages**
- No server needed
- Free hosting
- Easy domain connection

---

## 📝 UPDATING INVENTORY

### Simple Way:
1. Edit `assets/data/inventory.json`
2. Add/remove/modify products
3. Save file
4. Refresh browser - changes appear instantly!

### From Excel:
1. See `EXCEL_TO_JSON_GUIDE.md`
2. Export Excel as CSV
3. Convert online or with Python script
4. Replace JSON file

### Product Template:
```json
{
  "id": 1,
  "name": "Corona Extra",
  "category": "Beer",
  "type": "Lager",
  "size": "12 oz",
  "quantity": "12-Pack",
  "price": 15.99,
  "sku": "COR-12OZ-12PK",
  "image": "corona-extra.jpg",
  "description": "Crisp, refreshing lager"
}
```

---

## 🌍 DEPLOYMENT CHECKLIST

- [ ] **Test locally** - Run `python -m http.server 8000`
- [ ] **Add your images** - Place in `assets/images/`
- [ ] **Update inventory** - Edit `inventory.json` with your products
- [ ] **Create GitHub account** - Free at github.com
- [ ] **Upload to GitHub** - Follow `DEPLOYMENT_GUIDE.md`
- [ ] **Enable GitHub Pages** - In repository settings
- [ ] **Connect GoDaddy domain** - Update DNS settings
- [ ] **Test live domain** - Visit your new website!

---

## 🎯 COMMON TASKS

### Change Store Name
- `index.html` - Update `<div class="logo">U STOP LIQUOR</div>`
- `inventory.json` - Update store name object

### Change Colors
- Open `css/styles.css`
- Edit the `:root` section:
  ```css
  :root {
    --primary-black: #1a1a1a;
    --primary-red: #8b0000;
    --gold: #d4af37;
  }
  ```

### Add New Category
- Add to `inventory.json` → `categories` array
- Add products with that category
- Filter dropdowns auto-populate!

### Fix Search/Filter Issues
- Check browser console (F12 → Console tab)
- Verify JSON is valid: https://jsonlint.com
- Ensure category values match exactly

---

## 📚 DOCUMENTATION FILES

| File | Purpose |
|------|---------|
| `DEPLOYMENT_GUIDE.md` | How to deploy to GitHub Pages & connect domain |
| `EXCEL_TO_JSON_GUIDE.md` | Convert Excel spreadsheet to JSON |
| `README.md` | Full project documentation |
| `.gitignore` | Files to ignore in Git |

---

## ❓ QUICK HELP

**Q: Where do I put my product images?**
A: In the `assets/images/` folder. Then update filenames in `inventory.json`.

**Q: How do I add products?**
A: Edit `assets/data/inventory.json` - add a new product object.

**Q: Will it work on GitHub Pages?**
A: Yes! It's 100% static HTML/CSS/JavaScript - no server needed.

**Q: Can I connect my GoDaddy domain?**
A: Yes! Follow `DEPLOYMENT_GUIDE.md` → Part 3.

**Q: Do I need to pay?**
A: No! GitHub Pages is free. GitHub + domain hosting is all you need.

**Q: Where's the admin panel?**
A: Edit `inventory.json` directly - simple and effective!

---

## 🚨 BEFORE YOU DEPLOY

1. **Test locally first** - `python -m http.server 8000`
2. **Replace sample inventory** - Add your real products
3. **Add your images** - Replace placeholder bottle emoji
4. **Review all pages** - Check homepage and inventory
5. **Test search/filter** - Make sure it works
6. **Validate JSON** - Use jsonlint.com

---

## 📞 SUPPORT

For help:
1. Check the relevant `.md` file in the project folder
2. Read comments in `js/script.js` and `css/styles.css`
3. Visit GitHub Pages docs: https://docs.github.com/en/pages
4. Use JSON validator: https://jsonlint.com

---

## 🎉 YOU'RE ALL SET!

Your U Stop Liquor website is complete and ready to go live!

**Next step:** Follow the deployment guide when you're ready.

Good luck! 🍻

---

**Website Version:** 1.0  
**Date Created:** April 2024  
**Technologies:** HTML5, CSS3, Vanilla JavaScript (No dependencies!)
