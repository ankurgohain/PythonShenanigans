# database.py
import mysql.connector
from mysql.connector import Error

# def create_connection():
#     connection = None

def create_table():
    # connection = create_connection()
    # if connection:
    cursor = connection.cursor()
    try:
        cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    email VARCHAR(255) UNIQUE NOT NULL
                )
                """
            )
        connection.commit()
        print("Table 'users' created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()
        connection.close()

def add_user(name, email):
    # connection = create_connection()
    # if connection:
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        connection.commit()
        print(f"User {name} added successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()
        connection.close()

def get_all_users():
    # connection = create_connection()
    users = []
    # if connection:
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()
        connection.close()
    return users

def update_user(user_id, name=None, email=None):
    # connection = create_connection()
    # if connection:
    cursor = connection.cursor()
    try:
        query = "UPDATE users SET "
        params = []
        if name: 
            query += "name = %s, "
            params.append(name)
        if email: 
            query += "email = %s, "
            params.append(email)
        
        query = query.rstrip(", ") + " WHERE id = %s"
        params.append(user_id)
        
        cursor.execute(query, tuple(params))
        connection.commit()
        print(f"User {user_id} updated successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()
        connection.close()

def delete_user(user_id):
    # connection = create_connection()
    # if connection:
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        connection.commit()
        print(f"User {user_id} deleted successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()
    connection.close()

# Initialize database (create table if it doesn't exist)
if __name__ == "__main__":
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",    # Replace with your MySQL username
            passwd="password",  # Replace with your MySQL password
            # database="testdb"       # Replace with your database name
    )
        if connection.is_connected():
            print("Connection to MySQL DB successful")
        connection.cursor().execute("CREATE DATABASE IF NOT EXISTS testdb;")
        connection.cursor().execute("USE testdb;")
        create_table()
    except Error as e:
        print(f"The error '{e}' occurred")
