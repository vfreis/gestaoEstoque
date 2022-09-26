from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
db_name = 'consulta_app_alpha'
DB_NAME = 'atividades.db'
HOST = 'mysql://admin:123456789@meu-consultorio-app-mysql.ciofokjqok2t.us-east-1.rds.amazonaws.com:3306/consulta_app_alpha'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql:///{HOST}'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'{HOST}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Product

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('gestao/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')