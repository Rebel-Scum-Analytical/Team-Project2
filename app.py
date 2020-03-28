# Dependencies
import os
import sqlalchemy
from flask import Flask, render_template, jsonify, request, make_response, session, abort, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
import pymysql
# from flask_mysqldb import MySQL
# import MySQLdb.cursors
# import re

#################################################
# Set up the database
#################################################
HOSTNAME = "127.0.0.1"
PORT = 3306
USERNAME = "root"
PASSWORD = "password" # Enter you password here
DIALECT = "mysql"
DRIVER = "pymysql"
DATABASE = "usda"

# Connect to DB in DB Server
db_connection_string = (
    f"{DIALECT}+{DRIVER}://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}"
)

engine = create_engine(db_connection_string)
inspector = inspect(engine)
table_names = inspector.get_table_names()
print("Table names are: ", table_names)

Base = automap_base()
Base.prepare(engine, reflect=True)
print(Base.classes.values)

# create classes by mapping with names which match the table names
User_account = Base.classes.user_account
Meal_record = Base.classes.meal_record
Nutrition = Base.classes.nutrition


session = Session(bind=engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#############################################################################################
# Route #1("/")
# Home Page
#############################################################################################
@app.route("/")
def home():
    return render_template("index.html")

#############################################################################################
# Route #3(/login)
# Design a query for the existing user to login
#############################################################################################
#@app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != 'admin' or request.form['password'] != 'admin':
#             error = 'Invalid Credentials. Please try again.'
#         else:
#             return redirect(url_for('home'))
#     # return render_template('login.html', error=error)




@app.route("/login", methods=["GET", "POST"])


def login():
    # Output message if something goes wrong...
    msg=''
    print("Start of stuff")
    print("request.method: "+request.method)
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST': #and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        request_username = request.form['username']
        request_password = request.form['password']
        print("request_username: "+request_username+" | request_password: "+request_password)
        # Check if account exists using MySQL
        if request_username and request_password:   
            # Fetch one record and return result
            print("request_username: "+request_username+" | request_password: "+request_password)
            account = loginsys(request_username, request_password)
            if account:
                # return 'Logged in successfully!'
                return redirect('/meal')
                # return render_template('user_metrics.html', username=account.username, first_name=account.first_name, last_name=account.last_name)
            else:
            # Account doesnt exist or username/password incorrect
                msg = 'Incorrect username/password!'    
        # Show the login form with message (if any)
    return render_template('Login.html', msg=msg)


def loginsys(username, password):
    print("Username: "+username+" Password: "+password)
    user_ls = session.query(User_account.first_name, User_account.last_name, User_account.gender, User_account.username)\
                        .filter(User_account.username == username)\
                        .filter(User_account.password == password)\
                        .first()           
    print("user_ls: " + str(user_ls))                 
    return user_ls
    
#     try:
#             if request_username and request_password:
#                 account = loginsys(request_username, request_password)
#                 return jsonify(loginsys(request_username, request_password))
#             # return render_template("Login.html")   

#         except Exception as e:
#             return jsonify({"Status":"Failure!", "Error": str(e)})
        
#         # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         # cursor.execute('SELECT * FROM user_account WHERE username = %s AND password = %s', (username, password))
#         # Fetch one record and return result
#         # account = cursor.fetchone()
#     elif request.method == 'GET':  
#         def login():

#             request_username = request.args['username']
#             request_password = request.args['password']

#             try:
#                 if request_username and request_password:
#                     return jsonify(loginsys(request_username, request_password))
#             # return render_template("Login.html")   

#             except Exception as e:
#                 return jsonify({"Status":"Failure!", "Error": str(e)})    
#     return render_template("form.html")            
# #############################################################################################
# Route #2(/register)
# Design a query for the register a new user
#############################################################################################

@app.route("/register", methods=["GET"])
def register():
    requested_username = request.args['username']
    requested_password = request.args['password']
    requested_first_name = request.args['first_name']
    requested_last_name = request.args['last_name']
    requested_gender = request.args['gender']
    requested_dob = request.args['date_of_birth']
    requested_height = request.args['height']
    requested_weight = request.args['weight']
    # requested_pal = request.args('physical_activity_level')

    if requested_username:
        existing_user = session.query(User_account.username == requested_username).first()
        if existing_user:
            return  make_response(f'{requested_username} already existed!')
        if existing_user is None:
            new_user = User_account(username = requested_username,\
                                    password = requested_password,\
                                    first_name = requested_first_name,\
                                    last_name = requested_last_name,\
                                    gender =  requested_gender,\
                                    date_of_birth = requested_dob,\
                                    height = requested_height,\
                                    weight = requested_weight
                                    # physical_activity_level = requested_pal
                                    )
        else:
            pass
            session.add(new_user)
            session.commit()
    return render_template("New_user.html")


#############################################################################################
# Route #3(/login)
# Design a query for the existing user to login
#############################################################################################

# def loginsys(username, password):
#     user_ls = session.query(User_account.first_name, User_account.last_name, User_account.gender)\
#                         .filter(User_account.username == username)\
#                         .filter(User_account.password == password)\
#                         .first()                            
#     return user_ls

# @app.route("/login", methods=["GET"])
# def login():

#     request_username = request.args['username']
#     request_password = request.args['password']

#     try:
#         if request_username and request_password:
#             return jsonify(loginsys(request_username, request_password))
#             # return render_template("Login.html")   

#     except Exception as e:
#         return jsonify({"Status":"Failure!", "Error": str(e)})


#############################################################################################
# Route #4(/meal)
# Design a query that displays specific nutrients for the food consumed by the user. 
#############################################################################################

@app.route("/meal", methods=["GET"])
def meal():
    requested_meal_date = request.args['meal_date']
    requested_meal_time = request.args['meal_time']
    # requested_meal_item = request.args['meal_item']
    # requested_amount = request.args['amount']
    # requested_measure_unit = request.args['measure_unit']
    
    new_meal = Meal_record(meal_date = requested_meal_date,\
                        meal_time = requested_meal_time
                        # meal_item = requested_meal_item,\
                        # amount = requested_amount,\
                        # measure_unit = requested_measure_unit
                        # magnesium = amount * measure_unit
                        )

    session.add(new_meal)
    session.commit()

    return render_template("user_metrics.html")
#############################################################################################
# Route #5(/food_list)
# Design a query That displays food with specific nutrients. 
# Basically ask the user, what nutrient are you looking for and
# have it return a list of foods that are high in that nutrient.
#############################################################################################

if __name__ == "__main__":
    app.run(debug=True)
