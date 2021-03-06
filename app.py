from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, SelectField, DateField, validators
from wtforms.validators import *

app = Flask(__name__)

#------------ database connection -------------------
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DATABASE_DB'] = 'FormDB'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# mysql = MySQL()
# mysql.init_app(app)
# conn = mysql.connect()
# cursor = conn.cursor()
#----------------------------------------------------


#------------ index page ----------------------------
@app.route('/')
def index():
  return render_template('index.html')   #do this if 'GET' request
#----------------------------------------------------


#------------ verification endpoint --------
@app.route('/verification', methods=['GET', 'POST'])
def verification():
  if request.method == 'POST':
    form = request.form
    #args = request.args

    firstname = form['firstname']
    lastname = form['lastname']
    phone = form['phone']
    email = form['email']
    streetaddress = form['streetaddress']
    city = form['city']
    inches = form['inches']
    feet = form['feet']

    #for dropdown menu data
    # stateUSA = args.get('stateUSA')
    # month = args.get('month')
    # day = args.get('day')
    # year = args.get('year')

    # cursor.execute("INSERT INTO Data_Survey (firstname, lastname) VALUES (%s, %s)", (firstname, lastname))
    # conn.commit()
    # cursor.execute("SELECT firstname,lastname FROM Data_Survey ORDER BY form_id DESC LIMIT 1;")  #then get it back 
    # conn.commit()
    # data = cursor.fetchall()
    return render_template('verification.html', form=form)

  return render_template('verification.html')
#---------------------------------------------------


#--------------- main fxn --------------------------
if __name__ == "__main__":
  app.run()
