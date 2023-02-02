/*Обзор работодателей предлагающих более 5 вакансий Data Science.

Вакансии в области Data Science такие, в названии которых есть хотя бы одно из следующих сочетаний:
    -- 'data scientist';
    -- 'data science';
    -- 'исследователь данных';
    -- 'ML' (здесь не нужно брать вакансии по HTML);
    -- 'machine learning';
    -- 'машинн%обучен%'.
*/
SELECT
    e.name AS empl_name,
    COUNT(v.id) as ds_vac_count
FROM vacancies AS v
    JOIN employers AS e ON e.id = v.employer_id
WHERE 
    (
        LOWER(v.name) SIMILAR TO '%(data scientist|data science|исследователь данных|machine learning|машинн%обучен)%'
            OR 
            (
                v.name LIKE '%ML%'
                AND v.name NOT ILIKE '%HTML%'
            )
    )
GROUP BY 
    e.id
HAVING
    COUNT(v.id) >= 5
ORDER BY 
    ds_vac_count DESC
LIMIT 20
;