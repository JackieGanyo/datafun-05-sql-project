--Use COUNT, AVG, SUM, etc with tables

SELECT 
    COUNT(title) AS Number_of_books, 
    MIN(year_published) AS Oldest_Book, 
    MAX(year_published) AS Newest_Book,   
    AVG(year_published) AS Average_Year_Published
FROM books;
