from flask import Flask, render_template, request, session
from classes.player import Player

prev_option = ""

def apps_player():
    global prev_option
    ulogin=session.get("user")
    if (ulogin != None):
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if option == "edit":
            butshow, butedit = "disabled", "enabled"
        elif option == "delete":
            obj = Player.current()
            Player.remove(obj.id)
            if not Player.previous():
                Player.first()
        elif option == "insert":
            butshow, butedit = "disabled", "enabled"
        elif option == 'cancel':
            pass
        elif prev_option == 'insert' and option == 'save':
            strobj = str(Player.get_id(0))
            strobj = strobj + ';' + request.form["name"] + ';' + \
            request.form["dob"] + ';' + request.form["salary"]
            obj = Player.from_string(strobj)
            Player.insert(obj.id)
            Player.last()
        elif prev_option == 'edit' and option == 'save':
            obj = Player.current()
            obj.name = request.form["name"]
            obj.dob = request.form["dob"]
            obj.salary = float(request.form["salary"])
            Player.update(obj.id)
        elif option == "first":
            Player.first()
        elif option == "previous":
            Player.previous()
        elif option == "next":
            Player.nextrec()
        elif option == "last":
            Player.last()
        elif option == 'exit':
            return render_template("index.html", ulogin=session.get("user"))
        prev_option = option
        obj = Player.current()
        if option == 'insert' or len(Player.lst) == 0:
            id = 0
            id = Player.get_id(id)
            name = dob = salary = ""
        else:
            id = obj.id
            name = obj.name
            dob = obj.dob
            salary = obj.salary
        return render_template("Player.html", butshow=butshow, butedit=butedit, 
                        id=id,name = name,dob=dob,salary=salary, 
                        ulogin=session.get("user"))
    else:
        return render_template("index.html", ulogin=ulogin)



