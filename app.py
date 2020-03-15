import os
import pandas as pd
from flask import Flask, render_template, jsonify, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# The database URI
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/db_nutrometer.sql"

db = SQLAlchemy(app)


# Create our database model
class UserLogin(db.Model):
    __tablename__ = 'user_account'

    account_number = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email_id = db.Column(db.String)
    mobile_no = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % (self.name)


# Create database tables
@app.before_first_request
def setup():
    # Recreate database each time for demo
    # db.drop_all()
    db.create_all()



@app.route("/")
def home():
    return render_template("index.html")



 # Query the database and send the jsonified results for user login
@app.route("/send", methods=["POST"])
def send():
    if request.method == "POST":
        firstname = request.form["userFirstname"]
        lastname = request.form["userLastname"]
        email = request.form["useremail"]
        mobile = request.form["usermobilenumber"]

        pet = Pet(name=name, lat=lat, lon=lon)
        db.session.add(user)
        db.session.commit()
        print(user)
        return redirect("/", code=302)

    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
