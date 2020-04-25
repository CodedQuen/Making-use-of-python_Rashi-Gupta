# Client program
from socket import *
from time import sleep
Hostname = ‘localhost’
PortNumber = 12345
Buffer = 500
#Establish connection with the server
ServerAddress = (Hostname, PortNumber)
TCP_Client_Socket = socket(AF_INET, SOCK_STREAM)
TCP_Client_Socket.connect(ServerAddress)

while 1:
    print (‘The client is connected to the server’)
    ServerData = TCP_Client_Socket.recv(Buffer)
    if not ServerData:
        print (‘The server has sent nothing’)
        break
    else:
#process data received
        ServerStr=str(ServerData)
        if ServerStr.find(‘~~’)!=-1:
            ServerList=ServerStr.split(‘~~’)
        for i in range(len(ServerList)):
            print (ServerList[i])
    else:
        print (ServerStr)
DataStr = raw_input(‘Enter data to broadcast: ‘)
if not DataStr:
    print (‘The client has entered nothing; hence the connection\
to the server is closed’)
    break
#send data
    TCP_Client_Socket.send(DataStr)
    sleep(0.1)
#receive data from server
TCP_Client_Socket.close()
