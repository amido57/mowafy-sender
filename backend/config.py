import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///mowafy.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FB_APP_ID = os.getenv("FB_APP_ID", "")
    FB_APP_SECRET = os.getenv("FB_APP_SECRET", "")
    FB_REDIRECT_URI = os.getenv("FB_REDIRECT_URI", "http://localhost:5000/facebook/callback")
