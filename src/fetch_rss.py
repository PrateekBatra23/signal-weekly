import feedparser
from time import mktime
from datetime import datetime, timezone, timedelta
from config import RSS_FEEDS, LOOKBACK_DAYS

def fetch_rss_items():
    cutoff=datetime.now(timezone.utc)-timedelta(days=LOOKBACK_DAYS)
    items=[]
    for url in RSS_FEEDS:
        try:
            feed=feedparser.parse(url)
            source=feed.feed.title
            for entry in feed.entries:
                published=datetime.fromtimestamp(
                    mktime(entry.published_parsed),tz=timezone.utc
                )
                if published<cutoff or not entry.get("title"):
                    continue
                items.append({
                    "title":entry.title,
                    "link":entry.link,
                    "summary":entry.get("summary",""),
                    "published":published.isoformat(),
                    "source":source,
                    "score":0,
                    "score":0,
                    "comments":0,
                    "origin":"rss"
                })
        except Exception as e:
            print(f"Failed to fetch {url}:{e}")
            continue
    return items
if __name__ == "__main__":
    result=fetch_rss_items()
    print(len(result))