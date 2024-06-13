import sqlite3
cnt=sqlite3.connect('mydb.dp')

cnt.execute('CREATE TABLE stud_info(s_id int,s_name varchar)')
print('table created..')

cnt.execute(""" Insert into stud_info(s_id,s_name)VALUES(1,'shk'),(2,'sdg')""")
print('record is inserted...')
cnt.commit()

cursor=cnt.execute('SELECT *from stud_info')
for i in cursor:
	print(i)

upd_sql="""UPDATE stud_info set s_name='isha' where s_id=2"""
cnt.execute(upd_sql)
cursor=cnt.execute('SELECT *from stud_info')
for i in cursor:
	print(i)

delete_sql="""DELETE from stud_info where s_id=1"""
cnt.execute(delete_sql)
cursor=cnt.execute('SELECT *from stud_info')
for i in cursor:
	print(i)
