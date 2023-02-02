-- Задание 6.3

/*Сколько есть вакансий для DS, в которых в качестве ключевого навыка указан SQL или postgres?

Будем считать вакансиями для дата-сайентистов такие, в названии которых есть хотя бы одно из следующих сочетаний:
-- 'data scientist';
-- 'data science';
-- 'исследователь данных';
-- 'ML' (здесь не нужно брать вакансии по HTML);
-- 'machine learning';
-- 'машинн%обучен%'.
*/

SELECT
    COUNT(id) AS cnt_postgres_sql_ds_vacancies
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
        LOWER(key_skills) SIMILAR TO '%(postgres|sql)%'
    )
;