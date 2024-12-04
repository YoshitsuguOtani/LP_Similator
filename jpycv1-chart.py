import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

def get_historical_jpyc_data():
    try:
        # Set date range
        end_date = datetime.now()
        start_date = end_date - timedelta(days=365)
        
        # CoinGecko API endpoint
        url = f"https://api.coingecko.com/api/v3/coins/jpyc/market_chart/range"
        params = {
            "vs_currency": "jpy",
            "from": int(start_date.timestamp()),
            "to": int(end_date.timestamp())
        }
        
        print("Fetching data...")
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
            df.set_index('timestamp', inplace=True)
            return df
            
        else:
            print(f"API Error: Status Code {response.status_code}")
            return None
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def plot_multiple_charts(df):
    # Set plot style
    sns.set_style("whitegrid")
    
    # Create subplots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
    
    # 1. Line Plot
    sns.lineplot(data=df, y='price', x=df.index, ax=ax1)
    ax1.set_title('JPYC Price Trend (Line)')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Price (JPY)')
    
    # 2. Line Plot with Moving Averages
    df['MA7'] = df['price'].rolling(window=7).mean()
    df['MA30'] = df['price'].rolling(window=30).mean()
    
    sns.lineplot(data=df, y='price', x=df.index, ax=ax2, label='Price', alpha=0.5)
    sns.lineplot(data=df, y='MA7', x=df.index, ax=ax2, label='7-day MA')
    sns.lineplot(data=df, y='MA30', x=df.index, ax=ax2, label='30-day MA')
    ax2.set_title('Price with Moving Averages')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Price (JPY)')
    ax2.legend()
    
    # 3. Histogram (Price Distribution)
    sns.histplot(data=df, x='price', ax=ax3, bins=50)
    ax3.set_title('Price Distribution')
    ax3.set_xlabel('Price (JPY)')
    ax3.set_ylabel('Frequency')
    
    # 4. Box Plot (Monthly)
    df['month'] = df.index.strftime('%Y-%m')
    sns.boxplot(data=df, x='month', y='price', ax=ax4)
    ax4.set_title('Monthly Price Distribution')
    ax4.set_xlabel('Month')
    ax4.set_ylabel('Price (JPY)')
    ax4.tick_params(axis='x', rotation=45)
    
    # Adjust layout
    plt.suptitle('JPYC Price Analysis (Last 365 Days)', fontsize=16, y=1.02)
    plt.tight_layout()
    plt.show()
    
    # Display basic statistics
    print("\nBasic Statistics:")
    print(df['price'].describe())

def main():
    try:
        # Get data
        df = get_historical_jpyc_data()
        
        if df is not None:
            # Display data information
            print("\nData Period:")
            print(f"Start: {df.index[0]}")
            print(f"End: {df.index[-1]}")
            print(f"Number of data points: {len(df)}")
            
            # Plot multiple charts
            plot_multiple_charts(df)
            
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()