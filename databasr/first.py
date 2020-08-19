import mysql.connector
from mysql.connector import Error

try:
    connection=mysql.connector.connect(host='localhost',database='Test',
                                       user='root',password='1234')

    if connection.is_connected():
        db_info=connection.get_server_info()
        print("Connected to Mysql  Server version",db_info)
        cursor=connection.cursor()
        cursor.execute("select database();")
        record=cursor.fetchone()
        print("You're connected to database :",record)

except Error as e:
    print("Error while connecting to sql")
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("mysql connection closed")

