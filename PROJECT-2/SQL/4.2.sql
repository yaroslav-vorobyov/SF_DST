-- Задание 4.2 

/*Посмотрим на зарплаты. 
У какого количества вакансий заполнено хотя бы одно из двух полей с зарплатой?
*/

SELECT
    COUNT(id) AS cnt_vacancies_filled_salary
FROM
    vacancies
WHERE
    (
        salary_from IS NOT NULL 
        OR 
        salary_to IS NOT NULL
    )
;