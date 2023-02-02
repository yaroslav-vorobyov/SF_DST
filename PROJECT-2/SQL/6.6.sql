-- Задание 6.6

/*Напишите запрос, позволяющий вычислить, какую зарплату для DS в среднем указывают 
для каждого типа требуемого опыта (уникальное значение из поля experience).

При решении задачи примите во внимание следующее:
-- Рассматриваем только вакансии, у которых заполнено хотя бы одно из двух полей с зарплатой.
-- Если заполнены оба поля с зарплатой, считаем зарплату по каждой вакансии как сумму двух полей, делённую на 2. 
    Если заполнено только одно из полей, его и считаем зарплатой по вакансии.
-- Если в расчётах участвует null, в результате он тоже даст null (посмотрите, что возвращает запрос select 1 + null).

Чтобы избежать этой ситуации, мы воспользуемся функцией coalesce, которая заменит null на значение, которое мы передадим. 
Например, посмотрите, что возвращает запрос select 1 + coalesce(null, 0).
Выясните, на какую зарплату в среднем может рассчитывать дата-сайентист с опытом работы от 3 до 6 лет. 
Результат округлите до целого числа.

Будем считать вакансиями для дата-сайентистов такие, в названии которых есть хотя бы одно из следующих сочетаний:
-- 'data scientist';
-- 'data science';
-- 'исследователь данных';
-- 'ML' (здесь не нужно брать вакансии по HTML);
-- 'machine learning';
-- 'машинн%обучен%'.
*/

SELECT
    experience,
    AVG((COALESCE(salary_from, salary_to) + COALESCE(salary_to, salary_from)) / 2)::int AS avg_salary
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
        salary_from IS NOT NULL
        OR
        salary_to IS NOT NULL
    )
GROUP BY 
    experience
;