--  Confirmation Rate
-- Medium

-- Table: Signups
-- +----------------+----------+
-- | Column Name    | Type     |
-- +----------------+----------+
-- | user_id        | int      |
-- | time_stamp     | datetime |
-- +----------------+----------+
-- user_id is the column of unique values for this table.
-- Each row contains information about the signup time for the user with ID user_id.

 
-- Table: Confirmations
-- +----------------+----------+
-- | Column Name    | Type     |
-- +----------------+----------+
-- | user_id        | int      |
-- | time_stamp     | datetime |
-- | action         | ENUM     |
-- +----------------+----------+
-- (user_id, time_stamp) is the primary key (combination of columns with unique values) for this table.
-- user_id is a foreign key (reference column) to the Signups table.
-- action is an ENUM (category) of the type ('confirmed', 'timeout')
-- Each row of this table indicates that the user with ID user_id requested a confirmation message at time_stamp and that confirmation message was either confirmed ('confirmed') or expired without confirming ('timeout').

 
-- The confirmation rate of a user is the number of 'confirmed' messages divided by the total number of requested confirmation messages. The confirmation rate of a user that did not request any confirmation messages is 0. Round the confirmation rate to two decimal places.
-- Write a solution to find the confirmation rate of each user.
-- Return the result table in any order.
-- The result format is in the following example.
 
-- Example 1:
-- Input: 
-- Signups table:
-- +---------+---------------------+
-- | user_id | time_stamp          |
-- +---------+---------------------+
-- | 3       | 2020-03-21 10:16:13 |
-- | 7       | 2020-01-04 13:57:59 |
-- | 2       | 2020-07-29 23:09:44 |
-- | 6       | 2020-12-09 10:39:37 |
-- +---------+---------------------+
-- Confirmations table:
-- +---------+---------------------+-----------+
-- | user_id | time_stamp          | action    |
-- +---------+---------------------+-----------+
-- | 3       | 2021-01-06 03:30:46 | timeout   |
-- | 3       | 2021-07-14 14:00:00 | timeout   |
-- | 7       | 2021-06-12 11:57:29 | confirmed |
-- | 7       | 2021-06-13 12:58:28 | confirmed |
-- | 7       | 2021-06-14 13:59:27 | confirmed |
-- | 2       | 2021-01-22 00:00:00 | confirmed |
-- | 2       | 2021-02-28 23:59:59 | timeout   |
-- +---------+---------------------+-----------+
-- Output: 
-- +---------+-------------------+
-- | user_id | confirmation_rate |
-- +---------+-------------------+
-- | 6       | 0.00              |
-- | 3       | 0.00              |
-- | 7       | 1.00              |
-- | 2       | 0.50              |
-- +---------+-------------------+
-- Explanation: 
-- User 6 did not request any confirmation messages. The confirmation rate is 0.
-- User 3 made 2 requests and both timed out. The confirmation rate is 0.
-- User 7 made 3 requests and all were confirmed. The confirmation rate is 1.
-- User 2 made 2 requests where one was confirmed and the other timed out. The confirmation rate is 1 / 2 = 0.5.


SELECT 
    s.user_id, 
    ROUND(
        COALESCE(
            SUM(CASE WHEN c.action = 'confirmed' THEN 1.0 ELSE 0 END) / 
            NULLIF(COUNT(c.action), 0), 
        0),
    2) AS confirmation_rate
FROM 
    Signups s 
LEFT JOIN 
    Confirmations c ON s.user_id = c.user_id
GROUP BY 
    s.user_id;

-- COASLESCE():
-- Return the first non-null value in a list:
-- SELECT COALESCE(NULL, NULL, NULL, 'W3Schools.com', NULL, 'Example.com'); 
-- Returns: 'W3Schools.com'

-- NULLIF(expression1,expression2):
-- Return NULL if expression1=expression2 else return expression1
-- Eg: NULLIF(count(c.action),0)
-- Return NULL if count(c.action) is also 0 else return count(c.action)


-- Here are the key corrections and explanations:

-- Use LEFT JOIN instead of FULL OUTER JOIN:

-- Since we want to include all users from Signups, even those without any confirmations, a LEFT JOIN is more appropriate.
-- FULL OUTER JOIN would include rows that don't exist in either table, which is not needed here.


-- Subquery for total confirmations is replaced with COUNT(c.action):

-- The subquery approach was incorrect and would not work as intended.
-- We want to count the total number of confirmation requests for each user.


-- Handling users with no confirmations:

-- COALESCE ensures 0 is returned for users with no confirmation requests.
-- NULLIF(COUNT(c.action), 0) prevents division by zero.


-- Calculating confirmed actions:

-- SUM(CASE WHEN c.action = 'confirmed' THEN 1.0 ELSE 0 END) counts confirmed actions.
-- Using 1.0 ensures floating-point division.


-- Removed the extra 1 at the end of the previous query, which was a syntax error.

-- This solution will correctly handle all scenarios:

-- Users with no confirmation requests
-- Users with only confirmed or only timed-out requests
-- Users with a mix of confirmed and timed-out requests

-- The query will return the user_id and their confirmation rate rounded to two decimal places, matching the problem requirements.