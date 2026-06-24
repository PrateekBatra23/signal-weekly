import json
from fetch_rss import fetch_rss_items
from fetch_newsapi import fetch_newsapi_items
from rank import cluster_items,filter_published
from summarize import summarize_clusters

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

    print("Clustering...")
    clusters = cluster_items(all_items)
    print(len(clusters))

    print("Removing Prepublished titles.....")
    try:
        with open("published.json") as f:
            published = json.load(f)
    except FileNotFoundError:
        published = []

    clusters = filter_published(clusters, published)
    print(f"After dedup: {len(clusters)} fresh clusters")

    print("Summarizing with Claude...")
    result = summarize_clusters(clusters)

    with open("selected.txt", "w") as f:
        f.write("LAST WEEK IN AI\n")
        f.write("=" * 40 + "\n\n")
        for item in result["items"]:
            f.write(f"{item['headline']}\n")
            f.write(f"{item['summary']}\n")
            f.write(f"{item['link']}\n")
    print("Saved to selected.txt")

    with open("preview.json", "w") as f:
        json.dump(result["items"], f, indent=2)
    print("Saved to preview.json")
if __name__ == "__main__":
    main()