import pandas as pd

df = pd.read_csv("data/processed/matchup_predictions.csv")

records = {}

for _, row in df.iterrows():
    away, home, winner = row["away_team"], row["home_team"], row["predicted_winner"]
    for team in (away, home):
        if team not in records:
            records[team] = {"wins": 0, "losses": 0}
    if winner == away:
        records[away]["wins"] += 1
        records[home]["losses"] += 1
    else:
        records[home]["wins"] += 1
        records[away]["losses"] += 1

rows = [
    {"team": team, "predicted_wins": v["wins"], "predicted_losses": v["losses"]}
    for team, v in sorted(records.items())
]

out = pd.DataFrame(rows).sort_values("predicted_wins", ascending=False).reset_index(drop=True)
out.to_csv("data/processed/team_predicted_records.csv", index=False)
print(out.to_string(index=False))
