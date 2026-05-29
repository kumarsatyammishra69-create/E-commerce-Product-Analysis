# E-commerce-Product-Analysis
E-commerce product data pipeline: collection → cleaning → analysis → dashboard using Python, Pandas &amp; Matplotlib.

# E-Commerce Product Analysis

A complete data pipeline project that collects, cleans, analyzes, and visualizes 
e-commerce product data using Python.

## Objective
Build an end-to-end data pipeline — from raw data collection to an interactive 
visual dashboard — to uncover insights about product pricing, ratings, and revenue.

## Tools & Technologies
- Python 3
- Pandas — data cleaning & analysis
- Matplotlib — data visualization & dashboard
- Requests — API data collection
- BeautifulSoup — web scraping ready

## Pipeline Steps
1. **Data Collection** — Fetches product data from a public REST API + manual data
2. **Data Cleaning** — Removes duplicates, fixes missing values, standardizes categories
3. **Data Analysis** — Finds top products, avg prices, ratings, and revenue estimates
4. **Dashboard** — Generates a 6-chart visual dashboard saved as PNG

## Project Structure
├── step1_collect_data.py   # Data collection
├── step2_clean_data.py     # Data cleaning
├── step3_analysis.py       # Analysis & insights
├── step4_dashboard.py      # Dashboard visualization
├── run_all.py              # Run full pipeline at once
└── requirements.txt        # Dependencies

## How to Run
pip install -r requirements.txt
python run_all.py

## Output
- clean_data.csv — Processed dataset
- analysis_report.txt — Key findings
- dashboard.png — Visual dashboard
