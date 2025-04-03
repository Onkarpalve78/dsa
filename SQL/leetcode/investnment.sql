-- LC 585 https://leetcode.com/problems/investments-in-2016/description/

-- Medium

-- Table: Insurance

-- +-------------+-------+
-- | Column Name | Type  |
-- +-------------+-------+
-- | pid         | int   |
-- | tiv_2015    | float |
-- | tiv_2016    | float |
-- | lat         | float |
-- | lon         | float |
-- +-------------+-------+
-- pid is the primary key (column with unique values) for this table.
-- Each row of this table contains information about one policy where:
-- pid is the policyholder's policy ID.
-- tiv_2015 is the total investment value in 2015 and tiv_2016 is the total investment value in 2016.
-- lat is the latitude of the policy holder's city. It's guaranteed that lat is not NULL.
-- lon is the longitude of the policy holder's city. It's guaranteed that lon is not NULL.

 

-- Write a solution to report the sum of all total investment values in 2016 tiv_2016, for all policyholders who:

--     have the same tiv_2015 value as one or more other policyholders, and
--     are not located in the same city as any other policyholder (i.e., the (lat, lon) attribute pairs must be unique).

-- Round tiv_2016 to two decimal places.

-- The result format is in the following example.

 

-- Example 1:

-- Input: 
-- Insurance table:
-- +-----+----------+----------+-----+-----+
-- | pid | tiv_2015 | tiv_2016 | lat | lon |
-- +-----+----------+----------+-----+-----+
-- | 1   | 10       | 5        | 10  | 10  |
-- | 2   | 20       | 20       | 20  | 20  |
-- | 3   | 10       | 30       | 20  | 20  |
-- | 4   | 10       | 40       | 40  | 40  |
-- +-----+----------+----------+-----+-----+
-- Output: 
-- +----------+
-- | tiv_2016 |
-- +----------+
-- | 45.00    |
-- +----------+


# Write your MySQL query statement below


select ROUND(SUM(tiv_2016),2) as tiv_2016
from Insurance
where tiv_2015 IN
(select tiv_2015 from Insurance 
group by tiv_2015
having count(tiv_2015)>1 and
concat(lat,lon) not in 
(
    select concat(lat,lon) from Insurance 
    group by lat,lon
    having count(concat(lat,lon))>1
)
)


SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance
WHERE tiv_2015 IN (
    SELECT tiv_2015 
    FROM Insurance 
    GROUP BY tiv_2015 
    HAVING COUNT(*) > 1
)
AND (lat, lon) IN (
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
);
-- The first condition correctly identifies policies where tiv_2015 is shared with other policies
-- The second condition correctly identifies unique locations (lat, lon pairs that appear exactly once)
-- Using (lat, lon) as a composite key is cleaner than concatenating them