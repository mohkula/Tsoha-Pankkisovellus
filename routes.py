from app import app
from flask import render_template
from db import db


@app.route("/")
def index():
    if not mainUserCreated():
        addMainUser()    	
	
    
    return render_template("index.html")
    
def mainUserCreated():
    sql = "SELECT username FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":'Mainuser'})
    user = result.fetchone() 
    print(user)
    if user == None:
        return False
    
    return True
    
def addMainUser():
    sql = """INSERT INTO users (username,password, email, phone,address, mainUser)
            VALUES ('Mainuser','pbkdf2:sha256:150000$wBt7Fv97$0cf63583dc1f93855a58fb39d11f22712a6a0e6d4c3ee936387d6c079ee88754','Main.main@main.com', 1756475849,'Mainland', TRUE)"""
    db.session.execute(sql)
    db.session.commit()
    
    

@app.route("/mainuserPage")
def mainUserPage():

    return render_template("mainuserPage.html")