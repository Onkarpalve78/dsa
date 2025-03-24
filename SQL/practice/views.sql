-- Active: 1742208391141@@127.0.0.1@5432@practice
-- USE practice;
--  use \c practice in pg terminal as postgres doesnt support USE


CREATE VIEW user_orders AS
SELECT p.*,o.* 
FROM persons p
JOIN orders o ON p.id=o.personid ;

-- SELECT * from persons;

-- ALTER TABLE persons
-- RENAME COLUMN personid to id

-- ALTER TABLE orders
-- DROP COLUMN email;

SELECT * FROM user_orders ;