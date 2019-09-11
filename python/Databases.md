
# Databases

Databases are a very useful way for storing structured data.  A lot of the time it probably makes more sense for your program to use a simple database like SQLite than to save things to a text file.
They could be to store information about the players and high scores in a multi player game, or the contacts and messages for a chat application, or 1001 other possibilities. There isn't time or space to give an introduction to databases here – that would require another text of comparable size! What I can do is point you in the right direction if this is something you are going to experiment with.

An excellent tutorial for SQLite in general, and for using it with Python is available at:

* http://www.sqlitetutorial.net/sqlite-python/

I strongly recommend downloading and installing the DB Browser for SQLite. Use this tool to build your database first, and to create some sample records.

* http://sqlitebrowser.org/

The official documents for the SQLite language and for the Python library are available at:

* https://www.sqlite.org/lang.html
* https://docs.python.org/3/library/sqlite3.html

## SQLlite3 demo exercise

The following is a short demonstration that creates a database, inserts a couple of rows, and then reads them back.

```python
import sqlite3

# Connect to the database file
db_filename = "contacts.db"
db = sqlite3.connect(db_filename).cursor()

# Create the table
sql = """CREATE TABLE IF NOT EXISTS contacts (givenName text, familyName text, email text, phone text, dob text);"""
db.execute(sql)

# Add a couple of records
person1 = ("Luke", "Skywalker", "luke@jedi.com", "555 1111", "25/09/1951")
person2 = ("Leia", "Skywalker", "leia@rebels.com", "555 9876", "21/10/1956")
sql = "INSERT INTO contacts (givenName, familyName, email, phone, dob) VALUES (?,?,?,?,?)"
db.execute(sql, person1)
db.execute(sql, person2)

# Read the records
sql = "SELECT * FROM contacts WHERE familyName = ?"
filter = ("Skywalker",) # Note the trailing comma! (reason: type must be tuple)
db.execute(sql, filter)
rows = db.fetchall()
for row in rows:
    print(row)
```

<div class="page"/>

## MySQL

For MySQL, I've been using the pymysql library.

```python
import pymysql
import pymysql.cursors

class Database():

    def __init__(self, name, host="localhost", user="root", password=""):
        self.dbname = name
        self.dbhost = host
        self.dbuser = user
        self.dbpass = password

    def __connect(self):
        return pymysql.connect(
            host=self.dbhost,
            user=self.dbuser,
            password=self.dbpass,
            db=self.dbname,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)

    def execute(self, sql, data):
        # 2nd param must be a tuple, so making it one if it's not
        if not isinstance(data, tuple):
            data = tuple(data,)
        connection = self.__connect()
        try:
            cursor = connection.cursor()
            cursor.execute(sql, data)
            connection.commit()
        finally:
            connection.close()

    def read(self, sql, data):
        # 2nd param must be a tuple, so making it one if it's not
        if not isinstance(data, tuple):
            data = tuple(data,)
        connection = self.__connect()
        response = []
        try:
            cursor = connection.cursor()
            cursor.execute(sql, data)
            connection.commit()
            response = cursor.fetchall()
        finally:
            connection.close()
        return response
```

<div class="page"/>

Then in your main....

```python
from database import Database
# Connect to the database file
db = Database("demo", "localhost", "root", "its-a-secret")

# Create the table
sql = """CREATE TABLE IF NOT EXISTS contacts (givenName varchar(50), familyName varchar(50), email varchar(50), phone varchar(50), dob varchar(50), primary key (email));"""
db.execute(sql)

# Add a couple of records
person1 = ("Luke", "Skywalker", "luke@jedi.com", "555 1111", "25/09/1951")
person2 = ("Leia", "Skywalker", "leia@rebels.com", "555 9876", "21/10/1956")
sql = "INSERT INTO contacts (givenName, familyName, email, phone, dob) VALUES (?,?,?,?,?)"
db.execute(sql, person1)
db.execute(sql, person2)

# Read the records
sql = "SELECT * FROM contacts WHERE familyName = ?"
filter = ("Skywalker",) # Note the trailing comma! (reason: type must be tuple)
rows = db.read(sql, filter)
for row in rows:
    print(row)

```

* https://pypi.python.org/pypi/PyMySQL
* http://pymysql.readthedocs.io/en/latest/
* https://stackoverflow.com/questions/4960048/how-can-i-connect-to-mysql-in-python-3-on-windows
