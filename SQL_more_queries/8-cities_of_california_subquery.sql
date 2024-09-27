-- Use the database hbtn_0d_usa
USE hbtn_0d_usa;

-- Select cities where the state_id corresponds to California
SELECT * 
FROM cities 
WHERE state_id = (
    SELECT id 
    FROM states 
    WHERE name = 'California'
) 
ORDER BY id ASC;  -- Sort the results by cities.id in ascending order
