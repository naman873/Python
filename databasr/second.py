import mysql.connector
from mysql.connector import Error

try:
    connection=mysql.connector.connect(host="localhost",user='root',password='1234',
                                       database='Test')

    if connection.is_connected():
        info=connection.get_server_info()
        print("Server infomation is",info)
        cursor=connection.cursor()
        #cursor.execute("show databases")
        #for db in cursor:
         #   print(db)

        #cursor.execute("select * from hell")
        #res=cursor.fetchone()
        #print(res)

        #cursor.execute("Create table employee(name varchar(200), sal int(20))")
        #cursor.execute("Show tables")
        #for tb in cursor:
         #   print(tb)


except Error as e:
    print("no connection with database please check you credentialas in connection")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("connection closed")