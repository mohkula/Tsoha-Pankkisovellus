
from flask import render_template, session, request, redirect
from app import app
from db import db
import random



@app.route("/userPage", methods =["POST"])
def userPage():
	
    if(session["username"]):
		
        username = session["username"]

        sql = "SELECT username, email, phone, address FROM users WHERE username=:username"
        result = db.session.execute(sql, {"username":username})
        user = result.fetchone()    
	
	
	
        return render_template("userPage.html", info = user)

    return redirect("/")
    

@app.route("/showCards")
def showCards():
    if(session["username"]):
		
        username = session["username"]

        sql = "SELECT card_number, expirationdate FROM cards WHERE customer_id= (SELECT id FROM users WHERE username =:username)"
        result = db.session.execute(sql, {"username":username})
        card_info = result.fetchall()
	
	
        return render_template("userPage.html", cardInfo = card_info)

    return redirect("/")

@app.route("/addCard", methods =["POST"])    
def addCard():
    if(session["username"]):
		
        username = session["username"]
        
        card_number = ""
        for i in range(16):
            card_number += str(random.randint(0,9))
        
        card_number = int(card_number)


        sql = "SELECT id FROM users WHERE username=:username"
        result = db.session.execute(sql, {"username":username})
        customer_id = result.fetchone()[0]    
	
        sql = """INSERT INTO cards (customer_id, card_number)
            VALUES (:customer_id,:card_number)"""
            
            
        db.session.execute(sql, {"customer_id":customer_id,"card_number":card_number})
        db.session.commit()
        
        sql = "UPDATE cards SET expirationdate = expirationdate + interval '4 years' WHERE card_number =:card_number "
        db.session.execute(sql, {"card_number":card_number})
        db.session.commit()
        
        return render_template("userPage.html")
    
    return redirect("/")    
            
    

    
	
    