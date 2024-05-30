--Query filter tables using WHERE and conditions

--Filter authors by last name beginning with 'S'
SELECT * FROM authors WHERE last = 'S*';

--Filter books by year published in 1900s
SELECT * FROM books WHERE year_published BETWEEN 1900 AND 1999; 

