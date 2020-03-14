import altair as alt

import pandas as pd

from pysketball import nba_boxplot, nba_ranking, nba_scraper, nba_team_stats


def test_integration(tmp_path):
    """
    The function tests the integration of all the function in the package
    """
    nba_2001 = nba_scraper.nba_scraper(
        2001, "regular")

    # Boxplot test
    assert isinstance(nba_boxplot.nba_boxplot(
        nba_2001, stats="GP", position='POS', teams=None),
        alt.vegalite.api.Chart)

    # Ranking test
    assert isinstance(nba_ranking.nba_ranking(
        nba_2001, 'NAME', 'PTS', top=2, ascending=False, fun='mean'), tuple)
    assert isinstance(nba_ranking.nba_ranking(
        nba_2001, 'NAME', 'PTS', top=2, ascending=True, fun='mean')[0],
        pd.DataFrame)
    assert isinstance(nba_ranking.nba_ranking(nba_2001, 'NAME', 'PTS', top=2,
                      ascending=False, fun='mean')[1],
                      alt.vegalite.v4.api.LayerChart)

    # Stats test
    sample_stats_filter = ['GP', '3PM', 'FT%']
    sample_teams_filter = ['UTAH', 'DET']
    sample_positions_filter = ['C', 'PG']

    result = nba_team_stats.nba_team_stats(nba_2001)
    assert isinstance(
        result, dict) is True, "Function does not return a valid dictionary"

    result = nba_team_stats.nba_team_stats(
        nba_2001, teams_filter=sample_teams_filter)
    assert isinstance(
        result, dict) is True, "Function does not return a valid dictionary"

    result = nba_team_stats.nba_team_stats(
        nba_2001, positions_filter=sample_positions_filter)
    assert isinstance(
        result, dict) is True, "Function does not return a valid dictionary"

    result = nba_team_stats.nba_team_stats(
        nba_2001, stats_filter=sample_stats_filter)
    assert isinstance(
        result, dict) is True, "Function does not return a valid dictionary"

    result = nba_team_stats.nba_team_stats(
        nba_2001,
        teams_filter=sample_teams_filter,
        stats_filter=sample_stats_filter,
        positions_filter=sample_positions_filter)
    assert isinstance(
        result, dict) is True, "Function does not return a valid dictionary"
