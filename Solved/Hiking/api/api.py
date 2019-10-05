
import os


import pandas as pd
import numpy as np

import requests
import json
api_key = "200602075-3dd15f21d86fec1206fac0fe2d9117c8"

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


lat = "40.0274"
lon = "-105.2519"
maxDistance = "1000"
maxResults = "1000"

url = f"https://www.hikingproject.com/data/get-trails?lat={lat}&lon={lon}9&maxDistance={maxDistance}&maxResults={maxResults}&key={api_key}"

database_path = "C:/Users/blake/Desktop/Git Hub Repository/Project/project2/Solved/Hiking/db/hiking.sqlite"
engine = create_engine(f"sqlite:///{database_path}")
conn = engine.connect()

def return_json(apicall):
    try:
        response = requests.get(url)

        response.raise_for_status()
            # Jsonify Responce
        json_obj = response.json()
            # Create Pandas Dataframe
        df = pd.DataFrame(json_obj['trails'])
            # Send Pandas Dataframe to DB
        apicall.df.to_sql(name='hiking', con=engine, if_exists='replace', index=True)

        print(json_obj)
    except requests.exceptions.HTTPError as e:
        # if error keep going
       pass

