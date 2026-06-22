import json
from fetch_rss import fetch_rss_items
from fetch_newsapi import fetch_newsapi_items


def main():
    print("Fetching RSS....")
    rss_items = fetch_rss_items()
    print(f" {len(rss_items)} items")

    print("Fetching sAPI....")
    newsapi_items = fetch_newsapi_items()
    print(f" {len(newsapi_items)} items")

    all_items = rss_items + newsapi_items
    print(f" Total: {len(all_items)} items")

    with open("output_raw.json", "w") as f:
        json.dump(all_items, f, indent=2)
    print("Saved to output_raw.json")

if __name__ == "__main__":
    main()