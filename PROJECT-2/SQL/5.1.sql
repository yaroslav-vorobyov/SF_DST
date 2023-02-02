-- Задание 5.1
/*Напишите запрос, который позволит узнать, 
какие работодатели находятся на первом и пятом месте по количеству вакансий.

Выберите верный вариант ответа:
-- Яндекс — ИК СИБИНТЕК
-- Cybernet (Кибернет) — СНПА Промышленная безопасность
-- Яндекс — Газпром нефть (True)
-- Cybernet (Кибернет) — Газпром нефть
*/

/* Вывод 1 места */
(
    SELECT
        e.name AS employer_name,
        COUNT(e.id) AS cnt_vacancies
    FROM
        employers AS e
        JOIN vacancies AS v
            ON e.id = v.employer_id
    GROUP BY
        e.name
    ORDER BY
        cnt_vacancies DESC
    LIMIT 1
)
UNION ALL
/* Вывод 5 места */
(
    SELECT
        e.name AS employer_name,
        COUNT(e.id) AS cnt_vacancies
    FROM
        employers AS e
        JOIN vacancies AS v
            ON e.id = v.employer_id
    GROUP BY
        e.name
    ORDER BY
        cnt_vacancies DESC
    OFFSET 4
    LIMIT 1
)
ORDER BY
    cnt_vacancies DESC
;