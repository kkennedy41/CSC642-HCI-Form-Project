from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, SelectField, DateTimeField, SubmitField, validators
from wtforms.validators import *


class DataSurveyForm(FlaskForm):

  #----- name -----
  firstName = StringField('first_name', validators=[DataRequired(message='Please enter your first name'), Length(max=20)])
  lastName = StringField('last_name', validators=[DataRequired(message='Please enter your last name'), Length(max=20)])

  #--- address ----
  streetAddress = StringField('street_address', validators=[DataRequired(), Length(max=40)])
  city = StringField('city_label', validators=[DataRequired(message='Please enter your city'), Length(max=40)])
  state = SelectField(validators=[DataRequired(message='Please enter your state')])
  zipcode = StringField('zip', validators=[DataRequired(message='Please enter your zip code'), Length(min=5,max=5), NumberRange(min=0,max=99999)]) #positive value

  #----bday ------
  birthday = DateTimeField("birthday", format='%m/%d/%y', validators=[DataRequired(message='Please enter your date of birth')])

  #---- height ----
  feet = StringField('feet_label', validators=[NumberRange(min=2,max=15)]) #positive value
  inches = StringField('inches_label', validators=[NumberRange(min=0,max=11)]) #positive value

  #----edu --------
  edulevel = SelectField(validators=[])

  #----contact info----
  phone = StringField('phone_label',
                      validators=[
                        DataRequired(message='Please enter a phone number'),
                        Length(min=7, max=7),
                        NumberRange(min=0,max=9999999)
                      ])

  email = StringField('email_address', validators=[DataRequired(message='Please enter a valid email address'), Length(min=6, max=35)]) #must have @ and .
  confirmEmail = StringField('confirm_email', validators=[DataRequired(message='Please confirm your email address'), EqualTo(email, message='Emails do not match')])

  iAgree = BooleanField('i_accept', validators=[DataRequired(message='Please check the box to agree')])

  capcha = StringField('capcha_label', validators=[DataRequired(message='Please enter the required text'), EqualTo('not bot', message='Please enter the required text')])

  submit = SubmitField()

