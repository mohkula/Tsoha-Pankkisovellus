from db import db
from app import app
from werkzeug.security import check_password_hash, generate_password_hash
from flask import request, render_template, session, redirect

@app.route("/login", methods =["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    
    sql = "SELECT password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()    
    if user == None:
        # TODO: invalid username
        return redirect("/")
    	
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
	