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


SHORTLIST_PROMPT = """You are curating "Last Week in AI" for the Centre for Architecture & AI community at Hitachi Digital Services. Audience: enterprise architects, AI engineers, technology leaders who follow AI closely.

Here are news clusters from this week:

{clstr}

Select 8-10 stories using these criteria:

STRONGLY PREFER:
- Agentic AI advances — frameworks, control architectures, multi-agent orchestration, harness engineering, agent reliability
- Platform-level architectural shifts — when a major platform (Salesforce, Microsoft, Google Cloud, AWS) restructures itself around agents or AI-first operation
- Enterprise infrastructure for AI — MCP servers, context layers, payment rails, data governance, observability
- Security and dual-use — AI finding vulnerabilities, offensive security agents, governance failures, benchmark integrity
- Research with enterprise implications — capability acceleration reports, evaluation framework problems, governance gaps
- Open source tooling with real production value — agent runtimes, frameworks, CLIs engineers would actually use
- Model releases that shift the competitive landscape — architectural changes, not incremental updates

INCLUDE OCCASIONALLY:
- Surprising AI capability demonstrations revealing something genuinely new
- Long-arc research pointing to where computation or AI systems are heading

EXCLUDE ALWAYS:
- Consumer healthcare or wellness features
- Generic business news with weak AI angle
- Incremental model version bumps with no architectural change
- Academic papers without near-term practical implications
- Marketing announcements without technical substance

SUMMARY LENGTH GUIDANCE:
- For platform-level architectural shifts or major capability expansions: 5-6 sentences
- For significant but narrower releases: 3-4 sentences
- Always explain: what it is, what specifically changed, why it matters for architects or engineers building with AI

Be technically precise and opinionated about significance. If something represents a strategic shift, say so explicitly.

Return ONLY valid JSON, no other text, no markdown:
{{
  "items": [
    {{
      "headline": "concise factual headline",
      "summary": "3-6 sentences depending on significance",
      "link": "url"
    }}
  ]
}}"""
DIGEST_PROMPT = """You are writing the intro for "Last Week in AI" posted in the Centre for Architecture & AI community at Hitachi Digital Services on Viva Engage. The audience is enterprise architects, AI engineers, and technology leaders who follow AI developments closely.

Here are the selected stories:

{clstr}

Write the overall summary paragraph in this exact style — opinionated, thematic, technically precise, connecting individual stories into a single narrative about what the week means:

Example style:
"This week in AI was quite interesting, with the industry shifting from model launches toward the infrastructure needed to run autonomous systems reliably at scale, where persistent agent control loops, native payment rails, interpretability tooling, and governed enterprise context layers pointed to a new phase where orchestration, durability, and oversight matter as much as raw model capability. We saw major movement in production agent engineering: OpenAI and Anthropic introduced competing control architectures for long-running tasks, AWS added native transactional infrastructure for agents, Google pushed faster inference and continuous optimisation systems into production, and Microsoft focused on testing and benchmarking frameworks for agent reliability."

Rules:
- Open by identifying the dominant theme or shift of the week
- Name specific companies and what they specifically did
- Connect stories into a coherent narrative — not a list of events
- End with the broader implication for enterprise AI or architecture teams
- Be opinionated about significance — say what matters and why
- Tone: authoritative, analytical, technically informed — not neutral reporting, not hype
- Length: 4-6 sentences, dense with substance

Return ONLY valid JSON, no other text, no markdown:
{{
  "overall_summary": "4-6 sentence thematic overview"
}}"""
CLAUDE_MODEL = "claude-sonnet-4-6"