# pysketball 

![](https://github.com/UBC-MDS/pysketball/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/UBC-MDS/pysketball/branch/master/graph/badge.svg)](https://codecov.io/gh/UBC-MDS/pysketball) ![Release](https://github.com/UBC-MDS/pysketball/workflows/Release/badge.svg)

[![Documentation Status](https://readthedocs.org/projects/pysketball/badge/?version=latest)](https://pysketball.readthedocs.io/en/latest/?badge=latest)

This package is designated for all NBA enthusiasts! This package works
to scrape online tabular data from ESPN NBA website into a csv file. It
also includes various functions to create graphs and statistical
analysis for your interest (such as boxplots, player rankings by stats,
and a summary statistics table).

An example of the ESPN NBA 2018/19 Regular season player stats can be
found in the following url:

https://www.espn.com/nba/stats/player/_/season/2019/seasontype/2

### Installation:

```
pip install -i https://test.pypi.org/simple/ pysketball
```

### Functions
- `nba_scraper`
  * Scrapes data from ESPN NBA data into a csv file. User can specify the year of the season
  (2016, 2017, etc) and the season type (regular or playoffs).
  
- `nba_boxplot`
  * Creates a boxplot of the categorical variable of interest on the y-axis and 
   the stat of interest on the x-axis.
   
- `nba_ranking`
  * Generates a ranking and a visualization based on a column of a dataset  
  
- `nba_team_stats`
  * Generate summary stats for NBA players. The function provides descriptive team statistics of NBA data.


### Documentation
The official documentation is currently in development and not available now. We estimate that it will be hosted on "Read the Docs" by end March 2020: 

<https://pysketball.readthedocs.io/en/latest/>

### Credits
This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).

### Python Ecosystem 

This `pysketball` package aims to further gain understanding of ESPN NBA data and does not have a specific fit to the Python ecosystem. There are currently some similar packages in Python such as [`nba_api`](https://pypi.org/project/nba-api/) which takes data from sources such as NBA, but we do not know of any that takes data from ESPN NBA.



