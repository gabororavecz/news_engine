import requests

API_KEY = "ae2d5fe724d220b76b9862f9536bf89721b22965"

def get_latest_news():
    url = "https://cryptopanic.com/api/developer/v2/posts/"

    params = {
        "auth_token": API_KEY,
        "kind": "news",
        "public": "true"
    }

    response = requests.get(url, params=params)

    # Always validate response
    if response.status_code != 200:
        print("Status:", response.status_code)
        print("Response:", response.text)
        return []

    data = response.json()

    news = []

    for item in data.get("results", []):
        news.append({
            "title": item.get("title"),
            "published_at": item.get("published_at"),
            "currencies": [c["code"] for c in item.get("currencies", [])]
        })

    return news