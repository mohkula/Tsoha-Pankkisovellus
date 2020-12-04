from db import db
from app import app
from werkzeug.security import check_password_hash, generate_password_hash
from flask import render_template, session, redirect, request



def isMainuser(username):
    sql = "SELECT mainUser FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    status = str(result.fetchall())
    
    if "False" in status:
    	return False;
    return True
    	
	

@app.route("/login", methods =["POST"])
def login():
    
    username = request.form["username"]
    password = request.form["password"]
    
    
        
    
    sql = "SELECT password FROM users WHERE username=:username AND active = 't'"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()    
    if user == None:
        
        return render_template("index.html", error = "Väärä käyttäjänimi tai salasana")

    	
    else:
        hash_value = user[0]
    if check_password_hash(hash_value,password):
        
        	
        	
        session["username"] = username
        if(isMainuser(username)):
        	return render_template("mainuserPage.html")
        	
        	
    else:
        return render_template("index.html", error = "Väärä käyttäjänimi tai salasana")
  
    
    
    return render_template("userPage.html")
    
   
 
	