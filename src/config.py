RSS_FEEDS = [
    "https://openai.com/news/rss.xml",
    "https://huggingface.co/blog/feed.xml",
    "https://www.marktechpost.com/feed/",
    "https://venturebeat.com/category/ai/feed/",
    "https://techcrunch.com/tag/artificial-intelligence/feed/",
    "https://www.technologyreview.com/topic/artificial-intelligence/feed/",
    "https://www.theverge.com/rss/index.xml"
]


HN_SEARCH_TERMS = [
    "AI",
    "LLM",
    "large language model",
    "machine learning",
]

NEWSAPI_QUERY = "artificial intelligence OR LLM OR GPT OR machine learning"
SIMILARITY_THRESHOLD = 0.55
LOOKBACK_DAYS = 7
MIN_TOPICS = 5
MAX_TOPICS = 10


DIGEST_PROMPT = """You are curating a weekly AI news digest for a company portal.

Here are news clusters from this week:

{clstr}

Select 5-10 most important genuinely AI-relevant stories.
Ignore anything not directly about AI, machine learning, or LLMs.

Return ONLY valid JSON, no other text, no markdown:
{{
  "items": [
    {{
      "headline": "short headline",
      "summary": "2-3 sentence factual summary",
      "link": "url"
    }}
  ]
}}"""
CLAUDE_MODEL = "claude-sonnet-4-6"