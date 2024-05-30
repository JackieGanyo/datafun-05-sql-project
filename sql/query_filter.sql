--Filter authors by last name beginning with 'S'
SELECT * FROM authors WHERE last LIKE 'S%';

--Filter books published in 1900s
SELECT * FROM books WHERE year_published BETWEEN 1900 AND 1999; 

