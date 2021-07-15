#!/usr/bin/env python3
"""Project configuration"""
import random


def get_random_string(length):
    """Get random str"""
    letters = """abcdefghijklmnopqrstuvwxyz\
    ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789\
    ~`!@#$%^&*()-_=+|}]{["':;?/>.<, """
    result_str = "".join(random.choice(letters) for i in range(length))
    return result_str


SECRET_KEY = get_random_string(60)
SQL = "mysql"
USERNAME = ""

if SQL == "mysql":
    # MYSQL Username, password and host
    HOST = "your MySql server Ip or Domain"
    DB = "tabale name"
    USERNAME = "Your Mysql's Username"
    PASSWORD = "Your MySql user's password "


if not USERNAME:
    print("If you want to use Mysql:")
    print("please apply your settings under the comfig.py ")
    print(
        "file and then run the program again,\
    \b\b\b\notherwise no action is required."
    )
