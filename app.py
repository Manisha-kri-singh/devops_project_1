from flask import Flask

app = Flask(__name__)

@app.route("/info")
def lwinfo():
    return "I am LW from India"

@app.route("/phone")
def lwphone():
    return "910000000000"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)