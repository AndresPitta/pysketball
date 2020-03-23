import altair as alt

import numpy as np

import pandas as pd


def nba_boxplot(dataset, stats, position=None, teams=None):
    """
    Creates a boxplot of the categorical variable of interest on the y-axis and
    the stat of interest on the x-axis. You can only use one of position or
    teams argument for categorical variable and stats argument must be chosen.

    Parameters:
    -----------
    dataset: pd.DataFrame
        This dataframe is created after using the nba_scraper.py function or if
        the csv has already been loaded, read the csv in and pass it as the
        parameter.

    stats: str
        The parameter of interest
        examples: Points, 3_Pointers, Turnovers

    teams: list
        list of team names to compare
        examples: ["ORL", "UTAH", "LAC", "MIN", "BOS"]

    position: str
        to compare position's stats put "POS" in argument


    Returns:
    --------
    display : altair boxplot visual
        Boxplot

    Examples:
    ---------
    >>> from pysketball import nba_boxplot.py
    >>> d = {"POS" :["C", "FOR", "PO","FOR", "C"],
    "Team" : ["ORL", "UTAH", "LAC", "MIN", "BOS"],
    "GP" : [3, 5, 5, 2, 1]}
    >>> nba_2018 = pd.DataFrame(data=d)
    >>> nba_boxplot(nba_2018, position= "POS", teams= None, stats= "GP")

    """

    # Test input 'dataframe' is a dataframe
    if isinstance(dataset, pd.DataFrame) is False:
        raise TypeError("Input 'dataset' is not a dataset!")

    # throw error if both teams and position is used
    if teams and position is not None:
        raise ValueError(
            "position and teams argument cannot be used simultaneously, " +
            "choose one"
        )

    # throw error if neither teams and position is used
    if teams is None and position is None:
        raise ValueError(
            "Empty arguments, choose either position or teams argument " +
            "for plot"
        )

    # Check if teams is a list
    if not isinstance(teams, list) and teams is not None:
        raise TypeError("teams must be a list")

    # Checks if the position exists in the dataframe
    if position is not None and position != 'POS':
        raise TypeError("Must input 'POS' in position argument")

    # Checks if the stats exists in the dataframe
    if stats not in dataset.columns:
        raise TypeError(f"Column {stats} not found in data")

    # set stats column chosen as new column
    dataset['stats'] = dataset.loc[:, stats]

    # test for stats argument being a numerical column
    if np.issubdtype(dataset['stats'].dtype, np.number) is False:
        raise TypeError("stats argument has to be numeric")

    # Plots
    if position == 'POS' and teams is None:

        chart = alt.Chart(dataset).mark_boxplot().encode(
            alt.Y('POS:N',
                  title='Position'),
            alt.X('stats:Q',
                  title=stats)
        ).properties(
            width=600,
            height=300,
            title=("Plot for Position and stats in Dataset"))

    elif position is None and teams is not None:

        dataset = dataset[dataset['TEAM'].isin(teams)]

        chart = alt.Chart(dataset).mark_boxplot().encode(
            alt.Y('TEAM:N',
                  title='Teams'),
            alt.X('stats:Q',
                  title=stats)
        ).properties(
            width=600,
            height=300,
            title=("Plot for Teams and Stats in Dataset"))

    return chart
