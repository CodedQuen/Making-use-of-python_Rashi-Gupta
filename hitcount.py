#!/usr/bin/python2.2
import Cookie
import cgi
import os
from random import randint

dynhtml=’’’<HTML><HEAD><TITLE>
Hit Count</TITLE></HEAD>
<HR><CENTER><BODY><H2>You have visited this page %s time(s)</H2>
<p><H3>Your visitor ID is: <b>%s</b></p></H3><CENTER>
<HR>
</BODY></HTML>’’’
def getCookie(initialvalues={}):
    if os.environ.has_key(‘HTTP_COOKIE’):
        C=Cookie.Cookie(os.environ[‘HTTP_COOKIE’])
    else:
        C=Cookie.Cookie()
for eachkey in initialvalues.keys():
        if not C.has_key(eachkey):
            C[eachkey]=initialvalues[eachkey]
        elif C.has_key(‘studid’):
            C[‘studid’]=”S”+str(randint(10,100))
            pass
    return C
if __name__==’__main__’:
    cookie=getCookie({‘counter’:0,’studid’:”S01”})
    cookie[‘counter’]=int(cookie[‘counter’].value)+1
    print (cookie)
    print (“Content-type: text/html\n\n”)
    print (dynhtml %(cookie[‘counter’].value, cookie[‘studid’].value))
