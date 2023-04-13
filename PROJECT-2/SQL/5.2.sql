-- Задание 5.2

/*Напишите запрос, который для каждого региона выведет количество работодателей и вакансий в нём.

Среди регионов, в которых нет вакансий, найдите тот, в котором наибольшее количество работодателей. 
Впишите его название в поле ниже в том виде, который вернул запрос.
*/

SELECT
    a.name AS area_name,
    COUNT(DISTINCT e.id) AS cnt_employers,
    COUNT(DISTINCT v.id) AS cnt_vacancies
FROM
    areas AS a
    JOIN employers AS e 
        ON a.id = e.area
    LEFT JOIN vacancies AS v 
        ON a.id = v.area_id
WHERE
    v.id IS NULL
GROUP BY
    a.id
ORDER BY 
    cnt_vacancies,
    cnt_employers DESC
LIMIT 1
;