from flask import Flask
from flask_migrate import Migrate

from .model import configure as config_db
from .serializer import configure as config_ma


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../temp/teste.db'

    config_db(app)
    config_ma(app)

    Migrate(app, app.db)

    from .games import bp_games
    app.register_blueprint(bp_games)

    return app
