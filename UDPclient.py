from socket import *

Hostname=’localhost’
PortNumber=12345
Buffer=500
ServerAddress=(Hostname, PortNumber)

UDP_Client_Socket=socket(AF_INET, SOCK_DGRAM)

while 1:
    DataStr=raw_input(‘Enter data to send to the server: ‘)
    if not DataStr:
        print (‘The user has entered nothing; hence the client)
            socket is closed’
        break
    UDP_Client_Socket.sendto(DataStr, ServerAddress)
    ServerData, ServerAddress = UDP_Client_Socket.recvfrom(Buffer)
    if not ServerData:
        print (‘The server has sent nothing; hence the client)
            socket is closed’
        break
    print (‘The server has sent this data string: ‘, ServerData)
UDP_Client_Socket.close()
