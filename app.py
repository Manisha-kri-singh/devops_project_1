from flask import Flask

app = Flask(_name_)

@app.route("/info")
def lwinfo():
    return "I am LW from India"

@app.route("/phone")
def lwphone():
    return "910000000000"

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)