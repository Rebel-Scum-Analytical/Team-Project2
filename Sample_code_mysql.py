import os
from flask import Flask, render_template, jsonify, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
import pandas as pd

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# The database URI
#################################################



#app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/nutrometer.sql"

#######################SAMPLE CODE TO ACCESS DB###########################  
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:uv9y9g5t@127.0.0.1:3306/sakila"
#CONECTION STRING mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname> #########
#######################SAMPLE CODE TO ACCESS DB###########################  

db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

Actor = Base.classes.actor

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

#######################SAMPLE CODE TO ACCESS DB###########################  

@app.route("/actor")
def samples():
   
    stmt = db.session.query(Actor).statement
    df = pd.read_sql_query(stmt, db.session.bind)    
    data = {
        "first_name": df.first_name.tolist()}  
    return jsonify(data)
#######################SAMPLE CODE TO ACCESS DB###########################  


if __name__ == "__main__":
    app.run(debug=True)
