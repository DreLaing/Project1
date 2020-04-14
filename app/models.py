from . import db
from datetime import datetime

class userProfile(db.Model):

    __tablename__ = 'user_profiles'

    userid = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    email = db.Column(db.String(80))
    gender  = db.Column(db.String(10))
    location = db.Column(db.String(100))
    bio = db.Column(db.Text())
    image = db.Column(db.String(100))
    date_created = db.Column(db.DateTime())

    def __int__(self, firstname, lastname, email, location, bio, image):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.location = location
        self.bio = bio
        self.image = image


