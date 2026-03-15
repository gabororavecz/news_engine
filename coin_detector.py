COINS = {
    "BTC": ["bitcoin", "btc"],
    "ETH": ["ethereum", "eth"],
    "SOL": ["solana", "sol"],
    "ADA": ["cardano", "ada"],
}

def detect_coins(title):
    title = title.lower()

    detected = []

    for coin, keywords in COINS.items():
        for keyword in keywords:
            if keyword in title:
                detected.append(coin)
                break

    return detected