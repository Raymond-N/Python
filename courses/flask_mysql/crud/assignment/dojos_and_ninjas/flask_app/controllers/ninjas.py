from flask_app import app
from flask_app.models import ninja,dojo
from flask import render_template,request,redirect

@app.route("/add-ninja")
def ninja_form():
    dojos = dojo.Dojo.get_all_dojos()
    return render_template("ninja-form.html",dojos=dojos)

@app.route("/create-ninja",methods=["POST"])
def create_ninja():
    ninja.Ninja.create_ninja(request.form)
    return redirect("/ninjas")

@app.route("/ninjas")
def display_ninjas():
    ninjas = ninja.Ninja.get_all_ninjas()
    return render_template("ninjas.html",ninjas=ninjas)

@app.route("/ninjas/<int:id>")
def display_ninja(id):
    selected_ninja = ninja.Ninja.get_ninja_by_id(id)
    return render_template("ninja-details.html",ninja=selected_ninja)

@app.route("/ninjas/<int:id>/edit")
def edit_ninja(id):
    edit_ninja = ninja.Ninja.get_ninja_by_id(id)
    dojos = dojo.Dojo.get_all_dojos()
    return render_template("update-ninja.html",ninja=edit_ninja,dojos=dojos)

@app.route("/ninjas/<int:id>/delete")
def delete_ninja(id):
    ninja.Ninja.delete_ninja(id)
    return redirect("/ninjas")

@app.route("/ninjas/<int:id>/update",methods=["POST"])
def update_ninja(id):
    ninja.Ninja.update_ninja(request.form)
    return redirect(f"/ninjas/{id}")