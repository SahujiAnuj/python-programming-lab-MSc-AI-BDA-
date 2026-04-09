# 14_mysql_delete.py

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="testdb"
)

cursor = conn.cursor()
cursor.execute("DELETE FROM students WHERE id=1")

conn.commit()
print("Record deleted")

conn.close()
