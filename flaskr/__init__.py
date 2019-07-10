#!/usr/bin/env python3

import os

from flask import Flask
from flask_mail import Mail
from database import db
from routes.api import api


def create_app():
    """ Basic application factory for setting up the Flask app
    """
    mail = Mail()

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv[DATABASE_CONNECTION_STRING]

    db.init_app(app)
    mail.init_app(app)

    app.register_blueprint(api)

    return app
