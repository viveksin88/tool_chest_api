import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",('First Post', 'Content for the first post'))

cur.execute("INSERT INTO transaction_type (name) VALUES (?)",['luxury'])

cur.execute("INSERT INTO transaction_type (name) VALUES (?)",['eating_out'])

cur.execute("INSERT INTO transaction_type (name) VALUES (?)",['groceries'])

cur.execute("INSERT INTO transaction_type (name) VALUES (?)",['gas'])

cur.execute("INSERT INTO transactions (name, amount, transaction_type) VALUES (?, ?, ?)",('First transaction', 23.1, 'gas'))

cur.execute("INSERT INTO transactions (name, amount, transaction_type) VALUES (?, ?, ?)",('First transaction', 1.0, 'luxury'))

cur.execute("INSERT INTO transactions (name, amount, transaction_type) VALUES (?, ?, ?)",('First transaction', 24, 'eatingOut'))
cur.execute("INSERT INTO transactions (name, amount, transaction_type) VALUES (?, ?, ?)",('First transaction', 25, 'groceries'))

connection.commit()
connection.close()