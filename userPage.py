
from flask import render_template, session, request, redirect
from app import app
from db import db
import random



@app.route("/ShowUserInfo", methods =["POST"])
def ShowUserInfo():
	
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

        sql = "SELECT card_number, expirationdate FROM cards WHERE customer_id= (SELECT id FROM users WHERE username =:username) AND active = TRUE"
        result = db.session.execute(sql, {"username":username})
        card_info = result.fetchall()
        card_infoList = []
        for i in card_info:
            card_infoList.append(("kortin numero: " +str(i[0]),"kortin voimassaoloaika: " + str(i[1])))
            
             
	
        return render_template("userPage.html", cardInfo = card_infoList)

    return redirect("/")



def orderCard(username):
    sql = """INSERT INTO orders (type, customer_id)
        VALUES (1,  (SELECT id from users WHERE username =:username))"""
            
    db.session.execute(sql, {"username":username})
    db.session.commit()

@app.route("/addCard", methods =["POST"])    
def addCard():
    if(session["username"]):
		
        username = session["username"]
        orderCard(username)
        card_number = ""
        for i in range(16):
            card_number += str(random.randint(0,9))
        
        card_number = int(card_number)


        sql = "SELECT id FROM users WHERE username=:username"
        result = db.session.execute(sql, {"username":username})
        customer_id = result.fetchone()[0]    
	
        sql = """INSERT INTO cards (customer_id, account_id, card_number)
            VALUES (:customer_id,  (SELECT id from bankAccounts WHERE customer_id = (SELECT id FROM users WHERE username =:username))  ,:card_number)"""
            
            
        db.session.execute(sql, {"customer_id":customer_id, "username":username ,"card_number":card_number})
        db.session.commit()
        
        sql = "UPDATE cards SET expirationdate = expirationdate + interval '4 years' WHERE card_number =:card_number "
        db.session.execute(sql, {"card_number":card_number})
        db.session.commit()

        
        return render_template("userPage.html", success = "Kortti tilattu")
    
    return redirect("/")    
            
    

@app.route("/reportMissingCard", methods = ["POST"])
def reportMissingCard():

    return render_template("reportMissingCard.html")
    
	
    

@app.route("/addCardReport", methods = ["POST"])
def addCardReport():
    card_number = request.form["lostCard"]


    if not card_number.isdigit():
        return render_template("reportMissingCard.html", error = "Antamasi kortin numero ei kelpaa")



    if not isUsersCard(card_number):
        return render_template("reportMissingCard.html", error = "Korteistasi ei löydy korttia numerolla: " + card_number)


    type = int(request.form["type"])





    sql = """INSERT INTO cardWarnings (card_id,type)
        VALUES ((SELECT id from cards WHERE card_number =:card_number),:type)"""

    db.session.execute(sql, {"card_number":card_number,"type":type})
    db.session.commit()

    return render_template("userPage.html", success = "Kortti raportoitu")

def isUsersCard(card_number):


    username = session["username"]
    
    sql = "SELECT customer_id FROM cards WHERE card_number =:card_number"

    result = db.session.execute(sql, {"card_number":card_number})
   
    customer_id = result.fetchone()


    if customer_id == None:
        return False
    
    customer_id 

    sql = "SELECT id FROM users WHERE username =:username"

    result = db.session.execute(sql, {"username":username})

    if result.fetchone()[0] == customer_id[0]:
        return True

    return False

