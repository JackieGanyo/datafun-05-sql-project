# datafun-05-sql-project

## **Project 5 SQL Module**

Link to specs for Project (<https://github.com/denisecase/datafun-05-spec>)  

### **Recommended New Project Workflow**

Use the recommended workflow - it's reliable and most likely to work with the fewest issues:

1. Create a GitHub project repository with a default README.md.
2. Clone your repo down to your machine.
3. Open your project folder in VS Code (if you haven't already).
4. Add a useful .gitignore with a line for .vsode/ and .venv/ and whatever else doesn't need to go in the repo.
5. Create and activate a local virtual environment in .venv.
6. Install your dependencies into your .venv (pandas and pyarrow) and freeze into your requirements.txt.
7. Record the commands used in your README.md.
8. Git add and commit with a useful message (e.g. "initial commit") and push to GitHub.
9. Create your first project files (usually in VS Code).
10. As you work, git add / commit / push to GitHub.

### Detailed List of steps
#### 1. Databases: Create (using Python)

SQLite is a self-contained, serverless, and zero-configuration SQL database engine that doesn't require any external Database Management System (DBMS) like SQL Server or Oracle to operate. Each database is a self-contained file. SQLite is widely used in embedded systems, mobile applications, and for lightweight database needs. We use the sqlite3 library to interact with SQLite databases using Python. 

Creating a database is a common task, so let's create a function to create the database. We'll need one input - the Path to the database file we want to create. 
![Mod 5 Create empty db file](https://github.com/JackieGanyo/datafun-05-sql-project/assets/162255714/dea61e30-d808-4de5-ba0f-c983183d04b6)

#### 2. Tables: Create
Now, let's create some tables for the database. We do this with SQL CREATE TABLE statements. While setting things up, we typically re-run our Python code multiple times, so add some code to DROP TABLE IF EXISTS before creating (or recreating) the tables.

#### 3a. Records: Create with INSERT INTO
We can populate our tables in several ways - we'll look at two: (1) Using SQL INSERT INTO statements and (2) populating tables directly from compatible data files.

These simple examples use INSERT INTO statements to populate tables. These statements make it easy to create and populate your database when using online SQL tools for practice. Here are some simple examples (using a slightly different author schema):
-- Insert a single author
INSERT INTO authors (name) VALUES ('John Doe');

-- Insert multiple authors in a single statement
INSERT INTO authors (name) VALUES ('Alice Smith'), ('Bob Johnson'), ('Eva Brown');

-- Insert an author and retrieve the auto-generated ID (SQLite specific)
INSERT INTO authors (name) VALUES ('Jane Green');
SELECT last_insert_rowid();

#### 3b. Records: Create from Data Files
Populating tables right from data at rest (static data files, e.g., csv files) is also very common. For this project, we have our csv files in the data folder. We can write a function to populate them right from the CSV using pandas.  Note that the data must be compatible with our table structure for the direct import to work. Typically, there will be much more data cleaning and munging required to go from one system's Excel or csv files into a centralized relational database system. Optional/aside: For modern data storage formats, look up data warehouses, data lakes, and data lakehouses. 

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

#### 4. Records: Read with SQL SELECT
SQL makes it easy to retrieve information from tables as well. Understand how to use SELECT queries to get different pieces of information, like listing all movies of a certain genre.
-- Select specific fields from the movies table
SELECT title, genre, director, release_year
FROM movies;

#### 5. Records: Filter with WHERE (AND, OR, DISTINCT)
As you work through these, use your textbook and any other resources. Learn to filter data using the WHERE clause. Practice writing queries to select based on specific criteria, such as movies released after a certain year or movies by a specific director.

Just like Python, you can use operators (e.g., <, >) including AND and OR to combine conditions.

To avoid duplicate records, use SELECT DISTINCT.

#### 6. Records: Sort with ORDER BY
Master sorting query results with ORDER BY. Practice organizing information by different criteria, like sorting movies by release year or by ratings. 
-- Sort movies by release year in ascending order
SELECT * FROM movies ORDER BY release_year;
![Filter results](https://github.com/JackieGanyo/datafun-05-sql-project/assets/162255714/d95cd1ab-d63b-4478-a2aa-37ec8e9d8faf)

-- Sort movies by title in descending order
SELECT * FROM movies ORDER BY title DESC;

#### 7. Records: INNER JOIN
Explore how to use INNER JOIN to combine data from multiple tables. 
![JOIN results](https://github.com/JackieGanyo/datafun-05-sql-project/assets/162255714/04e56842-e308-4b5e-9038-713cbd9d58bb)

-- Example of an Inner join between authors and books tables
SELECT authors.first_name, authors.last_name, books.title, books.year_published
FROM authors
INNER JOIN books ON authors.author_id = books.author_id;

#### 8. Records: UPDATE
Learn how to update existing records with the UPDATE statement. Practice scenarios might include updating the genre of a movie or correcting a movie's release year.

-- Update the genre of a movie
UPDATE movies
SET genre = 'Adventure'
WHERE title = 'The Dark Knight';

-- Correct the release year of a movie
UPDATE movies
SET release_year = 2008
WHERE title = 'Pulp Fiction';

#### 9. Records: DELETE FROM
Understand how to delete records with DELETE FROM. Learn to remove specific records, like deleting movies that have been discontinued or have low ratings.

-- Delete movies by title
DELETE FROM movies WHERE title IN ('Batman', 'Spiderman', 'Avatar');

-- Delete discontinued movies
DELETE FROM movies WHERE discontinued = 1;

-- Delete movies with a rating below 5.0
DELETE FROM movies WHERE rating < 5.0;

#### 10. Records: COUNT, AVG, SUM, and GROUP BY 
SQL Functions
Like Python, SQL has built in functions, including COUNT(), AVG(), and SUM(). 
![Aggregate Results](https://github.com/JackieGanyo/datafun-05-sql-project/assets/162255714/b9d0c13b-b52a-4819-91a8-5c009f686d27)

 ![Coding for Aggregate PY SQL](https://github.com/JackieGanyo/datafun-05-sql-project/assets/162255714/618b489a-98b9-43b5-9692-df055dfc89f4)


-- count all rows
SELECT COUNT(*) FROM sales;
 

-- get average amount
SELECT AVG(amount) FROM sales;
 

-- combine functions
SELECT SUM(amount), AVG(amount), COUNT(*) FROM sales;
 

Grouping Data
![AVG YR RESULTS](https://github.com/JackieGanyo/datafun-05-sql-project/assets/162255714/5273b54f-3c35-4ffa-a6c3-7563f936f0a2)
![books by author results](https://github.com/JackieGanyo/datafun-05-sql-project/assets/162255714/f9b0649b-5edb-411c-b21a-aaa35af6b433)

These functions become even more powerful when used with the GROUP BY clause for grouped data analysis. See your textbook for more information. 


-- Get the total sales and average sales amount by a salesperson
SELECT salesperson_id, SUM(amount), AVG(amount) 
FROM sales 
GROUP BY salesperson_id;
