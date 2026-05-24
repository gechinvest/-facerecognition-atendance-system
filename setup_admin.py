import sqlite3

def main():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    c.execute('SELECT * FROM users WHERE username = ?', ('admin',))
    if c.fetchone():
        print("Admin user already exists!")
    else:
        c.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)',
                  ('admin', 'admin123', 'admin'))
        conn.commit()
        print("Admin user created successfully!")
        print("Username: admin")
        print("Password: admin123")
    
    conn.close()

if __name__ == "__main__":
    main()
