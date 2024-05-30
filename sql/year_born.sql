--Alter Table add column year_born
ALTER TABLE authors 
ADD COLUMN year_born INTEGER;

#Update authors table with year_born

UPDATE authors SET year_born =
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
INSERT INTO authors (author_id, first, last, year_born)
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