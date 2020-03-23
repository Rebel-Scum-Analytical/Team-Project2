import os
import sqlalchemy
from flask import Flask, render_template, jsonify, request, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from forms import RegistrationForm, LoginForm

# Setup the Database
HOSTNAME = "127.0.0.1"
PORT = 3306
USERNAME = "root"
PASSWORD = "PASSWORD"
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

all_users = session.query(User_account.account_number,
                        User_account.username,\
                        User_account.first_name, \
                        User_account.last_name, \
                        User_account.gender,\
                        User_account.date_of_birth,\
                        User_account.height,\
                        User_account.weight,\
                        User_account.physical_activity_level)\
                        .all()
# print(all_users)

app = Flask(__name__)

@app.route("/all_users")
def show_all():
    return jsonify(all_users)


def loginsys(username, password):
    user_ls = session.query(User_account.first_name, User_account.last_name, User_account.gender)\
                        .filter(User_account.username == username)\
                        .filter(User_account.password == password)\
                        .all()                            
    return user_ls

@app.route("/login")
def login():

    request_username = request.args['username']
    request_password = request.args['password']

    return jsonify(loginsys(request_username, request_password))
    # return render_template(".html")

 # @app.route("/login")
# def login():
#     form =LoginForm()
#     return render_template("login.html", title="Login", form=form)   


app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    form =RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', "success")
        return redirect(url_for('home'))
    return render_template("register.html", title="Register", form=form)


if __name__ == "__main__":
    app.run(debug=True)