# In Python, you can use the socket library to perform DNS lookups and resolve domain names to IP addresses. Here's an example code snippet:

import socket

domain_name = "example.com"

# perform DNS lookup
ip_address = socket.gethostbyname(domain_name)

print(f"The IP address of {domain_name} is {ip_address}")

# In this example, we first define the domain_name variable as the domain name we want to resolve. We then use the socket.gethostbyname() function to perform the DNS lookup and resolve the domain name to an IP address. Finally, we print the IP address using a formatted string.

# Note that this is a simple example and there are more advanced features available in the socket library for working with DNS, such as specifying a specific DNS server to use, setting timeouts, and more.
