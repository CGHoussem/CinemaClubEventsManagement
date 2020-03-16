"""
Ce module permettrai de gérer une base de donnée
"""

import sqlite3

conn = None

def open_connection(db_name):
    conn = sqlite3.connect(db_name)

def close_connection():
    if conn != None:
        conn.close()

