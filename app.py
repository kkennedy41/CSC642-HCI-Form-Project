from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, SelectField, DateField, validators
from wtforms.validators import *
from models.forms import DataSurveyForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey1'

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

  theForm = DataSurveyForm('mainform')  #create object of form class with form name in index.html


    #theForm.firstName = firstName

    
    #else: #do this if error in form
      #return "~ERROR~ not a valid form"

  #do this if 'GET' request
  return render_template('index.html')
#----------------------------------------------------


#------------ verification endpoint -----------------
@app.route('/verification', methods=['GET', 'POST'])
def verification():
  if request.method == 'POST':  #when new form button is clicked
    
    

  return render_template('verification.html', data=data) #left is what html reads {{formInfo}} right is what py reads
#---------------------------------------------------


#--------------- main fxn --------------------------
if __name__ == "__main__":
  app.secret_key = 'secretkey1'
  app.run(debug=True)
  #app.run(host='3.128.214.205', port='80', debug=True)
