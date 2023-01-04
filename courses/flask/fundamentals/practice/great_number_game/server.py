from flask import Flask,render_template,session,redirect,request
import random

app = Flask(__name__)

app.secret_key = "supersecret"

@app.route("/")
def index():
    if "num" not in session:
        session["num"] = random.randint(1,100)
    return render_template("index.html")

@app.route("/guess",methods=["post"])
def guess():
    session["guess"] = int(request.form["guess"])
    return redirect("/")

@app.route("/reset",methods=["post"])
def reset():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True,port=8000)