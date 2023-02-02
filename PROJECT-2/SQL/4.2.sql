-- Задание 4.2 

/*Посмотрим на зарплаты. 
У какого количества вакансий заполнено хотя бы одно из двух полей с зарплатой?
*/

SELECT
    COUNT(id)
FROM
    vacancies
WHERE
    (
        salary_from IS NOT NULL 
        OR 
        salary_to IS NOT NULL
    )
;