import streamlit as st
from config import APP_TITLE, APP_DESCRIPTION
from market_data import get_stock_data

st.set_page_config(
    page_title=APP_TITLE,
    page_icon="📈",
    layout="wide"
)

st.title(APP_TITLE)
st.write(APP_DESCRIPTION)

st.markdown(
    """
    ### Intelligent Stock Market Analysis Platform

    StockSense is a personal project for analyzing stock market data,
    exploring trends, and developing data-driven insights.

    🚧 **Development in progress**
    """
)

st.divider()

st.subheader("Project Modules")

st.divider()

st.subheader("📊 Market Data")

ticker = st.text_input(
    "Enter Stock Symbol",
    value="AAPL"
).upper()

period = st.selectbox(
    "Select Period",
    ["1mo", "3mo", "6mo", "1y", "2y", "5y"]
)

if st.button("Load Market Data"):
    with st.spinner("Fetching market data..."):
        data = get_stock_data(ticker, period)

    if data.empty:
        st.error("No market data found. Please check the stock symbol.")
    else:
        st.success(f"Market data loaded for {ticker}")

        st.subheader(f"{ticker} Historical Data")
        st.dataframe(data, use_container_width=True)

        st.subheader(f"{ticker} Closing Price")

        if "Close" in data.columns:
            st.line_chart(data["Close"])

col1, col2, col3 = st.columns(3)

with col1:
    st.info("📊 Market Data\n\nData collection and processing")

with col2:
    st.info("🤖 Machine Learning\n\nPrediction and analysis")

with col3:
    st.info("📈 Visualization\n\nCharts and market insights")