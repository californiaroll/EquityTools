"""
plotting.py
Visualization utilities for charts and financial plots.
"""
import matplotlib.pyplot as plt

def plot_confidence_interval(ticker_symbol, rangeForTickerInOneYear, current_price):
    plt.bar(['2.5% Result', 'Current Stock Price', '97.5% Result'], [rangeForTickerInOneYear[0], current_price, rangeForTickerInOneYear[1]], color='gray')
    plt.title('95% Confidence Interval for One Year Out - ' + ticker_symbol)
    plt.show()
    
def plot_price_series(dates, prices):
    """Plot price series."""
    pass


def plot_volatility(stock_data):
    """Plot volatility over time."""
    # Line chart for daily returns
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data.index, stock_data['volatility'])
    plt.title('Stock Volatility')
    plt.xlabel('Date')
    plt.ylabel('Volatility')
    plt.grid(True)
    plt.show()
    pass

    
def plot_stock_daily_returns(stock_data):
    # Line chart for daily returns
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data.index, stock_data['returns'])
    plt.title('Stock Daily Returns')
    plt.xlabel('Date')
    plt.ylabel('Daily Return')
    plt.grid(True)
    plt.show()
    pass

def plot_daily_stock_returns2(stock_data):
    # Line chart for daily returns
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data.index, stock_data['Daily Return'])
    plt.title('Stock Daily Returns')
    plt.xlabel('Date')
    plt.ylabel('Daily Return')
    plt.grid(True)
    plt.show()   
    pass


def plot_histogram_of_stock_returns(stock_data):
    # Histogram of returns
    plt.figure(figsize=(10, 3))
    plt.hist(stock_data['returns'], bins=30, edgecolor='black')
    plt.title('Distribution of Daily Returns')
    plt.xlabel('Daily Return')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()
    pass

def plot_histogram_of_stock_returns2(stock_data):
    # Histogram of returns 2
    plt.figure(figsize=(10, 12))
    plt.hist(stock_data['Daily Return'], bins=30, edgecolor='black')
    plt.title('Distribution of Daily Returns')
    plt.xlabel('Daily Return')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

def plot_ebitda_by_year(financial_data):
    """Plot EBITDA by year"""
    plt.figure(figsize=(8, 5))
    fig = financial_data["EBITDA"].plot(kind='bar')
    fig.set_title('EBITDA by Year')
    fig.set_xlabel('Year')
    fig.set_ylabel('EBITDA ($Billion)')
    fig.set_xticklabels(financial_data["Date"])
    pass



def plot_option_payoff(strikes, payoffs):
    """Plot option payoff diagram."""
    pass


def plot_dcf_components(years, cash_flows, discounted_values):
    """Plot DCF components."""
    pass