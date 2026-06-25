# Write your MySQL query statement below
SELECT DISTINCT author_id AS id 
-- DISTINCT removes duplicate authors.

FROM  Views

WHERE author_id = viewer_id

-- SOrt in assending order 
ORDER BY id;