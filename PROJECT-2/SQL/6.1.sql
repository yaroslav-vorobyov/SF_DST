-- Задание 6.1

/*Сколько вакансий имеет отношение к данным? 
Считаем, что вакансия имеет отношение к данным, если в её названии содержатся слова 'data' или 'данн'.
*/

SELECT
    COUNT(*) AS cnt_data_vacancies
FROM
    vacancies
WHERE
    LOWER(name) SIMILAR TO '%(data|данн)%'
ORDER BY
    1
;