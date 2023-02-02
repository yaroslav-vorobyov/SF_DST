-- Задание 5.6

/*С помощью запроса выясните, у какого количества работодателей в качестве сферы деятельности 
указана «Разработка программного обеспечения».
*/

SELECT
    COUNT(ei.employer_id) AS cnt_developer_employers
FROM
    employers_industries AS ei 
    JOIN industries as i
        ON ei.industry_id = i.id
WHERE 
    i.name LIKE 'Разработка программного обеспечения'
;