import sqlite3
import sys


def connect_to_db():
    conn = sqlite3.connect('database.db')
    return conn


def create_db_table():
    try:
        conn = connect_to_db()
        conn.execute('''
            CREATE TABLE IF NOT EXISTS btc (
                price INTEGER NOT NULL,
                timestamp DATETIME NOT NULL,
                currency TEXT NOT NULL );
        ''')
        conn.commit()
        print("Table created successfully")
    except Exception as e:
        print("Table creation failed", e)
        sys.exit("Quitting App")
    finally:
        conn.close()


if __name__ == '__main__':
    create_db_table()
