-- Задание 3.1

/*Сколько вакансий есть в базе?
*/

SELECT 
    COUNT(id) AS cnt_vacancies
FROM 
    vacancies
;