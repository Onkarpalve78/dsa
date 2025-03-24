
-- use practice;

CREATE INDEX ix_user_name ON persons(first_name);

-- SHOW INDEX FROM persons;

-- For postgres
-- SELECT * FROM pg_indexes WHERE tablename = 'persons';

