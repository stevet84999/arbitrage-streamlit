def detect_2way_arbitrage(edef find_arbitrage_opportunities(events, min_profit_margin=0.01):
    opportunities = []
    for event in events:
        for bookmaker in event['bookmakers']:
            for market in bookmaker['markets']:
                if market['key'] == 'h2h':
                    team1 = market['outcomes'][0]
                    team2 = market['outcomes'][1]
                    team_names = [team1['name'], team2['name']]
                    arbitrage_opportunity = {
                        team1['name']: team1['price'],
                        team2['name']: team2['price'],
                        "bookmaker": bookmaker['title']
                    }

                    best_odds = {}
                    best_bookies = {}
                    for outcome in team_names:
                        best_odds[outcome] = 0
                        best_bookies[outcome] = ""

                    for bookie in [arbitrage_opportunity]:
                        for outcome in team_names:
                            if outcome in bookie and bookie[outcome] > best_odds[outcome]:
                                best_odds[outcome] = bookie[outcome]
                                best_bookies[outcome] = bookie["bookmaker"]

                    if all(best_odds.values()):
                        total = sum(1 / best_odds[o] for o in team_names)
                        if total < 1:
                            profit = round((1 - total) * 100, 2)
                            if profit >= min_profit_margin * 100:
                                opportunities.append({
                                    "event": f"{event['home_team']} vs {event['away_team']}",
                                    "sport": event.get("sport_key", ""),
                                    "odds": best_odds,
                                    "bookmakers": best_bookies,
                                    "profit_margin": profit
                                })
    return opportunities

            }
    return None
