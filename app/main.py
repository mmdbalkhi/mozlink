#!env/bin/python3
"""this app power by flask
with this web app make short link!"""
import config
from flask import flash
from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from models import db
from models import hashids
from models import Urls

app = Flask(__name__)
app.secret_key = config.SECRET_KEY

app.config["SQLALCHEMY_DATABASE_URI"] = config.DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.TRACK_MODIFICATIONS

with app.app_context():
    db.init_app(app)
    db.create_all()

url = Urls()


@app.route("/about")
def about_page():
    """about page"""
    return render_template("about.html")


@app.route("/", methods=("GET", "POST"))
def index():
    """cryptography url and write url and
    crypto url to db, if url is none, app return error user"""

    if request.method == "POST":
        url = request.form["url"]

        # If user Enter empty Value; Flashing(!) Of the "The URL is required!"
        if not url:
            flash("The URL is required!")
            return render_template("index.html"), 405

        url_id = Urls(original_url=Urls.normalise_url(url)).save()
        short_url = request.host_url + hashids.encode(url_id)

        return render_template("index.html", short_url=short_url)

    return render_template("index.html")


@app.route("/<url_id>")
def url_redirect(url_id):
    """redirected "mozLink!" URL to orginal Url"""
    original_url = url.get(id=url_id)
    if original_url:
        return redirect(original_url.original_url)

    flash("Invalid URL")
    return render_template("index.html"), 404


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=False)
