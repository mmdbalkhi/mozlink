#!env/bin/python3
from flask import Flask, flash, redirect, render_template, request, url_for

from .modulus import is_valid, sqlitedb

app = Flask(__name__)
sql = sqlitedb(path="database.db")

@app.route('/', methods=('GET', 'POST'))
def index():
    """cryptography url and write url and
    crypto url to db, if url is none, app return error to user"""
   
    if request.method == 'POST':
        url = request.form['url']

        # If user Enter empty Value; Flashing(!) Of the "The URL is required!"
        if not url or not is_valid(url)
            flash('The URL is required!')
            return redirect(url_for('index')), 400

        if "http" not in url:
            url = "http://"+url
        
        url_data = sql.write(url)

        url_id = url_data.lastrowid
        short_url = request.host_url + hashids.encode(url_id)

        return render_template('index.html', short_url=short_url), 201

    return render_template('index.html')


@app.route('/<id>')
def url_redirect(id):
    """redirected "mozLink!" URL to orginal Url"""

    orginal_url = sql.load(id)
    
    if original_url:
        return redirect(original_url)
    
    flash('Invalid URL')
    return redirect(url_for('index')), 404


if __name__ == "__main__":
    sql.create_link_table()
    app.run("0.0.0.0", 5000, debug=False)
