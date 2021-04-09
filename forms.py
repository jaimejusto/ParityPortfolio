from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, InputRequired, Length, EqualTo, Email


class LoginForm(FlaskForm):
    # username must be between 5 and 15 characters
    username = StringField("Username", validators=[
        InputRequired(), 
        Length(min=5, max=15, message="Username must be between 5 and 15 characters long.")])
    password = PasswordField("Password", validators=[InputRequired()]) 
    submit = SubmitField("Login")