from pysketball import nba_ranking
from pytest import raises
import pandas as pd
import warnings

data_dictionary = {'A': [1, 2, 3],
                   'B': [2, 3, 4],
                   'C': ["A", "B", "C"]}

data = pd.DataFrame(data_dictionary)

def test_nba_ranking_input():
    '''
    This function test the function test_nba_ranking from package pysketball to make sure the functionality is not broken.
    
    Examples
    -------------------
    >>> test_nba_ranking_input()   
    
    '''
    
     # Test wrong data input
    with raises(TypeError):
        nba_ranking.nba_ranking('A', 'C' , 'B', top = 2, descending = True, fun = 'mean')
            
     # Test wrong column input
    with raises(TypeError):
        nba_ranking.nba_ranking(data, ['C'] , 'B', top = 2, descending = True, fun = 'mean')
            
    # Test wrong by input
    with raises(TypeError):
        nba_ranking.nba_ranking(data, 'C' , ['B'], top = 2, descending = True, fun = 'mean')
            
    # Test wrong top input
    with raises(TypeError):
        nba_ranking.nba_ranking(data, 'C' , 'B', top = 'a', descending = True, fun = 'mean')
            
    # Test wrong descending input
    with raises(TypeError):
        nba_ranking.nba_ranking(data, 'C' , 'B', top = 2, descending = 'a', fun = 'mean')
        
    # Test wrong descending input
    with raises(TypeError):
        nba_ranking.nba_ranking(data, 'C' , 'B', top = 2, descending = True, fun = 'a')
      
    # Testing the warning 
    with warnings.catch_warnings(record=True):
        warnings.simplefilter("always")
        nba_ranking.nba_ranking(data, 'C' , 'B', top = 100, descending = True, fun = 'mean')
        
def test_nba_ranking_output():
    '''
    This function test the function test_nba_ranking from package pysketball to make sure the functionality is not broken.
    
    Examples
    -------------------
    >>> test_nba_ranking_output()   
    
    '''
    
    assert isinstance(nba_ranking(data, 'C' , 'B', top = 2, ascending = False, fun = 'mean'), tuple)
    assert isinstance(nba_ranking(data, 'C' , 'B', top = 2, ascending = False, fun = 'mean')[0],pd.DataFrame)
    assert isinstance(nba_ranking(data, 'C' , 'B', top = 2, ascending = False, fun = 'mean')[1], alt.vegalite.v3.api.LayerChart)