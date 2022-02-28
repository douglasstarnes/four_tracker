import click

from app import create_app, db
from app.models.crypto_coin import CryptoCoin


app = create_app()

@app.cli.command("create-db")
@click.option("--reset", is_flag=True)
def create_db(reset):
    if reset:
        print("Dropping tables ...")
        db.drop_all()
    print("Creating db ...")
    db.create_all()
