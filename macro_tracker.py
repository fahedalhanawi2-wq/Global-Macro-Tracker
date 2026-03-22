import yfinance as yf
import matplotlib.pyplot as plt

# 1. Pull the data and drop any days where a market was closed for a holiday
macro_tickers = ["^GSPC", "CL=F", "GC=F"]
macro_data = yf.download(macro_tickers, period="1mo", threads=False)['Close'].dropna()

# 2. THE QUANTITATIVE FIX: Normalize all data to Base 100
# This divides every row by the first row, then multiplies by 100.
normalized_data = (macro_data / macro_data.iloc[0]) * 100

# 3. Set up the visual architecture
plt.figure(figsize=(12, 6))

# Plot the Normalized Assets
plt.plot(normalized_data.index, normalized_data['^GSPC'], color='#1f77b4', linewidth=2.5, label='S&P 500 (Equity)')
plt.plot(normalized_data.index, normalized_data['CL=F'], color='#d62728', linewidth=2, linestyle='dashed', label='Crude Oil (Geopolitics)')
plt.plot(normalized_data.index, normalized_data['GC=F'], color='#ff7f0e', linewidth=2, label='Gold (Safe Haven)')

# 4. Institutional Formatting
plt.title('Macro Volatility: 30-Day Percentage Shift (Base 100 Index)', fontsize=15, fontweight='bold')
plt.xlabel('Date', fontweight='bold')
plt.ylabel('Performance (Day 1 = 100)', fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.5)

# Add a baseline so you can easily see what went negative
plt.axhline(y=100, color='black', linestyle='-', linewidth=1, alpha=0.5)
plt.legend(loc='best', framealpha=0.9)

# Execute Render
print("\n--- FINAL RENDER INITIATED: BASE-100 NORMALIZATION ---")
plt.show()