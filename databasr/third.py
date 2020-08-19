import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',password='1234',
                             database='Test')

mycursor=mydb.cursor()

#sqlform="Insert  into employee(name,sal) values(%s,%s)"
#employees=[ ("naman", 21) , ("aman", 19) , ("ankita", 20), ]
#mycursor.executemany(sqlform,employees)
#mydb.commit()

mycursor.execute("Insert into employee(name,sal) values('bro',0)")
mydb.commit()