import streamlit as st
from arbitrage_engine import find_arbitrage_opportunities
from odds_api import fetch_odds
from config import SPORTS, BOOKMAKERS, MIN_PROFIT_MARGIN

st.set_page_config(page_title="Arbitrage Betting Dashboard", layout="wide")

st.title("💸 Real-Time Arbitrage Betting Dashboard")
st.markdown("Track live arbitrage opportunities across Football, Tennis, Basketball, Rugby, and Horse Racing.")

st.sidebar.header("⚙️ Settings")

min_profit_margin = st.sidebar.slider(
    "Minimum Profit Margin (%)", 
    min_value=0.1, 
    max_value=10.0, 
    value=MIN_PROFIT_MARGIN, 
    step=0.1
)

if st.button("🔍 Scan for Arbitrage Opportunities"):
    with st.spinner("Fetching live odds and calculating arbitrage..."):
        odds_data = fetch_odds(SPORTS, BOOKMAKERS)
        arbs = find_arbitrage_opportunities(odds_data, min_profit_margin)

    if arbs:
        st.success(f"Found {len(arbs)} arbitrage opportunities!")
        for arb in arbs:
            st.markdown("---")
            st.write(arb)
    else:
        st.info("No arbitrage opportunities found.")
 found. Try adjusting the profit margin or checking later.")
