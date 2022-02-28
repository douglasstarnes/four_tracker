from app import db 


class CoinPrice(db.Model):
    __tablename__ = "coin_price"

    id = db.Column(db.Integer, primary_key=True)
    coin_id = db.Column(db.String(64))
    current_value = db.Column(db.Float())
    timestamp = db.Column(db.DateTime())

    def __repr__(self):
        return f"<CoinPrice {self.coin_id}: ${self.current_value}>"
