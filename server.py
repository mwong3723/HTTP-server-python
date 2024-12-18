import socket
import sys

#create socket
serverSoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# when creating a socket its args are for family address and socket type
# AF_INET refers to the family address which is IPv4
# SOCK_STREAM refers to the socket type for TCP (Transmission Protocol) used for communinication in the network


#socName = socket.gethostname()
#print(f"{socName}")
# 'Matthews-MacBook-Pro.local'


serverAddress = ('localhost', 10000)
#print(f"{serverAddress}")

# using 'localhost' vs socket.gethostname(). Using 'localhost' creates a server only visble within the same machine
# socket.gethostname() creates a server visable to the outside world

serverSoc.bind(serverAddress)

serverSoc.listen(1)
# The arg in listen() is the number of connections we should queue up
# As its called our serverSoc is a listenign socket taht listens for a connection fro mout client


while True:
    (clientSoc, clientAdress) = serverSoc.accept()
    try:
        print("Connected to " , clientAdress)

        # Loop until we are done communicating 
        while True:
            data = clientSoc.recv(16)
            # .recv() and .send() are methods used to send and receive messages between sockets
            print("".format(data))
            if data:
                clientSoc.sendall(data)
            else:
                print('No data from ', clientAdress)
                break;
    finally:
        clientSoc.close()

