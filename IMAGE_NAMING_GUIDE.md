# Image Naming Guide for U Stop Liquor

## How Images Work

Each product in your inventory automatically looks for an image file named after the product. The website will:
1. **Convert product name to filename** → lowercase + spaces become dashes + `.jpg`
2. **Look in:** `assets/images/` folder
3. **Show placeholder emoji** (🍾) if image not found

## Naming Convention

```
Product Name          →  Filename
========================================
Bud Light 6pack Cans  →  bud-light-6pack-cans.jpg
Corona Extra Beer     →  corona-extra-beer.jpg
Jack Daniel's         →  jack-daniels.jpg
Coca Cola 2L          →  coca-cola-2l.jpg
```

**Rules:**
- All lowercase
- Spaces become dashes (-)
- Apostrophes removed or become dashes
- Special characters removed
- File format: `.jpg` (or .png, .webp)

## Step-by-Step Guide to Add Images

### Option 1: Get Free Product Images

1. **Google Images** (search: "Bud Light bottle PNG")
   - Right-click → Save image
   - Rename to match the convention above
   
2. **Unsplash** (unsplash.com)
   - Search for product name
   - Download free image
   
3. **Pexels** (pexels.com)
   - Free stock photos
   - Search for beverage products

### Option 2: Use AI Image Generation
- **DALL-E** (openai.com) - Generate product images
- **Stability AI** - Free AI image generator

### Option 3: Use Brand Images Directly
- Most spirits/beer brands have official bottle images online
- Download from brand websites

---

## Adding Images to Your Website

### Method 1: Drag & Drop (Easiest)

1. **Find images** on your computer
2. **Rename them** using the convention above
3. **Drag & drop** into `assets/images/` folder in your editor
4. **Done!** Website automatically shows them

### Method 2: Windows Explorer

1. Open: `d:\VS_Code2\U_Stop_Liquor\U_Stop_Liquor\assets\images\`
2. Save/rename images here with correct naming
3. Refresh your website to see them

### Method 3: Online Tools

1. Use `convert_csv_to_json.py` to list all product names
2. Batch download images from a service
3. Rename them all at once
4. Drop into `assets/images/`

---

## Automated Image Filename Generator

Here are your top 20 products that need images:

```
bud-light-6pack-cans.jpg
corona-extra-beer.jpg
modelo-especial.jpg
heineken.jpg
coors-light.jpg
[... and 3,357 more products]
```

To get all filenames, run:
```powershell
python list_image_names.py
```

---

## Tips for Best Results

✅ **Do:**
- Use high-quality images (at least 300x300px)
- Use consistent image sizes for neat appearance
- Use images with transparent backgrounds (PNG)
- Include the product bottle/can in the image

❌ **Don't:**
- Use very small images (<100px)
- Mix heavily different image styles
- Use complex backgrounds (simple backgrounds work best)

---

## Checking If Images Are Loaded

1. Open website at `http://localhost:8000`
2. Look for actual product images instead of 🍾 emoji
3. If emoji shows = image filename doesn't match or not found
4. Check console (F12 → Console) for 404 errors

