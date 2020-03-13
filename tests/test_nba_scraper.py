import pandas as pd

from pysketball import nba_scraper

from pytest import raises


def test_nba_scraper_input_type():
    """
    The function tests the nba_scraper function with various ranges of inputs
    to ensure the functionality is not
    broken.

    Examples
    --------
    >>> test_nba_scraper_input_type()
    """

    # Test wrong season_year input
    with raises(TypeError):
        nba_scraper.nba_scraper(
            season_year=-3.5, season_type="regular", csv_path=None)

    # Test wrong season_type input
    with raises(TypeError):
        nba_scraper.nba_scraper(
            season_year=2018, season_type="hello", csv_path=None)

    # Test wrong csv_path input not ending with ".csv"
    with raises(TypeError):
        nba_scraper.nba_scraper(
            season_year=2018, season_type="regular", csv_path="nba_2018")

    # Test wrong csv_path input type
    with raises(TypeError):
        nba_scraper.nba_scraper(
            season_year=2018, season_type="regular", csv_path=123)

    # Test wrong csv_path input type
    with raises(TypeError):
        nba_scraper.nba_scraper(
            season_year=2018, season_type="regular", csv_path=123)


def test_nba_scraper_output_df():
    """
    The function tests the nba_scraper function to check if it returns a
    DataFrame as output.

    Examples
    --------
    >>> test_nba_scraper_output_df()
    """

    assert isinstance(nba_scraper.nba_scraper(
        2018, "postseason"), pd.DataFrame) is True


def test_nba_scraper_output_csv(tmp_path):
    """
    The function tests the nba_scraper function to check if the output csv
    scraped has the same dimensions as the output dataframe returned from
    the function itself.

    Examples
    --------
    >>> test_nba_scraper_output_csv()
    """
    # tmp_path is a pathlib object.
    d = tmp_path / "sub"
    d.mkdir()
    # Create a csv file object for storing scraped data to be assigned later on
    p = d / "nba_2001.csv"

    # Note that p is a pathlib object. To get path in string format, you have
    # to use str(p.resolve())
    nba_2001 = nba_scraper.nba_scraper(
        2001, "regular", csv_path=str(p.resolve()))
    nba_2001_csv = pd.read_csv(str(p.resolve()))

    assert nba_2001.shape == nba_2001_csv.shape
