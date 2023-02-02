-- Задание 6.5

/*Сколько ключевых навыков в среднем указывают в вакансиях для DS?
Ответ округлите до двух знаков после точки-разделителя.

Будем считать вакансиями для дата-сайентистов такие, в названии которых есть хотя бы одно из следующих сочетаний:
-- 'data scientist';
-- 'data science';
-- 'исследователь данных';
-- 'ML' (здесь не нужно брать вакансии по HTML);
-- 'machine learning';
-- 'машинн%обучен%'.
*/

SELECT
    -- в конце строки отсутствует табуляция, корректируем +1 к количеству
    ROUND(AVG(LENGTH(key_skills) - LENGTH(REPLACE(key_skills, CHR(9), '')) + 1), 2) AS avg_keyskills
FROM
    vacancies
WHERE
    (
        LOWER(name) SIMILAR TO '%(data scientist|data science|исследователь данных|machine learning|машинн%обучен)%'
        OR 
        (
            name LIKE '%ML%' 
            AND 
            name NOT ILIKE '%HTML%'
        )
    )
;