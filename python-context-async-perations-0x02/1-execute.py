import sqlite3

class ExecuteQuery:
    """Context manager to execute a given query with parameters"""
    def __init__(self, query, params=()):
        self.query = query
        self.params = params

    def __enter__(self):
        self.conn = sqlite3.connect('users.db')
        self.cursor = self.conn.cursor()
        print("[INFO] Executing query...")
        self.cursor.execute(self.query, self.params)
        return self.cursor.fetchall()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        if exc_type:
            print("[ERROR] Query failed:", exc_val)
        else:
            print("[INFO] Query executed and connection closed.")

# Example usage
query = "SELECT * FROM users WHERE age > ?"
params = (25,)

with ExecuteQuery(query, params) as results:
    for row in results:
        print(row)
