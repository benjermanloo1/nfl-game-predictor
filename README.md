## Overview
Small-scale NFL game predictor.  

Retrieved data from the 2024 NFL season and trained a machine learning model to predict the outcomes of games for the remainder of the regular season.
* Utilized Selenium WebDriver to automate the scraping of scores and advanced statistics from Pro Football Reference.
* Processed raw HTML with BeautifulSoup, removing unnecessary elements for easier parsing
* Consolidated individual box scores into a unified pandas DataFrame, ensuring the dataset is in a format suitable for machine learning or statistical analysis.

## Data
Downloaded from [Pro Football Reference](https://www.pro-football-reference.com/)  
* Collected from the 2024 NFL season (up to TNF for week 15, 12/15 games onwards not included)

## Findings
Week 17:
* KAN > PIT (correct)
* BAL > HOU (correct)
* SEA > CHI (correct)
* LAC > NWE (correct)
* DEN < CIN (correct)
* ARI > LAR (incorrect)
* CAR > TAM (incorrect)
* NYJ > BUF (incorrect)
* IND < NYG (correct)
* GNB < MIN (correct)
* LVR > NOR (correct)
* TEN > JAX (incorrect)
* MIA > CLE (correct)
* DAL < PHI (correct)
* ATL > WAS (incorrect)
* DET > SFO (correct)
 
*Total: 11/16 (68.75%)*

Week 18:
* CLE < BAL (correct)
* LAC < LVR ()
* CIN > PIT (correct)
* SFO < ARI ()
* CAR > ATL (correct)
* KAN > DEN ()
* SEA < LAR ()
* HOU < TEN (incorrect)
* NYG < PHI (correct)
* JAX < IND (correct)
* MIN > DET ()
* WAS > DAL (correct)
* CHI < GNB (incorrect)
* MIA < NYJ ()
* NOR > TAM (incorrect)
* BUF > NWE (incorrect)

*Total: /16 (%)*

**Overall: /32 (%)**

## Limitations
* Due to time constraints of scraping, previous seasons were not considered when training model (originally planned to include 2016-2024 seasons)
    * Likely resulting in an undertrained model
* THIS IS VERY CHOPPED.
