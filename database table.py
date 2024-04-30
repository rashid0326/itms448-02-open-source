import sqlite3

# Connect to SQLite database (create a new one if not exists)
conn = sqlite3.connect('crm_database.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table to store customer information
cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE,
        phone TEXT,
        address TEXT
    )
''')

# Commit changes and close the connection
conn.commit()
conn.close()
