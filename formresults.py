#!/usr/local/bin/python
import cgi
header= “Content-Type: text/html\n\n”
formhtml=’’’<HTML>
<HEAD>
<TITLE>Login Page</TITLE>
</HEAD>
<BODY>
<HR><CENTER>
<FORM method=”POST” action=”http://localhost/cgi-bin/formresults1.py”>
<p>Login Name:<input type=”text” name=”login” value=””></p>
<p>Password: <input type=”password” name=”password” value=””></p>
<p><input type=”submit” value=”Submit”>
<input type=”reset” value=”Reset”></p>
</FORM>
</CENTER>
<HR>
</BODY>
</HTML>’’’
def show_form():
    print (header+formhtml)
dynhtml=’’’<HTML><HEAD><TITLE>
%s </TITLE></HEAD>
<BODY><CENTER><HR><H2> %s </H2> <H3> %s </H3><HR></CENTER>
</BODY></HTML>’’’
fs = cgi.FieldStorage()
passd=”password”
if not fs:
    show_form()
elif fs.has_key(‘login’) and (fs[‘login’].value!=””):
    if fs.has_key(‘password’):
            Ch=0
            fpass=fs[‘password’].value
            if fpass==passd:
                abc=”Connected”
                message=”Welcome...\n”
            else:
                abc=”Not connected”
                message=”Wrong password”
    else:
        abc=”Not connected”
        message=”Password not entered for”
    print header+dynhtml % (abc,message,fs[‘login’].value)
else:
    pass
