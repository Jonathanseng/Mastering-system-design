# Scalability is a concept that applies to the design and architecture of software systems, rather than to specific lines of code. However, here is an example of how you might use Python to implement a horizontally scalable web application using the Flask framework:

from flask import Flask, request

app = Flask(__name__)

# Define a route for the web application
@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    # Start the Flask web server on port 5000
    app.run(port=5000)

    
# This is a simple Flask web application that listens on port 5000 and returns the message "Hello, World!" when a user visits the root URL ("/"). To make this application horizontally scalable, you could deploy it on multiple servers and use a load balancer to distribute incoming requests across the servers.

# To demonstrate this, you could deploy the above code on two servers with IP addresses 192.168.1.10 and 192.168.1.11. Then, you could configure a load balancer to distribute incoming requests between the two servers. Here is an example of how you might use the haproxy load balancer to achieve this:    

frontend http
    bind *:80
    mode http
    default_backend app_servers

backend app_servers
    balance roundrobin
    server app1 192.168.1.10:5000 check
    server app2 192.168.1.11:5000 check

# This configuration file tells haproxy to listen on port 80 and distribute incoming requests to the two servers at IP addresses 192.168.1.10 and 192.168.1.11. The balance roundrobin line tells haproxy to distribute requests evenly between the servers using a round-robin algorithm.

# By deploying the Flask application on multiple servers and using a load balancer to distribute incoming requests, you have created a horizontally scalable web application that can handle an increased workload by adding more servers to the cluster.      
