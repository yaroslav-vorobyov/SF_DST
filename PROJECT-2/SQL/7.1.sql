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

-- подсчёт вакансий с навыком Python
(
    SELECT
        'Python' AS ds_skills,
        COUNT(id) AS cnt
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
-- подсчёт вакансий с навыком Postgres/SQL
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
-- подсчёт вакансий с навыком Postgres/SQL/Python
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
-- подсчёт вакансий с любым навыком
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
    cnt
;