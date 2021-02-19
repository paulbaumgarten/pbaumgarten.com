# models.py
from main import db
from datetime import datetime

class User(db.Model):
    userid = db.Column(db.String(100), primary_key=True)
    displayName = db.Column(db.String(100))
    password = db.Column(db.String(100))
    email = db.Column(db.String(100))
    avatar = db.Column(db.String(100))
    def __str__(self):
        return self.displayName + " ("+self.userid+")"

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(100))
    displayName = db.Column(db.String(100))
    dateTime = db.Column(db.DateTime, default=datetime.utcnow)
    ip = db.Column(db.String(20))
    message = db.Column(db.String(500))
    def as_dict(self):
        return {"id": self.id, 
            "displayName": self.displayName, 
            "dateTime":self.dateTime.timestamp(), 
            "message":self.message,
            "userid":self.userid}

