#!env/bin/python3
import sqlite3

from flask import Flask, flash, redirect, render_template, request, url_for
from hashids import Hashids

try:
    import config
except ImportError:
    print("\033[31m\033[01mConfiguration file not found\033[0m \
    \nPlease copy config.py.sample to config.py and\
    \b\b\brun the program again.")
    exit(1)


def IS_VALID_URL(URL):  # CHECK URL Is Valid Or no
    URL = URL.split("//")
    if "http" in URL[0]:
        Domain = URL[1].split("/")[0]
        if '.' in Domain:
            return True
        else:
            False
    else:
        Domain = URL[0].split("/")[0]
        if '.' in Domain:
            return True
        else:
            False


def create_link_table():
    """Create DB If Not Exsists"""
    conn = sqlite3.connect('database.db')
    conn.execute("""CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            original_url TEXT NOT NULL,
            clicks INTEGER NOT NULL DEFAULT 0);""")

    conn.commit()
    conn.close()


app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY

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

        if "http" not in url:  # Add http to URL if "http" not in Url
            if IS_VALID_URL(url) == False:
                flash('The URL is Not Valid!')
                return redirect(url_for('index'))
            elif IS_VALID_URL(url) == None:
                flash('The URL Not Valid!')
                return redirect(url_for('index'))
            else:
                url = "http://" + url

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
        url_data = conn.execute('SELECT original_url, clicks FROM urls'
                                ' WHERE id = (?)', (original_id,)
                                ).fetchone()
        original_url = url_data['original_url']
        clicks = url_data['clicks']

        conn.execute('UPDATE urls SET clicks = ? WHERE id = ?',
                     (clicks+1, original_id))

        conn.commit()
        conn.close()
        # If valid Id: return origin url example: moz.ln/abcd > https://google.com
        return redirect(original_url)
    else:
        flash('Invalid URL')  # If Not valid Id: return index site
        return redirect(url_for('index'))


if __name__ == "__main__":
    create_link_table()
    app.run("0.0.0.0", 5000, debug=False)
