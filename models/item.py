# model - ში კოდის ის ნაწილი რომელიც ჩვეენს მონაცემთა ბაზას უკავშირდება db
from models import db


class ItemModels(db.Model):
    __tablename__ = 'item'

    # id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), primary_key=True, unique=True)
    price = db.Column(db.REAL)
    quantity = db.Column(db.Integer)

    def __repr__(self):
        return '<name %r>' % self.name

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def json(self):
        return {"name": self.name, "price": self.price, "quantity": self.quantity}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def add_item_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_item_from_db(self):
        db.session.delete(self)
        db.session.commit()
