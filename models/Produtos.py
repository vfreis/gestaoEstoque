from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Produto():
    
    __tablename__ = 'produtos'

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String)
    preco = db.Column(db.Float)
    categoria = db.Column(db.String)

    
