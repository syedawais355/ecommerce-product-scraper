import requests
from bs4 import BeautifulSoup
import sqlite3

def get_product(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    info = soup.find("div", class_="product-information")
    product = {}

    product["name"] = info.find("h2").text.strip()

    product["category"] = ""
    product["subcategory"] = ""
    for p in info.find_all("p"):
        text = p.text.strip()
        if "Category:" in text:
            category_text = text.replace("Category:", "").strip()
            parts = [p.strip() for p in category_text.split(">")]
            product["category"] = parts[0]
            if len(parts) > 1:
                product["subcategory"] = parts[1]
        else:
            product["subcategory"] =  product["category"] = "None"  
    outer_span = info.find("span")
    inner_span = outer_span.find("span")
    product["price"] = inner_span.text.replace("Rs.", "").strip()
    product["availability"] = "In Stock" in info.text
    product["brand"] = ""
    for p in info.find_all("p"):
        b_tag = p.find("b")
        if b_tag and "Brand:" in b_tag.text:
            product["brand"] = b_tag.next_sibling.strip()

    image = soup.find("div", class_="view-product").find("img")
    product["image_url"] = "https://automationexercise.com" + image["src"]

    print("Name:", product["name"])
    print("Category:", product["category"])
    if product["subcategory"]:
        print("Subcategory:", product["subcategory"])
    print("Price:", product["price"])
    print("Brand:", product["brand"])
    print("In Stock:", "True" if product["availability"] else "False")
    print("Image Url:", product["image_url"])
    db = sqlite3.connect("product.db")
    cur = db.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            category TEXT,
            subcategory TEXT,
            price TEXT,
            image_url TEXT,
            availability TEXT,
            brand TEXT,
            product_url TEXT UNIQUE
        )
    """)
    cur.execute("""
        INSERT OR IGNORE INTO products
        (name, category, subcategory, price, image_url, availability, brand, product_url)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        product["name"], product["category"], product["subcategory"], product["price"],
        product["image_url"], product["availability"], product["brand"], url
    ))
    db.commit()
    db.close()

    print("Saved to product.db")

url = "https://automationexercise.com/product_details/30"
get_product(url)
