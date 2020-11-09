
from flask import Flask
from flask import redirect, render_template, request, session
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy

import re

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)



@app.route("/")
def index():
    try:
    	
        sql = "CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT, password TEXT)"
        db.session.execute(sql)
        db.session.commit()
    except:
    	print("taulu on jo luotu")
    	
    return render_template("index.html")

    
    
@app.route("/login", methods =["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    
    sql = "SELECT password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()    
    if user == None:
        # TODO: invalid username
        print("kayttajaa ei loydy")
    	
    else:
        hash_value = user[0]
    if check_password_hash(hash_value,password):
        session["username"] = username
    else:
        print("vaara salasana")
  
    
    
    # TODO: check username and password
    return redirect("/")
    
   
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
    
@app.route("/createNewUser", methods =["POST"])
def createNewUser():
	
	return render_template("createUser.html")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

    
