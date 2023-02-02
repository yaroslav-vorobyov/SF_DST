-- Задание 6.4

/*С помощью запроса, аналогичного предыдущему, проверьте, насколько популярен Python 
в требованиях работодателей к DS. 
Вычислите количество вакансий, в которых в качестве ключевого навыка указан Python.

Будем считать вакансиями для дата-сайентистов такие, в названии которых есть хотя бы одно из следующих сочетаний:
-- 'data scientist';
-- 'data science';
-- 'исследователь данных';
-- 'ML' (здесь не нужно брать вакансии по HTML);
-- 'machine learning';
-- 'машинн%обучен%'.
*/

SELECT
    COUNT(id)
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
    AND 
    (
        LOWER(key_skills) SIMILAR TO '%python%'
    )
;