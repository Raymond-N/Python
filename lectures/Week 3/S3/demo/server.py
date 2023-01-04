from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def index():
    all_users = [
{"name":"John","email":"j@j.com"},
{"name":"Kevin","email":"k@k.com"},
{"name":"Alex","email":"a@a.com"}
]
    return render_template("index.html",name="Test",users= all_users)

if __name__ == "__main__":
    app.run(debug=True,port=8000)