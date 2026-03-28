from datetime import datetime, timezone

def aggregate_sentiment(news, detect_coins, analyze_sentiment):

    scores = {}

    now = datetime.now(timezone.utc)

    for article in news:

        coins = detect_coins(article["title"])
        sentiment, score = analyze_sentiment(article["title"])

        # Parse published time
        published_time = datetime.fromisoformat(
            article["published_at"].replace("Z", "+00:00")
        )

        # Time difference in minutes
        minutes_ago = (now - published_time).total_seconds() / 60

        # Weight: more recent = higher weight
        weight = max(0.1, 1 / (1 + minutes_ago / 60))

        for coin in coins:

            if coin not in scores:
                scores[coin] = []

            scores[coin].append(score)

    results = {}

    for coin, coin_scores in scores.items():

        avg_score = sum(coin_scores) / len(coin_scores)

        if avg_score > 0.2:
            signal = "BULLISH"
        elif avg_score < -0.2:
            signal = "BEARISH"
        else:
            signal = "NEUTRAL"

        results[coin] = {
            "articles": len(coin_scores),
            "average_sentiment": avg_score,
            "signal": signal
        }

    return results