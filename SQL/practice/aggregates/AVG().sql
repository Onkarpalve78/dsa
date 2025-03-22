use practice ;

select p.first_name , ROUND(AVG(o.order_price),0) as avg_spenditure
from persons p
join orders o ON p.personid=o.personid
GROUP BY p.first_name
ORDER BY AVG(o.order_price) DESC LIMIT 100



