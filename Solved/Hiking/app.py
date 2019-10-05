# import necessary libraries
import os

import pandas as pd
import numpy as np

import requests
import json
# from .api_key import api_key
from sqlalchemy import create_engine

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)


app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db/hiking.sqlite"
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '')

db = SQLAlchemy(app)

from .models import hiking

# lat = "40.0274"
# lon = "-105.2519"
# maxDistance = "1000"
# maxResults = "1000"

# url = f"https://www.hikingproject.com/data/get-trails?lat={lat}&lon={lon}9&maxDistance={maxDistance}&maxResults={maxResults}&key={api_key}"


# create route that renders index.html template
@app.route("/")
def home():

    return render_template("index.html")

@app.route("/api/hiking")
def pals():
    results = db.session.query(hiking.id, 
    hiking.name, 
    hiking.type, 
    hiking.summary, 
    hiking.difficulty, 
    hiking.stars, 
    hiking.starVotes, 
    hiking.location, 
    hiking.url, 
    hiking.imgSqSmall,
    hiking.imgSmall,
    hiking.imgSmallMed,
    hiking.imgMedium,
    hiking.length,
    hiking.ascent,
    hiking.descent,
    hiking.high,
    hiking.low,
    hiking.longitude,
    hiking.latitude, 
    hiking.conditionStatus,
    hiking.conditionDetails, 
    hiking.conditionDate).all()

    id = [result[0] for result in results]
    name  = [result[1] for result in results]
    type  = [result[2] for result in results]
    summary  = [result[3] for result in results]
    difficulty  = [result[4] for result in results]
    stars  = [result[5] for result in results]
    starVotes  = [result[6] for result in results]
    location  = [result[7] for result in results]
    url = [result[8] for result in results] 
    imgSqSmall = [result[9] for result in results]
    imgSmall = [result[10] for result in results]
    imgSmallMed = [result[11] for result in results]
    imgMedium = [result[12] for result in results]
    length = [result[13] for result in results]
    ascent = [result[14] for result in results]
    descent = [result[15] for result in results]
    high = [result[16] for result in results]
    low = [result[17] for result in results]
    longitude = [result[18] for result in results]
    latitude  = [result[19] for result in results]
    conditionStatus = [result[20] for result in results]
    conditionDetails  = [result[21] for result in results]
    conditionDate = [result[22] for result in results]

    hiking_data = [{
        "id": id,
        "name": name,
        "type": type,
        "summary": summary,
        "difficulty": difficulty,
        "stars": stars,
        "starVotes": starVotes,
        "location": location,
        "url": url,
        "imgSqSmall": imgSqSmall,
        "imgSmall":imgSmall,
        "imgSmallMed": imgSmallMed,
        "imgMedium": imgMedium,
        "length": length,
        "ascent": ascent,
        "descent": descent,
        "high": high,
        "low": low,
        "longitude": longitude,
        "latitude": latitude,
        "conditionStatus": conditionStatus,
        "conditionDetails": conditionDetails,
        "conditionDate": conditionDate
    }]

    return jsonify(hiking_data)

# @app.route("/data")
# def return_json(database):
#     try:
#         response = requests.get(url)

#         response.raise_for_status()
#             # Jsonify Responce
#         json_obj = response.json()
#             # Create Pandas Dataframe
#         df = pd.DataFrame(json_obj['trails'])
#             # Send Pandas Dataframe to DB
#         df.to_sql(name='hiking', con=engine, if_exists='replace', index=True)

#         print('it worked?')
#     except requests.exceptions.HTTPError as e:
#         # if error keep going
#        pass
    
if __name__ == "__main__":
    app.run()
