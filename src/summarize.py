import anthropic
import json
import os
from config import DIGEST_PROMPT, CLAUDE_MODEL
from rank import cluster_items
from dotenv import load_dotenv
load_dotenv()


def summarize_clusters(clusters):
    # print("Cluster", clusters)
    client = anthropic.Anthropic()
    cluster_input = []
    clusters = clusters[:10]
    for c in clusters:
        cluster_input.append({
            "title": c[0]["title"],
            "sources": list({item["source"] for item in c}),
            "link": c[0]["link"],
            "num_articles": len(c)
        })
    prompt = DIGEST_PROMPT.format(clstr=json.dumps(cluster_input, indent=2))
    response = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}]
    )
    text = response.content[0].text.strip()
    # text= " "
    # print("RAW Response", text)
    if text.startswith("```"):
        text = text.strip("```").strip()
        if text.startswith("json"):
            text = text[4:].strip()
    return json.loads(text)

if __name__ == "__main__":
    import json
    with open("output_raw.json") as f:
        items = json.load(f)
    from rank import cluster_items, rank_clusters
    clusters = cluster_items(items)
    # print("Cluster", len(clusters))
    result = summarize_clusters(clusters)
    for item in result["items"]:
        print(f"\n{item['headline']}")
        print(item['summary'])
        print(item['link'])