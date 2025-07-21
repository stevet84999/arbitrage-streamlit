# config.py

API_KEY = "817c309e5d37829ba411d488fdab5e2a"  # Replace with your key if not already

SPORTS = {
    "Football": "soccer",
    "Tennis": "tennis",
    "Basketball": "basketball",
    "Horse Racing": "horse_racing"
}

BOOKMAKERS = ["coral", "ladbrokes", "betfred"]

REGIONS = "uk"  # or "us" if you want US-based bookmakers
MARKETS = "h2h"
ODDS_FORMAT = "decimal"
DATE_FORMAT = "iso"
 os

# Sports to track
SPORTS = ["soccer", "basketball", "tennis", "rugby_union", "horse_racing"]

# Bookmakers to prioritise
BOOKMAKERS = ["coral", "ladbrokes", "betfred"]

# Odds API settings (loaded securely from environment)
API_KEY = os.getenv("ODDS_API_KEY")
REGIONS = "uk"
MARKETS = "h2h"
