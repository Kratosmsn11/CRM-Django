# Install MySQL on the machine
# To install SQL on mac use brew install mysql (provided you have homebrew install, no need to update as it will automatically update the homebrew).
# To install the connector : pip install mysql-connector & pip install mysql-connector-python

import mysql.connector

database = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	password = 'password1234'
)

# cursor object
cursorObject = database.cursor()

#create a database
cursorObject.execute("CREATE DATABASE elderco")

print("all good")