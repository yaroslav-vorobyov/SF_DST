-- Задание 4.5

/*Напишите запрос, выводящий: 
-- значения поля Требуемый опыт работы (experience) 
-- в порядке возрастания количества вакансий, в которых указан данный вариант опыта.
*/

SELECT
    experience,
    COUNT(id) AS cnt_vacancies
FROM
    vacancies
GROUP BY
    experience
ORDER BY
    cnt_vacancies
;