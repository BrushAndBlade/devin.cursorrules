import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

def analyze_stocks(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
    normalized = data.div(data.iloc[0]).mul(100)
    
    plt.figure(figsize=(12,6))
    normalized.plot()
    plt.title('Stock Price Comparison')
    plt.ylabel('Normalized Price (%)')
    plt.xlabel('Date')
    plt.grid(True)
    
    filename = f"stock_comparison_{datetime.now().strftime('%Y-%m-%d')}.png"
    plt.savefig(filename)
    print(f"Chart saved as {filename}")

if __name__ == "__main__":
    analyze_stocks(['AAPL', 'MSFT', 'GOOGL'], '2020-01-01', datetime.now().strftime('%Y-%m-%d')) 