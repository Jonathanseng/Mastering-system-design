# Here's an example implementation of the bully algorithm for leader election in Python:

import time
import random
from threading import Thread

class Node:
    def __init__(self, id):
        self.id = id
        self.leader = None
        self.election_in_progress = False
        self.nodes = []

    def set_nodes(self, nodes):
        self.nodes = nodes

    def start_election(self):
        print(f"Node {self.id}: starting election")
        self.election_in_progress = True
        higher_nodes = [node for node in self.nodes if node.id > self.id]
        if higher_nodes:
            for node in higher_nodes:
                response = node.respond_to_election()
                if response == "OK":
                    self.election_in_progress = False
                    return
        self.become_leader()

    def respond_to_election(self):
        if self.leader is not None:
            return "NO"
        else:
            return "OK"

    def become_leader(self):
        print(f"Node {self.id}: I am the new leader")
        self.leader = self.id
        self.election_in_progress = False
        for node in self.nodes:
            if node.id != self.id:
                node.notify_leader(self.id)

    def notify_leader(self, leader_id):
        self.leader = leader_id
        print(f"Node {self.id}: updated leader to {leader_id}")

def run():
    nodes = [Node(i) for i in range(5)]
    for node in nodes:
        node.set_nodes(nodes)

    threads = []
    for node in nodes:
        t = Thread(target=node.start_election)
        t.start()
        threads.append(t)

    time.sleep(2)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    run()

 # In this implementation, we create a Node class to represent each node in the distributed system. Each node has a unique ID, a reference to the current leader, and a list of all the other nodes in the system. The set_nodes method is used to set the list of nodes for each node.

# When a node detects that the current leader has failed or is no longer responding, it calls the start_election method to initiate a leader election process. The node sends an election message to all other nodes with a higher ID. If there are any higher nodes, they respond with an "OK" message, and the election process ends. Otherwise, the node becomes the new leader and notifies all other nodes of its new status.

# In the run function, we create five nodes and start a separate thread for each node to simulate a distributed system. We wait for two seconds before joining all the threads to ensure that the leader election process has completed. The output of the code will show which node has become the leader.

# Note that this implementation is simplified and does not include features such as timeouts and retries, which are typically included in production-ready leader election algorithms to ensure that the leader is elected in a timely and reliable manner.   
    
