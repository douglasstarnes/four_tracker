from flask import Blueprint

from app.models.crypto_coin import CryptoCoin
from app.models.coin_price import CoinPrice

crypto_blueprint = Blueprint("crypto", __name__)

@crypto_blueprint.route("/current/<coin_symbol>")
def current(coin_symbol):
    crypto_coin = CryptoCoin.query.filter_by(coin_symbol=coin_symbol).first()
    if not crypto_coin:
        return "404"

    coin_id = crypto_coin.coin_id
    coin_price = CoinPrice.query.filter_by(coin_id=coin_id).order_by(CoinPrice.timestamp.desc()).first()

    if not coin_price:
        return "404"

    return f"${coin_price.current_value}"
