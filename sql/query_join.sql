--Query authors & books using JOIN
SELECT authors.first, authors.last, books.title, books.year_published
FROM authors
JOIN books
ON authors.author_id = books.author_id;