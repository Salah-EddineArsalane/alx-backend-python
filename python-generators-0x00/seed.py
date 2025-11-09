import mysql.connector
import csv
import uuid

def connect_db():
    """Connect to MySQL server."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password"
    )

def create_database(connection):
    """Create database ALX_prodev if it doesn’t exist."""
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    print("Database created or already exists.")
    cursor.close()

def connect_to_prodev():
    """Connect to ALX_prodev database."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="ALX_prodev"
    )

def create_table(connection):
    """Create user_data table."""
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id VARCHAR(50) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL(3,0) NOT NULL,
            INDEX (user_id)
        );
    """)
    print("Table user_data created successfully")
    cursor.close()

def insert_data(connection, csv_file):
    """Insert CSV data into user_data table."""
    cursor = connection.cursor()
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute("""
                INSERT IGNORE INTO user_data (user_id, name, email, age)
                VALUES (%s, %s, %s, %s);
            """, (str(uuid.uuid4()), row['name'], row['email'], row['age']))
    connection.commit()
    print("Data inserted successfully")
    cursor.close()
