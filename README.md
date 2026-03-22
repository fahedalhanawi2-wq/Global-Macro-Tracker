# Global Macroeconomic Volatility Dashboard

## Overview
An automated Python data pipeline engineered to pull live financial data and visualize the inverse correlation between global equities (S&P 500) and geopolitical/safe-haven assets (Crude Oil, Gold). 

## Technical Architecture
* **Language:** Python 3
* **Data Integration:** `yfinance` API (Yahoo Finance)
* **Data Manipulation:** `pandas`
* **Quantitative Visualization:** `matplotlib`

## Quantitative Methodology
To accurately compare assets with vastly different pricing scales (e.g., a $6,600 stock index vs. a $95 commodity), absolute prices were converted into a **Base-100 Percentage Index**. This normalization mathematically standardizes Day 1 of the timeframe to a value of 100, allowing for a 1:1 comparison of volatility and momentum across all asset classes.

## Visual Output
*(See Normalized_Macro_Dashboard.png in repository)*
