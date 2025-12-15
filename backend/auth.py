from flask import Blueprint, request
from database import db
from models import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    email = request.json.get("email")
    if not email:
        return {"error": "email required"}, 400
    user = User.query.filter_by(email=email).first()
    if not user:
        user = User(email=email)
        db.session.add(user)
        db.session.commit()
    return {"message": "logged in", "user_id": user.id}
