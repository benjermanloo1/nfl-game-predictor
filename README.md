## Overview
Small-scale NFL game predictor.  

Retrieved data from the 2024 NFL season and trained a machine learning model to predict the outcomes of games for the remainder of the season.
* Utilized Selenium WebDriver to automate the scraping of scores and advanced statistics from Pro Football Reference.
* Processed raw HTML with BeautifulSoup, removing unnecessary elements for easier parsing
* Consolidated individual box scores into a unified pandas DataFrame, ensuring the dataset is in a format suitable for machine learning or statistical analysis.

## Data
Downloaded from [Pro Football Reference](https://www.pro-football-reference.com/)  
* Collected from the 2024 NFL season (up to TNF for week 15, 12/15 games onwards not included)

## Findings
TBD

## Limitations
* Due to time constraints of scraping, previous seasons were not considered when training model (originally planned to include 2016-2024 seasons)
    * Likely resulting in an undertrained model
