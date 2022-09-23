import os
from flask import Flask
from views import views
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.register_blueprint(views, url_prefix = '/')

DB_NAME = 'database.db'
db = SQLAlchemy()
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

if __name__ == '__main__':
    porta = int(os.environ.get('PORT', 5002))
    app.run(host = '0.0.0.0', port = porta, debug = True)