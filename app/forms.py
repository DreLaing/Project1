from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField
from wtforms import TextAreaField
from wtforms import StringField
from wtforms import SelectField
from flask_wtf.file import FileField, FileAllowed, FileRequired

class myForm(FlaskForm):
    fname = StringField('Firstname', validators=[DataRequired()])
    lname = StringField('Lastname', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('Male', 'male'), ('Female', 'female')], validators=[DataRequired()])
    bio = TextAreaField('Biography')
    image = FileField('Image', validators=[FileAllowed(['jpg', 'png'], 'Images Only'), FileRequired("Please provide a picture")])