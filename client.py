import socket
import sys

#create socket
clientSoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# when creating a socket its args are for family address and socket type
# AF_INET refers to the family address which is IPv4
# SOCK_STREAM refers to the socket type for TCP (Transmission Protocol) used for communinication in the network


# For the client instead of using bind() to start a server and listen() to listen for a connection we use
# connect() to try and connect to our server
serverAddress = ('localhost', 10000)

clientSoc.connect(serverAddress)
message = input()    
try:
    # Send Data
    clientSoc.sendall(message)

    # Look for response
    amountRecieved = 0
    amountExpected = len(message)

    while amountRecieved < amountExpected:
        data = clientSoc.recv(16)
        amountRecieved += len(data)
        print('recieved {!r}'.format(data))
finally:
    clientSoc.close()
    

    