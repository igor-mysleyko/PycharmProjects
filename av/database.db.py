import sqlite3

conn= sqlite3.connect("mydata.db")
sql="CREATE TABLE IF NOT EXISTS books (url TEXT, data TEXT,title TEXT, cost TEXT )"
cursor= conn.cursor()

cursor.execute(sql)
conn.close()