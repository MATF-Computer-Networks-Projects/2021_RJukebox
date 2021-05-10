from flask import Flask, Blueprint, render_template,flash,request,redirect,url_for
from utilities.hash_utilities import generate_hash
from classes.User import User
from classes.Song import Song
from flask_login import login_user, login_required, logout_user, current_user
frontend = Blueprint('frontend', __name__)
@frontend.route('/')  
def index():
    return render_template("home.html")

"""
@frontend.route('/login',methods=['GET', 'POST']) # brisi ifove samo post
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
@frontend.route('/logout')
def logout():
    return render_template("home.html")
"""

@frontend.route('/sign-up', methods=['GET','POST']) #samo get bez if
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
    #request.label(f'Account created. Token: {token}',category="success") kako ovde staviti label?
    return render_template('user.html',user=user.name,token=token)
@frontend.route('/songs',methods=['GET','POST'])
def songs():
    if request.method =='GET':
        return render_template('songs.html')
    song_name = request.form.get('song')
    username = request.form.get('user')
    artist = request.form.get('artist')
    genre = request.form.get('genre')
    yt_link=request.form.get('yt_link')
    song=Song(artist,genre,song_name,yt_link)   

    success=song.input_song()

    if not success:
        flash("Song already exists!", category='error')
        return render_template("songs.html")
        
   
    return render_template('added_song.html',name=song.song_name)
@frontend.route('/charts')
def charts():
    return render_template('charts.html')    
@frontend.route('/user')
def main():
    return render_template('user.html')
