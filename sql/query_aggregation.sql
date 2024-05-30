--Use COUNT, AVG, SUM, etc with tables

SELECT COUNT(title) AS Number_of_books FROM books;
SELECT MIN(year_published) AS Oldest_Book FROM books;
SELECT MAX(year_published) AS Newest_Book FROM books;   
SELECT AVG(year_published) AS Average_Year_Published FROM books;
