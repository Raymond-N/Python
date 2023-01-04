from flask_app import app
from flask import render_template,request,redirect
from flask_app.models import product,category

@app.route("/add-product")
def product_form():
    categories = category.Category.get_all_categories()
    return render_template("product-form.html",categories=categories)

@app.route("/create-product",methods=["post"])
def create_product():
    product.Product.create_product(request.form)
    return redirect("/products")

@app.route("/products")
def display_products():
    products = product.Product.get_all_products()
    return render_template("products.html",products=products)

@app.route("/products/<int:id>")
def display_product(id):
    selected_product = product.Product.get_product_by_id(id)
    return render_template("product-details.html",product=selected_product)

@app.route("/products/<int:id>/delete")
def delete_product(id):
    product.Product.delete_product(id)
    return redirect("/products")

@app.route("/products/<int:id>/edit")
def edit_product(id):
    edit_product = product.Product.get_product_by_id(id)
    categories = category.Category.get_all_categories()
    return render_template("update-product.html",product=edit_product,categories=categories)

@app.route("/products/<int:id>/update",methods=["POST"])
def update_product(id):
    product.Product.update_product(request.form)
    return redirect(f"/products/{id}")