import mysql.connector

conn=mysql.connector.connect(host='localhost',username='root',password='Meet@#0000',database='connection1')
my_cursor=conn.cursor()

conn.commit()
conn.close()
print("connection succesfullycreated!")