import os
import sys
import pandas as pd
import pymysql
import dotenv
from dotenv import load_dotenv
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pickle
import numpy as np

# Load environment variables
load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")  # Ensure this is present in the .env file

# Check if environment variables are set
if not all([host, user, password, db]):
    raise ValueError("One or more required environment variables are missing!")

def read_sql_data():
    logging.info("Reading SQL database started")
    
    try:
        # Establish database connection
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=db  # Corrected parameter name
        )
        logging.info("Connection Established Successfully",mydb)

        # Read data into a DataFrame
        df = pd.read_sql('SELECT * FROM Student', con=mydb)  # Fixed `read_sql` method usage
        logging.info(f"Data fetched successfully. Rows: {len(df)}")

        print(df.head())

        # Close connection
        mydb.close()
        
        return df
        
    except Exception as ex:
        logging.error(f"Error while reading SQL data: {str(ex)}")
        raise CustomException(ex, sys)  # Passing `sys` for proper traceback

