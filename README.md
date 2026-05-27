## Overview
NFL game outcome predictor trained on twenty seasons of data (2006–2025) to forecast results for the 2026 regular season.

* Pulled team stats and schedules using the `nflreadpy` Python package
* Computed rolling pre-game averages (from all prior games) per team to match the prediction setup and avoid train/predict distribution mismatch
* Added win percentage and schedule strength (SOS) as engineered features
* Applied Sequential Forward Feature Selection (SFS) with time-series cross-validation to select the 30 most predictive features from ~80 candidates
* Trained a Logistic Regression model evaluated via rolling cross-season backtesting

## Data
Pulled via [`nflreadpy`](https://pypi.org/project/nflreadpy/)
* Training data: 2006–2025 NFL regular seasons (~9,100 team-game rows)
* Prediction targets: 2026 NFL regular season (weeks 1–18, 272 matchups)

## Pipeline

| Notebook | Description |
|---|---|
| `01_process_data.ipynb` | Merges raw team stats and schedule CSVs, mirrors opponent stats, filters to regular-season games |
| `03_predict.ipynb` | Computes rolling features, tunes regularization, runs SFS, cross-season backtest, trains final model, and outputs predictions |

## Model

* **Algorithm:** Logistic Regression (C=0.1)
* **Features:** Rolling season averages of passing, rushing, defensive, and special teams stats — plus win%, schedule strength (SOS), rest days, home/away, and division game flag
* **Feature selection:** Sequential Forward Selection → 30 features
* **Validation:** Rolling cross-season split (train on all prior seasons, test on next)

| Test Season | Accuracy |
|---|---|
| 2024 | 59.6% |
| 2025 | 61.0% |
| **Mean (2007–2025)** | **58.2%** |

Accuracy is in line with industry-standard NFL prediction benchmarks (~55–65%). The earlier inflated figures resulted from the model being trained on actual in-game stats rather than pre-game averages.

## Outputs
All outputs saved to `data/processed/`:
* `matchup_predictions.csv` — predicted winner for all 272 regular season matchups
* `team_predicted_records.csv` — aggregated predicted wins/losses per team, sorted by wins
