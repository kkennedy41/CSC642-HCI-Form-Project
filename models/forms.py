from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, SelectField, DateTimeField, SubmitField, validators
from wtforms.validators import *


class DataSurveyForm(FlaskForm):
  """model for each form instance submitted"""

  #----- name -----
  firstName = StringField('First name: ',
                          validators = [ 
                            DataRequired(message='Please enter your first name'),
                            Length(max=20, message='Max. length 20 characters')
                          ])

  lastName = StringField('Last name: ',
                          validators = [
                            DataRequired(message='Please enter your last name'),
                            Length(max=20)
                          ])

  #--- address ----
  streetAddress = StringField('Street address: ',
                              validators = [
                                DataRequired(message='Please enter your street address'),
                                Length(max=40, message='Max. length 40 characters')
                              ])

  city = StringField('City: ',
                      validators = [
                        DataRequired(message='Please enter your city'),
                        Length(max=40, message='Max. length 40 characters')
                      ])

  stateUSA = SelectField('State: ',
                        validators= [
                          DataRequired(message='Please enter your state')
                        ])

  zipcode = StringField('Zip code: ',
                        validators = [
                          DataRequired(message='Please enter your zip code'),
                          Length(min=5,max=5, message='Please enter a valid 5-digit zip code'),
                          NumberRange(min=00000,max=99999, message='Please enter a valid 5-digit zip code')
                        ])

  #----bday ------
  birthday = DateTimeField("Date of birth: ",
                          format='%m/%d/%y',
                          validators = [
                            DataRequired(message='Please enter your date of birth')
                          ])

  #---- height ----
  feet = StringField('feet_label',
                    validators = [ 
                      NumberRange(min=2,max=15, message='Please enter a valid height')
                    ])
  inches = StringField('inches_label',
                      validators = [
                        NumberRange(min=0,max=11, message='Please enter a valid height')
                      ])

  #----edu --------
  edulevel = SelectField('Education level:', validators=[])

  #----contact info----
  phone = StringField('Phone: ', 
                      validators = [
                        DataRequired(message='Please enter a phone number'),
                        Length(min=7, max=7, message='Do not your include area code'),
                        NumberRange(min=0,max=9999999, message='Please enter a valid phone number')
                      ])

  email = StringField('Email: ',
                      validators= [ 
                        DataRequired(message='Please enter a valid email address'),
                        Length(min=6, max=35, message='Please enter a valid email addres (max 35 characters)'),
                        Email('Please enter a valid email address')
                      ])

  confirmEmail = StringField('confirm_email',
                              validators = [
                                DataRequired(message='Please confirm your email address'),
                                EqualTo(email, message='Emails do not match')
                              ])
  
  #---- pre submit checks ----
  iAgree = BooleanField('i_accept',
                        validators = [ 
                          DataRequired(message='Please check the box to agree')
                        ])

  capcha = StringField('capcha_label',
                        validators = [ 
                          DataRequired(message='Please enter the required text'),
                          EqualTo('not bot', message='Please enter the required text')
                        ])

  submit = SubmitField()
