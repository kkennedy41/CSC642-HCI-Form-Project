from wtforms import Form, BooleanField, StringField, validators

class RegistrationForm(Form):
  firstname = StringField('First name', [validators.Length(min=4, max=25)])
  lastname = StringField('Last name', [validators.Length(min=4, max=25)])


  email = StringField('Email address', [validators.Length(min=6, max=35)])
  confirm = StringField()

  iagree = BooleanField('I accept the TOS', [validators.DataRequired()])

  capcha = StringField('', [
    validators.DataRequired(),
    validators.EqualTo('not bot', message='Please enter the required text')
  ])

