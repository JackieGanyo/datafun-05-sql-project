
--Insert year_born into original authors table
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

--insert at least 10 records into authors and books 
INSERT INTO authors (author_id, first_name, last_name)
VALUES
('10f88232-1ae7-4d88-a6a2-dfcebb22a597', 'William', 'Shakespeare', 1564),
('c3a47e85-2a6b-4196-a7a8-8b55d8fc1f10', 'Charles', 'Dickens', 1812),
('e0b75863-866d-4db4-85c7-df9bb8ee6dac', 'Edgar Allan', 'Poe', 1809), 
('7b144e32-7ff4-4b58-8eb0-e63d3c9f9b5a', 'Jules', 'Verne', 1854),
('8d8107b6-1f24-481c-8a21-7d72b13b62b5', 'Mark', 'Twain', 1835),
('0cc3c8e4-e0c0-482f-b2f7-af87329de214', 'Ernest', 'Hemingway', 1899),
('4dca0632-2c53-490c-99d5-4f6d41e56a1f', 'Herman', 'Melville', 1819),
('16f3e0a1-24cb-4ed6-a50d-509f63e365o5', 'Miguel', 'De Cervantes', 1547),
('06cf58ab-90f1-448d-8e54-055e4393a02c', 'John', 'Steinbeck', 1902),
('6b693b96-394a-4a1d-a4e2-792a47d7d952', 'Douglas', 'Adams', 1952);



--Insert year_published into original books table
INSERT INTO books (book_id, title, year_published, author_id)
VALUES
    ('d6f83870-ff21-4a5d-90ab-26a49ab6ed12', 'To Kill a Mockingbird', 1960, '10f88232-1ae7-4d88-a6a2-dfcebb22a596'),
    ('0f5f44f7-44d8-4f49-b8c4-c64d847587d3', '1984', 1949, 'c3a47e85-2a6b-4196-a7a8-8b55d8fc1f70'),
    ('f9d9e7de-c44d-4d1d-b3ab-59343bf32bc2', 'The Great Gatsby', 1925, 'e0b75863-866d-4db4-85c7-df9bb8ee6dab'),
    ('38e530f1-228f-4d6e-a587-2ed4d6c44e9c', 'Brave New World', 1932, '7b144e32-7ff4-4b58-8eb0-e63d3c9f9b8d'), 
    ('c2a62a4b-cf5c-4246-9bf7-b2601d245e6d', 'The Catcher in the Rye', 1951, '8d8107b6-1f24-481c-8a21-7d72b13b59b5'),
    ('c2a62a4b-cf5c-4246-9bf7-b2601d542e6d', 'The Lord of the Rings', 1954, '16f3e0a1-24cb-4ed6-a50d-509f63e367f7'),
    ('3a1d835c-1e15-4a48-8e8c-b12239604e98', 'Fahrenheit 451', 1953, '0cc3c8e4-e0c0-482f-b2f7-af87330de214'),
    ('c6e67918-e509-4a6b-bc3a-979f6ad802f0', 'Pride and Prejudice', 1813, '4dca0632-2c53-490c-99d5-4f6d41e56c0e'),
    ('be951205-6cc2-4b3d-96f1-7257b8fc8c0f', 'The Hobbit', 1937, '16f3e0a1-24cb-4ed6-a50d-509f63e367f7'),
    ('6b693b96-394a-4a1d-a4e2-792a47d7a568', 'Harry Potter and the Philosopher''s Stone', 1997, '6b693b96-394a-4a1d-a4e2-792a47d7a568');


--Insert 10 new records into books table
INSERT INTO books (book_id, title, year_published, author_id)
VALUES
    ('d6f83870-ff21-4a5d-90ab-26a49ab6ed11', 'Romeo & Juliet', 1597, '10f88232-1ae7-4d88-a6a2-dfcebb22a597'),
    ('0f5f44f7-44d8-4f49-b8c4-c64d847587d9', 'A Christmas Carol', 1843, 'c3a47e85-2a6b-4196-a7a8-8b55d8fc1f10'),
    ('f9d9e7de-c44d-4d1d-b3ab-59343bf32bc2', 'The Raven', 1845, 'e0b75863-866d-4db4-85c7-df9bb8ee6dac'),
    ('38e530f1-228f-4d6e-a587-2ed4d6c44e9c', 'Journey to the Centre of the Earth', 1867, '7b144e32-7ff4-4b58-8eb0-e63d3c9f9b5a'),
    ('c2a62a4b-cf5c-4246-9bf7-b2601d245e6d', 'The Adventures of Tom Sawyer', 1876, '8d8107b6-1f24-481c-8a21-7d72b13b62b5'),
    ('c2a62a4b-cf5c-4246-9bf7-b2601d542e6d', 'For Whom the Bell Tolls', 1940, '0cc3c8e4-e0c0-482f-b2f7-af87329de214'),
    ('3a1d835c-1e15-4a48-8e8c-b12239604m51', 'Moby Dick', 1851, '4dca0632-2c53-490c-99d5-4f6d41e56a1f'),
    ('c6e67918-e509-4a6b-bc3a-979f6ad805o5', 'Don Quixote', 1813, '16f3e0a1-24cb-4ed6-a50d-509f63e365o5'),
    ('be951205-6cc2-4b3d-96f1-7257b8fc8c0f', 'The Grapes of Wrath', 1939, '06cf58ab-90f1-448d-8e54-055e4393a02c'),
    ('6b693b96-394a-4a1d-a4e2-792a47d7da42', 'The Hitchhikers Guide to the Galaxy', 1979, '6b693b96-394a-4a1d-a4e2-792a47d7d952');

