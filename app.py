from flask import Flask, render_template, request, session
<<<<<<< HEAD
from classes.player import Player
from datafile import filename
from classes.game import Game
from classes.game_player import Game_player
from classes.tournament import Tournament

from classes.userlogin import Userlogin
from subs.apps_player import apps_player 
=======
from classes.game import Game
from datafile import filename
from classes.game_player import Game_player
from classes.player import Player
from classes.tournament import Tournament

from classes.userlogin import Userlogin
from subs.apps_player import apps_player
>>>>>>> 11e013834dcf7cc13e1dceef9261badcbf333104
from subs.apps_gform import apps_gform 
from subs.apps_subform import apps_subform 
from subs.apps_userlogin import apps_userlogin

app = Flask(__name__)

Player.read(filename + 'Grupo3.db')
<<<<<<< HEAD
Game.read(filename + 'Grupo3.db')
Game_player.read(filename + 'Grupo3.db')
Tournament.read(filename + 'Grupo3.db')

=======
>>>>>>> 11e013834dcf7cc13e1dceef9261badcbf333104
Userlogin.read(filename + 'Grupo3.db')
app.secret_key = 'BAD_SECRET_KEY'
@app.route("/")
def index():
    return render_template("index.html", ulogin=session.get("user"))
@app.route("/login")
def login():
    return render_template("login.html", user= "", password="", ulogin=session.get("user"),resul = "")
@app.route("/logoff")
def logoff():
    session.pop("user",None)
    return render_template("index.html", ulogin=session.get("user"))
@app.route("/chklogin", methods=["post","get"])
def chklogin():
    user = request.form["user"]
    password = request.form["password"]
    resul = Userlogin.chk_password(user, password)
    if resul == "Valid":
        session["user"] = user
        return render_template("index.html", ulogin=session.get("user"))
    return render_template("login.html", user=user, password = password, ulogin=session.get("user"),resul = resul)
@app.route("/Player", methods=["post","get"])
def player():
    return apps_player()
@app.route("/gform/<cname>", methods=["post","get"])
def gform(cname):
    return apps_gform(cname)
@app.route("/subform/<cname>", methods=["post","get"])
def subform(cname):
    return apps_subform(cname)
@app.route("/Userlogin", methods=["post","get"])
def userlogin():
    return apps_userlogin()
<<<<<<< HEAD
if __name__ == '__main__':
    app.run()
    
    
=======
if __name__ == '_main_':
    app.run()
    
>>>>>>> 11e013834dcf7cc13e1dceef9261badcbf333104
