import os

# Sports to track
SPORTS = ["soccer", "basketball", "tennis", "rugby_union", "horse_racing"]

# Bookmakers to prioritise
BOOKMAKERS = ["coral", "ladbrokes", "betfred"]

# Odds API settings (loaded securely from environment)
API_KEY = os.getenv("ODDS_API_KEY")
REGIONS = "uk"
MARKETS = "h2h"
