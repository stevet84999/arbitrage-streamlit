import streamlit as st
import pandas as pd

st.set_page_config(page_title="Arbitrage Dashboard")

st.title("Arbitrage Betting Dashboard")

data = {
    "Event": ["Football", "Tennis", "Basketball"],
    "Bookmaker A Odds": [1.9, 2.1, 1.85],
    "Bookmaker B Odds": [2.05, 1.95, 1.9],
    "Arbitrage %": [1.2, 0.8, 1.5]
}

df = pd.DataFrame(data)
st.dataframe(df)
