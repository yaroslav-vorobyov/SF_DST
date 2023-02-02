-- Задание 5.5

/*Напишите запрос, чтобы узнать название компании, находящейся на третьем месте в алфавитном списке (по названию) компаний, 
у которых указано четыре сферы деятельности.

Введите в поле ниже название этой компании так же, как оно указано в результате запроса.
*/

SELECT
    e.name AS employer_with_4_industries
FROM
    employers AS e
    JOIN employers_industries AS ei 
        ON e.id = ei.employer_id
GROUP BY
    e.id
HAVING
    COUNT(ei.employer_id) = 4
ORDER BY
    employer_with_4_industries
OFFSET 2
LIMIT 1
;