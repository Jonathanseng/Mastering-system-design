# Here's an example Python code for the three-way handshake process using the socket library:

import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the remote host and port
host = 'www.example.com'
port = 80
server_address = (host, port)
sock.connect(server_address)

# Perform the three-way handshake
seq_num = 1000  # random sequence number
sock.send(b'SYN')  # send SYN packet
data = sock.recv(1024)  # receive SYN-ACK packet
if data.startswith(b'SYN-ACK'):
    ack_num = seq_num + 1  # acknowledgment number
    sock.send(b'ACK')  # send ACK packet
    print('Connection established.')
else:
    print('Error: Invalid response received.')

# Close the socket
sock.close()

# In this code, we create a TCP/IP socket and connect it to a remote host and port. We then perform the three-way handshake by sending a SYN packet, receiving a SYN-ACK packet, and sending an ACK packet. Finally, we close the socket.

#Note that this code is just an example and should not be used in production systems without proper error handling and security measures.
