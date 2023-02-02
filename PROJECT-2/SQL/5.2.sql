-- Задание 5.2

/*Напишите запрос, который для каждого региона выведет количество работодателей и вакансий в нём.

Среди регионов, в которых нет вакансий, найдите тот, в котором наибольшее количество работодателей. 
Впишите его название в поле ниже в том виде, который вернул запрос.
*/

SELECT
    a.name,
    COUNT(DISTINCT e.id) AS cnt_emp,
    COUNT(v.id) AS cnt_vac
FROM
    areas AS a
    JOIN employers AS e 
        ON a.id = e.area
    LEFT JOIN vacancies AS v 
        ON a.id = v.area_id
GROUP BY
    a.id
ORDER BY 
    cnt_vac, 
    cnt_emp DESC
LIMIT 1
;