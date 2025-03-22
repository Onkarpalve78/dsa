SELECT p.first_name, p.email,
MIN(o.order_price) as minimum_order,
MAX(o.order_price) as maximum_order,
COUNT(o.order_id) as total_orders,
SUM(o.order_price) as total_spent
FROM persons p
JOIN orders o ON o.personid=p.personid
GROUP BY p.first_name,
p.email
ORDER BY total_spent DESC
