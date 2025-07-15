import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="Arbitrage Dashboard")
st.title("Arbitrage Betting Dashboard")

data = {
    "Event": ["Football", "Tennis", "Basketball"],
    "Bookmaker A Odds": [1.9, 2.1, 1.8],
    "Bookmaker B Odds": [2.05, 1.95, 2.0],
    "Arbitrage %": [1.2, 0.8, 1.5]
}
df = pd.DataFrame(data)
st.dataframe(df)

# 🔁 Add a live-updating clock to keep the app interactive
st.markdown("---")
st.subheader("Live Clock (Keeps App Active)")
placeholder = st.empty()

while True:
    placeholder.markdown(f"**Current time:** {time.strftime('%H:%M:%S')}")
    time.sleep(1)

