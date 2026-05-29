# ============================================================
# STEP 2: DATA CLEANING
# This file cleans and prepares the raw data for analysis
# We fix missing values, wrong types, duplicates, etc.
# ============================================================

import pandas as pd    # For data tables
import numpy as np     # For math operations

print("=" * 50)
print("  DATA CLEANING")
print("=" * 50)

# -------------------------------------------------------
# LOAD the raw data we collected in Step 1
# -------------------------------------------------------

print("\n[1] Loading raw data...")
df = pd.read_csv("raw_data.csv")
print(f"    Loaded {len(df)} rows")

# -------------------------------------------------------
# CHECK for problems in the data
# -------------------------------------------------------

print("\n[2] Checking data quality...")
print(f"    Missing values:\n{df.isnull().sum()}")
print(f"\n    Duplicate rows: {df.duplicated().sum()}")
print(f"\n    Data types:\n{df.dtypes}")

# -------------------------------------------------------
# FIX PROBLEM 1: Remove duplicate rows
# -------------------------------------------------------

before = len(df)
df = df.drop_duplicates()           # Remove exact duplicate rows
df = df.drop_duplicates(subset="id")  # Remove duplicate product IDs
after = len(df)

print(f"\n[3] Removed {before - after} duplicate rows")

# -------------------------------------------------------
# FIX PROBLEM 2: Handle missing values
# -------------------------------------------------------

df["price"]       = df["price"].fillna(df["price"].mean())       # Fill missing price with average
df["rating"]      = df["rating"].fillna(df["rating"].median())   # Fill missing rating with median
df["category"]    = df["category"].fillna("unknown")              # Fill missing category with "unknown"
df["num_reviews"] = df["num_reviews"].fillna(0)                   # Fill missing reviews with 0

print("[4] Missing values fixed ✅")

# -------------------------------------------------------
# FIX PROBLEM 3: Standardize category names
# (Make all lowercase and remove extra spaces)
# -------------------------------------------------------

df["category"] = df["category"].str.lower().str.strip()

# Rename similar categories to one standard name
category_map = {
    "men's clothing":   "clothing",
    "women's clothing": "clothing",
    "jewelery":         "jewelry",
}
df["category"] = df["category"].replace(category_map)

print("[5] Category names standardized ✅")

# -------------------------------------------------------
# ADD NEW COLUMNS (Feature Engineering)
# These new columns help us analyze data better
# -------------------------------------------------------

# Price category: cheap / mid-range / expensive
def label_price(price):
    if price < 30:
        return "Cheap"
    elif price < 100:
        return "Mid-range"
    else:
        return "Expensive"

df["price_label"] = df["price"].apply(label_price)

# Rating category: good / average / poor
def label_rating(rating):
    if rating >= 4.5:
        return "Excellent"
    elif rating >= 4.0:
        return "Good"
    elif rating >= 3.0:
        return "Average"
    else:
        return "Poor"

df["rating_label"] = df["rating"].apply(label_rating)

# Revenue estimate = price × number of reviews (rough estimate)
df["est_revenue"] = (df["price"] * df["num_reviews"]).round(2)

print("[6] New columns added: price_label, rating_label, est_revenue ✅")

# -------------------------------------------------------
# SAVE cleaned data to a new file
# -------------------------------------------------------

df.to_csv("clean_data.csv", index=False)

print(f"\n[7] Clean data saved to 'clean_data.csv'")
print(f"\n    Final dataset: {len(df)} rows, {len(df.columns)} columns")
print(f"\n    Preview:")
print(df.head())

print("\n✅ STEP 2 COMPLETE! Run step3_analysis.py next.")