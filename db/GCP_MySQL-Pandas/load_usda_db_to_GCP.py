#################################################
# Dependencies
#################################################

import pandas as pd
import os
from flask import Flask, render_template, jsonify, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from sqlalchemy.exc import ProgrammingError
import warnings

#################################################
# Set up the USDA database
#################################################
HOSTNAME = "127.0.0.1"
PORT = 3306
USERNAME = "root"
PASSWORD = "PASSWORD"  ## Enter MySQL password here
DIALECT = "mysql"
DRIVER = "pymysql"
DATABASE = "sr28"
TABLENAME = "nutrition"

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

# create classes by mapping with names which match the table names
Nutrition = Base.classes.abbrev

session = Session(bind=engine)

nutrition_info = session.query(
    Nutrition.Shrt_Desc,
    Nutrition.Water_g,
    Nutrition.Energ_Kcal,
    Nutrition.Protein_g,
    Nutrition.Lipid_Tot_g,
    Nutrition.Carbohydrt_g,
    Nutrition.Fiber_TD_g,
    Nutrition.Sugar_Tot_g,
    Nutrition.Calcium_mg,
    Nutrition.Iron_mg,
    Nutrition.Magnesium_mg,
    Nutrition.Phosphorus_mg,
    Nutrition.Potassium_mg,
    Nutrition.Sodium_g,
    Nutrition.Zinc_mg,
    Nutrition.Copper_mg,
    Nutrition.Manganese_mg,
    Nutrition.Selenium_mcg,
    Nutrition.Folic_Acid_mcg,
    Nutrition.Vit_C_mg,
    Nutrition.Vit_B12_mcg,
    Nutrition.Vit_B6_mg,
    Nutrition.Vit_D_mcg,
    Nutrition.Vit_K_mcg,
    Nutrition.Vit_A_IU,
    Nutrition.Vit_E_mg,
    Nutrition.Thiamin_mg,
    Nutrition.Riboflavin_mg,
    Nutrition.Niacin_mg,
    Nutrition.Panto_Acid_mg,
    Nutrition.Cholestrl_g,
    Nutrition.GmWt_1,
    Nutrition.GmWt_Desc1,
).all()
# print(type(nutrition_info))
df = pd.DataFrame(
    nutrition_info,
    columns=[
        "Food Desc",
        "Water",
        "Energy",
        "Protein",
        "Lipid_Total",
        "Carbohydrate",
        "Fiber",
        "Sugar",
        "Calcium",
        "Iron",
        "Magnesium",
        "Phosphorus",
        "Potassium",
        "Sodium",
        "Zinc",
        "Copper",
        "Manganese",
        "Selenium",
        "Folic_Acid",
        "Vitamin_C",
        "Vitamin_B12",
        "Vitamin_B6",
        "Vitamin_D",
        "Vitamin_K",
        "Vitamin_A",
        "Vitamin_E",
        "Thiamin",
        "Riboflavin",
        "Niacin",
        "Pantothenic_Acid_VB5",
        "Cholestrol",
        "Weight_grams",
        "Weight_desc",
    ],
)
# print(df)

# Convert the df to csv file
df.to_csv("file1.csv")
