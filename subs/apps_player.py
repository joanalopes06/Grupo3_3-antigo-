<<<<<<< HEAD
from flask import render_template, request, session
from datetime import datetime
=======
from flask import Flask, render_template, request, session
>>>>>>> 11e013834dcf7cc13e1dceef9261badcbf333104
from classes.player import Player

prev_option = ""

def apps_player():
    global prev_option
<<<<<<< HEAD
    ulogin = session.get("user")
    if ulogin:
=======
    ulogin=session.get("user")
    if (ulogin != None):
>>>>>>> 11e013834dcf7cc13e1dceef9261badcbf333104
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
<<<<<<< HEAD
            username = request.form["username"]
            level = int(request.form["level"])
            join_date = datetime.strptime(request.form["join_date"], "%Y-%m-%d")
            score = int(request.form["score"])
            obj = Player(None, username, level, join_date, score)
            Player.insert(obj)
            Player.last()
        elif prev_option == 'edit' and option == 'save':
            obj = Player.current()
            obj.username = request.form["username"]
            obj.level = int(request.form["level"])
            obj.join_date = datetime.strptime(request.form["join_date"], "%Y-%m-%d")
            obj.score = int(request.form["score"])
            Player.update(obj)
=======
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
>>>>>>> 11e013834dcf7cc13e1dceef9261badcbf333104
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
<<<<<<< HEAD
        if option == 'insert' or not obj:
            id = 0
            username = level = join_date = score = ""
        else:
            id = obj.id
            username = obj.username
            level = obj.level
            join_date = obj.join_date
            score = obj.score
        return render_template("Player.html", butshow=butshow, butedit=butedit,
                               id=id, username=username, level=level, join_date=join_date, score=score,
                               ulogin=session.get("user"))
    else:
        return render_template("index.html")
=======
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



>>>>>>> 11e013834dcf7cc13e1dceef9261badcbf333104
