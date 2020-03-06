import pandas as pd
def nba_team_stats(nba_data, stats_filter, teams_filter, positions_filter):
    """
    Generate summary stats for NBA players.

    The function filters the dataset further using the arguments provided and
    produces a tibble with summary statistics for a list of columns of a few players or teams.
    The function can only use one of the two filters - playerNames and teamNames. Hence, If playerNames
    are provided, teamNames are ignored.

    Parameters
    ----------
    nba_data : pandas.DataFrame
      A pandas DataFrame with overall statistics for a particular season of NBA.
    stats_filter : list
      A list of column names for whom summary stats are required
    teams_filter : list
      A list of team names for whom summary stats are required
    positions_filter : list
      A list of positions for whom summary stats are required

    Returns
    -------
    dict of str: pandas.DataFrame:
      The stats summarised in a dictionary where keys holds summary stats for each stat in stats_filter

    Examples
    --------
    >>> from pysketball import nba_team_stats
    >>> nba_team_stats.nba_team_stats(nba_data, stats_filter = ['GP', '3PM', 'FT%'])
    >>> nba_team_stats.nba_team_stats(nba_data, stats_filter = ['GP', '3PM', 'FT%'], teams_filter = ['UTAH', 'PHX', 'DET'])
    >>> nba_team_stats.nba_team_stats(nba_data, stats_filter = ['GP', '3PM', 'FT%'], teams_filter = ['UTAH', 'PHX', 'DET'], positions_filter = ['C', 'PG'])
    """
    # Check for incorrect inputs
    if not isinstance(nba_data, pd.DataFrame):
      print("Not dataframe")

    # Filter data on teams
    if len(teams_filter) != 0:
      nba_data = nba_data[nba_data['Team'].isin(teams_filter)]

    # Filter data on positions
    if len(positions_filter) != 0:
      nba_data = nba_data[nba_data['POS'].isin(positions_filter)]

    # Select stats to include
    if len(stats_filter) != 0:
      stats_filter = ['PLAYER', 'Team', 'POS'] + stats_filter
      nba_data = nba_data[stats_filter]

    # If all inputs (stats, teams, and positions) are NULL, show all
    if len(stats_filter) == 0 and len(teams_filter) == 0 and len(positions_filter) == 0:
      nba_data = nba_data

    # Generate summary
    # If position is null, only group_by Teams
    if len(positions_filter) == 0:
      group_by = ['Team']
    else:
      group_by = ['Team', 'POS']

      stats = dict()
      stats_filter = [stat for stat in stats_filter if stat not in ('PLAYER', 'Team', 'POS')]
      for stat in stats_filter:
        stats[stat] = nba_data.groupby(group_by).describe()[stat]

        return stats