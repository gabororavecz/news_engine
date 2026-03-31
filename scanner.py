def volatility_breakout(df, lookback=20, threshold=1.5):
    df['range'] = df['high'] - df['low']
    avg_range = df['range'].rolling(lookback).mean()
    latest_range = df['range'].iloc[-1]

    if latest_range > avg_range.iloc[-1] * threshold:
        return True
    return False

def market_regime(df):
    latest = df.iloc[-1]

    if latest['close'] > latest['ema20'] > latest['ema50']:
        return "STRONG UPTREND"

    if latest['close'] < latest['ema20'] < latest['ema50']:
        return "STRONG DOWNTREND"

    return "RANGE / CHOP"

def trade_score(df):
    score = 0
    latest = df.iloc[-1]

    if latest['rsi'] < 30:
        score += 2
    if latest['rsi'] > 70:
        score -= 2

    if latest['close'] > latest['ema20'] > latest['ema50']:
        score += 2
    if latest['close'] < latest['ema20'] < latest['ema50']:
        score -= 2

    if volatility_breakout(df):
        score += 1

    return score

def scan_market(df):
    latest = df.iloc[-1]

    signals = []

    if latest['rsi'] < 30:
        signals.append("OVERSOLD → Long candidate")

    if latest['rsi'] > 70:
        signals.append("OVERBOUGHT → Short candidate")

    if latest['close'] > latest['ema20'] > latest['ema50']:
        signals.append("Bullish momentum")

    if latest['close'] < latest['ema20'] < latest['ema50']:
        signals.append("Bearish momentum")

    if volatility_breakout(df):
        signals.append("Volatility breakout → Momentum trade")

    return signals







