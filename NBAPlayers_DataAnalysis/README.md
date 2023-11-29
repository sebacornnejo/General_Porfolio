# NBA Players Analysis

[Link Colab ->](https://colab.research.google.com/drive/1ogtZRB9T9vx_J84WUpaarhS0AO9YA57r?usp=sharing)

## How to Use

1. Clone the repository: `git clone --depth=1 --filter=blob:none https://github.com/sebacornnejo/General_Porfolio.git/NBAPlayers_DataAnalysis`
2. Install the required libraries: `pip install -r requirements.txt`
3. Run the individual analysis scripts or the full dashboard script.
4. Explore the generated charts and dashboard HTML files.

### 1. Individual Player Analysis

#### Extracted and analyzed key statistics for NBA players

- [Count of players based on their heights](https://sebacornnejo.github.io/bar_NBAplayersheight_count.html)
- [Player performance respect to player height](https://sebacornnejo.github.io/scatter_NBAplayersheight_performance.html)
- [Is a High Net Rating when Few Games have been Played?](https://sebacornnejo.github.io/NetRatingGamesPlayed_NBAplayer.html)

## Michael Jordan Analysis

- [Where is the Great Michael Jordan?](https://sebacornnejo.github.io/ComparisonMichaelJordanAverageSkills.html)

### 2. Top Players and Teams

- Identified top players based on points per game and overall performance.
- Top 10 Players based on Points per Game (and the Great Michael Jordan)
- Top 5 teams with the Best NBA Player Considering Points per Game
- Top 5 Teams with the Average Best Players in the NBA considering Points per Game
- Normalized and calculated an overall score for each player
- Top 10 NBA Players Based on a Normalized General Skill Statistic
- Top 5 Teams with Overall Best NBA Player
- Top 5 Teams with Average Overall Best NBA Players
- Explored top teams based on player performance.

### 3. Geographic Analysis

- Mapped the distribution of NBA players worldwide.
- Explored player distribution by country and state.

## Championship Analysis

### 1. NBA Championship Overview

#### Comparison of NBA Champions by Season vs Team with the Best Player and Team with the Best Players on Average

- [(a) Comparison of Main Points per Game by Season](https://sebacornnejo.github.io/ComparisonMainPointsperGamebySeason.html)
- [(b) Comparison of Main Overall by Season](https://sebacornnejo.github.io/ComparisonMainOverallbySeason.html)

#### Overall and Age Distribution of Players in the Top 5 Champion Teams in the last 26 years

- Merged and analyzed data on the top 5 teams with the most championships.
- [Players Ages of the Top 5 NBA Champion Teams](https://sebacornnejo.github.io/PlayersAgesTop5NBAChampionTeam.html)
- [Players Overall of the Top 5 NBA Champion Teams](https://sebacornnejo.github.io/PlayersOverallTop5NBAChampionTeams.html)

### 2. Geographic Distribution

#### Mapped the distribution of NBA players by country and state

- [Distribution of NBA Players by Country](https://sebacornnejo.github.io/Map_DistributionofNBAPlayersbyCountry.html)
- [Distribution of NBA Players (Top 5 Champion Teams) by Country](https://sebacornnejo.github.io/Map_DistributionofNBAPlayersTop5TeamsbyCountry.html)
- [Distribution of NBA Players by US States (from College data)](https://sebacornnejo.github.io/Map_DistributionofNBAPlayersTeamsbyStates.html)
- [Distribution of NBA Players (Top 5 Champion Teams) by US States (from College data)](https://sebacornnejo.github.io/Map_DistributionofNBAPlayersTop5TeamsbyStates.html)

### Additional Codes

- [predefined_codes.py](predefined_codes.py)

This Python function maps certain country names to their ISO 3166-1 alpha-3 codes. If a country name is not found in pycountry find in predefined list

For detailed comments and code, view the [predefined_codes.py](predefined_codes.py).

- [statebycollege.py](statebycollege.py)

These functions are used to map college names to their respective states and to map state names to their two-letter codes (ISO 3166-2).

For detailed comments and code, view the [statebycollege.py](statebycollege.py).

### Datasets

- [Kaggle NBA Players Data](https://www.kaggle.com/datasets/justinas/nba-players-data)
- [Shapefiles](https://earthworks.stanford.edu/)
- [Last 26 champions](championships.csv)

### Note: Visualizations and outputs are displayed using Plotly, and other relevant libraries
