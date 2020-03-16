import os
from flask import Flask, render_template, jsonify, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# The database URI
#################################################

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/nutrometer.sql"

db = SQLAlchemy(app)


# # Create our database model
# class UserLogin(db.Model):
#     __tablename__ = 'user_account'

#     first_name = db.Column(db.String)
#     last_name = db.Column(db.String)
#     # email_id = db.Column(db.String)
#     # mobile_no = db.Column(db.Integer)

#     def __repr__(self):
#         return '<User %r>' % (self.name)


# # Create database tables
# @app.before_first_request
# def setup():
#     # Recreate database each time for demo
#     # db.drop_all()
#     db.create_all()

#############################################################################################
# Route #1("/")
# Home Page
#############################################################################################

@app.route("/")
def home():
    return render_template("index.html")


#############################################################################################
# Route #2(/api/v1.0/user_login)
# Design a query for the existing user to login
#############################################################################################

# Query the database and send the jsonified results for user login
@app.route("/send", methods=["POST"])
def send():
    if request.method == "POST":
        firstname = request.form["userFirstname"]
        lastname = request.form["userLastname"]
        email = request.form["useremail"]
        mobile = request.form["usermobilenumber"]

        user = Users(first_name=firstname, last_name=lastname, email_id=email, mobile_no=mobile)
        db.session.add(user)
        db.session.commit()
        print(user)
        return redirect("/", code=302)

    return render_template("form.html")
#############################################################################################
# Route #3(/api/v1.0/create_user)
# Design a query create a new user
#############################################################################################

#############################################################################################
# Route #4(/api/v1.0/user_metrics)
# Design a query That displays specific nutrients for the food consumed by the user. 
#############################################################################################

#############################################################################################
# Route #5(/api/v1.0/food_list)
# Design a query That displays food with specific nutrients. 
# Basically ask the user, what nutrient are you looking for and
# have it return a list of foods that are high in that nutrient.
#############################################################################################

if __name__ == "__main__":
    app.run(debug=True)
