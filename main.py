import sqlite3

conn = sqlite3.connect('database.db')

cur = conn.cursor()

cur.execute("""
CREATE TABLE Users (
    id INT PRIMARY KEY,
    
)
""")


