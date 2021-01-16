import os
import json
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/projects/")
def projects():
    data = []
    with open("data/portfolio.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("projects.html", page_title="Portf", projects=data)


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
