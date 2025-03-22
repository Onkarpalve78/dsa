
-- The ROUND() function rounds a number to a specified number of decimal places.

-- Syntax
-- ROUND(number, decimals, operation)

-- SELECT ROUND(23.546,2) as round_value;

-- To solve this problem, I need to calculate the average processing time for each machine. Here's my approach:

-- First, I'll join the Activity table with itself to pair each 'start' activity with its corresponding 'end' activity
-- Then I'll calculate the difference between end and start timestamps
-- Finally, I'll group by machine_id and calculate the average processing time

-- Here's the SQL solution:
-- sql

SELECT 
    a1.machine_id,
    ROUND(AVG(a2.timestamp - a1.timestamp), 3) AS processing_time
FROM 
    Activity a1
JOIN 
    Activity a2 
    ON a1.machine_id = a2.machine_id
    AND a1.process_id = a2.process_id
    AND a1.activity_type = 'start'
    AND a2.activity_type = 'end'
GROUP BY 
    a1.machine_id;


-- This solution works by:

-- Joining the Activity table with itself where:

-- The machine_id and process_id match
-- The first record is a 'start' activity
-- The second record is an 'end' activity


-- Calculating the time difference between end and start timestamps
-- Grouping by machine_id to get the average time per machine
-- Using ROUND() to format the result to 3 decimal places

-- The result will match the expected output in the example, showing the average processing time for each machine.