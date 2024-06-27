import sqlite3

with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    usuarios = [
        (2, "chanchito"), 
        (3, "pokemon")
    ]

    cursor.executemany(
        "insert into usuarios values(?, ?)",usuarios,
    )