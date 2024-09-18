import pymysql

dataBase = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '123456'
    )

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE dentista")

print("Hecho!")