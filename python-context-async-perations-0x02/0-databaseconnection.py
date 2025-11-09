import sqlite3

class DatabaseConnection:
    """Custom context manager for handling DB connections"""
    def __enter__(self):
        self.conn = sqlite3.connect('users.db')
        self.cursor = self.conn.cursor()
        print("[INFO] Database connection opened.")
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print("[ERROR] Exception occurred:", exc_val)
        self.conn.close()
        print("[INFO] Database connection closed.")

# Using the custom context manager
with DatabaseConnection() as cursor:
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    for row in results:
        print(row)

["__init__"]
