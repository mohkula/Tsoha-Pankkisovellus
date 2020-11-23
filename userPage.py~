
from flask import render_template, session, request, redirect
from app import app
from db import db

@app.route("/userPage", methods =["POST"])
def userPage():
	
    if(session["username"]):
		
        username = session["username"]

        sql = "SELECT username, email, phone, address FROM users WHERE username=:username"
        result = db.session.execute(sql, {"username":username})
        user = result.fetchone()    
	
	
	
        return render_template("userInfo.html", info = user)

    return redirect("/")
    
    
@app.route("/addCard", methods =["POST"])    
def addCard():
    if(session["username"]):
		
        username = session["username"]
	
        sql = "SELECT id FROM users WHERE username=:username"
        result = db.session.execute(sql, {"username":username})
        customer_id = result.fetchone()[0]    
	
        sql = """INSERT INTO cards (customer_id, card_number, expirationDate)
            VALUES (:customer_id,:card_number,:expirationDate)"""
            
            
        db.session.execute(sql, {"customer_id":customer_id,"card_number":1232343434545656,"expirationDate":"2021-12-21"})
        db.session.commit()
        
            
    return render_template("userInfo.html")

    
	
    