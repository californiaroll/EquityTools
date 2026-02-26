"""
plotting.py
Visualization utilities for charts and financial plots.
"""

__all__ = [    
    "plot_confidence_interval",
    "plot_volatility"
    "plot_stock_daily_returns",
    "plot_daily_stock_returns2",
    "plot_histogram_of_stock_returns",
    "plot_histogram_of_stock_returns2",
    "plot_ebitda_by_year",
    "plot_simul_lines",
    "plot_price_with_rsi",
    "plot_price_with_bollinger",
    "plotHoldings",
    "plotSecors"
]


import matplotlib.pyplot as plt

def plot_confidence_interval(ticker_symbol, rangeForTickerInOneYear, current_price):
    plt.bar(['2.5% Result', 'Current Stock Price', '97.5% Result'], [rangeForTickerInOneYear[0], current_price, rangeForTickerInOneYear[1]], color='gray')
    plt.title('95% Confidence Interval for One Year Out - ' + ticker_symbol)
    plt.show()

    
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

def plot_simul_lines(data):
    """
    Plots multiple simulation lines from a list of lists of numbers.
    Each inner list is treated as a separate line (y-values).
    X-values are generated automatically as indices.
    """
    # Validate input
    if not isinstance(data, list) or not all(isinstance(row, list) for row in data):
        raise ValueError("Data must be a list of lists of numbers.")

    plt.figure(figsize=(12, 6))
    
    for idx, y_values in enumerate(data):
        if not all(isinstance(v, (int, float)) for v in y_values):
            raise ValueError(f"Line {idx+1} contains non-numeric values.")
        x_values = list(range(len(y_values)))  # Auto-generate X values
        plt.plot(x_values, y_values, marker='o', label=f"Simulation {idx+1}")

    plt.xlabel("Year")
    plt.ylabel("$")
    plt.title("10 Simulations")
    plt.legend()
    plt.grid(True)
    plt.show()
    
def plot_price_with_rsi(df, ticker: str):
    """
    Plot closing prices and RSI on two aligned subplots.
    Assumes df contains 'Close' and 'RSI_20' columns.
    """

    fig, (ax_price, ax_rsi) = plt.subplots(
        2, 1, figsize=(12, 8), sharex=True,
        gridspec_kw={'height_ratios': [3, 1]}
    )

    # --- Price chart ---
    ax_price.plot(df.index, df["Close"], label="Close Price", color="blue")
    ax_price.set_title(f"{ticker} Closing Price")
    ax_price.set_ylabel("Price ($)")
    ax_price.grid(True, linestyle="--", alpha=0.5)
    ax_price.legend()

    # --- RSI chart ---
    ax_rsi.plot(df.index, df["RSI_14"], label="RSI (20)", color="purple")
    ax_rsi.axhline(70, color="red", linestyle="--", alpha=0.7)
    ax_rsi.axhline(30, color="green", linestyle="--", alpha=0.7)
    ax_rsi.set_title("Relative Strength Index (RSI 20)")
    ax_rsi.set_ylabel("RSI")
    ax_rsi.set_xlabel("Date")
    ax_rsi.grid(True, linestyle="--", alpha=0.5)
    ax_rsi.legend()

    plt.tight_layout()
    plt.show()

def plot_price_with_bollinger(df, ticker: str, length: int = 20):
    """
    Plot closing prices with Bollinger Bands.
    Assumes df contains:
        - 'Close'
        - f'BB_upper_{length}'
        - f'BB_middle_{length}'
        - f'BB_lower_{length}'
    """

    upper = f"BB_upper_{length}"
    middle = f"BB_middle_{length}"
    lower = f"BB_lower_{length}"

    fig, ax = plt.subplots(figsize=(12, 6))

    # --- Price line ---
    ax.plot(df.index, df["Close"], label="Close Price", color="blue")

    # --- Bollinger Bands ---
    ax.plot(df.index, df[upper], label="Upper Band", color="red", linestyle="--", alpha=0.7)
    ax.plot(df.index, df[middle], label="Middle Band (MA)", color="orange", linestyle="--", alpha=0.7)
    ax.plot(df.index, df[lower], label="Lower Band", color="green", linestyle="--", alpha=0.7)

    # --- Fill between bands ---
    ax.fill_between(df.index, df[lower], df[upper], color="gray", alpha=0.15)

    ax.set_title(f"{ticker} Closing Price with Bollinger Bands ({length})")
    ax.set_ylabel("Price ($)")
    ax.set_xlabel("Date")
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.legend()

    plt.tight_layout()
    plt.show()

def plotHoldings(sizes, labels, ticker_symbol):
    plt.figure(figsize=(8,8))
    plt.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",
    startangle=140,
    pctdistance=0.85
    )
    plt.title(f"{ticker_symbol} Equity Holdings")
    plt.tight_layout()
    plt.show()

def plotSecors(sizes, labels):
    fig, ax = plt.subplots(figsize=(8, 8))
    wedges, texts, autotexts = ax.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%',  # Show percentage
        startangle=140,     # Rotate start
        shadow=True,        # Add shadow
        wedgeprops={'edgecolor': 'black'}
    )
    
    # Improve text appearance
    for text in texts:
        text.set_fontsize(10)
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(9)
    
    # Equal aspect ratio ensures pie is drawn as a circle
    ax.axis('equal')
    plt.title("Sector Allocation", fontsize=14, fontweight='bold')
    plt.tight_layout()
    
    # Show chart
    plt.show()
