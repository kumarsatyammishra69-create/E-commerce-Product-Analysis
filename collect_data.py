# DATA COLLECTION
# We use a FREE public API (no signup needed!) + manual data

import requests          # To fetch data from internet
import pandas as pd      
import json              
import time              
print("=" * 50)
print("  E-COMMERCE PRODUCT DATA COLLECTION")
print("=" * 50)

# Fetch data from a FREE public API

print("\n[1] Fetching product data from API...")

url = "https://fakestoreapi.com/products"  # Free public API

try:
    response = requests.get(url, timeout=10)  # Send request to API
    response.raise_for_status()               # Check if request was successful

    products_raw = response.json()            # Convert response to Python list

    print(f" Success! Got {len(products_raw)} products from API")

except requests.exceptions.RequestException as e:
    print(f"  API failed: {e}")
    print("    Using backup manual data instead...")
    products_raw = []

# Manual data (backup if API fails)

manual_products = [
    {"id": 101, "title": "Wireless Headphones",     "price": 49.99,  "category": "electronics",  "rating": {"rate": 4.5, "count": 320}},
    {"id": 102, "title": "Running Shoes",            "price": 79.99,  "category": "clothing",     "rating": {"rate": 4.2, "count": 150}},
    {"id": 103, "title": "Coffee Maker",             "price": 34.99,  "category": "kitchen",      "rating": {"rate": 4.0, "count": 200}},
    {"id": 104, "title": "Python Programming Book",  "price": 29.99,  "category": "books",        "rating": {"rate": 4.8, "count": 500}},
    {"id": 105, "title": "Yoga Mat",                 "price": 24.99,  "category": "sports",       "rating": {"rate": 4.3, "count": 180}},
    {"id": 106, "title": "Smart Watch",              "price": 199.99, "category": "electronics",  "rating": {"rate": 4.6, "count": 420}},
    {"id": 107, "title": "Backpack",                 "price": 44.99,  "category": "clothing",     "rating": {"rate": 4.1, "count": 290}},
    {"id": 108, "title": "Bluetooth Speaker",        "price": 59.99,  "category": "electronics",  "rating": {"rate": 4.4, "count": 310}},
]

# Combine API data + manual data
all_products = products_raw + manual_products

print(f"\n[2] Total products collected: {len(all_products)}")

# ORGANIZE DATA INTO A TABLE using Pandas

print("\n[3] Organizing data into a table...")

rows = []  # Empty list to store each product as a row

for product in all_products:
    row = {
        "id":          product.get("id", "N/A"),
        "title":       product.get("title", "Unknown"),
        "price":       product.get("price", 0),
        "category":    product.get("category", "unknown"),
        "rating":      product.get("rating", {}).get("rate", 0),
        "num_reviews": product.get("rating", {}).get("count", 0),
    }
    rows.append(row)

# Create a DataFrame (like an Excel table in Python)
df = pd.DataFrame(rows)

print(f"   Table created with {len(df)} rows and {len(df.columns)} columns")
print(f"\n    Columns: {list(df.columns)}")

# SAVE DATA TO CSV FILE

output_file = "raw_data.csv"
df.to_csv(output_file, index=False)

print(f"\n[4] Data saved to '{output_file}'")
print("\n    Preview (first 5 rows):")
print(df.head())

print("\n STEP 1 COMPLETE! Run step2_clean_data.py next.")
