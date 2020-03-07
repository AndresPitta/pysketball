import pandas as pd
def nba_team_stats(nba_data, stats_filter = None, teams_filter = None, positions_filter = None):
    """
    Generate summary stats for NBA players.

    The function provides descriptive team statistics of NBA data. Users can specify which
    statistic of interest (3PA, 3PM, etc) along with teams of interest (GS, HOU, etc). If positions of
    interest (C, PG, etc) are specified, the returned dictionary depicts relevant descriptive statistics for the
    relevant positions in the relevant teams.

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
    >>> nba_team_stats.nba_team_stats(nba_data, stats_filter = ['GP', '3PM', 'FT%'],
                                      teams_filter = ['UTAH', 'PHX', 'DET'])
    >>> nba_team_stats.nba_team_stats(nba_data, stats_filter = ['GP', '3PM', 'FT%'],
                                      teams_filter = ['UTAH', 'PHX', 'DET'],
                                      positions_filter = ['C', 'PG'])
    """
    # Check if nba_data is a DataFrame
    if not isinstance(nba_data, pd.DataFrame):
        raise TypeError("nba_data must be a DataFrame.")

    # Check if teams_filter is a list
    if not isinstance(teams_filter, list) and teams_filter != None:
        raise TypeError("teams_filter must be a list")

    # Check if stats_filter is a list
    if not isinstance(stats_filter, list) and stats_filter != None:
        raise TypeError("stats_filter must be a list")

    # Check if positions_filter is a list
    if not isinstance(positions_filter, list) and positions_filter != None:
        raise TypeError("positions_filter must be a list")

    # Filter data on teams
    if teams_filter != None:
        nba_data = nba_data[nba_data['Team'].isin(teams_filter)]

    # Filter data on positions
    if positions_filter != None:
        nba_data = nba_data[nba_data['POS'].isin(positions_filter)]

    # Select stats to include
    if stats_filter != None:
        stats_filter = ['PLAYER', 'Team', 'POS'] + stats_filter
        nba_data = nba_data[stats_filter]

    # If all inputs (stats, teams, and positions) are NULL, show all
    if stats_filter == None and teams_filter == None and positions_filter == None:
        nba_data = nba_data

    # Generate summary
    # If position is null, only group_by Teams
    if positions_filter == None:
        group_by = ['Team']
    else:
        group_by = ['Team', 'POS']

    stats = dict()
    if stats_filter == None:
        stats_filter = list(nba_data.columns.values)

    stats_filter = [stat for stat in stats_filter if stat not in ('PLAYER', 'Team', 'POS')]
    for stat in stats_filter:
        stats[stat] = nba_data.groupby(group_by).describe()[stat]

    return stats