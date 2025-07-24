# analysis/correlate_sentiment_prices.py

import pandas as pd
from coingecko.price_fetcher import get_historical_prices

def load_sentiment_data(filepath="data/sentiment_output.csv"):
    df = pd.read_csv(filepath, parse_dates=["date"])
    df['date'] = df['date'].dt.date  # Strip time
    return df

def average_daily_sentiment(df):
    return df.groupby('date')['sentiment'].mean().reset_index()

def load_price_data(coin="bitcoin", days=30):
    prices = get_historical_prices(coin_id=coin, days=days)
    return pd.DataFrame(prices)

def merge_and_correlate(sentiment_df, price_df):
    sentiment_df['date'] = pd.to_datetime(sentiment_df['date'])
    price_df['date'] = pd.to_datetime(price_df['date'])

    merged = pd.merge(sentiment_df, price_df, on='date', how='inner')
    correlation = merged['sentiment'].corr(merged['price'])

    return merged, correlation

if __name__ == "__main__":
    sentiment_df = load_sentiment_data()
    daily_sentiment = average_daily_sentiment(sentiment_df)

    price_df = load_price_data("bitcoin", 30)

    merged, corr = merge_and_correlate(daily_sentiment, price_df)

    print("[✓] Merged Data:")
    print(merged.head())

    print(f"\n[📊] Pearson Correlation between sentiment and price: {corr:.4f}")
    merged.to_csv("data/merged_sentiment_price.csv", index=False)