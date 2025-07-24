# crypto-news-sentiment-analyzer

A Python-based project that scrapes cryptocurrency-related content from Twitter, Reddit, and CoinTelegraph, analyzes sentiment using VADER, and visualizes trends to help assess public mood versus market movements.

⸻

Features
	•	Twitter & Reddit Sentiment Scraper using snscrape and praw
	•	News Article Scraper from CoinTelegraph via BeautifulSoup
	•	VADER Sentiment Analysis for positive/negative/neutral scoring
	•	Trend Visualization with matplotlib and pandas
	•	Optional Streamlit Dashboard
	•	Price Correlation analysis using CoinGecko API

⸻

Project Structure

crypto-news-sentiment-analyzer/
├── scraper/
│   ├── twitter_scraper.py
│   ├── reddit_scraper.py
│   └── news_scraper.py
├── sentiment/
│   ├── sentiment_pipeline.py
│   └── analyzer.py
├── data/
│   └── (scraped CSVs go here)
├── visualization/
│   └── plot_sentiment.py
├── streamlit_app.py
├── requirements.txt
└── README.md

⸻

Installation
	1.	Clone the repository:
git clone https://github.com/jake-armstrong07/crypto-news-sentiment-analyzer.git
cd crypto-news-sentiment-analyzer
	2.	Set up a Python environment (recommended: Python 3.11)
If you’re using pyenv:
pyenv install 3.11.5
pyenv virtualenv 3.11.5 crypto-env
pyenv activate crypto-env
	3.	Install dependencies:
pip install -r requirements.txt
Crypto News Sentiment Analyzer

Usage

Run the sentiment pipeline:

python -m sentiment.sentiment_pipeline

This will:
	•	Scrape tweets, Reddit posts, and news
	•	Analyze their sentiment
	•	Save results to data/ as CSV

Visualize results:

python visualization/plot_sentiment.py

(Optional) Launch the Streamlit dashboard:

streamlit run streamlit_app.py

⸻

Example Output
	•	CSVs with sentiment columns: compound, neg, pos, neu
	•	Graphs showing sentiment trends over time
	•	Insights into how public sentiment correlates with price action

⸻

Troubleshooting

Problem: AttributeError: 'FileFinder' object has no attribute 'find_module'
This is a known issue with snscrape and Python 3.12+.

Fix: downgrade to Python 3.11:

pyenv install 3.11.5
pyenv virtualenv 3.11.5 crypto-env
pyenv activate crypto-env

Alternatively, use the fixed fork:

pip uninstall snscrape
pip install git+https://github.com/jake-armstrong07/snscrape.git@patch-python312

⸻

License

MIT License © Jake Armstrong

⸻

Contact

Got ideas, bugs, or want to collaborate?

GitHub: https://github.com/jake-armstrong07
