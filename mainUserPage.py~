from flask import render_template, session, request
from app import app
from db import db

@app.route("/mainUserPage", methods =["POST"])
def mainUserPage():
	

    sql = "SELECT * FROM users"
    result = db.session.execute(sql)
    user = result.fetchall()    
	
    
	
	
    return render_template("userInfo.html", info = user)