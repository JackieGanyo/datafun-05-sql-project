
'''
Jackie Ganyo
Module 5 - Database Operations in SQLite
The purpose of this program is to demonstrate how to perform 
database operations in SQLite using Python. The program will
create a new SQLite database file ("project.sqlite3") in the current project directory and 
create a table in the database. The program will also insert data into 
the table. The program will then read the data from the table and display
the data in a pandas DataFrame.
'''
# Import Standard Libraries

import sys
import sqlite3

#Import External Libraries
import pathlib
import pandas as pd
import pyarrow as pa
import datetime
import logging

#Logging Configuration for the project. Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Program started")

#Define the database file in the current root project directory
db_file = "Module5.db"


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

#Function to create tables in the database.
#Function to read and execute SQL statements to create tables
def create_tables():

    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql", "project.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Tables created successfully.")
    except sqlite3.Error as e:
        print("Error creating tables:", e)


#Function to insert data into the tables from a CSV file.
def insert_data_from_csv():
    """Function to use pandas to read data from CSV files (in 'data' folder)
    and insert the records into their respective tables."""
    try:
        author_data_path = pathlib.Path("data", "authors.csv")
        book_data_path = pathlib.Path("data", "books.csv")
        authors_df = pd.read_csv(author_data_path)
        books_df = pd.read_csv(book_data_path)
        with sqlite3.connect(db_file) as conn:
            # use the pandas DataFrame to_sql() method to insert data
            # pass in the table name and the connection
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print("Error inserting data:", e)


def main():
    create_database()
    create_tables()
    insert_data_from_csv()
    logging.info("Program ended")
    print("Program ended")
if __name__ == "__main__":
    main()




