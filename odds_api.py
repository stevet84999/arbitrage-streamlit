import requests
from config import API_KEY, REGIONS, MARKETS

def fetch_odds(sports, bookmakers):
    if not API_KEY:
        raise ValueError("ODDS_API_KEY is missing. Please add it to Streamlit secrets.")

    base_url = "https://api.the-odds-api.com/v4/sports/odds"
    all_odds = []

    for sport in sports:
        response = requests.get(base_url, params={
            "apiKey": API_KEY,
            "sport": sport,
            "regions": REGIONS,
            "markets": MARKETS,
            "oddsFormat": "decimal",
            "bookmakers": ",".join(bookmakers)
        })

        if response.status_code == 200:
            try:
                all_odds.extend(response.json())
            except Exception as e:
                print(f"JSON parse error for {sport}: {e}")
        else:
            print(f"Error fetching odds for {sport}: {response.status_code} {response.text}")

    return all_odds

