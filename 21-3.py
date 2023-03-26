# Задание 21-3
CREATE TABLE book
(book_id int,
book_title text,
book_author text,
publisher_id int)

SELECT * FROM book
INSERT INTO book VALUES
(1, 'Анна Каренина', 'Толстой', 11),
(2, 'Господа Бовари', 'Флобер', 22),
(3, 'Красное и черное', 'Стендаль', 22),
(4, 'Ампир V', 'Пелевин', 11),
(5, 'Моби Дик', 'Милвилл', 22),
(6, 'Воскресение', 'Толстой', 11)


SELECT book_title, book_author FROM book WHERE publisher_id = 11
SELECT book_id, book_title, book_author FROM book WHERE book_author = 'Толстой'
SELECT book_title, book_author FROM book WHERE book_title LIKE 'А%'
