import requests
import pandas as pd
import matplotlib.pyplot as plt
import os

# Define paths
DATA_PATH = "assets/data/nifty50_data.csv"
OUTPUT_PATH = "assets/data/nifty50_analysis.txt"
PLOT_PATH = "assets/plots/gainer_losers.png"

# Ensure directories exist
os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
os.makedirs(os.path.dirname(PLOT_PATH), exist_ok=True)

# Function to fetch Nifty 50 stock data from NSE India
def fetch_nifty50_data():
    url = 'https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%2050'
    headers = {'User-Agent': 'Mozilla/5.0'}
    session = requests.Session()
    response = session.get(url, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data. Status code: {response.status_code}")
    
    data = response.json()
    stock_data = data.get('data', [])
    nifty50_df = pd.DataFrame(stock_data)

    # Save data to CSV
    nifty50_df.to_csv(DATA_PATH, index=False)

    return nifty50_df

# Fetch and process data
nifty50_df = fetch_nifty50_data()

# Check required columns
required_columns = {'symbol', 'lastPrice', 'previousClose', 'yearHigh', 'yearLow', 'perChange30d'}
if not required_columns.issubset(nifty50_df.columns):
    raise Exception("Missing required columns in data")

# Calculate daily percentage change
nifty50_df['daily_change'] = ((nifty50_df['lastPrice'] - nifty50_df['previousClose']) / nifty50_df['previousClose']) * 100

# Top gainers and losers
top_gainers = nifty50_df.nlargest(5, 'daily_change')[['symbol', 'daily_change']]
top_losers = nifty50_df.nsmallest(5, 'daily_change')[['symbol', 'daily_change']]

# Stocks 30% Below 52-Week High
nifty50_df['30_below_high'] = ((nifty50_df['yearHigh'] - nifty50_df['lastPrice']) / nifty50_df['yearHigh']) * 100
below_30_high = nifty50_df[nifty50_df['30_below_high'] >= 30].nlargest(5, '30_below_high')[['symbol', '30_below_high']]

# Stocks 20% Above 52-Week Low
nifty50_df['20_above_low'] = ((nifty50_df['lastPrice'] - nifty50_df['yearLow']) / nifty50_df['yearLow']) * 100
above_20_low = nifty50_df[nifty50_df['20_above_low'] >= 20].nlargest(5, '20_above_low')[['symbol', '20_above_low']]

# Stocks with Highest Returns in Last 30 Days
top_returns = nifty50_df.nlargest(5, 'perChange30d')[['symbol', 'perChange30d']]

# Save output to a text file
with open(OUTPUT_PATH, 'w') as f:
    f.write("Top 5 Gainers:\n")
    f.write(top_gainers.to_string(index=False) + "\n\n")
    f.write("Top 5 Losers:\n")
    f.write(top_losers.to_string(index=False) + "\n\n")
    f.write("Stocks 30% Below 52-Week High:\n")
    f.write(below_30_high.to_string(index=False) + "\n\n")
    f.write("Stocks 20% Above 52-Week Low:\n")
    f.write(above_20_low.to_string(index=False) + "\n\n")
    f.write("Top 5 Stocks with Highest Returns in Last 30 Days:\n")
    f.write(top_returns.to_string(index=False) + "\n")

# Visualization - Bar Chart for Top Gainers and Losers
plt.figure(figsize=(10, 5))
plt.bar(top_gainers['symbol'], top_gainers['daily_change'], color='green', alpha=0.6, label='Gainers')
plt.bar(top_losers['symbol'], top_losers['daily_change'], color='red', alpha=0.6, label='Losers')
plt.xlabel('Stocks')
plt.ylabel('Daily % Change')
plt.title('Top 5 Gainers and Losers')
plt.legend()

# Save the plot
plt.savefig(PLOT_PATH)
plt.close()

print("Analysis complete. Results saved in:")
print(f"- Data: {DATA_PATH}")
print(f"- Analysis Report: {OUTPUT_PATH}")
print(f"- Plot: {PLOT_PATH}")
