import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Configure style
sns.set(style="whitegrid")
plt.figure(figsize=(14, 7))

# Define stocks and timeframe
tickers = ['GOOGL', 'DPZ', 'SPY']  # Added SPY (S&P 500) as benchmark
end_date = datetime.now().strftime('%Y-%m-%d')

try:
    # Download data with error handling
    data = yf.download(tickers, start='2020-01-01', end=end_date, progress=False)
    
    if data.empty:
        raise ValueError("No data returned from Yahoo Finance")
        
    # Normalize prices to compare performance
    normalized = data['Adj Close'].div(data['Adj Close'].iloc[0]).mul(100)
    
    # Create plot
    ax = normalized.plot(linewidth=2.5, title='Stock Price Comparison (Normalized)')
    ax.set_ylabel('Percentage Change (%)')
    ax.set_xlabel('Date')
    
    # Add moving averages
    for ticker in tickers:
        normalized[ticker].rolling(50).mean().plot(linestyle='--', alpha=0.7)
    
    plt.legend(title='Tickers', loc='upper left')
    plt.tight_layout()
    
    # Save with timestamp
    filename = f'stock_comparison_{end_date}.png'
    plt.savefig(filename, dpi=300)
    print(f"Chart saved as {filename}")
    
except Exception as e:
    print(f"Error: {str(e)}")
    exit(1) 