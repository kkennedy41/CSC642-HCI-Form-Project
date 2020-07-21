from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import Form, BooleanField, StringField, PasswordField, SelectField, DateField, validators
from wtforms.validators import *
from flask_googlemaps import GoogleMaps, Map
from models.forms import DataSurveyForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey1'
#app.config['GOOGLEMAPS_KEY'] = ''  #get from google api website
#GoogleMaps(app, key)
Bootstrap(app)

#------------ database connection -------------------
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'FormDB'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL()
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()
#----------------------------------------------------


#------------ index page ----------------------------
@app.route('/', methods=['GET','POST'])
def index():
  return render_template('index.html')   #do this if 'GET' request
#----------------------------------------------------


#------------ verification endpoint --------
@app.route('/verification', methods=['GET', 'POST'])
def verification():
  form = request.form
  theForm = DataSurveyForm(form)

  if request.method == 'POST':
    theForm.firstname = form['firstname']
    theForm.lastname = form['lastname']
    theForm.phone = form['phone']
    theForm.birthday = form.get('bday')
    theForm.email = form['email']
    #theForm.confirm_email = form.get('confirm_email')
    #theForm.streetAddress = form['streetaddress']
    #theForm.inches = form['inches']
    #theForm.feet = form['feet']
    #theForm.capcha = form['capcha']
    #theForm.iAgree = form.get('i_agree')

  #if theForm.validate():
    #return render_template('verification.html', data=print(theForm))

  return render_template('verification.html', data=print("THERE ARE FORM ERRORS"))
#---------------------------------------------------


#--------------- main fxn --------------------------
if __name__ == "__main__":
  app.secret_key = 'secretkey1'
  app.run(debug=True)
  #app.run(host='0.0.0.0', port='80', debug=True)
