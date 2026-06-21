import streamlit as st
import requests

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="MarketPulse AI",
    page_icon="📈",
    layout="wide"
)

# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("📈 MarketPulse AI")

st.markdown("""
### Multi-Agent Equity Research Platform

Analyze stocks using a team of AI investment analysts:

- 🧠 Research Agent
- 📊 Financial Agent
- 📰 News Agent
- 🐂 Bull Agent
- 🐻 Bear Agent
- ⚠️ Risk Agent
- 🏛️ Investment Committee
""")

st.divider()

# --------------------------------------------------
# Input Section
# --------------------------------------------------

ticker = st.text_input(
    "Enter Stock Ticker",
    placeholder="NVDA, AAPL, MSFT, GOOGL..."
)

analyze_button = st.button(
    "🚀 Analyze Stock",
    use_container_width=True
)

# --------------------------------------------------
# Run Analysis
# --------------------------------------------------

if analyze_button:

    if ticker.strip() == "":
        st.error("Please enter a stock ticker.")
        st.stop()

    with st.status(
        "Running Multi-Agent Analysis...",
        expanded=True
    ) as status:

        st.write("🧠 Research Agent analyzing company...")
        st.write("📊 Financial Agent reviewing financials...")
        st.write("📰 News Agent scanning headlines...")
        st.write("🐂 Bull Agent building investment thesis...")
        st.write("🐻 Bear Agent building counter-thesis...")
        st.write("⚠️ Risk Agent assessing risks...")
        st.write("🏛️ Committee Agent making final decision...")

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

        except Exception as e:

            st.error(
                f"Request Failed: {e}"
            )

            st.stop()

        status.update(
            label="✅ Analysis Complete",
            state="complete"
        )

    # --------------------------------------------------
    # Market Snapshot
    # --------------------------------------------------

    st.divider()

    st.subheader("📊 Market Snapshot")

    metrics = result.get("metrics", {})

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Ticker",
            ticker.upper()
        )

    with col2:
        st.metric(
            "Price",
            metrics.get("price", "N/A")
        )

    with col3:
        st.metric(
            "Market Cap",
            metrics.get("market_cap", "N/A")
        )

    with col4:
        st.metric(
            "P/E Ratio",
            metrics.get("pe_ratio", "N/A")
        )

    st.caption(
        f"Sector: {metrics.get('sector', 'Unknown')}"
    )

    # --------------------------------------------------
    # Committee Decision
    # --------------------------------------------------

    st.divider()

    recommendation_text = result.get(
        "recommendation",
        result.get(
            "final_recommendation",
            "No recommendation available."
        )
    )

    st.subheader("🏛️ Investment Committee Decision")

    left, right = st.columns([1, 3])

    with left:

        recommendation_upper = recommendation_text.upper()

        if "BUY" in recommendation_upper:
            st.success("BUY")

        elif "SELL" in recommendation_upper:
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
    # Risk Metrics
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

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Risk Score",
            risk_score
        )

    with col2:

        st.metric(
            "Agents Used",
            "7"
        )

    # --------------------------------------------------
    # Investment Thesis
    # --------------------------------------------------

    st.divider()

    st.subheader("📈 Investment Thesis")

    if "bull_case" in result:

        with st.expander(
            "🐂 Bull Case",
            expanded=True
        ):
            st.write(
                result["bull_case"]
            )

    if "bear_case" in result:

        with st.expander(
            "🐻 Bear Case"
        ):
            st.write(
                result["bear_case"]
            )

    if "risk_report" in result:

        with st.expander(
            "⚠️ Risk Assessment"
        ):
            st.write(
                result["risk_report"]
            )

    # --------------------------------------------------
    # Supporting Analysis
    # --------------------------------------------------

    st.divider()

    st.subheader("📚 Supporting Analysis")

    if "financial_report" in result:

        with st.expander(
            "📊 Financial Report"
        ):
            st.write(
                result["financial_report"]
            )

    if "news_report" in result:

        with st.expander(
            "📰 News Report"
        ):
            st.write(
                result["news_report"]
            )

    if "research_report" in result:

        with st.expander(
            "🧠 Full Research Report"
        ):
            st.write(
                result["research_report"]
            )

    # --------------------------------------------------
    # Timeline
    # --------------------------------------------------

    st.divider()

    st.subheader(
        "🕒 Agent Activity Timeline"
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