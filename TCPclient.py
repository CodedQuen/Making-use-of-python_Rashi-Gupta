from socket import *

Hostname = ‘localhost’
PortNumber = 12345
Buffer = 500
ServerAddress = (Hostname, PortNumber)

TCP_Client_Socket = socket(AF_INET, SOCK_STREAM)
TCP_Client_Socket.connect(ServerAddress)

    while 1:
         print (‘The client is connected to the server’)
         DataStr = raw_input(‘Enter data to send to the server: ‘)
         if not DataStr:
             print (‘The client has entered nothing; hence the)
        connection to the server is closed’
             break
         TCP_Client_Socket.send(DataStr)
         ServerData = TCP_Client_Socket.recv(Buffer)
         if not ServerData:
             print (‘The server has sent nothing’)
             break
         print (‘The server has sent this data string: ‘, ServerData)
 TCP_Client_Socket.close()
