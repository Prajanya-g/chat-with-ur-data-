import sqlite3

# This function creates a sqlite database for a sql file 
# The function has two parameters the database file that needs to be created and the sql file of the database 
# The function returns nothing but creates a .db file
def create_sqlite_database(db_file, sql_file):
    try:
        # Connect to the SQLite database (creates a new one if it doesn't exist)
        conn = sqlite3.connect(db_file)

        # Create a cursor to execute SQL commands
        cursor = conn.cursor()

        # Read and execute SQL commands from the .sql file
        with open(sql_file, 'r') as sql_file:
            sql_commands = sql_file.read()
            cursor.executescript(sql_commands)

        # Commit the changes and close the database connection
        conn.commit()
        conn.close()
        print("Database creation and SQL execution successful.")
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    except Exception as e:
        print(f"Error: {e}")

