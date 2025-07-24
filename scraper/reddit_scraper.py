# scraper/reddit_scraper.py

import praw
import datetime

def scrape_reddit_posts(limit=20):
    reddit = praw.Reddit(
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
        user_agent="CryptoSentimentAnalyzer"
    )

    subreddit = reddit.subreddit("CryptoCurrency")
    posts = []

    for submission in subreddit.hot(limit=limit):
        posts.append({
            "source": "Reddit",
            "headline": submission.title,
            "url": submission.url,
            "score": submission.score,
            "date": datetime.datetime.fromtimestamp(submission.created_utc).isoformat()
        })

    return posts

if __name__ == "__main__":
    posts = scrape_reddit_posts()
    for post in posts:
        print(post)