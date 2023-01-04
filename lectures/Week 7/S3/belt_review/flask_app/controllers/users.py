from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models import user

@app.route("/")
def index():
    if "user_id" not in session:
        return render_template("index.html")
    return redirect("/dashboard")

@app.route("/register",methods=["POST"])
def register():
    # check for validation first

    if not user.User.validate_register(request.form):
        return redirect("/")
    user_id = user.User.register(request.form)
    print("__REGISTER USER ID__",user_id)
    session["user_id"] = user_id
    return redirect("/dashboard")

@app.route("/login",methods=["POST"])
def login():
    # check for validation first
    logged_in_user = user.User.validate_login(request.form)
    print("__USER__",logged_in_user)
    if not logged_in_user:
        return redirect("/")
    print("__LOGIN USER ID__",logged_in_user)
    session["user_id"] = logged_in_user.id
    return redirect("/dashboard")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")