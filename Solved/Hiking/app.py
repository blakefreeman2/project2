# import necessary libraries
import os

import pandas as pd
import numpy as np

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


# create route that renders index.html template
@app.route("/")
def home():

    return render_template("index.html")


def api_request():
    return {
        'url': request.host_url.rstrip('/') + url_for('notes_detail', key=key),
        'text': notes[key]
    }

# Query the database and send the jsonified results
@app.route("/apiCall", methods=["POST"])
def send():
    dicbody = request.json()
    if request.method == "POST":
   

    return render_template("form.html")


@app.route("/api/pals")
def pals():
    results = db.session.query(hiking.id, hiking.summary).all()

    return jsonify(results)


if __name__ == "__main__":
    app.run()
