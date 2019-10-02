from .app import db

class hiking(db.Model):
    __tablename__ = 'hiking'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    type = db.Column(db.String(64))
    summary = db.Column(db.String(600))
    difficulty = db.Column(db.String(64))
    stars = db.Column(db.Float)
    starVotes = db.Column(db.Integer)
    location = db.Column(db.String(64))
    url = db.Column(db.String(164))
    imgSqSmall = db.Column(db.String(164))
    imgSmall = db.Column(db.String(164))
    imgSmallMed = db.Column(db.String(164))
    imgMedium = db.Column(db.String(164))
    imgMedium = db.Column(db.String(164))
    length = db.Column(db.Float)
    ascent = db.Column(db.Float)
    descent = db.Column(db.Float)
    high = db.Column(db.Float)
    low = db.Column(db.Float)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    conditionStatus = db.Column(db.String(64))
    conditionDetails = db.Column(db.String(64))
    conditionDate = db.Column(db.Float)

