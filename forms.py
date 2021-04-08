from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Length, DataRequired, Email

class RegistrationForm(FlaskForm):
    # username must be between 5 and 15 characters
    username =StringField('Username', validators=[DataRequired(), Length(min=5, max=15)])
    
