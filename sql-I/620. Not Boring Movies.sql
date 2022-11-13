SELECT * FROM cinema c 
WHERE id % 2 = 1 AND description NOT LIKE 'boring' AND rating BETWEEN 0 AND 10
ORDER BY rating DESC;