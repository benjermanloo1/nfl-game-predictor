## Overview
NFL game outcome predictor trained on six seasons of data (2020–2025) to forecast results for the 2026 regular season.

* Utilized Selenium WebDriver to automate the scraping of scores and advanced statistics from Pro Football Reference
* Processed raw HTML with BeautifulSoup, removing unnecessary elements for easier parsing
* Consolidated individual box scores and schedules into a unified pandas DataFrame with both team and opponent-mirrored stats
* Applied Sequential Forward Feature Selection (SFS) with time-series cross-validation to select the 30 most predictive features
* Trained a RidgeClassifier on all six seasons, evaluated via rolling cross-season backtesting

## Data
Downloaded from [Pro Football Reference](https://www.pro-football-reference.com/)
* Training data: 2020–2025 NFL regular seasons (~3,400 team-game rows)
* Prediction targets: 2026 NFL regular season (weeks 1–18, 272 matchups)

## Pipeline

| Notebook | Description |
|---|---|
| `01_process_data.ipynb` | Merges raw team stats and schedule CSVs, mirrors opponent stats, filters to regular-season games |
| `02_upcoming_games.ipynb` | Builds feature rows for 2026 matchups using rolling averages from prior seasons |
| `03_predict.ipynb` | Runs SFS, cross-season backtest, trains final model, and outputs predictions |

## Model

* **Algorithm:** RidgeClassifier (alpha=1)
* **Feature selection:** Sequential Forward Selection → 30 features from ~80 candidates
* **Validation:** Rolling cross-season split (train on all prior seasons, test on next)

| Test Season | Accuracy |
|---|---|
| 2021 | 91.9% |
| 2022 | 87.8% |
| 2023 | 94.1% |
| 2024 | 93.0% |
| 2025 | 92.5% |
| **Mean** | **91.9%** |

## Findings
2026 season predictions (weeks 1–18) saved to `data/processed/matchup_predictions.csv`.
