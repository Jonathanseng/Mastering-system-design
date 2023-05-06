
import socket

HOST = 'localhost'  # The server's hostname or IP address
PORT = 8080        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

# This code creates a simple server that listens on port 8080 and echoes back any data received from a client. When a client connects, the server prints a message indicating the connection, and then enters a loop where it waits for data to be received. When data is received, the server sends it back to the client. The connection is closed when the client sends an empty message (i.e., not data).
