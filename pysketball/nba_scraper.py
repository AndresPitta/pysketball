import time

import pandas as pd

from selenium import webdriver

from selenium.webdriver import chrome


def nba_scraper(season_year, season_type="regular", csv_path=None):
    """
    Scrapes data from ESPN NBA data and returns a pandas DataFrame. User can
    specify the year of the season (2016, 2017, etc) and the season type
    (regular or postseason). If `csv_path` is given, the scraped data will
    be written to csv based on input path.

    Parameters
    ----------
    season_year : int
        An integer input of the year of interest for the NBA season.
    season_type : string
        A string input of the NBA season type (either "regular" or playoff).
        Default is "regular".
    csv_path_name : string
        A string input stating the path to store the scraped csv file and
        ending with ".csv". Default is None.

     Returns
    -------
    pandas.DataFrame
        scraped data in DataFrame format

    Examples
    --------
    >>> from pysketball.nba_scraper import nba_scraper
    >>> # Scrape regular season 2018/19 and return a dataframe while storing
    it as csv file called "nba_2018.csv"
    >>> nba_scraper(season_year = 2018, season_type = "regular",
    csv_path = "nba_2018.csv")
    >>>
    >>> # Scrape postseason season 2017/18 and return a dataframe without
    storing it as csv file.
    >>> nba_scraper(season_year = 2017, season_type = "postseason",
    csv_path = None)

    """
    # Check season_year is not integer or not within range
    if (round(season_year) != season_year) or (season_year < 2001) \
       or (season_year > 2019):
        raise TypeError("season_year must be an integer that is between \
            2001 to 2019")

    # Check season_type is not "regular" or "postseason"
    if ((season_type != "postseason") & (season_type != "regular")):
        raise TypeError(
            "'season_type' must be either 'regular' or 'postseason'")

    # Check csv_path is given input
    if (csv_path is not None):
        # but is not a string input
        if (not isinstance(csv_path, str)):
            raise TypeError(
                "'csv_path' must be string input if it is not None")
        # but does not end with .csv
        elif (csv_path[-4:] != ".csv"):
            raise TypeError(
                "'csv_path' must be end with '.csv' if it is not None")

    # Modify url based on user inputs on season year and type
    url_year = season_year + 1

    if season_type == "regular":
        url_season_type = 2
    else:
        url_season_type = 3

    url_link = 'https://www.espn.com/nba/stats/player/_/season/' + \
        str(url_year) + '/seasontype/' + str(url_season_type)

    # Initiate driver head type
    options = chrome.options.Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)

    # Print scraping commencing
    print("Scraping commencing. Please wait!")

    # Start navigating the url
    driver.get(url_link)

    # To click on "Show More" button until all data in table is shown using
    # Selenium headless driver
    while True:
        try:
            button = driver.find_element_by_xpath(
                '//*[@id="fittPageContainer"]/div[3]/div[1]/div/' +
                'section/div/div[3]/div/a')
            button.click()
            time.sleep(2)
        except Exception:
            break

    # Obtain the two main components of the table: Player and Stats tables.
    plyr_trs = driver.find_elements_by_xpath(
        '//*[@id="fittPageContainer"]/div[3]/div[1]/div/section/div/div[3]/' +
        'section/div[2]/table/tbody/tr')
    stats_trs = driver.find_elements_by_xpath(
        '//*[@id="fittPageContainer"]/div[3]/div[1]/div/section/div/div[3]/' +
        'section/div[2]/div/div[2]/table/tbody/tr')

    # Initiate empty dataframe
    df = pd.DataFrame(index=[i for i in range(len(plyr_trs))],
                      columns=['PLAYER', 'Team', 'POS', 'GP', 'MIN', 'PTS',
                               'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%',
                               'FTM', 'FTA', 'FT%', 'REB', 'AST',
                               'STL', 'BLK', 'TO', 'DD2', 'TD3', 'PER'])

    # For loop based on each player
    for i in range(len(plyr_trs)):

        # Table 1: Player name and Team
        df.loc[i, "PLAYER"] = plyr_trs[i].find_element_by_xpath(
            './/td[2]/div/a').text
        df.loc[i, "Team"] = plyr_trs[i].find_element_by_xpath(
            './/td[2]/div/span').text

        # Table 2: Player Position and Stats
        # stats = stats_trs[i]

        df.loc[i, "POS"] = stats_trs[i].find_element_by_xpath('.//td[1]').text
        df.loc[i, "GP"] = stats_trs[i].find_element_by_xpath('.//td[2]').text
        df.loc[i, "MIN"] = stats_trs[i].find_element_by_xpath('.//td[3]').text
        df.loc[i, "PTS"] = stats_trs[i].find_element_by_xpath('.//td[4]').text
        df.loc[i, "FGM"] = stats_trs[i].find_element_by_xpath('.//td[5]').text
        df.loc[i, "FGA"] = stats_trs[i].find_element_by_xpath('.//td[6]').text
        df.loc[i, "FG%"] = stats_trs[i].find_element_by_xpath('.//td[7]').text
        df.loc[i, "3PM"] = stats_trs[i].find_element_by_xpath('.//td[8]').text
        df.loc[i, "3PA"] = stats_trs[i].find_element_by_xpath('.//td[9]').text
        df.loc[i, "3P%"] = stats_trs[i].find_element_by_xpath('.//td[10]').text
        df.loc[i, "FTM"] = stats_trs[i].find_element_by_xpath('.//td[11]').text
        df.loc[i, "FTA"] = stats_trs[i].find_element_by_xpath('.//td[12]').text
        df.loc[i, "FT%"] = stats_trs[i].find_element_by_xpath('.//td[13]').text
        df.loc[i, "REB"] = stats_trs[i].find_element_by_xpath('.//td[14]').text
        df.loc[i, "AST"] = stats_trs[i].find_element_by_xpath('.//td[15]').text
        df.loc[i, "STL"] = stats_trs[i].find_element_by_xpath('.//td[16]').text
        df.loc[i, "BLK"] = stats_trs[i].find_element_by_xpath('.//td[17]').text
        df.loc[i, "TO"] = stats_trs[i].find_element_by_xpath('.//td[18]').text
        df.loc[i, "DD2"] = stats_trs[i].find_element_by_xpath('.//td[19]').text
        df.loc[i, "TD3"] = stats_trs[i].find_element_by_xpath('.//td[20]').text
        df.loc[i, "PER"] = stats_trs[i].find_element_by_xpath('.//td[21]').text

    # Stop driver
    driver.close()

    # If csv_path is given, store df
    if (csv_path is not None):
        # Store data without index column
        df.to_csv(csv_path, index=False)

    print("Year {0:} {1:} season scraping done!".format(
        season_year, season_type))

    return(df)
