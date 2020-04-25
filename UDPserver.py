from socket import *

Hostname=’’
PortNumber=12345
Buffer=500
ServerAddress=(Hostname, PortNumber)

UDP_Server_Socket=socket(AF_INET, SOCK_DGRAM)
UDP_Server_Socket.bind(ServerAddress)

while 1:
    print (‘The server is ready to receive data from the client’)
    ClientData, ClientAddress = UDP_Server_Socket.recvfrom(Buffer)
    print (‘Server has received data from ‘, ClientAddress)
    print (‘The client has send this data string: ‘, ClientData)
    UDP_Server_Socket.sendto(‘Hello! Client’, ClientAddress)
UDP_Server_Socket.close()
