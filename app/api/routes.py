from pydantic import BaseModel
from fastapi import APIRouter
from app.graph.workflow import graph

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

    return {
    "ticker": result["ticker"],
    "recommendation": result["final_recommendation"],
    "bull_case": result["bull_case"],
    "bear_case": result["bear_case"],
    "risk_report": result["risk_report"]
}