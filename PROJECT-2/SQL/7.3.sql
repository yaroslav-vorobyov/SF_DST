/*Расчёт среднего дохода с учетом полей, у которых заполнено хотя бы одно из двух полей с зарплатой,
в зависимости от опыта работы.
*/

SELECT
    experience,
    -- считаем среднюю з/п, учитывая пустоты в полях, переводим в целое значение
    AVG(COALESCE(salary_from, salary_to))::int "Мин. средн. от",
    AVG(COALESCE(salary_to, salary_from))::int "Макс. средн. до"
FROM 
    vacancies
GROUP BY  
    experience
ORDER BY
    "Мин. средн. от" DESC, "Макс. средн. до" DESC
;