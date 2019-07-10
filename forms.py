import flask
from flask_wtf import FlaskForm
from wtforms.fields import BooleanField, PasswordField, SelectField, \
    StringField , SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length,  Regexp,  \
    ValidationError,  url

class CreateCustomer(FlaskForm):
    first_name = StringField('First name: ', validators=[DataRequired()], Length(1, 80))
    last_name = StringField('Last name: ', validators=[DataRequired(), Length(1, 80)])
    email = StringField('Email: ', validators=[Email(), Length(3, 80)])
    address = StringField('Address: ', validators=[DataRequired()], Length(1, 80))
    state = StringField('State: ', validators=[DataRequired(),Length(2, 2)])
    city = StringField('City: ', validators=[DataRequired(),Length(1, 80)])
    zip = StringField('Zip: ', validators=[DataRequired()],Length(5,5)])
