import mysql.connector

db=mysql.connector.connect(host='localhost',user='root',database='test',
                           password='1234')

mycursor=db.cursor()

#mycursor.execute('select * from hell')
#mycursor.execute('insert into hell(name,age,id) values("pro",11,9)')
#mycursor.execute('delete from hell where name="pro"')
#db.commit()


## Joins
# Inner
#mycursor.execute('select hell.name,employee.sal from employee join hell on employee.name=hell.name')

#left outer Join
#mycursor.execute('select hell.name,employee.sal from employee left join hell on employee.name=hell.name')

#right outer Join
#mycursor.execute('select hell.name,employee.sal from employee right join hell on employee.name=hell.name')

#res=mycursor.fetchall()
#print(res)

#mycursor.execute("select name ,count(*) from employee group by sal")

# having and gorup by
mycursor.execute("select name ,count(*) from employee group by sal having count(*)>1")
res=mycursor.fetchall()
print(res)


