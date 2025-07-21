def detect_2way_arbitrage(event):
    arbitrage_opportunities = []
    team_names = []

    for bookmaker in event['bookmakers']:
        for market in bookmaker['markets']:
            if market['key'] == 'h2h' and len(market['outcomes']) == 2:
                team1 = market['outcomes'][0]
                team2 = market['outcomes'][1]
                team_names = [team1['name'], team2['name']]
                arbitrage_opportunities.append({
                    "bookmaker": bookmaker['key'],
                    team1['name']: team1['price'],
                    team2['name']: team2['price']
                })

    best_odds = {}
    best_bookies = {}
    for outcome in team_names:
        best_odds[outcome] = 0
        best_bookies[outcome] = ""

    for bookie in arbitrage_opportunities:
        for outcome in team_names:
            if outcome in bookie and bookie[outcome] > best_odds[outcome]:
                best_odds[outcome] = bookie[outcome]
                best_bookies[outcome] = bookie['bookmaker']

    if all(best_odds.values()):
        total = sum(1 / best_odds[o] for o in team_names)
        if total < 1:
            profit = round((1 - total) * 100, 2)
            return {
                "event": f"{event['home_team']} vs {event['away_team']}",
                "sport": event.get("sport_name", "unknown"),
                "odds": best_odds,
                "bookmakers": best_bookies,
                "profit_margin": profit
            }
    return None
