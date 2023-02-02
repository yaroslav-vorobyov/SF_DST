-- Задание 4.4

/*Напишите запрос, который выведет: 
-- количество вакансий для каждого сочетания типа рабочего графика (schedule) 
-- и типа трудоустройства (employment), используемого в вакансиях. 

Какая пара находится на втором месте по популярности?
*/

SELECT
    schedule,
    employment,
    COUNT(DISTINCT id) AS cnt
FROM
    vacancies
GROUP BY
    schedule, 
    employment
ORDER BY
    cnt DESC
-- Для ответа на вопрос в задании, приведённый в юните, следует раскомментировать операторы OFFSET & LIMIT
-- OFFSET 1
-- LIMIT 1
;