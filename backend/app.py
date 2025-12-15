from flask import Flask
from flask_cors import CORS
from config import Config
from database import db
from auth import auth_bp
from facebook import facebook_bp

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
db.init_app(app)

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(facebook_bp, url_prefix="/facebook")

@app.route("/")
def index():
    return {"status": "Mowafy Sender Backend Running"}

if __name__ == "__main__":
    app.run()
