from news import get_latest_news
from event_analyzer import analyze_event_impact
from coin_detector import detect_coins
from sentiment_analyzer import analyze_sentiment

news = get_latest_news()
reactions = analyze_event_impact(news)

if not news:
    print("No news returned.")
else:
    for article in news[:5]:

        coins = detect_coins(article["title"])
        sentiment, score = analyze_sentiment(article["title"])

        print("-" * 50)
        print("Title:", article["title"])
        print("Published:", article["published_at"])
        print("Detected coins:", coins)
        print("Sentiment:", sentiment)
        print("Score:", score)


for r in sorted(reactions, key=lambda x: x["volatility"], reverse=True)[:5]:
    print("\nASSET:", r["asset"])
    print("VOLATILITY REACTION:", round(r["volatility"], 3), "%")
    print("HEADLINE:", r["headline"])

import nltk
nltk.download('vader_lexicon')