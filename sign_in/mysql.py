import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="navin", password='1234')

mycursor = mydb.cursor()

mycursor.execute("showdatabases")

for i in mycursor:
    print(i)