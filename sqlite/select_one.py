import sqlite3
from pprint import pprint

with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute("SELECT * from usuarios")
    pprint(cursor.fetchall())