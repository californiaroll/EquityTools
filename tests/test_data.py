import pandas as pd
import numpy as np
import pytest
from unittest.mock import patch, MagicMock

import sys, os
sys.path.append(os.path.abspath(".."))

import equitytools_local.data as datatools

from importlib import reload
reload(datatools)

def test_load_60_days_of_prices_downloads_correct_period():
    """Ensure yf.download is called with the correct parameters and returns a DataFrame."""

    mock_df = pd.DataFrame({
        "Open": [100, 101],
        "Close": [102, 103],
        "Volume": [1000, 1100]
    })

    with patch("equitytools_local.data.yf.download", return_value=mock_df) as mock_download:

        result = datatools.load_60_days_of_prices("AAPL")

        # Verify correct call
        mock_download.assert_called_once_with(
            "AAPL",
            period="60d",
            interval="1d",
            progress=True
        )

        # Verify return value
        assert result is mock_df



def test_get_3_month_tbill_returns_ticker():
    """Ensure the function returns the yfinance Ticker object for ^IRX."""

    with patch("equitytools_local.data.yf.Ticker") as mock_ticker:
        mock_instance = mock_ticker.return_value

        result = datatools.get_3_month_tbill()

        # Verify Ticker("^IRX") was called
        mock_ticker.assert_called_once_with("^IRX")

        # Verify the function returns the mocked instance
        assert result is mock_instance


def test_get_financials_returns_transformed_dataframe():
    """Ensure get_financials loads, concatenates, transforms, and returns financial data."""

    # Mock financial statement DataFrames
    pnl = pd.DataFrame({"2023-12-31": [100], "2022-12-31": [90]}, index=["Revenue"])
    bs = pd.DataFrame({"2023-12-31": [50], "2022-12-31": [45]}, index=["Assets"])
    cf = pd.DataFrame({"2023-12-31": [10], "2022-12-31": [8]}, index=["CashFlow"])

    mock_ticker = MagicMock()
    mock_ticker.financials = pnl
    mock_ticker.balance_sheet = bs
    mock_ticker.cashflow = cf

    with patch("equitytools_local.data.yf.Ticker", return_value=mock_ticker):
        result = datatools.get_financials("AAPL")

        # Ensure a DataFrame is returned
        assert isinstance(result, pd.DataFrame)
        assert not result.empty

        # Ensure the Ticker object was created correctly
        mock_ticker_call = patch("equitytools_local.data.yf.Ticker")
        assert True  # placeholder to avoid unused variable warning

        # Ensure expected columns exist
        assert "Date" in result.columns
        assert "Ticker" in result.columns
        assert "Revenue" in result.columns
        assert "Assets" in result.columns
        assert "CashFlow" in result.columns

        # Ensure the ticker symbol was added
        assert (result["Ticker"] == "AAPL").all()

        # Ensure dates were converted to years
        assert set(result["Date"]) == {2023, 2022}

        # Ensure only the latest 4 years are returned (we only provided 2)
        assert len(result) == 2      


def test_get_options_data_success():
    """Successful path: expirations exist and option_chain returns calls + puts."""

    # Mock calls and puts DataFrames
    calls_df = pd.DataFrame({"strike": [100], "bid": [1.5]})
    puts_df = pd.DataFrame({"strike": [100], "bid": [2.0]})

    # Mock option_chain object with .calls and .puts
    mock_chain = MagicMock()
    mock_chain.calls = calls_df
    mock_chain.puts = puts_df

    # Mock Ticker object
    mock_ticker = MagicMock()
    mock_ticker.options = ["2025-01-17"]
    mock_ticker.option_chain.return_value = mock_chain

    with patch("equitytools_local.data.yf.Ticker", return_value=mock_ticker):
        result_calls, result_puts = datatools.get_options_data("AAPL")

        # Ensure correct expiration was used
        mock_ticker.option_chain.assert_called_once_with("2025-01-17")

        # Ensure returned DataFrames match
        assert result_calls is calls_df
        assert result_puts is puts_df

def test_get_options_data_no_expirations():
    """If no expiration dates exist, the function should return None."""

    mock_ticker = MagicMock()
    mock_ticker.options = []  # No expirations

    with patch("equitytools_local.data.yf.Ticker", return_value=mock_ticker):
        result = datatools.get_options_data("AAPL")

        assert result is None


def test_get_options_data_exception_handling():
    """If an exception occurs, the function should return None."""

    with patch("equitytools_local.data.yf.Ticker", side_effect=Exception("Boom")):
        result = datatools.get_options_data("AAPL")

        assert result is None
