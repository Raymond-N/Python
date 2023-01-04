from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models import user,recipe

@app.route("/recipes/new")
def add_recipe():
    if "user_id" not in session:
        return redirect("/")
    current_user = user.User.get_by_id(session["user_id"])
    return render_template("add-recipe.html",user=current_user)

@app.route("/add-recipe",methods=["POST"])
def create_recipe():
    if "user_id" not in session:
        return redirect("/")
    if recipe.Recipe.validate_recipe(request.form):
        recipe.Recipe.create_recipe(request.form)
        return redirect("/recipes")
    return redirect("/recipes/new")

@app.route("/recipes")
def recipes():
    if "user_id" not in session:
        return redirect("/")
    current_user = user.User.get_by_id(session["user_id"])
    all_recipes = recipe.Recipe.get_all_recipes()
    return render_template("recipes.html",user=current_user,recipes=all_recipes)

@app.route("/recipes/<int:id>")
def get_recipe(id):
    if "user_id" not in session:
        return redirect("/")
    current_user = user.User.get_by_id(session["user_id"])
    current_recipe = recipe.Recipe.get_recipe(id)
    return render_template("recipe-details.html",user=current_user,recipe=current_recipe)

@app.route("/recipes/edit/<int:id>")
def update_recipe(id):
    if "user_id" not in session:
        return redirect("/")
    current_user = user.User.get_by_id(session["user_id"])
    current_recipe = recipe.Recipe.get_recipe(id)
    return render_template("edit-recipe.html",user=current_user,recipe=current_recipe)

@app.route("/edit-recipe/<int:id>",methods=["POST"])
def edit_recipe(id):
    if "user_id" not in session:
        return redirect("/")
    if recipe.Recipe.validate_recipe(request.form):
        recipe.Recipe.update_recipe(request.form,id)
        return redirect(f"/recipes/{id}")
    return redirect(f"/recipes/edit/{id}")

@app.route("/recipes/delete/<int:id>")
def delete_recipe(id):
    if "user_id" not in session:
        return redirect("/")
    recipe.Recipe.delete_recipe(id)
    return redirect("/recipes")