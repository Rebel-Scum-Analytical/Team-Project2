# Dependencies
import os
import sqlalchemy
from flask import Flask, render_template, jsonify, request, make_response, session, abort, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
import pymysql

from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextField, PasswordField, SelectField, DateField, DecimalField, SubmitField
from wtforms.validators import InputRequired, Length, NumberRange, EqualTo
from passlib.hash import sha256_crypt


#################################################
# Flask Setup
#################################################

app = Flask(__name__)

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = '1a2b3c4d5e'

# Enter your database connection details below
# app.config['MYSQL_HOST'] = '127.0.0.1'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'password'
# app.config['MYSQL_DB'] = 'usda'

# Intialize MySQL
# mysql = MySQL(app)

#################################################
# Set up the database
#################################################
HOSTNAME = "127.0.0.1"
PORT = 3306
USERNAME = "root"
PASSWORD = "@200Piedmont"
DIALECT = "mysql"
DRIVER = "pymysql"
DATABASE = "nutrometer"

# Connect to DB in DB Server
db_connection_string = (
    f"{DIALECT}+{DRIVER}://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}"
)

engine = create_engine(db_connection_string)
inspector = inspect(engine)
table_names = inspector.get_table_names()
# print("Table names are: ", table_names)

Base = automap_base()
Base.prepare(engine, reflect=True)
# print(Base.classes.values)

# create classes by mapping with names which match the table names
User_account = Base.classes.user_account
Meal_record = Base.classes.meal_record
# Nutrition = Base.classes.nutrition


session_db = Session(bind=engine)
# print("session_db is: ", session_db)


#############################################################################################
# Route #1("/")
# Home Page
#############################################################################################
@app.route("/index.html")
@app.route("/")
def main():
    session['page']=' '
    if(checkLoggedIn() == True):
        session['page']='dashboard'
        return redirect('/dashboard')

    session['page']=' '
    return render_template("index.html")
#############################################################################################
# Route #2(/login)
# Design a query for the existing user to login
#############################################################################################
    
@app.route('/login', methods=['GET', 'POST'])
def login():
# Output message if something goes wrong...
    msg = ''
    print("Start of stuff")
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST': #and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        request_username = request.form['username']
        request_password = request.form['password']
        # Check if account exists using MySQL
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # cursor.execute('SELECT * FROM user_accounts WHERE username = %s AND password = %s', (username, password))
        if request_username and request_password:   
        # Fetch one record and return result
            print("request_username: "+request_username+" | request_password: "+request_password)
            account = loginsys(request_username, request_password)
                # If account exists in accounts table in out database
            if account:
            # Create session data, we can access this data in other routes
                session['loggedin'] = True
                session['username'] = account[3]
            # Redirect to home page
                session['page']='dashboard'
                return redirect('/dashboard')
            else:
            # Account doesnt exist or username/password incorrect
                msg = 'Incorrect username/password!'
    session['page']=' '
    return render_template('index.html', msg=msg)
    
def loginsys(username, password):
    print("Username: "+username+" Password: "+password)
    user_ls = session_db.query(User_account.first_name, User_account.last_name, User_account.gender, User_account.username)\
                        .filter(User_account.username == username)\
                        .filter(User_account.password == password)\
                        .first()           
    print("user_ls: " + str(user_ls))                 
    return user_ls


##############################################################################################
# Route #3(/register)
# Design a query for the register a new user
#############################################################################################

class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=20)])
    password = PasswordField('password', validators=[InputRequired()])
    confirm_password = PasswordField('confirm_password', validators=[InputRequired(), EqualTo('password')])
    first_name = StringField('first_name', validators=[InputRequired(),Length(min=2, max=50)])
    last_name = StringField('last_name', validators=[InputRequired(),Length(min=2, max=50)])
    gender = SelectField(u'gender', choices=[('male', 'Male'), ('female', 'Female')])
    date_of_birth = DateField('date_of_birth', format='%Y-%m-%d')
    height = DecimalField('height', places=2, rounding=None, validators=[InputRequired(), NumberRange(min=0, max=500, message='Blah')])
    weight = DecimalField('weight', places=2, rounding=None, validators=[InputRequired(), NumberRange(min=0, max=2000, message='Blah')])
    physical_activity_level = SelectField(u'physical_activity_level', choices=[('sedentary', 'Sedentary'), ('lightly active', 'Lightly Active'), ('moderately active', 'Moderately Active'), ('very active', 'Very Active'), ('extra active', 'Extra Active')])  
    submit = SubmitField('Get Started')

@app.route("/register", methods=["GET", "POST"])
def register():

        form = RegistrationForm(request.form)
        if form.validate_on_submit():
            flash(f'Account created for {form.username.data}!', 'success')

            new_user = User_account(username = form.username.data,\
                                    password = form.password.data,\
                                    confirm_password = form.confirm_password.data,\
                                    first_name = form.first_name.data,\
                                    last_name = form.last_name.data,\
                                    gender =  form.gender.data,\
                                    date_of_birth = form.date_of_birth.data,\
                                    height = form.height.data,\
                                    weight = form.weight.data,\
                                    physical_activity_level = form.physical_activity_level.data
                                    )
            session_db.add(new_user)
            session_db.commit()

            return redirect('/dashboard')
        return render_template("New_user.html", form=form)


##############################################################################################
# Route #4(/home)
# This will be the home page, only accessible for loggedin users
#############################################################################################


@app.route('/dashboard')
def dashboard():
    if(checkLoggedIn() == False):
        return redirect('/login')

    session['page']='dashboard'
    return render_template("dashboard.html")

@app.route('/analysis')
def analysis():
    if(checkLoggedIn() == False):
        return redirect('/login')
    session['page']='analysis'
    return render_template("Daily_vizualization.html")

def checkLoggedIn():
    if 'loggedin' in session:
        if session['loggedin'] == True:
            return True
    return False 

@app.route('/nutrition')
def nutrition():
    if(checkLoggedIn() == False):
        return redirect('/login')
    session['page']='nutrition'
    return render_template("nutrition.html")

# @app.route('/register')
# def register():
#     session['page']='register'
#     return render_template("New_user.html")

@app.route('/intake')
def intake():
    if(checkLoggedIn() == False):
        return redirect('/login')
    session['page']='intake'
    return render_template("intake.html")

@app.route('/logout')
def logout():
    if(checkLoggedIn() == False):
        session['page']=' '
        return render_template('login.html', msg="Already logged out!")
    else:
        session['loggedin'] = False
        messages = "loggedout"
        session['messages'] = messages
        session['page']=' '
        return redirect("/")  

if __name__ == "__main__":
    app.run(debug=True)
    #app.run() 