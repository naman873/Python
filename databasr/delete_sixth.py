import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',database='Test',
                             password='1234')

mycursor=mydb.cursor()

mycursor.execute("Delete from employee WHERE name='ankita'")
mydb.commit()







