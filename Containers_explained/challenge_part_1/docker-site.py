from flask import Flask, request, jsonify, render_template, Response, json

app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit-data", methods=["POST"])
def submit_data():
    data = request.get_json()
    if data and data.get("name") == "admin":
        return Response(json.dumps({"message": "Jarrett{Docker_"}), mimetype="application/json")
    else:
        return Response(json.dumps({"message": "So close!"}), mimetype="application/json")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
