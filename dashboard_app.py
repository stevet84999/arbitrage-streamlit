import streamlit as st
from odds_api import fetch_odds
from arbitrage_engine import detect_2way_arbitrage
import time

st.set_page_config(page_title="Arbitrage Dashboard", layout="wide")

st.title("🎯 Sports Arbitrage Opportunities")
st.caption("Real-time arbitrage detector for Football, Tennis, Basketball, Rugby, and Horse Racing")

min_profit = st.slider("Minimum Profit Margin (%)", 0.1, 10.0, 1.0, step=0.1)
st.markdown("---")

with st.spinner("Fetching odds and detecting arbitrage..."):
    odds_data = fetch_odds()
    arbs = []
    for event in odds_data:
        result = detect_2way_arbitrage(event)
        if result and result["profit_margin"] >= min_profit:
            arbs.append(result)

if arbs:
    st.success(f"✅ Found {len(arbs)} arbitrage opportunities!")
    for arb in arbs:
        st.subheader(f"{arb['event']} ({arb['sport'].title()})")
        num_cols = len(arb.get('odds', []))
if num_cols > 0:
    cols = st.columns(num_cols)
    for i, (bookmaker, odd) in enumerate(arb['odds'].items()):
        with cols[i]:
            st.write(f"**{bookmaker}**: {odd}")
else:
    st.warning("No odds data available for this event.")

        for idx, outcome in enumerate(arb['odds']):
            with cols[idx]:
                st.metric(
                    label=f"{outcome}",
                    value=f"Odds: {arb['odds'][outcome]}",
                    delta=f"Bookie: {arb['bookmakers'][outcome]}"
                )
        st.markdown(f"**Profit Margin:** {arb['profit_margin']}%")
        st.markdown("---")
else:
    st.warning("No arbitrage opportunities found with the current filters.")

st.caption("⏱️ Data refreshes each time you reload the page.")
