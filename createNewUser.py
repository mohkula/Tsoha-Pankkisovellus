from flask import render_template
from app import app

@app.route("/createNewUser", methods=["POST"])
def createNewUser():
    return render_template("createUser.html")
