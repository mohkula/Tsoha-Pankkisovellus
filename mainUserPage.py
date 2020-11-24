from flask import render_template, session, request, redirect
from app import app
from db import db






@app.route("/mainUserPage", methods =["POST"])
def mainUserPage():
    
    if(session["username"] == "Mainuser"):
        
        sql = "SELECT email, phone, address FROM users WHERE username <> 'Mainuser'"
        result = db.session.execute(sql)
        userInfo = result.fetchall()
    
    
    
    
        return render_template("mainuserPage.html", info = userInfo)
    
    return redirect("/")
    
    
@app.route("/changeUserInfo", methods =["POST"])
def changeUserInfo():
    if(session["username"] == "Mainuser"):
        username = request.form["user"]
        
        sql = "SELECT username FROM users WHERE username=:username"
        result = db.session.execute(sql, {"username":username})
        user = result.fetchone()[0]   
        
        sql = "SELECT email FROM users WHERE username=:username"
        result = db.session.execute(sql, {"username":username})
        email = result.fetchone()[0]  
        
        sql = "SELECT phone FROM users WHERE username=:username"
        result = db.session.execute(sql, {"username":username})
        phone = result.fetchone()[0]  
        
        sql = "SELECT address FROM users WHERE username=:username"
        result = db.session.execute(sql, {"username":username})
        address = result.fetchone()[0]  
        
        
        
        
        if(user == None):
            return render_template("mainuserPage.html", error = ("Asiakasta ei löytynyt nimellä " + username))
            
        return render_template("editInfo.html", username = username, currentEmail = email, currentPhone = phone, currentAddress = address)




