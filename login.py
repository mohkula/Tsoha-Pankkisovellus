from db import db
from app import app
from werkzeug.security import check_password_hash, generate_password_hash
from flask import render_template, session, redirect, request


@app.route("/login", methods =["POST"])
def login():
    print(3)
    username = request.form["username"]
    password = request.form["password"]
    
    sql = "SELECT password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()    
    if user == None:
        print(2)
        return redirect("/")
    	
    else:
        hash_value = user[0]
    if check_password_hash(hash_value,password):
        session["username"] = username
    else:
        print("vaara salasana")
        return redirect("/")
  
    
    print(1)
    return render_template("userPage.html")
    
   
 
	