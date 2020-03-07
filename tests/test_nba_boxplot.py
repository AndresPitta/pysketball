from pysketball import nba_boxplot
import pandas as pd
import numpy as np
from pytest import raises
   
def test_nba_boxplot():
  
    """
    The function tests the test_nba_boxplot function with various ranges of values to ensure the functionality is not
    broken
    Examples
    --------
    >>> test_nba_boxplot()
    """
  
    nba_2018 = pd.read_csv("https://raw.githubusercontent.com/kfoofw/nba_espn/master/0.data/NBA_reg_2018-2019.csv")

    with raises(TypeError, match= "Input 'dataset' is not a dataset!"):  
      nba_boxplot.nba_boxplot(np.array([4, 3, 3]), stats= "PTS", position= 'POS')
        
    with raises(ValueError, match= "position and teams argument cannot be used simultaneously, choose one"):
        nba_boxplot.nba_boxplot(nba_2018, stats= "GP", position= "POS", teams= ("ORL", "UTAH", "LAC", "MIN", "BOS"))
        
    with raises(ValueError, match= "Empty arguments, choose either position or teams argument for plot"):
        nba_boxplot.nba_boxplot(nba_2018, stats= "GP", position= None, teams= None)
        
    with raises(TypeError, match= "stats argument has to be numeric"):
        nba_boxplot.nba_boxplot(nba_2018, stats= "Team", position= "POS")
