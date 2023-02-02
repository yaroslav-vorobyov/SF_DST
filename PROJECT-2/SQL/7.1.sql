/*Вывод вакансий Data Science по обязательным требованиям к навыкам соискателя:
-- только Python;
-- только Postgres/SQL;
-- только Postgres/SQL/Python;
-- любые другие навыки или их сочетание.

Вакансии в области Data Science такие, в названии которых есть хотя бы одно из следующих сочетаний:
    -- 'data scientist';
    -- 'data science';
    -- 'исследователь данных';
    -- 'ML' (здесь не нужно брать вакансии по HTML);
    -- 'machine learning';
    -- 'машинн%обучен%'.
*/

(
    SELECT
        'Python' AS ds_skills,
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
)
UNION ALL
(
    SELECT
        'Postgres/SQL',
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
            LOWER(key_skills) SIMILAR TO '%(postgres|sql)%'
        )
)
UNION ALL
(
    SELECT
        'Postgres/SQL/Python',
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
            LOWER(key_skills) SIMILAR TO '%(postgres|sql|python)%'
        )
)
UNION ALL
(
    SELECT
        'Total',
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
            key_skills IS NOT NULL
        )
)
ORDER BY
    count
;