from socket import *        #Imports the attributes of the socket module
Hostname = ‘172.17.68.120’      #Defines the IP address of the server
#(IT Department computer). Uses the host name/IP address of the
#computer on which you are executing the server
PortNumber = 22222      #Defines the dedicated port number of the server

Buffer = 1024       #Defines the maximum size of data that can be
exchanged
ServerAddress = (Hostname, PortNumber)   #Defines the address of server
Client_Socket=socket(AF_INET, SOCK_STREAM)      #Creates a stream
#socket for the client
Client_Socket.connect(ServerAddress)        #Connects to the server
#at a given address
print
print (‘The client is connected to the server at’, ServerAddress)
print
while 1:
    DataToServer = raw_input(‘Enter data: ‘)        #Asks input for data
    if not Data:        #Checks if the variable is blank
        print
        print (‘********************************************’)
        print (‘**        You have entered nothing        **’)
        print (‘** The connection to the server is closed **’)
        print (‘********************************************’)
        print
        break
    Client_Socket.send(DataToServer)        #Sends data to server
    ServerData=Client_Socket.recv(Buffer)    #Receives data from client
    if not ServerData:      #Checks if the variable is blank
        print
        print (‘The server has ended the connection’)
        break
        print (‘~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~’)
        print (‘Message from the server:’, ServerData)
        print (‘~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~’)
        print
Client_Socket.close()       #Closes the client socket
