-- Задание 4.3 

/*Найдите средние значения для: 
-- нижней 
-- и верхней границы зарплатной вилки. 

Округлите значения до целого числа.
*/

SELECT
    ROUND(AVG(salary_from))::int AS "Min_AVG_salary_from",
    ROUND(AVG(salary_to))::int AS "Max_AVG_salary_to"
FROM
    vacancies
;