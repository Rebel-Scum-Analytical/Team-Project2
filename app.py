# Dependencies
import os
import sqlalchemy
from flask import Flask, render_template, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

#################################################
# Set up the database
#################################################
HOSTNAME = "127.0.0.1"
PORT = 3306
USERNAME = "root"
PASSWORD = "password"
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
# print(table_names)

Base = automap_base()
Base.prepare(engine, reflect=True)

# create classes by mapping with names which match the table names
User_account = Base.classes.user_account
Meal_record = Base.classes.meal_record

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
# Route #2(/api/register)
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

            session.add(new_user)
            session.commit()
            return render_template("register.html")


        
#############################################################################################
# Route #3(/api/login)
# Design a query for the existing user to login
#############################################################################################

def loginsys(username, password):
    user_ls = session.query(User_account.first_name, User_account.last_name, User_account.gender)\
                        .filter(User_account.username == username)\
                        .filter(User_account.password == password)\
                        .first()                            
    return user_ls

@app.route("/login", methods=["GET"])
def login():

    request_username = request.args['username']
    request_password = request.args['password']

    try:
        if request_username and request_password:
            return jsonify(loginsys(request_username, request_password))
            # return render_template("Login.html")   

    except Exception as e:
        return jsonify({"Status":"Failure!", "Error": str(e)})


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
