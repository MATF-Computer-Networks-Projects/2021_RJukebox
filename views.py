from flask import Blueprint, render_template
from flask_login import  login_required, current_user
from .models import song
views=Blueprint('views',__name__)

@views.route('/',methods=['GET','POST'])
@login_required
def home():
    if request.method=='POST':

        song=request.form.get('song')
        new_song=Song(data=song)
        db.session.commit()
        flash('Song added',category='success')

    return render_template("home.html")