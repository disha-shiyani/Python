import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='')
print(mydb)

create database
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='')
mycursor=mydb.cursor()
mycursor.execute('CREATE DATABASE data')

import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='')
mycursor=mydb.cursor()
mycursor.execute('show databases')
for i in mycursor:
	print(i)

import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='',database='data')
mycursor=mydb.cursor()
mycursor.execute('create table pro_info(pro_id int,pro_name varchar(25))')

import mysql.connector

try:
	mydb=mysql.connector.connect(host='localhost',user='root',password='',database='data')
	my_insert_query='insert into pro_info(pro_id,pro_name) values (%s,%s)'
	records_to_insert=[(1,'pen'),(2,'colors')]
	cursor=mydb.cursor()
	cursor.executemany(my_insert_query,records_to_insert)
	mydb.commit()
	print('Records inserted successfully....')
except mysql.connector.Error as error:
	print('Connection is not created...')
finally:
	if mydb.is_connected():
		cursor.close()
		mydb.close()
		print('Connection closed successfully..')


import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',password='',database='data')
mycursor=mydb.cursor()
mycursor.execute('select *from pro_info')
result=mycursor.fetchall()
for i in result:
	print(i)

import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',password='',database='data')
mycursor=mydb.cursor()
mycursor.execute('update pro_info set pro_name="book" where pro_id=2')

import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',password='',database='data')
mycursor=mydb.cursor()
mycursor.execute('delete from pro_info where pro_id=1')
