import requests
from bs4 import BeautifulSoup
import os
import urllib
import json
import pandas as pd
from sqlalchemy import create_engine, text
import re
from fastapi import FastAPI, HTTPException
import uvicorn
import nest_asyncio

#define the credentials
user = 'root'
password = 'DataengineerJAM0112'
host = '127.0.0.1'
port = 3306
database = 'kjcs_etl_database'

# Create SQLAlchemy engine
engine = create_engine(
    f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}',
    future=True
)

#API server

# Create FastAPI app
app = FastAPI()

@app.get("/cars_data")
def get_cars(limit: int = 10):
    """
    Fetch limited rows from MySQL table 'kjcs_project_7_tab'
    Example: /cars?limit=5
    """
    #query 
    query = text(f'SELECT * FROM kjcs_project_7_tab LIMIT {limit}')
    #connect to database and pull out data
    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        #convert Row objects → dict
    return df.to_dict(orient='records')