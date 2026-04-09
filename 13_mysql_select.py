# 13_mysql_select.py

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="testdb"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM students")

for row in cursor.fetchall():
    print(row)

conn.close()
