#!env/bin/python3
import re
import sqlite3

from flask import Flask, flash, redirect, render_template, request, url_for
from hashids import Hashids


try:
    import .config
except ImportError:
    print("please copy 'config.py.sample' to 'config.py' and add your Mysql Username, password and host to 'config.py'")
    exit(0)

SECRET_KEY = config.SECRET_KEY

def IS_VALID_URL(URL):
    # Regex to check valid URL
    regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")

    # Compile the ReGex
    clean = re.compile(regex)

    # If the string is empty
    # return false
    if URL is None:
        return False

    # Return if the URL
    # matched the ReGex
    if(re.search(clean, URL)):
        return True
    else:
        return False


def create_link_table():
    """Create DB If Not Exsists"""
    conn = sqlite3.connect('database.db')
    conn.execute("""CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            original_url TEXT NOT NULL
            );""")

    conn.commit()
    conn.close()


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

hashids = Hashids(min_length=3, salt=app.config['SECRET_KEY'])


@app.route('/', methods=('GET', 'POST'))
def index():
    """Index Site"""
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row

    if request.method == 'POST':
        url = request.form['url']

        # If user Enter empty Value; Flashing(!) Of the "The URL is required!"
        if not url:
            flash('The URL is required!')
            return redirect(url_for('index'))

        if "http" not in url:
            url = "http://"+url
        if not IS_VALID_URL(url):
            flash('The URL is Not Valid!')
            return redirect(url_for('index'))

        url_data = conn.execute('INSERT INTO urls (original_url) VALUES (?)',
                                (url,))  # Write URL data On DB
        conn.commit()
        conn.close()

        url_id = url_data.lastrowid
        hashid = hashids.encode(url_id)
        short_url = request.host_url + hashid

        return render_template('index.html', short_url=short_url)

    return render_template('index.html')


@app.route('/<id>')
def url_redirect(id):
    """redirected "mozLink!" URL to orginal Url"""
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row

    original_id = hashids.decode(id)
    if original_id:
        original_id = original_id[0]
        url_data = conn.execute('SELECT original_url FROM urls'
                                ' WHERE id = (?)', (original_id,)
                                ).fetchone()
        original_url = url_data['original_url']
        conn.close()
        # If valid Id: return origin url example: moz.ln/abcd > https://google.com
        return redirect(original_url)
    else:
        flash('Invalid URL')  # If Not valid Id: return index site
        return redirect(url_for('index'))


if __name__ == "__main__":
    create_link_table()
    app.run("0.0.0.0", 5000, debug=False)
