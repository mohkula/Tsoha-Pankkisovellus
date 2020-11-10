
    
from db import db
from flask import request, render_template, session, redirect
from app import app
from werkzeug.security import check_password_hash, generate_password_hash
import re
    
def emailMatch(email):
    pattern = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(pattern,email)):  
        return True
          
    else:  
        return False  
        
@app.route("/newUser", methods =["POST"])
def newUser():
    username = request.form["newUsername"]
    password = request.form["newPassword"]
    email = request.form["emailAddress"]
    phoneNumber = request.form["phoneNumber"]
    address = request.form["address"]
    
    if len(username) == 0:
    	print("Username cant be empty")
    	return render_template("createUser.html")
    	
    if not emailMatch(email):
    	return render_template("createUser.html")
   
    if len(phoneNumber) != 10 or not phoneNumber.isdigit():
    	print("phone number must be 10 digits")
    	return render_template("createUser.html")
    	

    
    sql = "SELECT username FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()    
    
    if user == None:
        if(len(password) >= 8):
        	
            hash_value = generate_password_hash(password)
            sql = "INSERT INTO users (username,password) VALUES (:username,:password)"
            db.session.execute(sql, {"username":username,"password":hash_value})
            db.session.commit()
        
            session["username"] = username
        else:
        	print("password too short")
  
    else:
    	print("user already exists")
    
  
    
    return redirect("/")    
    
