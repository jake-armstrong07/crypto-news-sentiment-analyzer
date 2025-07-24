# scraper/cointelegraph_scraper.py

import requests
from bs4 import BeautifulSoup
import datetime

def scrape_cointelegraph_articles(pages=1):
    base_url = "https://cointelegraph.com"
    all_articles = []

    for page in range(1, pages + 1):
        url = f"{base_url}/tags/bitcoin?page={page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        articles = soup.find_all("a", class_="post-card-inline__title-link")
        for article in articles:
            headline = article.text.strip()
            link = base_url + article['href']
            all_articles.append({
                "source": "CoinTelegraph",
                "headline": headline,
                "url": link,
                "date": datetime.datetime.now().isoformat()
            })

    return all_articles

if __name__ == "__main__":
    data = scrape_cointelegraph_articles(2)
    for item in data:
        print(item)