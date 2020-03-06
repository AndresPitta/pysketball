from pysketball import nba_team_stats
import pandas as pd
from pytest import raises

def test_nba_team_stats():

    # Sample test inputs
    sample_stats_filter = ['GP', '3PM', 'FT%']
    sample_teams_filter = ['UTAH', 'DET']
    sample_positions_filter = ['C', 'PG']
    nba_data = pd.read_csv("https://raw.githubusercontent.com/kfoofw/nba_espn/master/0.data/NBA_reg_2018-2019.csv")

    # Test for TypeErrors in input arguments
    with raises(TypeError):
        nba_team_stats.nba_team_stats("random data")
    with raises(TypeError):
        nba_team_stats.nba_team_stats(nba_data, teams_filter='sample_teams_filter')
    with raises(TypeError):
        nba_team_stats.nba_team_stats(nba_data, stats_filter='sample_stats_filter')
    with raises(TypeError):
        nba_team_stats.nba_team_stats(nba_data, positions_filter='sample_positions_filter')

    # General output tests
    result = nba_team_stats.nba_team_stats(nba_data)
    assert isinstance(result, dict) == True,  "Function does not return a valid dictionary"

    result = nba_team_stats.nba_team_stats(nba_data, teams_filter=sample_teams_filter)
    assert isinstance(result, dict) == True, "Function does not return a valid dictionary"

    result = nba_team_stats.nba_team_stats(nba_data, positions_filter=sample_positions_filter)
    assert isinstance(result, dict) == True, "Function does not return a valid dictionary"

    result = nba_team_stats.nba_team_stats(nba_data, stats_filter=sample_stats_filter)
    assert isinstance(result, dict) == True, "Function does not return a valid dictionary"

    result = nba_team_stats.nba_team_stats(nba_data, teams_filter=sample_teams_filter, stats_filter=sample_stats_filter, positions_filter=sample_positions_filter)
    assert isinstance(result, dict) == True, "Function does not return a valid dictionary"