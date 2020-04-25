#!/usr/local/bin/python
import cgi
import MySQLdb

print (“Content-Type: text/html\n”)
dynhtml=’’’<HTML><HEAD><TITLE>
Personal Details</TITLE></HEAD>
<BODY><HR><H2><center>Personal details for %s</H2>
<p>%s</p>
<HR>
</BODY></HTML>’’’
fs = cgi.FieldStorage()
name = fs[‘studname’].value
dob=fs[‘studdob’].value
add=fs[‘studadd’].value
country=fs[‘studcountry’].value
phone=fs[‘studphone’].value
email=fs[‘emailadd’].value
try:
    connection=MySQLdb.connect(host=”localhost”,db=”Registration”,\
        user=”root”,passwd=”new-password”)
    con=connection.cursor()
    sql_stmt=’insert into regdetails values\
(“%s”,”%s”,”%s”,”%s”,”%s”,”%s”)’ % (name,dob,add,country,phone,email)
    con.execute(sql_stmt)
    message=”Successfully entered in the database”
except:
    message=”Error writing data to the table”
#result_set=con.fetchall()
con.close()
print (dynhtml % (name,message))
