from flask import Flask, render_template,flash,request

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
    import api.api_post as api_post
    import api.api_delete as api_delete
    import api.api_patch as api_patch

    app.register_blueprint(api_get.api_getter)
    app.register_blueprint(api_post.api_post)
    app.register_blueprint(api_delete.api_delete)
    app.register_blueprint(api_patch.api_patch)
    app.config['SECRET_KEY']='asdasdasdasdasdasd'
    @app.route('/', methods=['GET', 'POST'])
    def index():
        return render_template("home.html")
    @app.route('/login',methods=['GET', 'POST'])
    def login():
        
        return render_template("login.html")
    @app.route('/logout')
    def logout():
        return "<p>logout</p>"
    @app.route('/sign-up', methods=['GET', 'POST'])
    def signup():
        if request.method=='POST':
            user=request.form.get('user')
            password1=request.form.get('password1')
            password2=request.form.get('password2')
            if len(user) < 3:
                flash('User must be greater then 3 characters',category='error')
            elif password1 != password2:
                flash('Password must match',category='error')
            elif len(password1) < 4:
                flash('Password must be greater then 4 characters',category='error')
            else:
            #add user to database
                flash('Account created!',category="success")

        return render_template("sign_up.html")
