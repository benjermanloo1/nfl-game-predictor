import nflreadpy as nfl
import pandas

YEARS = list(range(2020, 2026))

team_stats = nfl.load_team_stats(YEARS)
team_stats = team_stats.to_pandas()
team_stats.to_csv("data/raw/team_stats.csv")

team_schedules = nfl.load_schedules(YEARS)
team_schedules = team_schedules.to_pandas()
team_schedules.to_csv("data/raw/team_schedules.csv")
