# AI Reasoning Trace Demo

This repository contains a Python script that demonstrates **step‑by‑step reasoning** suitable for AI data training, created for the **Alignerr Machine Learning Engineer (AI Data Trainer)** role.

## What the script does

- Simulates a messy CSV/Excel dataset (nulls, outliers, missing dates)
- Cleans and validates the data (0% error tolerance approach)
- Detects outliers using the **IQR (Interquartile Range)** method
- Calculates average monthly revenue per product category
- Outputs a **structured reasoning trace** as if teaching an AI

## How to run

1. Make sure you have Python installed.
2. Install the required libraries:
   ```bash
   pip install pandas numpy
