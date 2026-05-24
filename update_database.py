import sqlite3
import os

DATABASE = 'database.db'

def update_database():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    
    print("Checking database schema...")
    
    try:
        c.execute('ALTER TABLE users ADD COLUMN full_name TEXT')
        print("Added 'full_name' column.")
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e):
            print("'full_name' column already exists.")
        else:
            print(e)
    
    try:
        c.execute('ALTER TABLE users ADD COLUMN email TEXT')
        print("Added 'email' column.")
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e):
            print("'email' column already exists.")
        else:
            print(e)
    
    conn.commit()
    conn.close()
    print("\n✅ Database updated successfully!")

if __name__ == "__main__":
    update_database()
