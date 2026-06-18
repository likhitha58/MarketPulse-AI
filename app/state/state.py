from typing import TypedDict

class AgentState(TypedDict):

    ticker: str

    company_name: str

    research_report: str

    financial_report: str

    news_report: str
    
    bull_case: str

    bear_case: str
    
    risk_report: str

    final_recommendation: str

    