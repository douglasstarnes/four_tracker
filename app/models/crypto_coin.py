from app import db

class CryptoCoin(db.Model):
    __tablename__ = "crypto_coin"
    
    id = db.Column(db.Integer, primary_key=True)
    coin_symbol = db.Column(db.String(64))
    coin_id = db.Column(db.String(64))

    def __repr__(self):
        return f"<CryptoCoin {self.coin_symbol}/{self.coin_id}>"