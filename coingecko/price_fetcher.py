# coingecko/price_fetcher.py

import requests
import datetime

def get_current_price(coin_id="bitcoin", currency="usd"):
    """
    Get current price of a cryptocurrency (e.g., bitcoin, ethereum).
    """
    url = f"https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": coin_id,
        "vs_currencies": currency
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data.get(coin_id, {}).get(currency)

def get_historical_prices(coin_id="bitcoin", currency="usd", days=30):
    """
    Get historical daily closing prices for the past 'days' days.
    """
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {
        "vs_currency": currency,
        "days": days,
        "interval": "daily"
    }
    response = requests.get(url, params=params)
    prices = response.json().get("prices", [])
    results = [
        {
            "date": datetime.datetime.utcfromtimestamp(p[0] / 1000).strftime('%Y-%m-%d'),
            "price": p[1]
        }
        for p in prices
    ]
    return results

if __name__ == "__main__":
    current = get_current_price("bitcoin")
    print(f"Bitcoin price now: ${current}")

    history = get_historical_prices("bitcoin", days=7)
    for entry in history:
        print(entry)