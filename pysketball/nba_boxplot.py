import numpy as np
import pandas as pd
import altair as alt

def nba_boxplot(dataset, yaxis, xaxis):
    """
    Creates a boxplot of the categorical variable of interest on the y axis and 
    the stat of interest on the xaxis.

    Parameters:
    -----------
    dataset: pd.DataFrame
        This dataframe is created after using the nba_scraper.py function or if 
        the csv has already been loaded, read the csv in and pass it as the parameter.

    yaxis: str
        The parameter of interest 
        examples: Points, 3_Pointers, Turnovers

    xaxis: str
        The categorical variable of interest 
        examples: Team, Position

    Returns:
    --------
    display : altair boxplot visual

    Examples:
    ---------
    >>> from pysketball import nba_boxplot.py
    >>> NBA_reg_01_02 = pd.read_csv("NBA_reg_2001-2002.csv")
    >>> nba_boxplot(NBA_reg_01_02, Team, Points)

    """