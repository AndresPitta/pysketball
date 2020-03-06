from pysketball import nba_scraper
from pytest import raises
import pandas as pd

def test_input_type_nba_scraper():
    
    # Test wrong season_year input
    with raises(TypeError):
            nba_scraper.nba_scraper(season_year = -3.5, season_type = "regular", csv_path = None)
    
    # Test wrong season_type input
    with raises(TypeError):
            nba_scraper.nba_scraper(season_year = 2018, season_type = "hello", csv_path = None)

    # Test wrong csv_path input not ending with ".csv"
    with raises(TypeError):
            nba_scraper.nba_scraper(season_year = 2018, season_type = "regular", csv_path = "nba_2018")

    # Test wrong csv_path input type
    with raises(TypeError):
            nba_scraper.nba_scraper(season_year = 2018, season_type = "regular", csv_path = 123)

    # Test wrong csv_path input type
    with raises(TypeError):
            nba_scraper.nba_scraper(season_year = 2018, season_type = "regular", csv_path = 123)

def test_nba_scraper_output_df():

        assert isinstance(nba_scraper.nba_scraper(2018, "postseason"), pd.DataFrame) == True

def test_nba_scraper_output_csv(tmp_path):
        
        # tmp_path is a pathlib object. 
        d = tmp_path / "sub"
        d.mkdir()
        # Create a csv file object for storing scraped data to be assigned later on
        p = d / "nba_2001.csv"
        
        # Note that p is a pathlib object. To get path in string format, you have to use str(p.resolve())
        nba_2001 = nba_scraper.nba_scraper(2001,"regular", csv_path = str(p.resolve()))
        nba_2001_csv = pd.read_csv(str(p.resolve()))

        assert nba_2001.shape == nba_2001_csv.shape