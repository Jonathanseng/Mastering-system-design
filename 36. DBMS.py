# To interact with a DBMS in Python, you will typically use a database driver or module specific to the type of database you are using. Here's an example of connecting to a MySQL database using the mysql-connector-python module and executing a simple query:

import mysql.connector

# establish a connection to the database
db = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="databasename"
)

# create a cursor object to execute SQL queries
cursor = db.cursor()

# execute a simple query to retrieve data from a table
query = "SELECT * FROM tablename"
cursor.execute(query)

# iterate over the results and print them
for row in cursor:
    print(row)

# close the cursor and database connections
cursor.close()
db.close()

# Note that this is just a simple example, and working with a DBMS in a production environment will typically involve more complex queries, transactions, and error handling. It's also important to ensure that your code is secure by using parameterized queries, sanitizing input data, and implementing appropriate access control and authentication mechanisms.
