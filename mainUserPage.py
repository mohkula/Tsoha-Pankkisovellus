from flask import render_template, session, request
from app import app
from db import db

@app.route("/mainUserPage", methods =["POST"])
def mainUserPage():
	

    sql = "SELECT email, phone, address FROM users WHERE username <> 'Mainuser'"
    result = db.session.execute(sql)
    userInfo = result.fetchall()    
	
    
	
	
    return render_template("mainuserPage.html", info = userInfo)