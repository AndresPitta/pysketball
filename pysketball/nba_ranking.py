def nba_ranking(data, column_name, by, top = 10):
    """
    Generates a ranking and a visualization based on a column of a dataset  

    Parameters
    ----------
    data : pandas.DataFrame
        pandas DataFrame where we calculate the ranking from
    column_name : str
        name of the column we want to rank
    by : str
        name of the column we want to rank by
    top : int
        number of elements for the ranking. Default is 10.

    Returns
    -------
    ranking : pandas.DataFrame
        Ranking table
    display : altair barplot
        A ranking visualization

    Examples
    --------
    >>> from pysketball import nba_ranking
    >>> nba_data = pd.read_csv("data/nba_data.csv")
    >>> nba_ranking(nba_data, 'Player', 'TD3', 10)
    """
    return (1)