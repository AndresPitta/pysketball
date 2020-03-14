import altair as alt

import numpy as np

import pandas as pd

from pysketball import nba_boxplot

from pytest import raises


def test_nba_boxplot():
    """
    The function tests the test_nba_boxplot function with various ranges of
    values to ensure the functionality is not broken
    Examples
    --------
    >>> test_nba_boxplot()
    """

    # test sample
    nba_2018 = pd.read_csv("https://raw.githubusercontent.com/kfoofw/" +
                           "nba_espn/master/0.data/NBA_reg_2018-2019.csv")

    nba_2018 = nba_2018.rename(columns={'Team': 'TEAM',
                               'PLAYER': 'NAME'})

    # testing input of dataset
    with raises(TypeError, match="Input 'dataset' is not a dataset!"):
        nba_boxplot.nba_boxplot(
            np.array([4, 3, 3]), stats="PTS", position='POS')

    # testing position and teams used simultaneously
    with raises(ValueError, match="position and teams argument cannot be " +
                "used simultaneously, choose one"):
        nba_boxplot.nba_boxplot(nba_2018, stats="GP", position="POS", teams=[
            "ORL", "UTAH", "LAC", "MIN", "BOS"])

    # testing position and teams empty arguments
    with raises(ValueError, match="Empty arguments, choose either position " +
                "or teams argument for plot"):
        nba_boxplot.nba_boxplot(nba_2018, stats="GP",
                                position=None, teams=None)

    # testing for wrong teams input
    with raises(TypeError, match="teams must be a list"):
        nba_boxplot.nba_boxplot(
            nba_2018, stats="GP", position=None, teams='None')

    # Test position column not belonging to dataframe
    with raises(TypeError):
        nba_boxplot.nba_boxplot(
            nba_2018, stats="GP", position='PdOS', teams=None)

    # Test stats column not belonging to dataframe
    with raises(TypeError):
        nba_boxplot.nba_boxplot(
            nba_2018, stats="GdP", position='POS', teams=None)

    # testing wrong stats type
    with raises(TypeError, match="stats argument has to be numeric"):
        nba_boxplot.nba_boxplot(nba_2018, stats="TEAM", position="POS")

    # testing plot output for teams
    assert isinstance(nba_boxplot.nba_boxplot(nba_2018, stats="GP", teams=[
        "ORL", "UTAH", "LAC"]), alt.vegalite.api.Chart)

    # testing plot output for position
    assert isinstance(nba_boxplot.nba_boxplot(
        nba_2018, stats="GP", position='POS', teams=None),
        alt.vegalite.api.Chart)
