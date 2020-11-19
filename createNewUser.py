from app import app
from flask import render_template
@app.route("/createNewUser", methods =["POST"]) 
def createNewUser(): 
    return render_template("createUser.html")