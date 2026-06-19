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
# Analysis Section
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
        st.write("📊 Financial Agent reviewing statements...")
        st.write("📰 News Agent scanning market news...")
        st.write("🐂 Bull Agent building bullish thesis...")
        st.write("🐻 Bear Agent building bearish thesis...")
        st.write("⚠️ Risk Agent assessing risks...")
        st.write("🏛️ Investment Committee making final decision...")

        response = requests.post(
            "http://127.0.0.1:8000/analyze",
            json={
                "ticker": ticker.upper()
            }
        )

        if response.status_code != 200:
            st.error(
                f"Backend Error: {response.status_code}"
            )
            st.stop()

        result = response.json()
        st.write(result)

        status.update(
            label="✅ Analysis Complete",
            state="complete"
        )

    # --------------------------------------------------
    # Dashboard
    # --------------------------------------------------

    st.divider()

    st.subheader("📊 Investment Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="Stock",
            value=ticker.upper()
        )

    with col2:
        st.metric(
            label="Agents",
            value="7"
        )

    with col3:
        st.metric(
            label="Status",
            value="Completed"
        )

    st.divider()

    # --------------------------------------------------
    # Final Recommendation
    # --------------------------------------------------

    st.subheader("🏛️ Final Recommendation")

    st.success(
        result["recommendation"]
    )

    # --------------------------------------------------
    # Agent Reports
    # --------------------------------------------------

    with st.expander("🧠 Research Report"):
        st.write(
            result["research_report"]
        )

    with st.expander("📊 Financial Report"):
        st.write(
            result["financial_report"]
        )

    with st.expander("📰 News Report"):
        st.write(
            result["news_report"]
        )

    with st.expander("🐂 Bull Case"):
        st.write(
            result["bull_case"]
        )

    with st.expander("🐻 Bear Case"):
        st.write(
            result["bear_case"]
        )

    with st.expander("⚠️ Risk Assessment"):
        st.write(
            result["risk_report"]
        )

    # --------------------------------------------------
    # Timeline
    # --------------------------------------------------

    st.divider()

    st.subheader("🕒 Agent Activity Timeline")

    st.markdown("""
✅ Research Agent Complete

✅ Financial Agent Complete

✅ News Agent Complete

✅ Bull Agent Complete

✅ Bear Agent Complete

✅ Risk Agent Complete

✅ Investment Committee Complete
""")