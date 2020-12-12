from flask import render_template, session, request, redirect
from app import app
from db import db
import newUser

@app.route("/showCustomerInfo", methods=["POST"])
def showCustomerInfo():

    if session["username"] == "Mainuser":
        if session["csrf_token"] == request.form["csrf_token"]:

            sql = """SELECT username, email, phone, address FROM users
            WHERE username <> 'Mainuser' AND active = TRUE"""
            result = db.session.execute(sql)
            userInfo = result.fetchall()
            if not userInfo:
                return render_template("mainuserPage.html", error="Asiakkaita ei löytynyt")



            userInfoList = []

            for i in userInfo:

                userInfoList.append("Käyttäjänimi: " + str(i[0]) +
                                    ", sähköpotiosoite:  " + str(i[1]) + ", puhelinnumero: "
                                    + str(i[2]) + ", osoite: " + str(i[3]))




            return render_template("mainuserPage.html", userInfo=userInfoList)

    return redirect("/")


@app.route("/changeUserInfo", methods=["POST"])
def changeUserInfo():
    if session["username"] == "Mainuser":
        if session["csrf_token"] == request.form["csrf_token"]:


            return render_template("editInfo.html")
    return redirect("/")



def usernameExists(username):
    sql = "SELECT username FROM users WHERE username=:username AND active = TRUE"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()

    if user is None:
        return False

    return True


@app.route("/applyNewUsername", methods=["POST"])
def applyNewUsername():
    if session["username"] == "Mainuser":
        if session["csrf_token"] == request.form["csrf_token"]:


            username = request.form["user"]
            newUsername = request.form["newUser"]
            sql = "SELECT username FROM users WHERE username=:username AND active = TRUE"
            result = db.session.execute(sql, {"username":username})
            user = result.fetchone()

            if user is None:
                return render_template("editInfo.html",
                                       error="Asiakasta ei löytynyt nimellä " + username)


            if len(newUsername) == 0:

                return render_template("editInfo.html", error="Käyttäjänimi ei saa olla tyhjä")

            if newUser.isTooLong(newUsername, 10):
                return render_template("editInfo.html",
                                       error="Käyttäjänimi saa olla enintään 10 merkkiä")


            if usernameExists(newUsername):
                return render_template("editInfo.html", error="Käyttäjänimi on jo olemassa")



            sql = "UPDATE users SET username =:newUsername WHERE username =:oldUserName"

            db.session.execute(sql, {"newUsername":newUsername, "oldUserName":username})
            db.session.commit()
            return render_template("mainuserPage.html",
                                   success="käyttäjän " + username +
                                   " käyttäjänimi vaihdettu, uusi käyttäjänimi: " + newUsername)

    return redirect("/")




@app.route("/changeUsername", methods=["POST"])
def changeUsername():
    if session["username"] == "Mainuser":
        if session["csrf_token"] == request.form["csrf_token"]:

            return render_template("editInfo.html", username="Käyttäjänimi")

    return redirect("/")





@app.route("/applyNewEmail", methods=["POST"])
def applyNewEmail():
    if session["username"] == "Mainuser":
        if session["csrf_token"] == request.form["csrf_token"]:

            username = request.form["user"]
            if not usernameExists(username):
                return render_template("editInfo.html", error="Käyttäjänimeä ei ole olemassa")

            newEmail = request.form["email"]
            if newUser.isTooLong(newEmail, 30):
                return render_template("editInfo.html",
                                       error="Sähköposti saa olla enintään 30 merkkiä")

            if not newUser.emailMatch(newEmail):
                return render_template("editInfo.html", error="Sähköposti ei kelpaa")

            sql = "UPDATE users SET email =:newEmail WHERE username =:username"

            db.session.execute(sql, {"newEmail":newEmail, "username":username})
            db.session.commit()

            return render_template("mainuserPage.html", success="käyttäjän "
                                   + username + """ sähköpotiosoite vaihdettu,
                                   uusi sähköpotiosoite: """ + newEmail)

    return redirect("/")


@app.route("/changeEmail", methods=["POST"])
def changeEmail():
    if session["username"] == "Mainuser":
        if session["csrf_token"] == request.form["csrf_token"]:

            return render_template("editInfo.html", email="Sähköposti")

    return redirect("/")

@app.route("/applyNewPhonenumber", methods=["POST"])
def applyNewPhonenumber():

    if session["username"] == "Mainuser":

        if session["csrf_token"] == request.form["csrf_token"]:
            username = request.form["user"]
            if not usernameExists(username):
                return render_template("editInfo.html", error="Käyttäjänimeä ei ole olemassa")

            newPhone = request.form["phoneNumber"]
            if len(newPhone) != 10 or not newPhone.isdigit():

                return render_template("editInfo.html", error=
                                       "Puhelinnumero ei kelpaa, täytyy olla 10 numeroa")



            sql = "UPDATE users SET phone =:newPhone WHERE username =:username"

            db.session.execute(sql, {"newPhone":newPhone, "username":username})
            db.session.commit()

            return render_template("mainuserPage.html", success="käyttäjän "
                                   + username + """ puhelinnumero vaihdettu,
                                   uusi puhelinnumero: """ + newPhone)


    return redirect("/")


@app.route("/changePhonenumber", methods=["POST"])
def changePhonenumber():
    if session["username"] == "Mainuser":
        if session["csrf_token"] == request.form["csrf_token"]:

            return render_template("editInfo.html", phoneNumber="Puhelinnumero")

    return redirect("/")



@app.route("/applyNewAddress", methods=["POST"])
def applyNewAddress():

    if session["username"] == "Mainuser":
        if session["csrf_token"] == request.form["csrf_token"]:


            username = request.form["user"]
            if not usernameExists(username):
                return render_template("editInfo.html", error="Käyttäjänimeä ei ole olemassa")

            newAddress = request.form["address"]
            if newUser.isTooLong(newAddress, 30):
                return render_template("editInfo.html", error="osoite saa olla enintään 30 merkkiä")



            sql = "UPDATE users SET address =:newAddress WHERE username =:username"

            db.session.execute(sql, {"newAddress":newAddress, "username":username})
            db.session.commit()

            return render_template("mainuserPage.html", success="käyttäjän "
                                   + username + " osoite vaihdettu, uusi osoite: " + newAddress)

    return redirect("/")


@app.route("/changeAddress", methods=["POST"])
def changeAddress():
    if session["username"] == "Mainuser":
        if session["csrf_token"] == request.form["csrf_token"]:


            return render_template("editInfo.html", address="osoite")

    return redirect("/")


@app.route("/showCardOrders", methods=["POST"])
def showCardOrders():

    if session["username"] == "Mainuser":
        if session["csrf_token"] == request.form["csrf_token"]:

            sql = "SELECT customer_id, orderingDate FROM orders WHERE type = 1"
            result = db.session.execute(sql)
            orderInfo = result.fetchall()


            if not orderInfo:
                return render_template("mainuserPage.html", error="Ei tilattuja kortteja")



            orderInfoList = []
            usernameList = []

            for i in orderInfo:
                orderer = getUsername(int(i[0]))

                orderInfoList.append("asiakas " + str(orderer) +
                                     " on tilannut kortin " + str(i[1]))
                usernameList.append(str(orderer))




            return render_template("mainuserPage.html", cardOrderInfo=orderInfoList,
                                   cardOrdererNameList=usernameList)

    return redirect("/")


@app.route("/showAccountOrders", methods=["POST"])
def showAccountOrders():

    if session["username"] == "Mainuser":
        if session["csrf_token"] == request.form["csrf_token"]:

            sql = "SELECT username, orderingDate FROM orders WHERE type = 0"
            result = db.session.execute(sql)
            orderInfo = result.fetchall()

            if not orderInfo:
                return render_template("mainuserPage.html", error="Ei tilattuja Käyttäjiä")

            orderInfoList = []
            usernameList = []
            for i in orderInfo:
                newUsername = str(i[0])

                orderInfoList.append("Uusi käyttäjä nimellä "
                                     + str(newUsername) + " tilattu " + str(i[1]))
                usernameList.append(str(newUsername))



            return render_template("mainuserPage.html", accountOrderInfo=
                                   orderInfoList, usernameList=usernameList)

    return redirect("/")



def getUsername(customer_id):
    ci = customer_id
    sql = "SELECT username FROM users WHERE id =:customer_id"

    result = db.session.execute(sql, {"customer_id":ci})


    return result.fetchone()[0]



def getCard(card_id):
    ci = card_id
    sql = "SELECT card_number FROM cards WHERE id =:card_id"

    result = db.session.execute(sql, {"card_id":ci})


    return result.fetchone()[0]


@app.route("/acceptSelectedCards", methods=["POST"])
def acceptSelectedCards():

    if session["username"] == "Mainuser":
        if session["csrf_token"] == request.form["csrf_token"]:

            checkBox = request.form.getlist('usersCards')

            for i in checkBox:
                verifyCard(i)

            return render_template("mainuserPage.html")

    return redirect("/")



def verifyCard(username):
    if username == 0:
        return

    sql = """UPDATE cards SET active = TRUE WHERE customer_id=
    (SELECT id FROM users WHERE username =:username)"""


    db.session.execute(sql, {"username":username})
    db.session.commit()


    sql = """UPDATE bankAccounts SET active = TRUE WHERE customer_id =
    (SELECT id FROM users WHERE username =:username)"""


    db.session.execute(sql, {"username":username})
    db.session.commit()

    sql = """DELETE FROM orders WHERE type = 1 AND customer_id
    = (SELECT id FROM users WHERE username =:username)"""
    db.session.execute(sql, {"username":username})
    db.session.commit()




@app.route("/acceptSelectedCustomers", methods=["POST"])
def acceptSelectedCustomers():

    if session["username"] == "Mainuser":

        if session["csrf_token"] == request.form["csrf_token"]:

            checkBox = request.form.getlist('users')

            for i in checkBox:
                verifyUser(i)

            return render_template("mainuserPage.html", success="Valitut käyttäjät hyväksytty")

    return redirect("/")



def verifyUser(username):
    if username == 0:
        return

    sql = "UPDATE users SET active = TRUE WHERE username =:username"


    db.session.execute(sql, {"username":username})
    db.session.commit()

    sql = "DELETE FROM orders WHERE username =:username AND type = 0"
    db.session.execute(sql, {"username":username})
    db.session.commit()

@app.route("/showWarnings", methods=["POST"])
def showWarnings():

    if session["username"] == "Mainuser":

        if session["csrf_token"] == request.form["csrf_token"]:

            sql = "SELECT card_id, type, date  FROM cardwarnings ORDER BY type DESC"

            result = db.session.execute(sql)
            warnings = result.fetchall()

            if not warnings:
                return render_template("mainuserPage.html", error="Ei varoituksia")


            warningList = []

            for i in warnings:

                if int(i[1]) == 1:
                    message = " on varastettu"

                elif int(i[1]) == 0:
                    message = " on kadonnut"


                warningList.append("kortti " + str(getCard(i[0])) +
                                   message + ", ilmoitettu: " + str(i[2]))




            return render_template("mainuserPage.html", warnings=warningList)

    return redirect("/")
