from pydantic import BaseModel
from fastapi import APIRouter

from app.graph.workflow import graph
from app.tools.chart_tool import get_stock_history
from app.tools.yfinance_tool import (
    get_stock_metrics,
    get_company_info
)
from app.tools.search_tool import resolve_ticker

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
    ticker = resolve_ticker(
        request.ticker
    )
    initial_state = {

        "ticker": ticker,

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
        ticker
    )
    
    company_info = get_company_info(
        ticker
    )

    history = get_stock_history(
        ticker
    )

    chart_data = {

        "dates":
            history.index.strftime(
                "%Y-%m-%d"
            ).tolist(),

        "prices":
            history["Close"].round(
                2
            ).tolist()
    }

    return {

        "ticker":
            ticker,

        "metrics":
            metrics,
        
        "company_info":
            company_info,

        "chart_data":
            chart_data,

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