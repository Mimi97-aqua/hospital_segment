from flask import Flask
from .models import db
from .routes import register_routes
from flask_migrate import  Migrate

import os


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patients3.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'static/uploads')
    app.config['SECRET_KEY'] = os.urandom(24)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    register_routes(app)

    return app
