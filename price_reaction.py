import ccxt
import pandas as pd

exchange = ccxt.binance()

def get_price_window(symbol, minutes=30):
    timeframe = "1m"
    limit = minutes

    bars = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
    df = pd.DataFrame(
        bars, columns=["timestamp", "open", "high", "low", "close", "volume"]
    )

    return df

def volatility_reaction(df):
    df["returns"] = df["close"].pct_change()
    return df["returns"].std() * 100