def aggregate_sentiment(news, detect_coins, analyze_sentiment):

    scores = {}

    for article in news:

        coins = detect_coins(article["title"])
        sentiment, score = analyze_sentiment(article["title"])

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