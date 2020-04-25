#!/usr/local/bin/python
import cgi
header= “Content-Type: text/html\n\n”
dynhtml=’’’<HTML><HEAD><TITLE>
%s </TITLE></HEAD>
<BODY><CENTER><HR><H2> %s </H2> <H3> %s </H3><HR></CENTER>
</BODY></HTML>’’’
fs = cgi.FieldStorage()
passd=”password”
if fs.has_key(‘login’) and (fs[‘login’].value!=””):
    if fs.has_key(‘password’):
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
        print (header+dynhtml % (abc,message,fs[‘login’].value))
else:
    abc=”not connected”
    message=”You have not entered a login name.”
    message2=”Click Back”
    print (header+dynhtml % (abc,message,message2))
