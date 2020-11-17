
from flask import render_template, session, request
from app import app
from db import db

@app.route("/userPage", methods =["POST"])
def userPage():
	
    username = session["username"]

    sql = "SELECT username, email, phone, address FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()    
	
    print(user)
	
	
    return render_template("userInfo.html", info = user)