from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models import user

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register",methods=["POST"])
def register():
    # check for validation first

    if not user.User.validate_register(request.form):
        return redirect("/")
    user_id = user.User.register(request.form)
    session["user_id"] = user_id
    return redirect("/home")