import flask
from flask import jsonify

app = flask.Flask(__name__)

@app.route("/")
def index():
    return jsonify(message = "Working docker example")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
