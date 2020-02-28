# pysketball 

![](https://github.com/AndresPitta/pysketball/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/AndresPitta/pysketball/branch/master/graph/badge.svg)](https://codecov.io/gh/AndresPitta/pysketball) ![Release](https://github.com/AndresPitta/pysketball/workflows/Release/badge.svg)

[![Documentation Status](https://readthedocs.org/projects/pysketball/badge/?version=latest)](https://pysketball.readthedocs.io/en/latest/?badge=latest)

This package is designated for all NBA enthusiasts! This package works to scrap online tabular data from ESPN NBA website and uses various functions to create graphs and statistical analysis. These include boxplots, rankings, and a summary statistics table.  
An example of the 2018/19 player stats can be found in the following url:

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
  
- `nbastats`
  * Generate summary stats for NBA players.
    The function filters the dataset further using the arguments provided and
    produces a tibble with summary statistics for a list of columns of a few players or teams.


### Documentation
The official documentation is hosted on Read the Docs: <https://pysketball.readthedocs.io/en/latest/>

### Credits
This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).

### Python Ecosystem 

This 'rsketball' package aims to further gain understanding of ESPN NBA data and does not have a specific fit to the Python ecosystem. There are currently no similar packages in Python. 



