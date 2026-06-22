from datetime import datetime, timezone, timedelta
from config import LOOKBACK_DAYS, NEWSAPI_QUERY
import requests
import os

def fetch_newsapi_items():
    api_key = os.environ["NEWSAPI_KEY"]
    cutoff = datetime.now(timezone.utc) - timedelta(days=LOOKBACK_DAYS)
    items = []
    try:
        Params = {
            "q": NEWSAPI_QUERY,
            "language": "en",
            "sortBy": "publishedAt",
            "apikey": api_key,
            "from": cutoff.strftime("%Y-%m-%d"),
            "pagesize": "100"
        }
        response = requests.get("https://newsapi.org/v2/everything", params=Params)
        data = response.json()
        for article in data["articles"]:
            if not article.get("description"):
                continue
            items.append({
                "title": article.get("title", ""),
                "link": article.get("url", ""),
                "summary": article.get("description", ""),
                "published": article.get("publishedAt", ""),
                "source": (article.get("source", {}).get("name", "")),
                "author": article.get("author", ""),
                "image": article.get("urlToImage", ""),
                "score": 0,
                "comments": 0,
                "origin": "news_api"
            })
    except Exception as e:
        print(f"Failed to fetch :{e}")
    return items

if __name__ == "__main__":
    result = fetch_newsapi_items()
    print(len(result))