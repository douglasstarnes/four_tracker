import requests

SYMBOLS = ["btc", "eth", "bnb", "xrp", "ada", "sol", "dot", "avax", "doge", "shib"]

GECKO_COIN_LIST_URL = "https://api.coingecko.com/api/v3/coins/list"

def get_coins(symbols):
    response = requests.get(GECKO_COIN_LIST_URL)
    coin_list = response.json()
    return dict([(symbol, next(coin for coin in coin_list if coin["symbol"] == symbol)["id"]) for symbol in symbols])
