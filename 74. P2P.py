# Peer-to-peer (P2P) is a decentralized network architecture that allows individual devices to connect and communicate directly with each other, without the need for a central server or intermediary. There are different P2P protocols, and the implementation of P2P communication can vary based on the specific protocol used.
import socket
import threading

# Define the IP address and port to use
HOST = 'localhost'
PORT = 5000

# Initialize a socket object for listening to incoming connections
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

# Define a function to handle incoming connections
def handle_connection(conn, addr):
    print(f"Connected by {addr}")
    while True:
        # Receive data from the client
        data = conn.recv(1024)
        if not data:
            break
        print(f"Received {data.decode('utf-8')} from {addr}")
        
        # Send a response back to the client
        response = f"You said: {data.decode('utf-8')}"
        conn.sendall(response.encode('utf-8'))
    conn.close()
    print(f"Connection closed by {addr}")

# Define a function to initiate connections to other peers
def initiate_connection(ip, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, port))
    while True:
        # Send data to the peer
        message = input("Enter message to send: ")
        client_socket.sendall(message.encode('utf-8'))
        
        # Receive response from the peer
        response = client_socket.recv(1024)
        print(f"Received {response.decode('utf-8')} from {ip}")
    client_socket.close()

# Start a new thread to handle incoming connections
threading.Thread(target=handle_connection, args=(server_socket.accept())).start()

# Initiate connections to other peers
peer1 = threading.Thread(target=initiate_connection, args=('localhost', 5001))
peer2 = threading.Thread(target=initiate_connection, args=('localhost', 5002))
peer1.start()
peer2.start()

# In this example, we first create a socket object for listening to incoming connections on a specified port. When a new connection is established, we start a new thread to handle the communication with that peer. We also initiate connections to other peers by creating new threads that establish a socket connection to the specified IP address and port. Once connected, the threads send and receive data to and from the peer. This creates a P2P network where each peer can communicate directly with each other.
