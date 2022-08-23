from flask import Blueprint, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

views = Blueprint(__name__, "views")

db_name = "hs_assignment_manager_db"

views.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

views.config['SQUALCHEMY_TRACK_MODIFICATION'] = True

db = SQLAlchemy(views)

@views.route("/")
def home():
    return render_template("main.html")

@views.route("/login", methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form('username') != 'admin' or request.form('password') != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for("main.html"))
        
    return render_template("login.html", error = error)

@views.route("/register", methods = ['GET', 'POST']) #check whether post also should go for it
def register():
    if request.method == 'GET':
        args = request.args
        name = args.get("name")
        username = args.get("username")
        password = args.get("password")
        db.session.query(name, username, password) #check this line again!! how to store data into query?
        
    return render_template("register.html")