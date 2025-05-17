from flask import Flask, render_template, request, session

<<<<<<< HEAD
from classes.player import Player
from classes.game_player import Game_player
from classes.game import Game
from classes.tournament import Tournament
=======
from classes.customer import Customer
from classes.product import Product
from classes.customerorder import CustomerOrder
from classes.orderproduct import OrderProduct
>>>>>>> 11e013834dcf7cc13e1dceef9261badcbf333104
from classes.userlogin import Userlogin

prev_option = ""

def apps_gform(cname=''):
    global prev_option
    ulogin=session.get("user")
    if (ulogin != None):
<<<<<<< HEAD
        cl = eval(cname.capitalize())
=======
        cl = eval(cname)
>>>>>>> 11e013834dcf7cc13e1dceef9261badcbf333104
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if prev_option == 'insert' and option == 'save':
            strobj = request.form[cl.att[0]]
            for i in range(1,len(cl.att)):
                strobj += ";" + request.form[cl.att[i]]
            obj = cl.from_string(strobj)
            cl.insert(getattr(obj, cl.att[0]))
            cl.last()
        elif prev_option == 'edit' and option == 'save':
            obj = cl.current()
            for i in range(1,len(cl.att)):
                setattr(obj, cl.att[i], request.form[cl.att[i]])
            cl.update(getattr(obj, cl.att[0]))
        else:
            if option == "edit":
                butshow = "disabled"
                butedit = "enabled"
            elif option == "delete":
                obj = cl.current()
                cl.remove(obj.id)
                if not cl.previous():
                    cl.first()
            elif option == "insert":
                butshow = "disabled"
                butedit = "enabled"
            elif option == 'cancel':
                pass
            elif option == "first":
                cl.first()
            elif option == "previous":
                cl.previous()
            elif option == "next":
                cl.nextrec()
            elif option == "last":
                cl.last()
            elif option == 'exit':
                return render_template("index.html", ulogin=session.get("user"))
        prev_option = option
        obj = cl.current()
        if option == 'insert' or len(cl.lst) == 0:
            obj = dict()
            obj[cl.att[0]] = 0
            for i in range(1, len(cl.att)):
                obj[cl.att[i]] = ""
        # else:
        #     for att in cl.att:
        #         dobj[att[1:]] = getattr(obj, att)
        # return render_template("gform.html", butshow=butshow, butedit=butedit, cname=cname, code=code,name = name,dob=dob,salary=salary)
        return render_template("gform.html", butshow=butshow, butedit=butedit, cname=cname, obj=obj,att=cl.att,des=cl.des,ulogin=session.get("user"))
    else:
        return render_template("index.html", ulogin=ulogin)
# -- coding: utf-8 --


