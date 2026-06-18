from tools.news_tool import get_company_news
from config.gemini import client


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

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text