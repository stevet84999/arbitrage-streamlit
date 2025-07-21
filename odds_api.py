import requests
from config import API_KEY, REGIONS, MARKET, SPORTS

def fetch_odds():
    all_odds = []
    for sport_name, sport_key in SPORTS.items():
        url = f"https://api.the-odds-api.com/v4/sports/{sport_key}/odds"
        params = {
            "apiKey": API_KEY,
            "regions": REGIONS,
            "markets": MARKET,
            "oddsFormat": "decimal"
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            for event in data:
                event['sport_name'] = sport_name
            all_odds.extend(data)
        else:
            print(f"Failed to fetch {sport_name}: {response.status_code}")
    return all_odds
