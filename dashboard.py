# ============================================================
# STEP 4: DASHBOARD / VISUALIZATIONS
# This file creates colorful charts and graphs
# It saves one big dashboard image + individual charts
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt    # For creating charts
import matplotlib.gridspec as gridspec
import numpy as np

print("=" * 50)
print("  CREATING DASHBOARD")
print("=" * 50)

# -------------------------------------------------------
# LOAD clean data
# -------------------------------------------------------

df = pd.read_csv("clean_data.csv")
print(f"\nLoaded {len(df)} products\n")

# Color palette (same colors used throughout)
COLORS = ["#4C72B0", "#DD8452", "#55A868", "#C44E52", "#8172B2", "#937860", "#DA8BC3"]

# ============================================================
# CREATE THE MAIN DASHBOARD (6 charts in one image)
# ============================================================

fig = plt.figure(figsize=(18, 12))
fig.suptitle("E-Commerce Product Analysis Dashboard", fontsize=22, fontweight="bold", y=0.98)

# Use GridSpec to arrange 6 charts in a 2-row, 3-column grid
gs = gridspec.GridSpec(2, 3, figure=fig, hspace=0.45, wspace=0.35)

# -------------------------------------------------------
# CHART 1: Bar Chart — Number of Products per Category
# -------------------------------------------------------
ax1 = fig.add_subplot(gs[0, 0])

category_count = df["category"].value_counts()
ax1.bar(category_count.index, category_count.values, color=COLORS[:len(category_count)])
ax1.set_title("Products per Category", fontweight="bold")
ax1.set_xlabel("Category")
ax1.set_ylabel("Number of Products")
ax1.tick_params(axis="x", rotation=30)

# Add number labels on top of each bar
for i, val in enumerate(category_count.values):
    ax1.text(i, val + 0.1, str(val), ha="center", fontweight="bold")

print("[1] Chart 1 created: Products per Category")

# -------------------------------------------------------
# CHART 2: Horizontal Bar — Average Price per Category
# -------------------------------------------------------
ax2 = fig.add_subplot(gs[0, 1])

avg_price = df.groupby("category")["price"].mean().sort_values()
ax2.barh(avg_price.index, avg_price.values, color=COLORS[:len(avg_price)])
ax2.set_title("Avg Price per Category", fontweight="bold")
ax2.set_xlabel("Average Price ($)")

# Add price labels
for i, val in enumerate(avg_price.values):
    ax2.text(val + 0.5, i, f"${val:.1f}", va="center", fontsize=9)

print("[2] Chart 2 created: Average Price per Category")

# -------------------------------------------------------
# CHART 3: Pie Chart — Price Label Distribution
# -------------------------------------------------------
ax3 = fig.add_subplot(gs[0, 2])

price_dist = df["price_label"].value_counts()
ax3.pie(
    price_dist.values,
    labels=price_dist.index,
    autopct="%1.1f%%",         # Show percentage
    colors=COLORS[:len(price_dist)],
    startangle=90,
    textprops={"fontsize": 11}
)
ax3.set_title("Price Distribution", fontweight="bold")

print("[3] Chart 3 created: Price Distribution Pie Chart")

# -------------------------------------------------------
# CHART 4: Scatter Plot — Price vs Rating
# -------------------------------------------------------
ax4 = fig.add_subplot(gs[1, 0])

categories = df["category"].unique()
for i, cat in enumerate(categories):
    subset = df[df["category"] == cat]
    ax4.scatter(subset["price"], subset["rating"],
                label=cat, color=COLORS[i % len(COLORS)], alpha=0.7, s=60)

ax4.set_title("Price vs Rating", fontweight="bold")
ax4.set_xlabel("Price ($)")
ax4.set_ylabel("Rating")
ax4.legend(fontsize=7, loc="lower right")
ax4.axhline(y=df["rating"].mean(), color="red", linestyle="--", alpha=0.5, label="Avg Rating")

print("[4] Chart 4 created: Price vs Rating Scatter")

# -------------------------------------------------------
# CHART 5: Bar Chart — Top 5 Products by Revenue
# -------------------------------------------------------
ax5 = fig.add_subplot(gs[1, 1])

top5 = df.nlargest(5, "est_revenue")
short_titles = [t[:20] + "..." if len(t) > 20 else t for t in top5["title"]]  # Shorten long titles
ax5.bar(short_titles, top5["est_revenue"], color=COLORS[:5])
ax5.set_title("Top 5 by Estimated Revenue", fontweight="bold")
ax5.set_xlabel("Product")
ax5.set_ylabel("Est. Revenue ($)")
ax5.tick_params(axis="x", rotation=30)
for i, val in enumerate(top5["est_revenue"].values):
    ax5.text(i, val + 100, f"${val:,.0f}", ha="center", fontsize=8, fontweight="bold")

print("[5] Chart 5 created: Top 5 by Revenue")

# -------------------------------------------------------
# CHART 6: Bar Chart — Avg Rating per Category
# -------------------------------------------------------
ax6 = fig.add_subplot(gs[1, 2])

avg_rating = df.groupby("category")["rating"].mean().sort_values(ascending=False)
bars = ax6.bar(avg_rating.index, avg_rating.values, color=COLORS[:len(avg_rating)])
ax6.set_title("Avg Rating per Category", fontweight="bold")
ax6.set_xlabel("Category")
ax6.set_ylabel("Average Rating")
ax6.set_ylim(0, 5.5)
ax6.tick_params(axis="x", rotation=30)
ax6.axhline(y=4.0, color="orange", linestyle="--", alpha=0.7, label="Target (4.0)")
ax6.legend()

for bar, val in zip(bars, avg_rating.values):
    ax6.text(bar.get_x() + bar.get_width() / 2, val + 0.05,
             f"{val:.2f}", ha="center", fontsize=9, fontweight="bold")

print("[6] Chart 6 created: Avg Rating per Category")

# -------------------------------------------------------
# SAVE the dashboard as an image
# -------------------------------------------------------

plt.savefig("dashboard.png", dpi=150, bbox_inches="tight")
print("\n✅ Dashboard saved as 'dashboard.png'")
plt.show()   # Also display on screen

print("\n✅ STEP 4 COMPLETE! All files are ready.")
print("\n📁 Files created:")
print("   raw_data.csv       — Original collected data")
print("   clean_data.csv     — Cleaned and processed data")
print("   analysis_report.txt — Text analysis results")
print("   dashboard.png      — Visual dashboard")