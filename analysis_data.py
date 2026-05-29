# ============================================================
# STEP 3: DATA ANALYSIS
# This file analyzes the cleaned data and finds insights
# We answer business questions using Pandas
# ============================================================

import pandas as pd    # For data analysis
import numpy as np     # For math

print("=" * 50)
print("  DATA ANALYSIS")
print("=" * 50)

# -------------------------------------------------------
# LOAD clean data
# -------------------------------------------------------

df = pd.read_csv("clean_data.csv")
print(f"\nLoaded {len(df)} products for analysis\n")

# -------------------------------------------------------
# ANALYSIS 1: Basic Statistics
# -------------------------------------------------------

print("=" * 40)
print("📊 BASIC STATISTICS")
print("=" * 40)
print(df[["price", "rating", "num_reviews", "est_revenue"]].describe().round(2))

# -------------------------------------------------------
# ANALYSIS 2: Products per Category
# -------------------------------------------------------

print("\n" + "=" * 40)
print("📦 PRODUCTS PER CATEGORY")
print("=" * 40)
category_count = df["category"].value_counts()
print(category_count)

# -------------------------------------------------------
# ANALYSIS 3: Average Price per Category
# -------------------------------------------------------

print("\n" + "=" * 40)
print("💰 AVERAGE PRICE PER CATEGORY")
print("=" * 40)
avg_price = df.groupby("category")["price"].mean().sort_values(ascending=False).round(2)
print(avg_price)

# -------------------------------------------------------
# ANALYSIS 4: Top 5 Highest Rated Products
# -------------------------------------------------------

print("\n" + "=" * 40)
print("⭐ TOP 5 HIGHEST RATED PRODUCTS")
print("=" * 40)
top_rated = df.nlargest(5, "rating")[["title", "category", "price", "rating"]]
print(top_rated.to_string(index=False))

# -------------------------------------------------------
# ANALYSIS 5: Top 5 Products by Estimated Revenue
# -------------------------------------------------------

print("\n" + "=" * 40)
print("💵 TOP 5 PRODUCTS BY ESTIMATED REVENUE")
print("=" * 40)
top_revenue = df.nlargest(5, "est_revenue")[["title", "price", "num_reviews", "est_revenue"]]
print(top_revenue.to_string(index=False))

# -------------------------------------------------------
# ANALYSIS 6: Average Rating per Category
# -------------------------------------------------------

print("\n" + "=" * 40)
print("🏆 AVERAGE RATING PER CATEGORY")
print("=" * 40)
avg_rating = df.groupby("category")["rating"].mean().sort_values(ascending=False).round(2)
print(avg_rating)

# -------------------------------------------------------
# ANALYSIS 7: Price Distribution Labels
# -------------------------------------------------------

print("\n" + "=" * 40)
print("🏷️  PRICE LABEL DISTRIBUTION")
print("=" * 40)
price_dist = df["price_label"].value_counts()
print(price_dist)

# -------------------------------------------------------
# SAVE analysis results to a text file
# -------------------------------------------------------

with open("analysis_report.txt", "w") as f:
    f.write("E-COMMERCE PRODUCT ANALYSIS REPORT\n")
    f.write("=" * 40 + "\n\n")
    f.write(f"Total Products Analyzed: {len(df)}\n\n")
    f.write("BASIC STATISTICS:\n")
    f.write(str(df[["price", "rating", "num_reviews"]].describe().round(2)))
    f.write("\n\nPRODUCTS PER CATEGORY:\n")
    f.write(str(category_count))
    f.write("\n\nAVERAGE PRICE PER CATEGORY:\n")
    f.write(str(avg_price))
    f.write("\n\nTOP 5 HIGHEST RATED PRODUCTS:\n")
    f.write(str(top_rated.to_string(index=False)))

print("\n[✅] Analysis report saved to 'analysis_report.txt'")
print("\n✅ STEP 3 COMPLETE! Run step4_dashboard.py next.")