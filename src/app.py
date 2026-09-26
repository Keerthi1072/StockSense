import streamlit as st
from config import APP_TITLE, APP_DESCRIPTION

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

col1, col2, col3 = st.columns(3)

with col1:
    st.info("📊 Market Data\n\nData collection and processing")

with col2:
    st.info("🤖 Machine Learning\n\nPrediction and analysis")

with col3:
    st.info("📈 Visualization\n\nCharts and market insights")