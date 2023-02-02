-- Задание 4.3 

/*Найдите средние значения для: 
-- нижней 
-- и верхней границы зарплатной вилки. 

Округлите значения до целого числа.
*/

SELECT
    AVG(salary_from)::int AS "Min AVG from:",
    AVG(salary_to)::int AS "Max AVG to:"
FROM
    vacancies
;