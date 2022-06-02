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
DATABASE_URI = "sqlite:///urls.db"
TRACK_MODIFICATIONS = False
