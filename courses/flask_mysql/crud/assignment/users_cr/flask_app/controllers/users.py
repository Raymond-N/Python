from flask_app import app
from flask_app.models import user
from flask import render_template, request, redirect

@app.route("/")
def index():
    users = user.User.get_all_users()
    print(users)
    return render_template("index.html",users=users)

@app.route("/create-user",methods=["POST"])
def create_user():
    user.User.create_user(request.form)
    return redirect("/display-users")

@app.route("/display-users")
def show_users():
    users = user.User.get_all_users()
    return render_template("display-users.html",users=users)