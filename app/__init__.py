#app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

#create database object globally to be used in other modules
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app) # to initialize the database with the Flask app

    from app.routes.auth import auth_bp # to import the authentication blueprint from the auth module
    from app.routes.tasks import task_bp
    app.register_blueprint(auth_bp) # to register the authentication blueprint with the Flask app
    app.register_blueprint(task_bp) # to register the tasks blueprint with the Flask app

    return app