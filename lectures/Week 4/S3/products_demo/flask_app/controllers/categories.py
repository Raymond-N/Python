from flask_app import app
from flask_app.models import category
from flask import render_template,request,redirect
@app.route("/")
def index():
    categories = category.Category.get_all_categories()
    return render_template("index.html",categories=categories)

@app.route("/add-category",methods=["post"])
def add_category():
    category.Category.create_category(request.form)
    return redirect("/")