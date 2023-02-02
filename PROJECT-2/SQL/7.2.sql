/*Расчёт среднего дохода в вакансиях Data Science с учетом полей, 
у которых заполнено хотя бы одно из двух полей с зарплатой, по всем регионам 
в зависимости от типа занятости

Вакансии в области Data Science такие, в названии которых есть хотя бы одно из следующих сочетаний:
    -- 'data scientist';
    -- 'data science';
    -- 'исследователь данных';
    -- 'ML' (здесь не нужно брать вакансии по HTML);
    -- 'machine learning';
    -- 'машинн%обучен%'.
*/

SELECT
    a.name AS area_name,
    v.schedule,
    -- считаем среднюю з/п, учитывая пустоты в полях, округляем до десятков тысяч, переводим в целое значение
    ROUND(AVG((COALESCE(v.salary_from, v.salary_to) + COALESCE(v.salary_to, v.salary_from)) / 2), -3)::int AS avg_salary
FROM
    areas AS a
    JOIN vacancies AS v 
        ON a.id = v.area_id
WHERE
    (
        LOWER(v.name) SIMILAR TO '%(data scientist|data science|исследователь данных|machine learning|машинн%обучен)%'
        OR 
        (
            v.name LIKE '%ML%' 
            AND 
            v.name NOT ILIKE '%HTML%'
        )
    )
    AND 
    (
        v.salary_from IS NOT NULL 
        OR 
        v.salary_to IS NOT NULL
    )
GROUP BY 
    area_name, schedule
ORDER BY
    area_name, avg_salary DESC
;