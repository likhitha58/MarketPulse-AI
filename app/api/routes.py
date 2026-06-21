from pydantic import BaseModel
from fastapi import APIRouter

from app.graph.workflow import graph
from app.tools.yfinance_tool import get_stock_metrics


class AnalyzeRequest(BaseModel):
    ticker: str


router = APIRouter()


@router.get("/")
def home():

    return {
        "message": "MarketPulse AI API Running"
    }


@router.post("/analyze")
def analyze_stock(request: AnalyzeRequest):

    initial_state = {

        "ticker": request.ticker,

        "company_name": "",

        "research_report": "",

        "financial_report": "",

        "news_report": "",

        "bull_case": "",

        "bear_case": "",

        "risk_report": "",

        "final_recommendation": ""

    }

    result = graph.invoke(initial_state)

    metrics = get_stock_metrics(
        request.ticker
    )

    return {

    "ticker": result["ticker"],

    "metrics": metrics,

    "recommendation":
        result["final_recommendation"],

    "research_report":
        result["research_report"],

    "financial_report":
        result["financial_report"],

    "news_report":
        result["news_report"],

    "bull_case":
        result["bull_case"],

    "bear_case":
        result["bear_case"],

    "risk_report":
        result["risk_report"]

}