import streamlit as st
from arbitrage_engine import find_arbitrage_opportunities
from odds_api import fetch_odds
from config import SPORTS, BOOKMAKERS

st.set_page_config(page_title="Sports Arbitrage Dashboard", layout="wide")

st.title("🎯 Sports Arbitrage Opportunities")
st.markdown("Real-time arbitrage detector for Football, Tennis, Basketball, Rugby, and Horse Racing")

min_profit_margin = st.slider(
    "Minimum Profit Margin (%)", min_value=0.1, max_value=10




