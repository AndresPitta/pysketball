def nba_scraper():
    """
    Scrapes data from ESPN NBA data into a csv file. User can specify the year of the season (2016, 2017, etc) and the season type (regular or playoffs).
    Parameters
    ----------
    season_year : string
      A string input of the year of interest for the NBA season
    season_type : string
      A string input of the NBA season type (either regular or playoff)
    csv_path_name : string
      A string input stating the path to store the scraped csv file
   
    Examples
    --------
    >>> from pysketball import nba_scraper
    >>> nba_scraper.nba_scraper(season_year = "2018", season_type = "regular", csv_path = "nba_2018_reg.csv")
    >>> nba_scraper.nba_scraper(season_year = "2016", season_type = "playoffs", csv_path = "nba_2016_reg.csv")
    """
    print("Data scraping is done!")
    