#server program
from socket import *
from time import sleep,time,ctime
import threading
ServerData=[]
Hostname = ‘’
PortNumber = 12345
Buffer = 500
ServerAddress = (Hostname, PortNumber)
#Create server socket
TCP_Server_Socket = socket(AF_INET, SOCK_STREAM)
TCP_Server_Socket.bind(ServerAddress)
TCP_Server_Socket.listen(4)
print (‘Server is waiting for connection’)
add=[]

class MyThread(threading.Thread):
    def run(self):
        while 1:
            TCP_Client_Socket, ClientAddress =\
                TCP_Server_Socket.accept()
            print (‘Server has accepted the connection request from ‘,\
                            ClientAddress)
            if ServerData:
                for i in range(len(ServerData)):
                    TCP_Client_Socket.send(str(ServerData[i]))
                    sleep(0.01)
            else:
                    TCP_Client_Socket.send(“Hi”)
            print (‘The Server is ready to receive data from \
                                the client’
            while 1:
                ClientData = TCP_Client_Socket.recv(Buffer)
                if not ClientData:
                    print (‘The client has closed the connection’)
                    break
                    print (‘The %s has sent this data string: %s’\
                                    % (ClientAddress,ClientData)
                    ClientData=ClientData+’~~’
#Collect the data sent by all clients in ServerData
                    ServerData.append(ClientData)
#send the data collected in ServerData
                    for i in range(len(ServerData)):
                        TCP_Client_Socket.send(str(ServerData[i]))
                        sleep(0.01)
                print (‘The Server is ready to receive more data from\
                                        the client’)
                TCP_Client_Socket.close()
                break
            TCP_Server_Socket.close()
ch=0
while ch<=3:
#Create four threads for four clients
    NewThreadObject = MyThread()
    NewThreadObject.start()
    threadarray.append(NewThreadObject)
    ch=ch+1
