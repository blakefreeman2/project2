import requests
import json
import pandas as pd
from api_key import api_key
from sqlalchemy import create_engine

lat = "40.0274"
lon = "-105.2519"
maxDistance = "1000"
maxResults = "1000"

url = f"https://www.hikingproject.com/data/get-trails?lat={lat}&lon={lon}9&maxDistance={maxDistance}&maxResults={maxResults}&key={api_key}"


response = requests.get(url)
response_json = response.json()


# print(url)
# print(json.dumps(response_json, indent=4,))

df=pd.DataFrame(response_json['trails'])
df


database_path = "C:/Users/blake/Desktop/Git Hub Repository/Project/Solved/Hiking/db/hiking.sqlite"
engine = create_engine(f"sqlite:///{database_path}")
conn = engine.connect()

df.to_sql(name='hiking', con=engine, if_exists='append', index=True)