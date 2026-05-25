import nflreadpy as nfl
import pandas as pd

YEARS = list(range(2020, 2026))

team_stats = nfl.load_team_stats(YEARS)

team_stats = team_stats.to_pandas()

team_stats.to_csv("data/raw/team_stats.csv")
