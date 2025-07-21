import streamlit as st
from arbitrage_engine import find_arbitrage_opportunities
from odds_api import get_odds_for_all_sports

st.set_page_config(page_title="Arbitrage Betting Dashboard", layout="wide")

st.title("🎯 Sports Arbitrage Opportunities")
st.markdown("Real-time arbitrage detector for Football, Tennis, Basketball, Rugby, and Horse Racing")

# Margin slider
min_profit_margin = st.slider(
    "Minimum Profit Margin (%)",
    min_value=0.1,
    max_value=10.0,
    value=1.0,
    step=0.1,
    format="%.2f"
)

# Load odds
with st.spinner("Fetching latest odds..."):
    all_odds = get_odds_for_all_sports()

# Detect arbitrage opportunities
arbs = find_arbitrage_opportunities(all_odds, min_profit_margin)

if not arbs:
    st.warning("No arbitrage opportunities found at this margin.")
else:
    st.success(f"✅ Found {len(arbs)} arbitrage opportunities!")

    for arb in arbs:
        st.subheader(f"{arb['event']} ({arb['sport'].title()})")

        num_cols = len(arb.get('odds', {}))
        if num_cols > 0:
            cols = st.columns(num_cols)
            for i, (bookmaker, odd) in enumerate(arb['odds'].items()):
                with cols[i]:
                    st.write(f"**{bookmaker}**: {odd}")
        else:
            st.warning("No odds data available for this event.")

        st.markdown("---")



