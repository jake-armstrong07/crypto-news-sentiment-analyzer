# scraper/twitter_scraper.py

import snscrape.modules.twitter as sntwitter
import datetime

def scrape_tweets(query="bitcoin", limit=50):
    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'{query} lang:en').get_items()):
        if i >= limit:
            break
        tweets.append({
            "source": "Twitter",
            "headline": tweet.content,
            "username": tweet.user.username,
            "date": tweet.date.isoformat()
        })
    return tweets

if __name__ == "__main__":
    results = scrape_tweets("ethereum", 20)
    for tweet in results:
        print(tweet)