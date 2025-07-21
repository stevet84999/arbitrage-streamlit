import streamlit as st
from arbitrage_engine import find_arbitrage_opportunities
from odds_api import fetch_odds
from config import SPORTS, BOOKMAKERS

st.set_page_config(page_title="Sports Arbitrage Dashboard", layout="wide")

st.title("🎯 Sports Arbitrage Opportunities")
st.markdown("Real-time arbitrage detector for Football, Tennis, Basketball, Rugby, and Horse Racing")

# ✅ Fixed: properly closed st.slider()
min_profit_margin = st.slider("Minimum Profit Margin (%)", min_value=0.1, max_value=10.0, value=1.0, step=0.1)

if st.button("🔍 Scan for Arbitrage Opportunities"):
    with st.spinner("Fetching live odds and detecting arbitrage..."):
        odds_data = fetch_odds(SPORTS, BOOKMAKERS)
        arbs = find_arbitrage_opportunities(odds_data, min_profit_percent=min_profit_margin)

    if arbs:
        st.success(f"✅ Found {len(arbs)} arbitrage opportunities!")

        for arb in arbs:
            st.subheader(f"{arb['event']} ({arb['sport'].title()})")
            
            odds = arb.get('odds', {})
            if odds:
                cols = st.columns(len(odds))
                for i, (bookmaker, odd) in enumerate(odds.items()):
                    with cols[i]:
                        st.write(f"**{bookmaker}**: {odd}")
            else:
                st.warning("No odds data available for this event.")

            st.markdown(f"**Profit Margin:** `{arb['profit_percent']:.2f}%`")
            st.markdown("---")
    else:
        st.warning("❌ No arbitrage opportunities found. Try adjusting the profit margin or checking later.")
