import pandas as pd


def nba_team_stats(nba_data, stats_filter=None, teams_filter=None,
                   positions_filter=None):
    """
    Generate summary stats for NBA players.

    The function provides descriptive team statistics of NBA data. Users can
    specify which statistic of interest (3PA, 3PM, etc) along with teams of
    interest (GS, HOU, etc). If positions of interest (C, PG, etc) are
    specified, the returned dictionary depicts relevant descriptive statistics
    for the relevant positions in the relevant teams.

    Parameters
    ----------
    nba_data : pandas.DataFrame
      A pandas DataFrame with overall statistics for a particular season of
      NBA.
    stats_filter : list
      A list of column names for whom summary stats are required
    teams_filter : list
      A list of team names for whom summary stats are required
    positions_filter : list
      A list of positions for whom summary stats are required

    Returns
    -------
    dict of str: pandas.DataFrame:
      The stats summarised in a dictionary where keys holds summary stats
      for each stat in stats_filter

    Examples
    --------
    >>> from pysketball import nba_team_stats
    >>> nba_team_stats.nba_team_stats(nba_data,
                                      stats_filter = ['GP', '3PM', 'FT%'])
    >>> nba_team_stats.nba_team_stats(nba_data,
                                      stats_filter = ['GP', '3PM', 'FT%'],
                                      teams_filter = ['UTAH', 'PHX', 'DET'])
    >>> nba_team_stats.nba_team_stats(nba_data,
                                      stats_filter = ['GP', '3PM', 'FT%'],
                                      teams_filter = ['UTAH', 'PHX', 'DET'],
                                      positions_filter = ['C', 'PG'])
    {'GP':           count  mean       std   min    25%   50%    75%   max
     Team POS
     DET  C      2.0  73.5  7.778175  68.0  70.75  73.5  76.25  79.0
          PG     1.0  82.0       NaN  82.0  82.00  82.0  82.00  82.0
     PHX  C      1.0  71.0       NaN  71.0  71.00  71.0  71.00  71.0
     UTAH C      1.0  81.0       NaN  81.0  81.00  81.0  81.00  81.0
          PG     1.0  68.0       NaN  68.0  68.00  68.0  68.00  68.0,
     '3PM':           count  mean       std  min    25%   50%    75%  max
     Team POS
     DET  C      2.0  0.05  0.070711  0.0  0.025  0.05  0.075  0.1
          PG     1.0  2.10       NaN  2.1  2.100  2.10  2.100  2.1
     PHX  C      1.0  0.00       NaN  0.0  0.000  0.00  0.000  0.0
     UTAH C      1.0  0.00       NaN  0.0  0.000  0.00  0.000  0.0
          PG     1.0  1.20       NaN  1.2  1.200  1.20  1.200  1.2,
     'FT%':           count  mean       std   min   25%   50%   75%   max
     Team POS
     DET  C      2.0  68.6  13.57645  59.0  63.8  68.6  73.4  78.2
          PG     1.0  86.4       NaN  86.4  86.4  86.4  86.4  86.4
     PHX  C      1.0  74.6       NaN  74.6  74.6  74.6  74.6  74.6
     UTAH C      1.0  63.6       NaN  63.6  63.6  63.6  63.6  63.6
          PG     1.0  85.5       NaN  85.5  85.5  85.5  85.5  85.5}
    """
    # Check if nba_data is a DataFrame
    if not isinstance(nba_data, pd.DataFrame):
        raise TypeError("nba_data must be a DataFrame.")

    # Check if teams_filter is a list
    if not isinstance(teams_filter, list) and teams_filter is not None:
        raise TypeError("teams_filter must be a list")

    # Check if stats_filter is a list
    if not isinstance(stats_filter, list) and stats_filter is not None:
        raise TypeError("stats_filter must be a list")

    # Check if positions_filter is a list
    if not isinstance(positions_filter, list) and positions_filter is not None:
        raise TypeError("positions_filter must be a list")

    # Check if the stats_filter elements exist in the dataframe
    if stats_filter is not None:
        if not set(stats_filter).issubset(set(nba_data.columns)):
            raise TypeError("Columns mentioned in stats_filter not found" +
                            " in data")

    # Check if the positions_filter elements exist in the dataframe
    if positions_filter is not None:
        if not set(positions_filter).issubset(set(nba_data['POS'].unique())):
            raise TypeError("Columns mentioned in positions_filter not found" +
                            " in data")

    # Check if the teams_filter elements exist in the dataframe
    if teams_filter is not None:
        if not set(teams_filter).issubset(set(nba_data['TEAM'].unique())):
            raise TypeError("Columns mentioned in teams_filter not found" +
                            " in data")

    # Filter data on teams
    if teams_filter is not None:
        nba_data = nba_data[nba_data['TEAM'].isin(teams_filter)]

    # Filter data on positions
    if positions_filter is not None:
        nba_data = nba_data[nba_data['POS'].isin(positions_filter)]

    # Select stats to include
    if stats_filter is not None:
        stats_filter = ['NAME', 'TEAM', 'POS'] + stats_filter
        nba_data = nba_data[stats_filter]

    # If all inputs (stats, teams, and positions) are NULL, show all
    if stats_filter is None and teams_filter is None and \
       positions_filter is None:
        nba_data = nba_data

    # Generate summary
    # If position is null, only group_by Teams
    if positions_filter is None:
        group_by = ['TEAM']
    else:
        group_by = ['TEAM', 'POS']

    stats = dict()
    if stats_filter is None:
        stats_filter = list(nba_data.columns.values)

    stats_filter = [stat for stat in stats_filter if stat not in (
        'NAME', 'TEAM', 'POS')]
    for stat in stats_filter:
        stats[stat] = nba_data.groupby(group_by).describe()[stat]

    return stats
