#!/usr/bin/python2.2
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
dynhtml=”””
<HTML><HEAD><TITLE>My Home Page</TITLE></HEAD>
<BR><BR><BR><BR><BR><BR><HR>
<BODY><CENTER><H1><U>Hello client!</U></H1>
<H2>You are connected to Mywebserver</H2><HR></BODY>
</HTML>”””
nf=”File not found”
class req_handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path==”/”:
            self.send_response(200)
            self.send_header(‘Content-type’,’text/html’)
            self.end_headers()
            self.wfile.write(dynhtml)
        else:
            self.send_error(404,nf)
try:
    server=HTTPServer((‘’,8000),req_handler)
    print (‘Welcome to the Mywebserver...’)
    print (‘Press ^C once or twice to quit’)
    server.serve_forever()
except KeyboardInterrupt:
        print (‘^C pressed, shutting down server’)
        server.socket.close()
