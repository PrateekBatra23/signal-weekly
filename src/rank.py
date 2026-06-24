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

def filter_published(clusters, published):
    from rank import similarity, normalize
    filtered = []
    for cluster in clusters:
        title = normalize(cluster[0]["title"])
        link = cluster[0]["link"]

        is_duplicate = False
        for p in published:
            if link == p["link"]:
                is_duplicate = True
                break
            if similarity(title, normalize(p["headline"])) >= 0.55:
                is_duplicate = True

        if not is_duplicate:
            filtered.append(cluster)
    return filtered

if __name__ == "__main__":
    import json
    with open("output_raw.json") as f:
        items = json.load(f)
    clusters = cluster_items(items)
    print("Clusters", len(clusters))