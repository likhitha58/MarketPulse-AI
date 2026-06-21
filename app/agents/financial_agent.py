from app.tools.financial_tool import get_financial_data
from app.config.groq_client import client
from app.utils.llm_helper import safe_generate


def financial_agent(ticker):

    financial_data = get_financial_data(ticker)

    prompt = f"""
You are a senior equity analyst.

Financial Data:

Revenue: {financial_data.get('revenue')}
Net Income: {financial_data.get('net_income')}
Cash: {financial_data.get('cash')}
Debt: {financial_data.get('debt')}
Operating Cash Flow: {financial_data.get('operating_cash_flow')}
P/E Ratio: {financial_data.get('pe_ratio')}
Profit Margin: {financial_data.get('profit_margin')}

Rules:
- Maximum 120 words
- No long explanations

Return EXACTLY:

REVENUE:
1 sentence

PROFITABILITY:
1 sentence

DEBT:
1 sentence

FINANCIAL HEALTH:
Strong / Average / Weak

SUMMARY:
2 sentences
"""

    return safe_generate(
    client,
    prompt
    )
