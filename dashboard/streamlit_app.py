# dashboard/streamlit_app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sentiment.sentiment_pipeline import run_sentiment_pipeline
from coingecko.price_fetcher import get_historical_prices
from analysis.correlate_sentiment_prices import load_sentiment_data, average_daily_sentiment, merge_and_correlate

st.set_page_config(page_title="Crypto News Sentiment Dashboard", layout="wide")

st.title("📈 Crypto News Sentiment Analyzer")

st.markdown("""
This dashboard combines sentiment from news, Reddit, and Twitter with crypto price data from CoinGecko to help visualize trends.
""")

# --- Controls ---
coin = st.selectbox("Select a cryptocurrency", ["bitcoin", "ethereum", "dogecoin"])
days = st.slider("Select number of past days", min_value=7, max_value=60, value=30)

# --- Run pipeline + fetch prices ---
with st.spinner("Running sentiment pipeline and fetching prices..."):
    run_sentiment_pipeline()
    sentiment_df = load_sentiment_data()
    daily_sentiment = average_daily_sentiment(sentiment_df)
    price_df = pd.DataFrame(get_historical_prices(coin_id=coin, days=days))
    merged_df, corr = merge_and_correlate(daily_sentiment, price_df)

st.success("Data updated successfully!")

# --- Plot ---
fig, ax1 = plt.subplots(figsize=(10, 5))

ax1.set_xlabel('Date')
ax1.set_ylabel('Price (USD)', color='blue')
ax1.plot(merged_df['date'], merged_df['price'], color='blue', label="Price")
ax1.tick_params(axis='y', labelcolor='blue')

ax2 = ax1.twinx()
ax2.set_ylabel('Sentiment Score', color='red')
ax2.plot(merged_df['date'], merged_df['sentiment'], color='red', linestyle='--', label="Sentiment")
ax2.tick_params(axis='y', labelcolor='red')

fig.tight_layout()
st.pyplot(fig)

st.markdown(f"**📊 Correlation between sentiment and price:** `{corr:.4f}`")

st.dataframe(merged_df.tail(10))