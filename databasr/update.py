import mysql.connector

mydb=mysql.connector.connect(user='root',host='localhost',
                             database='Test',password='1234')

mycursor=mydb.cursor()

#sql='Update employee set sal=70000 Where name="naman"'
#mycursor.execute(sql)
#mydb.commit()

sql=mycursor.execute("Update employee set sal=10000 where name='aman'")
mydb.commit()

