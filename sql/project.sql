-- Start by deleting any tables if the exist already
-- We want to be able to re-run this script as needed.
-- DROP tables in reverse order of creation 
-- DROP dependent tables (with foreign keys) first

DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;


-- Create the authors table 
-- Note that the author table has no foreign keys, so it is a standalone table

CREATE TABLE authors (
    author_id TEXT PRIMARY KEY,
    first_name TEXT,
    last_name TEXT
    year_born INTEGER
);
-- Insert authors data
INSERT INTO authors (author_id, first_name, last_name, year_born)
VALUES
    ('10f88232-1ae7-4d88-a6a2-dfcebb22a596', 'Harper', 'Lee', 1926),
    ('c3a47e85-2a6b-4196-a7a8-8b55d8fc1f70', 'George', 'Orwell', 1903),
    ('e0b75863-866d-4db4-85c7-df9bb8ee6dab', 'F. Scott', 'Fitzgerald', 1896),
    ('7b144e32-7ff4-4b58-8eb0-e63d3c9f9b8d', 'Aldous', 'Huxley', 1894),
    ('8d8107b6-1f24-481c-8a21-7d72b13b59b5', 'J.D.', 'Salinger', 1919),
    ('0cc3c8e4-e0c0-482f-b2f7-af87330de214', 'Ray', 'Bradbury', 1920),
    ('4dca0632-2c53-490c-99d5-4f6d41e56c0e', 'Jane', 'Austen', 1775),
    ('16f3e0a1-24cb-4ed6-a50d-509f63e367f7', 'J.R.R.', 'Tolkien', 1892),
    ('06cf58ab-90f1-448d-8e54-055e4393e75c', 'J.R.R.', 'Tolkien', 1892),
    ('6b693b96-394a-4a1d-a4e2-792a47d7a568', 'J.K.', 'Rowling', 1965);

-- Create the books table
-- Note that the books table has a foreign key to the authors table
-- This means that the books table is dependent on the authors table
-- Be sure to create the standalone authors table BEFORE creating the books table.

CREATE TABLE books (
    book_id TEXT PRIMARY KEY,
    title TEXT,
    year_published INTEGER,
    author_id TEXT,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);

INSERT INTO books (book_id, title, year_published, author_id)
VALUES
    ('d6f83870-ff21-4a5d-90ab-26a49ab6ed12', 'To Kill a Mockingbird', 1960, '10f88232-1ae7-4d88-a6a2-dfcebb22a596'),
    ('0f5f44f7-44d8-4f49-b8c4-c64d847587d3', '1984', 1949, 'c3a47e85-2a6b-4196-a7a8-8b55d8fc1f70'),
    ('f9d9e7de-c44d-4d1d-b3ab-59343bf32bc2', 'The Great Gatsby', 1925, 'e0b75863-866d-4db4-85c7-df9bb8ee6dab'),
    ('38e530f1-228f-4d6e-a587-2ed4d6c44e9c', 'Brave New World', 1932, '7b144e32-7ff4-4b58-8eb0-e63d3c9f9b8d'),
    ('c2a62a4b-cf5c-4246-9bf7-b2601d542e6d', 'The Catcher in the Rye', 1951, '8d8107b6-1f24-481c-8a21-7d72b13b59b5'),
    ('3a1d835c-1e15-4a48-8e8c-b12239604e98', 'Fahrenheit 451', 1953, '0cc3c8e4-e0c0-482f-b2f7-af87330de214'),
    ('c6e67918-e509-4a6b-bc3a-979f6ad802f0', 'Pride and Prejudice', 1813, '4dca0632-2c53-490c-99d5-4f6d41e56c0e'),
    ('be951205-6cc2-4b3d-96f1-7257b8fc8c0f', 'The Hobbit', 1937, '16f3e0a1-24cb-4ed6-a50d-509f63e367f7');
