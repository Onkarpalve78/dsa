use dvdrental;

-- CREATE INDEX return_date_index ON rental(return_date);

-- SELECT * FROM rental where inventory_id=282;

-- It took 28ms before to execute this query now it takes 4-6ms after creating index
SELECT * FROM rental where return_date='2005-08-25 02:29:36';

-- DROP INDEX "return_date_index";


-- SELECT * from pg_indexes WHERE tablename='rental'
