"""Project modules"""

import random
import re
import sqlite3

from hashids import Hashids

try:
    import config
except ImportError:
    print("If you want to use Mysql:")
    print("please apply your settings under the comfig.py ")
    print("file and then run the program again,\
    \b\b\b\notherwise no action is required.")

    with open("./config.py.sample", "r") as config_sample:
        with open("./config.py", "w") as config_orgin:
            config_orgin.write(config_sample.read())

    import config

hashids = Hashids(min_length=3, salt=config.SECRET_KEY)


class mysql:
    pass


class sqlitedb:
    """SQLite Db configuration and jobs
    """

    def __init__(self, path="database.db"):
        self.path = path
    
    
    def create_link_table(self):
        """Create DB If Not Exsists"""
    
        conn = sqlite3.connect(self.path)
    
        conn.execute("""CREATE TABLE IF NOT EXISTS urls (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                original_url TEXT NOT NULL
                );""")
    
        conn.commit()
        conn.close()
    
    
    def write(self, url):
        """ write url to db and hash it"""

        conn = sqlite3.connect(self.path)
        conn.row_factory = sqlite3.Row

        url_data = conn.execute('INSERT INTO urls (original_url) VALUES (?)',
                               (url,))  # Write URL data On DB
        conn.commit()
        conn.close()

        return url_data


    def read(self, id):
        """read orgin url from db"""

        conn = sqlite3.connect(self.path)
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
            return original_id
        return None


def get_random_string(length):
    """Get random str"""
    letters = """abcdefghijklmnopqrstuvwxyzABCDEFG\
    HIJKLMNOPQRSTUVWXYZ0123456789\
    ~`!@#$%^&*()-_=+\|}]{["':;?/>.<, """
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def is_valid(URL):
    """Check Is valid Url or Not"""
    # Regex to check valid URL
    regex = ("((http|https)://)?(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")

    clean = re.compile(regex)
    if(re.search(clean, URL)):
        return True
    
    return False
