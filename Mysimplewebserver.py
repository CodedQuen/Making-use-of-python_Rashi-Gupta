#!/usr/bin/python2.2
from os import curdir, sep
from BaseHTTPServer import HTTPServer

from SimpleHTTPServer import SimpleHTTPRequestHandler
class req_handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        try:
            f = open(curdir + sep + self.path)
            self.send_response(200)
            self.send_header(‘Content-type’,’text/html’)
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
        except IOError:
            self.send_error(404,’File Not Found: %s’ % self.path)
try:
    server=HTTPServer((‘’,8000),req_handler)
    print (‘Welcome to the My simple web server...’)
    print (‘Press ^C once or twice to quit’)
    server.serve_forever()
except KeyboardInterrupt:
    print (‘^C pressed, shutting down server’)
    server.socket.close()
