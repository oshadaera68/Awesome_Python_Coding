import sqlite3

conn = sqlite3.connect('user_db.db')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        email TEXT NOT NULL
    )""")

cursor.execute("""
INSERT INTO users (username, password, name, age, email) VALUES
('user1', 'pass123', 'era boy', 30, 'y9TqG@example.com'),
('user2', 'pass456', 'era', 50, 'era@example.com'),
('user3', 'pass789', 'sara', 30, 'y9TqG@example.com')
""")

conn.commit()
conn.close()
