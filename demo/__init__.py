# -*- coding: utf-8 -*-
from flask import Flask
from .database import db
from .views import bp


def create_app(config='config'):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    app.register_blueprint(bp)

    return app
