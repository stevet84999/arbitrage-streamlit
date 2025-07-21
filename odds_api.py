import requests
from config import API_KEY, REGIONS, MARKETS, ODDS_API_URL

def fetch_odds(sports, bookmakers):
    if not API_KEY:
        raise ValueError("Missing API_KEY. Please add it to config.py")

    headers = {"x-apisports-key": API_KEY}
    all_odds = {}

    for sport in sports:
        url = f"{ODDS_API_URL}/{sport}/odds"
        params = {
            "regions": REGIONS,
            "markets": MARKETS,
            "bookmakers": ",".join(bookmakers)
        }

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            all_odds[sport] = data.get("data", [])
        except Exception as e:
            print(f"Error fetching odds for {sport}: {e}")

    return all_odds


