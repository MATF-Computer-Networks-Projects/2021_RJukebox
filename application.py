from flask import Flask, render_template,flash,request,redirect,url_for # izbrisi suvisni svi sem flask
import os
import defaults
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash #importuj iz util
import logging 
from utilities.logger_utilities import setup_logger
from classes.User import User #prebaci
from test_db.create_db import setup_db
from flask_login import login_user, login_required, logout_user, current_user # cela linija
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
    app.config['SECRET_KEY']='asdasdasdasdasdasd'#dot env
    @app.route('/')  
    def index():
        return render_template("home.html")
    @app.route('/login',methods=['GET', 'POST']) # brisi ifove samo post
    def login():
        if request.method =='POST':
            user=request.form.get('user')
            password=request.form.get('password')
            if user:
                if check_password_hash(user.password,password):
                    flash('Logged in successfully!', category='success')
                    login_user(user,remember=True)
                    return redirect(url_for('views.main'))
                else:
                    flash('Incorrect password, try again', category='error')
            else:
                flash('Email does not exist',category='error')        
        return render_template("login.html")
    @app.route('/logout')
    @login_required
    def logout():
        return redirect(url_for('auth.login'))
    @app.route('/main')
    def main():
        return render_template('main.html')

    @app.route('/sign-up', methods=['GET','POST']) #samo get bez if
    def signup():
        if request.method =='GET':
            return render_template('sign_up.html')
        username = request.form.get('user')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User(username, password1)

        if password1 != password2:
            flash('Password must match',category='error')
            return render_template("sign_up.html")
        
        success = user.input_user()

        if not success:
            flash("User must have atleast 3 chars, password 4.", category='error')
            return render_template("sign_up.html")
        
        token = user.get_encoded_token()
        flash(f'Account created. Token: {token}',category="success")
        return redirect(render_template('main.html'))
            
        
