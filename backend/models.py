from database import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class FacebookPage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    page_id = db.Column(db.String(50))
    name = db.Column(db.String(200))
    access_token = db.Column(db.Text)
