import mysql.connector

mydb=mysql.connector.connect(user='root',host='localhost',database='Test',
                             password='1234')

mycursor=mydb.cursor()

mycursor.execute("Select * from employee")

#myresult=mycursor.fetchall()  ## it will fetch all data in one go
#print(myresult)

myresult=mycursor.fetchone()  ## it will fetch one data at a time

#for row in myresult:
print(myresult)