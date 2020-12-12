
from app import app
from flask import render_template, session, redirect
from db import db

@app.route("/")
def index():
    
    return render_template("index.html")

@app.route("/mainuserPage")
def mainUserPage():

    return render_template("mainuserPage.html")



@app.route("/userPage")
def userPage():

    return render_template("userPage.html")



@app.route("/logout")
def logout():
    del session["username"]

    return redirect("/")
