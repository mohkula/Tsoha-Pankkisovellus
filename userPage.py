
from flask import render_template, session, request, redirect
from app import app
from db import db

@app.route("/userPage", methods =["POST"])
def userPage():
	
    if(session["username"]):
		
        username = session["username"]

        sql = "SELECT username, email, phone, address FROM users WHERE username=:username"
        result = db.session.execute(sql, {"username":username})
        user = result.fetchone()    
	
	
	
        return render_template("userInfo.html", info = user)

    return redirect("/")