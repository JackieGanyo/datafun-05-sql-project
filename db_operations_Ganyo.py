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
# Import Libraries
import os
import sqlite3
import pathlib
import pandas as pd
import pyarrow 
import logging

#Logging Configuration for the project. Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Program started")

#Define the database file in the current root project directory
db_file = "Module5.db" 

#Define create-database function
def create_database():
    """Function to create a database. Connecting for the first time
    will create a new database file if it doesn't exist yet.
    Close the connection after creating the database
    to avoid locking the file."""
    try:
        conn = sqlite3.connect(db_file)
        conn.close()
        print("Module5.db created successfully.")
    except sqlite3.Error as e:
        print("Error creating the database:", e)

def create_tables():
    """Function to read and execute SQL statements to create tables"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql", "create_tables.sql")
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
        print("Error inserting CSV data:", e)
        
#Function to insert data into the tables from an SQL file. 
def insert_records(): 
    try:       
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql", "insert_records.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
        print("Data inserted successfully.")
    except sqlite3.Error as e:
        print("Error inserting data:", e)

#Function to delete Shakespeare records from the tables
def delete_records():
    with sqlite3.connect(db_file) as conn:
        sql_file = pathlib.Path('sql', 'delete_records.sql')
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file}")      

#Function to query database using AVG, COUNT, MAX, MIN      
def query_aggregation():
    try:
        db_file = pathlib.Path("Module5.db")
        # Connect to the SQLite database
        with sqlite3.connect(db_file) as conn:
            # Specify the SQL script file
            sql_file = pathlib.Path('sql', 'query_aggregation.sql')
            # Read the SQL script
            with open(sql_file, 'r') as file:
                sql_script = file.read()
             # Execute the SQL script
            cur = conn.executescript(sql_script)
           # Queries to fetch the results (assuming these are the same queries as in the script)
            queries = [
                ("Total Number of Books", "SELECT COUNT(title) AS Number_of_books FROM books;"),
                ("Oldest Published Book", "SELECT MIN(year_published) AS Oldest_Book FROM books;"),
                ("Newest Published Book", "SELECT MAX(year_published) AS Newest_Book FROM books;"),
                ("Average Published Year", "SELECT AVG(year_published) AS Average_Year_Published FROM books;")
            ]
            with open("Aggregate.txt", "w") as file:
                for description, query in queries:
                    cur.execute(query)
                    result = cur.fetchone()
                    if result:
                        column_names = [desc[0] for desc in cur.description]
                        file.write(f"{description}\n")
                        file.write('\t'.join(column_names) + '\n')
                        file.write('\t'.join(map(str, result)) + '\n\n')
            print(f"Executed SQL from {sql_file}")
    except sqlite3.Error as e:
        print("Error aggregating query data:", e)

#Function to query database using 
def query_filter():
    try: 
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path('sql', 'query_filter.sql')
            with open(sql_file, 'r') as file:
                sql_script = file.read()
                cur = conn.executescript(sql_script)
# Queries to fetch the results (assuming these are the same queries as in the script)
            queries = [
                ("Authors Last Name Beginning with ‘S%’", "SELECT * FROM authors WHERE (last) LIKE 'S%'"),
                ("Books Published in the 1900s", "SELECT * FROM books WHERE (year_published) BETWEEN 1900 AND 1999;")
                ]
            with open("Filter.txt", "w") as file:
                for description, query in queries:
                    cur.execute(query)
                    result = cur.fetchall()
                    if result:
                    # Write the description and column headers
                        column_names = [desc[0] for desc in cur.description]
                        file.write(f"{description}\n")
                        file.write('\t'.join(column_names) + '\n')
                        file.write('\t'.join(map(str, result)) + '\n\n')
                    # Write all rows
                        for row in result:
                            file.write('\t'.join(map(str, row)) + '\n')
                        file.write('\n')  # Separate results for readability
            print(f"Executed SQL from {sql_file}") 
    except sqlite3.Error as e:
        print("Error filter query data:", e)

#Function to query database using ORDER BY
def query_sorting():
    try:
        # Specify the source database file
        source_db_file = pathlib.Path("Module5.db")
        # Specify the target database file
        target_db_file = pathlib.Path("Sorted.db")
        
        # Connect to the source SQLite database
        with sqlite3.connect(source_db_file) as source_conn:
            # Read the SQL script
            sql_file = pathlib.Path('sql', 'query_aggregation.sql')
            with open(sql_file, 'r') as file:
                sql_script = file.read()
            
            # Execute the SQL script in the source database
            source_conn.executescript(sql_script)
            
            # Fetch sorted results from the source database
            source_cursor = source_conn.cursor()
            source_cursor.execute("SELECT * FROM books ORDER BY year_published ASC;")
            sorted_books = source_cursor.fetchall()
            books_columns = [description[0] for description in source_cursor.description]

            source_cursor.execute("SELECT * FROM authors ORDER BY last ASC;")
            sorted_authors = source_cursor.fetchall()
            authors_columns = [description[0] for description in source_cursor.description]
        
        # Connect to the target SQLite database (create it if it doesn't exist)
        with sqlite3.connect(target_db_file) as target_conn:
            target_cursor = target_conn.cursor()
            
            # Create books table in the target database
            target_cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS books (
                    {", ".join([f"{col} TEXT" for col in books_columns])}
                );
            """)
            
            # Insert sorted books into the target database
            for book in sorted_books:
                target_cursor.execute(f"""
                    INSERT INTO books ({", ".join(books_columns)}) 
                    VALUES ({", ".join(['?' for _ in books_columns])});
                """, book)
            
            # Create authors table in the target database
            target_cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS authors (
                    {", ".join([f"{col} TEXT" for col in authors_columns])}
                );
            """)
            
            # Insert sorted authors into the target database
            for author in sorted_authors:
                target_cursor.execute(f"""
                    INSERT INTO authors ({", ".join(authors_columns)}) 
                    VALUES ({", ".join(['?' for _ in authors_columns])});
                """, author)
            target_conn.commit()
            print(f"Sorted data has been inserted into {target_db_file}")
    except sqlite3.Error as e:
        print("Error processing query and sorting data:", e)

#Function to query database using GROUP BY 
def query_group_by():
    try:
        # Specify the source database file
        source_db_file = pathlib.Path("Module5.db")
        # Specify the target database file
        target_db_file = pathlib.Path("Grouped.db")
        
        # Connect to the source SQLite database
        with sqlite3.connect(source_db_file) as source_conn:
            # Read the SQL script
            sql_file = pathlib.Path('sql', 'query_group_by.sql')
            with open(sql_file, 'r') as file:
                sql_script = file.read()
            
            # Execute the SQL script in the source database
            source_conn.executescript(sql_script)
            
            # Perform the GROUP BY queries and fetch results
            group_queries = [
                ("Books per Author",
                """SELECT authors.first, authors.last, COUNT(books.book_id) AS book_count
                FROM authors
                JOIN books ON authors.author_id = books.author_id
                GROUP BY  authors.first, authors.last;"""
                ),
                ("Average Year Published per Author",
                """SELECT authors.first, authors.last, AVG(books.year_published) AS avg_year_published
                FROM authors
                JOIN books ON authors.author_id= books.author_id
                GROUP BY authors.first, authors.last;""")
                ]
            
            # Connect to the target SQLite database (create it if it doesn't exist)
            with sqlite3.connect(target_db_file) as target_conn:
                target_cursor = target_conn.cursor()
                
                # Create result tables in the target database
                target_cursor.execute(
                    """CREATE TABLE IF NOT EXISTS books_per_author(
                    first_name TEXT,
                    last_name TEXT,
                    book_count INTEGER);"""
                )
                
                target_cursor.execute(
                    """CREATE TABLE IF NOT EXISTS avg_year_published_per_author
                    (first_name TEXT,
                    last_name TEXT,
                    avg_year_published REAL);"""
                )
                
                # Execute the group queries and insert results into the target database
                for description, query in group_queries:
                    source_cursor = source_conn.cursor()
                    source_cursor.execute(query)
                    results = source_cursor.fetchall()
                    if results:
                        # Determine the target table based on the description
                        if "Books per Author" in description:
                            target_table = "books_per_author"
                        elif "Average Year Published per Author" in description:
                            target_table = "avg_year_published_per_author"
                        
                        # Insert the results into the appropriate table
                        for row in results:
                            target_cursor.execute(f"""
                                INSERT INTO {target_table} VALUES ({", ".join(['?' for _ in row])});
                            """, row)
                
                target_conn.commit()
                print(f"Grouped data has been inserted into {target_db_file}")
    
    except sqlite3.Error as e:
        print("Error processing group query and storing data:", e)

#Function to query database using JOIN
def query_join():
    try:
        # Specify the source database file
        source_db_file = pathlib.Path("Module5.db")
        # Specify the target database file
        target_db_file = pathlib.Path("JOIN.db")

        # Connect to the source SQLite database
        with sqlite3.connect(source_db_file) as conn:
            # Define the SQL query
            query = """
                SELECT authors.first, authors.last, books.title, books.year_published
                FROM authors
                JOIN books
                ON authors.author_id = books.author_id;
            """
            
            # Execute the SQL query
            cursor = conn.cursor()
            cursor.execute(query)
            
            # Fetch all results
            results = cursor.fetchall()

        # Connect to the target SQLite database
        with sqlite3.connect(target_db_file) as target_conn:
            # Create a new table in the target database to store the results
            target_cursor = target_conn.cursor()
            target_cursor.execute("""
                CREATE TABLE IF NOT EXISTS authors_books (
                    first_name TEXT,
                    last_name TEXT,
                    book_title TEXT,
                    year_published INTEGER
                );
            """)
            
            # Insert the fetched results into the new table
            target_cursor.executemany("""
                INSERT INTO authors_books VALUES (?, ?, ?, ?);
            """, results)

            # Commit the changes
            target_conn.commit()

        print("Results have been stored in JOIN.db database.")

    except sqlite3.Error as e:
        print("Error querying authors and books:", e)

            
def main():
    create_database()
    create_tables()
    insert_data_from_csv()
    insert_records() 
    delete_records()
    query_aggregation()
    query_filter()
    query_sorting()
    query_group_by()
    query_join()    
    
if __name__ == "__main__":
    main()
    
logging.info("Program ended")
