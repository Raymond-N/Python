from flask import Flask,render_template,request,redirect,session
import category
app = Flask(__name__)
app.secret_key = "supersecret"
@app.route("/")
def index():
    categories = category.Category.get_all_categories()
    return render_template("index.html",categories=categories)

@app.route("/add-category",methods=["post"])
def add_category():
    category.Category.create_category(request.form)
    return redirect("/")

if __name__== "__main__":
    app.run(debug=True,port=8000)