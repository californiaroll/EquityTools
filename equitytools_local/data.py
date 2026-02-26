"""Utilities for loading, cleaning, and transforming financial data."""

__all__ = [    
    "get_3_month_tbill",
    "get_ticker_data",
    "load_price_data",
    "load_60_days_of_prices",
    "download",
    "get_company_financials",
    "get_options_data"
]

import yfinance as yf
import pandas as pd
import numpy as np

def get_3_month_tbill():
    """ Get three month t-bill rate"""
    return yf.Ticker("^IRX") 
    
def get_ticker_data(ticker_symbol):
    """Gets ticker data from yFinance."""
    return yf.Ticker(ticker_symbol) 

def load_price_data(ticker, start=None, end=None):
    """Load price data for a given ticker."""
    return yf.Ticker(ticker)

def load_60_days_of_prices(ticker_symbol):
    """Load 60 days of price data for a given ticker."""
    return yf.download(ticker_symbol, period="60d", interval="1d", progress=True)

def download(ticker, start=None, end=None):
    """Download price data for a given ticker."""
    return yf.download(ticker, start, end)

def get_financials(ticker):
    """Get Income Statement"""
    try:
        stock = yf.Ticker(ticker)

        pnl = stock.financials  # Income Statement
        bs = stock.balance_sheet  # Balance Sheet
        cf = stock.cashflow  # Cash Flow Statement

        # Concatenate financials into one DataFrame
        fs = pd.concat([pnl, bs, cf])

        if fs.empty:
            return None

        # Replace NaN values with None for better JSON serialization
        fs = fs.replace({np.nan: None})

        # Transpose data so that items are rows and dates are columns
        fs_transposed = fs.T
        fs_transposed['Ticker'] = ticker
        fs_transposed.reset_index(inplace=True)
        fs_transposed.rename(columns={'index': 'Date'}, inplace=True)
        fs_transposed['Date'] = pd.to_datetime(fs_transposed['Date']).dt.year

        # Sort the data by Date and then limit it to the latest 4 years
        fs_transposed = fs_transposed.sort_values(by='Date', ascending=False).head(4)  # Limiting to 4 years

        return fs_transposed

    except Exception as e:
        print(f"Error fetching financials for {ticker}: {e}")
        return None

def get_company_financials(ticker):
    """ Get company financials from yFinance"""
    if not ticker:
        print("No ticker provided")
        return

    try:
        financial_data = get_financials(ticker)
        if financial_data is None or financial_data.empty:
            print(f"No financial data found for the given ticker: {ticker}")
            return

        # Set pandas to display all columns or a limited number of columns
        pd.set_option('display.max_columns', 20)  # Set to 20 columns (adjust as needed)
        
        # Print the financial data
        # print(financial_data)
        return financial_data

    except Exception as e:
        print(f"Failed to fetch stock data: {str(e)}")

def get_options_data(ticker_symbol):
    """ Get the options trading for a ticker """
    try:
        # Create a Ticker object
        ticker = yf.Ticker(ticker_symbol)

        # Get available option expiration dates
        expirations = ticker.options
        if not expirations:
            print(f"No options data available for {ticker_symbol}.")
            return

        # print(f"Available expiration dates for {ticker_symbol}:")
        # for date in expirations:
            # print(" -", date)

        # Example: Get the first expiration date's option chain
        first_expiration = expirations[0]
        # print(f"\nFetching option chain for expiration: {first_expiration}")

        option_chain = ticker.option_chain(first_expiration)

        # Calls and puts DataFrames
        calls_df = option_chain.calls
        puts_df = option_chain.puts

        return calls_df, puts_df

    except Exception as e:
        print(f"Error fetching options data: {e}")