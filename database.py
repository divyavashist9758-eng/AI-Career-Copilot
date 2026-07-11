import sqlite3

conn = sqlite3.connect("career.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    skills TEXT,
    interests TEXT,
    education TEXT
)
""")

conn.commit()