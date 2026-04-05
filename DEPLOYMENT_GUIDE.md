# U Stop Liquor Website - Deployment & Setup Guide

## Quick Start

Your website is ready to deploy! Follow these simple steps.

---

## PART 1: Upload to GitHub

### Step 1: Create a GitHub Repository

1. Go to [GitHub.com](https://github.com) and sign in (create an account if needed)
2. Click the **"+"** icon in the top-right corner
3. Select **"New repository"**
4. Fill in:
   - **Repository name:** `u-stop-liquor` (or any name you prefer)
   - **Description:** "U Stop Liquor - Premium Beverages & Spirits"
   - **Make it Public** (required for GitHub Pages)
   - **Do NOT initialize with README/gitignore** (we'll add our files)
   - Click **"Create repository"**

### Step 2: Upload Your Project Files

There are two methods:

#### **Method A: Using Git Command Line (Recommended)**

1. **Install Git** if you haven't already: https://git-scm.com/download
2. **Open PowerShell/Command Prompt** in your `U_Stop_L` folder
3. **Run these commands:**

```powershell
git init
git add .
git commit -m "Initial commit - U Stop Liquor website"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/u-stop-liquor.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

#### **Method B: Using GitHub Web Interface (Drag & Drop)**

1. On your new repository page, click **"uploading an existing file"**
2. Drag and drop all files from your `U_Stop_L` folder
3. Write a commit message: "Initial commit"
4. Click **"Commit changes"**

---

## PART 2: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** (gear icon)
3. Scroll down to **"Pages"** section
4. Under **"Build and deployment"**:
   - **Source:** Select **"Deploy from a branch"**
   - **Branch:** Select **"main"** (and "/" root)
   - Click **"Save"**
5. GitHub will display your site URL: `https://YOUR_USERNAME.github.io/u-stop-liquor/`
6. Wait 2-3 minutes, then visit that URL to see your live site!

---

## PART 3: Connect Your GoDaddy Domain

### Step 1: Get Your GitHub Pages IP Address

GitHub Pages uses these IP addresses (as of 2024):
- `185.199.108.153`
- `185.199.109.153`
- `185.199.110.153`
- `185.199.111.153`

### Step 2: Update GoDaddy DNS Settings

1. **Log in to GoDaddy** (godaddy.com)
2. Go to **My Products** → **Domains**
3. Click your domain name
4. Click **"Manage DNS"** or **"DNS"**
5. **Add/Update A Records:**
   - Find or create an **A record**
   - Points to: `185.199.108.153`
   - Repeat for all 4 IP addresses if there are multiple record slots
   - (Alternative: Use CNAME record pointing to `YOUR_USERNAME.github.io`)

6. **Add a CNAME Record (Alternative/Additional):**
   - Name: `www`
   - Type: `CNAME`
   - Points to: `YOUR_USERNAME.github.io`

7. Click **Save** and wait 24-48 hours for DNS to propagate

### Step 3: Add Custom Domain to GitHub

1. Go to your GitHub repository
2. Click **Settings** → **Pages**
3. Under **"Custom domain"**:
   - Enter your domain: `yourdomainname.com`
   - Click **"Save"**
4. GitHub will show a green checkmark when DNS is verified
5. **Enable HTTPS** (check the "Enforce HTTPS" box)

---

## Testing Your Domain

After DNS updates propagate:
1. Visit `https://yourdomainname.com` in a browser
2. You should see your U Stop Liquor website!
3. Test all pages and functionality

---

## UPDATING YOUR INVENTORY

### Method 1: Update Excel → Convert to JSON

When you have a new Excel file:

1. **Export Excel to CSV:**
   - Open in Excel
   - File → Save As → Format: **CSV (Comma delimited)**
   - Save as `inventory.csv`

2. **Convert CSV to JSON** (use online tool):
   - Go to: https://www.convertcsv.com/csv-to-json.htm
   - Upload your CSV
   - Copy the JSON output
   - Paste into `assets/data/inventory.json`
   - Commit and push to GitHub

### Method 2: Manually Edit JSON

Edit `assets/data/inventory.json` directly:

```json
{
  "store": { ... },
  "categories": ["Beer", "Wine", "Spirits", ...],
  "products": [
    {
      "id": 1,
      "name": "Product Name",
      "category": "Beer",
      "type": "Lager",
      "size": "12 oz",
      "quantity": "6-Pack",
      "price": 8.99,
      "sku": "SKU-CODE",
      "image": "filename.jpg",
      "description": "Product description"
    }
    // ... more products
  ]
}
```

After editing, commit and push:
```powershell
git add .
git commit -m "Updated inventory"
git push
```

---

## ADDING YOUR IMAGES

### Replace Placeholder Images

1. **Prepare your images** (JPG or PNG format, optimized)
2. **Upload to** `assets/images/` folder:
   - `hero-banner.jpg` - Homepage hero image
   - `category-beer.jpg` - Beer category image
   - `category-wine.jpg` - Wine category image
   - etc.

3. **Update filenames in:**
   - `index.html` - Change image references in featured categories
   - `inventory.json` - Update image filenames in product objects

4. **Push to GitHub:**
```powershell
git add .
git commit -m "Added product images"
git push
```

---

## FILE STRUCTURE

Your website should look like this:

```
U_Stop_L/
├── index.html                    (Homepage)
├── inventory.html                (Products page)
├── css/
│   └── styles.css               (All styling)
├── js/
│   └── script.js                (Search, filter, sort)
├── assets/
│   ├── images/                  (Your product & category images)
│   └── data/
│       └── inventory.json       (Product data - UPDATE THIS)
├── .gitignore                   (Optional - ignore files)
└── README.md                    (Optional - documentation)
```

---

## TROUBLESHOOTING

### Site not loading at custom domain?
- Wait 24-48 hours for DNS to propagate
- Clear browser cache (Ctrl+Shift+Delete)
- Check GitHub Pages settings - custom domain should be set
- Verify A or CNAME records in GoDaddy DNS

### Search/Filter not working?
- Check browser console (F12) for errors
- Verify `assets/data/inventory.json` path is correct
- Ensure JSON format is valid (use jsonlint.com to test)

### Images not showing?
- Verify image files are in `assets/images/` folder
- Check filenames match exactly in JSON/HTML
- Use relative paths: `./assets/images/filename.jpg`

---

## MAINTENANCE TIPS

1. **Backup your work:**
   ```powershell
   git clone https://github.com/YOUR_USERNAME/u-stop-liquor.git backup
   ```

2. **Make regular commits** when you make changes
3. **Test locally** before pushing (use a local web server)
4. **Monitor your domain** - renew before expiration on GoDaddy

---

## SUPPORT RESOURCES

- **Git Help:** https://git-scm.com/doc
- **GitHub Pages Docs:** https://docs.github.com/en/pages
- **GoDaddy Domain Help:** https://www.godaddy.com/help
- **JSON Validator:** https://jsonlint.com
- **CSV to JSON Converter:** https://www.convertcsv.com/csv-to-json.htm

---

## NEXT STEPS

1. ✅ Upload to GitHub (see Part 1)
2. ✅ Enable GitHub Pages (see Part 2)
3. ✅ Connect your GoDaddy domain (see Part 3)
4. ✅ Swap placeholder images with your real photos
5. ✅ Update inventory.json with your actual products
6. ✅ Test everything and go live!

Your website is ready! 🎉

