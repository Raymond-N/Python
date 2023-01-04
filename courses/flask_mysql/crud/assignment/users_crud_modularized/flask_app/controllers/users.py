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
def display_users():
    users = user.User.get_all_users()
    return render_template("display-users.html",users=users)

@app.route("/show-user/<int:id>")
def show_user(id):
    selected_user = user.User.get_user_by_id(id)
    return render_template("show-user.html",user=selected_user)

@app.route("/show-user/<int:id>/delete")
def delete_user(id):
    user.User.delete_user(id)
    return redirect("/display-users")

@app.route("/show-user/<int:id>/edit")
def edit_user(id):
    edit_user = user.User.get_user_by_id(id)
    return render_template("update-user.html",user=edit_user,)

@app.route("/show-user/<int:id>/update",methods=["POST"])
def update_user(id):
    user.User.update_user(request.form)
    return redirect(f"/show-user/{id}")