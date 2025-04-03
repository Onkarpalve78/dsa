-- LC 176 https://leetcode.com/problems/second-highest-salary/description/


-- Medium

-- Table: Employee

-- +-------------+------+
-- | Column Name | Type |
-- +-------------+------+
-- | id          | int  |
-- | salary      | int  |
-- +-------------+------+
-- id is the primary key (column with unique values) for this table.
-- Each row of this table contains information about the salary of an employee.

 

-- Write a solution to find the second highest distinct salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

-- The result format is in the following example.

 

-- Example 1:

-- Input: 
-- Employee table:
-- +----+--------+
-- | id | salary |
-- +----+--------+
-- | 1  | 100    |
-- | 2  | 200    |
-- | 3  | 300    |
-- +----+--------+
-- Output: 
-- +---------------------+
-- | SecondHighestSalary |
-- +---------------------+
-- | 200                 |
-- +---------------------+

-- Example 2:

-- Input: 
-- Employee table:
-- +----+--------+
-- | id | salary |
-- +----+--------+
-- | 1  | 100    |
-- +----+--------+
-- Output: 
-- +---------------------+
-- | SecondHighestSalary |
-- +---------------------+
-- | null                |
-- +---------------------+



--  SELECT salary
--     FROM Employee
--     WHERE id NOT IN (SELECT id WHERE salary=MAX(salary) FROM Employee)
--     )
--     FROM Employee

-- There are several syntax errors in your SQL query. Here's what's wrong:

--     You can't have a nested SELECT directly after MAX() like that
--     There's incorrect syntax in your subquery's WHERE clause
--     You can't use an aggregate function (MAX) inside a WHERE clause directly


SELECT MAX(salary) SecondHighestSalary 
FROM Employee 
WHERE salary < (SELECT MAX(salary) FROM Employee)