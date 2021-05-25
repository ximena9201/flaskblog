import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())
    #query means any action to the database in SQL syntax
    #read, create, update or delete  = CRUD  to a database   = query unit
    #HTTP get, post, put, delete     =request 

cur = connection.cursor()
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post') 
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
            )


connection.commit()
connection.close()

