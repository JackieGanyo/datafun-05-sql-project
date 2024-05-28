#Create a new SQLite database file in the current project directory
import sqlite3
import pandas as pd
import pathlib

## Define the database file in the current root project directory
#Check for db and delete if it exists


db_file = pathlib.Path("project.sqlite3")
if db_file.exists():
    db_file.unlink()

def create_database():
    """Function to create a database. Connecting for the first time
    will create a new database file if it doesn't exist yet.
    Close the connection after creating the database
    to avoid locking the file."""
    try:
        conn = sqlite3.connect(db_file)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print("Error creating the database:", e)

def main():
    create_database()

if __name__ == "__main__":
    main()