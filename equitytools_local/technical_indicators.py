"""
technical_indicators.py

Technical indicator utilities implemented with pure pandas.
Stable with Python 3.11 and yfinance DataFrames.
"""

import pandas as pd


def _normalize_df(df: pd.DataFrame) -> pd.DataFrame:
    """Ensure all columns are 1D Series."""
    df = df.copy()
    for col in df.columns:
        if isinstance(df[col], pd.DataFrame):
            df[col] = df[col].iloc[:, 0]
    return df


def add_sma(df: pd.DataFrame, length: int = 20) -> pd.DataFrame:
    df = _normalize_df(df)
    df[f"SMA_{length}"] = df["Close"].rolling(window=length, min_periods=1).mean()
    return df


def add_ema(df: pd.DataFrame, length: int = 20) -> pd.DataFrame:
    df = _normalize_df(df)
    df[f"EMA_{length}"] = df["Close"].ewm(span=length, adjust=False).mean()
    return df


def add_rsi(df: pd.DataFrame, length: int = 20) -> pd.DataFrame:
    df = _normalize_df(df)
    delta = df["Close"].diff()

    gain = delta.where(delta > 0, 0.0)
    loss = -delta.where(delta < 0, 0.0)

    avg_gain = gain.rolling(window=length, min_periods=length).mean()
    avg_loss = loss.rolling(window=length, min_periods=length).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    df[f"RSI_{length}"] = rsi
    return df


def add_macd(df: pd.DataFrame,
             fast: int = 12,
             slow: int = 26,
             signal: int = 9) -> pd.DataFrame:
    df = _normalize_df(df)
    ema_fast = df["Close"].ewm(span=fast, adjust=False).mean()
    ema_slow = df["Close"].ewm(span=slow, adjust=False).mean()

    macd = ema_fast - ema_slow
    macd_signal = macd.ewm(span=signal, adjust=False).mean()
    macd_hist = macd - macd_signal

    df["MACD"] = macd
    df["MACD_signal"] = macd_signal
    df["MACD_hist"] = macd_hist
    return df


def add_bollinger_bands(df: pd.DataFrame,
                        length: int = 20,
                        std: float = 2.0) -> pd.DataFrame:
    df = _normalize_df(df)
    ma = df["Close"].rolling(window=length, min_periods=1).mean()
    dev = df["Close"].rolling(window=length, min_periods=1).std()

    upper = ma + std * dev
    lower = ma - std * dev

    df[f"BB_middle_{length}"] = ma
    df[f"BB_upper_{length}"] = upper
    df[f"BB_lower_{length}"] = lower
    return df


def add_all_indicators(df: pd.DataFrame) -> pd.DataFrame:
    df = _normalize_df(df)
    df = add_sma(df, 20)
    df = add_ema(df, 20)
    df = add_rsi(df, 14)
    df = add_macd(df)
    df = add_bollinger_bands(df, 20, 2.0)
    return df
