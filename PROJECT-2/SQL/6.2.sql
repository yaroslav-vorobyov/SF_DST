-- Задание 6.2

/*Сколько есть подходящих вакансий для начинающего дата-сайентиста?

Будем считать вакансиями для дата-сайентистов такие, в названии которых есть хотя бы одно из следующих сочетаний:
-- 'data scientist';
-- 'data science';
-- 'исследователь данных';
-- 'ML' (здесь не нужно брать вакансии по HTML);
-- 'machine learning';
-- 'машинн%обучен%'.

Считаем вакансиями для специалистов уровня Junior следующие:
-- в названии есть слово 'junior' или
-- требуемый опыт — 'Нет опыта' или
-- тип трудоустройства — 'Стажировка'.
*/

SELECT
    COUNT(id) AS cnt_junior_ds_vacancies
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
        name ILIKE '%junior%' 
        OR 
        experience = 'Нет опыта'
        OR 
        employment = 'Стажировка'
    )
;