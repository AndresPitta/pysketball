def nbastats():
    """
    Generate summary stats for NBA players.

    The function filters the dataset further using the arguments provided and
    produces a tibble with summary statistics for a list of columns of a few players or teams.
    The function can only use one of the two filters - playerNames and teamNames. Hence, If playerNames
    are provided, teamNames are ignored.

    Parameters
    ----------
    data : pandas.DataFrame
      A pandas categorical.
    columnNames : list
      A list of column names for whom summary stats are required
    playerNames : list
      A list of player names
    teamNames : list
      A list of team names

    Returns
    -------
    pandas.DataFrame
      The stats summarised in a DataFrame

    Examples
    --------
    >>> from pysketball import nbastats
    >>> nbastats.nbastats(nba_data, columnNames = ['GP', '3PM', 'FT%'], playerNames = ['Stephen Curry', 'Paul George'])
    >>> nbastats.nbastats(nba_data, columnNames = ['GP', '3PM', 'FT%'], teamNames = ['UTAH', 'PHX', 'DET'])
    """
    return None