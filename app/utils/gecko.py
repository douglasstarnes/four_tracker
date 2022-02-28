import datetime

import requests

from app import db

from app.models.crypto_coin import CryptoCoin
from app.models.coin_price import CoinPrice

SYMBOLS = ["btc", "eth", "bnb", "xrp", "ada", "sol", "dot", "avax", "doge", "shib"]

GECKO_COIN_LIST_URL = "https://api.coingecko.com/api/v3/coins/list"
GECKO_COIN_PRICE_URL = "https://api.coingecko.com/api/v3/simple/price?ids={}&vs_currencies=usd"

def _get_recent_price_refresh_timestamp():
    coin_price = CoinPrice.query.order_by(CoinPrice.timestamp.desc()).first()
    if coin_price:
        return coin_price.timestamp
    return datetime.datetime.now() - datetime.timedelta(minutes=10)

def get_coins(symbols):
    response = requests.get(GECKO_COIN_LIST_URL)
    coin_list = response.json()
    return dict([(symbol, next(coin for coin in coin_list if coin["symbol"] == symbol)["id"]) for symbol in symbols])

def get_prices(force):
    delta = datetime.datetime.now() - _get_recent_price_refresh_timestamp()
    if delta.seconds > 300 or force == True:
        coins = CryptoCoin.query.filter(CryptoCoin.coin_symbol.in_(SYMBOLS))
        ids = ",".join([coin.coin_id for coin in coins])
        response = requests.get(GECKO_COIN_PRICE_URL.format(ids))
        prices = response.json()
        timestamp = datetime.datetime.now()
        for coin_id in prices.keys():
            price = prices[coin_id]["usd"]
            coin_price = CoinPrice(coin_id=coin_id, current_value=price, timestamp=timestamp)
            db.session.add(coin_price)
        db.session.commit()
        print("Updated coin prices ...")
    else:
        print("Less that 5 minutes since last update ... no update needed")
