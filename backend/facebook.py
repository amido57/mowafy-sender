import requests
from flask import Blueprint, redirect, request
from config import Config

facebook_bp = Blueprint("facebook", __name__)

@facebook_bp.route("/login")
def fb_login():
    url = (
        "https://www.facebook.com/v19.0/dialog/oauth"
        f"?client_id={Config.FB_APP_ID}"
        f"&redirect_uri={Config.FB_REDIRECT_URI}"
        "&scope=pages_show_list,pages_messaging"
    )
    return redirect(url)

@facebook_bp.route("/callback")
def fb_callback():
    code = request.args.get("code")
    if not code:
        return {"error": "no code"}
    token_url = "https://graph.facebook.com/v19.0/oauth/access_token"
    res = requests.get(token_url, params={
        "client_id": Config.FB_APP_ID,
        "client_secret": Config.FB_APP_SECRET,
        "redirect_uri": Config.FB_REDIRECT_URI,
        "code": code
    }).json()
    return res
