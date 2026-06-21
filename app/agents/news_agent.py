from app.tools.news_tool import get_company_news
from app.config.groq_client import client
from app.utils.llm_helper import safe_generate


def news_agent(ticker):

    news = get_company_news(ticker)

    prompt = f"""
You are a financial news analyst.

Analyze the following news:

{news}

Return ONLY the following format:

NEWS SENTIMENT:
Bullish / Neutral / Bearish

POSITIVE CATALYSTS:
- point 1
- point 2
- point 3

NEGATIVE CATALYSTS:
- point 1
- point 2
- point 3

OUTLOOK:
2-3 sentence summary.
"""

    return safe_generate(
    client,
    prompt
    )