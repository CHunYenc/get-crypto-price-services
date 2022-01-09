from app import db
from datetime import datetime


class FocusSymbol(db.Model):
    __tablename__ = "focus_symbol"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    exchange = db.Column(db.String(10), nullable=False, default='None')
    symbol = db.Column(db.String(10), nullable=False)


class CryptoPrice(db.Model):
    __tablename__ = "crypto_price"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    exchange = db.Column(db.String(10), nullable=False)
    symbol = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Float, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return f"<id:{id}>"