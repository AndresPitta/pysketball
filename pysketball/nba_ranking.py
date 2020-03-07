import pandas as pd
import altair as alt
import numpy as np
import warnings

def nba_ranking(data, column, by, top = 10, ascending = True, fun = 'mean'):
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
    ascending : bool
        True if we want to rank ascending false otherwise
    fun : {'mean', 'sum'}, default = 'mean'
        function to operate over the ranking variable 

    Returns
    -------
    ranking : pandas.DataFrame
        Ranking table
    display : altair barplot
        A ranking visualization

    Examples
    --------
    >>> from pysketball import nba_ranking
    >>> diction = {'A': [1, 2, 3, 6], 'B': [2, 1, 4, 6], 'C': ["A", "B", "A", "C"]}
    >>> data = pd.DataFrame(diction)
    >>> nba_ranking(data, 'C' , 'B', top = 2, ascending = False, fun = 'mean')
    """
    
    #Checks
    # The data should be a pandas dataframe
    if not isinstance(data, pd.DataFrame):
        raise TypeError("The data should be a pandas df")
        
    # The column argument should be a str
    if not isinstance(column, str):
        raise TypeError("The column argument should be a string")
        
    # The by argument should be a str
    if not isinstance(by, str):
        raise TypeError("The data is not a pandas df")
        
    # The descending argument should be a boolean
    if not isinstance(ascending, bool):
        raise TypeError("The ascending argument should be a boolean")
        
    # The descending argument should be a boolean
    if not (fun in ['sum', 'mean']):
        raise TypeError("The fun argument should be either var or mean")
        
    # Checks if the column exists in the dataframe
    if not column in data.columns:
        raise TypeError(f"Column {column} not found in data")
        
    if not by in data.columns:
        raise TypeError(f"Column {by} not found in data")
  
    # Warning
    
    #Warning to control the number of elements
    number_elements = len(data[column].unique())
    if top > number_elements:
        warnings.warn(f'The number of elements in the ranking is smaller than the one provided. \n Changing top value from {top} to {number_elements}', Warning)
        top = number_elements
    
    # Beginning of the function
    
    #Setting the sorting variable
    if ascending:
        sort_order = 'ascending'
    else:
        sort_order = 'descending'
   
    #Transforming the data
    transformed_data = data[[column, by]].groupby(column).agg(fun).sort_values(by = by, ascending = ascending).head(top).reset_index()
    transformed_data['ranking'] = pd.Series(range(0, len(transformed_data[by])), index = transformed_data.index) + 1
    transformed_data['text'] = transformed_data['ranking'].astype(str) + " - "+ transformed_data[column].astype(str) + " " + transformed_data[by].astype(str)
    
    #Plotting
    plot = alt.Chart(transformed_data).mark_bar(color = "#17408B").encode(
        alt.Y(column + ':N', 
              sort = alt.SortField(field = by,  order = sort_order),
              axis=alt.Axis(labels=False),
              title = ''),
        alt.X(by + ':Q',
              axis=alt.Axis(labels=False))
    ).properties(
        title = f'{column} ranking by {by}',
        height = 700,
        width = 700
    )
    
    text = alt.Chart(transformed_data).mark_text(
        color = "white",
        align = "right",
        baseline = "middle",
        dx = -15,
        size = np.maximum(100/top, 13)
    ).encode(
        alt.Y(column + ':N', 
              sort = alt.SortField(field = by,  order = sort_order),
              axis=alt.Axis(labels=False),
              title = ''),
        alt.X(by + ':Q',
              axis=alt.Axis(labels=False)),
        alt.Text('text:N')
    ).properties(
        title = f'{column} ranking by {by}',
        height = 700,
        width = 700
    )
    
    final_plot = (plot + text)
    return (transformed_data, final_plot)