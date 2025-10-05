import sqlite3
from datetime import datetime

DB_NAME = "database.db"

def create_tables():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE,
                    email TEXT,
                    password TEXT
                )''')

    
    c.execute('''CREATE TABLE IF NOT EXISTS operations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    operation_type TEXT,
                    input_path TEXT,
                    output_path TEXT,
                    timestamp TEXT,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                )''')
    conn.commit()
    conn.close()


def register_user(username, email, password):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    
    c.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", 
                  (username, email, password))
    conn.commit()
    
    
    conn.close()
    return True
def validate_user(username, password):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
    user = c.fetchone()
    conn.close()
    if user:
        return user[0]
    else:
        return None

def log_operation(user_id, operation_type, input_path, output_path):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    timestamp = datetime.now().isoformat()
    c.execute('''INSERT INTO operations (user_id, operation_type, input_path, output_path, timestamp)
                 VALUES (?, ?, ?, ?, ?)''', 
                 (user_id, operation_type, input_path, output_path, timestamp))
    conn.commit()
    conn.close()

def get_user_operations(user_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM operations WHERE user_id = ?", (user_id,))
    operations = c.fetchall()
    conn.close()
    return operations

