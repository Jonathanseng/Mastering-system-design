
import socket

host = 'localhost'
port = 8080

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client to the server
client_socket.connect((host, port))

# send a message to the server
message = "Hello, server!"
client_socket.send(message.encode())

# receive a response from the server
response = client_socket.recv(1024)
print(response.decode())

# close the connection
client_socket.close()

# In this example, we first create a socket object using the socket.socket() function, and then connect it to the server using the connect() method. We then send a message to the server using the send() method, and receive a response from the server using the recv() method. Finally, we close the connection using the close() method.

# Note that in this example, we are assuming that the server is running on the same machine as the client, and is listening on port 8080. If the server is running on a different machine, or is listening on a different port, you will need to modify the host and port variables accordingly.
