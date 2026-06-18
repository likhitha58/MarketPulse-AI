from typing import TypedDict


class AgentState(TypedDict):
    ticker: str
    company_name: str
    research_report: str
    financial_report: str
    decision: str