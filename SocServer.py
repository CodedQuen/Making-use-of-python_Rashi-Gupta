import SocketServer
from time import sleep

port=8888
class myR(SocketServer.StreamRequestHandler):
    def handle(self):
        print (“connection from”,self.client_address)
        try:
            self.wfile.write(“SocketServer works!”)
        except IOError:
            print (“Connection from the client “,\
                self.client_address,” closed”)
while 1:
    srvsocket=SocketServer.TCPServer((“”,port),myR)
print (“the socket is listening to the port”, port)
srvsocket.serve_forever()
