use practice;
-- SELECT first_name, email FROM persons
-- WHERE personid in (SELECT personid from orders );


SELECT * from persons 
WHERE personid = (SELECT o.personid from orders o WHERE o.order_price=(SELECT MAX(order_price) FROM orders) );
