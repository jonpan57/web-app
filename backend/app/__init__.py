from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()


def register_extension(app):
    db.init_app(app)
    login_manager.init_app(app)


def configure_database(app):
    @app.before_frist_request
    def initialize_database():
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()


def configure_logs(app):
    pass


def create_app(config):
    app = Flask(__name__, template_folder='dist')
    app.config.from_object(config)
    register_extension(app)
    configure_database(app)
    configure_logs(app)


    return app
