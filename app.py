from flask import flask
app = Flask(__name__)
@app.route("/info")
def lwinfo():
     return "i am LW from India"

@app.route("/phone")

def lwphone():
    return "910000000000"
app.route(host="0.0.0.0")