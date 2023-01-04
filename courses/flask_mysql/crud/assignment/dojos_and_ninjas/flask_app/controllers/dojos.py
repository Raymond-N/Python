from flask_app import app
from flask_app.models import dojo
from flask import render_template,request,redirect

@app.route("/")
def index():
    dojos = dojo.Dojo.get_all_dojos()
    return render_template("index.html",dojos=dojos)

@app.route("/add-dojo",methods=["POST"])
def add_dojo():
    dojo.Dojo.create_dojo(request.form)
    return redirect("/")

@app.route("/dojos/<id>")
def get_dojo_ninjas(id):
    ninjas = dojo.Dojo.get_dojo_ninjas(id)
    return render_template("ninjas.html",ninjas=ninjas)