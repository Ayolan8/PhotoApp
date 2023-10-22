import mysql.connector

dataBase = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'Afolabi@oredola18'

        )

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE ayolan")

print("all set!")
