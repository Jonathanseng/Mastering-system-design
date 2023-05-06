# Here is an example of a basic Python program that uses UDP sockets to send and receive data:

import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = b"Hello, World!"

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
print("message:", MESSAGE)

# create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send the message
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

# receive a response
data, addr = sock.recvfrom(1024)
print("received message:", data)

# close the socket
sock.close()

# This program sends the message "Hello, World!" to the IP address 127.0.0.1 (which is the loopback address, meaning the data will be sent to the same machine), using port number 5005. It then waits to receive a response and prints the received message. Note that this program assumes there is a server running on the specified IP address and port number that will respond to the message.

# This is just a basic example of using UDP sockets in Python. More complex applications may require additional error checking and handling, as well as the use of libraries or frameworks that simplify network programming.
