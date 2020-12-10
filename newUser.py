
    
from db import db
from flask import request, render_template, session, redirect
from app import app
from werkzeug.security import check_password_hash, generate_password_hash
import re
import random
    
def emailMatch(email):
    pattern = '^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(pattern,email)):  
        return True
          
    else:  
        return False  
        
        

def isTooLong(info,max_length):	
    
    if len(info) > max_length:
        return True        
    
    return False
  
def newBankAccount(username):

    account_number = "FI"

    for i in range(2):
        account_number += str(random.randint(0,9))
    
    for i in range(14):
        if i % 4 == 0:
            account_number += " "
        account_number += str(random.randint(0,9))
        

  

    sql = """INSERT INTO bankAccounts (customer_id ,account_number)
            VALUES ((SELECT id FROM users WHERE username =:username),:account_number)"""    

    db.session.execute(sql, {"username":username, "account_number":account_number})
    db.session.commit()




def orderUser(username):
    sql = "INSERT INTO orders (type,username) VALUES (0, :username )"
            
    db.session.execute(sql,{"username":username})
    db.session.commit()



def returnCreateUser(error, username, email, phone, address):
    return render_template("createUser.html", error = error, username = username, email = email, phone = phone, address = address)


@app.route("/newUser", methods =["POST"])
def newUser():
    username = request.form["newUsername"]
    password = request.form["newPassword"]
    email = request.form["emailAddress"]
    phoneNumber = request.form["phoneNumber"]
    address = request.form["address"]
    
    
    if len(username) == 0:
        
        return returnCreateUser("Käyttäjänimi ei saa olla tyhjä", username, email, phoneNumber, address)

    if len(password) == 0:
        
       return returnCreateUser("Salasana ei saa olla tyhjä", username, email, phoneNumber, address)
        
    if isTooLong(username, 10):
        return returnCreateUser("Salasana saa olla enintään 10 merkkiä", username, email, phoneNumber, address)

        
    if isTooLong(email, 30):
       return returnCreateUser("Sähköposti saa olla enintään 30 merkkiä", username, email, phoneNumber, address)
        
    if isTooLong(address, 30):
       return returnCreateUser("Osoite saa olla enintään 30 merkkiä", username, email, phoneNumber, address)
        
    if isTooLong(password, 30):
       return returnCreateUser("Salasana saa olla enintään 30 merkkiä", username, email, phoneNumber, address)
    

    	
    if not emailMatch(email):
       return returnCreateUser("Sähköposti ei kelpaa", username, email, phoneNumber, address)
   
    if len(phoneNumber) != 10 or not phoneNumber.isdigit():
    	
       return returnCreateUser("Puhelinnumero ei kelpaa, täytyy olla 10 numeroa", username, email, phoneNumber, address)
    	
    if len(address) == 0:
       return returnCreateUser("Osoite ei saa olla tyhjä", username, email, phoneNumber, address)
        

    
    sql = "SELECT username FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()    
    
    if user == None:
        if(len(password) >= 8):
        	
            hash_value = generate_password_hash(password)
            sql = """INSERT INTO users (username,password, email, phone,address)
            VALUES (:username,:password,:email,:phone,:address)"""
            db.session.execute(sql, {"username":username,"password":hash_value,"email"
            :email,"phone":phoneNumber,"address":address})
            db.session.commit()
        
           # session["username"] = username
        else:
            
            return returnCreateUser("Salasana liian lyhyt, täytyy olla vähintään 8 merkkiä", username, email, phoneNumber, address)

  
    else:
        return returnCreateUser("Käyttäjänimi on jo olemassa", username, email, phoneNumber, address)

    
  
    
    orderUser(username)
    newBankAccount(username)
    return render_template("index.html",success = "Käyttäjä tilattu")   
    
