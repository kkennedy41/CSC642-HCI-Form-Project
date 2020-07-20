from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, SelectField, DateTimeField, SubmitField, validators
from wtforms.validators import *


class DataSurveyForm(FlaskForm):
  #----- name -----
  firstname = StringField('first_name', validators=[DataRequired(), Length(max=20)])
  lastname = StringField('last_name', validators=[DataRequired(), Length(max=20)])

  #--- address ----
  streetaddress = StringField('street_address', validators=[DataRequired(), Length(max=40)])
  city = StringField('city_label')
  state = SelectField()

  #----bday ------
  birthday  = DateTimeField('Your Birthday', format='%m/%d/%y')

  #---- height ----
  feet = StringField('feet_label')
  inches = StringField('inches_label')

  #----contact info----
  phone = StringField('phone_label', validators=[DataRequired(), Length(min=7, max=7)])

  email = StringField('email_address', validators=[DataRequired(), Length(min=6, max=35)])
  confirmEmail = StringField('confirm_email', validators=[DataRequired(), EqualTo(email, message='Emails do not match')])

  iagree = BooleanField('i_accept', [validators.DataRequired()])

  capcha = StringField('capcha_label', [
    validators.DataRequired(),
    validators.EqualTo('not bot', message='Please enter the required text')
  ])

  submit = SubmitField()

