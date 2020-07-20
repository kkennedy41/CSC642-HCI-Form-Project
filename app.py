from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, SelectField, DateField, validators
from wtforms.validators import *
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from models.forms import DataSurveyForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey1'
app.config['GOOGLEMAPS_KEY'] = ''
GoogleMaps(app, key)
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
@app.route('/', methods=['GET', 'POST'])
def index():
  theForm = DataSurveyForm(request.form)  #create object

  if request.method == 'POST' and theForm.validate_on_submit():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    street = request.form['streetaddress']
    city = request.form['city']
    stateUSA = request.form['stateUSA']
    zipcode = request.form['zipcode']
    feet = request.form['feet']
    inches = request.form['inches']
    day = request.form['day']
    month = request.form['month']
    year = request.form['year']
    edu = request.form['education']
    phone = request.form['phone']
    email = request.form['email']


  #do this if 'GET' request
  return render_template('index.html')
#----------------------------------------------------


#------------ verification endpoint -----------------
@app.route('/verification', methods=['GET', 'POST'])
def verification():
  return_data = print()
  return render_template('verification.html', data=return_data)  #left is what html reads and sends to {{formInfo}}, right is what py reads
#---------------------------------------------------


#--------------- main fxn --------------------------
if __name__ == "__main__":
  app.secret_key = 'secretkey1'
  app.goo
  app.run(debug=True)
  #app.run(host='0.0.0.0', port='80', debug=True)
