# analysis/visualize.py

import pandas as pd
import matplotlib.pyplot as plt

def plot_sentiment_vs_price(csv_path="data/merged_sentiment_price.csv"):
    df = pd.read_csv(csv_path, parse_dates=["date"])

    fig, ax1 = plt.subplots(figsize=(10, 6))

    ax1.set_xlabel('Date')
    ax1.set_ylabel('Bitcoin Price (USD)', color='tab:blue')
    ax1.plot(df['date'], df['price'], label='Price', color='tab:blue')
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    ax2 = ax1.twinx()
    ax2.set_ylabel('Sentiment Score', color='tab:red')
    ax2.plot(df['date'], df['sentiment'], label='Sentiment', color='tab:red')
    ax2.tick_params(axis='y', labelcolor='tab:red')

    plt.title("Bitcoin Price vs Sentiment Score")
    fig.tight_layout()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    plot_sentiment_vs_price()