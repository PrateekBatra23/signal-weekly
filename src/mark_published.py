import sys
import json
from datetime import date, datetime
from summarize import summarize_clusters

def shortlist(numbers):
    with open("preview.json") as f:
        items = json.load(f)

    selected = []
    for i in numbers:
        selected.append(items[i])

    return selected

def publish(numbers=list(range(10))):
    selected = shortlist(numbers)
    published = summarize_clusters(selected, 2)

    filename = f"digest_{date.today()}_.md"
    with open(filename, "w") as f:
        f.write(f"{published['overall_summary']}\n")
        for item in selected:
            f.write(f"\n---\n\n")
            f.write(f"**{item['headline']}**({item['link']})\n")
            f.write("\n")
            f.write(f"{item['summary']}\n")
    print("Saved to digest.md")

    try:
        with open("published.json") as f:
            history = json.load(f)
    except FileNotFoundError:
        history = []

    for item in selected:
        item["published_date"] = datetime.now().strftime("%Y-%m-%d")
        history.append(item)

    with open("published.json", "w") as f:
        json.dump(history, f, indent=2)
    print(f"Added {len(selected)} stories to published history")

if __name__ == "__main__":
    publish()