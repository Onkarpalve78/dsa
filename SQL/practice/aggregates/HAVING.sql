SELECT p.first_name, COUNT(o.order_id) as orders
FROM persons p
JOIN orders o ON o.personid=p.personid
GROUP BY p.first_name
HAVING COUNT(o.order_id)>1