from flask import Flask

import os
import defaults

from dotenv import load_dotenv

import logging
from utilities.logger_utilities import setup_logger

from test_db.create_db import setup_db

load_dotenv('.env')
setup_logger(defaults.logger_config)

setup_db()

app = Flask(__name__)

with app.app_context():

    import api.api_getter as api_get

    app.register_blueprint(api_get.api_getter)

    @app.route('/')
    def index():
        return "Main page"
