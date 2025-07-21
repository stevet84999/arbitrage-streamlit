import streamlit as st
from arbitrage_engine import find_arbitrage_opportunities
from odds_api import fetch_all_odds
from config import SPORTS, PRIORITY_BOOKMAKERS

st.set_page_config(page_title="Arbitrage Dashboard", layout="wide")

st.title("🎯 Sports Arbitrage Opportunities")
st.caption("Real-time arbitrage detector for Football, Tennis, Basketball, Rugby, and Horse Racing")

min_profit = st.slider("Minimum Profit Margin (%)", min_value=0.1, max_value=10.0, value=1.0, step=0.1)

# Fetch & process
with st.spinner("Fetching live odds and calculating arbitrage..."):
    odds_data = fetch_all_odds(SPORTS)
    arbs = find_arbitrage_opportunities(odds_data, min_profit=min_profit, priority_bookmakers=PRIORITY_BOOKMAKERS)

if not arbs:
    st.info("No arbitrage opportunities found at this time.")
else:
    st.success(f"✅ Found {len(arbs)} arbitrage opportunities!")

    for arb in arbs:
        st.subheader(f"{arb['event']} ({arb['sport'].title()})")

        num_cols = len(arb.get('odds', []))
        if num_cols > 0:
            cols = st.columns(num_cols)

            # Display bookmaker odds
            for i, (bookmaker, odd) in enumerate(arb['odds'].items()):
                with cols[i]:
                    st.write(f"**{bookmaker}**: {odd}")

            # Display profit metric
            for idx, outcome in enumerate(arb['odds']):
                with cols[idx]:
                    st.metric(label=outcome, value=f"{arb['profit_margin']:.2f}%")
        else:
            st.warning("No odds data available for this event.")

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
