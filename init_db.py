import sqlite3

def initialize_db():
    conn = sqlite3.connect("database/jobs.db")
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS comments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        message TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    """)
    conn.commit()
    conn.close()
    print("Comments table created successfully.")

if __name__ == "__main__":
    initialize_db()
