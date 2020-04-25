from socket import *    #Imports the attributes of the socket module
Hostname = ‘’       #Defines the host name/IP address of the server.
#The variable is left blank, so that any available address can be used
PortNumber = 22222  #Defines a dedicated port number for the server
Buffer = 1024       #Defines the maximum size of data that can be
exchanged
ServerAddress = (Hostname, PortNumber) #Defines the address of the
server
Server_Socket=socket(AF_INET, SOCK_STREAM)      #Creates a stream
#socket for the server
Server_Socket.bind(ServerAddress)       #Binds the server address to
#the server socket
Server_Socket.listen(5)     #Listens for connections
print
print (‘!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!’)
print (‘Server is waiting for connection’)
print (‘!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!’)
print
while 1:        #Infinite loop starts
    Temp_Socket, ClientAddress = Server_Socket.accept()     #Accepts
client connection and passes it to a new temporary socket
    print (‘Server has accepted the connection request from ‘,)
ClientAddress
    print
    print (‘The server is ready to receive data from the client’)
    print (‘^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^’)
    print
    while 1:        #Client/server connection loop starts

    DataFromClient = Temp_Socket.recv(Buffer)       #Receives data
#from the client
    if not DataFromClient:      #Checks if the variable is blank
        print
        print
        print (‘************************************’)
        print (‘The client has closed the connection’)
        print (‘************************************’)
        print
        print
        print
        print
        print (‘!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!’)
        print (‘Server is waiting for a new connection’)
        print (‘!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!’)
        print
        break       #Client/server connection loop breaks
    WriteToFile=open(‘DataFile’, ‘a’)    #Opens a file in append
                                        #mode
    WriteToFile.write(DataFromClient + ‘\n’)     #Writes data to
                                        #file
    WriteToFile.close()     #Closes the file
    ReadfromFile=open(‘DataFile’,’r’)
    output=ReadfromFile.read()
    Temp_Socket.send(‘DATA \n%s \nWRITTEN TO THE FILE’ % output)
#Sends data to the client
    ReadfromFile.close()
    print
    print (‘~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~’)
    print (‘The server is ready to receive more data from the client’)
    print (‘~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~’)
    Temp_Socket.close()     #Closes the temporary socket
Server_Socket.close()       #Closes the server socket and stops the
#infinite loop
