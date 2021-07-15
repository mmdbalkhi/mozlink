#!env/bin/python3
"""this app power by flask
with this web app make short link!"""

from flask import Flask, flash, redirect, render_template, request, url_for

from modules import SECRET_KEY, SqlLitedb, hashids, is_valid

app = Flask(__name__)
sql = SqlLitedb(path="database.db")

sql.create_link_table()
app.secret_key = SECRET_KEY


@app.route('/', methods=('GET', 'POST'))
def index():
    """cryptography url and write url and
    crypto url to db, if url is none, app return error user"""

    if request.method == 'POST':
        url = request.form['url']

        # If user Enter empty Value; Flashing(!) Of the "The URL is required!"
        if not url or not is_valid(url):
            flash('The URL is required!')
            return redirect(url_for('index'))

        if "http" not in url:
            url = "http://"+url

        url_data = sql.write(url)

        url_id = url_data.lastrowid
        short_url = request.host_url + hashids.encode(url_id)

        return render_template('index.html', short_url=short_url), 201

    return render_template('index.html')


@app.route('/<url_id>')
def url_redirect(url_id):
    """redirected "mozLink!" URL to orginal Url"""

    original_url = sql.read(url_id)

    if original_url:
        return redirect(original_url)

    flash('Invalid URL')
    return redirect(url_for('index')), 404


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=False)
