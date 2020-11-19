
from flask import Flask
from flask import redirect, render_template, request, session
from os import getenv




import re

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")

                                                                    
from newUser import newUser
import routes
from login import login
from mainUserPage import mainUserPage
from createNewUser import createNewUser		



    


@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

    
