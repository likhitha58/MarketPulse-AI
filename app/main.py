from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="MarketPulse AI API",
    description="Multi-Agent Equity Research Platform powered by LangGraph, Groq and DeepSeek",
    version="1.0.0"
)

app.include_router(router)