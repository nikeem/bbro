#сброс проекта

import sys
import sqlite3

con = sqlite3.connect('test.db')

with con:
    cur = con.cursor()
    cur.execute("DELETE FROM Projs WHERE ProjId = 8")