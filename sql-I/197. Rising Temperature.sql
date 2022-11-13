SELECT DISTINCT w1.id FROM Weather w1, Weather w2
WHERE w2.temperature < w1.temperature 
AND DATE_ADD(w1.recordDate , INTERVAL -1 DAY) = w2.recordDate ;