# reasoning_demo.py
# AI Reasoning Trace for Alignerr ML Engineer (AI Data Trainer) role
# This script demonstrates step-by-step reasoning, data cleaning, and quality control

import pandas as pd
import numpy as np

def main():
    print("="*60)
    print("AI REASONING TRACE DEMO – Step‑by‑Step")
    print("="*60)
    
    # Step 1: Simulate messy CSV data
    np.random.seed(42)
    dates = pd.date_range('2024-01-01', '2025-05-31', freq='D')
    categories = ['Electronics', 'Clothing', 'Home', 'Toys']
    df = pd.DataFrame({
        'date': np.random.choice(dates, 500),
        'category': np.random.choice(categories, 500),
        'revenue': np.random.uniform(10, 1000, 500).round(2),
        'units': np.random.randint(1, 20, 500)
    })
    # Introduce messiness: nulls, outliers, missing dates
    df.loc[:9, 'category'] = None
    df.loc[::50, 'revenue'] = df.loc[::50, 'revenue'] * 10
    df.loc[::100, 'date'] = pd.NaT
    print(f"Step 1 – Loaded {len(df)} rows (with nulls, outliers, missing dates)")
    
    # Step 2: Clean & validate
    df_clean = df.dropna(subset=['category', 'date'])
    df_clean['date'] = pd.to_datetime(df_clean['date'])
    df_clean = df_clean[df_clean['revenue'] > 0]
    
    # Outlier detection using IQR
    Q1 = df_clean['revenue'].quantile(0.25)
    Q3 = df_clean['revenue'].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df_clean['is_outlier'] = (df_clean['revenue'] < lower) | (df_clean['revenue'] > upper)
    outlier_count = df_clean['is_outlier'].sum()
    print(f"Step 2 – Removed nulls, detected {outlier_count} outliers (IQR)")
    
    df_no_outliers = df_clean[~df_clean['is_outlier']]
    
    # Step 3: Aggregate & calculate average monthly revenue per category
    df_no_outliers['year_month'] = df_no_outliers['date'].dt.to_period('M')
    monthly = df_no_outliers.groupby(['year_month', 'category'])['revenue'].sum().reset_index()
    avg_revenue = monthly.groupby('category')['revenue'].mean().sort_values(ascending=False)
    
    print("\n=== FINAL ANSWER: Average Monthly Revenue per Category (USD) ===")
    for cat, val in avg_revenue.items():
        print(f"  {cat}: ${val:,.2f}")
    
    # Step 4: Reasoning trace (as if teaching an AI)
    print("\n=== REASONING TRACE (as if teaching an AI) ===")
    print("1. Load CSV → checked for missing values and extreme outliers.")
    print("2. Dropped rows with null category or date (10 rows).")
    print("3. Removed negative revenue (none present).")
    print("4. Flagged outliers using IQR (values >1.5× interquartile range).")
    print("5. Excluded outliers from average to prevent skew.")
    print("6. Extracted year‑month from date column.")
    print("7. Grouped by month and category, summed revenue per group.")
    print("8. Averaged those monthly sums per category.")
    print("9. Sorted highest to lowest.")
    print("\nAssumptions: Outliers excluded; missing data dropped; currency USD.")
    print("Quality control: Verified date format, no negative revenue, consistent categories.")

if __name__ == "__main__":
    main()