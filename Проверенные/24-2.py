# Задание 24-2
CREATE VIEW amount_by_author AS
SELECT author_id, SUM(amount) AS SA
from  book1
GROUP BY author_id

CREATE VIEW min_amount AS
SELECT MIN(SA) AS MSA
FROM (SELECT *FROM amount_by_author) que_1

SELECT name_author, SUM(amount) AS QTY
FROM author INNER JOIN book1
ON author.author_id = book1.author_id
GROUP BY name_author
HAVING SUM(amount) = (SELECT * FROM min_amount)