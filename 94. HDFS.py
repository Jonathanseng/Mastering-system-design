# To interact with Hadoop Distributed File System (HDFS) in Python, you can use the hdfs library which provides a Python interface to HDFS. Here are the steps to install and use hdfs library to interact with HDFS in Python:

#Install hdfs library:
#You can install the hdfs library using pip command:

pip install hdfs

# Note: You need to have the Hadoop distribution installed and configured on your system before using the hdfs library.
# Import hdfs library:
from hdfs import InsecureClient

#Create an InsecureClient object:
client = InsecureClient('http://<namenode_host>:<namenode_port>', user='<username>')

# Note: Replace <namenode_host>, <namenode_port> and <username> with the appropriate values for your Hadoop cluster.
# Use the client object to interact with HDFS:
# Here are some examples of using the client object to interact with HDFS:
# Create a new file:

client.write('/path/to/new_file.txt', 'Hello, World!')

# Read a file:

with client.read('/path/to/file.txt', encoding='utf-8') as reader:
    for line in reader:
        print(line)


# Create a new directory:
client.makedirs('/path/to/new_directory')


#List a directory:
contents = client.list('/path/to/directory')
print(contents)


# Rename a file or directory:
client.rename('/path/to/old_name', '/path/to/new_name')


# Delete a file or directory:
client.delete('/path/to/file_or_directory')

# These are some of the basic operations that you can perform using the hdfs library to interact with HDFS in Python.
