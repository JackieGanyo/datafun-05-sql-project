--Total Number of books
SELECT COUNT(title) AS Number_of_books FROM books;
--Oldest Published Book
SELECT MIN(year_published) AS Oldest_Book FROM books;
--Newest Published Book
SELECT MAX(year_published) AS Newest_Book FROM books;
--Average Published Year
SELECT AVG(year_published) AS Average_Year_Published FROM books;