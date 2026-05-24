import sqlite3
import os
import shutil

DATABASE = 'database.db'
BACKUP = 'database_backup.db'

def reset_database():
    print("Backing up old database...")
    if os.path.exists(DATABASE):
        shutil.copy2(DATABASE, BACKUP)
        print(f"Backup saved as {BACKUP}")
        os.remove(DATABASE)
        print("Old database removed.")
    
    print("\nCreating new database...")
    
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    
    c.execute('''
        CREATE TABLE users
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
         username TEXT UNIQUE NOT NULL,
         password TEXT NOT NULL,
         role TEXT DEFAULT 'user',
         full_name TEXT,
         email TEXT,
         created_at TEXT DEFAULT CURRENT_TIMESTAMP)
    ''')
    
    c.execute('''
        CREATE TABLE access_logs
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
         timestamp TEXT NOT NULL,
         username TEXT,
         action TEXT NOT NULL,
         status TEXT NOT NULL,
         details TEXT)
    ''')
    
    c.execute('''
        CREATE TABLE attendance
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
         username TEXT NOT NULL,
         date TEXT NOT NULL,
         check_in TEXT,
         check_out TEXT,
         status TEXT DEFAULT 'present')
    ''')
    
    c.execute('''
        CREATE TABLE visitors
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT NOT NULL,
         purpose TEXT,
         visit_date TEXT NOT NULL,
         check_in TEXT,
         check_out TEXT,
         visited_person TEXT,
         status TEXT DEFAULT 'pending')
    ''')
    
    c.execute('''
        CREATE TABLE door_access
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
         username TEXT,
         door_name TEXT DEFAULT 'Main Door',
         access_time TEXT NOT NULL,
         access_granted INTEGER DEFAULT 0,
         method TEXT)
    ''')
    
    print("Adding default admin user...")
    c.execute('INSERT INTO users (username, password, role, full_name, email) VALUES (?, ?, ?, ?, ?)',
              ('admin', 'admin123', 'admin', 'System Administrator', 'admin@example.com'))
    c.execute('INSERT INTO users (username, password, role, full_name, email) VALUES (?, ?, ?, ?, ?)',
              ('user', 'user123', 'user', 'Regular User', 'user@example.com'))
    
    conn.commit()
    conn.close()
    
    print("\n✅ Database reset successfully!")
    print("Admin login: admin / admin123")
    print("User login: user / user123")

if __name__ == "__main__":
    reset_database()
