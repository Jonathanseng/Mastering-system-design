import sqlite3

# Connect to the database
conn = sqlite3.connect('example.db')

# Create a table
conn.execute('''CREATE TABLE users
             (id INTEGER PRIMARY KEY,
             name TEXT NOT NULL,
             email TEXT NOT NULL,
             password TEXT NOT NULL);''')

# Insert data into the table
conn.execute("INSERT INTO users (id, name, email, password) \
             VALUES (1, 'John Doe', 'johndoe@email.com', 'password123')")

# Retrieve data from the table
cursor = conn.execute("SELECT * FROM users")
for row in cursor:
    print(row)

# Commit changes and close the connection
conn.commit()
conn.close()

# 
Here's an example of how to create a relational database using Python and SQLite:

python
Copy code
import sqlite3

# Connect to the database
conn = sqlite3.connect('example.db')

# Create a table
conn.execute('''CREATE TABLE users
             (id INTEGER PRIMARY KEY,
             name TEXT NOT NULL,
             email TEXT NOT NULL,
             password TEXT NOT NULL);''')

# Insert data into the table
conn.execute("INSERT INTO users (id, name, email, password) \
             VALUES (1, 'John Doe', 'johndoe@email.com', 'password123')")

# Retrieve data from the table
cursor = conn.execute("SELECT * FROM users")
for row in cursor:
    print(row)

# Commit changes and close the connection
conn.commit()
conn.close()

#In this example, we first connect to the database using the sqlite3.connect() method and create a new table called "users" with four columns (id, name, email, and password). We then insert a single row of data into the table using the conn.execute() method.

#Next, we retrieve the data from the "users" table using a SELECT statement and print it to the console using a for loop.

#Finally, we commit our changes to the database using the conn.commit() method and close the connection using the conn.close() method.

#Note that this is a very basic example, and there are many other operations you can perform on a relational database using Python, such as updating data, deleting data, and creating more complex queries.




