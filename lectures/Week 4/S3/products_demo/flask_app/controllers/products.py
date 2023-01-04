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