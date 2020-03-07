from pysketball import nba_boxplot
import pandas as pd
import numpy as np
from pytest import raises
import altair as alt

   
def test_nba_boxplot():
  
    """
    The function tests the test_nba_boxplot function with various ranges of values to ensure the functionality is not
    broken
    Examples
    --------
    >>> test_nba_boxplot()
    """
    
    #test sample
    nba_2018 = pd.read_csv("https://raw.githubusercontent.com/kfoofw/nba_espn/master/0.data/NBA_reg_2018-2019.csv")
    
    #testing input of dataset
    with raises(TypeError, match= "Input 'dataset' is not a dataset!"):  
      nba_boxplot.nba_boxplot(np.array([4, 3, 3]), stats= "PTS", position= 'POS')
    
    #testing position and teams used simultaneously    
    with raises(ValueError, match= "position and teams argument cannot be used simultaneously, choose one"):
        nba_boxplot.nba_boxplot(nba_2018, stats= "GP", position= "POS", teams= ("ORL", "UTAH", "LAC", "MIN", "BOS"))
    
    #testing position and teams empty arguments    
    with raises(ValueError, match= "Empty arguments, choose either position or teams argument for plot"):
        nba_boxplot.nba_boxplot(nba_2018, stats= "GP", position= None, teams= None)
    
    #testing wrong stats type   
    with raises(TypeError, match= "stats argument has to be numeric"):
        nba_boxplot.nba_boxplot(nba_2018, stats= "Team", position= "POS")
    
        
    #testing plot output for teams
    assert isinstance(nba_boxplot.nba_boxplot(nba_2018, stats= "GP", teams= ("ORL", "UTAH", "LAC")), alt.vegalite.v4.api.Chart)

    #testing plot output for position
    assert isinstance(nba_boxplot.nba_boxplot(nba_2018, stats= "GP", position= 'POS', teams= None), alt.vegalite.v4.api.Chart)
