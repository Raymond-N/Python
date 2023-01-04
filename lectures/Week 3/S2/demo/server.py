from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

if __name__ == "__main__":
    # ON WINDOWS its running on 5000 by default
    # app.run(debug=True)
    app.run(debug=True,port=8000)