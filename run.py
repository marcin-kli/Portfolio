import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    data = []
    with open("data/portfolio.json", "r") as json_data:
        data = json.load(json_data)
    return render_template(
        "index.html", page_title="Portfolio", projects=data)


@app.route("/projects", methods=["GET", "POST"])
def projects():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("projects.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
