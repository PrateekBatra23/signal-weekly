from difflib import SequenceMatcher
from config import SIMILARITY_THRESHOLD
import re


def normalize(text):
    if not text:
        return ""
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text.strip()

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

def cluster_items(items):
    clusters = []
    for item in items:
        norm_title = normalize(item["title"])
        placed = False

        for cluster in clusters:
            rep = cluster[0]
            rep_norm = normalize(rep["title"])
            # print(f"Processing:{rep_norm}")

            if similarity(norm_title, rep_norm) >= SIMILARITY_THRESHOLD:
                cluster.append(item)
                placed = True
                break

        if not placed:
            clusters.append([item])
    return clusters


def rank_clusters(clusters):
    clusters.sort(key=lambda x: len(x), reverse=True)
    return clusters

if __name__ == "__main__":
    import json
    with open("output_raw.json") as f:
        items = json.load(f)
    clusters = cluster_items(items)
    print("Clusters", len(clusters))