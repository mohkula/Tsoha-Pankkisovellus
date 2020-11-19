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