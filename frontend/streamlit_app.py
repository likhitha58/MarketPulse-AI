import streamlit as st
import requests

st.set_page_config(
    page_title="MarketPulse AI",
    page_icon="📈",
    layout="wide"
)

st.title("📈 MarketPulse AI")

st.subheader(
    "Multi-Agent Equity Research Platform"
)

ticker = st.text_input(
    "Enter Stock Ticker",
    placeholder="NVDA"
)

analyze_button = st.button(
    "Analyze Stock"
)
if analyze_button:

    response = requests.post(
        "http://127.0.0.1:8000/analyze",
        json={
            "ticker": ticker
        }
    )

    result = response.json()

    st.write(result)