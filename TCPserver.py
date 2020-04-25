from socket import *

Hostname = ‘’
PortNumber = 12345
Buffer = 500
ServerAddress = (Hostname, PortNumber)
TCP_Server_Socket = socket(AF_INET, SOCK_STREAM)
TCP_Server_Socket.bind(ServerAddress)
TCP_Server_Socket.listen(2)

while 1:
    print (‘Server is waiting for connection’)
    TCP_Client_Socket, ClientAddress = TCP_Server_Socket.accept()
    print (‘Server has accepted the connection request from ‘,)
            ClientAddress
    print (‘The Server is ready to receive data from the client’)

    while 1:
        ClientData = TCP_Client_Socket.recv(Buffer)
        if not ClientData:
            print (‘The client has closed the connection’)
            break
        print (‘The client has sent this data string: ‘,\)
            ClientData
        TCP_Client_Socket.send(‘Hello! Client’)
        print (‘The server is ready to receive more data)
    from the client’
        TCP_Client_Socket.close()

TCP_Server_Socket.close()
