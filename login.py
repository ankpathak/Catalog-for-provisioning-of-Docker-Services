#!/usr/bin/python
import cgi, cgitb
import MySQLdb
cgitb.enable()
print "Content-type:text/html\r\n\r\n"
db = MySQLdb.connect("localhost","root","Cascaders1@3","Minor")
form = cgi.FieldStorage()
username = form.getvalue('username')
password = form.getvalue('password')
cursor = db.cursor()
sql='select password from LOGIN where username="'+username+'"'
try:
#Execute the SQL command
  	cursor.execute(sql)
	results = cursor.fetchone()
	pasw = results[0]
	if password == pasw:
		print "Login Successful"
	else:
		print "Invalid username or password"
except:
	print "Error: Database Error"
#disconnect from server
db.close()
