# Server-side code:
import socket

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

# bind the socket to a public host and a port
serversocket.bind((host, 9999))

# become a server socket
serversocket.listen(1)

while True:
    # establish a connection
    clientsocket, address = serversocket.accept()

    print("Got a connection from %s" % str(address))

    msg = 'Thank you for connecting' + "\r\n"
    clientsocket.send(msg.encode('ascii'))
    clientsocket.close()

# Client-side code:
import socket

# create a socket object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

# connection to hostname on the port.
clientsocket.connect((host, 9999))

# receive no more than 1024 bytes
msg = clientsocket.recv(1024)

clientsocket.close()
print(msg.decode('ascii'))


# In this example, the server binds to a host and port and listens for incoming connections. When a client connects, it sends a message back to the client and closes the connection. The client connects to the server, receives the message, and then closes the connection.




