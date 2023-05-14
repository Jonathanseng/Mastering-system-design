#There are several graph database libraries available for Python, such as Neo4j and NetworkX. Here's an example of using NetworkX to create a graph and perform some basic operations:
import networkx as nx

# Create an empty graph
G = nx.Graph()

# Add nodes to the graph
G.add_node('A')
G.add_node('B')
G.add_node('C')

# Add edges between nodes
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('C', 'A')

# Get the number of nodes and edges in the graph
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()

# Get the neighbors of a node
neighbors = list(G.neighbors('A'))

# Get the shortest path between two nodes
shortest_path = nx.shortest_path(G, 'A', 'C')

# Print the graph properties and results
print("Number of nodes: ", num_nodes)
print("Number of edges: ", num_edges)
print("Neighbors of A: ", neighbors)
print("Shortest path between A and C: ", shortest_path)



# This code uses the NetworkX library to create a graph, add nodes and edges to the graph, and perform some basic operations such as getting the number of nodes and edges, getting the neighbors of a node, and finding the shortest path between two nodes.

# Note that this is a very basic example and is not intended for production use. In real-world applications, you would typically use a dedicated graph database system like Neo4j, which provides more advanced features such as data persistence, query optimization, and distributed processing.
