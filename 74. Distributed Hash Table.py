
import hashlib
import socket

class DHTNode:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.data = {}
        self.finger_table = [None] * 8
        self.predecessor = None
    
    def join(self, existing_node):
        self.predecessor = None
        existing_node.find_successor(self.hash_key(), self)
    
    def find_successor(self, key, requester):
        if self.predecessor is None or self.in_range(self.predecessor.hash_key(), self.hash_key(), key):
            requester.notify(self.finger_table[0])
        else:
            node = self.closest_preceding_node(key)
            node.find_successor(key, requester)
    
    def closest_preceding_node(self, key):
        for i in range(7, -1, -1):
            if self.finger_table[i] is not None and self.in_range(self.hash_key(), key, self.finger_table[i].hash_key()):
                return self.finger_table[i]
        return self
    
    def notify(self, node):
        if self.predecessor is None or self.in_range(self.predecessor.hash_key(), self.hash_key(), node.hash_key()):
            self.predecessor = node
    
    def in_range(self, start, end, key):
        if start == end:
            return True
        elif start < end:
            return start <= key < end
        else:
            return start <= key or key < end
    
    def hash_key(self, key):
        sha1 = hashlib.sha1()
        sha1.update(key.encode())
        return int(sha1.hexdigest(), 16) % 2**8

class DHT:
    def __init__(self, ip, port):
        self.node = DHTNode(ip, port)
        self.node.finger_table = [self.node] * 8
    
    def listen(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.node.ip, self.node.port))
        server_socket.listen(1)
        while True:
            client_socket, address = server_socket.accept()
            request = client_socket.recv(1024).decode()
            response = self.handle_request(request)
            client_socket.sendall(response.encode())
            client_socket.close()
    
    def handle_request(self, request):
        request_parts = request.split(' ')
        command = request_parts[0]
        key = request_parts[1]
        if command == 'PUT':
            value = request_parts[2]
            self.put(key, value)
            return 'OK'
        elif command == 'GET':
            value = self.get(key)
            return value if value is not None else 'NOT FOUND'
    
    def put(self, key, value):
        node = self.node.find_successor(self.node.hash_key(key), self.node)
        node.data[key] = value
    
    def get(self, key):
        node = self.node.find_successor(self.node.hash_key(key), self.node)
        return node.data.get(key, None)

# This implementation uses a simplified version of the Chord protocol to create a distributed hash table. The DHTNode class represents a single node in the hash table, and the DHT class represents the entire table. Each node keeps track of its own data as well as a finger table containing references to other nodes in the network. When a node receives a request to store or retrieve data, it first finds the node responsible for that key by performing a search through
