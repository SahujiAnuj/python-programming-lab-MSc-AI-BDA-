# 15_mysql_query.py

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="testdb"
)

cursor = conn.cursor()
cursor.execute("SELECT name FROM students WHERE marks > 80")

for row in cursor.fetchall():
    print(row)

conn.close()
