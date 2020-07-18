from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL

app = Flask(__name__)

#-------------database connection --------------------
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
  return render_template('index.html')

#----------------------------------------------------


#------------ verification endpoint -----------------
@app.route('/verification', methods=['GET', 'POST'])
def verification():
  if request.method == 'POST':
    cursor = mysql.connection.cursor()

    firstname = request.form['firstname']
    lastname = request.form['lastname']


  return render_template('verification.html')

#----------------------------------------------------


#--------------- main fxn ---------------------------
if __name__ == "__main__":
  app.run(debug=False)

def main():
  index()
