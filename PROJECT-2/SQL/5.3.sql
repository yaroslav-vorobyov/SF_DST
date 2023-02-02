-- Задание 5.3

/*Для каждого работодателя посчитайте количество регионов, в которых он публикует свои вакансии.
Выберите максимальное значение из получившегося списка.
*/

SELECT
    e.name AS employer_name,
    COUNT(DISTINCT v.area_id) AS cnt_areas
FROM
    employers AS e
    JOIN vacancies AS v 
        ON e.id = v.employer_id
GROUP BY
    e.id
ORDER BY 
    cnt_areas DESC
-- Для ответа на вопрос в задании, приведённый в юните, следует раскомментировать оператор OFFSET
-- LIMIT 1
;