from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "supersecret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process",methods=["POST"])
def create_user():
    print("Got Post Info")
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect("/result")

@app.route("/result")
def show_user():
    return render_template("results.html")

if __name__ =="__main__":
    app.run(debug=True,port=8000)