#################################################
# Dependencies
#################################################

import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
import warnings

#################################################
# Set up the database
#################################################

USER = "root"
PASSWORD = "PASSWORD"  # Enter you SQL password here
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "usda_db"
TABLENAME = "nutrition"

# Create the database usig csv file
df = pd.read_csv("file1.csv")
# print(df.head())

engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}")

try:
    engine.execute(f"CREATE DATABASE {DATABASE}")
except ProgrammingError:
    warnings.warn(
        f"Could not create database {DATABASE}. Database {DATABASE} may already exist."
    )
    pass

engine.execute(f"USE {DATABASE}")
engine.execute(f"DROP TABLE IF EXISTS {TABLENAME}")
df.to_sql(name=TABLENAME, con=engine)
