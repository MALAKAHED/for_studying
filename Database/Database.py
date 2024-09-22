import mysql.connector

# Connect to MySQL server
connection = mysql.connector.connect(
    host='localhost',
    user='yourusername',
    password='yourpassword'
)

# Create a cursor object to interact with the server
cursor = connection.cursor()

# Create a new database
cursor.execute("CREATE DATABASE IF NOT EXISTS example_db")

# Connect to the new database
connection.database = 'example_db'

# Create a new table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL
)
''')

# Commit the changes and close the connection
connection.commit()
connection.close()