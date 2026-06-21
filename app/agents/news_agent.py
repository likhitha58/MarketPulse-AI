from app.tools.news_tool import get_company_news
from app.config.groq_client import client
from app.utils.llm_helper import safe_generate


def news_agent(ticker):

    news = get_company_news(ticker)

    prompt = f"""
You are a financial news analyst.

Analyze:

{news}

Rules:
- Maximum 80 words
- Concise

Return:

SENTIMENT:
Bullish / Neutral / Bearish

POSITIVE:
- point
- point

NEGATIVE:
- point
- point

OUTLOOK:
1-2 sentences
"""

    return safe_generate(
    client,
    prompt
    )