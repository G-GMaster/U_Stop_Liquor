// Global variables
let allProducts = [];
let filteredProducts = [];

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
  // Load inventory data
  loadInventory();
  
  // Set active navigation
  setActiveNav();
});

// Load inventory from JSON
async function loadInventory() {
  try {
    const response = await fetch('./assets/data/inventory.json');
    const data = await response.json();
    allProducts = data.products;
    filteredProducts = [...allProducts];
    
    // Display products if on inventory page
    const productsContainer = document.getElementById('products-container');
    if (productsContainer) {
      displayProducts(filteredProducts);
    }
  } catch (error) {
    console.error('Error loading inventory:', error);
  }
}

// Display products
function displayProducts(products) {
  const container = document.getElementById('products-container');
  
  if (!container) return;
  
  if (products.length === 0) {
    container.innerHTML = `
      <div class="no-results" style="grid-column: 1/-1;">
        <h3>No Products Found</h3>
        <p>Try adjusting your filters or search terms.</p>
      </div>
    `;
    return;
  }
  
  container.innerHTML = products.map(product => `
    <div class="product-card">
      <div class="product-image">
        <img src="assets/images/${product.image}" 
             alt="${product.name}" 
             onerror="this.replaceWith(document.createTextNode('🍾'))"
             style="width: 100%; height: 100%; object-fit: contain;">
      </div>
      <div class="product-info">
        <div class="product-category">${product.category}</div>
        <div class="product-name">${product.name}</div>
        <div class="product-details">
          <div class="product-detail-row">
            <span><strong>Type:</strong></span>
            <span>${product.type}</span>
          </div>
          <div class="product-detail-row">
            <span><strong>Size:</strong></span>
            <span>${product.size}</span>
          </div>
          <div class="product-detail-row">
            <span><strong>Qty:</strong></span>
            <span>${product.quantity}</span>
          </div>
        </div>
        <div class="product-price">$${product.price.toFixed(2)}</div>
        <div class="product-sku">SKU: ${product.sku}</div>
        <button class="add-to-cart-btn" onclick="addToCart('${product.name}', ${product.price})">Add to Cart</button>
      </div>
    </div>
  `).join('');
}

// Search function
function searchProducts() {
  const searchTerm = document.getElementById('search-input')?.value.toLowerCase() || '';
  
  filteredProducts = allProducts.filter(product =>
    product.name.toLowerCase().includes(searchTerm) ||
    product.type.toLowerCase().includes(searchTerm) ||
    product.sku.toLowerCase().includes(searchTerm)
  );
  
  displayProducts(filteredProducts);
}

// Filter products
function filterProducts() {
  const categoryFilter = document.getElementById('category-filter')?.value || '';
  const sizeFilter = document.getElementById('size-filter')?.value || '';
  const priceMin = parseFloat(document.getElementById('price-min')?.value) || 0;
  const priceMax = parseFloat(document.getElementById('price-max')?.value) || Infinity;
  
  filteredProducts = allProducts.filter(product => {
    const categoryMatch = categoryFilter === '' || product.category === categoryFilter;
    const sizeMatch = sizeFilter === '' || product.size === sizeFilter;
    const priceMatch = product.price >= priceMin && product.price <= priceMax;
    
    return categoryMatch && sizeMatch && priceMatch;
  });
  
  displayProducts(filteredProducts);
}

// Sort products
function sortProducts() {
  const sortValue = document.getElementById('sort-select')?.value || 'name-asc';
  
  switch(sortValue) {
    case 'name-asc':
      filteredProducts.sort((a, b) => a.name.localeCompare(b.name));
      break;
    case 'name-desc':
      filteredProducts.sort((a, b) => b.name.localeCompare(a.name));
      break;
    case 'price-asc':
      filteredProducts.sort((a, b) => a.price - b.price);
      break;
    case 'price-desc':
      filteredProducts.sort((a, b) => b.price - a.price);
      break;
    default:
      break;
  }
  
  displayProducts(filteredProducts);
}

// Reset filters
function resetFilters() {
  document.getElementById('search-input').value = '';
  document.getElementById('category-filter').value = '';
  document.getElementById('size-filter').value = '';
  document.getElementById('price-min').value = '';
  document.getElementById('price-max').value = '';
  document.getElementById('sort-select').value = 'name-asc';
  
  filteredProducts = [...allProducts];
  displayProducts(filteredProducts);
}

// Add to cart (placeholder - can be expanded)
function addToCart(productName, price) {
  alert(`Added "${productName}" ($${price.toFixed(2)}) to cart!`);
  // In a real app, this would update a cart system
}

// Populate filter dropdowns
function populateFilterDropdowns() {
  const categoryFilter = document.getElementById('category-filter');
  const sizeFilter = document.getElementById('size-filter');
  
  if (categoryFilter && allProducts.length > 0) {
    const categories = [...new Set(allProducts.map(p => p.category))];
    categories.forEach(cat => {
      const option = document.createElement('option');
      option.value = cat;
      option.textContent = cat;
      categoryFilter.appendChild(option);
    });
  }
  
  if (sizeFilter && allProducts.length > 0) {
    const sizes = [...new Set(allProducts.map(p => p.size))];
    sizes.forEach(size => {
      const option = document.createElement('option');
      option.value = size;
      option.textContent = size;
      sizeFilter.appendChild(option);
    });
  }
}

// Set active navigation
function setActiveNav() {
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('nav a');
  
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPage || (currentPage === '' && href === 'index.html')) {
      link.classList.add('active');
    } else {
      link.classList.remove('active');
    }
  });
}

// Load featured categories on homepage
function loadFeaturedCategories() {
  const categoriesContainer = document.getElementById('featured-categories-list');
  
  if (!categoriesContainer || allProducts.length === 0) return;
  
  const categories = [...new Set(allProducts.map(p => p.category))];
  
  categoriesContainer.innerHTML = categories.map(cat => `
    <div class="category-card" onclick="goToCategory('${cat}')">
      <div class="category-image">🏪</div>
      <h3>${cat}</h3>
    </div>
  `).join('');
}

// Navigate to category
function goToCategory(category) {
  window.location.href = `inventory.html?category=${encodeURIComponent(category)}`;
}

// Handle URL parameters on inventory page
function handleUrlParams() {
  const params = new URLSearchParams(window.location.search);
  const category = params.get('category');
  
  if (category && document.getElementById('category-filter')) {
    document.getElementById('category-filter').value = category;
    filterProducts();
  }
}

// Run on inventory page load
if (window.location.pathname.includes('inventory.html')) {
  document.addEventListener('DOMContentLoaded', () => {
    setTimeout(populateFilterDropdowns, 500);
    setTimeout(handleUrlParams, 500);
  });
}

// Run on homepage load
if (window.location.pathname.includes('index.html') || window.location.pathname.endsWith('/')) {
  document.addEventListener('DOMContentLoaded', () => {
    setTimeout(loadFeaturedCategories, 500);
  });
}
