import requests
import os

API_KEY = os.getenv("CRYPTOPANIC_KEY")

def get_latest_news():
    url = "https://cryptopanic.com/api/developer/v2/posts/"

    params = {
        "auth_token": API_KEY,
        "kind": "news",
        "public": "true",
        "currencies": "BTC"
    }

    response = requests.get(url, params=params, timeout=10)

    if response.status_code != 200:
        print("Status:", response.status_code)
        print("Response:", response.text)
        return []

    data = response.json()

    news = []

    for item in data.get("results", []):
        news.append({
            "id": item.get("id"),
            "title": item.get("title"),
            "published_at": item.get("published_at"),
            "source": item.get("source", {}).get("title"),
            "votes": item.get("votes"),
        })

    return news

print("API KEY:", API_KEY)