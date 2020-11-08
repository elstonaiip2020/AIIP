from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "Hello World"


@app.route("/get_json")
def get_json():
    return {"msg": "Hello World"}


app.run(debug=True)
