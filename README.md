🛒 Ecommerce Product Scraper

A Python-based web scraper that extracts product details (name, price, brand, availability, image, category, subcategory, etc.) from an ecommerce site and saves the data into a SQLite database.

✨ Features:

	Scrapes product details (name, price, brand, category, subcategory, availability, image link).

	Saves data into SQLite (product.db) with unique product URLs to avoid duplicates.

	Works with a single URL or multiple product URLs.

	Clean, structured data storage for easy analysis or future integration.

⚡ How It Works:

	Provide a product URL (or a list of product URLs).

	The scraper will fetch and parse the page using requests and BeautifulSoup.

	Product details are stored in a local SQLite database.

🔄 Single vs Multiple URLs:

Single URL:

url = "https://automationexercise.com/product_details/30"
get_product(url)


Multiple URLs:

Just create a Python list of URLs and loop over them:

urls = [
    "https://automationexercise.com/product_details/30",
    "https://automationexercise.com/product_details/31",
    "https://automationexercise.com/product_details/32"
]
for url in urls:
    get_product(url)


This way, you can scrape multiple products at once with the same script.

📂 Files:

	scraper.py → Main script to scrape and save product data.

	requirements.txt → List of Python dependencies.

	README.md → Project documentation.

🚀 Usage :

Clone this repo:

	git clone https://github.com/syedawais355/ecommerce-product-scraper.git
	cd ecommerce-product-scraper


Install dependencies:

	pip install -r requirements.txt


Run the scraper:

	python scraper.py

🛠️ Tech Stack:

	Python (requests, BeautifulSoup, sqlite3)

	SQLite3 for lightweight database storage