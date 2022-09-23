from time import timezone
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    price = db.Column(db.Float)
    cetegory = db.Column(db.String)

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150))
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    creation_dt = db.Column(db.Datetime(timezone=True), default = func.now())


    
