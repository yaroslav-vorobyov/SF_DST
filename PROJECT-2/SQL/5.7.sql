-- Задание 5.7

/*Для компании «Яндекс» выведите список регионов-миллионников, 
в которых представлены вакансии компании, вместе с количеством вакансий в этих регионах. 

Также добавьте строку Total с общим количеством вакансий компании.
*/
(
    SELECT
        a.name AS area_name,
        COUNT(v.id) AS cnt_yandex_vacancies
    FROM
        employers AS e
        JOIN vacancies AS v
            ON e.id = v.employer_id
            AND
            e.name = 'Яндекс' 
        JOIN areas AS a
            ON v.area_id = a.id
            AND 
            a.name IN ('Москва','Санкт-Петербург','Новосибирск','Екатеринбург','Казань',
                'Нижний Новгород','Челябинск','Красноярск','Самара','Уфа',
                'Ростов-на-Дону','Омск','Краснодар','Воронеж','Пермь','Волгоград')
            -- a.name IN {cities}
    GROUP BY
        a.id
)
UNION ALL
(
    SELECT
        'Total',
        COUNT(v.id)
    FROM
        employers AS e
        JOIN vacancies AS v
            ON e.id = v.employer_id
            AND
            e.name = 'Яндекс' 
        JOIN areas AS a
            ON v.area_id = a.id
            AND 
            a.name IN ('Москва','Санкт-Петербург','Новосибирск','Екатеринбург','Казань',
                'Нижний Новгород','Челябинск','Красноярск','Самара','Уфа',
                'Ростов-на-Дону','Омск','Краснодар','Воронеж','Пермь','Волгоград')
            -- a.name IN {cities}
)
ORDER BY
    cnt_yandex_vacancies
;