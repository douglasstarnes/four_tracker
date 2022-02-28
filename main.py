import click

from app import create_app, db
from app.models.crypto_coin import CryptoCoin
from app.utils.gecko import get_coins, get_prices, SYMBOLS


app = create_app()

@app.cli.command("create-db")
@click.option("--reset", is_flag=True)
def create_db(reset):
    if reset:
        print("Dropping tables ...")
        db.drop_all()
    print("Creating db ...")
    db.create_all()

@app.cli.command("get-symbols")
def get_symbols():
    print("Getting coin symbols and ids ...")
    CryptoCoin.query.delete()
    coins = get_coins(SYMBOLS)
    for symbol, id in coins.items():
        crypto_coin = CryptoCoin(coin_symbol=symbol, coin_id=id)
        db.session.add(crypto_coin)
    db.session.commit()

@app.cli.command("get-prices")
@click.option("--force", is_flag=True)
def get_coin_prices(force):
    get_prices(force)
