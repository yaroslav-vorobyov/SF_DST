-- Задание 5.4

/*Напишите запрос для подсчёта количества работодателей, у которых не указана сфера деятельности.
Введите количество, которое вернул запрос, в поле ниже.
*/

SELECT
    COUNT(e.id)
FROM
    employers AS e
    LEFT JOIN employers_industries AS ei 
        ON e.id = ei.employer_id
WHERE 
    ei.industry_id IS NULL
;
