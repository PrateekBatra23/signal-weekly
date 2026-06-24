import anthropic
import json
import os
from config import DIGEST_PROMPT, CLAUDE_MODEL,SHORTLIST_PROMPT
from rank import cluster_items
from dotenv import load_dotenv
load_dotenv()

def extarct_json(text):
    start = text.find("{")
    end = text.rfind("}") + 1
    if start == -1 or end == 0:
        raise ValueError("No JSON found in response")
    return json.loads(text[start:end])

def summarize_clusters(clusters, method=0):
    # print("Cluster", clusters)
    if method == 0:
        cluster_input = []
        for c in clusters:
            cluster_input.append({
                "title": c[0]["title"],
                "sources": list({item["source"] for item in c}),
                "link": c[0]["link"],
                "num_articles": len(c)
            })
        prompt = SHORTLIST_PROMPT.format(clstr=json.dumps(cluster_input, indent=2))
        MAX_TOKEN_COUNT = 3000
    else:
        prompt = DIGEST_PROMPT.format(clstr=json.dumps(clusters, indent=2))
        MAX_TOKEN_COUNT = 700

    client = anthropic.Anthropic()
    response = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=MAX_TOKEN_COUNT,
        messages=[{"role": "user", "content": prompt}]
    )
    text = response.content[0].text.strip()

    return extarct_json(text)

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