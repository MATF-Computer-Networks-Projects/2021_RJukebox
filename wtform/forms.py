from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, TextField,PasswordField

from wtforms.validators import DataRequired, Length


class ContactForm(FlaskForm):
    name=StringField('Name',
    [DataRequired()]
    )
    password=PasswordField(
        'Password',[
            Password(message=("Not a valid password")),
            DataRequired(),
            Length(min=4, message=("Your password is too short."))
        ]
    )

    song=TextField('Song',
    [
        DataRequired()
    ])
    submit=SubmitField('Submit')
    