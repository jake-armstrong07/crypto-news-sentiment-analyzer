# sentiment/sentiment_pipeline.py

from sentiment.sentiment_model import analyze_sentiment
from scraper.cointelegraph_scraper import scrape_cointelegraph_articles
from scraper.reddit_scraper import scrape_reddit_posts
from scraper.twitter_scraper import scrape_tweets
import pandas as pd

def main():
    # Scrape data
    print("Scraping CoinTelegraph articles...")
    ct_articles = scrape_cointelegraph_articles()
    
    print("Scraping Reddit posts...")
    reddit_posts = scrape_reddit_posts()
    
    print("Scraping Twitter tweets...")
    tweets = scrape_tweets()
    
    # Combine all scraped data into one DataFrame (example assumes each returns a DataFrame)
    print("Combining scraped data...")
    combined_df = pd.concat([ct_articles, reddit_posts, tweets], ignore_index=True)
    
    # Analyze sentiment on combined data (assumes 'text' column contains content)
    print("Analyzing sentiment...")
    combined_df['sentiment'] = combined_df['text'].apply(analyze_sentiment)
    
    # Save to CSV
    print("Saving combined data with sentiment to data/sentiment_data.csv...")
    combined_df.to_csv('data/sentiment_data.csv', index=False)
    
    print("Sentiment pipeline completed successfully.")

if __name__ == "__main__":
    main()