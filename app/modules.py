#!/usr/bin/env python3
"""Project modules"""

import re
import sqlite3

from config import SECRET_KEY
from hashids import Hashids
from mysql import escape_string
from mysql.connector import Error, connect, errorcode

hashids = Hashids(min_length=3, salt=SECRET_KEY)


class MySql:  # TODO: Not working right now!
    """mysql Db configuration and jobs"""

    def __init__(self, host, username, password, db):
        self.config = {
            "user": username,
            "password": password,
            "host": host,
            "database": db,
            "charset": "utf8",
        }

    def get_database_connection(self):
        """connects to the MySQL database and returns the connection"""
        try:
            return connect(**self.config)
        except Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                raise

    def create_link_table(self):
        """Create DB If Not Exsists"""
        db = self.get_database_connection()

        cur = db.cursor()

        try:
            cur.execute(
                """CREATE TABLE IF NOT EXISTS  urls(
                        id INT AUTO_INCREMENT NOT NULL,
                        primary key (id),
                        original_url TEXT NOT NULL
                        );"""
            )
            db.commit()
        except Exception:
            print("Table creation is having trouble. \n\n")
            raise

    def write(self, orginal_url):
        """write url to TABLE and hash it"""
        db = self.get_database_connection()

        cur = db.cursor()

        try:
            cur.execute(
                f"""INSERT INTO urls (original_url)\
                        VALUES ("{orginal_url}");"""
            )
            db.commit()

            return cur.lastrowid

        except Exception:
            print("Write To table is having trouble. \n")
            raise

    def read(self, url_id):
        """read orgin url from tabale"""

        db = self.get_database_connection()

        cur = db.cursor()
        original_id = hashids.decode(url_id)
        if original_id:
            original_id = original_id[0]
            # try:
            return cur.execute(
                escape_string(
                    f"""SELECT original_url FROM urls where id in ({original_id});"""
                )
            ).fetchone()

            # except Exception as err:
            #    print(f"Write To table is having trouble. \n {err}")


class SqlLitedb:
    """SQLite Db configuration and jobs"""

    def __init__(self, path="database.db"):
        self.path = path

    def create_link_table(self):
        """Create DB If Not Exsists"""

        conn = sqlite3.connect(self.path)

        conn.execute(
            """CREATE TABLE IF NOT EXISTS urls (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                original_url TEXT NOT NULL
                );"""
        )

        conn.commit()
        conn.close()

    def write(self, url):
        """write url to db and hash it"""

        conn = sqlite3.connect(self.path)
        conn.row_factory = sqlite3.Row

        # Write URL data On DB
        url_data = conn.execute(
            "INSERT INTO urls (original_url) \
        VALUES (?)",
            (url,),
        )

        conn.commit()
        conn.close()

        return url_data.lastrowid

    def read(self, url_id):
        """read orgin url from db"""

        conn = sqlite3.connect(self.path)
        conn.row_factory = sqlite3.Row

        original_id = hashids.decode(url_id)
        if original_id:
            original_id = original_id[0]
            url_data = conn.execute(
                "SELECT original_url FROM urls" " WHERE id = (?)", (original_id,)
            ).fetchone()
            original_url = url_data["original_url"]
            conn.close()
            # If valid Id: return origin url
            return original_url
        return None


def is_valid(site_url):
    """Check Is valid Url or Not"""
    # Regex to check valid URL
    regex = (
        "((http|https)://)?(www.)?"
        + "[a-zA-Z0-9@:%._\\+~#?&//=]"
        + "{2,256}\\.[a-z]"
        + "{2,6}\\b([-a-zA-Z0-9@:%"
        + "._\\+~#?&//=]*)"
    )

    clean = re.compile(regex)

    if re.search(clean, site_url):
        return True

    return False
