import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet
import tempfile

# --------------------------------------------------
# Page Config
# --------------------------------------------------

if "result" not in st.session_state:
    st.session_state.result = None

if "ticker" not in st.session_state:
    st.session_state.ticker = ""
    
st.set_page_config(
    page_title="MarketPulse AI",
    page_icon="📈",
    layout="wide"
)

# --------------------------------------------------
# Watchlist
# --------------------------------------------------

if "watchlist" not in st.session_state:
    st.session_state.watchlist = []

st.sidebar.title(" -> Watchlist")

for stock in st.session_state.watchlist:
    st.sidebar.write(f"📈 {stock}")

# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("📈 MarketPulse AI")

st.markdown("""
### Multi-Agent Equity Research Platform

Analyze stocks using a team of AI investment analysts:

- Research Agent
- Financial Agent
- News Agent
- Bull Agent
- Bear Agent
- Risk Agent
- Investment Committee
""")

st.divider()

# --------------------------------------------------
# Input
# --------------------------------------------------

ticker = st.text_input(
    "Enter Company Name or Ticker",
    placeholder="NVIDIA, Apple, Tesla, NVDA, AAPL..."
)

analyze_button = st.button(
    "Analyze Stock",
    use_container_width=True
)


# --------------------------------------------------
# Analysis
# --------------------------------------------------

if analyze_button:

    if ticker.strip() == "":
        st.error("Please enter a stock ticker.")
        st.stop()

    with st.status(
        "Running Multi-Agent Analysis...",
        expanded=True
    ) as status:

        st.write("Research Agent analyzing company...")
        st.write("Financial Agent reviewing financials...")
        st.write("News Agent scanning headlines...")
        st.write("Bull Agent building investment thesis...")
        st.write("Bear Agent building counter-thesis...")
        st.write("Risk Agent assessing risks...")
        st.write("Committee Agent making final decision...")

        try:

            response = requests.post(
                "http://127.0.0.1:8000/analyze",
                json={
                    "ticker": ticker.upper()
                },
                timeout=300
            )

            if response.status_code != 200:
                st.error(
                    f"Backend Error: {response.status_code}"
                )
                st.stop()

            result = response.json()
            st.session_state.result = result
            st.session_state.ticker = ticker.upper()

        except Exception as e:

            st.error(
                f"Request Failed: {e}"
            )
            st.stop()

        status.update(
            label="✅ Analysis Complete",
            state="complete"
        )

if st.session_state.result:

    result = st.session_state.result
    ticker = st.session_state.ticker

    # --------------------------------------------------
    # Company Profile
    # --------------------------------------------------

    company = result.get(
        "company_info",
        {}
    )

    st.subheader(
        company.get(
            "name",
            ticker.upper()
        )
    )

    c1, c2 = st.columns(2)

    with c1:

        st.write(
            f"**Sector:** {company.get('sector', 'N/A')}"
        )

        st.write(
            f"**Industry:** {company.get('industry', 'N/A')}"
        )

    with c2:

        st.write(
            f"**Country:** {company.get('country', 'N/A')}"
        )

        st.write(
            f"**Employees:** {company.get('employees', 'N/A')}"
        )

    st.divider()

    # --------------------------------------------------
    # Market Snapshot
    # --------------------------------------------------

    st.subheader("📊 Market Snapshot")

    metrics = result.get(
        "metrics",
        {}
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Ticker",
            ticker.upper()
        )

    with col2:
        st.metric(
            "Price",
            metrics.get(
                "price",
                "N/A"
            )
        )

    with col3:
        st.metric(
            "Market Cap",
            metrics.get(
                "market_cap",
                "N/A"
            )
        )

    with col4:
        st.metric(
            "P/E Ratio",
            metrics.get(
                "pe_ratio",
                "N/A"
            )
        )

    st.caption(
        f"Sector: {metrics.get('sector', 'Unknown')}"
    )

    if st.button("➕ Add To Watchlist"):

        if ticker.upper() not in st.session_state.watchlist:

            st.session_state.watchlist.append(
                ticker.upper()
            )

            st.success(
                f"{ticker.upper()} added to watchlist."
            )

    st.divider()

    # --------------------------------------------------
    # Stock Chart
    # --------------------------------------------------

    chart = result.get(
        "chart_data",
        {}
    )

    if chart:

        st.subheader(
            "📈 1-Year Stock Performance"
        )

        df = pd.DataFrame({

            "Date": chart["dates"],
            "Price": chart["prices"]

        })

        fig = px.line(
            df,
            x="Date",
            y="Price",
            title=f"{ticker.upper()} Stock Price"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    # --------------------------------------------------
    # Recommendation
    # --------------------------------------------------

    recommendation_text = result.get(
        "recommendation",
        "No recommendation available."
    )

    confidence = 0

    if "CONFIDENCE SCORE:" in recommendation_text.upper():

        try:

            confidence = int(
                recommendation_text
                .upper()
                .split(
                    "CONFIDENCE SCORE:"
                )[1]
                .split("%")[0]
                .strip()
            )

        except:
            confidence = 0

    st.subheader(
        "Investment Committee Decision"
    )
    
    left, right = st.columns([1, 3])

    with left:

        text = recommendation_text.upper()

        if "BUY" in text:

            st.success("BUY")

        elif "SELL" in text:

            st.error("SELL")

        else:

            st.warning("HOLD")

    with right:

        st.markdown(
            f"""
### Committee Analysis

{recommendation_text}
"""
        )

    # --------------------------------------------------
    # Confidence Meter
    # --------------------------------------------------

    st.subheader(
        "Confidence Score"
    )

    st.progress(
        confidence / 100
    )

    st.caption(
        f"{confidence}%"
    )

    # --------------------------------------------------
    # Recommendation Gauge
    # --------------------------------------------------

    value = 50

    if "BUY" in recommendation_text.upper():
        value = 90

    elif "SELL" in recommendation_text.upper():
        value = 10

    fig = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=value,

            title={
                "text":
                "Recommendation Strength"
            },

            gauge={
                "axis": {
                    "range": [0, 100]
                }
            }
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # --------------------------------------------------
    # Risk Score
    # --------------------------------------------------

    risk_text = result.get(
        "risk_report",
        ""
    )

    risk_score = "N/A"

    if "Risk Score:" in risk_text:

        try:

            risk_score = (
                risk_text
                .split("Risk Score:")[1]
                .split("\n")[0]
                .strip()
            )

        except:
            pass

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Risk Score",
            risk_score
        )

    with col2:
        st.metric(
            "Analysis Status",
            "Complete"
        )

    st.divider()

    # --------------------------------------------------
    # Thesis
    # --------------------------------------------------

    st.subheader(
        "📈 Investment Thesis"
    )

    with st.expander(
        "Bull Case",
        expanded=True
    ):
        st.write(
            result.get(
                "bull_case",
                ""
            )
        )

    with st.expander(
        "Bear Case"
    ):
        st.write(
            result.get(
                "bear_case",
                ""
            )
        )

    with st.expander(
        "Risk Assessment"
    ):
        st.write(
            result.get(
                "risk_report",
                ""
            )
        )

    st.divider()

    # --------------------------------------------------
    # Reports
    # --------------------------------------------------

    st.subheader(
        "Supporting Analysis"
    )

    with st.expander(
        "Financial Report"
    ):
        st.write(
            result.get(
                "financial_report",
                ""
            )
        )

    with st.expander(
        "News Report"
    ):
        st.write(
            result.get(
                "news_report",
                ""
            )
        )

    with st.expander(
        "Full Research Report"
    ):
        st.write(
            result.get(
                "research_report",
                ""
            )
        )

    st.divider()

    # --------------------------------------------------
    # Timeline
    # --------------------------------------------------

    st.divider()

    st.subheader(
        "📄 Export Report"
    )

    if st.button(
        "Generate PDF Report"
    ):

        pdf_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        )

        pdf = SimpleDocTemplate(
            pdf_file.name
        )

        styles = getSampleStyleSheet()

        elements = [

            Paragraph(
                "MarketPulse AI Report",
                styles["Title"]
            ),

            Paragraph(
                f"Ticker: {ticker.upper()}",
                styles["BodyText"]
            ),

            Paragraph(
                recommendation_text,
                styles["BodyText"]
            ),

            Paragraph(
                result.get(
                    "bull_case",
                    ""
                ),
                styles["BodyText"]
            ),

            Paragraph(
                result.get(
                    "bear_case",
                    ""
                ),
                styles["BodyText"]
            ),

            Paragraph(
                result.get(
                    "risk_report",
                    ""
                ),
                styles["BodyText"]
            )

        ]

        pdf.build(elements)

        with open(
            pdf_file.name,
            "rb"
        ) as f:

            st.download_button(
                "⬇ Download PDF",
                f,
                file_name=f"{ticker.upper()}_Report.pdf",
                mime="application/pdf"
            )

    st.subheader(
        "Agent Activity Timeline"
    )

    st.markdown("""
✅ Research Agent Complete

✅ Financial Agent Complete

✅ News Agent Complete

✅ Bull Agent Complete

✅ Bear Agent Complete

✅ Risk Agent Complete

✅ Investment Committee Complete
""")
