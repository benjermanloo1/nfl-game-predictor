import nflreadpy as nfl
import pandas

YEARS = list(range(2006, 2026))

team_stats = nfl.load_team_stats(YEARS)
team_stats = team_stats.to_pandas()
team_stats.to_csv("data/raw/team_stats.csv")

team_schedules = nfl.load_schedules(YEARS)
team_schedules = team_schedules.to_pandas()
team_schedules.to_csv("data/raw/team_schedules.csv")

future_games = nfl.load_schedules(2026)
future_games = future_games.to_pandas()
future_games.to_csv("data/raw/future_games.csv")
