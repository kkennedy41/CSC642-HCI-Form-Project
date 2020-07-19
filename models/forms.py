from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, validators
from wtforms.validators import DataRequired

class DataSurvey(Form):
  firstname = StringField('First name', [validators.Length(max=20)])
  lastname = StringField('Last name', [validators.Length(max=20)])


  email = StringField('Email address', [validators.Length(min=6, max=35)])
  confirm = StringField()

  iagree = BooleanField('I accept the TOS', [validators.DataRequired()])

  capcha = StringField('', [
    validators.DataRequired(),
    validators.EqualTo('not bot', message='Please enter the required text')
  ])

  submit = SubmitField('Submit')

