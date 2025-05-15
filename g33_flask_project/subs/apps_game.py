from flask import Flask, render_template, request, session
from classes.game import Game

prev_option = ""

def apps_game():
    global prev_option
    ulogin=session.get("user")
    if (ulogin != None):
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if option == "edit":
            butshow, butedit = "disabled", "enabled"
        elif option == "delete":
            obj = Game.current()
            Game.remove(obj.id)
            if not Game.previous():
                Game.first()
        elif option == "insert":
            butshow, butedit = "disabled", "enabled"
        elif option == 'cancel':
            pass
        elif prev_option == 'insert' and option == 'save':
            strobj = str(Game.get_id(0))
            strobj = strobj + ';' + request.form["name"] + ';' + \
            request.form["dob"] + ';' + request.form["salary"]
            obj = Game.from_string(strobj)
            Game.insert(obj.id)
            Game.last()
        elif prev_option == 'edit' and option == 'save':
            obj = Game.current()
            obj.name = request.form["name"]
            obj.dob = request.form["dob"]
            obj.salary = float(request.form["salary"])
            Game.update(obj.id)
        elif option == "first":
            Game.first()
        elif option == "previous":
            Game.previous()
        elif option == "next":
            Game.nextrec()
        elif option == "last":
            Game.last()
        elif option == 'exit':
            return render_template("index.html", ulogin=session.get("user"))
        prev_option = option
        obj = Game.current()
        if option == 'insert' or len(Game.lst) == 0:
            id = 0
            id = Game.get_id(id)
            name = dob = salary = ""
        else:
            id = obj.id
            name = obj.name
            dob = obj.dob
            salary = obj.salary
        return render_template("Game.html", butshow=butshow, butedit=butedit, 
                        id=id,name = name,dob=dob,salary=salary, 
                        ulogin=session.get("user"))
    else:
        return render_template("index.html", ulogin=ulogin)
# -*- coding: utf-8 -*-

