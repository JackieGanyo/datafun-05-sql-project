-- Count the number of books per author
SELECT authors.first, authors.last, COUNT(books.book_id) AS book_count
FROM authors
JOIN books ON authors.author_id = books.author_id
GROUP BY authors.first, authors.last;

-- Calculate the average year of publication for each author
SELECT authors.first, authors.last, AVG(books.year_published) AS avg_year_published
FROM authors
JOIN books ON authors.author_id = books.author_id
GROUP BY authors.first, authors.last;