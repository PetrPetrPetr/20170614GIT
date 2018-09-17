import sqlite3
print(sqlite3.apilevel)
print(sqlite3.sqlite_version)

con = sqlite3.connect("catalog.db")
cur = con.cursor()

