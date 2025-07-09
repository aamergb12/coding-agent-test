from datetime import datetime
import sqlite3

class ContactManager:
    def __init__(self, db_path="crm.db"):
        self.db_path = db_path
        self.init_database()

    def init_database(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT UNIQUE,
                phone TEXT,
                company TEXT,
                created_at TIMESTAMP,
                last_updated TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()

    def add_contact(self, first_name, last_name, email, phone=None, company=None):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        now = datetime.now()
        try:
            cursor.execute('''
                INSERT INTO contacts (first_name, last_name, email, phone, company, created_at, last_updated)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (first_name, last_name, email, phone, company, now, now))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            conn.close()

    def get_contact(self, email):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM contacts WHERE email = ?', (email,))
        contact = cursor.fetchone()
        conn.close()
        return contact

    def update_contact(self, email, **kwargs):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        updates = []
        values = []
        for key, value in kwargs.items():
            updates.append(f"{key} = ?")
            values.append(value)
        
        values.append(datetime.now())
        values.append(email)
        
        query = f'''
            UPDATE contacts 
            SET {", ".join(updates)}, last_updated = ?
            WHERE email = ?
        '''
        
        cursor.execute(query, values)
        conn.commit()
        conn.close()
        return cursor.rowcount > 0

    def delete_contact(self, email):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM contacts WHERE email = ?', (email,))
        conn.commit()
        conn.close()
        return cursor.rowcount > 0