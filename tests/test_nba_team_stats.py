import pandas as pd

from pysketball import nba_team_stats

from pytest import raises


def test_nba_team_stats():
    """
    The function tests the nba_team_stats function with various ranges of
    values to ensure the functionality is not broken

    Examples
    --------
    >>> test_nba_team_stats()
    """

    # Sample test inputs
    sample_stats_filter = ['GP', '3PM', 'FT%']
    sample_teams_filter = ['UTAH', 'DET']
    sample_positions_filter = ['C', 'PG']

    invalid_stats_filter = ['A', 'B', 'C']
    invalid_teams_filter = ['A', 'B']
    invalid_positions_filter = ['A', 'B']
    nba_data = pd.read_csv(
        "https://raw.githubusercontent.com/kfoofw/nba_espn/master/0.data/" +
        "NBA_reg_2018-2019.csv")

    nba_data = nba_data.rename(columns={'Team': 'TEAM',
                               'PLAYER': 'NAME'}
                              )  

    # Test for TypeErrors in input arguments
    with raises(TypeError):
        nba_team_stats.nba_team_stats("random data")
    with raises(TypeError):
        nba_team_stats.nba_team_stats(
            nba_data, teams_filter='sample_teams_filter')
    with raises(TypeError):
        nba_team_stats.nba_team_stats(
            nba_data, stats_filter='sample_stats_filter')
    with raises(TypeError):
        nba_team_stats.nba_team_stats(
            nba_data, positions_filter='sample_positions_filter')
    with raises(TypeError):
        nba_team_stats.nba_team_stats(
            nba_data,
            positions_filter=invalid_positions_filter,
            stats_filter=sample_stats_filter,
            teams_filter=sample_teams_filter)
    with raises(TypeError):
        nba_team_stats.nba_team_stats(
            nba_data,
            positions_filter=sample_positions_filter,
            stats_filter=invalid_stats_filter,
            teams_filter=sample_teams_filter)
    with raises(TypeError):
        nba_team_stats.nba_team_stats(
            nba_data,
            positions_filter=sample_positions_filter,
            stats_filter=sample_stats_filter,
            teams_filter=invalid_teams_filter)

    # General output tests
    result = nba_team_stats.nba_team_stats(nba_data)
    assert isinstance(
        result, dict) is True, "Function does not return a valid dictionary"

    result = nba_team_stats.nba_team_stats(
        nba_data, teams_filter=sample_teams_filter)
    assert isinstance(
        result, dict) is True, "Function does not return a valid dictionary"

    result = nba_team_stats.nba_team_stats(
        nba_data, positions_filter=sample_positions_filter)
    assert isinstance(
        result, dict) is True, "Function does not return a valid dictionary"

    result = nba_team_stats.nba_team_stats(
        nba_data, stats_filter=sample_stats_filter)
    assert isinstance(
        result, dict) is True, "Function does not return a valid dictionary"

    result = nba_team_stats.nba_team_stats(
        nba_data,
        teams_filter=sample_teams_filter,
        stats_filter=sample_stats_filter,
        positions_filter=sample_positions_filter)
    assert isinstance(
        result, dict) is True, "Function does not return a valid dictionary"
